# Fase 1: contratos, adaptadores y store (2026-10-08)

Nuevo: evaluation/ (independiente de tracker/, solo stdlib y numpy; sin cv2) y outputs/store/.

## evaluation/
- contracts.py: Detection, TrackUpdate, Track, Provenance, RunResult, StageStat, StageTiming,
  Box, FrameDetections, reconstruct_tracks. Nombres y semántica de spoorpredictioneval.contracts.
  Añadidos (con valor por defecto, marcados "# added"): TrackUpdate.box_xywh (la caja escrita en
  esa fila, también en coasting), TrackUpdate.is_matched, Track.matched_update_count,
  RunResult.observation_count / update_count / track_ids.
- provenance.py: build_provenance fija las claves de extra: predictor, claim (accuracy, parity,
  regression, detections), dataset, video_id, config, inputs {label: {path, sha256}}, notes
  (incluye la ventana de frames del clip original), más campos libres. store_ref da
  "<dataset>|<video_id>|<dimensión>".
- hashing.py: sha256_file, sha256_tree (hash de tracker/*.py ignorando __pycache__), sha256_json.
- store.py: ResultStore (Protocol), JsonlResultStore(root).persist(result, ref) / resolve(id o
  ref) / bind / refs, content_run_id (hash de procedencia + salida completa, sin reloj).
- adapters/: gt_csv (claim accuracy; curación "independent manual annotation"; sha256 de los
  dos CSV de GT y del mp4; comprueba que el CSV de detecciones del GT es la misma caja fila a
  fila), cloud_csv (claim parity), detections_csv (observaciones sin track_id, confianza 1.0 con
  nota), tracker_csv (formato 6 columnas: todas las filas son observaciones y coasting_known =
  False en la procedencia; formato 10 columnas: fila emparejada -> Detection + TrackUpdate con
  confianza 1.0, fila en coasting -> solo TrackUpdate con confianza 0.0 y missed_frame_count),
  motchallenge (exportador gt.txt / seqinfo.ini / seqmaps / trackers/<name>/data/<seq>.txt,
  frames 1-based, ids enteros positivos con tabla devuelta).

## Verificado sobre los datos reales (conteos de la Fase 0)
| run | observaciones | updates | tracks |
|---|---|---|---|
| flock gt | 10142 | 10142 | 25 |
| flock cloud | 3542 | 3542 | 17 |
| flock detector | 4424 | 0 | 0 |
| flock baseline (6 col) | 7571 | 7571 | 78 |
| turbine gt | 241 | 241 | 1 |
| turbine cloud | 397 | 397 | 8 |
| turbine detector | 734 | 0 | 0 |
| turbine baseline (6 col) | 1822 | 1822 | 35 |

Ida y vuelta por el store sin pérdida (correctness, tracks y provenance iguales; el id de
contenido coincide al releer). La caja duplicada del GT (frame 517, ids 79136 y 79139) se
conserva y queda anotada en provenance.extra.facts. Hash de tracker/: 7b65976a888fbd3c...

Store poblado en outputs/store con las referencias:
flock|20251012_164031_1DAC|{gt, baseline:cloud, detections:real, kit:baseline} y las cuatro
equivalentes de turbine|20250920_063942_6C42.

Exportación MOTChallenge probada en un directorio temporal: gt.txt 10142 líneas, baseline 7571,
cloud 3542.

## Decisiones tomadas (delegadas)
- Región ignorada por defecto en la bandada: rectángulo del rótulo de fecha, x 0..721, y 0..400.
  Se reportará con y sin.
- Exactitud en la turbina: solo frames 53..293 (único pájaro etiquetado); paridad y regresión en
  todo el clip.
- TrackEval fijado al commit 12c8791b303e0a0b50f753af204249e622d0281a; los alias np.float y
  np.int se definen en nuestro código antes de importarlo, sin parchear su fuente.
