from services.embedding_service import get_embedding


text = "Hamare ward 12 mein 5 din se paani nahi aa raha."


try:
    embedding = get_embedding(text)

    print("Embedding generated successfully.")
    print("Dimensions:", len(embedding))
    print("First 5 values:", embedding[:5])

except Exception as exc:
    print("Embedding test failed.")
    print(f"{type(exc).__name__}: {exc}")