from fastapi import FastAPI

from app.controllers.paciente_controller import router as paciente_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.cita_controller import router as cita_router

app = FastAPI(title="ClinCare API")

app.include_router(paciente_router)
app.include_router(colaborador_router)
app.include_router(cita_router)