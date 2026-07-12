---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #acquisizione #outreach #apsoc #bibbia #wrap #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# ARCHITETTURA — A2 Acquisizione / Outreach

> **Ecosistema:** 01-AGENCY · **Standard:** CF-grade (ADR-007) · **ADR-003:** il runtime è ATTIVO, si WRAPPA, non si riscrive.
> Questo reparto avvolge la pipeline di outreach esistente — non la sostituisce, non la modifica fino a validazione del wrapper.

---

## 0. Confine ADR-003 — cosa NON è questo reparto

A2 **documenta e governa** un runtime che già gira in produzione. Il codice vive FUORI da questa
cartella, in `Outreach/Outreach Workflow/`, `Outreach/LinkedIn Automation/`, `Outreach/Instagram Automation/`.
Questo reparto **non possiede il codice**: lo registra nell'organigramma V2, ne definisce i
contratti di handoff, aggiunge il layer di supervisione CF-grade (gate Bibbia formalizzato, KPI,
namespace memoria, state) e descrive come ogni agente INVOCA gli script esistenti.

**Regola d'oro:** nessun file di runtime viene toccato. Ogni motore wrappato è marcato `[WRAPPA]`
con il nome reale dello script. Se serve cambiare il motore → si propone un ADR, non si riscrive.

---

## 1. Gerarchia del reparto

```
L1 01-AGENCY (AG-DIR)
  └── L2 A2 ACQUISIZIONE (AG-A2-COORD — coordinator, orchestra i 4 WF)
        ├── Strategia / Scrittura
        │   ├── AG-A2-STRAT  (sonnet) — angolo APSOC per lead   [WRAPPA strategist.py, insight.py]
        │   ├── AG-A2-WRITE  (sonnet) — copy APSOC + variazione  [WRAPPA writer.py, humanizer.py, copy_knowledge.py]
        │   └── AG-A2-FUP    (sonnet) — sequenze follow-up        [WRAPPA followup_writer.py]
        ├── QA / Gate
        │   └── AG-A2-QA     (sonnet, verifier) — Gate Bibbia 3 check  [WRAPPA bibbia_team.py] — BLOCCA, non suggerisce
        ├── Invio per canale
        │   ├── AG-A2-SEND   (haiku) — email + rate limiter       [WRAPPA sender.py]
        │   ├── AG-A2-LI     (haiku) — LinkedIn 20+20+30/gg       [WRAPPA scripts 01→05 + comment_posts.py]
        │   └── AG-A2-IG     (haiku) — Instagram 30 DM/gg         [WRAPPA Instagram DM flow]
        └── Risposta / Booking
            ├── AG-A2-TRIAGE (haiku) — classifica risposta        [skill outreach-reply-triage + reply_monitor.py]
            └── AG-A2-BOOK   (sonnet) — interessato → slot call → conferma → handoff A8
```

**Principio di coordinamento:** AG-A2-COORD apre la run, fa pre-flight delle credenziali,
carica il batch lead e fa fan-out `star` sui 3 canali; ogni canale è internamente una
`pipeline` STRAT → WRITE → QA(Bibbia) → SEND. Nessun messaggio parte senza gate Bibbia verde.

---

## 2. Pipeline operativa — STRAT → WRITE → QA → SEND

```
Batch lead qualificati (da A1, leads.db)
  │
  ▼
AG-A2-COORD (orchestrator.py) — pre-flight credenziali + carico batch
  │
  ├──────────────┬──────────────┬──────────────┐
  ▼              ▼              ▼              ▼
EMAIL          LINKEDIN       INSTAGRAM      REPLY (event-driven)
  │              │              │              │
  ▼              ▼              ▼              ▼
AG-A2-STRAT    AG-A2-LI       AG-A2-IG       AG-A2-TRIAGE
(angolo APSOC) (01→05+comment)(hashtag→DM)   (classifica)
  │              │              │              │
  ▼              │              │         interessato?
AG-A2-WRITE      │              │              ▼
(copy APSOC)     │              │         AG-A2-FUP (conversazione)
  │              │              │              ▼
  ▼              │              │         AG-A2-BOOK (slot call)
AG-A2-QA  ◄──────┴──────────────┘              │
GATE BIBBIA (3 check sequenziali)              ▼
  │                                       HC-AG-CL-01 → A8 Closing
  ├── PASS ──► AG-A2-SEND (cap + log)      HC-AG-AM-01 → A7 Account
  └── FAIL ──► torna a AG-A2-WRITE con note (NON parte)
```

**Regola gate (Art. ADR-003 + REGOLE R1):** un solo check Bibbia FAIL → il messaggio NON
viene inviato. Torna al writer con le note del checker. Il gate è BLOCCANTE, non un suggerimento.

---

## 3. Gate Bibbia — i 3 check sequenziali (AG-A2-QA)

Il gate è eseguito da `AG-A2-QA` che wrappa `bibbia_team.py`. È **sequenziale**: il check N+1
parte solo se il check N è PASS. Un FAIL a qualsiasi check blocca l'intero messaggio.

| # | Check | Cosa verifica | FAIL se |
|---|---|---|---|
| 1 | **Struttura APSOC** | Il messaggio segue Attenzione→Problema→Soluzione→Obiezione→CTA; P prima di S | manca una sezione APSOC, oppure S compare prima di P |
| 2 | **CTA corretta** | La CTA punta a `presentazione-empire.vercel.app`; un solo invito chiaro | CTA assente, link errato, doppia CTA confusa |
| 3 | **No dependency-language** | Nessun linguaggio che crea dipendenza dall'agenzia ("non potrete farcela senza di noi"); tono da "agenzia progettata per essere licenziata" | presenza di dependency-language / promesse non provabili |

**Verdetto:** PASS solo se tutti e 3 i check sono PASS. Il gate è binario — niente "quasi".
L'esito (PASS/FAIL + check fallito + nota) si registra in `agency/a2/email/` (o canale corrispondente).

---

## 4. Wrapper di handoff — contratto I/O del reparto

**Input (da A1 Ricerca → AG-A2-COORD):**
```json
{
  "fornitore": "A1-Ricerca",
  "batch_id": "BATCH-20260622-001",
  "lead_ref": "leads.db (score >= soglia)",
  "canali": ["email", "linkedin", "instagram"],
  "cta_standard": "presentazione-empire.vercel.app",
  "vincoli_cap": "email <=500/gg cap 100/h · LI 20+20+30/gg · IG 30 DM/gg"
}
```

**Output (da AG-A2-BOOK → A8 Closing):**
```json
{
  "handoff": "HC-AG-CL-01",
  "lead_ref": "id interno (no PII nello schema state)",
  "canale_origine": "email | linkedin | instagram",
  "stato": "call_confermata",
  "slot_confermato": "YYYY-MM-DDTHH:MM",
  "thread_ref": "agency/a2/reply/{thread_id}",
  "anagrafica_aperta": "HC-AG-AM-01 → A7"
}
```

---

## 5. Namespace memoria — `agency/a2/` + `agency/outreach`

| Namespace | Path AgentDB | Contenuto | Owner scrittura |
|---|---|---|---|
| Outreach (cross-canale) | `agency/outreach` | Template attivi, performance per variante, log invii | AG-A2-SEND + AG-A2-WRITE |
| Email | `agency/a2/email/` | Per batch: n. inviati, bounce, esiti gate Bibbia (pass/fail) | AG-A2-SEND |
| LinkedIn | `agency/a2/linkedin/` | Connessioni/messaggi/commenti per giorno, stato accettazioni | AG-A2-LI |
| Instagram | `agency/a2/instagram/` | DM inviati/gg, stato follow-up | AG-A2-IG |
| Reply | `agency/a2/reply/` | Thread per lead, stato triage, esito (PII-scan prima di ogni store) | AG-A2-TRIAGE + AG-A2-BOOK |

**Regola PII (REGOLE R3):** prima di ogni store nel namespace `reply` si esegue il PII-scan
(`aidefence_has_pii`). Lo schema di state NON contiene PII (no nomi, no email, no handle in chiaro):
solo riferimenti interni e contatori. Le baseline KPI sono `[DM]` finché non misurate.

Nota: lo stato runtime del motore (DB lead, sessioni, JSON batch) resta nel motore esistente in
`Outreach/Outreach Workflow/` (`leads.db`, `emails_*_ready.json`, sessioni). Il layer memoria
qui sopra è il layer di registrazione/learning del reparto — non duplica il motore.

---

## 6. Namespace script e invocazione del motore

I motori si invocano tramite gli entrypoint esistenti (skill installate + .bat del runtime),
mai riscrivendoli. La mappatura completa vive in `scripts/README.md`. Sintesi:
- `/avvia-email` → WF-OUTREACH-EMAIL (orchestrator.py → strategist → writer → bibbia → sender)
- `/avvia-linkedin` → WF-OUTREACH-LINKEDIN (scripts 01→05 + comment_posts.py)
- `/avvia-ig` → WF-OUTREACH-INSTAGRAM (Instagram DM flow)
- `/avvia-parallel` → Email + Instagram in parallelo
- `/avvia-scraper` → scrape_only.py (raccolta lead, a monte del reparto)
- reply event-driven → `run_reply_manager.py` + `reply_monitor.py` (WF-REPLY-BOOKING)

---

## 7. State e ripartibilità

Ogni run di canale aggiorna un `state.json` nel namespace corrispondente con i contatori del
giorno (inviati, cap residuo, gate pass/fail) e `last_updated`. Questo permette la
**ripartibilità a freddo**: una run interrotta riprende dal cap residuo del giorno senza
risuperare i lead già processati e senza sforare i cap reali. Schema completo in `state/README.md`.

---

## Connessioni

- [[README]] · `README.md` — missione, roster, come si attiva
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A2`
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/03 - Resources/concepts/Framework_Cold_Outreach_APSOC.md`
