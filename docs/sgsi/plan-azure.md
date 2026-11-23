# Plan de nube Azure sin gasto de bolsillo

**Consulta:** 23 de noviembre de 2026. **Preferencia:** solo cuotas gratuitas, sin consumir el saldo de creditos. El procesamiento permanece en el equipo local; Azure aporta una copia cifrada en Blob unicamente si el portal confirma una cuota gratuita vigente para esta suscripcion.

## Oferta y condicion de uso

Azure for Students anuncia USD 100 de creditos por 12 meses y acceso gratuito a cantidades seleccionadas de servicios. La oferta exige elegibilidad y puede cambiar. La pagina oficial de servicios gratuitos enumera Azure Blob Storage con 5 GB de almacenamiento LRS Hot, 20,000 lecturas y 10,000 escrituras al mes durante 12 meses para cuentas elegibles nuevas. Antes de desplegar, el titular debe verificar que esas cuotas aparezcan en su cuenta y que el recurso este cubierto por el nivel gratuito. No se debe asumir que todo usuario educativo califica.

El plan de este proyecto no autoriza a gastar los USD 100 de creditos. Si Azure muestra cargos, saldo de credito consumido o la cuota no esta disponible, no desplegar Blob. Mantener copia local y usar medio externo cifrado de laboratorio mientras se valida una opcion gratuita aprobada por el curso. No cambiar a pago por uso.

## Arquitectura de costo cero dentro de cuota

| Capa | Servicio | Regla de uso |
|---|---|---|
| Aplicacion, API, PostgreSQL, Redis y worker | Equipo local con Docker Compose | Sin computo Azure |
| Copia fuera de sitio | Azure Blob LRS Hot, contenedor privado | Solo dentro de la cuota visible; sin Cool, versioning, soft delete ni Change Feed |
| Identidad | Entra ID incluido | RBAC sobre el contenedor y autenticacion OAuth; validar MFA de cuenta |
| Red | HTTPS saliente | Sin VM, VPN Gateway, NAT, Private Endpoint, firewall administrado ni Marketplace |

La cuenta usa endpoint publico de servicio, acceso anonimo deshabilitado, Shared Key deshabilitada, HTTPS obligatorio y TLS 1.2. El endpoint es publico pero autenticado; no equivale a conectividad privada. El operador debe tener solo el rol necesario en el contenedor.

La plantilla evita funciones de versionado, retencion y Change Feed para no crear consumo adicional fuera de la cuota. El script limita la carga local a 4.5 GB totales como margen bajo la cuota publicada de 5 GB. Las cuotas de operaciones tambien aplican. La descarga/restauracion gasta lecturas; registra los contadores observados y evita ciclos repetidos.

## Controles de presupuesto

1. El titular revisa en Azure Portal la elegibilidad y las cuotas especificas de Storage antes de autorizar.
2. Dejar activo el limite de gasto estudiantil y no actualizar a pago por uso.
3. Leer Bicep y scripts; solo continuar si el portal indica que el despliegue y las operaciones caben en cuota gratuita.
4. `deploy-storage.ps1` requiere escribir `DEPLOY-FREE-BLOB`; no ejecutarlo si la cuota no esta confirmada.
5. `upload-backup.ps1` rechaza archivos distintos de `.tar.enc`, exige el `.sha256` y limita el contenedor a 4.5 GB.
6. Revisar costo/consumo tras cada operacion. Si el costo estimado es mayor que cero, detener cargas y no usar creditos.
7. Antes de que venza el periodo gratuito, eliminar el recurso si no se tiene otra cuota gratuita confirmada. La eliminacion puede borrar el unico respaldo externo: verificar y guardar previamente la copia local.
8. No cargar datos reales de estudiantes hasta que Juridica apruebe ubicacion, transferencia, contrato, retencion y derechos de titulares.

## Despliegue condicionado

1. Instalar Azure CLI y el titular inicia sesion localmente con `az login`; nunca compartir contrasenas, tokens o subscription ID en el repositorio.
2. Confirmar la cuota gratuita actual en el portal, saldo, limites y fecha de vencimiento. La plantilla propone `southcentralus`; cambiarla si la oferta no cubre la region.
3. Ejecutar `infrastructure/azure/deploy-storage.ps1` solo si los costos previstos son cero y el titular acepta crear el recurso.
4. Verificar en Access Control (IAM) la asignacion RBAC y en la cuenta TLS, acceso privado del contenedor, acceso anonimo y Shared Key.
5. Cargar backup sintetico cifrado con `upload-backup.ps1`; comprobar SHA-256 y restaurar en entorno aislado.
6. Anotar bytes, operaciones, elegibilidad, fecha, hash y resultado en evidencia. No afirmar RPO/RTO cumplido sin medirlo.

La infraestructura esta preparada, pero no desplegada. No se ha recibido permiso para consumir creditos, ni se han creado recursos Azure.

## Referencias oficiales

Microsoft. (s. f.). *Azure for Students*. https://learn.microsoft.com/azure/education-hub/about-azure-for-students

Microsoft. (s. f.). *Azure free services*. https://azure.microsoft.com/en-us/pricing/free-services/

Microsoft. (s. f.). *Azure spending limit*. https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit

Microsoft. (s. f.). *Azure Blob Storage pricing*. https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
