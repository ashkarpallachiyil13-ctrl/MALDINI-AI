from database import get_connection


# ==========================
# Create Conversation
# ==========================

def create_conversation(title="New Chat"):
    """
    Creates a new conversation.

    Returns:
        int: Conversation ID
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO conversations (title) VALUES (?)",
        (title,)
    )

    conversation_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return conversation_id


# ==========================
# Save Message
# ==========================

def save_message(conversation_id, role, content):
    """
    Saves a message to the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (conversation_id, role, content)
        VALUES (?, ?, ?)
        """,
        (conversation_id, role, content)
    )

    conn.commit()
    conn.close()


# ==========================
# Load Conversation
# ==========================

def load_conversation(conversation_id):
    """
    Returns all messages in OpenAI format.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE conversation_id=?
        ORDER BY id ASC
        """,
        (conversation_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "role": role,
            "content": content
        }
        for role, content in rows
    ]


# ==========================
# Conversation List
# ==========================

def get_conversations():
    """
    Returns every saved conversation.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, created_at
        FROM conversations
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================
# Rename Conversation
# ==========================

def rename_conversation(conversation_id, new_title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE conversations
        SET title=?
        WHERE id=?
        """,
        (new_title, conversation_id)
    )

    conn.commit()
    conn.close()


# ==========================
# Delete Conversation
# ==========================

def delete_conversation(conversation_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM conversations
        WHERE id=?
        """,
        (conversation_id,)
    )

    conn.commit()
    conn.close()