import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl

from app.models.project import ProjectStatus


class ProjectBase(BaseModel):
    """Base project schema with common attributes."""

    name: str
    url: HttpUrl
    git_repo: str | None = None


class ProjectCreate(ProjectBase):
    """Schema for creating a new project."""

    pass


class ProjectUpdate(BaseModel):
    """Schema for updating an existing project."""

    name: str | None = None
    url: HttpUrl | None = None
    git_repo: str | None = None
    status: ProjectStatus | None = None


class ProjectResponse(ProjectBase):
    """Schema for returning project data in API responses."""

    id: uuid.UUID
    user_id: uuid.UUID
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
