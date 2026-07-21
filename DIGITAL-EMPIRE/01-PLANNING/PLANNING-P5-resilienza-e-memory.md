# PLANNING-P5 — Resilienza, Fallback Ladder & Memory-First
> Livello 5 di 7 · migliora P4: il piano non si rompe se qualcosa fallisce; ogni evento lascia traccia in memoria.

## 1. Fallback ladder per ogni punto di rottura

| Punto di rottura | Livello 1 | Livello 2 | Livello 3 (ultima spiaggia) |
|---|---|---|---|
| Checkout S2 | Stripe Payment Link | Gumroad | PayPal.me / bonifico con modulo Typeform |
| Pubblicazione caroselli S3 | Meta Graph API | Buffer | manuale batch (25/07, 20') |
| Pipeline S4 | Meta Graph API + gate QA auto | Buffer + QA auto | **NESSUN fallback manuale**: se non è 100% auto → standby (condizione Max F-07) |
| Video S5 | API Fliki | script + stock footage (Pexels) + TTS + ffmpeg | solo pubblicazione differita; S5 slitta, S1/S2 intoccati |
| Swarm Opus occupato | coda priorità (P3 §4) | task degradato a esecuzione singola | slitta alla finestra successiva |
| Max irreperibile | default decisions (veto scade → vale default) | Chief Forge esegue il default | checkpoint + notifica in dashboard |

## 2. Kill criteria & gates (mancavano nel dossier — chiusura A-05)

| Gate | Data | Condizione GO | Se NO-GO |
|------|------|---------------|----------|
| Gate-DEC | 21/07 h20:00 | DEC-001 ATTIVA (decisa o default) | impossibile: il default scatta da solo |
| Gate-FUNNEL | 22/07 h20:00 | checkout test €1 riuscito | passa al fallback checkout (max 2h) |
| Gate-CONTATTI | 23/07 h12:00 | 7/7 contattati | Max delega follow-up a script Claude; push S2 compensa |
| Gate-S4 | 24/07 h20:00 | pipeline E2E: batch→QA→scheduler→report OK | mentalita.brutale resta STANDBY (regola Max) |
| Gate-S5 | 23/07 h18:00 | test API Fliki OK | fallback ladder video; se anche quello fallisce → S5 alla settimana prox |
| Gate-REV | 26/07 | ≥1 anticipo incassato | RETRO onesta: causa radice → pattern correttivo in ReasoningBank |

## 3. Protocollo Memory-First (GIÀ ATTIVO in `00-MEMORY/`)
- **Regola zero**: task chiuso → checkpoint. Comando: `python3 00-MEMORY/memory_manager.py checkpoint --task <WF> --note <esito>`.
- **Tipi di atomo**: `checkpoint`, `decision` (con veto window), `plan` (P1..P7 registrati), `brainstorm`, `error`, `metric`, `pattern` (ReasoningBank), `retro`.
- **Tracciabilità P12**: ogni atomo ha `id` + `trace: "<ID>#estate-2026"`. Ogni artefatto cita gli ID delle decisioni che lo hanno generato.
- **Cadenza obbligatoria**: EOD h19:00 checkpoint giornaliero + metriche del giorno (`metric --name ...`); a fine WF `checkpoint --task WF-*`.
- **ReasoningBank**: in RETRO (26/07) ogni "cosa ha funzionato" diventa `pattern` riusabile dai WF futuri (es. oggetto WA con più risposte, hook carosello con più engagement, sequenza chiusura S1).

## 4. Failure modes per stream (sintesi operativa)

| Stream | Fallimento tipico | Sintomo | Recupero |
|--------|-------------------|---------|----------|
| S1 | "Ti richiamo a settembre" | risposta dilatoria | msg-3 binario + bonus in scadenza (WF-S1 §obiezioni) |
| S1 | lead sparisce | nessuna risposta 48h | follow-up msg-4 + canale alternativo (da lista G-02) |
| S2 | checkout rotto | test €1 fallito | fallback ladder, max 2h poi escalation Chief Forge |
| S3/S4 | action-block IG | publish rifiutato | stop 24h, ripresa a 1 contenuto/2gg (R-06) |
| S5 | Fliki 429/5xx | errore API | retry×3 → error in memoria → ladder video |
| S6 | nome impugnato a veto | veto entro finestra | shortlist passa alla #2, dominio verificato entro 24/07 |

## 5. Integrazione sistema nervoso (ruflo)
Hook pre/post task → chiamate `memory_manager.py` (vedi `06-NERVOUS-SYSTEM/swarm.estate.yaml`). Se ruflo non è installabile nell'ambiente, **l'orchestrazione resta eseguibile da file**: `03-WORKFLOWS/workflows.yaml` + questo protocollo bastano a far girare il workshop.

---
⛓️ Trace P12: `PLANNING-P5#estate-2026` · input: P4 · chiude: A-05 · vincoli: F-07
