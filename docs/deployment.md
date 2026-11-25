# Despliegue del CGSI

## Laboratorio local

Docker Compose es el entorno ejecutable. Nginx expone la web por `APP_PORT` (8080 por defecto); PostgreSQL y Redis permanecen en red interna sin puertos host. El servicio de backup cifrado es perfil opcional. Siga el [README](../README.md) para levantar la aplicación y [backup-restore.md](backup-restore.md) para generar y comprobar copias.

## Azure educativo

La plantilla Bicep está desplegada en `rg-sgsi-ufvv-demo`: cuenta Blob Standard LRS Hot y contenedor privado `sgsi-backups`, con RBAC para el operador. Verificadas HTTPS, TLS 1.2, acceso anónimo deshabilitado y Shared Key deshabilitada. El portal confirmó medidores gratuitos de Blob Hot LRS; revisar el consumo después de 24–48 horas. El 24 de noviembre de 2026 se cargó un respaldo cifrado de demostración de SecureCommerce (179.03 KiB) con su manifiesto SHA-256 (115 B); la restauración remota no se ha probado. La suscripción Free Trial vence el 23 de diciembre de 2026; el servicio es temporal sin una alternativa gratuita aprobada. No se creó VM, VPN Gateway, firewall administrado ni Private Endpoint.

## Producción institucional

El diseño objetivo requiere revisión de arquitectura, región y contratos por la institución; TLS, WAF, observabilidad, política de acceso, retención, recuperación y presupuesto aprobados. El Compose local no debe presentarse como producción ni certificación. No iniciar un plan de pago para la demo sin aprobación presupuestal separada.
