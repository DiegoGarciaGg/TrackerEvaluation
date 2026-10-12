# Fase 3: métricas y diagnóstico (2026-10-08)

Nuevo en evaluation/: views.py, similarity.py, trackeval_bridge.py, diagnostics.py, evaluate.py.
TrackEval instalado en .venv desde GitHub fijando el commit 12c8791b303e0a0b50f753af204249e622d0281a
(MIT); pytest instalado para la Fase 4. (El pip del venv tenía un shebang roto de otra ruta;
se instala con `.venv/bin/python -m pip`.)

## numpy 2.x y TrackEval
hota.py usa np.float e identity.py usa np.int (eliminados en numpy 1.24). trackeval_bridge.py
define np.float = float y np.int = int antes de importar trackeval, sin modificar su fuente, y
lo deja escrito en la procedencia de cada reporte.

## Similitud
s = max(0, 1 - d/T). CLEAR e Identity emparejan con s >= 0.5, es decir d <= T/2; el usuario da
la distancia en píxeles y T = 2 * px (8 px -> T = 16). HOTA barre alpha 0.05..0.95, o sea
distancias 0.95 T .. 0.05 T; el reporte da la media (valor estándar) y el valor en alpha = 0.5
(exactamente la distancia configurada). LocA y MOTP se convierten a píxeles: T * (1 - valor).
Sensibilidad por defecto: 4, 6, 8 y 12 px.

## Vistas
- observations: solo filas emparejadas (las Detection del repo). Requiere formato de 10
  columnas; con el baseline de 6 columnas se rechaza y el reporte lo anota.
- updates: todas las filas tal como se escriben (coasting incluido).
- Región ignorada (rectángulos y polígonos): se eliminan las entradas con centro dentro, en
  candidato y referencia. Por defecto para la bandada: rótulo de fecha (0,0)-(721,400). Se
  reporta siempre con y sin.
- Rango de frames opcional (turbina: 53..293).

## Diagnóstico propio (diagnostics.py)
Asociación húngara por frame con puerta de distancia y el mismo desempate que CLEAR (se prefiere
el id que cubría el objeto en el frame anterior), así la lista de cambios de identidad explica
el IDSW de CLEAR (coinciden: 227 y 156 en las dos vistas del run real). Produce: lista de
cambios (frame, id GT, id anterior -> nuevo, posición, frames desde la cobertura anterior), ids
del tracker por pájaro, ids huérfanos, ids contra pájaros, huecos y duraciones por track.
Nota: el Frag de CLEAR cuenta reanudaciones tras cualquier interrupción, incluidas las ausencias
del propio GT (111 huecos en la bandada), así que un tracker perfecto da Frag = 111; la
fragmentación del diagnóstico solo cuenta interrupciones dentro de los frames etiquetados.

## Resultados de humo (bandada, 8 px)
| run | vista | región | HOTA | DetA | AssA | MOTA | IDF1 | IDSW | TP | FP | FN | ids / huérfanos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GT contra GT | obs | no | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0 | 10142 | 0 | 0 | 25 / 0 |
| baseline (6 col) | updates | no | 0.239 | 0.115 | 0.519 | -0.393 | 0.146 | 227 | 1906 | 5665 | 8236 | 78 / 60 |
| baseline (6 col) | updates | sí | 0.252 | 0.129 | 0.519 | -0.233 | 0.160 | 227 | 1906 | 4041 | 8236 | 35 / 17 |
| real_default (10 col) | observations | sí | 0.273 | 0.128 | 0.594 | -0.069 | 0.180 | 156 | 1634 | 2180 | 8508 | 35 / 17 |
| E3 GT como detecciones | observations | no | 0.962 | 0.992 | 0.934 | 0.993 | 0.973 | 17 | 10091 | 0 | 51 | 25 / 0 |
| E3 GT como detecciones | updates | no | 0.892 | 0.918 | 0.868 | 0.913 | 0.936 | 15 | 10091 | 815 | 51 | 25 / 0 |

Lecturas rápidas (se desarrollan en la Fase 5):
- 43 de los 78 ids del baseline viven enteros dentro del rótulo de fecha: la región ignorada
  los elimina (78 -> 35 ids). Quedan 17 ids huérfanos fuera de la región.
- Con detecciones reales, el recall a 8 px es 0.19 (todas las filas) porque el detector cubre
  solo el 17 % del GT: E1 mide sobre todo al detector.
- Con detecciones perfectas (E3) el tracker da 25 ids para 25 pájaros, 17 cambios de identidad
  y 51 FN (las dos primeras detecciones de cada track nunca se escriben: 2 x 25, más la caja
  duplicada del frame 517). Los cambios se concentran en frames 91..132 (entradas de pájaros,
  un track confirmado roba la detección del recién llegado) y 467..480 (cruce).
- Turbina, baseline contra GT en 53..293: TP 215, FN 26, IDSW 0, FP 499 (objetos sin
  etiquetar y pala); en todo el clip FP 1607. El GT parcial de la turbina solo sostiene recall y
  continuidad de identidad del pájaro etiquetado.

Tiempos: evaluación completa (2 vistas x 2 regiones x 4 px) del run real de la bandada: 16 s.
