"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from user_service.config import load_config
from user_service.errors import AppError
from user_service.lifecycle import install_signal_handlers
from user_service.observability import init_correlation_id

logger = get_logger("user-service")


def update_user_profile(user_id: str) -> None:
    logger.info("user_profile_updated", user_id=user_id)


def run() -> None:
    cfg = load_config("user-service")
    cid = init_correlation_id()
    install_signal_handlers("user-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        update_user_profile("user-123")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
