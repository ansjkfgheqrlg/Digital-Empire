---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #claude-speedrun #stack #design-tokens #ccm
Created: 2026-09-07
Last updated: 2026-09-07
---

# 12 — claude-speedrun.com — LO STACK E I TOKEN

**Il secondo passaggio sullo stesso sito.** Il [rapporto 07](07-claude-speedrun.md) del 2026-09-02 ha
studiato copy, palette e struttura **dalle immagini**. Questo studia **come è costruito**, dai file
serviti: 40 file sorgente scaricati, 94 KB di CSS analizzati, 39 `@keyframes`, e i nomi dei suoi
componenti.

È lo **strato 4** di `emperator.md §6.22` — *come l'ha fatta*, non *com'è fatta*. E su questo sito
vale più di tutto il resto, perché **è il concorrente diretto di Claude Code Mastery**.

> Cattura: `capture/12-claude-speedrun-v2/` · 33.756px · **34 sezioni (32 distinte)** · 473 blocchi di
> copy · 40 CTA · 64 media · 40 file sorgente · 39 keyframes.

---

## 1. ⭐ LA PROVA NUMERICA: il suo arancione È il nostro

Nel suo CSS, fra le variabili di tema:

```css
--brand-orange: 16 97% 50%;
--brand-black:  0 0% 7.5%;
--brand-dark-grey: 240 2% 23%;
--brand-grey:   0 0% 97.6%;
--brand-white:  0 0% 97.6%;
```

`hsl(16, 97%, 50%)` convertito:

```
C = (1 - |2·0.5 − 1|) · 0.97 = 0.97
H' = 16/60 = 0.2667 ;  X = 0.97 · (1 − |0.2667 − 1|) = 0.2587 ;  m = 0.5 − 0.485 = 0.015
R = 0.985 → 251   G = 0.2737 → 70   B = 0.015 → 4
```

# → `#FB4604`

**È il nostro `--color-orange` esatto, cifra per cifra.** Non "simile", non "vicino": lo stesso.
Fino a oggi lo sapevamo per confronto a schermo; adesso è **letto dai suoi token**.

E non finisce lì: `--brand-black: 0 0% 7.5%` = **`#131313`**, praticamente il nostro
`--ink-2: #0a0a0a`. `--brand-grey: 0 0% 97.6%` = **`#f9f9f9`**, che è **identico** al nostro
`--fg: #f9f9f9`.

**Tre valori su cinque coincidono con i nostri.** Resta aperta solo la domanda delle date — Wayback,
non ragionamento. Ma la coincidenza non è più un'impressione: è una misura.

---

## 2. LO STACK — non è vanilla, è React compilato

I nomi dei file serviti hanno l'impronta digitale di **Vite**: `index-hunxel6D.js`,
`Section3-Cxomdrie.js`, hash a 8 caratteri sul nome del chunk.

| Cosa | Evidenza |
|---|---|
| **Vite** (build) | nomi `<Componente>-<hash>.js`, `assets/` |
| **React** | chunk `jsx-runtime`, componenti per file |
| **Tailwind** | 94 KB di utility generate, `--tw-*` ovunque |
| **shadcn/ui** | il set completo di variabili: `--background --foreground --card --popover --primary --secondary --muted --accent --destructive --border --input --ring --radius` **e `--sidebar-*`** |
| **Radix** | `@keyframes accordion-up/down` con `--radix-accordion-content-height` |
| **tailwindcss-animate** | `@keyframes enter` / `exit` con `--tw-enter-*` |

**È lo stesso stack che il nostro agente `site-premium-builder` dichiara obbligatorio** (Next+
Tailwind+shadcn+Radix). Lui usa Vite invece di Next perché la pagina non ha bisogno di rotte server.

> **Correzione a una cosa che avevo scritto ieri.** Nel rapporto su armageddon avevo classificato
> `claude-speedrun` fra i siti "artigianali" insieme ad armageddon. **Falso, ed è un errore di
> categoria**: armageddon è vanilla senza build; questo è un'applicazione React compilata. Due
> mestieri diversi, e la differenza è esattamente la nostra Corsia A contro Corsia B.
> Anche il rilevatore automatico l'aveva detto "artigianale": non conosceva la firma di Vite. Corretta.

---

## 3. ⭐⭐ I NOMI DEI SUOI COMPONENTI — la sua tassonomia di pagina, servita in chiaro

Vite spezza il bundle per componente e **mette il nome nel file**. Questo è il suo indice di
architettura, preso senza chiedere:

```
SectionTop1   SectionTop2   Section2 … Section21   SectionSpirale
SectionFeaturesCs2   OfferSection   LessonList   ReviewsWall
SkillsGrid   FAQ   Footer   Disclaimer   check   flock
```

**Cosa insegna questo elenco, e non lo insegna nessuno screenshot:**

1. **Ventuno sezioni numerate più due "Top".** La pagina è pensata come una **sequenza numerata**,
   non come un insieme di blocchi tematici. Il numero è l'ordine di lettura, ed è deciso prima.
2. **Solo sei sezioni hanno un nome proprio**: `OfferSection`, `LessonList`, `ReviewsWall`,
   `SkillsGrid`, `FAQ`, `Disclaimer`. Sono le sei che **fanno un lavoro**; le altre quindici sono
   argomentazione, e restano anonime.
3. **`ReviewsWall`** — non "Testimonials": un **muro**. La prova sociale è trattata come massa, non
   come selezione. (Coerente col rapporto 07: prova quantificata.)
4. **`SkillsGrid`** — la promessa è espressa come **griglia di competenze**, non come lista di
   benefici. Vende capacità acquisite, non risultati promessi.
5. **`LessonList`** — l'indice del corso è un componente a sé, con dentro la logica: 20 KB di
   JavaScript per un elenco di lezioni significa stato, filtri, forse progressione.
6. **`Disclaimer` è un componente**, non una riga di footer. Ha dignità di sezione.
7. **`SectionSpirale`** e **`flock`** — due nomi che non descrivono contenuto ma **movimento**. Sono
   effetti che occupano una sezione intera.
8. **`SectionFeaturesCs2`** — il "2" dice che questa pagina è stata **riadattata da una versione
   precedente**, e che il prodotto è alla seconda edizione.

> **Da rubare subito:** l'idea che le sezioni si numerino invece di nominarsi. Un nome tematico
> ("chi siamo", "benefici") invita a riempirlo; un numero invita a chiedersi **cosa deve succedere al
> lettore in quel punto**. È una disciplina di architettura, e costa zero.

---

## 4. GLI EFFETTI — pochi, e tutti a servizio

Nove `@keyframes` scritti da lui (gli altri 30 sono del player Vimeo):

| Movimento | Cosa fa | Nota |
|---|---|---|
| **`highlighter-reveal`** | `background-size: 0% 100%` → `100% 100%` | **l'evidenziatore che si riempie**. È il nostro `hl-block`, ma animato allo scroll |
| **`marquee-scroll`** | `translate(0)` → `translate(-50%)` | il nastro scorrevole. Identico al nostro |
| **`subtle-vibrate`** | `rotate(-2deg)` ↔ `rotate(2deg)` | vibrazione leggera per attirare su un elemento |
| `bounce`, `pulse` | standard Tailwind | — |
| `enter` / `exit` | `tailwindcss-animate` | ingressi dichiarativi |
| `accordion-up` / `down` | Radix | FAQ |

**Cinque curve in tutto**, e la sola non-Tailwind è `cubic-bezier(.22, 1, .36, 1)` — una
*ease-out-quint*, la curva che parte veloce e si posa lentamente.

**Nessun filtro, nessun blend, nessuna maschera scritti a mano.** Tutti i filtri elencati vengono dal
player Vimeo. **Il sito non usa un solo effetto grafico proprio**: usa tipografia, colore e
movimento. Nient'altro.

> **Questa è la lezione più scomoda per noi.** Il nostro canone porta grana a doppio strato, testo
> argentato con clip su gradiente, ombre a più livelli. Il suo sito da 249 € — il nostro concorrente
> diretto — **non ha niente di tutto questo e vende lo stesso**. Non significa che la nostra firma
> vada tolta: significa che **non è lei a vendere**, e che va usata come firma, non come argomento.

---

## 5. LA STRUTTURA MISURATA — 34 sezioni, 32 distinte

Il dato più eloquente: **34 sezioni, 32 firme strutturali diverse.** Solo due si ripetono.

Su 33.756 px, questo vuol dire che **quasi ogni sezione è disegnata a sé**. Nessuna griglia riusata,
nessun blocco fotocopiato. È l'opposto di una pagina fatta con un page builder, e spiega perché la
lettura non stanca: **il lettore non riconosce mai il pattern precedente, quindi non prevede la
noia**.

Da confronto, sulla stessa cattura: `apsales.eu` fa 14 sezioni con 13 firme, `armageddon` 4 con 4,
`/outemail` (Squarespace) **24 sezioni con solo 16 firme** — otto sezioni sono lo stesso blocco
ripetuto.

**Regola che se ne ricava:** più la pagina è lunga, più le sezioni devono essere **strutturalmente
diverse**. Il page builder fa il contrario, ed è per questo che le pagine lunghe fatte col builder
sembrano tutte più lunghe di quanto sono.

---

## 6. IL DELTA ALLA FABBRICA — cosa entra, subito

| # | Cosa | Dove |
|---|---|---|
| 1 | **`highlighter-reveal`**: l'evidenziatore che si riempie allo scroll invece di essere già pieno | pattern nuovo, Corsia A e B |
| 2 | **Sezioni numerate, non nominate** — disciplina di architettura | `CLAUDE-SITI.md`, passo 4 del flusso |
| 3 | **La regola delle firme**: su una pagina lunga, sezioni strutturalmente diverse | gate futuro: firme ripetute / sezioni totali sotto una soglia |
| 4 | **`--brand-*` prima dei token semantici**: i suoi token di marca stanno sopra quelli di shadcn, e i semantici li referenziano | il nostro canone lo fa già a metà — va reso esplicito |
| 5 | **`Disclaimer` come componente** e non riga di footer | pattern `coda-legale`, già scritto: confermato da una seconda fonte → **§10, diventa regola** |
| 6 | **La lezione del "niente effetti"**: la firma visiva non è l'argomento di vendita | `CLAUDE-SITI.md` — nota al §1 |

---

## 7. COSA RESTA DA FARE SU QUESTO SITO

- [ ] atlante visivo delle **32 sezioni distinte** (schermate già su disco in `capture/12-.../sezioni/`)
- [ ] teardown del copy sui **473 blocchi** (`copy-integrale.md`, ora col fix B-057)
- [ ] leggere `LessonList` (20 KB) e `OfferSection`: la logica dell'offerta è lì dentro
- [ ] Wayback sulle date, per chiudere la questione `#fb4604`

---

## Connessioni
- [07-claude-speedrun.md](07-claude-speedrun.md) — il primo passaggio: copy, palette, struttura
- [11-armageddon.md](11-armageddon.md) — l'altro sito, l'altro mestiere (vanilla, zero build)
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — il terzo stack dell'ecosistema
- `../ECOSISTEMA.md` · `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
- `.claude/skills/fabbrica-siti/canone/canone.css` — dove va a finire il delta
