import json

from database import Complaint
from services.similarity_service import cosine_similarity


CLUSTER_SIMILARITY_THRESHOLD = 0.90


def parse_embedding(embedding_json: str) -> list[float]:
    """Convert stored JSON embedding into a list of floats."""
    values = json.loads(embedding_json)

    if not isinstance(values, list):
        raise ValueError("Stored embedding is not a list.")

    return [float(value) for value in values]


def build_clusters(
    min_similarity: float = CLUSTER_SIMILARITY_THRESHOLD,
) -> list[dict]:
    """
    Build simple semantic complaint clusters.

    This is an MVP clustering approach based on embedding similarity.
    The 0.90 threshold is an initial prototype threshold and has not
    been validated for production use.
    """

    complaints = (
        Complaint.query
        .filter(Complaint.embedding.isnot(None))
        .order_by(Complaint.id.asc())
        .all()
    )

    clusters = []

    for complaint in complaints:

        try:
            complaint_vector = parse_embedding(
                complaint.embedding
            )
        except (ValueError, TypeError, json.JSONDecodeError):
            continue

        matching_cluster = None

        for cluster in clusters:

            representative = cluster["representative"]

            similarity = cosine_similarity(
                complaint_vector,
                representative["embedding"],
            )

            if similarity >= min_similarity:
                matching_cluster = cluster
                break

        if matching_cluster is None:

            clusters.append(
                {
                    "cluster_id": len(clusters) + 1,
                    "representative": {
                        "complaint_id": complaint.id,
                        "embedding": complaint_vector,
                    },
                    "complaints": [complaint],
                }
            )

        else:
            matching_cluster["complaints"].append(
                complaint
            )

    results = []

    for cluster in clusters:

        complaints_in_cluster = cluster["complaints"]

        categories = [
            c.category
            for c in complaints_in_cluster
            if c.category
        ]

        locations = [
            c.location
            for c in complaints_in_cluster
            if c.location
        ]

        category = (
            max(set(categories), key=categories.count)
            if categories
            else "Uncategorized"
        )

        location = (
            max(set(locations), key=locations.count)
            if locations
            else "Multiple / Not specified"
        )

        results.append(
            {
                "cluster_id": cluster["cluster_id"],
                "complaint_count": len(
                    complaints_in_cluster
                ),
                "category": category,
                "location": location,
                "complaints": complaints_in_cluster,
            }
        )

    results.sort(
        key=lambda cluster: cluster["complaint_count"],
        reverse=True,
    )

    return results