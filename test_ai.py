from services.ai_service import analyze_complaint


complaint = "Hamare ward 12 mein 5 din se paani nahi aa raha."

try:
    result = analyze_complaint(complaint)

    print("\nAI ANALYSIS")
    print("=" * 40)

    for key, value in result.items():
        print(f"{key}: {value}")

except Exception as exc:
    print("\nAI TEST FAILED")
    print("=" * 40)
    print(f"{type(exc).__name__}: {exc}")