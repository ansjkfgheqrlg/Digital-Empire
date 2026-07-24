# 00 — SCELTA DEL VIDEO

> Run: `run-2026-07-23-001` · Stream: S5 (YouTube) · Scope: **1 video end-to-end**, niente scaling.
> Nicchia: AI/Claude in italiano (DEC-EST-004, default per veto scaduto).

---

## Idea scelta

**#1 — "Come installare e configurare Claude Code in 5 minuti (Tutorial Completo)"**
Fonte idea: `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/03_20_IDEE_VIDEO.md`,
Categoria A (Setup & Terminal Basics), idea #1.

Angolo: rimuovere l'ostacolo iniziale dell'installazione da terminale.

---

## Criterio di scelta: domanda misurata, non gusto

Non è la mia idea preferita per estetica: è quella con più segnali di domanda reale già
raccolti nei dossier di scouting, per tre motivi indipendenti.

### 1. Il cluster di canali più vicino segnala esplicitamente questa opportunità come "Altissima"
Da `01_MAPPA_CANALI.md`, cluster **"Tech-Hacker Screencast"** (Martes AI ~20.000 iscritti/2.000-5.000
view a video, Piero Savastano ~19.500/2.000-5.000, SOS Automazioni ~19.300/1.500-4.000, Armand
Thanasi ~27.600/3.000-10.000, Alberto Olla ~50.200/5.000-15.000): stesso pubblico (sviluppatori e
appassionati tecnici italiani), stesso formato (screencast tecnico), e il documento dice
testualmente: *"Opportunità per il Manuale: Altissima. Questo formato attira programmatori e
appassionati tecnici che vogliono installare e usare Claude Code ma si scontrano con le
configurazioni dei server MCP o delle API."* — cioè esattamente il problema che un video di
installazione risolve. Non è un'inferenza mia: è scritto nel dossier di scouting.

### 2. È lo stadio di consapevolezza con il bacino più ampio per un canale a zero storico
`03_20_IDEE_VIDEO.md` classifica l'idea #1 come **Problem/Solution Aware** (Categoria A), il
livello più basso di prerequisiti: non serve che lo spettatore sappia già cosa sono MCP, n8n o gli
agenti AI — gli basta voler provare Claude Code. Le idee delle categorie C e D (es. #16 "server
MCP", #20 "ROI risparmiato") presuppongono un pubblico già Product/Decision Aware, che un canale al
primo video non ha ancora. Partire da lì sarebbe una scommessa di gusto, non di dati.

### 3. Esiste già un asset interno validato per questa idea specifica
`WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/script-video-claude/SCRIPT_01_INSTALLAZIONE.md` è uno script
completo, proprietario di Digital Empire (non una traduzione di un video di terzi — nessuna fonte
esterna citata, framework APSOC applicato in astratto), già scritto per **esattamente questa idea**
prima di questo lotto. Il fatto che il lavoro precedente del team avesse già isolato questa idea
come prioritaria (script #1 su 20) è un secondo segnale indipendente di validazione, non generato
da questo lotto. Ho **adattato** quello script (non copiato 1:1): ho accorciato l'hook, spostato la
struttura in scene con timing dichiarato, e soprattutto ho inserito una CTA verbale alla risorsa
gratuita (Parte 1 del Manuale) nei primi 70 secondi — elemento richiesto da questo lotto e assente
nella versione originale, che rimandava tutta l'offerta al minuto 10:30.

### Alternative scartate (per mostrare che è una decisione, non un default)
- **Idea #16 "Server MCP"** — richiede pubblico già Product Aware; scartata per un canale al primo
  video (nessuno storico da cui attingere fiducia sufficiente per un argomento avanzato).
- **Idea #20 "Ho risparmiato €3.400"** — richiede un case study reale con cifre verificabili che
  questo lotto non ha (nessuna fattura/preventivo reale a disposizione): usarla ora avrebbe
  significato inventare un numero, cosa esplicitamente vietata dal metodo (§5 invariante
  "decisione su dati, mai su intuizione" della skill `youtube-automation-factory`).
- **Idea #6 "Scraper di contatti"** — buon video, ma presuppone che lo spettatore abbia già
  Claude Code installato e funzionante: è un video "secondo", non un video "zero".

---

## Gate anti-copia (stage 5 della pipeline S5)

Nessun video di terzi è stato guardato, trascritto o tradotto per produrre questo script. La base
è: (a) i pattern aggregati di 20 canali italiani della nicchia (mappa + pattern vincenti, materiale
di scouting proprio), (b) un asset interno Digital Empire pre-esistente sulla stessa idea. Il
contenuto (hook, problema, step di installazione, CTA) è stato riscritto da zero in questo run per
adattarlo al formato a 10 scene richiesto e per rispettare il vincolo "CTA gratuita nei primi 10%".

---

## Fonti consultate in questo run
- `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/01_MAPPA_CANALI.md`
- `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/02_PATTERN_VINCENTI.md`
- `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/03_20_IDEE_VIDEO.md`
- `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/04_TEMPLATE_DESCRIZIONE_SEO.md`
- `.claude/skills/youtube-automation-factory/SKILL.md` + `.claude/skills/youtube-automation-factory/references/teoria-script.md` + `.claude/skills/youtube-automation-factory/workflows/WF3-production.md` (metodo hook/intro/CTA, riusato non riscritto)
- `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/script-video-claude/SCRIPT_01_INSTALLAZIONE.md` (asset interno adattato)
- `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-S5-YOUTUBE.md` (regole del ladder di render e revenue path)
