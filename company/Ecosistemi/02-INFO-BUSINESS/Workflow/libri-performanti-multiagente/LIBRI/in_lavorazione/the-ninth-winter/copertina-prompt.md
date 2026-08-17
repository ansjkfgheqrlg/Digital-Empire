# Prompt copertina — The Ninth Winter

**Come si usa:** copia il blocco `PROMPT` qui sotto e incollalo nel tuo modello di immagini.
Il testo della copertina (titolo, sottotitolo, autore) è **dentro il prompt**: deve
disegnarlo il modello, non lo aggiungiamo dopo.

**Quando torna il PNG:**
```
python -m engine.kdp consegna the-ninth-winter --cover <percorso.png>
```
Il codice lo porta a 1800×2700 (6×9in @300dpi) e **non riscrive il titolo sopra**. Se il
modello sbaglia le lettere o le omette, rilancia con `--scrivi-titolo` e le stampiamo noi.

**Controlla prima di consegnarmelo:**
- il titolo si legge quando rimpicciolisci l'immagine a francobollo (è così che la vedono su Amazon)
- **THE NINTH WINTER** è scritto esattamente così, senza refusi
- è verticale, non quadrato
- nessuna scritta inventata dal modello oltre a quelle richieste

---

## PROMPT

```
Book cover illustration for a contemporary Amish suspense novel. Vertical portrait
format, 2:3 aspect ratio (e.g. 1600 x 2400 px or larger). NOT square. High resolution,
crisp, print-quality, sharp focus edge to edge, no blur, no noise, no compression
artifacts.

SCENE:
A frozen flooded quarry pond at dusk in deep winter, seen from the shoreline. The ice
is grey-blue and dull, not glassy — old ice, snow-dusted, with faint darker patches
where it is thinner. A low bank of dark pine trees runs along the far side of the water,
their tops black against the sky. In the mid-distance, standing alone on the snow at the
edge of the ice with her back to the viewer, a young Amish woman: long dark winter dress
and black shawl, white prayer kapp, no coat, arms held close to her body. She is small in
the frame — the landscape dominates her. Her footprints lead from the bottom of the frame
to where she stands, a single line of them in fresh snow.

Far in the background on the right, almost lost in the dusk, a rusted wire fence with a
gap in it, and beyond the treeline the faint warm rectangle of a single lit farmhouse
window — the only warm light in the whole image.

MOOD AND LIGHT:
Last light of a January afternoon, overcast, the sun already gone. Cold blue-grey
twilight. Melancholy, restrained, quietly ominous — grief and suspicion rather than
horror. Absolute stillness. No wind. This should feel like a held breath, not a scream.

COLOUR PALETTE:
Desaturated and cold: slate blue, ash grey, bone white, deep charcoal for the pines and
the woman's dress. One single warm accent only — the amber of the distant window. No
other warm colour anywhere in the image. No teal-and-orange blockbuster grading.

STYLE:
Painterly literary-fiction cover art in the tradition of upmarket suspense — closer to
oil painting or high-end digital matte painting than to photography. Visible but
controlled brushwork in the sky and snow. Fine detail on the ice texture and the
treeline. Naturalistic, dignified, respectful. NOT gothic horror, NOT romance-novel
glamour, NOT folk-art or quaint "Amish country" prettiness. The woman is a person, not a
costume: no bonnet clichés, no rosy cheeks, no smiling.

COMPOSITION:
Keep the upper third of the image visually simple and uncluttered — open sky with soft
tonal gradient — so the title can sit there and stay readable. Keep the bottom eighth
relatively clear and dark for the author name. The figure sits on the lower-third line,
slightly left of centre. Plenty of negative space.

TEXT ON THE COVER — render all of the following as part of the image, spelled exactly:

Main title, upper third, centred, very large, all capitals, in an elegant high-contrast
serif with tight letter-spacing, in warm off-white (bone) with a subtle dark drop shadow
so it separates from the sky:
THE NINTH WINTER

Directly beneath the title, much smaller (about one fifth of the title height), centred,
in spaced small capitals, same off-white at slightly lower opacity:
AN AMISH SUSPENSE NOVEL

At the bottom of the cover, centred, small — larger than the subtitle but far smaller
than the title — in the same serif, all capitals, off-white:
REBECCA MILLER

Spell every letter exactly as written above. Do not paraphrase, translate, abbreviate or
re-order the text. Do not add any other words, taglines, review quotes, series numbering,
publisher marks, logos, page furniture, borders or frames. No watermark. No signature.

The title must remain clearly legible when the whole cover is reduced to thumbnail size.
```

---

## Note sulle scelte, se vuoi cambiarle

- **Autore "REBECCA MILLER"** — pseudonimo neutro, coerente col genere. Se preferisci un
  altro nome dillo e riscrivo il prompt: il nome va **anche** in `progetto.json`, perché
  finisce nei metadati KDP.
- **Sottotitolo** — "An Amish Suspense Novel" è la formula che i concorrenti forti in
  prima pagina usano quasi tutti; dice il genere in tre parole a chi scorre.
- **Nessuna figura maschile in copertina** — le copertine del genere spesso mettono la
  coppia. Qui il libro è di Rebecca e il romance è tenuto pulito e secondario: una figura
  sola mantiene la promessa giusta al lettore, che è suspense con cuore, non romanzo rosa.
- **La finestra accesa** — è l'unico punto caldo dell'immagine ed è deliberato: il libro
  finisce con Rebecca che torna a una cucina illuminata. Chi lo rilegge dopo lo riconosce.
