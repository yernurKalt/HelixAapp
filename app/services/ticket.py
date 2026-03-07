from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import db_session
from app.models.ticket import Ticket
from app.models.users import User
from app.repositories.comment import CommentRepository
from app.repositories.ticket import TicketRepository
from app.schemas.ticket import TicketCreate, TicketResponse


class TicketService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.ticket_repo = TicketRepository(self.session)
        self.comment_repo = CommentRepository(session)


    async def create_ticket(self, *, payload: TicketCreate):
        subject = payload.subject.strip()
        description = payload.description.strip()

        if not subject:
            raise ValueError("Subject cannot be empy")
        
        if not description:
            raise ValueError("description cannot be empty")


        ticket = await self.ticket_repo.create(
            org_id=payload.org_id,
            created_by=payload.created_by,
            subject=subject,
            description=description,
        )

        await self.comment_repo.create(
            org_id=payload.org_id,
            ticket_id=ticket.id,
            author_id=payload.created_by,
            body=description,
            is_internal=False,
        )

        return ticket