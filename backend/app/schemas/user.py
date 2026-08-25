import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema with shared attributes."""

    email: EmailStr


class UserCreate(UserBase):
    """Schema for user registration requiring a raw password."""

    password: str = Field(
        min_length=8,
        max_length=128,
        description="Raw password with minimum 8 characters",
    )


class UserUpdate(BaseModel):
    """Schema for updating user details."""

    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8, max_length=128)
    is_active: bool | None = None


class UserResponse(UserBase):
    """Schema for returning user data (strictly excludes password)."""

    id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
