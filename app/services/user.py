from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user_repo = UserRepository(session)


    async def create_user(self, *, payload: UserCreate):
        return await self.user_repo.create(payload=payload)

    async def get_users(self):
        return await self.user_repo.get_all()