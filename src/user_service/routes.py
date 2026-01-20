"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import update_user_profile
from .schemas import UpdateUserProfileRequest, UpdateUserProfileResponse

router = APIRouter()


@router.post("/users/profile", response_model=UpdateUserProfileResponse)
def update_user_profile_route(req: UpdateUserProfileRequest) -> UpdateUserProfileResponse:
    update_user_profile(req.user_id)
    return UpdateUserProfileResponse(status="ok")
