"""
User profile and account management logic.

Handles user data retrieval, profile updates, and preference management.
Validates user input and tracks profile modification history.
"""
from datetime import datetime
from typing import Optional

from core_logger import get_logger

from .errors import NotFoundError, ValidationError

logger = get_logger("user-service")

USERS = {
    "user-001": {"email": "alice@example.com", "display_name": "Alice", "preferences": {}},
    "user-002": {
        "email": "bob@example.com",
        "display_name": "Bob",
        "preferences": {"theme": "dark"},
    },
}


def get_user(user_id: str) -> dict:
    logger.debug("user_lookup", user_id=user_id)
    user = USERS.get(user_id)
    if not user:
        raise NotFoundError("user_not_found", details={"user_id": user_id})
    return {"user_id": user_id, **user}


def update_user_profile(
    user_id: str,
    email: Optional[str],
    display_name: Optional[str],
    preferences: dict,
) -> dict:
    logger.info("profile_update_started", user_id=user_id)

    user = USERS.get(user_id)
    if not user:
        raise NotFoundError("user_not_found", details={"user_id": user_id})

    updated_fields = []

    if email is not None:
        if "@" not in email:
            raise ValidationError("invalid_email_format")
        logger.debug("email_updated", user_id=user_id)
        updated_fields.append("email")

    if display_name is not None:
        if len(display_name) < 2:
            raise ValidationError("display_name_too_short")
        logger.debug("display_name_updated", user_id=user_id)
        updated_fields.append("display_name")

    if preferences:
        logger.debug("preferences_updated", user_id=user_id, keys=list(preferences.keys()))
        updated_fields.append("preferences")

    logger.info("profile_updated", user_id=user_id, updated_fields=updated_fields)
    return {
        "user_id": user_id,
        "updated_fields": updated_fields,
        "updated_at": datetime.utcnow(),
    }
