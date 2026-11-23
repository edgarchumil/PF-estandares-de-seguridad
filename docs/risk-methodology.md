# Método de riesgos de SGSI-UFVV

## Fuentes y proceso

La matriz académica `docs/sgsi/04-riesgos.csv` usa el proceso de evaluación de NIST SP 800-30 Rev. 1: preparar contexto, identificar eventos y fuentes de amenaza, vulnerabilidades y condiciones predisponentes; estimar probabilidad e impacto; determinar nivel; comunicar y revisar. ISO/IEC 27005:2022 estructura el ciclo de riesgo de seguridad de información, tratamiento, comunicación, aceptación, monitoreo y revisión. OCTAVE Allegro aporta la evaluación cualitativa de activos críticos en `docs/sgsi/05-octave-allegro.md`.

## Criterios

La probabilidad y el impacto se puntúan de 1 a 5; el riesgo se calcula `probabilidad × impacto`. Las bandas institucionales propuestas son bajo (1–4), medio (5–9), alto (10–16) y crítico (17–25). No son probabilidades estadísticas; son escalas ordinales que requieren calibración y aprobación con dueños de proceso. El tratamiento se registra como mitigar, evitar, transferir o aceptar y debe señalar control, responsable, fecha, estado y residual esperado.

El residual de CSV es una estimación posterior al control propuesto, no una observación. Solo se convierte en resultado observado cuando existe evidencia de implementación y una nueva medición. La inteligencia artificial no decide las puntuaciones.

## Trazabilidad

`docs/sgsi/02-inventario-activos.csv` describe activos, propietarios, custodios, información, C/I/D y dependencia. `03-bia.csv` relaciona procesos con impactos, MTPD, RTO y RPO. La matriz de riesgos enlaza escenario, activo, amenaza, vulnerabilidad, controles, decisión y residual esperado. Los controles específicos se vinculan con estándares y evidencia en `docs/sgsi/06-controles.csv`.

Todos los datos son supuestos de una universidad ficticia. No son entrevistas, escaneo, auditoría ni mediciones de una organización real.
