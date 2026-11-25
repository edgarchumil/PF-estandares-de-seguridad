# Plan de nube Azure sin gasto de bolsillo

**Consulta:** 24 de noviembre de 2026. **Preferencia:** solo cuotas gratuitas, sin consumir créditos promocionales ni actualizar a pago por uso. El procesamiento permanece en el equipo local; Azure aporta una copia cifrada en Blob dentro de la cuota gratuita confirmada en el portal.

## Oferta y condicion de uso

La cuenta observada es una prueba gratuita de Azure, no una suscripción Azure Sponsorships activa. En el portal, la tabla **Servicios gratuitos durante 12 meses** confirma para esta suscripción los medidores de Blob Hot LRS: 5 GB de almacenamiento por mes, 20,000 operaciones de lectura y 10,000 de escritura, además de operaciones de lista/creación de contenedor. La captura mostraba uso 0 y vencimiento de la cuota el 23 de diciembre de 2027. La cuota aplica solo dentro de esos límites y su consumo puede tardar hasta 24 horas en reflejarse.

La prueba también muestra crédito promocional con vencimiento el 23 de diciembre de 2026. Este trabajo no autoriza su consumo ni una actualización a pago por uso. La suscripción de prueba se deshabilitará al vencer si no se actualiza; por tanto, cualquier despliegue en esta suscripción sirve solo para una demostración temporal y no garantiza disponibilidad posterior. Si la cuota gratuita no cubre el recurso o el portal refleja consumo de crédito/costo, detener el despliegue y conservar únicamente la copia local cifrada.

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

1. El portal ya confirma una cuota gratuita para Blob Hot LRS en esta suscripción; revisar uso y límites antes y después de cada operación.
2. Dejar activo el limite de gasto estudiantil y no actualizar a pago por uso.
3. Leer Bicep y scripts; solo continuar si el portal indica que el despliegue y las operaciones caben en cuota gratuita.
4. `deploy-storage.ps1` ejecuta `what-if` y requiere escribir `APPLY-FREE-BLOB`; cancela si la vista previa falla o la cuota no está confirmada.
5. `upload-backup.ps1` rechaza archivos distintos de `.tar.enc`, exige el `.sha256` y limita el contenedor a 4.5 GB.
6. Revisar costo/consumo tras cada operacion. Si el costo estimado es mayor que cero, detener cargas y no usar creditos.
7. Antes del vencimiento de la prueba el 23 de diciembre de 2026, verificar y guardar la copia local y eliminar el recurso temporal si no se ha aprobado una alternativa gratuita que mantenga la disponibilidad. El vencimiento de la prueba deshabilita la suscripción aunque la cuota Blob indique vigencia hasta 2027.
8. No cargar datos reales de estudiantes hasta que Juridica apruebe ubicacion, transferencia, contrato, retencion y derechos de titulares.

## Despliegue y estado observado

1. Azure CLI se instaló el 24 de noviembre de 2026 para desplegar infraestructura. El 25-11-2026 su autenticación de datos falló con `AADSTS530035`; la carga se completó desde el portal con la sesión MFA de Entra. No incluir tokens, contraseñas o ID de suscripción en el repositorio.
2. El portal confirmó la cuota de Blob gratuita. La plantilla se desplegó en `southcentralus` al grupo `rg-sgsi-ufvv-demo`.
3. `what-if` mostró cuatro recursos. Azure informó `Succeeded`; se creó la cuenta `ufvvsgsi63svuskqb2xne` y el contenedor `sgsi-backups`.
4. Verificación posterior: Standard LRS Hot, HTTPS obligatorio, TLS 1.2, acceso anónimo y Shared Key deshabilitados, contenedor sin acceso público y RBAC `Storage Blob Data Contributor` para el operador.
5. El 24-11-2026 el portal confirmó la carga de `securecommerce-20261125T013838Z.tar.enc` (179.03 KiB) y su `.sha256` (115 B) al contenedor privado. El hash local se verificó antes de transferir. El respaldo de demostración es de SecureCommerce; la copia descargada desde Azure y la restauración aún no se han probado.
6. El portal indicó uso gratuito cero antes del despliegue; revisar de nuevo en 24–48 horas, porque los medidores pueden demorarse. Registrar métricas y no afirmar RPO/RTO cumplido sin ejercicio de restauración.

El recurso está desplegado para demostración dentro de la cuota gratuita. La suscripción Free Trial vence el 23 de diciembre de 2026; sin una alternativa aprobada y sin costo, Azure deshabilitará la suscripción y el respaldo dejará de estar disponible. No consumir el crédito promocional ni actualizar a pago por uso.

## Referencias oficiales

Microsoft. (s. f.). *Check usage of free services included with your Azure free account*. https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/check-free-service-usage

Microsoft. (s. f.). *Avoid charges with your Azure free account*. https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/avoid-charges-free-account

Microsoft. (s. f.). *Microsoft Entra authentication & authorization error codes*. https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes

Microsoft. (s. f.). *Azure free services*. https://azure.microsoft.com/en-us/pricing/free-services/

Microsoft. (s. f.). *Azure spending limit*. https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit

Microsoft. (s. f.). *Azure Blob Storage pricing*. https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
