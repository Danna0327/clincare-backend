# Resumen de diseño de software - ClinCare

## Arquitectura

El sistema utiliza una arquitectura en capas:

- Models
- Schemas
- Repositories
- Services
- Controllers

## Principios SOLID

### SRP
Cada clase tiene una sola responsabilidad.

### OCP
Las reglas pueden extenderse sin modificar código existente.

### LSP
Las capas pueden reemplazarse sin afectar el sistema.

### ISP
Cada módulo mantiene responsabilidades específicas.

### DIP
Los controladores dependen de servicios y repositorios.