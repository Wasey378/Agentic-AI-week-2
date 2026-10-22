"""Phase 03: make a GET request and process a JSON response."""

import requests


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)
        print(f"HTTP status: {response.status_code}")
        response.raise_for_status()

        post = response.json()
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()
