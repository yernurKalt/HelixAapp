from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.health import router as health_router
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME
)

if settings.ENV.lower() == "dev":
    origins = settings.cors_origin_list
    print(origins)

    if origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_haeders=["*"]
        )

app.include_router(health_router)