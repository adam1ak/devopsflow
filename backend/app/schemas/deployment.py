import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.deployment import DeploymentStatus


class DeploymentBase(BaseModel):
    """Base deployment schema."""

    commit_hash: str | None = None


class DeploymentCreate(DeploymentBase):
    """Schema for triggering a new deployment task."""

    project_id: uuid.UUID


class DeploymentResponse(DeploymentBase):
    """Schema for returning deployment details and build logs."""

    id: uuid.UUID
    project_id: uuid.UUID
    status: DeploymentStatus
    logs: str | None = None
    started_at: datetime
    finished_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
