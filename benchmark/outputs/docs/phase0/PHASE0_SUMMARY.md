# Fase 0: exploración (2026-10-08)

Carpeta de trabajo: /Users/diegogarciagonzalez/tracker-kit-Eval. No se ha modificado nada en
tracker/, run_tracker.py, data/, results/ ni en tracker-kit-Changing. Lo nuevo: ground_truth/
(copia del GT con SHA256SUMS) y outputs/phase0/ (este resumen y los frames extraídos).

## 1. Inventario de GT (/Users/diegogarciagonzalez/tracker-kit-Changing/GT)

| archivo | bytes | filas | clip |
|---|---|---|---|
| 20251012_164031_1DAC_detections_corrected.csv | 383913 | 10142 | bandada (data/20251012_164031_1DAC.mp4) |
| 20251012_164031_1DAC_reference_tracks_corrected.csv | 335552 | 10142 | bandada |
| 20250920_063942_6C42_detections_corrected.csv | 9287 | 241 | turbina (data/20250920_063942_6C42.mp4) |
| 20250920_063942_6C42_reference_tracks_corrected.csv | 8065 | 241 | turbina |

sha256 (copiados a ground_truth/, verificados con shasum -c):
- 503255dd... 1DAC_detections_corrected
- a89c6bc9... 1DAC_reference_tracks_corrected
- 9a7b813b... 6C42_detections_corrected
- 0c09f3ba... 6C42_reference_tracks_corrected
- vídeos: fbc117d9... 1DAC.mp4, d16e8f3b... 6C42.mp4 (lista completa en ground_truth/SHA256SUMS y en la salida de shasum)

## 2. Esquemas

GT detections: frame_number, frame_timestamp, x, y, w, h, area, classifier_name. Todo entero,
classifier_name = "corrected", area == w*h, frame_timestamp == frame_number*40. Es EXACTAMENTE
el esquema de data/*_detections.csv (única diferencia cosmética: area es int en GT y float
"323.0" en el detector). Sirve directamente como entrada perfecta para E3.

GT reference tracks: frame_number, obj_id, x1, y1, x2, y2, bbox_size. Todo entero. Caja xyxy en
píxeles, x2 > x1 e y2 > y1 en todas las filas, bbox_size == (x2-x1)*(y2-y1). La identidad del
pájaro es obj_id (enteros de 5 cifras, p. ej. 78911). Frames empiezan en 0 (bandada: 0..1008,
1009 frames, todos con al menos una caja).

Relación entre los dos CSV: misma fila a fila (x==x1, y==y1, x+w==x2, y+h==y2, mismo orden).
Son las mismas cajas, una con obj_id y otra sin él.

## 3. Alineación con el clip

Frame 0: GT (1857,3450,17,19) == detector == nube obj 491. Frames 1 y 2 también idénticos en
las tres fuentes. Frame 3: GT (1851,3445,15,12), detector (1851,3417,36,40): misma x, caja
distinta (el detector da una caja mayor). Sistema de coordenadas: xywh esquina superior
izquierda en píxeles del vídeo 2160x3840, sin desfase de frames. Vídeo verificado con cv2:
2160x3840, 25 fps, 1009 frames (turbina: 671 frames).

## 4. Datos medidos: lo que coincide y lo que NO

| dato | dicho | medido en los CSV de GT |
|---|---|---|
| frames | 1009 | 1009 (0..1008) |
| identidades | 40 | **25** |
| cajas | 10500 | **10142** |
| caja mediana | 9x7 | 9x7 (medias 9.6 x 7.6; w 2..25, h 2..26) |
| mediana vecino más cercano | 17 px | 17.1 px (sobre 9600 cajas con vecino en el mismo frame; 542 sin vecino) |
| vecino < 20 px | 66 % | 66.9 % de las cajas con vecino (63.3 % de todas) |
| franja y | 2703..3469 | 2703..3469 (x 0..2159) |
| idénticas a detector o nube | 362 | **360** (330 al detector, 359 a la nube) |
| nube identidades | 17 | 17 |
| baseline | 78 IDs, 7571 filas | 78 IDs, 7571 filas |
| detecciones | 4424 | 4424 |
| arriba a la izquierda (y<400, x<721) | 484 | **471** (cualquier variante del criterio da 471; y<2703 da 492) |

Las cifras 40 identidades y 10500 cajas NO salen de estos CSV. El sufijo "_corrected" sugiere
que son una versión corregida de la exportación de Supervisely (identidades fusionadas y cajas
eliminadas). Necesito confirmación de cuál es la versión buena.

Otros hallazgos del GT de la bandada:
- obj_id 78911 cubre los 1009 frames (de (1857,3450) a (47,2725)); la nube lo parte en 491
  (0..896) y 647 (840..1008).
- 20 de 25 identidades tienen huecos: 111 huecos, 102 de 1 frame, 8 de 2, 1 de 3 (121 frames).
- Una caja duplicada: frame 517, caja (122,2851)-(132,2857) asignada a DOS obj_id, 79136 y
  79139. En TrackEval contará como dos GT en el mismo punto.
- 243 pares de pájaros distintos a <= 8 px en el mismo frame (184 frames); 425 cajas tienen un
  vecino a < 8 px y 160 a < 4 px. A 8 px habrá ambigüedad real en esos frames.
- Máximo 25 cajas por frame.

## 5. Turbina (20250920_063942_6C42)

SÍ hay ground truth, pero es parcial: UNA sola identidad (obj_id 78914), 241 frames (53..293),
un pájaro que cruza de x=0 a x=2151 a y 3210..3269. Coincide con la nube obj 372 (227 frames en
común, 111 cajas idénticas, distancia de centros mediana 0.5 px). Los otros 7 obj_id de la nube
(353, 363, 381, 390, 440, 458, 468), incluidos 381 y 390 que coexisten en 121..222 con el
pájaro etiquetado, NO están etiquetados, y la reaparición tras la pala (nube 440 en 482..514)
tampoco. El detector del kit pone una detección a <= 8 px del centro del GT en 215/241 frames.
Consecuencia: en la turbina la exactitud solo es defendible como recall / continuidad de ID de
ese pájaro en los frames 53..293; la precisión y los FP necesitan región ignorada o restricción
de frames. Paridad y regresión sí son completas.

## 6. Coasting: cómo saber si una fila del tracker está emparejada

Leído en simple_sort_tracker.py y tracked_object.py y verificado ejecutando el tracker sin
vídeo (importado sin cambios, misma secuencia de llamadas que run_tracker.py):

- match_and_track: (1) asocia, (2) update() en los emparejados: añade la detección a
  track.detections y pone age = 0, (3) borra no emparejados (confirmados solo si age >= max_age),
  (4) crea tentativos, (5) predict() en TODOS los supervivientes: age += 1.
- Por tanto, tras match_and_track, age == 1 si y solo si el track fue emparejado (o creado) en
  este frame; age == 1 + fallos consecutivos. age NO es la edad desde el nacimiento.
- Criterio robusto: track.detections[-1].frame_number == frame actual. Los tres criterios
  (frame_number de la última detección, identidad del objeto detección, age == 1) coinciden en
  las 7571 filas de la bandada y las 1822 de la turbina.
- Un track confirmado con age == max_age (30) en el paso 3 se borra: coastea 29 frames escritos
  (age 2..30 en el CSV) y muere en el 30.º fallo.
- Confirmación en la 3.ª detección (tentative_threshold = 3): la primera fila escrita de cada
  track tiene len(detections) == 3 en los 78 tracks. Las 2 primeras detecciones de cada track
  nunca se escriben.

Cifras de la bandada: 7571 filas = 4173 emparejadas + 3398 en coasting; 251 detecciones nunca
se escriben (156 = 2 x 78 previas a la confirmación, 95 en tentativos que murieron). 74 de los
78 tracks terminan con 29 filas en coasting (2146 filas "fantasma" al final de tracks), 2
terminan emparejados al final del clip. Huecos internos cerrados: 232 de 1 frame, 77 de 2, ...,
hasta 29 frames. Turbina: 1822 = 556 + 1266, 35 tracks, 32 con cola de 29 filas.

Reproducción del baseline: la ejecución sin vídeo reproduce results/flock/baseline_tracks.csv y
results/turbine/baseline_tracks.csv fila a fila (comparación de cadenas de las 6 columnas). El
vídeo solo aporta el recuento de frames y el dibujo, así que experiments/ puede correr sin
abrir el mp4 (comprobación obligatoria de la Fase 2 ya satisfecha en el scratchpad).

## 7. Detecciones arriba a la izquierda (decisión pendiente del usuario)

471 detecciones del kit con y < 400 y x < 721: y entre 0 y 19, x entre 7 y 450, w mediana 62,
h mediana 34, en 437 frames (máximo 2 por frame), desde el frame 23 hasta el 1008. Imágenes en
outputs/phase0/frames/ (frames 23, 353, 592, 825, 1008): vista completa a 1/4 con la zona
marcada, y recorte x 0..600, y 0..120 a 3x, crudo y con las cajas. Lo que se ve en el recorte:
la zona corresponde al rótulo de fecha y hora grabado en el vídeo ("12.10.2025 16:43:26"), y la
caja roja cae sobre los dígitos de minutos/segundos. En la turbina ocurre lo mismo (113
detecciones, recorte del frame 448 incluido). Además hay 2 detecciones diminutas fuera de la
franja en los frames 993 y 998 (y 2421 y 2386).

## 8. Detector frente a GT (contexto para interpretar E1)

Distancia entre centros, bandada:
- Cajas del GT con una detección del kit a <= 4/6/8/12/20 px: 13.7 / 15.3 / 16.8 / 20.8 / 29.2 %.
- Detecciones del kit con un centro del GT a <= 8 px: 37.5 %; mediana de distancia al GT más
  cercano 90.7 px. Dentro de la franja hay 3929 detecciones, de w mediana 33 (GT: 9): el
  detector une varios pájaros en línea en una caja ancha (frame 200: 25 GT, 5 detecciones).
- Nube: cubre el 15.3 % del GT a 8 px. Baseline (todas las filas): 19.3 % del GT a 8 px, pero
  solo el 25.5 % de sus filas tienen GT cerca.
Turbina: el detector cubre el 89 % del GT a 8 px.

Es decir: E1 medirá sobre todo al detector (recall bajo por diseño de la entrada); el techo
real del tracker se verá en E3 y E4.

## 9. TrackEval

Clonado en el scratchpad: commit 12c8791b303e0a0b50f753af204249e622d0281a (2022-11-29, HEAD de
main). Formato por secuencia (data dict): num_timesteps, num_gt_ids, num_tracker_ids,
num_gt_dets, num_tracker_dets, gt_ids[t] y tracker_ids[t] (arrays int con IDs reetiquetados a
0..n-1 contiguos), similarity_scores[t] (matriz n_gt_t x n_trk_t). HOTA no umbraliza (barre
alpha 0.05..0.95); CLEAR e Identity emparejan con similarity >= THRESHOLD (0.5 por defecto).
Con s = max(0, 1 - d/T), d <= T*(1 - 0.5): para 8 px, T = 16.

Incompatibilidad con numpy 2.5.3 (confirmada en el código): hota.py usa np.float (5 veces) e
identity.py usa np.int (3 veces); ambos alias se eliminaron en numpy 1.24. CLEAR no los usa.
Opciones: (a) alias en nuestro código antes de importar trackeval (np.float = float,
np.int = int), sin tocar su fuente; (b) parche local al clon; (c) instalar numpy < 1.24 en un
venv aparte. Pendiente de decisión.

## 10. Entorno

.venv: Python 3.12.10, numpy 2.5.3, scipy 1.18.1, opencv 5.0.0. No hay pandas, pytest ni
trackeval. git disponible (la carpeta de trabajo no es un repositorio).

## 11. Tiempo de ejecución

Un run del tracker sobre la bandada sin vídeo (1009 frames, detecciones reales, parámetros por
defecto) tarda 224.9 s en este equipo. Para E4 (varias semillas y niveles de degradación) y E5
(barridos de max_age y tentative_threshold) hay que planificar decenas de runs: conviene
ejecutarlos en paralelo por proceso y cachear por hash de entrada y parámetros.
