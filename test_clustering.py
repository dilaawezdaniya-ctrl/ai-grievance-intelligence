from app import app
from services.cluster_service import build_clusters


with app.app_context():

    clusters = build_clusters(
        min_similarity=0.90
    )

    print()
    print("COMPLAINT CLUSTERS")
    print("=" * 60)

    if not clusters:
        print("No clusters found.")
        raise SystemExit

    for cluster in clusters:

        print()
        print(
            f"Cluster #{cluster['cluster_id']}"
        )

        print(
            f"Complaints: "
            f"{cluster['complaint_count']}"
        )

        print(
            f"Category: "
            f"{cluster['category']}"
        )

        print(
            f"Location: "
            f"{cluster['location']}"
        )

        print("-" * 60)

        for complaint in cluster["complaints"]:
            print(
                f"#{complaint.id}: "
                f"{complaint.complaint_text}"
            )
            