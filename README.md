# user-service

Manages user profile data and updates.

## Why this repo exists

Isolating user data management enables independent scaling and development of user-related features without impacting other services.

## Core Components

### `update_user_profile(user_id: str)`
Updates a user's profile information.

**Logs:**
- `user_profile_updated` — Logged when a profile update completes successfully

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/users/profile` | POST | Updates a user profile |

### Running the service

```bash
uvicorn src.user_service.app:app --host 0.0.0.0 --port 8002
```
