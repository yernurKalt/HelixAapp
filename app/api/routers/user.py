from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService


router = APIRouter(
    prefix=f"{settings.API_PREFIX}/users",
    tags=["users"]
)


@router.post("", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    user = await service.create_user(payload=user)
    return UserResponse.model_validate(user)

@router.get("", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    users = await service.get_users()
    return [UserResponse.model_validate(user) for user in users]