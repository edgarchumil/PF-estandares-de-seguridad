# Discusión académica y referencias

## 10.1 Zero Trust en nube pública y arquitectura híbrida

En nube pública, el proveedor opera la infraestructura física y ofrece controles centralizados de identidad, políticas de recursos, telemetría y cifrado; la universidad sigue siendo responsable de cuentas, datos, permisos, aplicación y recuperación. En el entorno híbrido, las decisiones deben cubrir identidad y postura de dispositivos tanto en campus como fuera de él, aplicaciones legacy, endpoints, administración local, red física y conectividad hacia Azure. La ubicación dentro del campus no concede confianza: se autentica y autoriza por recurso, sesión y contexto. Para mantener el costo de laboratorio bajo, la UFVV inicia una conexión HTTPS autorizada hacia Blob; no instala VPN Gateway ni Private Endpoint. Esto protege transferencia y permisos, aunque no crea conectividad privada ni elimina la exposición de un endpoint público.

## 10.2 MDM y DLP para dispositivos móviles

El dispositivo se registra antes de acceder a correo o expediente y debe demostrar sistema soportado, cifrado, bloqueo, parcheo y protección endpoint. MDM separa datos institucionales, permite revocar sesiones y borrar el espacio de trabajo; BYOD recibe un perfil limitado y un aviso claro sobre la telemetría que puede ver la universidad. DLP aplica etiquetas y reglas a correo, nube, portapapeles, impresión y medios extraíbles; bloquea o justifica exportaciones de expedientes y deja rastro de incidentes. La UFVV revisa falsos positivos y accesibilidad y conserva excepciones con vencimiento. Ni una política escrita ni la existencia de un campo “móvil” demuestra enrolamiento real.

## 10.3 Cumplimiento local e internacional

Antes de procesar información real, la UFVV debe identificar si es privada o pública, qué datos personales y sensibles trata, su propósito, retención, destinatarios, proveedores y transferencias internacionales. En Guatemala, los registros del Congreso consultados muestran propuestas legislativas de protección de datos personales en discusión; una iniciativa no es por sí misma ley vigente. Asesoría Jurídica debe comprobar el estado normativo en la fecha de tratamiento y obligaciones especiales de la institución. Si hay estudiantes o datos sujetos a reglas extranjeras (por ejemplo, personas de la Unión Europea), se identifican las normas y garantías aplicables a ese tratamiento y al proveedor cloud, sin asumir que seleccionar una región de Azure basta para cumplirlas. Contratos, derechos de titulares, retención, notificación de incidentes, subencargados y borrado deben constar antes de cargar datos reales. Este apartado informa el análisis académico y no constituye asesoría legal.

## 10.4 SIEM, EDR y XDR frente a mecanismos tradicionales

Un antivirus tradicional bloquea firmas o comportamientos en un endpoint y syslog conserva eventos con búsqueda limitada. EDR agrega telemetría, línea temporal, aislamiento y respuesta por endpoint. Un SIEM recibe registros de identidad, red, aplicación y endpoint, normaliza y correlaciona eventos con reglas y alertas. XDR correlaciona señales en varios dominios y coordina respuesta desde una plataforma integrada. La combinación puede acortar detección y contención, pero requiere fuentes de datos completas, reglas mantenidas, personal, reloj confiable y pruebas; comprar una herramienta no garantiza que un incidente se detecte. La arquitectura UFVV propone Wazuh/Suricata para laboratorio y los registra como pendientes de despliegue.

## 10.5 Mejora continua tras una certificación ISO/IEC 27001

La certificación sería un estado verificable con alcance y fecha, no una conclusión de que el riesgo desapareció. La UFVV mantendría contexto, objetivos, riesgos, SoA, auditorías internas, revisión directiva, incidentes, métricas, no conformidades y acciones correctivas. Los cambios en matrícula, servicios, nube, proveedores y legislación reabren la evaluación; ejercicios BIA/DR y revisión de privilegios comprueban eficacia. Las lecciones se traducen en recursos, cambios controlados y nueva medición antes de aprobar la siguiente revisión.

## 10.6 COBIT 2019 e ITIL 4

COBIT ayuda a Dirección a gobernar prioridades, apetito de riesgo, recursos, desempeño y cumplimiento mediante objetivos como EDM03, APO12, APO13, DSS04 y MEA03. ITIL 4 vuelve ejecutables esos objetivos en el catálogo, gestión de incidentes, cambios, problemas, niveles de servicio, configuración, activos y continuidad. Para UFVV, el objetivo COBIT DSS04 requiere que TI pruebe el DRP; la práctica ITIL de Service Continuity Management define plan, responsables, runbook y resultados de la prueba. Una matriz de objetivos, prácticas, responsables, indicadores y evidencia hace trazable el gobierno al servicio que recibe el estudiante.

## Referencias (APA 7.ª edición)

Caralli, R. A., Stevens, J. F., Young, L. R., & Wilson, W. R. (2007). *Introducing OCTAVE Allegro: Improving the information security risk assessment process* (CMU/SEI-2007-TR-012). Software Engineering Institute, Carnegie Mellon University. https://doi.org/10.1184/R1/6574790.v1

International Organization for Standardization. (2019). *ISO 22301:2019 Security and resilience—Business continuity management systems—Requirements* (incluye Amendment 1:2024). https://www.iso.org/standard/75106.html

International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection—Information security management systems—Requirements* (Amendment 1:2024). https://www.iso.org/standard/27001.html

International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection—Information security controls*. https://www.iso.org/standard/75652.html

International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection—Guidance on managing information security risks*. https://www.iso.org/standard/80585.html

International Organization for Standardization. (2024). *ISO 22301:2019/Amd 1:2024 Security and resilience—Business continuity management systems—Requirements—Amendment 1: Climate action changes*. https://www.iso.org/standard/88412.html

ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. https://www.isaca.org/resources/cobit

Microsoft. (s. f.). *Azure for Students*. Microsoft Learn. Recuperado el 23 de noviembre de 2026, de https://learn.microsoft.com/azure/education-hub/about-azure-for-students

National Institute of Standards and Technology. (2012). *Guide for conducting risk assessments* (NIST Special Publication 800-30 Rev. 1). https://doi.org/10.6028/NIST.SP.800-30r1

National Institute of Standards and Technology. (2020). *Zero trust architecture* (NIST Special Publication 800-207). https://doi.org/10.6028/NIST.SP.800-207

National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST Cybersecurity White Paper 29). https://doi.org/10.6028/NIST.CSWP.29

National Institute of Standards and Technology. (2025). *Incident response recommendations and considerations for cybersecurity risk management: A CSF 2.0 community profile* (NIST Special Publication 800-61 Rev. 3). https://doi.org/10.6028/NIST.SP.800-61r3

PeopleCert. (s. f.). *ITIL 4 practices*. Recuperado el 23 de noviembre de 2026, de https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1

Telecommunications Industry Association. (2024). *ANSI/TIA-942-C data center infrastructure standard*. https://tiaonline.org/resource/tia-942-c-data-center-infrastructure-standard/

Congreso de la República de Guatemala. (2025, 8 de julio). *Iniciativa que dispone aprobar Ley de Protección de Datos Personales (Iniciativa 6572)*. https://www.congreso.gob.gt/detalle_pdf/iniciativas/6256

Congreso de la República de Guatemala. (2026, 16 de julio). *Protección de información digital sigue causando discusión*. https://www.congreso.gob.gt/noticias_congreso/16492/2026/3

## Nota de vigencia

La referencia de continuidad usa ISO 22301:2019 con su enmienda 2024; ISO informa que una revisión de la norma está en desarrollo. Verifica edición y estado antes de entregar. El registro legislativo guatemalteco cambia con el tiempo; Jurídica debe verificar fuentes oficiales antes de utilizar el documento para una institución real.
