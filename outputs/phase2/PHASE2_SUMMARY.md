# Fase 2: runner de experimentos (2026-10-08)

Nuevo: experiments/ (run_experiment.py, detection_sources.py, sweep.py, specs/) y
outputs/runs/, outputs/detections/. tracker/ y run_tracker.py intactos (hash de tracker/
7b65976a888fbd3c...; run_tracker.py se importa para reutilizar load_detections_by_frame,
build_detections y check_frame_alignment, sin cambios).

## run_experiment.py
- Conduce el tracker igual que run_tracker.run (una llamada a match_and_track por frame, en
  orden, frame_timestamp = round(frame*1000/fps)). El vídeo solo se abre para frame_count y
  fps; no se decodifica ningún frame ni se escribe vídeo anotado.
- CSV de salida: las 6 columnas del baseline con los mismos valores y formato, más
  matched, detection_count, missed_frame_count y age_frames (semántica documentada en el
  manifiesto y en la cabecera del módulo).
- --check-baseline: compara la proyección de 6 columnas byte a byte con el archivo dado.
- Manifiesto <out>.manifest.json: sha256 del vídeo, del CSV de detecciones (con etiqueta de
  fuente y detalles de degradación si los hay) y de la salida; parámetros del tracker; hash
  de tracker/ y de run_tracker.py; entorno; tiempo; recuentos (filas, emparejadas, coasting,
  ids). Clave de run = hash de (detecciones, vídeo, parámetros, hash de tracker/); si existe
  un manifiesto con la misma clave y la salida intacta, se reutiliza salvo --force.

## Comprobación obligatoria: superada
| clip | filas | emparejadas | coasting | ids | bytes idénticos al baseline | tiempo |
|---|---|---|---|---|---|---|
| bandada | 7571 | 4173 | 3398 | 78 | sí | 286.7 s |
| turbina | 1822 | 556 | 1266 | 35 | sí | 3.6 s |

## Fuentes de detecciones (todas con el esquema del detector)
- real: data/<video_id>_detections.csv.
- gt: ground_truth/<video_id>_detections_corrected.csv tal cual (ya tiene el esquema).
- gt degradado: detection_sources.write_degraded_gt con drop_rate, center_noise_px (gaussiano
  por eje, redondeado a píxel, tamaño intacto), false_positives_per_frame (Poisson por frame,
  posición uniforme en la franja etiquetada, tamaño muestreado de las cajas del GT), seed
  (numpy default_rng). Determinista: dos generaciones con los mismos argumentos dan el mismo
  sha256 (23d5b795...). Manifiesto propio junto al CSV, que el run del tracker incorpora.
  Prueba: drop 0.10, ruido 1.0 px, 0.5 FP/frame, seed 1: 1041 eliminadas, 7745 desplazadas,
  500 espurias, 9601 filas, alineación 0..1008 correcta.

## sweep.py
Ejecuta una lista JSON de runs en procesos paralelos, con reutilización. Probado con el
barrido E5 de la turbina (12 runs, 4 procesos, 16.6 s; el run por defecto se reutilizó).
Especificaciones escritas en experiments/specs/: e3_gt.json (2 runs), e4_degraded_flock.json
(70 runs: drop {0, .1, .2, .3} x ruido {0, 1, 3} x FP {0, .5} x semillas {1, 2, 3}),
e5_params.json (24 runs: max_age {5, 15, 30, 60} x tentative_threshold {2, 3, 5}, ambos clips).

Runs ya terminados: outputs/runs/flock/real_default, outputs/runs/turbine/real_default y los
12 del barrido E5 de la turbina. El run E3 de la bandada (GT como detecciones) sigue en curso.
