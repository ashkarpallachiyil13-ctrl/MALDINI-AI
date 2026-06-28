from prompts import SYSTEM_PROMPT

from session import (
    has_active_conversation,
    get_current_conversation,
    set_current_conversation
)

from memory import (
    create_conversation,
    load_conversation,
    save_message
)

from text_engine import stream_text


# ==========================
# Main Engine
# ==========================

def chat(user_message):

    """
    Main AI engine.

    Creates a conversation if needed,
    loads history,
    saves messages,
    streams the AI response.
    """

    # ----------------------
    # Create conversation
    # ----------------------

    if not has_active_conversation():

        conversation_id = create_conversation()

        set_current_conversation(
            conversation_id
        )

    else:

        conversation_id = get_current_conversation()

    # ----------------------
    # Load memory
    # ----------------------

    history = load_conversation(
        conversation_id
    )

    # ----------------------
    # Save user message
    # ----------------------

    save_message(
        conversation_id,
        "user",
        user_message
    )

    # ----------------------
    # Build messages
    # ----------------------

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    messages.extend(history)

    messages.append({

        "role": "user",
        "content": user_message

    })

    # ----------------------
    # Stream AI
    # ----------------------

    full_reply = ""

    for chunk in stream_text(messages):

        full_reply += chunk

        yield chunk

    # ----------------------
    # Save AI reply
    # ----------------------

    save_message(

        conversation_id,

        "assistant",

        full_reply

    )