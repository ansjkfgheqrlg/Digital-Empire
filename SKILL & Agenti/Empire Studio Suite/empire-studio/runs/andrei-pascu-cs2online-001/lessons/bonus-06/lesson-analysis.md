# Bonus 6 — Automatizzare processi con skills

**Corso:** Claude Speedrun 2 | **Sezione:** Lezioni BONUS (6/6 — ULTIMA LEZIONE DEL RUN)
**URL:** https://www.andrei-copy.com/cs2online/bonus-6--346en
**Video:** Vimeo `1178259409`, durata 20:36 (1236s)
**Tipo:** **PRATICA** — lezione capstone, confermata con 28 frame (14 scan 90s + 14 dense).
**Fonte:** panoramica + "Cosa hai imparato" ufficiali (16 bullet), nessuna trascrizione .md.

---

## Mappa timeline (confermata)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–6:00 | Talking head — SOP prerequisito, domain knowledge, terminologia (discovery/strategy/onboarding call) | — |
| 6:00 | **Demo**: draw.io/diagrams.net vuoto, palette forme (processo/trigger/rombo/database) | `frame-t6m00s...jpg` |
| 9:00 | **Demo**: flowchart reale "Trigger → chiamata di discovery → sviluppo preventivo (icona AI) → pagamento → chiamata onboarding → [richiami cliente / contratto per iva]" | `frame-t9m00s...jpg` |
| 11:00 | **Demo**: flowchart esteso "chiamata onboarding → client overview document → contesto per AI" (Wispr Flow visibile in menu bar, confermando uso reale del tool dettatura già visto in lezione 13) | `frame-t11m00s...jpg` |
| 14:00 | **Demo — SKILL.md COMPLETO E LEGGIBILE**: skill "sviluppo-preventivo", vedi testo integrale sotto | `frame-t14m00s...jpg` |
| 18:00 | **Demo**: file reference "struttura-preventivo.md" — Pagina 1: design cartina, Pagina 2: introduzione al business, Pagina 3... | `frame-t18m00s...jpg` |
| 19:30 | **Demo**: Claude genera il preventivo, checklist step visibile, "Step 3: Validazione... utilizza expert per effort max", "Step 4: crea il preventivo finale in PDF seguendo brand guidelines" | `frame-t19m30s...jpg` |
| 20:15 | **Demo**: flowchart finale completo con icone robot AI su tutti gli step automatizzati (sviluppo preventivo, client overview document, contesto per AI) — tab browser "Preventivo - Bolletta Zer..." visibile, esempio reale di cliente | `frame-t20m15s...jpg` |
| 20:20–20:36 | Talking head, chiusura corso | — |

---

## SKILL.md osservato per intero (verbatim, frame t14m00s)

```
---
name: sviluppo-preventivo
description: Serve per sviluppare preventivi per clienti. Usare quando l'utente chiede di fare un preventivo.
---

## Informazioni in entrata
Entreranno le seguenti informazioni con la seguente documentazione. Se queste info non
entrano, chiederle all'utente e rifiutarsi categoricamente di procedere senza le seguenti
documentazioni:
1. Trascrizione della discovery call
2. Ipotetica trascrizione della eventuale discovery call 2
3. Tabella o lista con le condizioni o i prezzi.

## Informazioni in uscita [cosa devi produrre tu, Claude]
Devi creare un preventivo finale in PDF seguendo le indicazioni sotto.

## Steps da seguire

### step 1
Creare un markdown con il copy del preventivo. Il preventivo è diviso nelle seguenti pagine e
puoi trovare un esempio in esempio.md in references.
```

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Precondizione per automatizzare: serve un processo ripetitivo GIÀ standardizzato (SOP) — "la maggior parte della gente non riesce a implementare l'AI perché non ha un processo ripetuto che vale la pena automatizzare". | "Cosa hai imparato" |
| KA-02 | Concetto "domain knowledge": bisogna essere esperti del processo PRIMA di automatizzarlo, altrimenti l'automazione non porta risultati — eco diretto del principio "meccanico esperto" di lezione 1 del run cs2online. | "Cosa hai imparato" |
| KA-03 | Metodo di documentazione visiva: diagram maker gratuito (draw.io/diagrams.net) con forme standard (processo=rettangolo, trigger, terminator, scelta=rombo, database) per mappare il processo prima di automatizzarlo. | "Cosa hai imparato" + frame t6m00s |
| KA-04 | Processo di acquisizione clienti reale mappato: Trigger (prospect qualificato) → chiamata di discovery → **sviluppo preventivo (AI)** → pagamento → chiamata onboarding → **client overview document (AI)** → **contesto per AI**. Solo alcuni step marcati con icona robot = automatizzabili, altri (call, pagamento) restano manuali. | frame-t9m00s, t11m00s, t20m15s |
| KA-05 | **Pattern anti-hallucination confermato per la terza volta nel run** (dopo Bonus 2 KA-04 e lezione 1): SKILL.md scritto per "rifiutarsi categoricamente di procedere" se mancano documenti obbligatori (trascrizione discovery call, tabella prezzi) — non un'eccezione isolata, è un pattern sistematico dell'autore. | frame-t14m00s (SKILL.md verbatim) |
| KA-06 | Principio "step singoli, non compressi": dividere il workflow in step separati e validati uno per uno invece di comprimere tutto in un prompt unico — l'AI "lavora meglio con step singoli e validati". | "Cosa hai imparato" |
| KA-07 | Struttura reference multi-file per una skill complessa: `esempio.md` (preventivo reale passato, per stile/tono), `struttura-preventivo.md` (struttura pagine), `brand-guidelines.json` — collegati e visualizzabili con la graph view di Obsidian. | "Cosa hai imparato" + frame t18m00s |
| KA-08 | Parametro **"effort max"**: usato selettivamente SOLO sullo step di validazione (non su tutto il task) — osservato a schermo: "Step 3: Validazione... utilizza expert per effort max", "Step 4: crea il PDF finale". Uso mirato del massimo sforzo computazionale solo dove serve precisione, non ovunque. | frame-t19m30s |
| KA-09 | Possibilità di aggiungere asset (foto, immagini) dentro la cartella skill per farli inserire automaticamente nel documento finale generato. | "Cosa hai imparato" |

## Connessione con Knowledge Base esistente — MOLTO RILEVANTE

**Questa lezione tocca DIRETTAMENTE il dominio della tensione aperta con `beast-preventivi`** (segnalata a Max nel run YouTube, video 24 `EBU57iVAutA`, mai risolta). Qui l'autore mostra un intero sistema di **generazione preventivi via AI** con struttura a pagine definita (`struttura-preventivo.md`). Non ci sono elementi in questo materiale che risolvono direttamente la tensione KA-14/AP-05 (breakdown prezzi sì/no), ma:
- KA-05 (rifiuto categorico se mancano dati) è un pattern di sicurezza generale, applicabile a `beast-preventivi` indipendentemente da quella tensione — vedi enrichment-report per valutazione.
- Il sistema completo (flowchart + SOP + skill Obsidian) è un caso di studio concreto e maturo di "skill per processo ripetitivo" — utile come possibile secondo riferimento per `beast-preventivi` se Max decide di estenderla con automazione AI.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 28 frame visionati, SKILL.md trascritto per intero da screenshot leggibile |
| NO-STUB | PASS — video 20:36 intero mappato |
| P12 traceability | PASS |

**RUN COMPLETATO**: questa era l'ultima lezione nell'ordine richiesto da Max (16 → Bonus 1-6). Vedi MASTER-RUN-TRACKER.md per stato finale.
