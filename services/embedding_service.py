import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing from the .env file."
    )

client = genai.Client(api_key=API_KEY)


def get_embedding(text: str) -> list[float]:
    """
    Generate a semantic embedding for a grievance.

    Gemini embedding-2 does not use the task_type parameter.
    We instead include the task instruction in the text.
    """

    text = text.strip()

    if not text:
        raise ValueError("Text cannot be empty.")

    embedding_input = (
        "task: semantic similarity | "
        "Represent this grievance for finding other grievances "
        "with similar meaning.\n\n"
        f"grievance: {text}"
    )

    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=embedding_input,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        ),
    )

    if not result.embeddings:
        raise RuntimeError("Gemini returned no embedding.")

    values = result.embeddings[0].values

    if not values:
        raise RuntimeError("Gemini returned an empty embedding.")

    return list(values)