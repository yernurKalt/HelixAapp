import uuid
from sqlalchemy import Enum, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from app.models.enums import TicketStatus
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class TicketStatusHistory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "ticket_status_histories"
    __table_args__ = (
        Index("ix_ticket_status_histories_ticket_id_created_at", "ticket_id", "created_at"),
        Index("ix_ticket_status_histories_org_id_created_at", "org_id", "created_at")
    )
    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tickets.id", ondelete="CASCADE"),
        nullable=False
    )
    changed_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False
    )
    org_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("organizations.id", ondelete="RESTRICT"),
        nullable=False
    )
    from_status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, name="ticket_status"),
        nullable=False
    )
    to_status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, name="ticket_status"),
        nullable=False
    )