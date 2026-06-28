from database import supabase


# ==========================
# Register User
# ==========================

def register(email: str, password: str):

    """
    Creates a new user account.
    """

    try:

        response = supabase.auth.sign_up({

            "email": email,
            "password": password

        })

        return {
            "success": True,
            "data": response.user
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# Login User
# ==========================

def login(email: str, password: str):

    """
    Logs a user into MALDINI.
    """

    try:

        response = supabase.auth.sign_in_with_password({

            "email": email,
            "password": password

        })

        return {
            "success": True,
            "user": response.user,
            "session": response.session
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# Logout User
# ==========================

def logout():

    """
    Logs out the current user.
    """

    try:

        supabase.auth.sign_out()

        return {
            "success": True
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# Current User
# ==========================

def get_current_user():

    """
    Returns the currently authenticated user.
    """

    try:

        response = supabase.auth.get_user()

        return response.user

    except Exception:

        return None