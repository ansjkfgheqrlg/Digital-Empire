---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #apsales #atlante-visivo #design-system #reference
Created: 2026-09-07
Last updated: 2026-09-07
---

# ATLANTE VISIVO — apsales.eu

**Ogni schermata della pagina, con sotto come è fatta.** Colori e misure letti da `scheda.json`
(campionati dal DOM), effetti letti da `estratto-css.md` e dai file sorgente in `src/`. Le 14
schermate sono state aperte una per una con lo strumento di visione; nessuna descrizione qui sotto
viene da uno screenshot non guardato.

Questo documento è materiale di lavoro per la Fabbrica Siti: si apre quando si costruisce, non quando
si decide la strategia (per quello vedi [08-apsales.md](08-apsales.md)) né quando serve lo stack
tecnico (vedi [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md)).

> **Le immagini** vivono in `../capture/13-apsales-v2/sezioni/`. **14 sezioni misurate, 13 firme
> strutturali distinte** — solo la Tavola 9 ripete esattamente la firma della Tavola 5 (stesso schema
> di layout: un solo livello di annidamento, nessun media, nessuna CTA); per questo non ha una tavola
> propria, è documentata come variante dentro la Tavola 5.
>
> **Palette di sfondo usata in queste tavole** (nomi interni dal CSS, HEX calcolato nel report
> gemello): `bg-void` = `#0a0a0b` · `bg-pitch` = `#111111` · `bg-paper` = `#f9f9f9` · `bg-black` =
> `#000000` (nero assoluto, un solo uso, Tavola 2) · `transparent` (eredita il fondo sotto, Tavola 14).

---

## TAVOLA 1 — La testata e l'hero
![sezione 01](../capture/13-apsales-v2/sezioni/01-il-traffico-si-compra-i-clienti-si.png)

### Cosa si vede
H1 su tre righe in bianco 80px, l'ultima parola (*convertono*) in corsivo nero 900. Sotto, un
paragrafo e due CTA affiancate. A destra, un occhio in stile ASCII/inchiostro, bianco su nero,
quadrato. Sotto l'occhio, tre righe KPI (`CVR`, `CPL`, `Spesa in ads`) separate da filetti. In fondo,
al 50% di opacità, la riga di qualificazione del cliente.

### Misure — da `scheda.json`, sezione i=1
| Campo | Valore |
|---|---|
| y / altezza | 65px / 902px |
| Sfondo | `oklch(0.1448 0.002 285)` = `#0a0a0b` (bg-void) |
| Heading | "Il traffico si compra. I clienti si convertono." |
| Blocchi di testo | 10 |
| Parole | 73 |
| Densità | 8 |
| Media | 1 — `img /ascii/occhio.webp`, 358×358, a y=223 x=897 |
| CTA | 2 — "Voglio aumentare le conversioni →" (blu, 340×58) · "Vedi i servizi" (fantasma, 163×60) |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|M\|C\|5` — gruppo 1, **rappresentante** |

### Effetti attivi
Il componente `Ascii` sull'occhio: `mix-blend-screen` + `contrast(1.3) brightness(1.45)` (misurato in
`01-Ascii-BML5uz1H.js`) — il nero della webp si annulla nel fondo, il bianco si brucia più nitido.

### Cosa cade se sbagli
È la prima schermata: la riga di qualificazione ("Solo per B2B e B2B SaaS che investono da €5.000 a
€100.000 al mese in ads") sta qui, al 50% di opacità, subito sotto la CTA. Se si sposta più in basso o
si toglie, si perde il filtro d'ingresso che tiene fuori le chiamate sbagliate (mossa già registrata
in [08-apsales.md](08-apsales.md) §6.2).

---

## TAVOLA 2 — I cinque guerrieri
![sezione 02](../capture/13-apsales-v2/sezioni/02-section.png)

### Cosa si vede
Cinque spartani in armatura, su fondo nero assoluto: `design` · `statistica` · **`APsales`** (il
guerriero centrale, più grande, in armatura completa) · `vendita` · `persuasione`, ognuno con
un'etichetta collegata da una linea tratteggiata. Sullo sfondo, un campo fitto di caratteri `x`/`o`/`×`
in bassissima opacità. In alto a destra, un piccolo globo 3D.

### Misure — sezione i=2
| Campo | Valore |
|---|---|
| y / altezza | 967px / 720px |
| Sfondo | `#000000` — **l'unica sezione della pagina con nero assoluto**, non `bg-void` |
| Heading | nessuno |
| Blocchi di testo | **285** — il valore più alto di tutta la pagina |
| Parole | 276 |
| Densità | 38 — la più alta della pagina |
| Media | 8 (5 guerrieri + globo + 2 SVG di collegamento) |
| CTA | 0 |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-black\|3\|M\|-\|4` — gruppo 2, rappresentante |

I 285 blocchi di testo non sono copy: sono i singoli `<span>` del campo di rumore ASCII (`x`, `o`,
`×`), confermato riga per riga in `copy-integrale.md` (decine di span da un solo carattere, tutti
`oklch(0.9821 0 0)` a 12,96px).

### Effetti attivi
Stesso componente `Ascii` (blend screen + boost) sui 5 guerrieri e sul globo. `bg-black` puro invece
di `bg-void` — coerente col fatto che qui non c'è testo lungo da leggere (solo etichette brevi), quindi
non si applica la nota del nostro canone ("il nero puro non è un fondo per testo lungo").

### Cosa cade se sbagli
È l'unica sezione che il rapporto 08 segnala come debole: *"non regge l'esame che il sito stesso
impone al cliente"* (creatività con un perché) — i guerrieri sono atmosfera, non informazione. Se si
riproduce questa sezione nella Fabbrica, si eredita anche il difetto: va usata come riferimento
tecnico (il trucco `Ascii`), non come modello di contenuto.

---

## TAVOLA 3 — La fila dei loghi cliente
![sezione 03](../capture/13-apsales-v2/sezioni/03-section.png)

### Cosa si vede
Un marquee orizzontale di 10 loghi cliente (Altlife Agency, BM Ecom, Pearl West Brands, Pets are
Kids, Lecca Milano, M.P. Edile, CA, Vidiren, LSP, AGL Aste Immobiliari), preceduto dalla scritta "Si
fidano di noi aziende in Italia e in Europa." e da un piccolo simbolo a freccia doppia.

### Misure — sezione i=3
| Campo | Valore |
|---|---|
| y / altezza | 1687px / 309px |
| Sfondo | `#0a0a0b` (bg-void), bordo superiore e inferiore (`border-y`) |
| Heading | nessuno |
| Blocchi di testo | 25 |
| Parole | 10 |
| Densità | 3 — la più bassa della pagina insieme alla Tavola 12 |
| Media | **25** — i 10 loghi duplicati per il loop infinito più l'icona freccia |
| CTA | 0 |
| Firma / gruppo | `section\|relative.overflow-hidden.border-y\|4\|M\|-\|2` — gruppo 3, rappresentante |

### Effetti attivi
Animazione dichiarata in `scheda.json`: `logo-marquee 40s linear` (unica animazione nominata di tutta
la pagina). Ai due bordi della fascia, le maschere `mask-image` a doppia soglia simmetrica lette in
`estratto-css.md` (es. `linear-gradient(90deg,#0000,#000 10% 90%,#0000)`) dissolvono i loghi in
ingresso/uscita invece di tagliarli di netto.

### Cosa cade se sbagli
Senza il fade ai bordi, il loop del marquee mostra i loghi apparire/sparire di scatto ai margini della
fascia — un dettaglio piccolo ma che si nota subito su un ciclo di 40 secondi ripetuto in continuo.

---

## TAVOLA 4 — Il paragrafo-manifesto
![sezione 04](../capture/13-apsales-v2/sezioni/04-section.png)

### Cosa si vede
Un solo paragrafo centrato, 45px, su fondo scuro pieno: *"Siamo AP Sales, un'agenzia di CRO
specializzata nel **capire cosa si può fare per ottenere più risultati con il proprio marketing**
usando la scienza e l'arte della persuasione etica."* — la parte in grassetto è più pesante (700),
il resto è leggero (400).

### Misure — sezione i=4
| Campo | Valore |
|---|---|
| y / altezza | 1996px / 563px |
| Sfondo | `oklch(0.1776 0 0)` = `#111111` (bg-pitch) |
| Heading | nessuno (è un `p`, non un `h*`) |
| Blocchi di testo | **1** — la sezione più semplice della pagina |
| Parole | 29 |
| Densità | 5 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|bg-pitch\|1\|-\|-\|3` — gruppo 4, rappresentante |

### Effetti attivi
Nessuno: solo tipografia (45px, due pesi).

### Cosa cade se sbagli
**È l'unico blocco centrato di tutta la pagina** — il resto è allineato a sinistra su `x=184`
(12,8% di 1440px). Se si centra anche il resto, o si allinea questo a sinistra, si perde l'unico
punto di respiro visivo di una pagina altrimenti tutta a bandiera sinistra.

---

## TAVOLA 5 — Il problema / La soluzione (e la sua variante, Tavola 9)
![sezione 05](../capture/13-apsales-v2/sezioni/05-il-problema.png)

### Cosa si vede
Due colonne speculari su un unico riquadro bordato: "Il problema" (bianco) a sinistra, "La
**soluzione**" (soluzione in corsivo nero) a destra, tre righe ciascuna separate da filetti orizzontali,
bullet quadrati blu sulla colonna soluzione. Sotto il riquadro, tre celle KPI (`=` grigio, `↓` blu,
`↑` blu) con frecce.

### Misure — sezione i=5
| Campo | Valore |
|---|---|
| y / altezza | 2559px / 1004px |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | "Il problema" + "La soluzione" |
| Blocchi di testo | 19 |
| Parole | 116 |
| Densità | 12 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|-\|-\|5` — **gruppo 5, rappresentante** |

### La variante — Tavola 9 (stessa firma, non rappresentante)
![sezione 09](../capture/13-apsales-v2/sezioni/09-agenzia-generalista-freelancer-o-a.png)

Sezione i=9, y=6931 h=1034, heading "Agenzia generalista, freelancer o assumere? Nessuno dei tre." —
**stessa firma esatta** (`section|scroll-mt-16.bg-void|1|-|-|5`, gruppo 5) della Tavola 5: stesso
schema di composizione (un livello di annidamento, zero media, zero CTA dirette), contenuto
completamente diverso (qui c'è la tabella comparativa 4 colonne × 6 righe: AP Sales / Agenzia
generalista / Freelancer / Team interno, coi simboli `✓`/`✕`/`~`). 48 blocchi di testo, 108 parole,
densità 10.

### Effetti attivi (entrambe)
Nessun effetto grafico: solo filetti divisori (`border`) e colore. Nella Tavola 9, il velo blu al 4%
sulla colonna "AP Sales" (`oklab(0.556 ... / 0.04)`, misurato in `palette_sfondi`) è invisibile come
colore ma leggibile come "colonna un millimetro più avanti delle altre".

### Cosa cade se sbagli
**Tavola 5**: le tre frasi-problema citano il cliente tra virgolette (*"spendi di più"*, *"a me piace
il blu"*) — se si genericizza il copy si perde la specificità che le rende credibili.
**Tavola 9**: la tabella concede un punto all'avversario (`Costo fisso mensile → Freelancer: ✓ No`) —
se si toglie quella concessione, la tabella torna propaganda invece di confronto verificabile (già
segnalato in [08-apsales.md](08-apsales.md) §6.7).

---

## TAVOLA 6 — "Facciamo solo due cose. Per scelta."
![sezione 06](../capture/13-apsales-v2/sezioni/06-facciamo-solo-due-cose-per-scelta.png)

### Cosa si vede
Due card affiancate su fondo scuro pieno: "Landing page" (illustrazione wireframe di un laptop in
puntini) e "Consulenza con Andrei Pascu" (un mirino circolare fatto di puntini, con un punto blu al
centro). Ognuna con 3 bullet e una CTA fantasma in fondo.

### Misure — sezione i=6
| Campo | Valore |
|---|---|
| y / altezza | 3563px / 1482px |
| Sfondo | `#111111` (bg-pitch) |
| id | `servizi` |
| Heading | "Facciamo solo due cose. Per scelta." + "Landing page" + "Consulenza con Andrei Pascu" |
| Blocchi di testo | 20 |
| Parole | 126 |
| Densità | 9 |
| Media | 2 — `laptop.webp` (440×440) e `mirino-dot.webp` (440×440) |
| CTA | 2 — "Come funziona" → `/landing-page` · "Fai una consulenza" → `/consulenza` |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|M\|C\|7` — gruppo 6, rappresentante |

### Effetti attivi
Componente `Ascii` su entrambe le illustrazioni (stesso blend screen + boost). Sul mirino a puntini
del secondo box è verosimile una delle maschere radiali (`radial-gradient(closest-side,...)`,
`radial-gradient(circle,...)`) che ne dissolve il bordo esterno — coerente con quanto visibile nello
screenshot (i puntini si diradano verso i margini).

### Cosa cade se sbagli
Il titolo dice "due cose. Per scelta." — se si aggiunge una terza card si perde la prova di
posizionamento per restrizione di scopo (competenza dimostrata col limite, non con l'elenco).

---

## TAVOLA 7 — "Metodo statistico. Non opinioni."
![sezione 07](../capture/13-apsales-v2/sezioni/07-metodo-statistico-non-opinioni.png)

### Cosa si vede
Quattro colonne numerate `01`-`04` (Tracciamo, Guardiamo, Costruiamo, Misuriamo), ognuna con una
frase e delle "chip" in font monospaziato (GA4, Meta Pixel, Clarity...). Sotto, un riquadro a due
colonne: a sinistra un wireframe di pagina con tre blocchi che si illuminano di blu (heatmap), a
destra "Quello che vediamo" con altre chip mono.

### Misure — sezione i=7
| Campo | Valore |
|---|---|
| y / altezza | 5045px / 1194px |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `metodo` |
| Heading | "Metodo statistico. Non opinioni." + Tracciamo/Guardiamo/Costruiamo/Misuriamo + "Quello che vediamo" |
| Blocchi di testo | 42 |
| Parole | 147 |
| Densità | 12 |
| Media | 1 — `tracking-heatmap.webp`, 614×343 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|M\|-\|6` — gruppo 7, rappresentante |

### Effetti attivi
Nessun effetto grafico oltre al colore (numeri e alcune chip in `--brand-blue` `#0062ff`). L'effetto
vero è tipografico: le chip (`GA4`, `Clarity`, `Heatmap`, `CVR`...) sono in `DM Mono` — il font più
usato di tutta la pagina (240 occorrenze), qui concentrato.

### Cosa cade se sbagli
Se si sostituisce il monospaziato con un font normale sulle chip, si perde il segnale "qui si misura"
che il font trasmette senza bisogno di scriverlo — la mossa tipografica che il rapporto 08 chiama "la
più imitabile della pagina".

---

## TAVOLA 8 — "Non facciamo solo pagine. Orchestriamo la conversione."
![sezione 08](../capture/13-apsales-v2/sezioni/08-non-facciamo-solo-pagine-orchestri.png)

### Cosa si vede
Titolo su due righe, un sottotitolo in grassetto, poi tre colonne separate da filetti verticali:
Offerta, Coerenza ads ↔ pagina, Fiducia — un H3 e un paragrafo ciascuna, nessuna icona.

### Misure — sezione i=8
| Campo | Valore |
|---|---|
| y / altezza | 6239px / 692px |
| Sfondo | `#111111` (bg-pitch) |
| Heading | "Non facciamo solo pagine. Orchestriamo la conversione." + Offerta/Coerenza/Fiducia |
| Blocchi di testo | 8 — fra i più bassi della pagina |
| Parole | 64 |
| Densità | 9 |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|-\|-\|3` — gruppo 8, rappresentante |

### Effetti attivi
Nessuno: solo filetti divisori verticali fra le tre colonne.

### Cosa cade se sbagli
È una sezione volutamente minimale (8 blocchi contro i 42 della Tavola 7 appena sopra) — se si
arricchisce con icone o media, si perde il contrasto di ritmo con le sezioni dense che la circondano.

---

## TAVOLA 9 — vedi Tavola 5 (stessa firma strutturale)

La tabella comparativa "Agenzia generalista, freelancer o assumere? Nessuno dei tre." è documentata
sopra, dentro la Tavola 5, perché condivide con essa la stessa firma di layout misurata in
`scheda.json` (`rappresentante: false`).

---

## TAVOLA 10 — "Piccola agenzia. Standard alti."
![sezione 10](../capture/13-apsales-v2/sezioni/10-piccola-agenzia-standard-alti.png)

### Cosa si vede
**L'unica sezione su fondo chiaro di tutta la pagina.** A sinistra: titolo, due paragrafi, tre numeri
in colonna (250.000 follower, 100+ clienti, 1.500+ professionisti formati) e una CTA fantasma "Conosci
il team ↗". A destra: la foto del founder Andrei Pascu (bianco e nero, maglietta nera, catena d'oro),
e due strisce verticali strette con le etichette "Impatto" e "Team" ruotate di 90°.

### Misure — sezione i=10
| Campo | Valore |
|---|---|
| y / altezza | 7965px / 978px |
| Sfondo | `oklch(0.9821 0 0)` = `#f9f9f9` (bg-paper) — unica sezione chiara |
| id | `chi-siamo` |
| Heading | "Piccola agenzia. Standard alti." |
| Blocchi di testo | 26 |
| Parole | 83 |
| Densità | 8 |
| Media | 3 — `founder.webp` (328×640), `impatto.webp` e `team.webp` (64×640 ciascuna, le due strisce collassate) |
| CTA | 4 — "Conosci il team ↗" più i tre "bottoni" cliccabili Founder/Impatto/Team che espandono le strisce |
| Firma / gruppo | `section\|scroll-mt-16.theme-paper.bg-paper\|1\|M\|C\|5` — gruppo 10, rappresentante |

### Effetti attivi
Nessun filtro o maschera: qui il trucco è di layout, non grafico — le due card "Impatto"/"Team" sono
larghe **64px** con il testo in `writing-mode` verticale, contro i **328px** della card Founder
aperta. Tre card, una aperta e due "di taglio".

### Cosa cade se sbagli
Le card collassate sono il "componente da rubare" del rapporto 08: se si sostituiscono con un
carosello o degli accordion, si perde la densità informativa orizzontale (tre informazioni visibili
insieme, senza JavaScript e senza swipe).

---

## TAVOLA 11 — "Deleghiamo. Ma mai a caso."
![sezione 11](../capture/13-apsales-v2/sezioni/11-deleghiamo-ma-mai-a-caso.png)

### Cosa si vede
Un riquadro scuro su fondo scuro (leggermente più chiaro del fondo pagina), con un templare in pixel
art bianco e nero a sinistra e testo a destra: titolo in due pesi ("Deleghiamo." bianco pieno, "Ma mai
a caso." grigio) e un paragrafo che ammette l'uso di collaboratori esterni.

### Misure — sezione i=11
| Campo | Valore |
|---|---|
| y / altezza | 8943px / 652px |
| Sfondo | `#0a0a0b` (bg-void) |
| Heading | "Deleghiamo. Ma mai a caso." |
| Blocchi di testo | 3 — fra i più bassi della pagina |
| Parole | 44 |
| Densità | 7 |
| Media | 1 — `templare-pixel.webp`, 137×153 |
| CTA | 0 |
| Firma / gruppo | `section\|scroll-mt-16.bg-void\|1\|M\|-\|3` — gruppo 11, rappresentante |

### Effetti attivi
Componente `Ascii` sul templare pixel-art (stesso blend screen).

### Cosa cade se sbagli
È l'ammissione di outsourcing fatta per prime, prima che il cliente la scopra da sé — se si taglia
questa sezione per "sembrare più grandi", si perde il disinnesco preventivo dell'obiezione numero uno
contro le agenzie piccole (unica ammissione di questo tipo in tutto l'ecosistema Andrei Pascu,
segnalato in [08-apsales.md](08-apsales.md) §6.9).

---

## TAVOLA 12 — Domande frequenti
![sezione 12](../capture/13-apsales-v2/sezioni/12-domande-frequenti.png)

### Cosa si vede
Titolo "Domande frequenti." e sette righe accordion chiuse, ognuna con una chevron a destra, separate
da filetti sottili: Cos'è la CRO? · Con chi lavorate? · Che tipo di accordo offrite? · E se le
conversioni non aumentano? · Quanto costa? · Fate anche ads, social, SEO? · Quanto tempo devo
dedicarci io?

### Misure — sezione i=12
| Campo | Valore |
|---|---|
| y / altezza | 9594px / 1077px |
| Sfondo | `#111111` (bg-pitch) |
| id | `faq` |
| Heading | "Domande frequenti." + le 7 domande |
| Blocchi di testo | 15 |
| Parole | 31 — densità di parole bassa (sono solo le domande, le risposte sono chiuse) |
| Densità | 3 — la più bassa della pagina insieme alla Tavola 3 |
| Media | 7 — le 7 icone chevron |
| CTA | 7 — i 7 trigger dell'accordion |
| Firma / gruppo | `section\|scroll-mt-16.bg-pitch\|1\|M\|C\|5` — gruppo 12, rappresentante |

### Effetti attivi
Il componente `accordion` (Radix Collapsible + shadcn), animato con `@keyframes accordion-down` /
`accordion-up` letti in `estratto-css.md` — l'altezza del pannello si anima da `0` all'altezza reale
via CSS custom property `--radix-accordion-content-height`, non con un `max-height` fisso.

### Cosa cade se sbagli
Tre delle sette domande sono scomode di proposito (*"E se le conversioni non aumentano?"*, *"Quanto
costa?"*, *"Fate anche ads, social, SEO?"*) — se si tolgono per "ripulire" la sezione, si perde la
fiducia che si genera affrontando di petto le obiezioni invece di aggirarle.

---

## TAVOLA 13 — La CTA finale
![sezione 13](../capture/13-apsales-v2/sezioni/13-vediamo-se-ha-senso-lavorare-insie.png)

### Cosa si vede
Titolo grande su due righe ("Vediamo se ha senso **lavorare insieme**.", l'ultima parte in corsivo),
un paragrafo, una CTA blu piena ("Parla con noi →") e sotto, in grigio, "Nessun impegno. Niente
countdown finti."

### Misure — sezione i=13
| Campo | Valore |
|---|---|
| y / altezza | 10671px / 712px |
| Sfondo | `#0a0a0b` (bg-void) |
| id | `contatti` |
| Heading | "Vediamo se ha senso lavorare insieme." |
| Blocchi di testo | 6 |
| Parole | 37 |
| Densità | 5 |
| Media | 0 |
| CTA | 1 — "Parla con noi →" (blu, 191×58) |
| Firma / gruppo | `section\|relative.overflow-hidden.bg-void\|2\|-\|C\|4` — gruppo 13, rappresentante |

### Effetti attivi
Nessuno oltre al colore e alla tipografia.

### Cosa cade se sbagli
La CTA è condizionale e bilaterale ("Vediamo **SE** ha senso", "**e se possiamo aiutarti**") — se si
riscrive in forma assertiva ("Lavoriamo insieme!") si alza il rischio percepito dal cliente invece di
abbassarlo, che è esattamente il lavoro che questa frase fa (segnalato in
[08-apsales.md](08-apsales.md) §6.11).

---

## TAVOLA 14 — Il footer
![sezione 14](../capture/13-apsales-v2/sezioni/14-footer.png)

### Cosa si vede
Nello screenshot: fondo pressoché nero con il wordmark "APsales" enorme in blu pieno, in alto; il
resto dell'inquadratura, in basso, appare vuoto/nero.

### Misure — sezione i=14
| Campo | Valore |
|---|---|
| y / altezza | 11383px / 1182px |
| Sfondo (misurato dal DOM) | `transparent` — eredita il fondo di quanto sta sotto |
| tag | `footer` (non `section`) |
| Heading | nessuno |
| Blocchi di testo | 19 |
| Parole | 32 |
| Densità | 3 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `footer\|relative\|2\|M\|-\|6` — gruppo 14, rappresentante |

### Effetti attivi — la discrepanza da verificare
Il componente `RevealFooter` dichiara nel codice sorgente `bg-blue text-white` su un contenitore
`position:fixed` innestato dentro un box `relative` con `clipPath:inset(0)` (misurato in
`03-RevealFooter-B34lvwld.js`, dettaglio completo in
[13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) §3). Lo screenshot automatico non mostra
il blu pieno atteso dal codice — verosimilmente perché un elemento `fixed` dentro un ritaglio a
sezione non si comporta come nel browser reale durante lo scroll. **Non decido qui quale dei due sia
il render "vero"**: lo segnalo come discrepanza misurata, da verificare a mano prima di replicare
l'effetto.

Il copy del footer completo (link `Servizi`/`Landing page`/`Consulenza`/`Chi siamo`/`Lavora con
noi`/`Assistenza`/`Instagram`/`Termini e condizioni`, indirizzo P.IVA, copyright) è presente in
`copy-integrale.md` ma a coordinate `y` più basse di quelle della sezione footer stessa (9972-10114
contro gli 11383+ della sezione) — segno che quel blocco di link viene renderizzato altrove nel DOM
(verosimilmente dentro un dialog/menu mobile) e non nel footer visibile in fondo pagina.

### Cosa cade se sbagli
Se si replica "alla lettera dallo screenshot" (solo wordmark su nero), si perde il comportamento reale
dichiarato nel codice (`bg-blue`, footer a piena altezza che scorre da sotto). Verificare nel browser
prima di scegliere quale versione costruire.

---

## Connessioni

- [08-apsales.md](08-apsales.md) — il primo passaggio: copy, palette, struttura, le 9 mosse da copiare
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — lo stack, i token OKLCH→HEX, i componenti, il delta alla Fabbrica
- [11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md) — il modello di questo stesso formato, su un altro sito dell'ecosistema
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
