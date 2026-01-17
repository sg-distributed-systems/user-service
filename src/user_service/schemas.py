from pydantic import BaseModel


class UpdateUserProfileRequest(BaseModel):
    user_id: str


class UpdateUserProfileResponse(BaseModel):
    status: str
