---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #vsl #script #video #L2.1
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-VSL — Workflow Script VSL

> **Ecosistema:** 04-MARKETING · **Reparto:** L2.1 Copywriting · **Durata target:** 60-90 min
> **Gate di uscita:** score A8 ≥80 + timing check + G2 brand gate

---

## Scopo

Produce lo script completo di un VSL (Video Sales Letter) strutturato per la registrazione
video. Il VSL è una sales page in formato video: stessa struttura APSOC, ma adattata al
parlato e al timing. Ogni sezione dello script ha una durata target in minuti. Usato da
02-INFO-BUSINESS per lanci corsi e da 01-AGENCY per video di presentazione offerta.

---

## Caratteristiche dello script VSL

- **Lunghezza target:** 8-20 minuti di video parlato (±1.500-3.500 parole di script)
- **Formato:** script parlato, non pagina web — frasi brevi, ritmo naturale, pause indicate
- **Struttura:** APSOC adattato al video con timing per sezione
- **Annotazioni:** lo script include note di regia (pausa per proof, mostra screen, cambio tono)

---

## Timing consigliato per sezione

| Sezione | Durata target | Contenuto |
|---|---|---|
| A — Hook video | 0:00-1:00 | Prima frase nei 5 secondi; hook che blocca lo scroll |
| P — Problema | 1:00-4:00 | Amplificazione dolore; speaker si avvicina all'identitario |
| S — Soluzione | 4:00-8:00 | USP + meccanismo unico + proof visiva (screen, testimonianze) |
| O — Obiezioni | 8:00-10:00 | 2-3 CPB; tono diretto "lo so che stai pensando..." |
| C — CTA | 10:00-12:00 | CTA specifica + urgenza reale + passi concreti |

---

## Passi del workflow

### Step 1 — Contratto (COPY-MASTER)
**Agente:** COPY-MASTER
**Input:** contratto con `formato: "vsl"`, durata target, piattaforma (YouTube, Vimeo, funnel)
**Azione:** verifica ICP + awareness; definisce durata e struttura timing; coordina con 05-MB
se il VSL è per YouTube
**Output:** contratto validato + struttura timing dichiarata

### Step 2 — Briefing VSL (A1)
**Agente:** A1 Briefing Analyst
**Input:** contratto + materiali + durata target
**Azione:** briefing-vsl.md con timing dichiarato per sezione + proof visive disponibili (schermata,
demo, testimonianza video se disponibile)
**Output:** `briefing-vsl.md`

### Step 3 — Avatar + pain map (A2, se non in namespace)
**Agente:** A2 Target Analyst
**Output:** avatar + pain map + language map in namespace

### Step 4 — Script APSOC (A3-A7 per sezioni VSL)
**Agente:** COPY-MASTER coordina A3-A7 in sequenza con annotazioni timing
- **A3:** hook video 0-5 secondi (più critico del headline scritto) + apertura 0:00-1:00
- **A4:** script sezione P 1:00-4:00; tono parlato; ZERO prodotto; pause indicate
- **A5:** script sezione S 4:00-8:00; proof visiva (note: "mostra risultato X a schermo")
- **A6:** script sezione O 8:00-10:00; 2-3 CPB in formato dialogico
- **A7:** script sezione C 10:00-12:00; CTA con URL dichiarato esplicitamente
**Output:** `script-vsl.md` con timing e annotazioni regia

### Step 5 — Gate G1 (A8)
**Agente:** A8 Copy Reviewer
**Input:** script-vsl.md + briefing-vsl.md
**Azione:** scoring APSOC 100pt adattato a formato parlato + timing check (il timing è
rispettato? le sezioni sono bilanciate?) + violazioni automatiche
**Gate G1:** ≥80 → PASS | < 80 → COPY-QA-LEAD
**Output:** `qa-report-vsl.md` con score + timing check

### Step 6 — Gate G2 brand (BR-QA, L2.5)
**Agente:** BR-QA Brand Consistency Verifier
**Input:** script gated G1 + brand_kit
**Azione:** check voce del brand nel formato parlato (la brand voice cambia tono nel parlato?)
**Gate G2:** PASS → rilascio | FAIL → feedback specifico
**Output:** `brand-gate-vsl.md`

---

## Gate di uscita

| Gate | Responsabile | Soglia | Bloccante |
|---|---|---|---|
| G1 Score APSOC | A8 | ≥80 | SI |
| Timing check | A8 | sezioni bilanciate | SI — script fuori timing non si consegna |
| G2 Brand | BR-QA (L2.5) | PASS | SI |

---

## Connessioni

- [[WF-COPY-FULL]] · `workflow/WF-COPY-FULL.md` — pipeline base da cui deriva la struttura
- [[copy-master]] · `agenti/copy-master.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[L2-5-Brand-Creative-Strategy]] · gate G2 brand voice nel formato parlato
