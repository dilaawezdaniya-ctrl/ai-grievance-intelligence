from app import app
from database import Complaint, db
from services.similarity_service import (
    cosine_similarity,
    parse_embedding,
)


with app.app_context():

    complaints = (
        Complaint.query
        .filter(Complaint.embedding.isnot(None))
        .order_by(Complaint.id.asc())
        .all()
    )

    print("Complaints with embeddings:", len(complaints))

    if len(complaints) < 2:
        print("Need at least 2 complaints with embeddings.")
        print("Submit another complaint through the website first.")
        raise SystemExit

    first = complaints[0]
    second = complaints[1]

    vector_a = parse_embedding(first.embedding)
    vector_b = parse_embedding(second.embedding)

    similarity = cosine_similarity(vector_a, vector_b)

    print()
    print("COMPLAINT SIMILARITY TEST")
    print("=" * 40)

    print(f"Complaint A #{first.id}:")
    print(first.complaint_text)

    print()

    print(f"Complaint B #{second.id}:")
    print(second.complaint_text)

    print()

    print(
        f"Cosine similarity: {similarity:.4f}"
    )

    print(
        f"Similarity percentage: {similarity * 100:.2f}%"
    )