from datetime import datetime, timedelta, timezone

from app import app
from database import Complaint, db


now = datetime.now(timezone.utc)

demo_complaints = [
    # Previous period: 2 complaints
    {
        "complaint_text": "Garbage has not been collected in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=5),
    },
    {
        "complaint_text": "A dead animal is lying near the Ward 12 road.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=4),
    },

    # Recent period: 6 complaints
    {
        "complaint_text": "Garbage is piling up in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=2),
    },
    {
        "complaint_text": "Dead animal reported near the market in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=2),
    },
    {
        "complaint_text": "Waste has not been cleared from Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=1),
    },
    {
        "complaint_text": "Animal carcass found near a residential area in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now - timedelta(days=1),
    },
    {
        "complaint_text": "Garbage collection has stopped in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now,
    },
    {
        "complaint_text": "Waste and sanitation issue reported again in Ward 12.",
        "category": "Sanitation and Public Health",
        "location": "ward 12",
        "created_at": now,
    },
]


with app.app_context():

    for item in demo_complaints:

        complaint = Complaint(
            complaint_text=item["complaint_text"],
            district="Demo District",
            ward="ward 12",
            issue=item["category"],
            category=item["category"],
            department="Municipal / Sanitation Authority",
            location=item["location"],
            duration="Not specified",
            summary=item["complaint_text"],
            status="Submitted",
            created_at=item["created_at"],
            embedding=None,
        )

        db.session.add(complaint)

    db.session.commit()

    print(
        f"Added {len(demo_complaints)} synthetic demo complaints."
    )
    print("These records are for prototype demonstration only.")