# Políticas de seguridad de la información

**Propietario:** Dirección General. **Administrador:** Responsable SGSI. **Revisión:** anual y después de un incidente mayor o cambio sustancial. Estas políticas son una propuesta académica; requieren aprobación formal y comunicación antes de ser obligatorias.

## 1. Identidades, autenticación y privilegios

Cada persona recibe una identidad individual; se prohíben cuentas compartidas para trabajo ordinario. Recursos Humanos inicia altas, cambios y bajas; el dueño del proceso aprueba el rol y TI aplica el cambio. Personal, docentes y administradores usan MFA. Los administradores emplean cuentas separadas para tareas ordinarias y privilegiadas, privilegios temporales y una cuenta de emergencia sellada con revisión posterior. Las claves y códigos MFA no se comparten ni se incorporan a reportes, repositorios o capturas. Se revocan sesiones al finalizar una relación o ante sospecha de compromiso. Las membresías se revisan trimestralmente.

## 2. Equipos, hardening y parches

Solo dispositivos registrados pueden acceder a recursos administrativos. TI mantiene inventario de propietario, custodia, sistema operativo, cifrado, estado de parches y agente de protección. Los equipos institucionales usan configuración endurecida, bloqueo automático, antivirus/EDR, firewall local, cifrado de disco y actualización automática. Los parches críticos se evalúan en 72 horas y se aplican con prioridad según exposición y pruebas. Se prohíbe desactivar el agente, instalar software no autorizado o utilizar medios extraíbles sin aprobación. Los servidores se gestionan desde la VLAN administrativa mediante salto autenticado y MFA.

## 3. Uso aceptable, roles y acceso remoto

La información institucional solo se usa para tareas autorizadas. Estudiantes, docentes, administrativos, TI, dirección y terceros reciben permisos acordes a su función. Se prohíbe extraer listas de estudiantes a cuentas personales o compartir expedientes por mensajería no aprobada. El acceso remoto usa HTTPS, MFA y dispositivo conforme; no se publican SSH/RDP ni bases de datos a Internet. El acceso de proveedor tiene dueño, plazo de expiración, supervisión y ticket.

## 4. Dispositivos móviles y BYOD

Los teléfonos y laptops institucionales se enrolan en MDM antes de acceder a datos confidenciales. Se exige PIN robusto, cifrado, bloqueo automático, sistema soportado, parcheo y borrado remoto. Los datos institucionales deben permanecer en una aplicación o contenedor administrado; no se copian a almacenamiento personal. BYOD solo accede a vistas web limitadas y no descarga expedientes o calificaciones. TI puede revocar tokens y borrar el perfil institucional. La institución explica qué información recoge MDM y limita la telemetría al trabajo institucional.

## 5. Nube y proveedores

Antes de incorporar una plataforma cloud, el dueño evalúa propósito, datos, ubicación, retención, subencargados, autenticación, incidentes, respaldo, exportación y eliminación. Se usa Entra con MFA y RBAC por recurso; se prohíben contenedores anónimos, claves compartidas y secretos en Git. Los respaldos se cifran antes de abandonar el campus, se transmiten con TLS y se validan por hash. La suscripción educativa se conserva bajo límite de gasto; se eliminan recursos de prueba una vez capturada la evidencia. Asesoría Jurídica valida contratos y transferencias internacionales antes de cargar datos reales.

## 6. Clasificación, privacidad y DLP

El dueño etiqueta información pública, interna, confidencial o restringida y define usuarios, retención, transferencias y eliminación. Expedientes, notas y nómina se tratan como confidenciales; credenciales y secretos son restringidos. Se aplican reglas DLP para impedir copias a correo personal, USB y almacenamiento no aprobado. Como el caso solo usa datos sintéticos, ninguna captura demostrativa debe incluir personas, correo, tokens o datos reales. La revisión legal determina los avisos, derechos, retención y notificación de incidentes que correspondan al tipo de institución.

## 7. Registro, incidentes y respuesta

Se registran inicios de sesión, cambios de rol, exportaciones, acciones administrativas, alertas de endpoint, firewall, base de datos y almacenamiento. Los eventos se envían a un SIEM separado del sistema productivo con hora sincronizada y retención aprobada. El personal informa sospechas de phishing, pérdida de equipo o divulgación inmediatamente al canal de guardia. El responsable clasifica severidad, conserva evidencias, contiene accesos y coordina comunicaciones. El ticket incluye activo, hora, alcance, medidas, responsable y recuperación; los documentos de la defensa usan solo identificadores ficticios.

## 8. Respaldo, recuperación y destrucción

El backup de sistemas críticos se cifra en origen, se almacena en una cuenta separada del entorno de producción y se valida con hash. TI revisa diariamente el estado del trabajo. El objetivo propuesto para SIS es RPO 1 hora y RTO 2 horas; se considera alcanzado únicamente tras una prueba cronometrada y registrada. Se prueba restauración trimestral y continuidad anual. La destrucción de copias sigue la retención aprobada y verifica que no existan bloqueos legales; una retención inmutable solo se activa después de probar el ciclo de vida.

## Procedimiento de excepciones

La excepción debe indicar control afectado, razón, datos y activos expuestos, medidas compensatorias, riesgo residual, responsable y fecha de caducidad. El dueño del riesgo y el Responsable SGSI la elevan a Dirección cuando sea alto o crítico. No hay excepciones permanentes ni aceptación tácita por falta de presupuesto.

## Aprobación pendiente

| Aprobador | Rol | Estado |
|---|---|---|
| Rectoría de la UFVV | Aprobación de política y apetito de riesgo | Pendiente; entidad ficticia |
| Dirección de TI | Operación técnica | Pendiente |
| Asesoría Jurídica | Revisión legal y privacidad | Pendiente |
| Recursos Humanos | Comunicación, sanciones y formación | Pendiente |
