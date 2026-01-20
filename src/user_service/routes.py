"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import UpdateUserProfileRequest, UpdateUserProfileResponse
from .service import update_user_profile

router = APIRouter()


@router.post("/users/profile", response_model=UpdateUserProfileResponse, status_code=200)
def update_user_profile_route(req: UpdateUserProfileRequest) -> UpdateUserProfileResponse:
    result = update_user_profile(
        user_id=req.user_id,
        email=req.email,
        display_name=req.display_name,
        preferences=req.preferences,
    )
    return UpdateUserProfileResponse(
        user_id=result["user_id"],
        updated_fields=result["updated_fields"],
        updated_at=result["updated_at"],
    )
