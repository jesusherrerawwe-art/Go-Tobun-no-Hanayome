# Verificación previa al proyecto — *The Fujioka Variable*

> **Lo que pediste:** que confirmara que la biblia y el resto del repositorio están en orden antes de empezar.
> **Resultado general: ✅ EL REPOSITORIO ESTÁ EN ORDEN.** 2 hallazgos menores corregidos en esta pasada (enlace roto y una edad inconsistente). 5 pendientes conocidos que no bloquean. 3 decisiones de producción que el Plan de Acción debe cerrar.
>
> Verificación hecha por Alejandra Medina — 16 de octubre de 2026.

---

## 1. Checklist de estado

| # | Punto verificado | Resultado |
|---|---|---|
| 1 | Árbol de trabajo limpio (`git status`) | ✅ Sin cambios sin guardar |
| 2 | Rama sincronizada con el remoto (mismo SHA) | ✅ `f05d28b` local = remoto. 4 commits por delante de `main` |
| 3 | Historial legible y con mensajes útiles | ✅ 4 commits de esta revisión, todos descriptivos |
| 4 | Completitud de la biblia (10 secciones + índice) | ✅ Las 10 completas, índice al día |
| 5 | Enlaces e imágenes internas | ✅ **0 roto(a)s** (se corrigió 1: `biblia/07`, un enlace mal formado a "2024") |
| 6 | Coherencia de nombres del autor | ✅ "Haruba" en todo el repo; "Haruma" solo aparece en la tabla de erratas de la auditoría, como dato histórico |
| 7 | Coherencia de romanizaciones | ✅ 36 erratas resueltas; Kyōka Yūki y Sanpei Yūki ya romanizados con fuente |
| 8 | Terminología japonesa unificada | ✅ "Kioto" 36 veces / "Kyoto" 0; símbolos oficiales ∬ (14), ∽ (29), ＊ (15) correctos |
| 9 | Atribución y disclaimers de derechos | ✅ Presentes en `README.md` y `arte-oficial/README.md` (proyecto de fan, sin fines de lucro, © Haruba/Kodansha/Comité) |
| 10 | Inconsistencia detectada y corregida en esta pasada | ⚠️→✅ Edad de Jesús en la Fase 2: decía "16, cumple 17" y la fecha de nacimiento fijada (2/11/2001) implica "cumple 16". **Corregido** |

---

## 2. Inventario actual (37,265 palabras en 18 archivos Markdown + 15 imágenes)

| Bloque | Palabras |
|---|---:|
| **Biblia (10 secciones + índice)** | **25,988** |
| `docs/` (auditoría, Fase 1, Fase 2, pacto, esta verificación) | **10,830** |
| Ficha del personaje (repo) | 299 |
| Portadas y READMEs | 435 |
| **TOTAL** | **37,265** |

Nuevo desde tu última visita: `docs/auditoria-2026-10-16.md`, `docs/fase-1-decisiones.md`, `docs/fase-2-ficha-narrativa-fujioka.md`, `docs/pacto-ale-chuy.md` y este documento.

---

## 3. Hallazgo bonito: el póster ya está en el repositorio

Verifiqué por **huella digital (md5)** el póster que me acabas de mandar contra el que está en `assets/poster.png`:

```
93673fde29ea965074f7284f9153813f  poster.png (el que me mandaste)
93673fde29ea965074f7284f9153813f  assets/poster.png (el del repositorio)
```

**Son el mismo archivo.** El póster del repositorio ya es la versión con Jesús Fujioka **en el lugar de Futaro**, dentro del visual oficial de la franquicia, con el **ajolote bordado en la camisa**. Es decir: la portada del proyecto ya declara su tesis en una sola imagen — el chico está exactamente donde estaba el tutor.

**Nota profesional:** al ser una edición sobre arte oficial, la línea de © 春場ねぎ・講談社／「五等分の花嫁」製作委員会 debe seguir visible y el disclaimer de proyecto de fan sin fines de lucro debe acompañarlo siempre. El repositorio ya cumple ambas cosas; solo hay que mantener la regla cuando el póster viaje a Wattpad.

---

## 4. Pendientes conocidos que NO bloquean el arranque

Los cinco puntos abiertos de la auditoría siguen abiertos (romanización de 中村路之将/雅楽雅, el crédito exacto de Kyōka Yūki como "niña de la foto", la atribución del apodo "Fū-kun" a Miku, la cita sin fuente del fandom japonés y la regla de no publicar alturas de las quintillizas). **Ninguno afecta la escritura de la novela**: son datos de la obra original, no de nuestra historia. Se cierran cuando aparezca la fuente; mientras, se quedan marcados como "pendiente de verificar".

---

## 5. Lo que el prompt de hoy obliga a revisar (aviso honesto)

Tu nuevo enunciado cambia **la premisa arquitectónica**: *Jesús Fujioka reemplaza a Futaro Uesugi al principio de la historia*. Eso deja desalineadas algunas partes de la ficha de Fase 2 que yo misma escribí, y prefiero decírtelo yo antes de que lo descubras:

| Parte de la ficha de Fase 2 | Qué pasa ahora |
|---|---|
| §9, lista negra, punto 1: "no es rival romántico de Futaro" | **Obsoleto**: es el protagonista y "se enamora" (ya me lo confirmaste) |
| §10.6: la amistad con Futaro | **A revisar**: ¿Futaro existe en este mundo, y cómo? |
| §11, acto I: "el tutor sigue siendo Futaro" | **Obsoleto**: la premisa dice lo contrario |
| §12, pregunta 1 ("¿se enamora?") | **Respondida**: sí ❤️ |
| Toda la ficha | **Sigue sirviendo el 80%**: identidad, genealogía, voz, ajolote, las cinco hermanas. Lo que cambia es su lugar en la historia, no quién es |

**Esto no es un problema: es exactamente lo que el Plan de Acción debe cerrar.** Pero hay una pregunta grande que sí necesito que decidas, porque de ella depende casi todo lo demás (ver §6.1).

---

## 6. Las tres decisiones de producción que el Plan debe cerrar

### 6.1 La sustitución: ¿trasplante completo o injerto? ⚠️ *la más importante*

Si Futaro sale de la ecuación, hay que decidir **quién se queda con cada pieza de su arquitectura**, porque no son adornos: son motores.

| Pieza del canon | Pregunta |
|---|---|
| **Raiha** (la hermana menor) | ¿Existe? ¿Es hermana de Fujioka? ¿Es otra persona? ¿Desaparece? |
| **La pobreza de los Uesugi** (el motor de que Futaro acepte el trabajo) | ¿Qué motiva a Fujioka a ser tutor? Él ya tiene familia y no pasa hambre |
| **Maruo** (el padrastro que contrata) | ¿Por qué contrataría a Fujioka? ¿Sigue siendo por el historial escolar? |
| **El pasado de Kioto / la foto doblada** | ¿Ese misterio existe? ¿Y si existe, de quién es? |
| **La boda del "día 2000"** | ¿Sigue habiendo boda? ¿Con quién? |
| **Kintarō** (el alter ego rubio) | ¿Lo toma Fujioka? ¿O desaparece con Futaro? |

**Mi recomendación:** decidir esto **antes** de escribir el capítulo 1, no sobre la marcha. Es la diferencia entre una novela que se sostiene y un castillo de naipes que se cae en el capítulo ocho.

### 6.2 El presupuesto de palabras (matemática pura)

| Escenario | Palabras por capítulo | Total (26 capítulos) | Equivalente |
|---|---:|---:|---|
| Ambicioso | 4,500 | **117,000** | ~3 volúmenes de novela ligera |
| **Recomendado** | **2,500–3,000** | **65,000–78,000** | 1 volumen largo / 2 tomos |
| Ágil | 1,800 | 46,800 | 1 novela ligera estándar |

**Contexto:** una novela ligera japonesa promedio pesa entre 40,000 y 60,000 palabras. Lo que tú pides (26 capítulos, cada uno con diseño y estructura propios) es **más que un volumen**: es una serie de dos tomos. Hay que decidirlo con el calendario en la mano, no con la ilusión.

### 6.3 El calendario (el cumpleaños de Roberto) ⚠️

Me dijiste que es un **regalo de cumpleaños con acceso anticipado** para tu hermano menor. **Necesito la fecha.** No es un detalle: de ella sale el ritmo de escritura, el tamaño de cada capítulo y si podemos permitirnos editar dos veces o una. Dime el día y yo te devuelvo una tabla de entregas realista.

---

## 7. El registro que propongo para la parte "Ecchi" (con fuente, no con opinión)

Me pediste **Slice of Life + Ecchi**. Lo anoto y lo escribo con gusto, pero tengo que darte dos datos verificados antes de firmar nada, porque es exactamente lo que me toca hacer:

**1) La propia obra tiene una regla escrita.** En tu `biblia/01` §1 (filosofía de Haruba Negi) está documentado, con el término original: **「パンチラしたら負け」 — "si enseñas bragas, pierdes"**. Haruba evitó deliberadamente el fanservice explícito y sostuvo la serie con personalidad y expresividad. *El ecchi de esta franquicia es de situación, no de exposición.*

**2) La plataforma tiene reglas, y las verificamos hoy.** Las *Content Guidelines* de Wattpad (actualizadas el 10 de agosto de 2026) dicen, textualmente: se permite "romantic or sexual relationships as part of a broader story" y "non-explicit or implied sexual content"; el contenido explícito solo se admite **entre personas adultas (18+)** y bajo la etiqueta **Mature (17+)**, siempre que "supports the story, not the main purpose"; y hay **tolerancia cero a cualquier contenido sexual con menores**. Se elimina además todo contenido "created primarily for sexual arousal".

**Traducción a nuestro caso:** nuestros protagonistas son estudiantes de 16–17 años. El registro que **sí** se puede escribir —y que además es el de la obra— es el **ecchi de situación**: la tensión, el doble sentido, el gag, la cámara que nunca es vulgar, el momento que se corta justo antes. Eso lo escribo, y lo escribo bien. El registro explícito, con estas edades y en esa plataforma, **no es una decisión de estilo: es una puerta cerrada**, y prefiero decirte por qué antes de que lo intentemos.

**Necesito de ti:** la **edad de Roberto** y el **registro** que quieres (① comedia sugerente al estilo del anime — mi recomendación; ② sugerente con alguna escena intensa pero nunca explícita; ③ otra cosa, lo hablamos).

---

## 8. Resumen ejecutivo para que no tengas que releer

- ✅ **El repositorio está en orden.** Biblia completa, enlaces sanos, git limpio y sincronizado, póster del proyecto en su lugar.
- ✅ **2 hallazgos corregidos hoy:** un enlace roto en `biblia/07` y una edad inconsistente en mi propia ficha de Fase 2.
- ⚠️ **5 pendientes documentales** (ninguno afecta la novela).
- ⚠️ **3 decisiones de producción pendientes:** cómo sustituimos a Futaro (§6.1), cuántas palabras caben (§6.2) y para cuándo (§6.3).
- ⚠️ **1 acuerdo de registro:** el ecchi de situación (§7), con la edad de Roberto sobre la mesa.
- 📌 **Dato para tu tranquilidad:** la Fase 2 sigue siendo el 80% válida. La reviso entera cuando el Plan de Acción quede firmado, y esa revisión la hago yo por mi cuenta.

---

*Verificado el 16 de octubre de 2026. Política de plataforma consultada en `policies.wattpad.com/content` (guías vigentes desde el 10/8/2026) y cobertura de prensa sobre su aclaración de criterios. Datos de la obra: secciones 1–10 de esta biblia.*
