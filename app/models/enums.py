from enum import Enum

from sqlalchemy.dialects import postgresql


class UserRole(str, Enum):
    ADMIN = "admin"
    AGENT = "agent"
    USER = "user"


class TicketStatus(str, Enum):
    OPEN = "open"
    PENDING = "pending"
    RESOLVED = "resolved"
    CLOSED = "closed"


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


ticket_status_enum = postgresql.ENUM(
    "open", "pending", "resolved", "closed",
    name="ticket_status",
    create_type=False,
)