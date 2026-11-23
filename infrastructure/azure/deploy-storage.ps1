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

Write-Host 'Despliega solo si el portal confirma que esta cuenta tiene cuota Blob gratuita disponible.'
Write-Host 'La cuota depende de elegibilidad, cuenta y vigencia; no uses créditos ni actualices a pago por uso.'
Write-Host 'El perfil usa Blob LRS Hot y no activa versiones, retenciones ni Change Feed.'
Write-Host 'No se crea VM, VPN Gateway, firewall administrado o Private Endpoint.'
$confirmation = Read-Host 'Escribe DEPLOY-FREE-BLOB para continuar'
if ($confirmation -cne 'DEPLOY-FREE-BLOB') {
  throw 'Despliegue cancelado.'
}

az account set --subscription $SubscriptionId
if ($LASTEXITCODE -ne 0) { throw 'No se pudo seleccionar la suscripción.' }

$operatorId = az ad signed-in-user show --query id --output tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($operatorId)) {
  throw 'Inicia sesión con una cuenta Entra de usuario antes del despliegue.'
}

az group create --name $ResourceGroup --location $Location --output none
if ($LASTEXITCODE -ne 0) { throw 'No se pudo crear o verificar el grupo de recursos.' }

az deployment group create `
  --resource-group $ResourceGroup `
  --template-file $template `
  --parameters location=$Location operatorPrincipalId=$operatorId `
  --output table
if ($LASTEXITCODE -ne 0) { throw 'El despliegue falló. Revisa el mensaje de Azure y el saldo educativo.' }

Write-Host 'Despliegue completado. Revisa Access control (IAM), Cost Management y la cuenta antes de cargar datos.'
