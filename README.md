
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
=======
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

