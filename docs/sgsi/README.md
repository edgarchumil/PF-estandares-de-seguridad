# Centro de Gestión de Seguridad de la Información (CGSI)

Paquete académico para el diseño e implementación demostrable del Sistema de Gestión de Seguridad de la Información de la **Universidad Ficticia del Valle Verde (UFVV)**. Todos los datos de la universidad, personas, procesos, activos, costos y riesgos son supuestos para el proyecto; no describen una entidad real ni una auditoría.

## Entregables

| Archivo | Entregable |
|---|---|
| [informe-final.md](informe-final.md) | Informe académico integrado; completar autor, equipo, curso y docente |
| [presentacion.md](presentacion.md) | Guion de presentación de 10 diapositivas |
| [00-escenario-y-alcance.md](00-escenario-y-alcance.md) | Organización, contexto, alcance, procesos y supuestos |
| [01-arquitectura-hibrida.md](01-arquitectura-hibrida.md) | Arquitectura, zonas, flujos, Azure y costos |
| [02-inventario-activos.csv](02-inventario-activos.csv) | Inventario de activos con propietario, custodio y C/I/D |
| [03-bia.csv](03-bia.csv) | Business Impact Analysis por proceso crítico |
| [04-riesgos.csv](04-riesgos.csv) | Evaluación NIST SP 800-30, criterios, inherente y residual |
| [05-octave-allegro.md](05-octave-allegro.md) | Evaluación cualitativa OCTAVE Allegro |
| [06-controles.csv](06-controles.csv) | Matriz de controles y trazabilidad entre riesgo y marcos |
| [07-politicas.md](07-politicas.md) | Políticas institucionales y controles previstos |
| [08-continuidad-y-datacenter.md](08-continuidad-y-datacenter.md) | BCP, DRP, recuperación y evaluación de diseño TIA-942-C |
| [09-gobierno-y-servicios.md](09-gobierno-y-servicios.md) | Aplicación concreta de COBIT 2019 e ITIL 4 |
| [10-evidencias-y-estado.md](10-evidencias-y-estado.md) | Registro de evidencia y distinción entre diseño e implementación |
| [11-discusion-y-referencias.md](11-discusion-y-referencias.md) | Discusión del curso, fuentes y referencias APA 7 |
| [plan-azure.md](plan-azure.md) | Plan de Azure Free Trial, cuota Blob gratuita y límites de vigencia |

## Estado de implementación

El codigo local ofrece autenticacion, roles, MFA TOTP opcional, inventario, evaluacion NIST CSF 2.0, matriz de riesgos, tratamientos, incidentes, auditoria y respaldos cifrados. Docker Compose separa los servicios de borde de PostgreSQL y Redis mediante redes de contenedores. La cuenta Azure y la carga tienen plantilla Bicep y scripts, pero no se han desplegado: el titular debe confirmar la cuota gratuita vigente y ejecutar el paso interactivo sin consumir creditos.

Suricata/Wazuh, MDM, DLP corporativo, VPN de sitio, redundancia física y certificación TIA-942 se presentan como diseño o tareas de laboratorio hasta que exista evidencia real. No se deben marcar como controles implementados sin desplegarlos y capturar resultados auténticos.

## Supuestos por validar para una defensa

La matrícula de 4,500 estudiantes, 450 colaboradores, dos sedes, impactos y objetivos BIA son parámetros ficticios de trabajo. Un equipo real de Registro Académico, TI, Finanzas, Docencia y Dirección tendría que validarlos. Las organizaciones y credenciales de demostración de la base local heredada pueden persistir en volúmenes existentes; no elimines volúmenes para limpiar el demo sin guardar primero los datos que quieras conservar.
