# Escenario y alcance del SGSI

## Organización ficticia

La Universidad Ficticia del Valle Verde (UFVV) es una institución privada sin fines de lucro ubicada en Quetzaltenango, Guatemala. Para este caso se supone que atiende a 4,500 estudiantes y 450 docentes y colaboradores en dos campus. Imparte carreras presenciales e híbridas y utiliza sistemas propios para expedientes y calificaciones, un LMS, correo institucional, biblioteca digital, identidad, pagos y redes de campus. La organización, cifras y servicios son ficticios.

La Dirección General patrocina el SGSI. La Dirección de TI opera un equipo supuesto de 12 personas: infraestructura, desarrollo, soporte, seguridad y continuidad. Las unidades de Registro Académico, Docencia, Finanzas, Recursos Humanos, Biblioteca, Asesoría Jurídica y proveedores de nube son dueños o custodios de información y servicios. Los grupos de usuarios son estudiantes, docentes, administrativos, TI, directivos, terceros y visitantes.

## Problema y objetivos

La interrupción del sistema académico o la exposición de expedientes, calificaciones, identificadores y documentos podría detener clases y matrícula, vulnerar la confianza institucional y activar obligaciones contractuales o legales. El SGSI busca proteger confidencialidad, integridad y disponibilidad mediante gobierno, evaluación de riesgos, controles verificables, continuidad y mejora periódica.

### Objetivo general

Diseñar e implementar de forma demostrable un SGSI basado en riesgos para proteger los servicios académicos y la información de la UFVV, mediante controles organizativos y tecnológicos y una arquitectura híbrida de campus y nube pública.

### Objetivos específicos

1. Definir el contexto, las partes interesadas, los procesos críticos y los límites del SGSI.
2. Inventariar activos y dependencias, y estimar impactos de interrupción mediante BIA.
3. Analizar riesgos con NIST SP 800-30 y priorizar escenarios mediante OCTAVE Allegro.
4. Seleccionar controles de ISO/IEC 27001 y 27002 vinculados a riesgos y responsables.
5. Aplicar Zero Trust, IAM, MFA, segmentación, registros, respuesta, protección de datos y controles de dispositivos.
6. Diseñar continuidad, recuperación y el cuarto de servidores con referencias ISO 22301 y ANSI/TIA-942-C.
7. Asignar gobierno de TI y gestión de servicios usando COBIT 2019 e ITIL 4.
8. Separar evidencia de controles desplegados de diseños, propuestas y supuestos académicos.

## Alcance propuesto

El SGSI cubre los procesos de matrícula, expediente y calificaciones; aprendizaje virtual; identidad y correo; red de campus; finanzas y nómina; biblioteca digital; soporte de TI; gestión de proveedores; respaldos y recuperación. Incluye las personas, instalaciones, estaciones, dispositivos móviles, aplicaciones, bases de datos, red y sala de servidores que soportan esos procesos en ambos campus, además del almacenamiento de copias cifradas en Azure.

El límite tecnológico local comprende el firewall de campus, las VLAN de usuario, servidores de virtualización y contenedores, proxy inverso, API, base de datos, caché, servicio de respaldo y consola de gestión. El límite cloud comprende la suscripción educativa Azure, control de acceso Microsoft Entra, una cuenta de Azure Blob Storage y su contenedor privado de respaldos. La conexión de datos del campus con Blob usa HTTPS saliente y autorización Entra; una VPN dedicada queda fuera del plan gratuito y no se declara instalada.

Se excluyen del alcance los sistemas personales no administrados que no accedan a información institucional; se les aplican las reglas BYOD y acceso de bajo privilegio. Los proveedores quedan bajo evaluación, contrato y evidencias de sus controles, sin asumir que el proveedor transfiere a la universidad la responsabilidad sobre su información.

## Partes interesadas y obligaciones

| Parte interesada | Necesidad o expectativa | Evidencia requerida |
|---|---|---|
| Estudiantes | Confidencialidad de expediente y continuidad de clases | Avisos, acceso controlado, incidentes y continuidad |
| Docentes | Disponibilidad de LMS y registro íntegro de calificaciones | RTO/RPO, control de cambios y revisión de permisos |
| Dirección | Riesgos aceptados, gasto y desempeño del SGSI | Acta de revisión, indicadores y registro de riesgos |
| Personal administrativo | Acceso por función y protección de documentos | IAM, MFA, formación y políticas |
| TI y seguridad | Responsabilidades, inventario, herramientas y escalamiento | Procedimientos, bitácoras, controles y runbooks |
| Proveedores | Reglas de acceso, notificación y devolución/borrado de datos | Contratos, evaluación y revisión anual |
| Autoridades y terceros | Cumplimiento aplicable y cooperación ante incidentes | Matriz legal validada por asesoría jurídica |

## Política de evaluación del riesgo

Se usa una escala didáctica de probabilidad e impacto de 1 a 5. El puntaje es P × I y se agrupa en 1–4 bajo, 5–9 medio, 10–16 alto y 17–25 crítico. Una persona responsable del riesgo aprueba la aceptación residual; el equipo que implementa el control no puede aceptar por sí solo el riesgo. Los umbrales y niveles BIA aquí propuestos requieren aprobación de Dirección.

## Clasificación de información

| Clase | Ejemplos | Regla mínima |
|---|---|---|
| Pública | Oferta académica publicada | Revisión de publicación y control de integridad |
| Interna | Procedimientos, calendarios y material interno | Acceso autenticado y distribución institucional |
| Confidencial | Expedientes, calificaciones, nómina y contratos | Mínimo privilegio, cifrado, registro, retención y eliminación controlada |
| Restringida | Credenciales, secretos, claves criptográficas y datos especialmente sensibles | Acceso nominal estrictamente limitado, MFA, almacenamiento protegido y monitoreo reforzado |

## Supuestos y límites

Los conteos, escalas, impactos, tiempos de recuperación y escenarios de amenazas son hipótesis para un ejercicio académico; no son entrevistas, mediciones de la UFVV ni evidencia de auditoría. La universidad ficticia carece de contratos y expedientes reales. No se declara certificación ISO, rating TIA-942 ni cumplimiento legal. Las decisiones que dependen de una institución real deben validarse con dueños de proceso, asesoría jurídica, TI y Dirección.
