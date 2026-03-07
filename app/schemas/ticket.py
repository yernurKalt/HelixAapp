from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import TicketPriority, TicketStatus


class TicketBase(BaseModel):
    subject: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1)
    org_id: uuid.UUID
    created_by: uuid.UUID
    assigned_to: uuid.UUID

class TicketCreate(TicketBase):
    pass


class TicketResponse(TicketBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    status: TicketStatus
    priority: TicketPriority
    latest_activity_at: datetime

    model_config = ConfigDict(from_attributes=True)