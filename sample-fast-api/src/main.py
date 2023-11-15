import logging.config

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .shared.app_config import AppConfig
from .shared.logging_config import LOGGING_CONFIG
from .healthcheck.routers import healthcheck_router

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=AppConfig.TITLE,
    summary=AppConfig.SUMMARY,
    docs_url=f"{AppConfig.CONTEXT_PATH}/docs",
    redoc_url=f"{AppConfig.CONTEXT_PATH}/redoc",
    openapi_url=f"{AppConfig.CONTEXT_PATH}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization"],
)

app.include_router(healthcheck_router.router, prefix=AppConfig.CONTEXT_PATH)