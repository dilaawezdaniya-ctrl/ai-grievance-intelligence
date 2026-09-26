import json
import math

from database import Complaint


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """Calculate cosine similarity between two embedding vectors."""

    if len(vector_a) != len(vector_b):
        raise ValueError("Embedding dimensions do not match.")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def parse_embedding(embedding_json: str) -> list[float]:
    """Convert stored JSON embedding into a list of floats."""

    values = json.loads(embedding_json)

    if not isinstance(values, list):
        raise ValueError("Stored embedding is not a list.")

    return [float(value) for value in values]


def find_similar_complaints(
    complaint_id: int,
    top_k: int = 5,
    min_similarity: float = 0.75,
) -> list[dict]:
    """
    Find complaints that are semantically similar to the selected complaint.

    0.75 is an initial MVP threshold, not a validated production threshold.
    """

    target = Complaint.query.get(complaint_id)

    if target is None:
        raise ValueError(
            f"Complaint #{complaint_id} was not found."
        )

    if not target.embedding:
        raise ValueError(
            f"Complaint #{complaint_id} does not have an embedding."
        )

    target_vector = parse_embedding(target.embedding)

    complaints = (
        Complaint.query
        .filter(Complaint.embedding.isnot(None))
        .filter(Complaint.id != complaint_id)
        .all()
    )

    results = []

    for complaint in complaints:

        try:
            comparison_vector = parse_embedding(
                complaint.embedding
            )

            similarity = cosine_similarity(
                target_vector,
                comparison_vector,
            )

            if similarity >= min_similarity:

                results.append(
                    {
                        "complaint_id": complaint.id,
                        "complaint_text": complaint.complaint_text,
                        "category": complaint.category,
                        "location": complaint.location,
                        "similarity": similarity,
                        "similarity_percentage": round(
                            similarity * 100,
                            2,
                        ),
                    }
                )

        except (ValueError, TypeError, json.JSONDecodeError):
            # Ignore malformed embeddings instead of breaking the
            # entire similarity search.
            continue

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    return results[:top_k]