import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HealthCheckBase(BaseModel):
    """Base health check schema."""

    status_code: int | None = None
    response_time_ms: float | None = None
    is_healthy: bool
    error_message: str | None = None


class HealthCheckResponse(HealthCheckBase):
    """Schema for returning monitoring metrics and ping results."""

    id: uuid.UUID
    project_id: uuid.UUID
    checked_at: datetime

    model_config = ConfigDict(from_attributes=True)
