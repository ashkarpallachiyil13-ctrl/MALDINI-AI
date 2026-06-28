from database import supabase


# ==========================
# Create Conversation
# ==========================

def create_conversation(user_id, title="New Chat"):

    response = (
        supabase
        .table("conversations")
        .insert({
            "user_id": user_id,
            "title": title
        })
        .execute()
    )

    return response.data[0]["id"]


# ==========================
# Save Message
# ==========================

def save_message(conversation_id, role, content):

    (
        supabase
        .table("messages")
        .insert({
            "conversation_id": conversation_id,
            "role": role,
            "content": content
        })
        .execute()
    )


# ==========================
# Load Conversation
# ==========================

def load_conversation(conversation_id):

    response = (
        supabase
        .table("messages")
        .select("role, content")
        .eq("conversation_id", conversation_id)
        .order("created_at")
        .execute()
    )

    return response.data


# ==========================
# Get All Conversations
# ==========================

def get_conversations(user_id):

    response = (
        supabase
        .table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return response.data


# ==========================
# Rename Conversation
# ==========================

def rename_conversation(conversation_id, new_title):

    (
        supabase
        .table("conversations")
        .update({
            "title": new_title
        })
        .eq("id", conversation_id)
        .execute()
    )


# ==========================
# Delete Conversation
# ==========================

def delete_conversation(conversation_id):

    (
        supabase
        .table("conversations")
        .delete()
        .eq("id", conversation_id)
        .execute()
    )