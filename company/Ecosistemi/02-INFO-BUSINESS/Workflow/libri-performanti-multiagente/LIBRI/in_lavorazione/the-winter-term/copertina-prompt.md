# Prompt copertina — The Winter Term

Da dare a un generatore di immagini (LM Arena, Midjourney, Ideogram). Il testo del titolo
deve essere disegnato DENTRO l'immagine: il codice non lo riscrive sopra.

---

## Prompt (inglese, da incollare intero)

Vertical 2:3 book cover, high resolution, dark academia mystery novel.

SCENE: a lone eighteen-year-old girl in a heavy charcoal wool coat and a dark green college
scarf, seen from behind and slightly below, standing at the foot of a vast Georgian boarding
school on an English moor. She is small against the building. Her back is to the viewer, her
head turned just enough to show the line of her jaw and one ear, never her full face. Snow
lies thin and grey over dead heather. A single line of her footprints comes toward the
viewer through the snow, and there is a second, older line of footprints beside hers that
stops halfway and does not continue.

ARCHITECTURE: an eighteenth-century stone college, four storeys, tall sash windows in
symmetrical rows, a square clock tower on the left with a lit bell chamber, iron railings, a
gravel forecourt swallowed by snow. Every window is dark except three, which glow a weak
amber. Bare black elms frame the right edge.

ATMOSPHERE AND LIGHT: late winter afternoon, roughly four o'clock, the light already
failing. Freezing fog rising from the valley behind the building so the roofline dissolves
into it. Overcast, no sun, no visible sky beyond a pale grey wash. The only warm light comes
from the three lit windows and the bell chamber, small and far away and not enough. Mood:
cold, hushed, beautiful, wrong.

PALETTE: dominated by slate grey, bone white, wet charcoal and deep bottle green. Accent
colours only in the window light, a muted amber and a dull gold. One single note of oxblood
red in the girl's gloves. No other saturated colour anywhere.

STYLE: painterly digital illustration with the texture of oil on board, visible brushwork in
the sky and the snow, soft edges in the fog and crisp edges on the architecture. Restrained
and literary, in the tradition of prestige dark academia hardback jackets. Fine film grain
over the whole image. No photorealism, no 3D render, no glossy CGI, no anime, no cartoon.

COMPOSITION: the college occupies the lower two thirds of the frame, the girl stands small
in the lower left third, the footprints lead the eye from the bottom edge up to her. The top
third of the image is empty fog and sky, deliberately kept clear and low-contrast so the
title sits on it cleanly. A narrower clear band across the very bottom for the author name.

TEXT ON THE COVER, rendered exactly and spelled letter for letter:

Title, across the empty upper third, in three stacked lines, centred:
THE
WINTER
TERM

Set in a high-contrast classical serif with sharp thin serifs, in the manner of Didot or
Bodoni, in bone white with a very faint warm glow behind the letterforms so they stay legible
against the grey fog. Generous letter spacing. The word WINTER is the widest line and sets
the measure. The title block takes about a third of the image width at minimum and must stay
readable at thumbnail size.

Subtitle, immediately under the title, centred, much smaller, in spaced small capitals,
muted gold:
A DARK ACADEMIA MYSTERY

Author name, along the bottom clear band, centred, small capitals, bone white, about half the
height of the subtitle:
MAREN ASHCROFT

NEGATIVE, do not include: any other text, no taglines, no review quotes, no publisher logo,
no watermark, no signature, no page numbers, no borders, no decorative frames, no ornamental
corners, no faces looking at the viewer, no blood, no skulls, no owls, no floating books, no
magical or fantasy elements, no modern cars, no people other than the single girl.

---

## Se l'immagine torna senza testo o col titolo sbagliato

Solo in quel caso, e non come norma:
```
python -m engine.kdp consegna the-winter-term --cover <file.png> --scrivi-titolo
```
