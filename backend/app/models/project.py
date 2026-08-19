import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, DateTime, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from app.core.database import Base


if TYPE_CHECKING:
    from app.models.user import User

class ProjectStatus(str, enum.Enum):
    """Enum representing current health or deployment state of a project."""
    HEALTHY = "HEALTHY"
    UNHEALTHY = "UNHEALTHY"
    DEPLOYING = "DEPLOYING"
    OFFLINE = "OFFLINE"

class Project(Base):
    """Project database model representing a monitored service or repository."""
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    url: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    git_repo: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    status: Mapped[ProjectStatus] = mapped_column(
        SQLEnum(ProjectStatus),
        default=ProjectStatus.HEALTHY,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="projects"
    )