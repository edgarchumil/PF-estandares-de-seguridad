# Arquitectura de SGSI-UFVV

## Entorno local real

El prototipo ejecutable usa Nginx como puerta de entrada a React y FastAPI. PostgreSQL y Redis viven en una red interna de Docker Compose. Celery ejecuta tareas de reportes. Esta separación es útil para el laboratorio, pero no implementa VLAN de campus, NGFW, DMZ física, alta disponibilidad ni zero trust de extremo a extremo.

## Arquitectura objetivo

La propuesta educativa combina los servicios académicos y bases de datos del campus con una copia externa cifrada en Azure Blob. El campus inicia carga HTTPS 443 autenticada por Microsoft Entra; el contenedor es privado, con RBAC en alcance de contenedor, TLS mínimo 1.2, bloqueo de Shared Key, cifrado de servicio, versionado y retención lógica. La plantilla de [`infrastructure/azure`](../infrastructure/azure) crea únicamente Storage Account y container. No se ha desplegado; requiere una sesión de Azure del titular y consume crédito de Azure for Students.

Las decisiones, flujos, VLAN de destino y límites de costos están en el [diseño híbrido](sgsi/01-arquitectura-hibrida.md) y el [plan Azure](sgsi/plan-azure.md). El [escenario institucional](sgsi/00-escenario-y-alcance.md) describe UFVV y el alcance propuesto.

## Límites conocidos

- El runtime actual ejecutable es Docker local. No hay infraestructura Azure aplicada ni red híbrida privada.
- El control de acceso de aplicación usa roles y filtros multi organización; MFA TOTP está disponible, no impuesta globalmente.
- La auditoría de la aplicación no equivale a SIEM. MDM, DLP, EDR/XDR, NGFW e IDS/IPS no están conectados al repo.
- La cuenta de Azure y un contenedor sirven para copia externa; no ofrecen una nube de recuperación de cómputo de alta disponibilidad.
- La configuración de producción debe incorporar revisión legal de región, cifrado, retención, costos y permisos antes de datos reales.
