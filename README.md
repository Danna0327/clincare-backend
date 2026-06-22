# ClinCare Backend - T02.03

Sistema de Gestión de Citas Médicas desarrollado con FastAPI y SQLAlchemy, siguiendo principios SOLID y arquitectura por capas.

## Tecnologías
- Python 3.11
- FastAPI
- SQLAlchemy
- SQL Server
- Pydantic

## Arquitectura
El proyecto está organizado en capas:
- **Controllers**: exposición de endpoints REST
- **Services**: lógica de negocio
- **Repositories**: acceso a datos
- **Models**: entidades ORM
- **Schemas**: validación y serialización

## Principios SOLID aplicados
- **S**: cada capa tiene una responsabilidad única
- **O**: el sistema puede extenderse agregando nuevos módulos sin modificar la estructura base
- **L**: las clases de servicio/repositorio mantienen contratos consistentes
- **I**: los esquemas y operaciones están separados según el contexto
- **D**: los servicios dependen de abstracciones de persistencia y sesiones inyectadas

## Ejecución
```bash
python -m uvicorn app.main:app --reload