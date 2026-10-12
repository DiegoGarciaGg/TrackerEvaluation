# Evaluación del tracker de pájaros: informe general

Fecha: 9 de octubre de 2026. Carpeta de trabajo: `tracker-kit-Eval`.

Este documento explica, sin entrar en detalles técnicos, qué se construyó, cómo funciona y qué
se aprendió. Los detalles están en los resúmenes por fase dentro de `outputs/phase0` a
`outputs/phase5` y en las tablas de `outputs/reports/SUMMARY.md`.

## 1. El problema en una frase

Una cámara graba pájaros cerca de un aerogenerador. Un programa (el **detector**) mira cada
imagen y dice "aquí hay un pájaro". Otro programa (el **tracker**) une esas marcas de imagen en
imagen para decir "este pájaro de ahora es el mismo que el de hace un segundo". El encargo era
medir solo la segunda parte: ¿une bien el tracker las marcas, o confunde unos pájaros con
otros?

## 2. Con qué se compara

Para medir hace falta una "respuesta correcta". Teníamos tres candidatas, y cada una sirve para
afirmar algo distinto:

- **Ground truth** (etiquetado a mano): una persona marcó, imagen por imagen, dónde está cada
  pájaro y cuál es cuál. Comparar contra esto mide **exactitud**: si el tracker acierta.
- **La nube**: la salida de otro sistema de seguimiento más pesado. Comparar contra esto mide
  **paridad**: si el tracker se parece a ese otro sistema. No dice quién tiene razón.
- **El baseline congelado**: la salida del propio tracker guardada el 22 de septiembre.
  Comparar contra esto mide **regresión**: si algo ha cambiado desde entonces.

Cada reporte dice en su primera línea cuál de las tres afirmaciones está haciendo.

Hay dos clips. El de la **bandada** (1009 imágenes, 40 segundos) tiene 25 pájaros etiquetados
con 10,142 marcas; son pájaros diminutos, de unos 9 por 7 píxeles, y dos de cada tres vuelan a
menos de 20 píxeles de otro. El de la **turbina** (671 imágenes) tiene un solo pájaro
etiquetado durante 241 imágenes, cruzando por delante de las palas.

## 3. Lo que se construyó, en orden

**Fase 0, mirar antes de construir.** Se inventarió el etiquetado, se comprobó que las
coordenadas y la numeración de imágenes coinciden entre etiquetado, detector y vídeo, y se
verificaron todas las cifras previas. Dos sorpresas: el etiquetado tiene 25 pájaros y no 40
(resultó ser intencionado: solo se etiquetó la primera bandada), y las 471 detecciones que el
detector produce en la esquina superior izquierda caen sobre el reloj de fecha y hora grabado
en el vídeo: el detector confunde los dígitos que cambian con pájaros. También se leyó el
código del tracker para saber, con certeza, cuándo una fila de su salida es una detección real y
cuándo es una "estimación" (el tracker sigue escribiendo la última posición conocida de un
pájaro durante hasta 29 imágenes después de perderlo).

**Fase 1, el vocabulario común.** Se definieron las estructuras de datos con los mismos nombres
que usa el repositorio de la empresa, para poder trasladar el trabajo después. Se escribió un
"traductor" por cada fuente (etiquetado, nube, detector, tracker) hacia ese vocabulario, y un
almacén donde cada resultado queda guardado con una huella digital de todo lo que lo produjo
(qué vídeo, qué detecciones, qué parámetros, qué versión del código). Así cualquier número se
puede rastrear semanas después.

**Fase 2, ejecutar el tracker de forma controlada.** Un programa que corre el tracker sin
cambiarle una línea, pero anota en cada fila si fue una detección real o una estimación, y
deja junto a la salida un manifiesto con la procedencia. Se comprobó que reproduce byte a byte
la salida guardada del 22 de septiembre. También genera "detecciones perfectas" a partir del
etiquetado, y versiones deliberadamente estropeadas de esas detecciones (quitando un
porcentaje, moviéndolas unos píxeles, añadiendo falsas) para ver cómo reacciona el tracker.

**Fase 3, las métricas.** Se usó TrackEval, la librería estándar que usan las competiciones
académicas de seguimiento, con una adaptación necesaria: la medida habitual de "misma caja"
(solape de rectángulos) no funciona con pájaros de 9 píxeles, así que se mide por distancia
entre centros, con 8 píxeles por defecto y pruebas a 4, 6 y 12. Las tres métricas principales:

- **HOTA** (de 0 a 1): la nota global. Combina "¿encontró los pájaros?" y "¿los siguió sin
  confundirlos?".
- **MOTA**: una nota clásica que penaliza mucho las falsas alarmas; puede ser negativa.
- **IDF1**: qué fracción del tiempo cada pájaro llevó su identidad correcta.

Además del número, el sistema lista cada confusión de identidad (en qué imagen, qué pájaro,
qué identidades se intercambiaron) y cada identidad del tracker que no corresponde a ningún
pájaro, para poder ir a mirar el vídeo en ese punto.

**Fase 4, comprobar que el medidor mide bien.** Se verificó que nuestros números coinciden
exactamente con los de TrackEval ejecutado por su vía oficial (0 diferencias en 26 campos), que
el emparejamiento ocurre exactamente a la distancia configurada (8.00 píxeles sí, 8.01 no), y
se contrastó con el evaluador que ya tiene la empresa, explicando cada diferencia. 35 pruebas
automáticas quedan en la carpeta `tests/`.

**Fase 5, los experimentos.** 98 ejecuciones del tracker y 102 evaluaciones, resumidas abajo.

## 4. Qué se aprendió

**El tracker, por sí solo, asocia bien.** Cuando se le dan las detecciones perfectas del
etiquetado (experimento E3), produce exactamente 25 identidades para 25 pájaros, con HOTA 0.96
e IDF1 0.97. Solo comete 17 confusiones, concentradas en dos momentos: cuando entra un pájaro
nuevo cerca de otro ya seguido (el seguido "se queda" con el recién llegado durante un par de
imágenes), y en un cruce entre dos pájaros que vuelan pegados. En la turbina es casi perfecto
(HOTA 0.99).

**Con las detecciones reales el resultado es malo, pero la culpa es sobre todo del detector.**
Contra el etiquetado (E1), HOTA baja a 0.27 e IDF1 a 0.18. La razón principal: el detector
real solo encuentra el 17 % de los pájaros etiquetados (pone una caja ancha sobre varios
pájaros en fila, o no los ve). El tracker no puede seguir lo que no se detecta. Además, 43 de
sus 78 identidades en la bandada están sobre el reloj grabado en el vídeo, no sobre pájaros;
por eso el sistema permite ignorar esa zona y muestra los resultados con y sin ella.

**El punto débil real del tracker son las detecciones perdidas.** El experimento E4 estropea
las detecciones perfectas de forma controlada. Mover las cajas 1 píxel no afecta. Pero quitar
un 10 % de las detecciones multiplica por ocho las confusiones de identidad (de 18 a unas 150),
y quitar un 20 % hunde HOTA de 0.96 a 0.51. Y lo hace de una forma concreta: el número de
identidades no sube; lo que pasa es que, mientras un pájaro está "en estimación", su
identidad salta a un vecino. En una bandada donde los pájaros vuelan a 17 píxeles unos de otros,
eso ocurre constantemente. Las falsas detecciones añadidas agravan el efecto.

**Los parámetros del tracker no arreglan eso.** El barrido E5 prueba 12 combinaciones de los
dos parámetros principales (cuánto tiempo espera a un pájaro perdido, y cuántas detecciones
seguidas pide antes de creer que algo es un pájaro). Con detecciones reales, la nota global no
se mueve (HOTA entre 0.271 y 0.275). Exigir 5 detecciones seguidas en vez de 3 elimina
identidades falsas (de 35 a 25) sin perder nada. Esperar 60 imágenes en vez de 30 no cambia
absolutamente nada: ningún pájaro vuelve a engancharse después de 30.

**La nube no sirve como respuesta correcta.** Solo cubre el 15 % de los pájaros etiquetados de
la bandada; la paridad con ella (E2) es baja (IDF1 0.50) y no dice nada sobre quién acierta.

## 5. Sobre la segunda bandada sin etiquetar

En el vídeo de la bandada hay dos bandadas y solo se etiquetó la primera. El detector y el
tracker, en cambio, intentan seguir todo lo que ven, incluida la segunda. ¿Afecta a la
comparación? Sí, a la mitad de las métricas, y se midió cuánto:

- De las 2180 filas del tracker que no caen sobre ningún pájaro etiquetado, 1688 están a más
  de 50 píxeles de cualquier pájaro etiquetado, casi todas entre las imágenes 200 y 600. Son
  cinco trayectorias largas (de 47 a 262 detecciones cada una) que cruzan el ancho entero un
  poco por encima de la bandada etiquetada: la segunda bandada. Hay además once identidades
  cortas que aparecen siempre en el mismo punto, que parece la punta de la pala.
- Al evaluar, todo eso cuenta como "falsa alarma", porque el etiquetado dice que ahí no hay
  nada. Eso castiga las métricas que miden falsas alarmas: MOTA, la precisión de identidad y
  la cuenta de identidades sobrantes. No castiga las que miden si los pájaros etiquetados se
  encontraron y se siguieron bien: pájaros perdidos, confusiones de identidad y continuidad.

Para cuantificarlo se añadió una opción que descarta la salida del tracker que está lejos de
todo pájaro etiquetado en esa imagen (a 50 píxeles). Con ella, en el run real de la bandada:

| | sin la opción | con la opción (50 px) |
|---|---|---|
| falsas alarmas (FP) | 2180 | 492 |
| MOTA | -0.07 | +0.10 |
| precisión de identidad (IDP) | 0.33 | 0.59 |
| HOTA | 0.273 | 0.294 |
| identidades del tracker | 35 | 18 |
| pájaros perdidos (FN) | 8508 | 8508 |
| confusiones de identidad | 156 | 156 |
| IDF1 | 0.180 | 0.204 |

Conclusión: la segunda bandada infla las falsas alarmas y hace que MOTA parezca peor de lo
que es, pero no cambia ninguna conclusión de fondo: el recall sigue en el 16 %, las confusiones
siguen siendo 156, y la nota global sube solo de 0.27 a 0.29. Los experimentos E3, E4 y E5 no
se ven afectados, porque ahí las detecciones salen del propio etiquetado y no incluyen la
segunda bandada. Y en el experimento con detecciones reales, las identidades que el tracker
crea sobre la segunda bandada son trayectorias largas y limpias (hasta 262 detecciones
seguidas), lo que confirma que el tracker funciona cuando el detector le da buen material.

Las dos formas de tratarlo, a tu elección: usar la opción de proximidad en los reportes de la
bandada (ya disponible con `--reference-proximity-px 50`, y los reportes lo dejan escrito), o
etiquetar la segunda bandada, que haría innecesaria la opción y daría más datos de prueba.

## 6. Qué no está hecho y qué conviene decidir

- El etiquetado de la turbina solo cubre un pájaro; en ese clip solo son defendibles las
  métricas de "¿se encontró y se siguió ese pájaro?".
- Las curvas de robustez están en tablas; no se generaron gráficos porque la librería de
  dibujo no estaba entre las dependencias acordadas.
- La zona del reloj que se ignora en la bandada la elegí yo (rectángulo de 721 por 400 píxeles
  arriba a la izquierda). Conviene que la confirmes.
- Nada está en control de versiones: la carpeta no es un repositorio git.

## 7. Dónde está cada cosa

| carpeta | contenido |
|---|---|
| `ground_truth/` | copia del etiquetado con sus huellas digitales |
| `evaluation/` | el evaluador (lee salidas terminadas y reporta; nunca ejecuta el tracker) |
| `experiments/` | el ejecutor del tracker y las recetas de los experimentos |
| `tests/` | 35 pruebas automáticas y dos scripts de validación |
| `outputs/runs/` | las 98 salidas del tracker con sus manifiestos |
| `outputs/reports/` | `SUMMARY.md` con todas las tablas y un reporte por ejecución |
| `outputs/phase0` a `phase5` | el resumen técnico de cada fase |
| `evaluation/quick_metrics.py` | script suelto para sacar HOTA, MOTA e IDF1 de cualquier CSV |
