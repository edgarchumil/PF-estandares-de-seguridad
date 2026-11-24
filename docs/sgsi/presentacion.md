# Presentación: Centro de Gestión de Seguridad de la Información (CGSI)

**Duración sugerida:** 8–10 minutos · **10 diapositivas**  
Personalizar portada con autor/equipo, curso, docente y fecha de entrega.

## 1. Portada

**Diseño e implementación académica de un SGSI**  
Universidad Ficticia del Valle Verde · Centro de Gestión de Seguridad de la Información (CGSI)
Autor/equipo · Curso · Docente · Fecha

## 2. Problema y contexto

- Universidad ficticia, dos sedes, 4,500 estudiantes y 450 colaboradores.
- Registro, LMS, identidad, finanzas e investigación dependen de servicios digitales.
- Fallas, ransomware o exposición de expedientes afectan continuidad académica y confianza.
- Cifras y riesgos son supuestos académicos, no datos de una entidad real.

## 3. Alcance y gobierno

- Alcance: procesos académicos y de apoyo, aplicaciones, información, usuarios, proveedores y TI.
- Rectoría patrocina; Comité prioriza y acepta riesgos autorizados.
- Seguridad coordina; TI opera; dueños de proceso clasifican y validan información.
- 20 activos; Registro y LMS tienen prioridad de recuperación.

## 4. Marcos integrados

Visual sugerido: ISO 27001 como sistema de gestión; 27002 como controles; 27005/NIST 800-30 para riesgo; CSF 2.0 para resultados; OCTAVE Allegro como revisión cualitativa; COBIT e ITIL para gobierno/operación; ISO 22301 para continuidad; TIA-942-C para diseño del DC.

- Aplicación adaptada al caso; no equivale a auditoría o certificación.

## 5. Arquitectura híbrida

- Local: frontend/API, PostgreSQL, Redis y worker en Docker Compose.
- Respaldo cifrado del lado local; Azure Blob privado con TLS, Entra ID y RBAC.
- Copia y hash se verifican; IaC Bicep y scripts preparados.
- No hay despliegue Azure, VPN privada, SIEM ni segmentación física demostrada.

Visual sugerido: host local → backup cifrado → endpoint Blob autenticado; marcar “preparado, pendiente de despliegue”.

## 6. BIA: procesos prioritarios

- Registro/calificaciones: RTO 4 h, RPO 1 h (objetivos preliminares).
- LMS/clases: RTO 4 h, RPO 1 h.
- Identidad: RTO 4 h, RPO 1 h.
- Finanzas: RTO 8 h, RPO 4 h.
- Validar impactos, MTPD y objetivos con dueños de proceso.

## 7. Riesgos prioritarios

- Phishing y robo de credenciales.
- Ransomware y pérdida de disponibilidad.
- Exposición de expediente académico.
- Falla del respaldo o del proveedor cloud.
- Privilegios excesivos y cambios no controlados.

Controles: MFA, mínimo privilegio, parches, segmentación, logs, copias aisladas, restauración y respuesta coordinada. Puntaje 1–25 orienta prioridad; residual es estimado, no medido.

## 8. Políticas y controles

- Identidades, acceso, clasificación y retención.
- Dispositivos y BYOD; uso aceptable.
- Proveedores y servicios nube.
- Logs e incidentes; continuidad y respaldos.
- 25 controles ISO 27002 mapeados a riesgos, responsables, indicadores y evidencia.
- Aprobación por Rectoría y responsables aún pendiente.

## 9. Continuidad y Data Center

- BCP/DRP con prioridades, responsables, escalamiento y restauración limpia.
- Diseño objetivo alineado a criterios TIA-942-C Rated-2; no existe certificación.
- Brecha concreta: respaldo diario actual no cumple RPO de 1 hora.
- Próximo paso: aumentar frecuencia, probar restauración y medir RTO/RPO.

## 10. Plan y conclusión

- 0–30 días: aprobar alcance, roles, criterios y corrección de respaldo.
- 31–60 días: despliegue Blob por el propietario, hash y recuperación aislada.
- 61–90 días: simulacro, métricas, evidencias y reevaluación de riesgo.
- Azure for Students con límite de gasto; Blob consume créditos y no es gratuito garantizado.
- Entregables completos como diseño y prototipo; cerrar con pruebas observadas y revisión legal.

### Referencias breves

ISO/IEC 27001/27002/27005, ISO 22301, NIST CSF 2.0 y SP 800-30, COBIT 2019, ITIL 4, TIA-942-C, Microsoft Azure for Students. Referencias APA y enlaces oficiales en el informe.
