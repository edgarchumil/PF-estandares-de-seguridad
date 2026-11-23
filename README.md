# SGSI-UFVV

**Proyecto académico:** Diseño e implementación demostrable del Sistema de Gestión de Seguridad de la Información de la Universidad Ficticia del Valle Verde (UFVV).

UFVV es una organización universitaria ficticia en Guatemala. Los nombres, población, procesos, activos, impactos, riesgos y tiempos son supuestos académicos, no una organización ni auditoría real. El sistema usa una aplicación local de gestión de activos, NIST CSF, riesgos, incidentes y auditoría; el paquete completo de diseño y entregables está en [`docs/sgsi`](docs/sgsi/README.md).

## Arranque local

Requisitos: Docker Desktop con Compose v2.

```powershell
Copy-Item .env.example .env
# En .env: cambie SECRET_KEY, POSTGRES_PASSWORD y DEMO_PASSWORD.
docker compose up --build -d
docker compose run --rm api alembic upgrade head
docker compose run --rm api python -m app.seed
```

- Aplicación: <http://localhost:8080>
- OpenAPI: <http://localhost:8080/docs>
- Liveness: <http://localhost:8080/api/v1/health/live>
- Readiness: <http://localhost:8080/api/v1/health/ready>
- Acceso demo: `administrador@demo.local`, con el valor local de `DEMO_PASSWORD`.

En una base persistente heredada, la carga educativa agrega el tenant UFVV y no borra el tenant anterior. Seleccione **Universidad Ficticia del Valle Verde (UFVV)** en el selector. No ejecute `docker compose down -v` si desea conservar la información local.

Detener: `docker compose down`. PostgreSQL, Redis y respaldos se mantienen en volúmenes locales.

## Entregables SGSI

- [Informe académico final](docs/sgsi/informe-final.md) y [presentación de 10 diapositivas](docs/sgsi/presentacion.md)
- [Escenario y alcance](docs/sgsi/00-escenario-y-alcance.md)
- [Arquitectura híbrida](docs/sgsi/01-arquitectura-hibrida.md)
- [Inventario de activos](docs/sgsi/02-inventario-activos.csv)
- [BIA](docs/sgsi/03-bia.csv)
- [Matriz de riesgos](docs/sgsi/04-riesgos.csv) y [OCTAVE Allegro](docs/sgsi/05-octave-allegro.md)
- [Matriz de controles](docs/sgsi/06-controles.csv) y [políticas](docs/sgsi/07-politicas.md)
- [Continuidad y centro de datos](docs/sgsi/08-continuidad-y-datacenter.md)
- [COBIT 2019 e ITIL 4](docs/sgsi/09-gobierno-y-servicios.md)
- [Estado y registro de evidencia](docs/sgsi/10-evidencias-y-estado.md)
- [Discusión y referencias APA 7](docs/sgsi/11-discusion-y-referencias.md)

El paquete distingue capacidades de la aplicación, plantillas de despliegue, controles propuestos y evidencia pendiente. No afirma certificación ISO, rating TIA-942 ni despliegues cloud que no hayan ocurrido.

## Nube Azure de costo limitado

La arquitectura mantiene computo y bases en el laboratorio y prepara una copia cifrada Azure Blob solo si la suscripcion confirma cuota gratuita disponible. El titular puede ejecutar [`storage.bicep`](infrastructure/azure/storage.bicep) con [`deploy-storage.ps1`](infrastructure/azure/deploy-storage.ps1) y cargar un `.tar.enc` con [`upload-backup.ps1`](infrastructure/azure/upload-backup.ps1).

Azure for Students publica cuotas gratuitas por servicio y periodo; el nivel gratuito de Blob debe confirmarse en el portal para esta cuenta antes de desplegar. El plan no autoriza a consumir creditos: si el recurso queda fuera de cuota gratuita, no desplegarlo. Mantenga el limite de gasto activo y no actualice a pago por uso. Consulte [plan-azure.md](docs/sgsi/plan-azure.md).

No cargue expedientes reales. La región elegida queda fuera de Guatemala y exige revisión legal de datos y transferencia internacional antes de un uso institucional.

## Marcos aplicados

ISO/IEC 27001 y 27002 orientan el SGSI y la selección de controles; ISO/IEC 27005 y NIST SP 800-30 definen la gestión y evaluación de riesgos; OCTAVE Allegro aporta evaluación cualitativa centrada en activos; NIST CSF 2.0 estructura resultados de ciberseguridad; NIST SP 800-207 guía Zero Trust; ISO 22301 informa continuidad; COBIT 2019 organiza gobierno; ITIL 4 aterriza la operación de servicios; ANSI/TIA-942-C guía el diseño de la sala de servidores.

## Desarrollo

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".\backend[dev]"
python -m uvicorn app.main:app --app-dir backend --reload --port 8001
```

En otra terminal: `cd frontend`, `npm ci`, `npm run dev`. Para credenciales, base, migraciones y ejecución completa use Docker Compose.

La aplicación heredada tenía una empresa demo y material TecnoMarket. Los documentos históricos de importación y capturas no se consideran evidencia de los controles educativos. Las matrices de esta versión son supuestos de proyecto y deben validarse antes de presentarse como resultados medidos.
