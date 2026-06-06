import os
import logging
from google import genai

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Try models in order — if one fails, fallback to next
MODELS = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash",
    "gemini-flash-latest",
]


def summarize_url(url: str) -> str:
    """
    Use Google Gemini AI to generate a one-line summary of what a URL is about.
    Tries multiple models in order — falls back automatically if one is unavailable.
    Returns None if all models fail or API key is not set.
    """
    if not GEMINI_API_KEY:
        logger.warning("GEMINI_API_KEY not set. Skipping AI summary.")
        return None

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = (
        f"In exactly one short sentence (max 15 words), describe what this URL is about. "
        f"Be specific and informative. Do not include the URL itself in your answer.\n\n"
        f"URL: {url}"
    )

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            summary = response.text.strip().strip('"').strip("'")
            logger.info(f"AI summary generated using {model}: {summary}")
            return summary

        except Exception as e:
            logger.warning(f"Model {model} failed: {type(e).__name__}: {e}. Trying next...")
            continue

    logger.error("All Gemini models failed. Returning None.")
    return None
