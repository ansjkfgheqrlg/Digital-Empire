# Prompt copertina — The Second-Hand Spellbook

**Generala adesso, mentre scrivo i capitoli.** Il prompt è completo: testo della copertina
incluso, lo disegna il modello.

**Quando torna il PNG:**
```
python -m engine.kdp consegna the-second-hand-spellbook --cover <percorso.png>
```

**Prima di darmelo, controlla:**
- **almeno 1600×2400 px**, meglio 1800×2700 (la scorsa volta erano 832×1248 = 139 DPI reali
  contro i 300 che KDP chiede: bella in miniatura, morbida sul cartaceo)
- il titolo si legge quando rimpicciolisci a francobollo
- **THE SECOND-HAND SPELLBOOK** scritto esattamente così, col trattino
- verticale, non quadrato

---

## PROMPT

```
Book cover illustration for a cozy fantasy novel. Vertical portrait format, 2:3 aspect
ratio, at least 1800 x 2700 px. NOT square. High resolution, crisp, print-quality, sharp
focus edge to edge, no blur, no noise, no compression artifacts.

SCENE:
The warm interior of a small second-hand bookshop at dusk, seen from just inside the
doorway. Crowded wooden shelves lean slightly with age. In the centre of the composition,
a tall ladder rests against a high shelf near the ceiling, and on that top shelf a row of
books glows very faintly from within, a soft honey-gold light leaking out from between the
pages and spilling down the ladder rungs. The books lower down are ordinary, unlit, worn.

A woman in her mid-thirties stands at the foot of the ladder with her back three-quarters
to the viewer, one hand resting on a rung, looking up at the glowing shelf. Simple modern
clothes, dark cardigan, hair tied back. She is calm, not frightened. A grey cat sits on
the counter behind her, watching the same shelf.

Through the shop window on the left, a cold blue evening: a harbour, masts, rain on the
glass. The contrast between the cold blue outside and the warm amber inside is the whole
point of the image.

MOOD AND LIGHT:
Warm, safe, quietly enchanted. Lamplight and the gold glow from the high shelf. Autumn
seaside evening. Inviting, lived-in, a little dusty. Gentle wonder, NOT spooky, NOT
gothic, NOT menacing. This should feel like a place you would want to stay in.

COLOUR PALETTE:
Warm amber, honey gold, worn leather brown, soft cream for the lamplight. Cold slate blue
and grey confined to the window and the world outside. No neon, no purple magic clichés,
no sparkles or floating glitter particles.

STYLE:
Painterly illustrated cover art in the tradition of contemporary cozy fantasy: closer to a
warm digital painting or a children's-classic illustration for adults than to photography.
Visible but controlled brushwork. Fine detail on book spines, wood grain, the ladder.
Charming and dignified, NOT cartoonish, NOT anime, NOT chibi. No cluttered whimsy.

COMPOSITION:
Keep the upper third relatively simple, the darker ceiling area above the shelves, so the
title can sit there and stay readable. Keep the bottom eighth clear and dark for the
author name. The ladder and the woman sit slightly right of centre. Plenty of negative
space in the upper area.

TEXT ON THE COVER, render all of the following as part of the image, spelled exactly:

Main title, upper third, centred, large, in an elegant warm serif with generous letter
spacing, in cream white with a subtle dark outline so it separates from the ceiling:
THE SECOND-HAND SPELLBOOK

Directly beneath the title, much smaller, about one fifth of the title height, centred, in
spaced small capitals, same cream at slightly lower opacity:
A COZY FANTASY NOVEL

At the bottom of the cover, centred, small, larger than the subtitle but far smaller than
the title, same serif, all capitals, cream white:
MAREN ASHCROFT

Spell every letter exactly as written above, including the hyphen in SECOND-HAND. Do not
paraphrase, translate, abbreviate or re-order the text. Do not add any other words,
taglines, review quotes, series numbering, publisher marks, logos, borders or frames. No
watermark. No signature.

The title must remain clearly legible when the whole cover is reduced to thumbnail size.
```
