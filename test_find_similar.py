from app import app
from services.similarity_service import find_similar_complaints


TEST_COMPLAINT_ID = 2


with app.app_context():

    try:
        results = find_similar_complaints(
            complaint_id=TEST_COMPLAINT_ID,
            top_k=5,
            min_similarity=0.75,
        )

        print()
        print("SIMILAR COMPLAINTS")
        print("=" * 50)

        if not results:
            print("No similar complaints found.")
        else:
            for result in results:
                print(
                    f"Complaint #{result['complaint_id']} "
                    f"— {result['similarity_percentage']}%"
                )

                print(
                    f"Text: {result['complaint_text']}"
                )

                print(
                    f"Category: {result['category']}"
                )

                print(
                    f"Location: {result['location']}"
                )

                print("-" * 50)

    except Exception as exc:
        print("Similarity search failed.")
        print(f"{type(exc).__name__}: {exc}")