# Despliegue de SGSI-UFVV

## Laboratorio local

Docker Compose es el entorno ejecutable. Nginx expone la web por `APP_PORT` (8080 por defecto); PostgreSQL y Redis permanecen en red interna sin puertos host. El servicio de backup cifrado es perfil opcional. Siga el [README](../README.md) para levantar la aplicación y [backup-restore.md](backup-restore.md) para generar y comprobar copias.

## Azure educativo

La plantilla Bicep prepara una cuenta Azure Blob privada para copia externa autenticada. El usuario titular debe revisar sus permisos y crédito y ejecutar los scripts de [`infrastructure/azure`](../infrastructure/azure). Los recursos consumen crédito educativo. La plantilla no crea VM, VPN Gateway, firewall administrado ni Private Endpoint. No contiene datos ni secretos; tampoco se ha aplicado en una suscripción.

## Producción institucional

El diseño objetivo requiere revisión de arquitectura, región y contratos por la institución; TLS, WAF, observabilidad, política de acceso, retención, recuperación y presupuesto aprobados. El Compose local no debe presentarse como producción ni certificación. No iniciar un plan de pago para la demo sin aprobación presupuestal separada.
