"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class UpdateUserProfileRequest(BaseModel):
    user_id: str
    email: Optional[str] = None
    display_name: Optional[str] = None
    preferences: Dict = Field(default_factory=dict)


class UpdateUserProfileResponse(BaseModel):
    user_id: str
    updated_fields: List[str]
    updated_at: datetime
