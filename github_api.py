import requests
from config import load_config
from datetime import datetime

config = load_config()
GITHUB_TOKEN = config.get("github_token")


def format_github_date(date_str):
    if not date_str:
        return "Not specified"
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return "Not specified"


def fetch_github_user_data():
    if not GITHUB_TOKEN:
        print("Токен отсутствует! Укажите его в config.yaml файле.")
        return {}

    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    api_url = "https://api.github.com/user"

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        user_data = response.json() or {}
        print("Данные из GitHub API:", user_data)
        return {
            "name": user_data.get("name", "Не указано"),
            "login": user_data.get("login", "Не указано"),
            "email": user_data.get("email", "Не указано"),
            "public_repos": user_data.get("public_repos", "Не указано"),
            "created_at": format_github_date(user_data.get("created_at")),
            "bio": user_data.get("bio", "Не указано"),
            "blog": user_data.get("blog", "Не указано"),
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return {}
