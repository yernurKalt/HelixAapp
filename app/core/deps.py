from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.session import get_db


def db_session() -> AsyncSession:
    return Depends(get_db)