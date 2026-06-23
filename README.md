# ClinCare Backend - T02.03

Sistema de Gestión de Citas Médicas desarrollado con FastAPI y SQLAlchemy, siguiendo principios SOLID y arquitectura por capas.

## Descripción

ClinCare es una aplicación backend desarrollada con FastAPI para la gestión de citas médicas. El sistema permite administrar usuarios, colaboradores, pacientes y citas médicas mediante una API REST documentada con Swagger.

## Integrantes

* Karen Ushca
* Danna Montece

## Tecnologías

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- SQL Server / SQLite
- PyODBC
- Swagger / OpenAPI

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

## Estructura del Proyecto

```text
app/
├── controllers/
├── services/
├── repositories/
├── schemas/
├── models/
└── core/
    ├── config.py (configuración multi-BD)
    ├── database.py (sesiones SQLAlchemy)
    └── security.py

database/
├── clincare.db (SQLite desarrollo)
└── clincare_sqlserver.sql (SQL Server esquema)

docs/
requirements.txt
.env
```

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

## Principios SOLID Aplicados

- **S**: cada capa tiene una responsabilidad única
- **O**: el sistema puede extenderse agregando nuevos módulos sin modificar la estructura base
- **L**: las clases de servicio/repositorio mantienen contratos consistentes
- **I**: los esquemas y operaciones están separados según el contexto
- **D**: los servicios dependen de abstracciones de persistencia y sesiones inyectadas

## Ejecución

### Instalación de dependencias:

```bash
pip install -r requirements.txt
```

### Configuración de BD

El proyecto soporta dos tipos de bases de datos:

**SQLite (Desarrollo - Default):**
```
DB_TYPE=sqlite
```

**SQL Server (Producción):**
```
DB_TYPE=sqlserver
DB_SERVER=servidor
DB_PORT=1433
DB_NAME=clincare_db
DB_TRUSTED_CONNECTION=yes
```

### Ejecutar aplicación:

```bash
python -m uvicorn app.main:app --reload
```

### Documentación Swagger:

```text
http://localhost:8000/docs
```

### Documentación ReDoc:

```text
http://localhost:8000/redoc
```

