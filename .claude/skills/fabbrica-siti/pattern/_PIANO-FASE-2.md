# PIANO — Fabbrica Siti, Fase 2: i pattern

**Metodo:** `emperator.md §6.20` — il piano si scrive, poi si critica fino a tre volte, e ogni giro
attacca **il giro precedente**, non l'originale. I giri restano scritti: il valore sta nel poter
leggere cosa è stato scartato e perché.

**Data:** 2026-09-06 · **Giri fatti:** P0 → P1 → P2 → P3 (chiuso a P3: il terzo giro ha tagliato, e
un quarto avrebbe solo ripetuto)

---

## I FATTI, prima del piano

Misurati sul disco, non ricordati:

| Fatto | Misura |
|---|---|
| `empire-premium-style/references/section-patterns.md` | **117 righe** — è una **tabella di mappatura** con 17 ID, non 17 schede |
| Dove stanno davvero i pattern Empire | dentro `reference-page-full.tsx` — **JSX + Tailwind**, cioè **solo Corsia B** |
| Misure nei pattern esistenti | **nessuna**. Solo `bg`, `max-w`, e "(vedi file)" |
| Righe con puntatore già stale | 10 su 17 dicono `(vedi file)` invece del numero di riga |
| Pattern in Corsia A (vanilla) | **zero** |

**Conseguenza sul dossier 32:** la riga *"11 nostri già scritti + 9 da estrarre"* era ottimista.
Gli 11 non sono scritti: sono **nominati**. E sono nominati in un formato che serve a una corsia sola.

---

## P0 — IL PIANO

Scrivere 20 schede di pattern in `pattern/`, una per file:
11 dalla galleria Empire esistente + 9 estratti dall'atlante visivo di armageddon.
Ogni scheda: a cosa serve, struttura HTML, misure in frazioni di `--u`, effetti con i tempi, quando
**non** usarla.
Aggiornare `section-patterns.md` perché punti alle nuove schede.

---

## P1 — LA CRITICA DI P0

**Attacco 1 — P0 si fonda su un dato falso.**
Gli 11 pattern Empire non esistono come schede. Trascriverli dal JSX in prosa produrrebbe 11
documenti che descrivono del codice — cioè **una seconda copia della verità**, che invecchierà
appena qualcuno tocca `reference-page-full.tsx`. È esattamente il guasto che ha già colpito
`section-patterns.md`: 10 puntatori su 17 sono già stale.

**Attacco 2 — P0 viola la legge appena scritta, il giorno dopo averla scritta.**
ADR-023 e `CLAUDE-SITI.md §5`: *"un pattern nuovo si scrive prima in vanilla, poi la Corsia B lo
avvolge."* I nostri 11 esistono **solo** in JSX. Un piano che li porta avanti così com'è nasce fuori
legge.

**Attacco 3 — una scheda in prosa non è verificabile.**
Il canone ha `canone_sync.py` che dice PASS o FAIL. Un pattern in prosa non ha modo di essere
sbagliato. E un artefatto che non può fallire non può nemmeno essere corretto: resta un'opinione ben
impaginata.

**Attacco 4 — 20 documenti sono il problema di ieri con un vestito nuovo.**
Abbiamo appena chiuso "quattro sistemi che nessuno sa quale aprire". Venti schede che nessuno apre
non sono un miglioramento: sono lo stesso guasto spostato di un livello.

### P1 — il piano corretto
- Un pattern **non è un documento: è codice che gira.** Ogni pattern porta un file HTML vanilla,
  autoconsistente, che importa `canone.css` e si apre nel browser.
- La scheda resta, ma **corta**, e accanto al codice: serve a dire *quando* e *quando no*, non *come*
  (il come è nel file, e il file non può mentire).
- **Non venti.** Si scelgono i pattern che compongono davvero una pagina, in ordine di necessità.
- Una **galleria** che li mostra tutti insieme: è la verifica visiva che il canone regge quando i
  pezzi si toccano.

---

## P2 — LA CRITICA DI P1

**Attacco 1 — la galleria di P1 invecchierà come `section-patterns.md`.**
Se è un file HTML scritto a mano che elenca i pattern, alla terza aggiunta qualcuno si dimentica di
aggiornarla, e torniamo ai puntatori stale. **Deve essere generata dalle cartelle**, mai
mantenuta a mano. Un indice scritto a mano è un debito con una data di scadenza.

**Attacco 2 — "i pattern che servono davvero" è vago quanto le schede che sto criticando.**
P1 non dice come si sceglie. Va misurato: si prendono le sezioni realmente presenti in
`armageddon.bsns.it` (che è anche il bersaglio del collaudo di Fase 5) e si tiene ciò che compone
**una pagina di lancio dall'inizio alla fine**. Non "i più belli": i necessari a chiudere un lavoro
vero.

**Attacco 3 — P1 dimentica la Corsia B.**
Se Fase 2 produce solo vanilla, la Corsia B resta senza pattern e `empire-premium-style` continua a
essere l'autorità di fatto. La legge dice che B **avvolge** A: quella regola va scritta da qualche
parte, o non esiste.

**Attacco 4 — nessuno dice se un pattern rispetta il canone.**
`canone_sync.py` controlla il canone con sé stesso. Nessuno controlla che un pattern usi solo i
valori del canone. Serve almeno un controllo, anche minimo.

### P2 — il piano corretto
- Ogni pattern = **una cartella** `pattern/<id>/` con `pattern.html` (vanilla, gira) + `scheda.md`
  (corta: quando sì, quando no, cosa cade se sbagli).
- `scripts/galleria.py` **genera** `pattern/GALLERIA.html` leggendo le cartelle. Mai a mano.
- La scelta dei pattern è **derivata** dalla struttura reale di armageddon + ciò che una pagina di
  lancio Empire deve avere in più (prova sociale, garanzia).
- Un file solo `CORSIA-B.md` con la regola di avvolgimento, non uno per pattern.
- `galleria.py` fa anche da controllo: se un pattern usa un colore fuori canone, lo segnala.

---

## P3 — LA CRITICA DI P2

**Attacco unico, e cade sull'ambizione — come previsto.**

P2 vale, ma è diventato grosso: 20 cartelle × 2 file = 40 file, più generatore, più galleria, più
`CORSIA-B.md`. **È un sistema da mantenere costruito prima di aver fatto un solo sito con esso.**

E c'è una regola nostra che P2 sta ignorando: `CLAUDE-SITI.md §10` — *una soluzione che ha funzionato
in due cantieri diventa un pattern.* Se il criterio per **promuovere** un pattern è averlo usato due
volte, allora scriverne venti prima di aver aperto un cantiere è esattamente ciò che quella regola
vieta. **Stavo per violare il mio §10 mentre costruivo lo strumento che deve farlo rispettare.**

**Il secondo taglio:** `pattern.html` per venti pattern significa venti pagine da tenere in vita.
Otto no.

### P3 — il piano definitivo

**Fase 2 consegna OTTO pattern**, e sono gli otto che compongono **una pagina di lancio completa,
dall'alto in basso** — cioè esattamente il bersaglio del collaudo di Fase 5 (rifare `armageddon` col
nostro canone). Non i più belli: quelli senza i quali il collaudo non può nemmeno partire.

| # | id | Origine | Cosa risolve |
|---|---|---|---|
| 1 | `testata-targa` | Andrei + noi | la navigazione come parte della composizione, non incollata sopra |
| 2 | `hero-due-strati` | Andrei (titolo) + noi (chip, marquee, silver) | il titolo che passa dietro e davanti al soggetto |
| 3 | `cucitura-fotografica` | Andrei | una fotografia che attraversa due sezioni senza mostrare la linea |
| 4 | `prova-video` | Andrei | il video in pagina, un clic solo, con il richiamo sopra |
| 5 | `oggetto-che-si-posa` | Andrei | l'oggetto che arriva sparso, si compone, e solo dopo risponde al mouse |
| 6 | `contatore-scadenza` | Andrei | la scadenza accessibile, su un attributo solo, col comportamento a scaduta |
| 7 | `faq-native` | Andrei | `<details>` che funziona senza JavaScript |
| 8 | `coda-legale` | Andrei + noi | disclaimer più largo del corpo, firma, link che non usano il blu di default |

**Gli altri dodici non si scrivono adesso.** Si scrivono quando un cantiere li chiede — §10. La
galleria e il generatore nascono con otto e reggono venti senza modifiche.

**Cosa resta fuori da Fase 2, dichiarato:** i pattern Empire di contenuto (stats, timeline,
testimonial, value stack, is-for, chi-sono, case study, garanzia) restano dove sono, in
`reference-page-full.tsx`, e ci restano finché un cantiere non li porta in Corsia A. Non li
trascrivo in prosa: sarebbe una seconda copia della verità, ed è l'attacco 1 di P1.

---

## Cosa consegna Fase 2

```
pattern/
├── _PIANO-FASE-2.md          ← questo file, coi quattro giri
├── CORSIA-B.md               ← come la Corsia B avvolge un pattern vanilla
├── GALLERIA.html             ← GENERATA, mai scritta a mano
├── testata-targa/            ├── pattern.html + scheda.md
├── hero-due-strati/          │
├── cucitura-fotografica/     │
├── prova-video/              │
├── oggetto-che-si-posa/      │
├── contatore-scadenza/       │
├── faq-native/               │
└── coda-legale/              ┘
scripts/galleria.py           ← genera la galleria e controlla i colori fuori canone
```

**Criterio di chiusura di Fase 2:** `galleria.py` gira, produce `GALLERIA.html`, e non segnala
colori fuori canone. Non "le schede sono scritte": **la macchina dice PASS.**
