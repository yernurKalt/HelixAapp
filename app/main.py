from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.health import router as health_router
from app.api.routers.ticket import router as ticket_router
from app.api.routers.organization import router as organization_router
from app.api.routers.user import router as user_router
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME
)


if settings.ENV.lower() == "dev":
    origins = settings.cors_origin_list
    if origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )

app.include_router(health_router)
app.include_router(ticket_router)
app.include_router(organization_router)
app.include_router(user_router)