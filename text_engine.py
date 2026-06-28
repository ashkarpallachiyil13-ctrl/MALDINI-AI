import os
import traceback
from openai import OpenAI

# ==========================
# Configuration
# ==========================

MODEL = "nvidia/nemotron-nano-9b-v2:free"

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set."
    )

# ==========================
# OpenRouter Client
# ==========================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

# ==========================
# Streaming Text Generation
# ==========================

def stream_text(messages):

    """
    Streams text from the NVIDIA Nemotron model.

    Args:
        messages (list):
            OpenAI-format message list.

    Yields:
        str:
            Response chunks.
    """

    try:

        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=True,

            extra_headers={
                "HTTP-Referer": "https://your-site.com",
                "X-OpenRouter-Title": "M.A.L.D.I.N.I"
            }
        )

        for chunk in stream:

            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if delta is None:
                continue

            content = getattr(delta, "content", None)

            if content:
                yield content

    except Exception:

        traceback.print_exc()

        yield "Sorry, the text engine encountered an error."


# ==========================
# Normal Text Generation
# ==========================

def generate_text(messages):

    """
    Returns a complete response.
    Useful for future APIs that don't stream.
    """

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        return response.choices[0].message.content

    except Exception:

        traceback.print_exc()

        return "Sorry, the text engine encountered an error."