# Diseño del Sistema de Gestión de Seguridad de la Información de la Universidad Ficticia del Valle Verde

**Sistema:** Centro de Gestión de Seguridad de la Información (CGSI)
**Versión:** 1.0 · 23 de noviembre de 2026  
**Tipo de trabajo:** diseño académico con prototipo local y preparación de arquitectura híbrida  
**Autor/equipo:** completar por el estudiante  
**Curso/docente:** completar por el estudiante

> **Carácter del caso.** UFVV, su matrícula, personal, procesos, activos, riesgos, tiempos y costos estimados son supuestos académicos ficticios. Este documento no es una auditoría ni una certificación. Distingue diseño, prototipo local y controles pendientes de evidencia. No contiene datos reales de estudiantes.

## Resumen ejecutivo

Este proyecto adapta una plataforma de gestión de seguridad a un escenario de educación superior y establece un SGSI para la Universidad Ficticia del Valle Verde (UFVV), institución privada ficticia situada en Quetzaltenango, Guatemala, con dos sedes, 4,500 estudiantes y 450 colaboradores como parámetros de diseño. Se cubren Registro Académico, aprendizaje virtual, identidad, investigación, recursos humanos, finanzas y servicios de TI.

El alcance propone proteger la información, los servicios digitales y la infraestructura que los soporta. El modelo integra ISO/IEC 27001:2022 y 27002:2022, gestión de riesgos basada en ISO/IEC 27005:2022 y NIST SP 800-30, funciones de NIST CSF 2.0, OCTAVE Allegro como método complementario, gobierno COBIT 2019, prácticas ITIL 4 y continuidad ISO 22301:2019. TIA-942-C se usa como referencia de diseño de centro de datos, no como afirmación de certificación.

La solucion tecnologica mantiene la aplicacion, PostgreSQL y Redis en Docker Compose local, con redes de servicio separadas y respaldo cifrado preparado para Azure Blob. La plantilla y los scripts estan listos; no se creo recurso remoto. Solo se permite desplegar si el portal confirma la cuota gratuita, sin consumir el saldo de creditos; si no califica, se mantiene el respaldo local/externo cifrado de laboratorio.

Los análisis entregables incluyen inventario de 20 activos, BIA de 10 procesos, 15 escenarios de riesgo con tratamientos propuestos, 27 controles trazados y políticas institucionales. El análisis identifica una brecha prioritaria: la copia diaria predeterminada no cumple el RPO de una hora asignado al SIS y LMS. Los objetivos RTO/RPO son hipótesis de planificación y requieren validación y pruebas cronometradas.

## 1. Introducción

La universidad depende de servicios digitales para inscripción, calificaciones, clases, identidad, investigación y pagos. La interrupción de estos servicios puede afectar la continuidad académica y la confidencialidad de información personal. La adopción de una herramienta técnica aislada no sustituye gobierno, asignación de responsabilidades, evaluación de impacto, tratamiento de riesgos ni mejora continua.

Este trabajo define un sistema de gestión aplicable al caso académico, adapta el prototipo SecureCommerce heredado al Centro de Gestión de Seguridad de la Información (CGSI) y organiza los documentos necesarios para evaluar riesgos, escoger controles, proponer continuidad y preparar una arquitectura híbrida de bajo costo. Las decisiones basadas en supuestos están identificadas para evitar presentarlas como hechos verificados.

## 2. Objetivos y alcance

### Objetivo general

Diseñar y preparar la implementación demostrable de un SGSI para los procesos académicos y de apoyo de UFVV, con controles trazables a marcos reconocidos, continuidad de servicios y arquitectura local-híbrida compatible con Azure for Students.

### Objetivos específicos

1. Definir contexto, partes interesadas, límites del SGSI y criterios de clasificación.
2. Identificar activos y procesos críticos y establecer impactos, MTPD, RTO y RPO preliminares.
3. Evaluar escenarios de riesgo, seleccionar tratamientos y mapear controles a marcos.
4. Establecer políticas de identidad, dispositivos, uso aceptable, proveedores, datos, registro, incidentes y respaldo.
5. Diseñar continuidad, recuperación y requisitos objetivo del centro de datos.
6. Adecuar el prototipo y preparar IaC y procedimientos sin crear recursos facturables.

El alcance cubre los sistemas de información, personas, procesos, proveedores y servicios que soportan Registro Académico, LMS, identidad, investigación, recursos humanos, finanzas y TI en dos sedes ficticias. Excluye de la implementación demostrada los sistemas físicos de campus, plataformas SaaS no controladas, la operación de un centro de datos certificado y cualquier dato personal real. Los límites, exclusiones y partes interesadas se amplían en [00-escenario-y-alcance.md](00-escenario-y-alcance.md).

## 3. Enfoque y métodos

Se usó análisis documental y modelado de escritorio, con supuestos explícitos para una institución ficticia. El inventario asigna propietario, custodio, ubicación y necesidades de confidencialidad, integridad y disponibilidad. El BIA estima impacto por proceso y objetivos de recuperación. La evaluación NIST SP 800-30 usa probabilidad e impacto en escala de 1 a 5; la puntuación es P×I y los niveles orientan prioridad. La matriz registra escenario, activo, amenaza, vulnerabilidad, controles existentes o propuestos, riesgo inherente, tratamiento, responsable y riesgo residual previsto.

OCTAVE Allegro aporta una revisión cualitativa centrada en activos de información y contenedores; no se realizaron entrevistas ni talleres con personal real. Los controles se seleccionaron mediante ISO/IEC 27002:2022 y se relacionaron con riesgos, responsables, métricas y evidencia esperada. NIST CSF 2.0 organiza resultados por gobernar, identificar, proteger, detectar, responder y recuperar. COBIT 2019 e ITIL 4 se aplican a decisiones de gobierno y operación. ISO 22301 orienta continuidad. TIA-942-C informa requisitos de infraestructura física del DC objetivo.

La correspondencia entre controles de diferentes marcos es una adaptación funcional; no constituye equivalencia formal, evaluación de conformidad ni certificación. Véanse los criterios completos en [05-octave-allegro.md](05-octave-allegro.md), [06-controles.csv](06-controles.csv), [09-gobierno-y-servicios.md](09-gobierno-y-servicios.md) y [11-discusion-y-referencias.md](11-discusion-y-referencias.md).

## 4. Organización, gobierno y activos

UFVV se define como universidad privada ficticia de dos sedes. La Rectoría patrocina el SGSI; el Comité de Seguridad aprueba prioridades y acepta riesgos dentro de su autoridad; el responsable de seguridad coordina el sistema; TI opera infraestructura e identidad; Registro Académico, Docencia, Finanzas, Recursos Humanos, Investigación y Biblioteca son propietarios de sus procesos y datos. Proveedores y responsables de privacidad participan cuando corresponda.

La clasificación propuesta es pública, interna, confidencial y restringida. Los registros académicos y las credenciales se consideran restringidos; procedimientos internos y telemetría se protegen según contenido. La matriz de inventario contiene 20 activos, incluidos SIS, LMS, directorio, base de datos académica, estaciones administrativas, red, respaldos, biblioteca digital y proveedor de pagos. Cada propietario debe validar clasificación, retención, dependencias y acceso.

El prototipo ofrece módulos de inventario, evaluación NIST, riesgos, incidentes, auditoría y reportes. El seed crea o actualiza UFVV y conserva las demás organizaciones registradas como tenants independientes. El selector muestra las organizaciones activas para las que la cuenta tiene membresía; tras la carga se debe cerrar sesión y volver a ingresar para renovar la lista.

## 5. Arquitectura híbrida propuesta

El entorno local usa Docker Compose para frontend/API, worker, PostgreSQL, Redis y perfil opcional de respaldo. La base de datos y Redis permanecen en la red privada de Compose sin publicar puertos de host en el diseño. El perímetro físico se segmentaría en administración, servidores, personal, estudiantes, móviles y visitantes; estas VLAN y reglas son un diseño y no una configuración desplegada.

La arquitectura hibrida propuesta usaria Azure Blob Storage Standard LRS Hot, un contenedor privado, HTTPS/TLS 1.2, acceso anonimo y Shared Key deshabilitados, y acceso OAuth/RBAC. Versionado, retenciones y Change Feed quedan desactivados para limitar operaciones y almacenamiento. La cuota gratuita publicada es de 5 GB LRS Hot, 20,000 lecturas y 10,000 escrituras por mes durante 12 meses para cuentas elegibles nuevas; el titular debe confirmar que su suscripcion califica. La plantilla no se despliega hasta confirmar esa cuota. El script limita carga total a 4.5 GB. La cuenta mantiene endpoint de servicio publico autenticado; no se afirma conectividad privada o VPN.

El diseño excluye VM permanente, VPN Gateway, NAT Gateway, firewall administrado, Private Endpoint, licencias premium y servicios Marketplace. Azure for Students ofrece creditos educativos y algunas cuotas gratuitas con elegibilidad y limites; este proyecto solo autoriza Blob dentro de una cuota que se confirme gratuita en el portal. No consumir creditos para este despliegue. No usar datos reales de estudiantes sin evaluacion, autorizacion y revision de transferencia internacional.

El diagrama de flujos, zonas y controles está en [01-arquitectura-hibrida.md](01-arquitectura-hibrida.md); el plan de costos y pasos operativos está en [plan-azure.md](plan-azure.md).

## 6. BIA y objetivos de recuperación

El BIA prioriza Registro Académico y calificaciones, LMS y clases, identidad, finanzas, recursos humanos, investigación y biblioteca. Cada proceso registra impactos en operación, cumplimiento, reputación, seguridad física y enseñanza. El MTPD es el máximo tiempo estimado de interrupción antes de daño inaceptable; RTO es el tiempo objetivo para reanudar; RPO es la pérdida de datos máxima objetivo expresada en tiempo. Los valores del archivo [03-bia.csv](03-bia.csv) son supuestos académicos que deben aprobarse con dueños de proceso.

Para Registro y LMS se propone RTO de 4 horas y RPO de 1 hora; identidad tiene RTO de 4 horas y RPO de 1 hora. Finanzas propone RTO de 8 horas y RPO de 4 horas. La copia diaria que entrega el perfil actual permite como máximo un punto diario antes del siguiente respaldo en el mejor caso; no demuestra el RPO de una hora. Se requiere respaldos más frecuentes o mecanismo incremental/WAL, almacenamiento separado, observabilidad y restauración medida. El RTO tampoco se considera satisfecho hasta completar un ejercicio cronometrado.

## 7. Evaluación y tratamiento de riesgos

La matriz [04-riesgos.csv](04-riesgos.csv) contiene 15 escenarios. Entre los prioritarios figuran robo de credenciales por phishing, ransomware en estación o servidor, indisponibilidad de SIS/LMS, exposición de expedientes, fallo de respaldo, compromiso de proveedor, abuso de privilegios, daño físico/eléctrico y error de cambio. El puntaje inherente permite ordenar atención; el residual indica expectativa después del tratamiento y no una medición observada.

Se recomienda mitigar con MFA resistente a phishing para roles críticos, mínimo privilegio y revisiones trimestrales, protección de endpoint y parches priorizados, copias cifradas e inmutables o aisladas, pruebas de restauración, gestión de cambios, segmentación, centralización de logs, respuesta coordinada y evaluación contractual de proveedores. La aceptación de riesgo debe tener dueño autorizado, justificación, controles compensatorios y fecha de expiración. Las fechas propuestas son planificadas, no evidencia de cumplimiento.

OCTAVE Allegro complementa la lista cuantificada con amenazas y contenedores de la información, pero requiere talleres con responsables de Registro, Docencia, TI, Jurídica y Finanzas para confirmar impactos, requisitos y escenarios.

La revision de dependencias frontend encontro inicialmente 19 avisos; se actualizaron paquetes compatibles y Vitest a la version 5.1.1. El build Docker posterior y la instalacion reportaron cero vulnerabilidades npm al 23 de noviembre de 2026. Se conserva el control de monitoreo continuo; la suite no se ejecuto.

## 8. Aplicación de estándares y controles

La matriz de controles selecciona 27 medidas de ISO/IEC 27002:2022 y las vincula a riesgos UFVV, propietarios, indicador y evidencia. Se priorizan políticas (A.5), responsabilidades y gestión de identidades (A.5.15–A.5.18), proveedores (A.5.19–A.5.23), incidentes (A.5.24–A.5.28), continuidad (A.5.29–A.5.30), clasificación/transferencia (A.5.12–A.5.14), configuración, acceso y respaldo (A.8), registro/monitoreo (A.8.15–A.8.16), vulnerabilidades y desarrollo seguro.

ISO/IEC 27001 define los requisitos del sistema de gestión y la mejora continua; la selección de controles debe formalizarse en una Declaración de Aplicabilidad con inclusión, justificación y estado tras aprobación. NIST CSF 2.0 sirve de perfil de resultados y conversación de brecha, NIST 800-30 soporta la evaluación, OCTAVE Allegro el análisis cualitativo, COBIT asigna gobierno, ITIL guía gestión de cambios/incidentes/continuidad, ISO 22301 guía continuidad y TIA-942-C guía diseño de infraestructura del DC.

## 9. Políticas y operación

El paquete [07-politicas.md](07-politicas.md) propone política general de seguridad, identidades y acceso, uso aceptable/BYOD, clasificación y protección de datos, endpoints, proveedores/nube, registros, respuesta a incidentes y continuidad/respaldos. La Rectoría debe aprobarlas; responsables nombrados deben comunicarlas y revisar al menos anual o ante cambio significativo. Los plazos de conservación se aprueban con Jurídica/Privacidad, no por valores genéricos del prototipo.

COBIT 2019 conecta apetito de riesgo, proveedores, seguridad, cambios, activos, incidentes, continuidad y monitoreo con objetivos institucionales. ITIL 4 organiza catálogo de servicios, niveles de servicio, cambios, activos/configuración, monitoreo, incidentes y mejora. El RACI documenta responsables; los SLA y métricas requieren datos operativos antes de fijar objetivos contractuales.

## 10. Continuidad y centro de datos

El [plan de continuidad](08-continuidad-y-datacenter.md) incluye activación, prioridades, roles, comunicaciones, recuperación técnica, dependencias, estrategias temporales y calendario de ejercicios. Los procedimientos deben practicar escenarios de ransomware, caída de identidad, indisponibilidad de campus, pérdida del proveedor y restauración de respaldo. La recuperación debe ser aislada y libre de malware antes de reconectar.

Para el DC objetivo se propone evaluar disponibilidad y mantenibilidad al nivel de diseño equivalente a TIA-942-C Rated-2, con rutas de energía y refrigeración, UPS/generador, control ambiental, detección/extinción de incendio, acceso físico, CCTV, monitoreo, mantenimiento, inventario y contratos de soporte. El proyecto no posee DC físico, equipo de infraestructura ni auditoría externa; no reclama rating, cumplimiento, certificación ni alta disponibilidad real.

## 11. Plan de implementación

### 0–30 días

Nombrar sponsor y Comité, validar alcance/activos con dueños de proceso, aprobar criterios de riesgo, corregir la cadencia de respaldo para el objetivo RPO, establecer MFA y control de privilegios para operadores, acordar clasificación y completar Declaración de Aplicabilidad inicial.

### 31–60 días

Desplegar el almacenamiento educativo tras consentimiento del titular, probar carga cifrada y hash, realizar restauración aislada cronometrada, establecer tickets de incidentes y cambios, centralizar logs disponibles y completar una revisión de proveedores y privacidad.

### 61–90 días

Ejecutar simulacro de continuidad, medir RTO/RPO, revisar accesos y vulnerabilidades, aprobar políticas pendientes, recopilar evidencias identificadas, reevaluar riesgos residuales y presentar un plan de mejora al Comité.

Las tareas dependen de disponibilidad de responsables, una cuota gratuita vigente y politicas de proveedor; ninguna fecha se presenta como ejecutada.

## 12. Discusión, límites y conclusiones

La arquitectura híbrida logra un equilibrio académico entre control local y réplica externa, pero el diseño no equivale a alta disponibilidad. Sin redes privadas en Azure, almacenamiento autenticado y cifrado previo reducen exposición accidental, mientras que la ubicación, disponibilidad del servicio, dependencia de credenciales y gasto de transacciones siguen siendo riesgos. Una estrategia local única puede quedar expuesta al ransomware; es necesario tener una copia desconectada o protegida contra borrado, y probarla.

La matriz P×I es sencilla y auditable para un proyecto de curso, pero no sustituye análisis de incertidumbre, pérdida monetaria, dependencia temporal ni criterios legales específicos. La escala es ordinal y sus puntuaciones no deben interpretarse como probabilidades estadísticas. La propuesta OCTAVE no contiene entrevistas. Impactos y objetivos BIA requieren aprobación real en una universidad operativa.

Para Guatemala se recomienda revisión legal de datos personales y transferencias antes de operar. Las referencias consultadas sobre iniciativas legislativas muestran propuestas registradas/debatidas, no permiten concluir una obligación legal vigente en este proyecto; validar estado actualizado con fuentes oficiales y asesoría local antes de implementación. ISO y TIA son fuentes protegidas; el proyecto no reproduce los textos normativos completos ni pretende certificación.

El trabajo deja una linea base academica coherente y un prototipo local denominado Centro de Gestión de Seguridad de la Información (CGSI), matrices de BIA/riesgo/controles, politicas, gobierno, continuidad, IaC y procedimientos de evidencia. La prioridad es materializar evidencia autentica: restauracion y tiempos, configuracion observada, pruebas de control, aprobacion institucional, elegibilidad/costo cero y ejercicio de continuidad. Hasta entonces, el estado es disenado o preparado, no certificado ni totalmente implementado.

## Referencias

Caralli, R. A., Stevens, J. F., Young, L. R., & Wilson, W. R. (2007). *Introducing OCTAVE Allegro: Improving the information security risk assessment process* (CMU/SEI-2007-TR-012). Software Engineering Institute, Carnegie Mellon University. https://doi.org/10.1184/R1/6574790.v1

International Organization for Standardization. (2019). *ISO 22301:2019 Security and resilience—Business continuity management systems—Requirements*. https://www.iso.org/standard/75106.html

International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security management systems—Requirements*. https://www.iso.org/standard/27001.html

International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security controls*. https://www.iso.org/standard/75652.html

International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Guidance on managing information security risks*. https://www.iso.org/standard/80585.html

ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. https://www.isaca.org/resources/cobit

Microsoft. (s. f.). *Azure for Students*. Microsoft Learn. https://learn.microsoft.com/azure/education-hub/about-azure-for-students

National Institute of Standards and Technology. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). https://doi.org/10.6028/NIST.SP.800-30r1

National Institute of Standards and Technology. (2020). *Zero trust architecture* (NIST SP 800-207). https://doi.org/10.6028/NIST.SP.800-207

National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29

National Institute of Standards and Technology. (2025). *Incident response recommendations and considerations for cybersecurity risk management: A CSF 2.0 community profile* (NIST SP 800-61 Rev. 3). https://doi.org/10.6028/NIST.SP.800-61r3

PeopleCert. (s. f.). *ITIL 4 practices*. https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1

Telecommunications Industry Association. (2024). *ANSI/TIA-942-C data center infrastructure standard*. https://tiaonline.org/resource/tia-942-c-data-center-infrastructure-standard/

Las seis respuestas del análisis académico, las referencias adicionales y la nota de vigencia legal y normativa están en [11-discusion-y-referencias.md](11-discusion-y-referencias.md).

## Anexos del expediente

- Inventario de activos: [02-inventario-activos.csv](02-inventario-activos.csv).
- BIA y objetivos de recuperación: [03-bia.csv](03-bia.csv).
- Registro de riesgos: [04-riesgos.csv](04-riesgos.csv).
- Evaluación OCTAVE Allegro: [05-octave-allegro.md](05-octave-allegro.md).
- Matriz de controles: [06-controles.csv](06-controles.csv).
- Políticas: [07-politicas.md](07-politicas.md).
- Continuidad y diseño DC: [08-continuidad-y-datacenter.md](08-continuidad-y-datacenter.md).
- Gobierno y operación: [09-gobierno-y-servicios.md](09-gobierno-y-servicios.md).
- Estado de evidencia: [10-evidencias-y-estado.md](10-evidencias-y-estado.md).
- Infraestructura Azure: [plan-azure.md](plan-azure.md) y `infrastructure/azure/`.
