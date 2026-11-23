param(
  [Parameter(Mandatory = $true)]
  [string]$BackupFile,
  [Parameter(Mandatory = $true)]
  [string]$StorageAccount
)

$ErrorActionPreference = 'Stop'
if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
  throw 'Instala Azure CLI antes de ejecutar este script.'
}

$resolved = (Resolve-Path -LiteralPath $BackupFile).Path
if ($resolved -notmatch '\.tar\.enc$') {
  throw 'Solo se permite cargar un archivo de respaldo ya cifrado con extensión .tar.enc.'
}
$hashFile = "$resolved.sha256"
if (-not (Test-Path -LiteralPath $hashFile)) {
  throw 'No existe el manifiesto SHA-256 generado junto con el respaldo.'
}

$existingJson = az storage blob list --account-name $StorageAccount --container-name sgsi-backups `
  --auth-mode login --query "[].properties.contentLength" --output json
if ($LASTEXITCODE -ne 0) { throw 'No se pudo consultar el uso actual del contenedor.' }
$existingBytes = 0L
foreach ($length in (ConvertFrom-Json -InputObject $existingJson)) {
  $existingBytes += [long]$length
}
$incomingBytes = (Get-Item -LiteralPath $resolved).Length + (Get-Item -LiteralPath $hashFile).Length
if (($existingBytes + $incomingBytes) -gt 4500000000) {
  throw 'El limite local de seguridad es 4.5 GB; limpia/archiva con aprobacion o no cargues esta copia.'
}

$blobName = '{0}/{1}' -f (Get-Date -Format 'yyyy/MM'), (Split-Path -Leaf $resolved)
az storage blob upload --account-name $StorageAccount --container-name sgsi-backups `
  --file $resolved --name $blobName --auth-mode login --overwrite false --only-show-errors
if ($LASTEXITCODE -ne 0) { throw 'La carga cifrada falló.' }

az storage blob upload --account-name $StorageAccount --container-name sgsi-backups `
  --file $hashFile --name "$blobName.sha256" --auth-mode login --overwrite false --only-show-errors
if ($LASTEXITCODE -ne 0) { throw 'La carga del hash falló; revisa el blob antes de continuar.' }

Write-Host "Copia cifrada cargada: $blobName"
Write-Host 'Verifica el hash y registra fecha, RPO y resultado en la bitácora de continuidad.'
