---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PIANO-COMPLETAMENTO-L3.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# ARCHITETTURA — Completamento Workflow Estate
> 2026-07-23 · Claude · Struttura che i 6 lotti costruiscono. Contratti prima del codice.

## 1. Principio portante
Il Workflow Estate ha già i **piani** (P7, WF-S1..S6) e ha già il **motore** (`empire/flow`).
Quello che manca è il ponte fra i due: **i fatti**. Un gate rosso perché nessuno ha scritto il fatto
è indistinguibile da un gate rosso perché il lavoro non è stato fatto — ed è esattamente l'errore
che ha tenuto Gate-DEC rosso mentre la decisione era attiva da due giorni.

```
        PIANI (.md)                MOTORE (empire/)              REALTÀ (file, €, video)
   PLANNING-P7, WF-S1..S6   →   flow · inspect · dash   ←→   pagine, PDF, lead.csv, video
                                        ▲
                                        │
                                    I FATTI
                              empire/.data/flow/facts.json
```
**Regola architetturale:** un fatto si scrive solo se corrisponde a qualcosa di verificabile su disco
o confermato da un umano. Nessun fatto "di comodo".

## 2. Componenti — cosa costruisce ogni lotto

### 2.1 `empire/inspect/` — LOTTO 1 (nuovo)
Il modulo che la dashboard invoca da giorni e che non esiste.
```
empire/inspect/
  __init__.py     API pubblica: status(), telemetry(), scorecard(), first_pass(), ttd(), feedback(), traceability()
  sources.py      da dove vengono i numeri: 02-AUTOMAZIONI-E-SCRIPTS/{performances,feedback,sessions,checkpoints}
  metrics.py      calcolo delle 6 metriche
  cli.py          `empire inspect status|telemetry|scorecard`
```
**Contratto con la dashboard:** ogni metrica ritorna `{value, status, source, note}`.
Se non ci sono dati, ritorna `value=0, note="nessun dato registrato"` — **mai** `n/d (non implementato)`.
La differenza è sostanziale: "zero esecuzioni registrate" è un'informazione vera, "modulo non
implementato" è un difetto travestito da metrica.

### 2.2 `empire/flow` — LOTTO 2 (estensione)
- `decisions.py` (nuovo): applica ADR-EST-006. Legge il blocco `decisions:` di `workflows.yaml`,
  confronta `veto_deadline` con adesso, e se scaduto senza veto registrato → **decisione ATTIVA**
  + fatto `dec_<id>_attiva = 1`. Idempotente.
- `gate.py` (estensione): i gate `human` guadagnano un campo **evidence** — un'evidenza calcolata
  dai dati veri e mostrata all'umano che deve confermare. Il gate resta human: l'evidenza informa,
  non decide.
- **Fonte evidenza Gate-CONTATTI:** `06-DASHBOARD-E-METRICHE/lead.csv`, colonna stato/ultimo contatto.

### 2.3 Checkout — LOTTO 3 (nuovo)
Il pezzo che trasforma la landing in un incasso.
```
Crea siti/Siti CCM/
  checkout.config.json   ← UNICA fonte di verità dei link di pagamento
  pagamento.html         ← fallback attivo oggi (PayPal / bonifico / form)
empire/tools/checkout.py ← inietta i link nelle pagine · `--check` conta i placeholder
```
**Contratto:** nessun link di pagamento è scritto a mano nell'HTML. Max incolla 2 link nel JSON,
lancia un comando, tutto il sito è allineato. Il gradino 2 della ladder (`pagamento.html`) è
**attivo da subito**: il visitatore può pagare oggi anche senza Stripe.

### 2.4 Prova commerciale — LOTTO 4 (nuovo)
```
Clienti/Prof Autocad/preventa-launch-kit/
  07_CASE_STUDY_NOVACAR.{md,html,pdf}
Crea siti/Preventa/
  index.html            landing standalone dal copy 01_LANDING_COPY_ONE_PAGE.md
```
**Fonte dei numeri (non inventati):** CP-20260702-003, CP-20260702-002, CP-20260703-001 —
template sul modello Novacar, 14 regole, gate IMG/R, PDF via cdp, GUI premium, .exe validata.
**Vincolo:** ogni cifra nel case study deve essere rintracciabile a un checkpoint. Se un numero
non ha fonte, non entra.

### 2.5 Pacchetto video — LOTTO 5 (nuovo)
```
WORKFLOW-ESTATE/07-VIDEO-RUN/<run-id>/
  00-SCELTA.md         video competitor scelto + perché (dati da youtube-niche-scout-analysis)
  01-SCRIPT-IT.md      script italiano a scene (riformulato, non tradotto — gate anti-copia)
  02-TTS.txt           testo pulito per sintesi vocale
  03-SHOTLIST.md       inquadratura per scena
  04-SEO-PACK.md       titolo, descrizione con link Manuale, tag, capitoli
  05-STATO.md          quale gradino della ladder si è raggiunto, onestamente
```
**Contratto di onestà:** `05-STATO.md` dichiara esattamente cosa esiste. Se il render non è
avvenuto, lo dice e registra l'errore. La chiave Fliki è **vuota** (verificato): il gradino 1 è
morto in partenza.

### 2.6 Chiusura — LOTTO 6
```
empire/flow/eod.py                            WF-MEM-EOD + WF-MEM-RETRO eseguibili
empire/estate.py                              il comando unico di verdetto (L3 §2)
06-DASHBOARD-E-METRICHE/AZIONI-MAX.md         le 4 cose che restano a Max
```

## 3. Contratti fra lotti (le uniche interfacce ammesse)

| Da | A | Cosa passa | Come |
|---|---|---|---|
| 1 | 6 | metriche telemetria | `empire.inspect.status()` |
| 2 | 6 | stato gate | `empire.flow.gate.evaluate_all()` |
| 3 | 2 | pagine senza placeholder | file su disco, letto dal Gate-FUNNEL |
| 4 | 6 | artefatti da registrare | percorsi dei file prodotti |
| 5 | 6 | esito ladder | `05-STATO.md` |

Nessun altro accoppiamento è consentito. Se un lotto sente il bisogno di un'altra interfaccia,
è un segnale che il perimetro è sbagliato: si ferma e lo segnala.

## 4. Struttura finale di WORKFLOW-ESTATE
```
01-FLUSSI-E-PIANI/      + PIANO-COMPLETAMENTO-L1/L2/L3 + ARCHITETTURA-COMPLETAMENTO
02-AUTOMAZIONI-E-SCRIPTS/  (sorgente dati per inspect)
03-AGENTI-E-RUOLI/
04-SKILLS-E-REFERENCE/     (sola lettura per tutti i lotti)
05-TEMPLATES-E-KIT/
06-DASHBOARD-E-METRICHE/   + AZIONI-MAX.md
07-VIDEO-RUN/           ← NUOVO (lotto 5)
```

## 5. Cosa NON si costruisce (deciso, non dimenticato)
- **Pubblicazione caroselli su `crea.illtuo_impero`** — pagina a zero (D-EST-006). La fabbrica sì, la pubblicazione no.
- **Riscrittura di `agency-empire`** — già toccato da un'altra sessione, ADR-003.
- **Scaling YouTube oltre 1 video** — taglio 80/20 di P7 §6.
- **Invio outreach reale** — gated a Max (G-A4).

---
⛓️ P12: `ARCH-COMPL#estate-2026` · attua: L3 · verdetto: `python -m empire estate`
