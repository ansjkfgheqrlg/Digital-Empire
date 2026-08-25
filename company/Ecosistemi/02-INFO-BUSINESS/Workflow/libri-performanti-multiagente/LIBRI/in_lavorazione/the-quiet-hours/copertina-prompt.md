# Prompt copertina — The Quiet Hours (versione 2)

**Perché si rifà.** La prima era un collage: viso, chiave, camice, stetoscopio, incidente,
cornice crepata, telefono, sangue. Otto elementi che si contendono l'occhio, nessun punto
focale, e il titolo sopra un viso, quindi senza contrasto. Le due copertine del catalogo che
funzionano (*The Ninth Winter*, *The Second-Hand Spellbook*) hanno **una scena sola** e un
terzo superiore quasi vuoto.

**Autore: DIGITAL EMPIRE.** Su tutte le copertine, sempre. Mai pseudonimi.

**Quando torna il PNG:**
```
python -m engine.kdp consegna the-quiet-hours --cover <percorso.png>
```

**Controlla prima di darmelo:**
- **almeno 1800×2700 px** (le ultime due erano 139 e 171 DPI reali contro i 300 di KDP)
- **THE QUIET HOURS** e **DIGITAL EMPIRE** scritti esatti
- verticale, e il titolo leggibile rimpicciolito a francobollo
- **una scena sola**: se ci sono più di due oggetti riconoscibili, è sbagliata

---

## PROMPT

```
Book cover illustration for a psychological thriller. Vertical portrait format, 2:3 aspect
ratio, at least 1800 x 2700 px. NOT square. High resolution, crisp, print-quality, sharp
focus, no blur, no noise, no compression artifacts.

ONE SCENE ONLY. This is the most important instruction in this brief. Do not add extra
objects, insets, vignettes, split panels, collage elements or secondary images. No cars, no
photographs, no phones, no keys, no medical equipment. If a viewer can name more than two
objects in this image, the composition has failed.

SCENE:
A long empty corridor in a care home, at three o'clock in the morning, seen straight down
its length from one end. Institutional but not clinical: a worn vinyl floor with a soft
sheen, painted walls in a dull warm beige, a wooden handrail running along both sides, a
row of identical closed doors receding into the distance on the left and the right.

Most of the corridor is unlit. The overhead lights are off. The only illumination comes
from two sources: a dim emergency strip low along the skirting, and one single door, far
down on the left, standing very slightly ajar with warm yellow light spilling out across
the floor in a narrow wedge.

At the far end of the corridor, small in the frame and almost lost in the dark, the
silhouette of a woman in nurse's scrubs, standing still, facing away from the viewer. She
is not walking. She has stopped. She is very small: she should occupy no more than one
twelfth of the image height. The corridor dominates her completely.

MOOD AND LIGHT:
Deep quiet. Not horror, not gore, not a jump scare. The unease of being awake when
everybody else is asleep, and of not being certain how you got where you are standing.
Heavy stillness. The light is low and directional and leaves most of the frame in shadow.

COLOUR PALETTE:
Desaturated and dark: charcoal, deep slate blue, muddy beige, near-black in the corners.
One warm accent only, the yellow light from the ajar door. No red. No blood. No teal-and-
orange grading. No neon.

STYLE:
Painterly digital illustration in the tradition of upmarket psychological suspense: closer
to an oil painting or a high-end matte painting than to photography. Controlled brushwork.
Fine detail on the floor reflection and the door frames. Restrained and adult. NOT
photobashed, NOT a collage, NOT cinematic poster art with multiple focal points.

COMPOSITION:
The upper third of the image is dark ceiling and the top of the corridor walls, kept
deliberately simple and almost empty, so the title sits there with nothing behind it. The
vanishing point sits slightly below centre. The bottom eighth is dark floor, clear, for the
author name. Strong one-point perspective. Plenty of negative space.

TEXT ON THE COVER, render all of the following as part of the image, spelled exactly:

Main title, upper third, centred, very large, all capitals, in a clean high-contrast serif
with tight letter-spacing, in cold bone white, sitting on the dark ceiling area with no
object behind it:
THE QUIET HOURS

Directly beneath the title, much smaller, about one fifth of the title height, centred, in
spaced small capitals, same white at lower opacity:
A PSYCHOLOGICAL THRILLER

At the bottom of the cover, centred, small, larger than the subtitle but far smaller than
the title, same serif, all capitals, bone white:
DIGITAL EMPIRE

Spell every letter exactly as written above. Do not paraphrase, translate, abbreviate or
re-order the text. Do not add any other words, taglines, review quotes, series numbering,
publisher marks, logos, borders or frames. No watermark. No signature.

The title must remain clearly legible when the whole cover is reduced to thumbnail size.
```
