import os
import streamlit as st

# Streamlit Cloud uses st.secrets
if hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets:
    secrets = st.secrets
else:
    # Local development: load from .env
    from dotenv import load_dotenv
    load_dotenv()
    secrets = os.environ

DB_CONFIG = {
    "host": secrets.get("DB_HOST"),
    "database": secrets.get("DB_NAME"),
    "user": secrets.get("DB_USER"),
    "password": secrets.get("DB_PASSWORD"),
    "port": int(secrets.get("DB_PORT", 5432))
}

OPENAI_API_KEY = secrets.get("OPENAI_API_KEY")
