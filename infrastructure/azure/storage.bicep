targetScope = 'resourceGroup'

@description('Nombre globalmente único de la cuenta de almacenamiento (3–24 minúsculas/números).')
@minLength(3)
@maxLength(24)
param storageAccountName string = toLower('ufvvsgsi${uniqueString(resourceGroup().id)}')

@description('Object ID del operador que recibirá acceso al contenedor de copias.')
param operatorPrincipalId string

@description('Región Azure que la suscripción educativa tenga habilitada.')
param location string = resourceGroup().location

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: false
    allowSharedKeyAccess: false
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
    publicNetworkAccess: 'Enabled'
    defaultToOAuthAuthentication: true
    allowCrossTenantReplication: false
    encryption: {
      keySource: 'Microsoft.Storage'
      requireInfrastructureEncryption: true
      services: {
        blob: {
          enabled: true
          keyType: 'Account'
        }
        file: {
          enabled: true
          keyType: 'Account'
        }
      }
    }
    networkAcls: {
      bypass: 'AzureServices'
      defaultAction: 'Allow'
      ipRules: []
      virtualNetworkRules: []
    }
  }
}

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-05-01' = {
  parent: storage
  name: 'default'
  properties: {
    isVersioningEnabled: false
    deleteRetentionPolicy: {
      enabled: false
    }
    containerDeleteRetentionPolicy: {
      enabled: false
    }
    changeFeed: {
      enabled: false
    }
  }
}

resource backupContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: blobService
  name: 'sgsi-backups'
  properties: {
    publicAccess: 'None'
    metadata: {
      dataClassification: 'restricted-encrypted-backups'
      owner: 'UFVV-IT'
    }
  }
}

resource backupWriter 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  scope: backupContainer
  name: guid(backupContainer.id, operatorPrincipalId, 'storage-blob-data-contributor')
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      'ba92f5b4-2d11-453d-a403-e96b0029c9fe'
    )
    principalId: operatorPrincipalId
    principalType: 'User'
  }
}

output storageAccountName string = storage.name
output backupContainerName string = backupContainer.name
output blobEndpoint string = storage.properties.primaryEndpoints.blob
