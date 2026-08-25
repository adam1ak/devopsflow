import uuid

from pydantic import BaseModel


class Token(BaseModel):
    """Schema for returning JWT access token upon successful login"""

    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Internal schema representing decoded JWT payload data."""

    sub: uuid.UUID | None = None
