# Final Project: JSONPlaceholder Post Client

This command-line application demonstrates API communication, JSON processing,
and HTTP/network error handling by retrieving a post from JSONPlaceholder. It
does not build or run an AI agent.

## Setup

From the `final_project` folder, create and activate a virtual environment,
then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python .\src\main.py 1
```

Pass a positive post ID as the argument. The app prints the post ID, user ID,
title, and body.

## API operation

- **API:** JSONPlaceholder
- **HTTP method:** `GET`
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required parameter:** `post_id`, a positive integer in the URL path.
- **Optional parameters:** None.
- **Request body:** None.
- **Authentication:** Not required; no credentials are used.

The response is a JSON object containing `userId`, `id`, `title`, and `body`.

## Error handling

The client handles 401 authentication failures (unexpected for this public
endpoint), 404 not found, 429 rate limiting (including `Retry-After` where
provided), other unsuccessful HTTP statuses, timeouts, connection/request
failures, and malformed or incomplete JSON responses.

## Future agent-tool representation

The operation can later be exposed as a tool with a name (`get_post_by_id`), a
description, a required integer input (`post_id`), the GET endpoint, its output
fields, and possible errors. An agent could select that tool and supply an ID;
the tool would call this API operation and return the post data. The current
application is a direct API client, not an AI agent.

See [the Phase 06 tool specification](../phase06/tool_specification.md) and
[the Phase 05 API client](../phase05/api_client.py).
