# Evaluación cualitativa OCTAVE Allegro

## Método y límites

Se aplica OCTAVE Allegro como taller cualitativo centrado en activos de información y su contexto, complementario a la matriz cuantitativa de NIST SP 800-30. El proceso recorre sus ocho actividades: establecer criterios de medición; desarrollar perfiles de activos; identificar contenedores; identificar áreas de preocupación; definir escenarios de amenaza; identificar riesgos; analizar riesgos; y seleccionar mitigaciones.

Esta primera iteración es un ejercicio de escritorio construido a partir del escenario ficticio; no hubo talleres con empleados reales. La Dirección debe confirmar los criterios de impacto, dueños, amenazas y compromisos de tratamiento antes de tomar decisiones operativas.

## Criterios de impacto

Las consecuencias se valoran como bajo, moderado, alto o crítico según el perjuicio a la misión académica, privacidad, obligaciones, confianza y costo de recuperación. El impacto alto o crítico en integridad de calificaciones, disponibilidad de matrícula o confidencialidad de expedientes eleva la prioridad aunque un cálculo económico sea impreciso. La tolerancia institucional propuesta es cero para modificación deliberada de calificaciones y divulgación no autorizada de expedientes.

## Perfil de activos críticos

| Activo de información | Valor institucional | Dueño | Contenedores |
|---|---|---|---|
| Expediente y calificaciones | Inscripción, progresión y certificación académica | Registro Académico | SIS, PostgreSQL, estaciones Registro, respaldos |
| Identidades, credenciales y sesiones | Acceso a todos los servicios | Dirección TI | Directorio, app, Entra del operador, autenticadores |
| Cursos y evaluaciones | Docencia presencial e híbrida | Dirección Académica | LMS, laptops docentes, copias de curso |
| Copias de recuperación | Restauración verificable de procesos críticos | Dirección TI | Backup local cifrado y Azure Blob propuesto |
| Registros y evidencias | Detección, atribución, auditoría y defensa | Responsable SGSI | AuditLog, SIEM propuesto, repositorio de evidencia |

## Escenarios priorizados

| Escenario de amenaza | Consecuencia | Riesgo relacionado |
|---|---|---|
| Docente abre enlace de phishing y el atacante reutiliza la sesión | Cambio de notas, acceso a expedientes, pérdida de confianza | R-01, R-05 |
| Ransomware alcanza las bases y copias montadas | Interrupción de SIS/LMS y pérdida de disponibilidad e integridad | R-02, R-03 |
| Contenedor de respaldo queda expuesto o cuenta Azure se compromete | Divulgación de expedientes y secretos | R-06 |
| Corte eléctrico o de conectividad afecta la sala de servidores | Clases, matrícula e identidad indisponibles | R-08 |
| Laptop docente se pierde sin cifrado o borrado remoto | Copia local de información académica expuesta | R-07 |
| Cambio de firewall mezcla administración, estudiantes y servidores | Movimiento lateral y acceso a activos críticos | R-10 |

## Resultados y decisiones

Las acciones de mayor prioridad son hacer obligatoria MFA para personal, separar copias del dominio operativo, reducir privilegios de Registro y administración, verificar restauración, proteger dispositivos móviles y asignar presupuesto a infraestructura de continuidad. R-01, R-02, R-06 y R-08 tienen puntaje inherente crítico (20, 20, 15 y 20 según la matriz cuantitativa); los valores residuales son objetivos de tratamiento y no resultados probados.

La evaluación se repite después de cambios de arquitectura, incidentes importantes, cambios de proveedor y cada ciclo académico. La actualización debe dejar fecha, participantes, propietario del activo, evidencia revisada, criterio de impacto y aprobación de Dirección.
