from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.organization import OrganizationRepository
from app.schemas.organization import OrganizationCreate, OrganizationResponse


class OrganizationService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.organization_repo = OrganizationRepository(session)


    async def create_organization(self, *, payload: OrganizationCreate):
        if not payload.name:
            raise ValueError("Name cannot be empty")
        
        if not payload.plan:
            raise ValueError("Plan cannot be empty")
        organization = await self.organization_repo.create(payload=payload)
        return organization

    
    async def get_organizations(self):
        return await self.organization_repo.get_all()
        