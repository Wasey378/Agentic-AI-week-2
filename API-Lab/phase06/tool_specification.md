# Phase 06: Agent-Oriented Tool Specification

## Tool: `get_post_by_id`

**Purpose:** Retrieve a JSONPlaceholder post using its ID.

**Input:**

| Name | Type | Required | Description |
|---|---|---:|---|
| `post_id` | integer | Yes | ID of the post to retrieve. |

**HTTP method:** `GET`  
**Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`  
**Request body:** None.  
**Authentication:** Not required.

**Output fields:**

| Name | Type | Description |
|---|---|---|
| `id` | integer | ID of the retrieved post. |
| `title` | string | Post title. |
| `body` | string | Post body. |
| `userId` | integer | ID of the user who created the post. |

**Possible errors:** `401` authentication failure (not expected for this
public API), `404` post not found, `429` rate limit exceeded, other HTTP or
request/network failures, invalid response JSON, and timeout.

An agent could use this specification to decide when this operation is
appropriate, supply the required `post_id`, and consume the returned post
fields. This phase defines the tool shape only; it does not implement an agent.
