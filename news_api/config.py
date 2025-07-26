import os
import streamlit as st

NEWS_API_KEY = st.secrets.get("NEWS_API_KEY") or os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("API key not found in secrets or .env file")

NEWS_API_URL = "https://newsapi.org/v2/everything"