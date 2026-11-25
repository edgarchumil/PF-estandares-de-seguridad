# Respaldo y restauración de SGSI-UFVV

El perfil Compose `backup` crea una copia cifrada de PostgreSQL y de los reportes; la implementación predeterminada es diaria. La configuración en [BIA](sgsi/03-bia.csv) propone RPO de una hora para SIS/LMS. Por lo tanto, el job diario **no cumple el objetivo** hasta implementar cadencia/incremental apropiado y medirlo. El RTO también necesita un ejercicio cronometrado.

## Operación local

Mantenga la clave de cifrado en `.secrets/backup-encryption.env`, excluida de Git, con al menos 32 caracteres aleatorios. Para invocar Compose use ambos archivos de entorno, en este orden, para que la clave aleatoria reemplace cualquier valor de ejemplo en `.env`:

```powershell
docker compose --env-file .env --env-file .secrets/backup-encryption.env --profile backup up -d backup
docker compose --profile backup logs backup
```

Para copia única, verificar hash y listar archivo:

```powershell
docker compose --env-file .env --env-file .secrets/backup-encryption.env --profile backup run --rm -e BACKUP_RUN_ONCE=true backup
docker compose --env-file .env --env-file .secrets/backup-encryption.env --profile backup run --rm --entrypoint sh backup -c "ls -lh /backups"
docker compose --env-file .env --env-file .secrets/backup-encryption.env --profile backup run --rm --entrypoint /usr/local/bin/verify.sh `
  -e BACKUP_FILE=/backups/sgsi-ufvv-FECHA.tar.enc backup
```

Restauración sobrescribe la base objetivo. Trabaje sobre un proyecto Compose aislado, inspeccione el respaldo y confirme que el target no contiene datos necesarios.

## Réplica Azure

El plan y scripts están en `infrastructure/azure` y `docs/sgsi/plan-azure.md`. El 24-11-2026 se cargaron al contenedor privado `sgsi-backups` una copia cifrada de demostración y su manifiesto `.sha256` mediante el portal de Azure. La verificación del hash se hizo sobre el archivo local; falta descargar la copia remota y ensayar restauración aislada. Mantenga activo spending limit y revise los medidores de Blob; el archivo ocupa almacenamiento mientras permanezca en la cuenta.

## Registro de prueba

Anote EV-ID, fecha, origen, tamaño, hash, crédito antes/después, descarga, resultado de descifrado/restauración, usuario autorizado, duración observada, RPO/RTO alcanzados, fallas y acciones. Nunca incluya la clave, token, URI SAS o información real de estudiantes en la evidencia.
