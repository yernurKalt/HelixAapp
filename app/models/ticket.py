from datetime import datetime
import uuid
from sqlalchemy import DateTime, Enum, ForeignKey, Index, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from app.models.enums import TicketPriority, TicketStatus
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Ticket(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "tickets"
    __table_args__ = (
        Index("ix_ticket_list_by_status", "org_id", "status"),
        Index("ix_agent_queue", "org_id", "assigned_to", "status"),
        Index("ix_recent_activity_ordering", "org_id", "latest_activity_at"),
        # Fix: Missing comma was causing broken Index definition.
        Index("ix_priority_filtering", "org_id", "priority"),
    )
    org_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id", ondelete="RESTRICT"),
        nullable=False,
    )
    created_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )
    assigned_to: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[TicketStatus] = mapped_column(Enum(TicketStatus, name="ticket_status"), nullable=False)
    priority: Mapped[TicketPriority] = mapped_column(Enum(TicketPriority, name="ticket_priority"), nullable=False)
    latest_activity_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

