from typing import List
from fastapi import APIRouter, Depends
from app.core.config import settings
from app.db.session import get_db
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.organization import OrganizationService


router = APIRouter(
    prefix=f"{settings.API_PREFIX}/organizations",
    tags=["organizations"]
)


@router.post("", response_model=OrganizationResponse)
async def create_organization(organization: OrganizationCreate, db: AsyncSession = Depends(get_db)):
    service = OrganizationService(db)
    organization = await service.create_organization(payload=organization)
    return OrganizationResponse.model_validate(organization)

@router.get("", response_model=List[OrganizationResponse])
async def get_organizations(db: AsyncSession = Depends(get_db)):
    service = OrganizationService(db)
    organizations = await service.get_organizations()
    return [OrganizationResponse.model_validate(organization) for organization in organizations]