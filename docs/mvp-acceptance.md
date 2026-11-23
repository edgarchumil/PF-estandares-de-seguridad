# Estado de aceptación del prototipo SGSI-UFVV

La aplicación base ofrece flujos locales de organizaciones y roles, perfil, MFA TOTP opcional, activos, evaluación NIST CSF, riesgos y tratamientos, recomendaciones, dashboard, reportes, incidentes, auditoría, configuración y sesiones. Los módulos se han reorientado visualmente a una universidad ficticia y el seed incluye un tenant educativo; una base persistente heredada conserva sus registros anteriores.

La carpeta `docs/sgsi` contiene las matrices, políticas y decisiones académicas. El prototipo no equivale a SGSI certificado, no representa una universidad real ni acredita que se hayan desplegado Azure, MDM, DLP, EDR, SIEM o la arquitectura física descrita.

## Evidencia disponible / pendiente

- La aplicación y Compose son ejecutables en local; la base productiva de demostración anterior se conserva para evitar borrar datos sin autorización.
- NIST CSF, activos, riesgos, tratamientos, incidentes, MFA y auditoría existen en el código base con diferentes niveles de configuración; la evaluación debe repetirse con datos UFVV y guardar evidencia sin secretos.
- El respaldo cifrado local tiene scripts y runbook. La cadencia diaria no satisface el objetivo SIS de una hora; deben implementarse frecuencia o WAL y aprobarse una prueba de recuperación.
- Azure cuenta con plantilla Bicep y herramientas de carga preparadas, no desplegadas.
- Las suites automatizadas del repo heredado no se han ejecutado sobre esta adaptación. El cambio de seed y las etiquetas requieren revisar y luego ejecutar la suite antes de declarar aceptación.
- Falta capturar evidencia real de cloud, restauración, separación de red, telemetría, MDM/DLP, operación de servicios y sala física.
