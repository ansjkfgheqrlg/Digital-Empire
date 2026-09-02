# Lezione 17 — Introduzione al vibe coding

**Corso:** Claude Speedrun 2 (Andrei Pascu)
**Sezione:** AI - per coding e simili (1/7)
**Tipo:** PRATICA (reclassificato da TEORIA — 14 workflow dimostrati, demo live VS Code)
**Data analisi:** 2026-09-01 (ripresa dopo crash sessione)

---

## Panoramica ufficiale

In questa lezione impari cos'e' il vibe coding e come creare un sito web da zero usando Claude, senza saper programmare. Installi Visual Studio Code con l'estensione Live Server, capisci la struttura base di HTML5 (tag, elementi semantici come header/main/footer), CSS3 (reset, collegamento al foglio di stile) e JavaScript (variabili, getElementById, event listener). Impari a comunicare con Claude in formato JSON, a fargli generare un prompt ottimizzato e poi il codice del sito diviso in tre file separati. Carichi tutto su GitHub e scopri come inserire immagini tramite hosting esterno. Una panoramica pratica per partire.

---

## Knowledge Atoms (KA)

### KA-17-01: Definizione vibe coding
Generare codice (siti web, automazioni) sfruttando l'AI, senza saper programmare. Non e' "non sapere niente" — serve capire almeno le basi di come funziona un sito web o un'automazione.

### KA-17-02: Stack minimo per vibe coding web
- **Editor:** Visual Studio Code (gratuito, cross-platform)
- **Preview:** estensione Live Server (Ritwick Dey) — hot reload su save
- **AI:** Claude (claude.ai) come generatore di codice
- **Hosting codice:** GitHub (repository per versionamento + collegamento a hoster)
- **Hosting immagini:** Imgur (per ottenere URL diretti da passare al codice)
- **Alternativa editor:** Cursor (fork VS Code con AI nativa, supporta Claude)

### KA-17-03: Struttura base progetto web — 3 file separati
Regola esplicita di Andrei: **MAI** HTML+CSS+JS in un unico file. Sempre separati:
1. `index.html` — struttura (perche' "index": gli hoster lo riconoscono come pagina principale)
2. `style.css` — aspetto visivo
3. `main.js` — comportamento dinamico

Motivazione: leggibilita', facilita' di modifica con AI, meno errori del server.

### KA-17-04: HTML5 boilerplate — shortcut e struttura
- Shortcut VS Code: digitare `html:5` → Emmet Abbreviation genera tutto il boilerplate
- Struttura: `<!DOCTYPE html>` → `<html lang="en">` → `<head>` (meta, CSS link, SEO) + `<body>` (contenuto visibile)
- Titolo: `<title>` nel head (appare nella tab del browser)

### KA-17-05: Elementi semantici HTML — non decorazione, funzione
Tre contenitori obbligatori nel body:
- `<header>` — navbar
- `<main>` — contenuto
- `<footer>` — info legali, copyright

**Perche' semantici e non div:** accessibilita' (screen reader per non vedenti), SEO e indicizzazione Google. Non e' opzionale, e' strutturale.

### KA-17-06: CSS reset universale — primo step sempre
```css
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
```
- **padding:** spaziatura interna
- **margin:** spaziatura esterna
- **box-sizing: border-box:** il padding non aggiunge larghezza extra

Collegamento: nel `<head>` con `<link rel="stylesheet" href="./style.css">`

### KA-17-07: JavaScript — ruolo e meccanismo base
- Ruolo: rendere pagine dinamiche (bottoni, popup, interazioni)
- Collegamento: `<script src="./main.js">` **prima della chiusura `</body>`** (non nel head)
- Pattern base:
  1. Dare `id` agli elementi HTML
  2. `let elemento = document.getElementById("id")`
  3. `elemento.addEventListener("click", function() { ... })`
  4. Modificare contenuto con `.innerHTML`

### KA-17-08: Formato JSON per comunicare con Claude
Claude capisce il JSON **molto meglio del linguaggio naturale** per progetti strutturati. Il JSON funziona come una scaletta che divide il progetto in sezioni e sottosezioni. Pattern:
1. Descrivere il progetto in linguaggio naturale
2. Chiedere a Claude di convertirlo in prompt JSON
3. Chiedere "E' il miglior prompt che puoi darmi?" per farlo iterare
4. Rispondere alle domande di Claude (target, stile visivo, servizi)
5. Specificare le tecnologie (HTML5, CSS3, JavaScript)
6. Usare il prompt JSON finale in una **nuova chat** per generare il codice

### KA-17-09: Workflow vibe coding — 2 fasi distinte
**Fase 1 — Prompt engineering:** una chat dedicata per far generare/raffinare il prompt JSON
**Fase 2 — Code generation:** chat nuova, prompt JSON incollato, Claude genera il codice
Separare le fasi evita contaminazione del contesto.

### KA-17-10: Regola file separati nel codice generato
Se Claude genera tutto in un blocco unico → chiedere esplicitamente di separare in 3 file (HTML, CSS, JS). Motivazione: leggibilita', modifiche puntuali piu' facili, meno errori server.

### KA-17-11: Gestione immagini — hosting esterno obbligatorio
Non basta "mandare un'immagine a Claude" — il codice ha bisogno di URL. Workflow:
1. Hostare l'immagine su Imgur (o simile)
2. Copiare il link diretto dell'immagine
3. Passare quel link a Claude nel prompt

### KA-17-12: GitHub come deposito codice
- "Social media dei programmatori"
- Repository: nome senza spazi ne' caratteri speciali (usare underscore)
- Upload: drag & drop tramite "Upload an existing file" → Commit Changes
- Collegamento a hosting: funziona anche con repo privati

### KA-17-13: Front-end vs back-end — distinzione operativa
- **Front-end:** cio' che vede l'utente (HTML/CSS/JS nel browser)
- **Back-end:** cio' che accade dietro le quinte (automazioni, database, API)
- Esempio concreto: un form di contatto generato da Claude **non funziona da solo** — va collegato a un back-end tramite API

### KA-17-14: API — definizione pratica
Prendono dati, li inviano a un server/database e ricevono una risposta. Per le automazioni, Python e' preferito a JS perche' ha piu' librerie e possibilita' (incluse le chiamate API).

### KA-17-15: Approccio reale al lavoro — ibrido
Non "vibe coding tutto da zero". Nella realta': usare un website builder (Squarespace, WordPress) per la struttura, e il codice generato dall'AI **solo per personalizzazioni specifiche** (code block custom).

### KA-17-16: Pattern multi-chat per progetto completo
Non fare tutto in un singolo prompt. Dividere il lavoro in chat separate:
- Una per il copy
- Una per il branding
- Una per la struttura
- Una per le immagini
Ogni chat ha il contesto giusto per il suo dominio.

### KA-17-17: Gestione errori — console → Claude
Copiare l'errore dalla console del browser e incollarlo direttamente a Claude, senza cercare di spiegarlo. Claude capisce subito dove intervenire.

### KA-17-18: Trucchi VS Code
- `lorem` + numero di parole → genera testo placeholder
- `Ctrl+S` / `Cmd+S` → salvare dopo ogni modifica (Live Server aggiorna in automatico)
- Dividere schermo tra codice e browser per lavorare comodi
- Tasto destro → "Open with Live Server" per preview

---

## 14 Workflow dimostrati

1. Installare e configurare Visual Studio Code
2. Creare struttura base progetto web in VS Code
3. Visualizzare sito in tempo reale con Live Server
4. Strutturare pagina HTML con elementi semantici
5. Rendere pagina dinamica con JavaScript (esempio bottone)
6. Creare repository su GitHub e caricare file
7. Generare prompt JSON ottimizzato con Claude per creare sito web
8. Generare sito web da prompt JSON con Claude
9. Copiare codice generato da Claude in VS Code e lanciare sito
10. Inserire immagine nel sito tramite hosting su Imgur
11. Modificare un code block direttamente in VS Code
12. Gestire errori dando output console all'AI
13. Fare modifiche continue al sito usando memoria di Claude
14. Approccio multi-chat per sito completo (copy, branding, codice, immagini)

---

## Analisi frame (parziale — 78 frame, primi ~3 min)

| Frame | Contenuto |
|---|---|
| 001-020 | Talking head — Andrei introduce il concetto di vibe coding |
| 020 | Slide: logo Visual Studio Code |
| 025-029 | Talking head — spiega il ruolo di VS Code |
| 030 | Screen share: pagina download VS Code (code.visualstudio.com) |
| 035 | VS Code aperto — progetto "CORSO" vuoto, schermata welcome |
| 040 | VS Code — testo overlay "index.html" (spiega naming) |
| 050-054 | VS Code — creazione file nell'explorer |
| 055 | VS Code — file "index.html" appare nel campo di testo del nuovo file |
| 058-060 | VS Code — index.html aperto, file vuoto |
| 063 | VS Code — digita `html:5`, autocomplete Emmet Abbreviation |
| 065 | VS Code — boilerplate HTML5 generato (DOCTYPE→html→head→body), tutto selezionato |
| 068 | VS Code — cursor posizionato su `<title>Document</title>` |
| 070 | VS Code — titolo cambiato in "Corso su Vib..." + sottotitolo: "Cio' che vedi adesso e' come un sito (ogni sito al mondo) e' fatto da dietro le quinte" |
| 072-078 | VS Code — completato titolo "Corso su Vibe coding", scritto "Corso vibe coding" nel body (linea 9) |

**Nota:** estrazione frame interrotta dal crash della sessione. Il video completo (su disco) copre tutti i 14 workflow elencati. Il testo ufficiale della piattaforma ("Cosa hai imparato" + workflow) fornisce copertura completa del contenuto.

---

## Connessioni a skill/workflow DE

| Skill DE | Connessione | Gap? |
|---|---|---|
| `site-build` | Andrei insegna esattamente il workflow base che `site-build` automatizza: HTML+CSS+JS separati, prompt strutturato, Live Server. DE lo fa gia' a livello industriale con agenti dedicati (shell/pages/interactions). | No gap — DE e' piu' avanzato |
| `site-premium-stack` | Andrei usa stack base (HTML5/CSS3/JS vanilla). DE usa Next.js + Tailwind + shadcn + Framer Motion + GSAP. Distanza enorme, ma il principio "file separati" e' lo stesso. | No gap |
| `frontend-design` | "Elementi semantici per accessibilita'/SEO" — gia' coperto in DE. | No gap |
| `web-builder` | Andrei consiglia ibrido builder+code custom — DE ha `web-builder` con design system. | No gap |
| `site-copy` | Pattern "multi-chat per dominio" (una chat copy, una branding, una struttura) — DE lo fa con agenti separati (`site-copy-hero`, `site-copy-body`, `site-copy-meta`). | No gap — DE e' piu' avanzato |
| `impeccable` | "Prompt JSON per strutturare la richiesta" — DE usa gia' prompt strutturati. | No gap |

**Verdetto enrichment:** nessuna patch necessaria. Il contenuto di questa lezione e' **entry-level** rispetto a dove DE opera. Il valore per DE e' pedagogico (come Andrei spiega concetti base ai non-tecnici), non tecnico.

---

## Pattern didattici rilevanti

1. **"E' il miglior prompt che puoi darmi?"** — tecnica di auto-iterazione del prompt. Semplice ma efficace per utenti non tecnici.
2. **2-fase (prompt engineering → code generation)** — separare la preparazione del brief dalla generazione. Identico al pattern DE di brief→design→build.
3. **Console error → AI** — "non spiegare l'errore, copialo e incollalo" — approccio corretto, riduce il "telephone game" tra utente e AI.
