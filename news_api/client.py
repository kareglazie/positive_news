import requests
from .config import NEWS_API_KEY, NEWS_API_URL

def fetch_news(query="positive news", language="en", page_size=20):
    params = {
        "apiKey": NEWS_API_KEY,
        "q": f"{query} AND (good OR happy OR positive OR success OR breakthrough)",
        "language": language,
        "pageSize": page_size,
        "sortBy": "publishedAt",
        "searchIn": "title,description,content"
    }
    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("articles", [])