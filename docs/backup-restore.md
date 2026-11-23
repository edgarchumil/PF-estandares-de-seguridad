# Respaldo y restauración de SGSI-UFVV

El perfil Compose `backup` crea una copia cifrada de PostgreSQL y de los reportes; la implementación predeterminada es diaria. La configuración en [BIA](sgsi/03-bia.csv) propone RPO de una hora para SIS/LMS. Por lo tanto, el job diario **no cumple el objetivo** hasta implementar cadencia/incremental apropiado y medirlo. El RTO también necesita un ejercicio cronometrado.

## Operación local

Configure `BACKUP_ENCRYPTION_KEY` de al menos 32 caracteres aleatorios en `.env` y no la almacene en Git. Inicie el perfil opcional:

```powershell
docker compose --profile backup up -d backup
docker compose logs backup
```

Para copia única, verificar hash y listar archivo:

```powershell
docker compose --profile backup run --rm -e BACKUP_RUN_ONCE=true backup
docker compose --profile backup run --rm --entrypoint sh backup -c "ls -lh /backups"
docker compose --profile backup run --rm --entrypoint /usr/local/bin/verify.sh `
  -e BACKUP_FILE=/backups/sgsi-ufvv-FECHA.tar.enc backup
```

Restauración sobrescribe la base objetivo. Trabaje sobre un proyecto Compose aislado, inspeccione el respaldo y confirme que el target no contiene datos necesarios.

## Réplica Azure

El plan y scripts están en `infrastructure/azure` y `docs/sgsi/plan-azure.md`. Requieren que el titular se autentique en su Azure for Students y ejecute el despliegue interactivo. Cargue solo el `.tar.enc` y su manifiesto `.sha256` con `upload-backup.ps1`. Descargue y verifique en entorno aislado antes de declarar que la copia externa se puede restaurar. Mantenga activo spending limit; Azure Blob consume crédito y la retención genera almacenamiento.

## Registro de prueba

Anote EV-ID, fecha, origen, tamaño, hash, crédito antes/después, descarga, resultado de descifrado/restauración, usuario autorizado, duración observada, RPO/RTO alcanzados, fallas y acciones. Nunca incluya la clave, token, URI SAS o información real de estudiantes en la evidencia.
