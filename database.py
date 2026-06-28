import os

from supabase import create_client, Client

# ==========================
# Configuration
# ==========================

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    raise RuntimeError(
        "SUPABASE_URL is not set."
    )

if not SUPABASE_KEY:
    raise RuntimeError(
        "SUPABASE_KEY is not set."
    )

# ==========================
# Supabase Client
# ==========================

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)