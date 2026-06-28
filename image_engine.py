import os
import json
import requests

# ==========================
# Configuration
# ==========================

MODEL = "bytedance-seed/seedream-4.5"

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set."
    )

API_URL = "https://openrouter.ai/api/v1/images"

# ==========================
# Image Generation
# ==========================

def generate_image(prompt: str):

    """
    Generates an image using Seedream.

    Args:
        prompt (str):
            Image prompt.

    Returns:
        dict:
            OpenRouter response.
    """

    try:

        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",

                # Optional
                "HTTP-Referer": "https://your-site.com",
                "X-OpenRouter-Title": "M.A.L.D.I.N.I"
            },
            data=json.dumps({
                "model": MODEL,
                "prompt": prompt
            })
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }