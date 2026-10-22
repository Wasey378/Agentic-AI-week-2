"""Fetch and display a post from the public JSONPlaceholder API."""

import argparse

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
REQUEST_TIMEOUT_SECONDS = 10


class APIError(Exception):
    """An HTTP or response-format error returned by the API."""


def get_post_by_id(post_id: int) -> dict:
    """Fetch one post and return its parsed JSON object."""
    response = requests.get(
        f"{API_URL}/{post_id}",
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    if response.status_code == 401:
        raise APIError(
            "Authentication failed (HTTP 401). This public API needs no credentials."
        )
    if response.status_code == 404:
        raise APIError(f"Post {post_id} was not found (HTTP 404).")
    if response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        message = "Rate limit exceeded (HTTP 429)."
        if retry_after:
            message += f" Retry after {retry_after}."
        raise APIError(message)

    response.raise_for_status()

    try:
        post = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise APIError("The API returned an invalid JSON response.") from error

    if not isinstance(post, dict):
        raise APIError("The API response was not a JSON object.")

    required_fields = ("id", "title", "body", "userId")
    missing_fields = [field for field in required_fields if field not in post]
    if missing_fields:
        raise APIError(
            "The API response is missing required fields: "
            + ", ".join(missing_fields)
        )

    return post


def positive_integer(value: str) -> int:
    """Parse a positive integer for the command-line post ID."""
    try:
        post_id = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("post_id must be an integer") from error
    if post_id < 1:
        raise argparse.ArgumentTypeError("post_id must be greater than zero")
    return post_id


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a post from the JSONPlaceholder API."
    )
    parser.add_argument(
        "post_id",
        type=positive_integer,
        help="ID of the post to retrieve (for example, 1)",
    )
    args = parser.parse_args()

    try:
        post = get_post_by_id(args.post_id)
    except requests.exceptions.Timeout:
        print(f"Request timed out after {REQUEST_TIMEOUT_SECONDS} seconds.")
        return 1
    except requests.exceptions.ConnectionError as error:
        print(f"Could not connect to the API: {error}")
        return 1
    except requests.exceptions.HTTPError as error:
        print(f"API returned an unsuccessful HTTP status: {error}")
        return 1
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")
        return 1
    except APIError as error:
        print(f"API error: {error}")
        return 1

    print(f"Post ID: {post['id']}")
    print(f"User ID: {post['userId']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
