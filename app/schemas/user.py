from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import UserRole


class UserBase(BaseModel):
    email: str = Field(min_length=1, max_length=255)
    password: str = Field(min_length=1)
    role: UserRole = Field(default=UserRole.USER)
    org_id: uuid.UUID


class UserCreate(UserBase):
    pass


class UserResponse(BaseModel):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    is_active: bool
    email: str = Field(min_length=1, max_length=255)
    role: UserRole = Field(default=UserRole.USER)
    org_id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)