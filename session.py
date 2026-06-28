from database import supabase


# ==========================
# Get Current Session
# ==========================

def get_session():
    """
    Returns the current authenticated session.
    """

    try:

        response = supabase.auth.get_session()

        return response.session

    except Exception:

        return None


# ==========================
# Get Current User
# ==========================

def get_user():
    """
    Returns the currently authenticated user.
    """

    try:

        response = supabase.auth.get_user()

        return response.user

    except Exception:

        return None


# ==========================
# Get User ID
# ==========================

def get_user_id():
    """
    Returns the logged-in user's ID.
    """

    user = get_user()

    if user:

        return user.id

    return None


# ==========================
# Get User Email
# ==========================

def get_user_email():
    """
    Returns the logged-in user's email.
    """

    user = get_user()

    if user:

        return user.email

    return None


# ==========================
# Check Login Status
# ==========================

def is_logged_in():
    """
    Returns True if a user is logged in.
    """

    return get_user() is not None


# ==========================
# Refresh Session
# ==========================

def refresh_session():
    """
    Refreshes the current session.
    """

    try:

        session = get_session()

        if session:

            return supabase.auth.refresh_session(
                session.refresh_token
            )

        return None

    except Exception:

        return None


# ==========================
# Clear Session
# ==========================

def clear_session():
    """
    Logs out the current user.
    """

    try:

        supabase.auth.sign_out()

    except Exception:

        pass