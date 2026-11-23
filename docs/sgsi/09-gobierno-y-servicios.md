# Gobierno de TI y gestión de servicios

## Modelo de gobierno inspirado en COBIT 2019

Rectoría y Dirección General conservan la autoridad de aprobar apetito de riesgo, presupuesto, excepciones, alcance y prioridades académicas. El Comité de Seguridad y Continuidad se reúne trimestralmente y tras incidentes mayores. Dirección de TI ejecuta y mide; cada proceso conserva su dueño y acepta el riesgo residual de su área; Asesoría Jurídica revisa obligaciones y contratos.

| Objetivo COBIT 2019 | Decisión concreta UFVV | Responsable | Indicador |
|---|---|---|---|
| EDM03 – Ensure Risk Optimization | Dirección revisa riesgos críticos, apetito, excepciones y recursos | Comité de Dirección | % riesgos críticos con decisión vigente |
| APO12 – Managed Risk | Mantener matriz NIST 800-30, OCTAVE y tratamientos relacionados con el BIA | Responsable SGSI | Riesgos vencidos y residual fuera de tolerancia |
| APO13 – Managed Security | Aprobar políticas, identidad, incidentes y controles de seguridad | Dirección TI / SGSI | Controles con dueño y evidencia actual |
| APO10 – Managed Vendors | Evaluar nube, LMS, nómina, biblioteca y contratos | Compras / Jurídica / TI | Proveedores críticos revisados en el año |
| BAI06 – Managed IT Changes | Aprobar, probar, registrar impacto y rollback antes de desplegar | Mesa de cambios | Cambios urgentes y cambios con reversa probada |
| BAI09 – Managed Assets | Custodiar inventario de activos, dueño, ubicación y ciclo de vida | Dueños de proceso / TI | Activos críticos con owner y clasificación |
| DSS02 – Managed Service Requests and Incidents | Registrar solicitudes y eventos de servicio, priorizar y escalar | Mesa de ayuda | Cumplimiento de SLA por severidad |
| DSS04 – Managed Continuity | Probar backup, recuperación, RTO y comunicación de contingencia | Dirección TI / proceso | Pruebas aprobadas contra BIA |
| DSS05 – Managed Security Services | Operar controles de acceso, endpoint, registros, red y respuesta | Responsable SOC/SGSI | Alertas críticas investigadas dentro del plazo |
| MEA03 – Managed Compliance with External Requirements | Mantener requisitos, responsable, evidencia y revisión legal | Jurídica / SGSI | Requisitos con estado y próxima revisión |

Se propone una madurez inicial objetivo de nivel 2 (proceso repetible y medido en áreas críticas), sin afirmar una calificación COBIT real. El comité calcula la capacidad después de recopilar evidencia, entrevistas y resultados de auditoría.

## ITIL 4 aplicado al catálogo de servicios

| Práctica ITIL 4 | Servicio UFVV | Flujo acordado | Medida |
|---|---|---|---|
| Service Desk / Incident Management | SIS, LMS, identidad, red | Registrar, categorizar, priorizar, asignar, comunicar y cerrar | Tiempo de reconocimiento y resolución |
| Problem Management | Incidentes repetidos de matrícula o autenticación | Investigar causa raíz, registrar workaround y eliminar causa | Reincidencia mensual |
| Change Enablement | Cambios SIS, red, roles y versiones | Evaluar riesgo, aprobación adecuada, ventana, plan de reversa y validación | Cambios fallidos o de emergencia |
| Service Level Management | Disponibilidad SIS/LMS | Acordar horario, RTO, RPO, contacto y medición con dueños/proveedores | Disponibilidad y cumplimiento RTO/RPO |
| IT Asset Management | Dispositivos, licencias y equipos | Adquirir, asignar, mantener, retirar y eliminar datos | Activos críticos inventariados |
| Service Configuration Management | Dependencias entre identidad, base, DNS, red y aplicaciones | Mantener CI, propietario, versión, relación, cambio e impacto | CIs críticos con relaciones vigentes |
| Service Continuity Management | Recuperación académica | Preparar recursos, respaldos, responsables y pruebas de recuperación | Ejercicios realizados y acciones cerradas |
| Information Security Management | Identidades, datos, dispositivos y proveedores | Política, controles, formación, evidencia y mejora | Hallazgos repetidos y excepciones abiertas |
| Monitoring and Event Management | API, SIEM, EDR y red | Alertar, correlacionar, validar y abrir ticket de incidente | Alertas accionables atendidas |

COBIT establece quién decide y cómo se revisa valor, riesgo y cumplimiento. ITIL aterriza esas decisiones en el flujo cotidiano de servicios y soporte. La tabla de prioridades no demuestra que las prácticas estén implantadas: las métricas solo se calculan con tickets, contratos y logs reales de la UFVV.

## RACI resumido

| Actividad | Dirección | SGSI | TI / SOC | Dueño del proceso | Jurídica / RRHH |
|---|---|---|---|---|---|
| Aprobar apetito y aceptación de riesgo alto | A | R | C | C | C |
| Mantener activos y procesos | I | C | R | A/R | C |
| Aplicar control técnico | I | C | A/R | C | I |
| Declarar incidente mayor | A | R | R | C | C |
| Aprobar política | A | R | C | C | C |
| Probar recuperación y aceptar servicio | I | C | R | A | I |

R = responsable ejecutor; A = responsable que aprueba y responde por resultado; C = consultado; I = informado. Una persona puede cubrir varios roles en el prototipo, pero sus aprobaciones deben conservar separación en los registros.
