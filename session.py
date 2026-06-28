# ==========================
# Active Session
# ==========================

_current_conversation = None


# ==========================
# Set Active Conversation
# ==========================

def set_current_conversation(conversation_id):
    """
    Sets the active conversation.
    """

    global _current_conversation
    _current_conversation = conversation_id


# ==========================
# Get Active Conversation
# ==========================

def get_current_conversation():
    """
    Returns the active conversation ID.
    """

    return _current_conversation


# ==========================
# Check Session
# ==========================

def has_active_conversation():
    """
    Returns True if a conversation is active.
    """

    return _current_conversation is not None


# ==========================
# Reset Session
# ==========================

def reset_session():
    """
    Clears the active conversation.
    """

    global _current_conversation
    _current_conversation = None