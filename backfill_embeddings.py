from app import app
from database import Complaint, db
from services.embedding_service import get_embedding

import json


with app.app_context():

    complaints = (
        Complaint.query
        .filter(
            (Complaint.embedding.is_(None)) |
            (Complaint.embedding == "")
        )
        .all()
    )

    print("Complaints needing embeddings:", len(complaints))

    for complaint in complaints:

        print(f"Generating embedding for Complaint #{complaint.id}...")

        embedding = get_embedding(complaint.complaint_text)

        complaint.embedding = json.dumps(embedding)

        db.session.commit()

        print(
            f"Embedding saved for Complaint #{complaint.id}"
        )

    print()
    print("Backfill complete.")