from core_logger import get_logger

logger = get_logger("user-service")


def update_user_profile(user_id: str) -> None:
    logger.info("user_profile_updated", user_id=user_id)


if __name__ == "__main__":
    update_user_profile("user-123")
