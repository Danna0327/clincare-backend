# ClinCare Backend

Sistema de Gestión de Citas Médicas desarrollado con **FastAPI**, **SQLAlchemy** y **SQL Server**.

## Tecnologías
- Python
- FastAPI
- SQLAlchemy
- SQL Server
- PyODBC

## Arquitectura
El proyecto sigue una arquitectura por capas basada en principios **SOLID**:

- **Controllers**: exponen endpoints REST
- **Services**: contienen la lógica de negocio
- **Repositories**: gestionan el acceso a datos
- **Models**: representan las entidades de la base de datos
- **Schemas**: validan las entradas y salidas de la API

## Estructura del proyecto
```bash
app/
├── controllers/
├── core/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py