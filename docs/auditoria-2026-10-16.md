# Auditoría del repositorio y plan de trabajo

> **Revisión editorial de *The Fujioka Variable*** — por Alejandra Medina.
> Fecha: **16 de octubre de 2026**. Alcance: los 29 archivos del repositorio (`README.md`, `biblia/` completa, `arte-oficial/`, `personajes/jesus-fujioka/`, `assets/`).
> Método: lectura íntegra de los 10 documentos de la biblia (26,182 palabras), contraste interno cruzado entre secciones, y verificación externa de los datos dudosos en fuentes japonesas (Wikipedia JP, prensa de la industria, sitios oficiales de estudio y discográfica).

---

## 1. Resumen ejecutivo

El repositorio está **muy por encima del promedio** de un proyecto de fan: la biblia de 10 secciones es trabajo de documentación serio, con jerarquía de fuentes, notas de verificación al pie y —lo más valioso— **un bloque de "Notas para el escritor" en cada sección** que ya define la mayoría de las reglas duras del universo. Eso no se ve en proyectos de fan: se ve en proyectos que se van a terminar.

Dicho eso, hay tres conclusiones:

1. **La investigación está completa; la obra no ha empezado.** El repositorio contiene 26,182 palabras de aparato (biblia, arte, ficha promocional) y **cero palabras de *The Fujioka Variable***. El `README.md` promete "Capítulos de la novela ligera" y "Notas del autor": ninguna de las dos existe todavía.
2. **Hay erratas objetivas y ya quedaron corregidas** (36 cambios en 11 archivos, con fuente de verificación en la tabla de la sección 3). Ninguna afectaba ideas de fondo, pero varias afectaban datos que se iban a repetir en la novela (una fecha de emisión, un título oficial en japonés, un nombre de seiyuu, dos romanizaciones).
3. **Falta lo que hace que una variable sea variable:** la ficha de Jesús Fujioka describe *cómo se ve* (altura, colores, gustos, el ajolote), pero no **qué cambia** en la historia. Sin esa decisión no se puede escribir el capítulo 1 sin riesgo de tirar trabajo después.

---

## 2. Inventario del repositorio

| Archivo | Palabras | Estado |
|---|---:|---|
| `README.md` | 137 | Portada correcta y concisa, pero promete contenido inexistente |
| `biblia/README.md` | 248 | Índice + declaración de completitud (15/10/2026) |
| `biblia/01-historia-produccion.md` | 2,222 | Completa. Producción, staff, música, recepción, seiyuu |
| `biblia/02-temporada-i.md` | 3,898 | Completa. Ficha, temas, 12 episodios, notas al escritor |
| `biblia/03-temporada-ii.md` | 4,187 | Completa. Ficha, temas, 12 episodios, notas al escritor |
| `biblia/04-pelicula.md` | 2,061 | Completa. Ficha, argumento por hermana, taquilla, notas |
| `biblia/05-personajes-principales.md` | 3,263 | Completa. Quintillizas, Futaro, Raiha, Rena, tabla rápida |
| `biblia/06-personajes-secundarios.md` | 2,768 | Completa. Familias, Asahi, secundarios, tabla de seiyuu |
| `biblia/07-diferencias-anime-manga.md` | 1,908 | Completa. Mapeo capítulo↔episodio y cortes documentados |
| `biblia/08-otros-medios.md` | 1,671 | Completa. Juegos, música, radio, libros, colaboraciones |
| `biblia/09-datos-curiosos.md` | 1,667 | Completa. Autor, encuestas, el "5", estado 2026 |
| `biblia/10-mestizos-extranjeros-japon.md` | 1,651 | Completa como investigación; **desalineada con el personaje** (ver §5) |
| `personajes/jesus-fujioka/README.md` + 5 PNG | 281 | Ficha tipo *promo card*, no ficha narrativa |
| `arte-oficial/README.md` + 9 imágenes | 220 | Atribución correcta; erratas de fecha y tipografía (corregidas) |
| `assets/poster.png` | — | Portada del repo |

**Volumen total:** 29 archivos, 6.9 MB, 26,182 palabras.

---

## 3. Errata corregida el 16/10/2026 (36 cambios, 11 archivos)

Todo lo de esta tabla se corrigió en el repositorio en esta misma revisión. La columna "fuente" indica con qué se verificó.

| # | Archivo | Decía | Dice ahora | Fuente |
|---|---|---|---|---|
| 1 | `README.md` (alt del póster) | `Hanayume` | `Hanayome` | Título oficial |
| 2 | `README.md` (pie) | propiedad de Negi **Haruma** | Negi **Haruba** | Wikipedia JP |
| 3 | `arte-oficial/README.md` | © Negi **Haruma** | © Negi **Haruba** | Wikipedia JP |
| 4 | `arte-oficial/README.md` | Temporada 2 **∫** (integral simple) | Temporada 2 **∬** (doble integral, símbolo oficial) | Logo oficial TBS |
| 5 | `arte-oficial/README.md` | Especial de TV **(2022)** | Especial de TV **∽ (2023)** | Sección 1 de la propia biblia |
| 6 | `biblia/01` §3.1 | "**calidad de animación irregular** ( *inconsistencies* de *sakuga*)" | "**calidad de animación irregular** (inconsistencias de *sakuga*)" | Redacción en español |
| 7 | `biblia/01` §3.2 | Emisión T2: "**7 al 26 de marzo de 2021**" | Emisión T2: "**del 8 de enero al 26 de marzo de 2021**" | Sección 3 de la biblia + MANTANWEB |
| 8 | `biblia/01` §4 | OP de la T2: **五等分の形** | OP de la T2: **五等分のカタチ** (katakana, título oficial) | Lisani!/Pony Canyon |
| 9 | `biblia/01` §3.1 | "Michinosuke Nakamura (中村路之将) y Miyabi Uta (雅楽)" | "中村路之将 y **雅楽雅** (romanización pendiente)" | Animatetimes: el segundo diseñador es 雅楽**雅** |
| 10 | `biblia/07` §7 | "Michinori Nakamura (T1)" | "中村路之将 y 雅楽雅 (T1)" — coherente con §01 | Animatetimes |
| 11 | `biblia/03` §3 (ep. 6) | "**Yusuke Takeda (武田)** , compañero" | "**Takeda Yūsuke (武田)**, compañero" | Orden japonés usado en todo el repo |
| 12 | `biblia/03` §3 (nota del ep. 12) | Sisters War: "(capítulo 59 en adelante)" | "(capítulos **78–86**; la confesión del 59 es su detonante)" | Sección 7 de la biblia |
| 13 | `biblia/04` §3 | "el equipo (Jinbo, Ōchi, Katsumata, Ōgiyama, Matsuyama, Chiba, Takemiya)" — nombres sin cargo | Cada nombre **con su cargo**: dirección, guion, personajes, arte, color (Matsuyama Aiko), fotografía (Chiba Daisuke), edición (Takemiya Mutsumi) | Animatetimes (staff del film) |
| 14 | `biblia/04` §1 | Ficha sin color/fotografía/edición/sonido | Añadidas 4 filas: 松山愛子, 千葉大輔, 武宮むつみ, 髙桑一 | Animatetimes |
| 15 | `biblia/05` §9 | "…en el epílogo. **seria**, aplicada…" | "…en el epílogo. **Seria**, aplicada…" | Ortografía |
| 16 | `biblia/05` §9 | "crítica de dulces semi-anónima **que es celebrities en** la industria" (frase rota) | "crítica de dulces semianónima **que la volvió celebridad en** la industria" | Redacción en español |
| 17 | `biblia/06` §1 y tabla §5 | Isanari: "**Satoru** Hino" | "**Satoshi** Hino (日野聡)" | Wikipedia JP |
| 18 | `biblia/06` §4 | "la **compañiera** de la primaria" | "la **compañera** de la primaria" | Ortografía |
| 19 | `biblia/06` §4 y tabla §5 | "Hisako **Higashiro**" | "Hisako **Higashijō** (東城日沙子)" | Lectura del kanji 東城 = Higashijō |
| 20 | `biblia/06` (nota 5) | "La serie siembra**这些** guiños" (resto en chino) | "La serie siembra **estos** guiños" | Redacción en español |
| 21 | `biblia/08` (nota 7) | "**Paraambientar** tu fic" | "**Para ambientar** tu fic" | Ortografía |
| 22 | `biblia/10` (título) | "Mestizos y Extranjeros en Japón (**ブロック** hāfu)" — resto editorial | "…en Japón (hāfu)" | Coherencia con el índice |
| 23 | `biblia/05`, `06`, `09` | Kyōka Yūki y Sanpei Yūki listados solo en kanji | **Romanizados** (Kyōka Yūki 京花優希 / Sanpei Yūki 三瓶雄樹), con nota de fuente | Wikipedia JP + sitio de su agencia (ambos en KENYU Office) |
| 24 | `biblia/07` §2 | Tabla de correspondencia con fronteras ambiguas (22 y 25 aparecían en dos episodios) | Añadida **nota de precisión** sobre las fronteras | Coherencia interna |

**Lo que no toqué a propósito:** la afirmación del `README.md` de que existen "capítulos de la novela ligera" y "notas del autor". No se corrige borrando: se corrige escribiéndolos.

---

## 4. Pendientes de verificación (5 puntos abiertos)

| # | Dónde | Problema | Recomendación |
|---|---|---|---|
| 1 | `biblia/01` §3.1, `biblia/07` §7 | La romanización de 中村路之将 (y de 雅楽雅) no consta en las fuentes consultadas. Antes decía "Michinosuke" en un archivo y "Michinori" en otro: **se contradecían** | Dejar el kanji (ya está así) o verificarlo en el *character design book* / libro de material oficial. No inventar lectura |
| 2 | `biblia/05` §10, `06` §4, `09` §5 | El crédito de Kyōka Yūki como **"la niña de la foto"** de Kioto no aparece literal en las fuentes: la ficha de la actriz acredita 女の子 (T2), 竹林 (T2/película) y 中野零奈 (película) | Ya redactado con la reserva correcta ("crédito niña"). Si alguien consigue los créditos finales del film, se cierra el círculo |
| 3 | `biblia/05` §6 (Nino) | "'Fū-kun' (apodo que le robó a Miku, **la inventora original**)" — Miku llama a Futaro "Fūtarō", no "Fū-kun"; la atribución del apodo a Miku no está documentada | Reescribir como: "apodo con el que **Nino marca territorio** tras su confesión (consciente de que Miku también le dice Fūtarō)" |
| 4 | `biblia/07` §4 | Cita del fandom japonés ("四葉のあの超名シーンが映画でカット") atribuida a "la videografía de reseñas japonesas" sin fuente concreta | Citarla con canal/URL o retirarla: es la única cita de la biblia sin origen trazable |
| 5 | `biblia/05` §3 | La escaleta del anime como fuente de los 178 cm de Futaro (ya usado también en la ficha de Fujioka) | Correcto, solo anotar que la biblia no debe dar **alturas de las quintillizas** (no se publicaron), regla que ya se respeta |

**Cerrado en esta revisión (dato que dudaba y quedó confirmado):** el cierre de taquilla del film —**~¥2,240 millones y ~1.7 millones de asistentes**— está correcto y bien citado (MANTANWEB 2023). El perfil de Haruba Negi (27/07/1991, Chita, Aichi) y el bloque musical del especial ＊ (五等分の笑顔 / メモリーズ) también quedaron verificados sin observaciones.

---

## 5. Hallazgos estructurales (lo importante)

### 5.1 La novela no existe todavía

| Lo que el `README.md` promete | Estado real |
|---|---|
| "Capítulos de la novela ligera" | **No hay carpeta de capítulos ni un solo capítulo** |
| "Notas del autor" | **No existen** |
| "Ilustraciones y arte conceptual" | ✅ `personajes/jesus-fujioka/` con 5 imágenes |

No hay **sinopsis larga**, **argumento**, **escaleta de volúmenes**, **mapa de capítulos**, **cronología interna con fechas** ni **hoja de continuidad**. Tampoco **guía de estilo** (punto de vista, tiempos verbales, tratamiento de honoríficos, política de términos japoneses, proporción de diálogo) ni **glosario**. Para una novela de más de 4,500 palabras por capítulo, eso es andar sin plano.

### 5.2 "La variable" todavía no es una variable

La ficha de Jesús Fujioka es una **promo card** (altura, ojos, colores, gustos, ajolote). Le faltan los datos que un personaje necesita para sostener una novela: **fecha de nacimiento**, estructura familiar, escuela y clase, heridas y arco, función dramática, voz propia (cómo habla, qué dice cuando no puede decir nada) y **su relación con cada una de las cinco**, una por una. Sobre todo, falta la respuesta a la única pregunta que importa: **¿qué cambia Fujioka cuando entra?** Una variable sin efecto medible no es una variable, es un invitado.

Tres detalles de la ficha, además, piden decisión consciente:

- **178 cm** es *exactamente* la estatura canónica de Futaro (sección 5). Si es deliberado, es un espejo potentísimo (dos chicos de la misma altura, uno rubio teñido del pasado y uno castaño del presente). Si es descuido, es una coincidencia que se va a leer como intención. Hay que firmarla.
- **El ajolote de la suerte** es el mejor hallazgo de la ficha: es el equivalente mexicano exacto del **amuleto de Raiha** (el objeto-hito de la temporada 1). Debe formalizarse como objeto-narrativo con reglas propias.
- **Apellido japonés + apellido mexicano.** Que el apellido japonés sea *Fujioka* significa que **el lado japonés de la familia es Fujioka**. De ahí se deriva todo lo demás (quién es el padre/madre japonés, en qué idioma se habla en su casa, cómo lo llaman en la escuela).

### 5.3 Desalineación entre la Sección 10 y el personaje

La sección 10 es un capítulo excelente de investigación **sobre la comunidad brasileña y peruana de Aichi** (28% de los brasileños de Japón viven ahí, Toyota como municipio más extranjero, el hito Miyamoto, el vocabulario hāfu/daburu/mikkusu). El personaje, en cambio, es **nipo-mexicano**: Fujioka + Hernández + ajolote, como el propio Chuy (Guadalajara).

No está mal —está **incompleto**. La comunidad mexicana en Japón existe y es distinta del patrón nikkei-dekasegi brasileño: hay que documentarla con el mismo rigor y decir con claridad qué comparte y qué no con la brasileña. Es la única sección de la biblia cuya tesis no aterriza en el personaje que va a protagonizar la novela.

### 5.4 La regla de oro que la biblia todavía no explota

La sección 10 lo dice mejor que yo: *"identidad ≠ apariencia"* es el argumento del abuelo, del test de los cinco vestidos y de las quintillizas de colores imposibles. Un personaje hāfu puede **encarnar** lo que la serie solo insinúa. Ese es el ángulo temático que hace que esta novela valga la pena: **no** "un chico nuevo entre cinco chicas", sino *"el chico que demuestra en carne propia la tesis de la serie"*. La obra ya te dio el argumento; falta decidir cómo se usa.

---

## 6. Plan de trabajo propuesto (7 fases)

| Fase | Entregable | Depende de |
|---|---|---|
| **0** | Auditoría del repositorio y errata ✅ *(este documento)* | — |
| **1** | **Reglas duras del AU** — una página que congela las decisiones creativas (ver §7). Sin esto, cualquier capítulo es trabajo a riesgo | Respuestas de Chuy |
| **2** | **Ficha narrativa completa de Jesús Fujioka** — biografía, familia, herida, arco, voz, tics, matriz de 5 relaciones (una con cada hermana), reglas del ajolote y su "número" dentro del sistema numérico de la obra | Fase 1 |
| **3** | **Biblia de la novela** — sinopsis larga, escaleta de volúmenes, mapa de capítulos con meta de palabras, cronología interna anclada al canon (2000 días, 5 de mayo, 14 de agosto, el festival) y hoja de continuidad de una página | Fases 1–2 |
| **4** | **Guía de estilo** — POV y tiempo verbal, tratamiento de honoríficos (-kun/-san/keigo) y apodos, política de términos japoneses en español, proporción diálogo/narración, longitud por capítulo y por parte (Wattpad) | Fase 3 |
| **5** | **Sinopsis de Wattpad + portada** — logline, sinopsis de escaparate, etiquetas, blurb de 200 palabras | Fase 3 |
| **6** | **Capítulo 1** (meta: 4,500+ palabras) + revisión editorial contra la hoja de continuidad | Fases 4–5 |
| **7** | **Calendario de publicación** y seguimiento de comentarios/lectores | Fase 6 |

**Recomendación de arranque:** Fase 1 y Fase 2 en la misma sesión de trabajo. Son cortas, y sin ellas la Fase 3 se convierte en adivinanza.

---

## 7. Decisiones que necesito de Chuy (para la Fase 1)

1. **¿Cuándo entra Fujioka?** (a) antes de la tutoría, (b) en el arco de Kioto/2.º año, (c) en el 3.er año con el grupo ya formado, (d) después de la película.
2. **¿Qué es "la variable"?** (a) sustituye a Futaro como tutor, (b) es el **sexto** que rompe la simetría del cinco, (c) es el catalizador que acelera la elección final, (d) es un testigo externo que humaniza a Futaro.
3. **¿El final sigue siendo Yotsuba?** (a) sí, respetamos el canon y la variable opera alrededor, (b) no, la variable reescribe el desenlace (y entonces hay que firmarlo con el lector desde el capítulo 1).
4. **Nivel de intervención:** conservador (nada del manga cambia; la variable vive en los huecos ya documentados: el verano en blanco, los capítulos no animados 36–38/72/77, la era universitaria) o radical (línea alternativa declarada desde el título).
5. **Los padres de Fujioka:** ¿el japonés es el padre o la madre? ¿Hernández viene del lado mexicano completo o hay mezcla? ¿En qué idioma se habla en su casa?
6. **¿Qué relación tiene con el pasado de Futaro?** (el rubio de primaria, Kioto, Takebayashi) — es la zona de máximo riesgo canónico y de máximo potencial.
7. **Formato de publicación en Wattpad:** capítulo largo partido en partes de ~1,500 palabras (mi recomendación) o capítulos de 1,500–2,000 y meta global más alta.
8. **Tono:** comedia romántica escolar con carga dramática (canon), drama puro, o misterio heredado de la obra.

---

## 8. Anexo: mapa de reglas duras ya disponibles en la biblia

No hay que inventar el reglamento: **está escrito, solo está disperso**. Este es el índice para consolidarlo en la Fase 3.

| Regla disponible | Fuente |
|---|---|
| La novia es Yotsuba; Rena = Yotsuba (pasado y campana) | `04` §5 (1–3) |
| Distinguir a las cinco = prestar atención; tesis del abuelo | `04` §5 (5), `05` §… abuelo, `06` §abuelo |
| Cuatro besos + uno que no (firma de la película) | `04` §5 (4) |
| Oficios y materias del epílogo (canon intocable) | `05` §11–12 |
| Tratamiento/apodos como termómetro emocional | `05` §12 (5) |
| Futaro **no** se ablanda: su crecimiento es social | `05` §12 (7) |
| Cómo distinguirlas (piercing, listones, audífonos, conejo, estrellas) | `05` §12 (1) |
| El "5" como firma estilística y de titulación | `09` §6, `09` §8 (5) |
| Boda = día 2000; brújula de fechas | `09` §8 (6), `02` §3 |
| Fuera de cámara: caps. 36–38, 72, 77; el verano en blanco es territorio libre | `07` §8 (2), `08` §8 (3) |
| El inglés como puerta canónica de "lo extranjero" | `10` §2, `10` §7 (7) |
| Apariencia ≠ identidad (tesis anti-esencialista) | `10` §2, `10` §7 (2) |
| Nada de caricatura del personaje mestizo | `10` §7 (8) |
| Aichi real: Nihon Fukushi, Ōtagawa, Nagashima Spaland | `09` §8 (3) |
| Objetos-Recuerdo rastreables (amuleto de Raiha) | `05` §12 (6), `02` §5 (4) |

---

*Auditoría redactada por Alejandra Medina el 16 de octubre de 2026. Los datos verificados externamente provienen de Wikipedia JP, Animatetimes, MANTANWEB, Lisani! y Pony Canyon. Las interpretaciones y recomendaciones editoriales están marcadas como tales.*
