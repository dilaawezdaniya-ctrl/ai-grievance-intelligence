from datetime import datetime, timezone

from app import app
from database import Complaint
from services.emerging_issue_service import detect_emerging_issues


with app.app_context():

    complaints = Complaint.query.all()

    signals = detect_emerging_issues(
        complaints=complaints,
        recent_days=3,
        baseline_days=3,
        min_recent_count=3,
        min_increase_ratio=2.0,
    )

    print()
    print("EMERGING ISSUE DETECTION")
    print("=" * 60)

    if not signals:
        print("No potential emerging issues detected.")
    else:
        for signal in signals:

            print()
            print(
                f"Category: {signal['category']}"
            )

            print(
                f"Location: {signal['location']}"
            )

            print(
                f"Recent complaints: "
                f"{signal['recent_count']}"
            )

            print(
                f"Previous period: "
                f"{signal['previous_count']}"
            )

            if signal["increase_percent"] is not None:
                print(
                    f"Increase: "
                    f"{signal['increase_percent']}%"
                )
            else:
                print(
                    "Increase: New activity detected "
                    "from a zero baseline"
                )

            print(
                f"Status: {signal['status']}"
            )

            print("-" * 60)