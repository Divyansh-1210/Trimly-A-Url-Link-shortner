import os
import logging
from google import genai

logger = logging.getLogger(__name__)

# Configure Gemini with API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")


def summarize_url(url: str) -> str:
    """
    Use Google Gemini AI to generate a one-line summary of what a URL is about.
    Returns None if AI is unavailable or API key is not set.
    """
    if not GEMINI_API_KEY:
        logger.warning("GEMINI_API_KEY not set. Skipping AI summary.")
        return None

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        prompt = (
            f"In exactly one short sentence (max 15 words), describe what this URL is about. "
            f"Be specific and informative. Do not include the URL itself in your answer.\n\n"
            f"URL: {url}"
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        summary = response.text.strip().strip('"').strip("'")
        logger.info(f"AI summary generated for {url}: {summary}")
        return summary

    except Exception as e:
        logger.error(f"Gemini AI summarization failed: {type(e).__name__}: {e}")
        return None
