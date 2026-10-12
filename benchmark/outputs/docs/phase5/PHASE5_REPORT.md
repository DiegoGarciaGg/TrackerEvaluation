# Fase 5: experimentos y reporte (2026-10-09)

Todo lo reportado aquí sale de `outputs/reports/SUMMARY.md` (tablas completas) y de los reportes
por run en `outputs/reports/runs/<clip>/<run>__vs_<referencia>.md|.json` (procedencia,
sensibilidad a 4/6/8/12 px, ambas vistas, con y sin región ignorada, lista de cambios de
identidad, ids por pájaro, huérfanos, huecos y duraciones). Salvo que se diga otra cosa: 8 px
de distancia entre centros (T = 16), vista "emparejadas" (solo filas con detección), región del
rótulo de fecha ignorada en la bandada, y frames 53..293 en la turbina contra GT.

Motor de métricas: TrackEval commit 12c8791b (MIT), validado contra su propio flujo estándar
(Fase 4). Ninguna métrica es una puerta de aceptación.

## Qué ejecuté
- 70 runs de GT degradado (E4), 24 runs del barrido de parámetros (E5), 2 runs de GT como
  detecciones (E3), 2 runs con detecciones reales y columnas extra (reproducen el baseline byte
  a byte). Cada run con su manifiesto (sha256 del vídeo, de las detecciones y de la salida,
  parámetros, hash de `tracker/`, semilla y parámetros de degradación cuando aplica).
- 102 evaluaciones (cada run contra GT; los runs por defecto y los baselines congelados también
  contra la nube).
- Incidencia: con pérdida de detecciones, a veces desaparece la única caja del frame 0 o del
  último frame y el archivo degradado queda en 1..1008 o 0..1007; la comprobación de alineación
  de `run_tracker.py` lo rechaza. Los runs de GT (turbina, 53..293) y de GT degradado se
  ejecutan con `--allow-partial-coverage` (el archivo está en la numeración del clip por
  construcción), anotado en cada manifiesto. `sweep.py` tolera ahora fallos individuales.

## E1 exactitud: baseline congelado contra ground truth

| clip | vista | HOTA | DetA | AssA | MOTA | IDF1 | IDSW | TP | FP | FN | ids / pájaros | huérfanos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bandada | todas las filas (6 col) | 0.252 | 0.129 | 0.519 | -0.233 | 0.160 | 227 | 1906 | 4041 | 8236 | 35 / 25 | 17 |
| bandada | emparejadas (10 col) | 0.273 | 0.128 | 0.594 | -0.069 | 0.180 | 156 | 1634 | 2180 | 8508 | 35 / 25 | 17 |
| turbina | todas las filas | 0.477 | 0.287 | 0.793 | -1.178 | 0.450 | 0 | 215 | 499 | 26 | 15 / 1 | 14 |
| turbina | emparejadas | 0.682 | 0.567 | 0.821 | 0.361 | 0.734 | 0 | 213 | 126 | 28 | 12 / 1 | 11 |

Sin región ignorada la bandada tiene 78 ids y 60 huérfanos: 43 ids viven enteros en el rótulo
de fecha. Lectura: el recall del 16 % en la bandada es del detector (cubre el 17 % de las cajas
del GT a 8 px, Fase 0), no del tracker; la mitad de las filas escritas son coasting (3398 de
7571) y en la vista "todas" cuentan como FP. En la turbina el pájaro etiquetado se sigue sin
ningún cambio de identidad; los FP son los objetos sin etiquetar y la pala.

## E2 paridad: baseline contra la nube

| clip | vista | HOTA | DetA | AssA | IDF1 | IDSW | ids / ids nube |
|---|---|---|---|---|---|---|---|
| bandada | todas | 0.399 | 0.440 | 0.362 | 0.389 | 177 | 35 / 17 |
| bandada | emparejadas | 0.504 | 0.642 | 0.397 | 0.497 | 170 | 35 / 17 |
| turbina | todas | 0.357 | 0.186 | 0.684 | 0.315 | 0 | 35 / 8 |
| turbina | emparejadas | 0.732 | 0.575 | 0.931 | 0.732 | 0 | 35 / 8 |

La nube cubre solo el 15 % del GT de la bandada (Fase 0), así que la paridad mide acuerdo entre
dos salidas pobres; no sustituye al GT.

## E3 techo de asociación: GT como detecciones

| clip | HOTA | DetA | AssA | IDF1 | IDSW | TP | FP | FN | ids / pájaros |
|---|---|---|---|---|---|---|---|---|---|
| bandada | 0.962 | 0.992 | 0.934 | 0.973 | 17 | 10091 | 0 | 51 | 25 / 25 |
| turbina | 0.992 | 0.992 | 0.992 | 0.996 | 0 | 239 | 0 | 2 | 1 / 1 |

Con cajas perfectas el tracker da exactamente un id por pájaro. Los 51 FN son las dos primeras
detecciones de cada track (nunca se escriben, 2 x 25) más la caja duplicada del frame 517. Los
17 cambios de identidad se agrupan en dos sitios (lista completa en el reporte del run):
frames 91..132, donde un track confirmado roba la detección de un pájaro recién entrado
durante sus frames tentativos (la cascada de `matching.py` compara la característica (x, y,
área) con umbral 250 px), y frames 467..480, un cruce entre 79136 y 79139. Insensible a la
distancia de emparejamiento (4 a 12 px). En la vista "todas las filas" aparecen 815 FP: las
colas de coasting de 29 frames al morir cada track.

## E4 robustez: GT degradado (bandada, 3 semillas por punto, media)

| pérdida | ruido px | FP/frame | HOTA | AssA | IDF1 | IDSW | ids |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0.963 | 0.934 | 0.973 | 18 | 25 |
| 0 | 1 | 0 | 0.891 | 0.868 | 0.973 | 17 | 25 |
| 0 | 3 | 0 | 0.605 | 0.534 | 0.803 | 96 | 25 |
| 0 | 0 | 0.5 | 0.850 | 0.742 | 0.841 | 44 | 27 |
| 0.1 | 0 | 0 | 0.812 | 0.760 | 0.882 | 153 | 25 |
| 0.2 | 0 | 0 | 0.508 | 0.354 | 0.530 | 496 | 25 |
| 0.3 | 0 | 0 | 0.349 | 0.180 | 0.343 | 914 | 24 |
| 0.1 | 1 | 0.5 | 0.471 | 0.281 | 0.481 | 475 | 30 |
| 0.3 | 3 | 0.5 | 0.195 | 0.077 | 0.207 | 1570 | 33 |

Curvas completas (HOTA, IDF1, IDSW contra pérdida por cada nivel de ruido y FP) y dispersión
entre semillas en SUMMARY.md. Lecturas:
- La pérdida de detecciones es el factor dominante: un 10 % perdido multiplica por 8 los
  cambios de identidad (18 a 153) y un 20 % hunde HOTA a 0.51. El número de ids no sube: no es
  fragmentación sino intercambio de identidades entre tracks vivos mientras uno coastea, en una
  bandada donde el 63 % de las cajas tiene un vecino a menos de 20 px. Es el mecanismo que
  las detecciones reales (que cubren el 17 % del GT) disparan en E1.
- El ruido de 1 px apenas cuesta identidad (IDF1 0.973 igual); el de 3 px cuesta HOTA sobre
  todo por localización (DetA 0.68 a 8 px) y empieza a costar identidad (IDSW 96).
- 0.5 FP/frame sin otra degradación ya duplica los cambios (44) y añade dos ids; combinado con
  pérdida, los FP multiplican el daño (0.1 de pérdida: IDSW 153 sin FP, 453 con FP).
- Dispersión entre semillas grande en los puntos intermedios (pérdida 0.2: HOTA 0.51 +- 0.13),
  así que una sola semilla no basta para comparar variantes del tracker ahí.

## E5 parámetros: max_age x tentative_threshold con detecciones reales

Bandada (HOTA / IDF1 / IDSW / ids, emparejadas, región ignorada):

| max_age \ tentative | 2 | 3 | 5 |
|---|---|---|---|
| 5 | 0.271 / 0.176 / 175 / 65 | 0.271 / 0.176 / 164 / 58 | 0.273 / 0.178 / 125 / 41 |
| 15 | 0.271 / 0.177 / 151 / 43 | 0.271 / 0.178 / 147 / 41 | 0.273 / 0.180 / 126 / 29 |
| 30 | 0.272 / 0.178 / 159 / 37 | 0.273 / 0.180 / 156 / 35 | 0.275 / 0.182 / 138 / 25 |
| 60 | 0.272 / 0.178 / 159 / 37 | 0.273 / 0.180 / 156 / 35 | 0.275 / 0.182 / 138 / 25 |

Turbina (HOTA / IDF1 / FP / ids):

| max_age \ tentative | 2 | 3 | 5 |
|---|---|---|---|
| 5 | 0.494 / 0.449 / 146 / 27 | 0.515 / 0.475 / 114 / 13 | 0.530 / 0.495 / 93 / 8 |
| 15 | 0.661 / 0.703 / 154 / 20 | 0.685 / 0.738 / 123 / 11 | 0.711 / 0.770 / 96 / 8 |
| 30 | 0.656 / 0.697 / 159 / 19 | 0.682 / 0.734 / 126 / 12 | 0.710 / 0.769 / 97 / 8 |
| 60 | 0.656 / 0.697 / 159 / 19 | 0.682 / 0.734 / 126 / 12 | 0.710 / 0.769 / 97 / 8 |

Lecturas:
- Con detecciones reales ningún parámetro mueve HOTA en la bandada (0.271 a 0.275): el techo lo
  pone el detector. `tentative_threshold` 5 reduce ids de 35 a 25 y huérfanos de 17 a 9 sin
  perder TP apreciables (1634 a 1599): quita tracks nacidos de ruido.
- `max_age` 30 y 60 son idénticos en los dos clips: ningún track se reengancha coasteando más
  de 30 frames. `max_age` 5 fragmenta (65 ids en la bandada; en la turbina AssA cae de 0.82 a
  0.45 porque el pájaro se pierde tras la pala y vuelve con otro id).
- En la turbina, `max_age` 15 iguala a 30 con menos filas fantasma.

## Sensibilidad a la distancia (emparejadas)
Bandada real: HOTA 0.251 / 0.264 / 0.273 / 0.283 a 4 / 6 / 8 / 12 px; IDSW 104 / 135 / 156 /
173. Bandada E3: 0.961 / 0.962 / 0.962 / 0.962. Turbina real: 0.652 / 0.675 / 0.682 / 0.707.
La elección de 8 px no cambia ninguna conclusión; con cajas reales más anchas que los pájaros
(w mediana 33 frente a 9) el emparejamiento gana TP al relajar la distancia, como era de esperar.

## Herramientas entregadas
- `evaluation/cli.py`: reporte de un run contra una referencia por rutas explícitas.
- `evaluation/batch_report.py`: todos los runs de `outputs/runs` y SUMMARY.md.
- `evaluation/quick_metrics.py`: script suelto, HOTA/MOTA/IDF1 de CSVs sin pipeline.
- `experiments/run_experiment.py`, `experiments/sweep.py`, `experiments/specs/*.json`.
- `tests/`: 35 tests (14 s). `tests/validation/`: validación IoU contra TrackEval estándar y
  validación cruzada contra `evaluate_track_quality`.

## Qué no está hecho o queda abierto
- No hay gráficas: las curvas de E4 están como tablas (matplotlib no está entre las
  dependencias acordadas). Se añaden en minutos si se autoriza.
- El GT de la turbina es parcial (un pájaro): precisión y FP en la turbina no son exactitud.
- Región ignorada de la bandada: el rectángulo del rótulo (0,0)-(721,400), decidido por mí.
- La caja duplicada del frame 517 y los huecos del GT se dejaron tal cual (decisión tuya).
- Nada se ha commiteado: la carpeta no es un repositorio git.

## Añadido el 2026-10-09: segunda bandada sin etiquetar
De las 2180 filas emparejadas del run real que no caen sobre un pájaro etiquetado (región del
rótulo ya excluida), 1688 están a más de 50 px de cualquier caja del GT, casi todas en frames
200..600: cinco tracks largos (ids 36, 40, 45, 64, 69; 47 a 262 filas; y 2796..2980) que son la
segunda bandada, más once ids cortos en un punto fijo (x 790..830, y 3160..3240), probablemente
la punta de la pala. Nueva opción `reference_proximity_px` (CLI `--reference-proximity-px`):
descarta las entradas del candidato a más de R px de todo objeto etiquetado en su frame, y el
reporte lo anota. Efecto a 50 px sobre real_default (emparejadas, región): FP 2180 -> 492, MOTA
-0.069 -> 0.097, IDP 0.329 -> 0.590, HOTA 0.273 -> 0.294, ids 35 -> 18, huérfanos 17 -> 0; sin
cambio en TP, FN, IDR ni IDSW. E3, E4 y E5 no se ven afectados (sus detecciones salen del GT).
