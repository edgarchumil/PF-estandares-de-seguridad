param(
  [Parameter(Mandatory = $true)]
  [string]$SubscriptionId,
  [string]$ResourceGroup = 'rg-sgsi-ufvv-demo',
  [string]$Location = 'southcentralus'
)

$ErrorActionPreference = 'Stop'
$template = Join-Path $PSScriptRoot 'storage.bicep'

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
  throw 'Instala Azure CLI antes de ejecutar este script.'
}

Write-Host 'Despliega solo los recursos Blob cubiertos por la cuota gratuita confirmada en el portal.'
Write-Host 'No uses crédito promocional ni actualices a pago por uso.'
Write-Host 'El perfil usa Blob LRS Hot y no activa versiones, retenciones ni Change Feed.'
Write-Host 'No se crea VM, VPN Gateway, firewall administrado o Private Endpoint.'

az account set --subscription $SubscriptionId
if ($LASTEXITCODE -ne 0) { throw 'No se pudo seleccionar la suscripción.' }
$account = az account show --query '{name:name,state:state}' --output json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0 -or $account.state -ne 'Enabled') {
  throw 'La suscripción no está activa; no se desplegaron recursos.'
}
Write-Host "Suscripción activa: $($account.name)"

$operatorId = az ad signed-in-user show --query id --output tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($operatorId)) {
  throw 'Inicia sesión con una cuenta Entra de usuario antes del despliegue.'
}

az group create --name $ResourceGroup --location $Location --output none
if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear o verificar el grupo de recursos.' }

Write-Host 'Vista previa de los recursos solicitados (what-if):'
az deployment group what-if `
  --resource-group $ResourceGroup `
  --template-file $template `
  --parameters location=$Location operatorPrincipalId=$operatorId `
  --result-format FullResourcePayloads `
  --output jsonc
if ($LASTEXITCODE -ne 0) { throw 'La validación what-if falló; no se desplegaron recursos.' }

$confirmation = Read-Host 'Si el resultado es solo la cuenta Blob privada prevista, escribe APPLY-FREE-BLOB'
if ($confirmation -cne 'APPLY-FREE-BLOB') {
  throw 'Despliegue cancelado después de what-if.'
}

az deployment group create `
  --resource-group $ResourceGroup `
  --template-file $template `
  --parameters location=$Location operatorPrincipalId=$operatorId `
  --output table
if ($LASTEXITCODE -ne 0) { throw 'El despliegue falló. Revisa el mensaje de Azure y el saldo educativo.' }

Write-Host 'Despliegue completado. Revisa Access control (IAM), Cost Management y la cuenta antes de cargar datos.'
