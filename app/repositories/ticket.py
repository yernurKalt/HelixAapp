from datetime import datetime, timezone
from sqlalchemy import select
from app.models.enums import TicketPriority, TicketStatus
from app.models.ticket import Ticket
from app.repositories.base import BaseRepository


class TicketRepository(BaseRepository):
    async def get_by_id(self, ticket_id, org_id):
        stmt = select(Ticket).where(
            Ticket.id == ticket_id,
            Ticket.org_id == org_id
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(
        self,
        *,
        org_id,
        created_by,
        subject: str,
        description: str,
        priority: TicketPriority = TicketPriority.MEDIUM
        ) -> Ticket:
        ticket = Ticket(
            org_id=org_id,
            created_by=created_by,
            assigned_to=None,
            subject=subject,
            description=description,
            status=TicketStatus.OPEN,
            priority=priority,
            latest_activity_at=datetime.now(timezone.utc)
        )
        self.session.add(ticket)
        await self.session.flush()
        await self.session.refresh(ticket)
        return ticket
    
    async def get_by_id(self, *, ticket_id, org_id) -> Ticket | None:
        stmt = select(Ticket).where(
            Ticket.id == ticket_id,
            Ticket.org_id == org_id,
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()