# Fase 4: validación y tests (2026-10-08)

Nuevo: tests/ (35 tests pytest, 14 s), tests/validation/ (dos scripts de validación, fuera de
evaluation/), pytest.ini, reportes en outputs/phase4/.

## Validación IoU contra el flujo estándar de TrackEval (outputs/phase4/trackeval_iou_validation.md)
Exportación MOTChallenge con nuestro exportador, puntuada por trackeval.Evaluator +
MotChallenge2DBox (preprocesado desactivado) y por nuestro puente con similitud IoU sobre las
mismas vistas. 26 campos comparados (HOTA, DetA, AssA, LocA, DetRe, DetPr, AssRe, AssPr, MOTA,
MOTP, IDSW, Frag, TP, FN, FP, MT, PT, ML, Re, Pr, IDF1, IDP, IDR, IDTP, IDFN, IDFP) en 5 casos
(turbina baseline, bandada baseline, nube, real_default emparejadas, E3): 0 discrepancias.

## Caso sintético de distancia exacta (tests/test_distance_exact.py)
Desplazamiento de 8.0 px con match 8 px: 10 TP, IDF1 1, MOTP 8.0 px. Desplazamiento de 8.01 px:
0 TP, 10 FP, 10 FN; con 12 px vuelve a 10 TP. Desplazamiento diagonal (3, 4) empareja a 5 px y
no a 4.9. En alpha = 0.5 de HOTA la similitud vale exactamente 0.5 y HOTA_TP = 10.

## Validación cruzada contra evaluate_track_quality (outputs/phase4/crossvalidation_reference.md)
Modo center_distance, mismos px (4 y 8), mismas vistas. Resultados:
- Turbina: idénticos (IDF1, IDTP, cambios, fragmentación).
- real_default emparejadas con región: IDF1 0.1790 frente a 0.1797 a 8 px, cambios 156/156,
  fragmentación 419/415. La diferencia de IDF1 viene de 35 frames con dos pájaros a menos de 8 px
  de una misma caja del tracker: TrackEval cuenta todos los pares dentro del umbral como
  emparejamientos potenciales y resuelve una asignación global; la referencia solo cuenta su
  emparejamiento greedy por frame. IDTP nuestro >= el de la referencia siempre.
- Baseline todas las filas con región, 8 px: cambios 241 (ref) frente a 227 (nuestro); 19 solo
  en la referencia y 5 solo en el nuestro, todos listados por (frame, id GT). Causa: greedy
  nearest-first frente a húngaro con preferencia por el id que cubría el objeto en el frame
  anterior; en varios casos el mismo cambio aparece desplazado uno o dos frames.
- E3: 87 cambios en la referencia frente a 17 nuestros. Los 70 extra caen en frames 456..480
  sobre los pájaros 79136 y 79139 (los de la caja compartida del frame 517), que vuelan a pocos
  píxeles: el greedy alterna la asignación entre ambos cada frame y cuenta un cambio por pájaro
  y por vuelta. El húngaro con continuidad solo reporta los intercambios del propio tracker.

## Tests (tests/)
- test_similarity.py: funciones puras en sus límites (escala, similitud a 0 / px / T, IoU
  idéntico, disjunto y medio solape, distancia euclídea).
- test_adapters.py: conteos de la Fase 0 (GT 10142/25, turbina 241/1, nube 3542/17, detector
  4424, baseline 7571/78); formato de 6 columnas marca coasting desconocido y rechaza la vista
  de emparejadas; en el formato de 10 columnas una fila en coasting nunca produce una Detection
  (sobre el run real y sobre un CSV sintético); filas inconsistentes se rechazan.
- test_rules.py: reetiquetado a mitad = 1 cambio; intercambio mutuo = 2; perder y recuperar con
  el mismo id = 0 cambios y 1 fragmento; recuperar con otro id tras un hueco = 1 cambio; ids
  huérfanos e ids por pájaro. Documentado un matiz de TrackEval: CLEAR no cuenta un Frag si la
  interrupción cae en frames sin ninguna entrada del candidato (salta el frame antes de
  actualizar su memoria); el diagnóstico propio sí lo cuenta.
- test_store.py: ida y vuelta, ids de contenido iguales/distintos, referencias, id del store real.
- test_properties.py: GT contra sí mismo HOTA = IDF1 = MOTA = 1 y 0 cambios; renombrar los ids
  del candidato no cambia ninguna métrica (turbina real y caso sintético).
- test_distance_exact.py y test_trackeval_validation.py: lo de arriba.
- test_experiments.py: GT degradado determinista y con esquema correcto; sin degradación
  reproduce las cajas; run_experiment reproduce results/synthetic/baseline_tracks.csv byte a
  byte y reutiliza el run en la segunda llamada.
