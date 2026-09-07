# Report — A6/L01 «SEO YouTube manuale operativo» (17:54)

- **Durata:** 17:54 · ~2.477 parole · **profondità ORO**
- **Letta:** parlato integrale + 21/74 frame unici (campione motivato, vedi `frame-scelti.md`)
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)

---

## 1. Cosa insegna

Metodo SEO manuale: ricerca diretta su YouTube per capire il posizionamento reale, uso
dell'estensione vidIQ per leggere punteggio e tag di video competitor, riscrittura (non copia) di
titoli ispirati a video che già funzionano, tre hashtag mirati, generazione di titolo/descrizione
via ChatGPT, assegnazione ad almeno due playlist (raccomandazione dichiarata di YouTube stesso),
capitoli automatici, tag che includono il nome del canale.

## 2. Cosa facciamo oggi

`apex7_orchestrator.py` genera title/description/tags/keyword automaticamente e li passa a
`seo_score.py` per un punteggio deterministico (5 elementi pesati, soglia di passaggio 70/100).
Verificato leggendo il codice, non assunto dal nome dei file:

| Elemento del punteggio (seo_score.py) | Popolato da | Reale? |
|---|---|---|
| title (25 pt) | `apex7_orchestrator.py:1510`, keyword+idea_title | ✅ reale |
| description (25 pt) | riga 1503-1506, hook+intro+cta+CTA iscrizione | ✅ reale |
| tags (20 pt) | riga 1495, canale+idea+keyword | ✅ reale |
| thumbnail (15 pt) | riga 1514, `not skip_thumbnail` | ✅ reale, condizionale |
| **subtitles (15 pt)** | riga 1515, **`True` fisso** | ❌ **falso — mai verificato** |

## 3. Delta

**Il delta più importante di questo giro di studio non è nel metodo SEO del corso (che
riconosciamo quasi per intero: keyword research, riscrittura da competitor, tag ricchi): è un
difetto reale nel nostro gate.** `seo_score.py` pesa i "sottotitoli" 15/100 punti, e il proprio
commento sorgente li definisce come "indicizzati da YouTube" — cioè la traccia CC nativa, non i
sottotitoli karaoke bruciati nel video da Fliki (già trovati assenti come automazione in
`A6-L00-01`). `apex7_orchestrator.py:1515` scrive `"subtitles": True` **senza alcuna verifica**,
a fianco di un campo analogo (`thumbnail`) che invece **è** condizionale sul reale. **Ogni video
prodotto riceve 15 punti su 100 per un elemento che non esiste mai.** Non è teorico: sposta
`pass_soglia_70` — un video borderline a 55-69 "onesti" oggi passa lo stesso, gonfiato dai 15
punti falsi. Un secondo hardcoded identico esiste in `agents.py:222` ma è **dichiaratamente un
mock** ("dati finti, non usare in produzione") — non lo stesso difetto, un simulatore deve
inventare dati per costruzione.

Tre gap minori, coerenti con `A6-L00-02` (playlist mai assegnata) ma con un dettaglio nuovo: il
docente cita **"almeno due playlist"** come raccomandazione esplicita di YouTube — la regola
`A6-L00-02` va aggiornata con questo numero, non duplicata.

## 4. Conflitti

Nessuno reale. Il metodo del corso (riscrivere, non copiare, un titolo che già funziona) è
coerente con quello che l'orchestratore fa (genera da zero con keyword, non copia un competitor)
— sono due strade diverse allo stesso principio, non in contraddizione.

## 5. Regole estratte

Quattro: una nuova rischio **alto** (il difetto reale), due che rafforzano regole già registrate
(citate, non riscritte), una procedura.

| id | regola in una riga | tocca |
|---|---|---|
| `A6-L01-01` | `seo_score.py` valuta 15/100 punti di "sottotitoli" leggendo un campo che `apex7_orchestrator.py` scrive sempre `True` senza verifica: il punteggio SEO reale di ogni video è gonfiato di 15 punti fissi | `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py` (binario B) |
| `A6-L01-02` | **Aggiorna `A6-L00-02`**: la raccomandazione di YouTube citata dal corso è **almeno due playlist per video**, non "una playlist" generica | `04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md` |
| `A6-L01-03` | I tag dovrebbero includere il nome del canale, così chi cerca il canale per nome trova tutti i video: **verificato assente** — `tag_candidates` (riga 1494-1495) somma `high_performing_tags` + `tag_tema` + `idea_tokens` + `keyword`, mai il nome canale | `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py` (binario B, candidato gate A6) |
| `A6-L01-04` | vidIQ (mistrascritto "BDQ") è lo strumento reale usato dal corso per leggere tag/punteggio dei competitor: non è nel nostro "catalogo strumenti" (`scelta-strumenti.md`, A4-L00-01) | `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` |

## 6. Applicabilità

**Alta sulla scoperta del bug di scoring** — tocca direttamente il gate che decide se un video
reale si pubblica o no. Media sulla playlist (rinforza un gap già noto con un numero preciso).
Bassa-media sul resto: il metodo di keyword research e riscrittura titoli è già, nella sostanza,
quello che l'orchestratore automatizza — non un delta, una conferma che la strada presa era
giusta.
