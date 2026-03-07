from datetime import datetime
import uuid
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db
from app.models.enums import UserRole
from app.models.users import User
from pwdlib import PasswordHash


def db_session() -> AsyncSession:
    return Depends(get_db)

pwd_context = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


TEMP_USER_ID = uuid.UUID("11111111-1111-1111-1111-111111111111")
user = User(
    id=TEMP_USER_ID,
    created_at=datetime.now(),
    updated_at=datetime.now(),
    org_id=uuid.uuid4(),
    email="the_kalfa@mail.ru",
    password_hash="123123123",
    role=UserRole.USER,
    is_active=True
)

async def get_current_user(db: AsyncSession = Depends(get_db)) -> User:
    """stmt = select(User).where(User.id == TEMP_USER_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Temporary current user not found. Seed this user in DB first.",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is inactive.",
        )
"""
    return user