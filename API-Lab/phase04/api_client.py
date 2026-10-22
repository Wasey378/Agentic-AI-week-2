"""Phase 04: read API configuration from the environment."""

import os

import requests
from dotenv import load_dotenv

DEFAULT_POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
REQUEST_TIMEOUT_SECONDS = 10


def main() -> None:
    load_dotenv()
    posts_url = os.getenv("JSONPLACEHOLDER_POSTS_URL", DEFAULT_POSTS_URL).rstrip("/")

    try:
        response = requests.get(
            f"{posts_url}/1",
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        post = response.json()
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    except requests.exceptions.Timeout:
        print(f"Request timed out after {REQUEST_TIMEOUT_SECONDS} seconds.")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()
