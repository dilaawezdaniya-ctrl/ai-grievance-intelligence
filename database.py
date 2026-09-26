from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Complaint(db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)

    complaint_text = db.Column(db.Text, nullable=False)

    district = db.Column(db.String(100))
    ward = db.Column(db.String(100))

    issue = db.Column(db.String(255))
    category = db.Column(db.String(255))
    department = db.Column(db.String(255))
    location = db.Column(db.String(255))
    duration = db.Column(db.String(100))
    summary = db.Column(db.Text)

    # Stores the semantic embedding of the complaint.
    embedding = db.Column(db.Text)

    status = db.Column(
        db.String(50),
        nullable=False,
        default="Submitted"
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )