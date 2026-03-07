from sqlalchemy import select
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate
from app.repositories.base import BaseRepository


class OrganizationRepository(BaseRepository):
    async def create(self, *, payload: OrganizationCreate):
        organization = Organization(
            name=payload.name,
            plan=payload.plan
        )
        self.session.add(organization)
        await self.session.flush()
        await self.session.refresh(organization)
        return organization

    async def get_all(self):
        stmt = select(Organization)
        result = await self.session.execute(stmt)
        return result.scalars().all()