import json
import os
import time
from typing import Any

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Please add it to the .env file."
    )

client = genai.Client(api_key=API_KEY)


class ComplaintAnalysis(BaseModel):
    issue: str = Field(
        description="The main problem described by the citizen."
    )

    category: str = Field(
        description="The most appropriate public-service category."
    )

    department: str = Field(
        description="Suggested responsible department or authority."
    )

    location: str = Field(
        description="Location explicitly mentioned in the complaint."
    )

    duration: str = Field(
        description="How long the problem has existed."
    )

    summary: str = Field(
        description="A short factual summary of the complaint."
    )


PROMPT_TEMPLATE = """
You are an AI assistant for a public-service grievance system.

Analyze the citizen's complaint and extract structured information.

Rules:
1. Do not invent facts.
2. Use only information supported by the complaint.
3. If location is unavailable, return "Not specified".
4. If duration is unavailable, return "Not specified".
5. Department is only a suggestion, not a final government decision.
6. Keep the summary concise and factual.
7. The citizen may write in Hindi, English, or Hinglish.
8. Return the extracted information in clear English.

Citizen complaint:

{complaint}
"""


def _request_analysis(model: str, complaint: str) -> ComplaintAnalysis:
    response = client.models.generate_content(
        model=model,
        contents=PROMPT_TEMPLATE.format(complaint=complaint),
        config={
            "response_mime_type": "application/json",
            "response_schema": ComplaintAnalysis,
        },
    )

    if response.parsed is not None:
        if isinstance(response.parsed, ComplaintAnalysis):
            return response.parsed

        if hasattr(response.parsed, "model_dump"):
            return ComplaintAnalysis.model_validate(
                response.parsed.model_dump()
            )

        if isinstance(response.parsed, dict):
            return ComplaintAnalysis.model_validate(response.parsed)

    if response.text:
        data = json.loads(response.text)
        return ComplaintAnalysis.model_validate(data)

    raise RuntimeError("Gemini returned an empty response.")


def analyze_complaint(complaint: str) -> dict[str, Any]:
    complaint = complaint.strip()

    if not complaint:
        raise ValueError("Complaint cannot be empty.")

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
    ]

    last_error = None

    for model in models:
        for attempt in range(3):
            try:
                result = _request_analysis(model, complaint)

                print(f"AI analysis completed using {model}")

                return result.model_dump()

            except Exception as exc:
                last_error = exc

                error_text = str(exc)

                # Retry temporary server/rate-limit failures.
                if "503" in error_text or "UNAVAILABLE" in error_text:
                    wait_seconds = 2 ** attempt
                    time.sleep(wait_seconds)
                    continue

                # Try next model for other model-specific failures.
                break

    raise RuntimeError(
        f"AI analysis failed after retries. Last error: {last_error}"
    )