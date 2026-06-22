

# ClinCare – Sistema de Gestión de Citas Médicas

## Descripción

ClinCare es una aplicación backend desarrollada con FastAPI para la gestión de citas médicas. El sistema permite administrar usuarios, colaboradores, pacientes y citas médicas mediante una API REST documentada con Swagger.

---

## Integrantes

* Karen Ushca
* Danna Montece

---

## Tecnologías utilizadas

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQL Server
* PyODBC
* Swagger / OpenAPI

---

## Arquitectura

El proyecto implementa una arquitectura en capas basada en principios SOLID:

### Models

Representan las entidades de la base de datos.

### Schemas

Validan los datos de entrada y salida utilizando Pydantic.

### Repositories

Gestionan el acceso a los datos.

### Services

Contienen la lógica de negocio y validaciones.

### Controllers

Exponen los endpoints REST mediante FastAPI.

---

## Estructura del Proyecto

```text
app/
├── controllers/
├── services/
├── repositories/
├── schemas/
├── models/
└── core/

database/
docs/
README.md
```

---

## Funcionalidades Implementadas

### Autenticación

* Inicio de sesión de usuarios.
* Generación de token de acceso.

### Gestión de Colaboradores

* Registrar colaboradores.
* Consultar colaboradores.
* Actualizar colaboradores.
* Eliminar colaboradores.

### Gestión de Pacientes

* Registrar pacientes.
* Consultar pacientes.
* Actualizar pacientes.
* Eliminar pacientes.

### Gestión de Citas

* Registrar citas médicas.
* Consultar citas.
* Actualizar citas.
* Cancelar citas.

---


## Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar aplicación:

```bash
uvicorn app.main:app --reload
```

Documentación Swagger:

```text
http://localhost:8000/docs
```

# ClinCare Backend

# ClinCare Backend - T02.03
>>>>>>> ea48053 (Integrar backend ClinCare T02.03 con routers, versionado API y documentación Swagger)

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

app/
├── controllers/
├── core/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py


python -m uvicorn app.main:app --reload
