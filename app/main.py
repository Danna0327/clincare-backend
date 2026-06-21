from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)


@app.get("/", tags=["Health Check"])
def root():
    return {
        "message": "ClinCare API funcionando correctamente",
        "version": settings.APP_VERSION
    }


@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }