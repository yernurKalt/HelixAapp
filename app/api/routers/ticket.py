from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.users import User
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services.ticket import TicketService


router = APIRouter(
    prefix="/ticket",
    tags=["tickets"]
)

@router.post("", response_model=TicketResponse)
async def create_ticket(payload: TicketCreate, db: AsyncSession = Depends(get_db)):
    service = TicketService(db)

    try:
        ticket = await service.create_ticket(payload=payload)
        return TicketResponse.model_validate(ticket)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    


@router.get("")
async def get_ticket():
    pass