# Continuidad del negocio y diseño de centro de datos

## Estrategia de continuidad

El BIA prioriza identidad, matrícula/expedientes, LMS, calificaciones y red de campus. Los RTO/RPO son objetivos académicos supuestos y deben ser aprobados por dueños de proceso. El proyecto local demuestra el núcleo de aplicación y un mecanismo de respaldo cifrado; no demuestra conmutación física o recuperación cloud completa.

## Plan de continuidad (BCP)

| Interrupción | Activación | Continuidad mínima | Responsable |
|---|---|---|---|
| Indisponibilidad del SIS/LMS | Falla supera 30 min o amenaza integridad | Aviso por canal alterno; lista de estudiantes limitada; recepción diferida de tareas | Dueño del sistema y Dirección Académica |
| Corte eléctrico o de Internet | Interrupción confirmada en ambos enlaces o UPS bajo umbral | Mantener cargas críticas con UPS; failover de enlace; reducir servicios no académicos | Facilities y Dirección TI |
| Ransomware o cuenta comprometida | Indicador validado por seguridad o proveedor | Aislar segmentos, revocar tokens, preservar imagen/logs, activar respuesta | Responsable SGSI y administrador IAM |
| Fuga o exposición de respaldo | Acceso anónimo o actividad anómala confirmada | Revocar rol/SAS, bloquear exportaciones, evaluar alcance, proteger copia intacta | Operador Azure y Responsable SGSI |
| Sala local fuera de servicio | Riesgo físico o pérdida de energía prolongada | Activar recuperación temporal; restaurar primero identidad, SIS y LMS | Dirección TI y Rectoría |

## Plan de recuperación (DRP)

1. Declarar incidente y registrar autoridad, hora, servicios y alcance.
2. Aislar equipo afectado y preservar logs, hashes, respaldos y cadena de custodia.
3. Confirmar imagen limpia, cuenta administrativa y copia cifrada que se va a restaurar.
4. Recuperar primero DNS/red de administración e identidad; después base SIS, API y UI; luego LMS, correo y finanzas.
5. Validar integridad con recuentos, checksums, controles de rol, acceso por campus y prueba de negocio; el dueño acepta el servicio restaurado.
6. Comunicar estado a usuarios, documentar pérdida de datos real frente a RPO, medir RTO y registrar lecciones.

### Objetivos propuestos por proceso

Los tiempos se encuentran en [03-bia.csv](03-bia.csv). La copia programada actual se describe con cadencia diaria; por ello **no satisface el RPO de una hora previsto para SIS** hasta habilitar copias incrementales/log shipping o snapshots horarios y probarlos. Mientras eso no se implemente, la diferencia se mantiene como riesgo abierto. El uso de almacenamiento Azure no equivale a recuperación de cómputo: el ejercicio debe aprovisionar un host temporal y restaurar los datos.

## Calendario de pruebas

| Frecuencia | Ejercicio | Criterio de éxito |
|---|---|---|
| Mensual | Verificación de hash y legibilidad de backup | Hash coincide; archivo descifrable por dos custodios autorizados |
| Trimestral | Restaurar SIS/LMS en entorno aislado | Acceso con roles; recuento y registros validados; RTO medido |
| Semestral | Simular phishing/robo de cuenta y revocación | Sesiones revocadas, cuenta protegida y escalamiento en SLA |
| Anual | Simulacro de pérdida de sala local | Decisiones y servicios recuperados contra RTO/RPO aprobados |

## Buenas prácticas TIA-942-C para sala local

La propuesta adopta como objetivo **Rated-2** para una sala universitaria pequeña: capacidad redundante de infraestructura crítica, con puntos únicos de falla reconocidos. No se afirma que la instalación cumpla o esté certificada. Antes de construir debe verificarse el estándar completo, planos y normativa de seguridad física y construcción.

| Dominio | Diseño propuesto | Evidencia necesaria para decir implementado |
|---|---|---|
| Energía | Circuitos identificados, UPS dimensionada y prueba de autonomía; generador o procedimiento de apagado controlado | Plano unifilar, carga calculada, mantenimiento y prueba bajo carga |
| Climatización | Temperatura/humedad monitoreada, equipos mantenibles sin detener cargas | Sensores, alarmas y registro de pruebas |
| Cableado | Rutas documentadas, etiquetado y separación de energía/datos | Plano as-built y certificación de enlaces |
| Redundancia | Enlace alterno y componentes duplicados en puntos definidos | Prueba de failover y lista de puntos únicos |
| Seguridad física | Acceso con tarjeta, visitantes acompañados, CCTV conforme privacidad | Bitácora de acceso, revisión de puertas y retención aprobada |
| Incendio/agua | Detección temprana, extintores/supresión apropiada y sensores de fuga | Inspección, mantenimiento y simulacro |
| Monitoreo | UPS, temperatura, humedad, agua y capacidad enviados a alertas | Captura de consola y atención documentada |
| Ubicación y riesgos | Riesgo de inundación, sismo, polvo y disponibilidad eléctrica evaluados | Evaluación de sitio y plan de mitigación |

La nube elimina la obligación de diseñar toda la infraestructura del proveedor; la universidad conserva responsabilidad por selección, configuración, identidad, retención y recuperación de sus datos.
