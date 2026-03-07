from sqlalchemy import select
from app.core.deps import get_password_hash
from app.models.users import User
from app.repositories.base import BaseRepository
from app.schemas.user import UserCreate


class UserRepository(BaseRepository):
    async def create(self, *, payload: UserCreate):
        user = User(
            email=payload.email,
            password_hash=get_password_hash(payload.password),
            role=payload.role,
            org_id=payload.org_id,
            is_active=True
        )
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def get_all(self):
        stmt = select(User)
        result = await self.session.execute(stmt)
        return result.scalars().all()