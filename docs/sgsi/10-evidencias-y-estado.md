# Estado de implementación y evidencia

El proyecto separa los controles ejecutables del repositorio, los preparados para laboratorio y los que son propuesta de diseño. El documento final solo debe asignar estado **Implementado** si existe una captura, exportación o registro auténtico fechado, identificable y sin secretos. Las muestras que aún no se han tomado aparecen como **Pendiente**, no como resultados.

| Elemento | Estado en esta carpeta | Qué falta para cerrar |
|---|---|---|
| App SGSI local y API | Ejecutable en Docker Compose | Captura del panel UFVV con datos ficticios y build actual |
| PostgreSQL y Redis internos | Ejecutables en red privada de Compose | Captura `docker compose ps` y prueba de que no publican puertos al host |
| Inventario educativo y BIA | Matrices redactadas como supuestos | Exportar/adjuntar acta de validación (imposible para una universidad ficticia) y explicar supuesto |
| Riesgos, matriz y tratamientos | Matriz CSV creada; pantalla de la app conserva matriz 5×5 | Importar riesgos o documentar CSV como fuente oficial; validar dueños y fechas ficticias |
| NIST CSF 2.0 y IAM/MFA | Módulo NIST, roles y opción TOTP existen | Captura de MFA activada con secretos/códigos ocultos; demostrar revisión de acceso |
| Azure Blob | Bicep y scripts escritos, sin despliegue | Iniciar sesión, desplegar con créditos, capturar RBAC y cuenta sin claves/anónimos |
| Respaldo cifrado local | Script y runbook existentes; el perfil es opcional | Crear copia, verificar SHA-256, descifrar/restaurar en proyecto aislado y medir RPO/RTO |
| Respaldo externo Azure | Script `upload-backup.ps1`, no ejecutado | Subir solo backup cifrado, comparar hash, capturar operación Blob y consumo de crédito |
| SIEM/EDR e IDS/IPS | Decisión documentada; no integrado en Compose | Desplegar Wazuh/Suricata en equipo de laboratorio suficiente y generar alerta de prueba real |
| MDM/DLP | Política y controles de diseño | Enrolar dispositivo de prueba/licencia aprobada y mostrar solo resultado anonimizado; si no hay licencia, dejarlo como diseñado |
| NGFW, VLAN, DMZ, VPN | Diseño conceptual; no hay configuración física o virtual en el repo | Instalar firewall de laboratorio, capturar reglas y ejecutar prueba positiva/negativa por segmento |
| Continuidad y Data Center | BCP/DRP y lista de verificación de diseño | Simulacro real cronometrado y evidencia física; no afirmar rating o certificación TIA-942 |
| Gobierno COBIT/ITIL | Modelo de funciones y métricas propuesto | Aprobar RACI, crear catálogo/SLA/tickets/actas de comité y calcular métricas |
| Reporte y presentación | `informe-final.md` y `presentacion.md` | Completar autor/equipo, curso y docente; adaptar el guion a la plantilla requerida por el curso |

## Formato mínimo por evidencia

Cada archivo debe tener código (EV-##), fecha y hora, fuente, control/riesgo asociado, responsable, breve resultado, redacción de datos sensibles y hash SHA-256 cuando sea exportación. La evidencia debe ser repetible y mostrar el resultado observado. No se incluyen contraseñas, tokens, claves, datos personales reales, identificadores reales de estudiantes o información de proveedores.

## Dependencias frontend

Se aplicaron actualizaciones compatibles y el salto a Vitest 5. La instalacion y el build Docker del 2026-11-23 reportaron 0 vulnerabilidades en npm audit; falta guardar el reporte como evidencia versionada y mantener escaneo continuo en CI. La suite de pruebas no se ejecuto.

## Evidencias preliminares del repositorio

`docs/video_securecommerce/screens` contiene capturas previas de la interfaz de la plataforma heredada. No las presentes como controles de la UFVV porque no son evidencia del contexto académico actualizado. Los reportes en `backend/output/pdf` también pertenecen a la aplicación anterior hasta regenerarlos con el tenant UFVV. No se alteran capturas para que parezcan configuraciones cloud, SIEM, MDM o firewall.

