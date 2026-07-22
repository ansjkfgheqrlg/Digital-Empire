# FAQ & Steel-manning (`faq.md`)
> Domande di criticità, failure modes e risoluzioni proattive generate secondo il pattern P4.

### Q: Cosa accade se wf-master.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-MASTER.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-MASTER.md](#a-014)

### Q: Cosa accade se loop giornaliero non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Loop giornaliero fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Loop giornaliero](#a-015)

### Q: Cosa accade se mappa gate (specchietto rapido) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Mappa gate (specchietto rapido) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Mappa gate (specchietto rapido)](#a-017)

### Q: Cosa accade se dipendenze (da p3 dag) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Dipendenze (da P3 DAG) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Dipendenze (da P3 DAG)](#a-018)

### Q: Cosa accade se handoff memoria non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Handoff memoria fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Handoff memoria](#a-019)

### Q: Cosa accade se wf-perf-loop.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-PERF-LOOP.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-PERF-LOOP.md](#a-020)

### Q: Cosa accade se 1. il ciclo (t0 → t5, chiuso e confermato) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 1. IL CICLO (T0 → T5, chiuso e confermato) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [1. IL CICLO (T0 → T5, chiuso e confermato)](#a-021)

### Q: Cosa accade se 2. lo schema — performance record (`00-memory/performances/perf-nnn-*.md`) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2. LO SCHEMA — Performance Record (`00-MEMORY/performances/PERF-NNN-*.md`) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2. LO SCHEMA — Performance Record (`00-MEMORY/performances/PERF-NNN-*.md`)](#a-022)

### Q: Cosa accade se 3. lo schema — feedback record (`00-memory/feedback/fb-nnn-*.md`) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3. LO SCHEMA — Feedback Record (`00-MEMORY/feedback/FB-NNN-*.md`) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3. LO SCHEMA — Feedback Record (`00-MEMORY/feedback/FB-NNN-*.md`)](#a-023)

### Q: Cosa accade se 5. esempi concreti (dal workshop reale) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 5. ESEMPI CONCRETI (dal workshop reale) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [5. ESEMPI CONCRETI (dal workshop reale)](#a-025)

### Q: Cosa accade se 6. attivazione non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 6. ATTIVAZIONE fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [6. ATTIVAZIONE](#a-026)

### Q: Cosa accade se 1. setup (21/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 1. Setup (21/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [1. Setup (21/07)](#a-028)

### Q: Cosa accade se 4. cadence & tracking (controllo di qualità ≥92%) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 4. Cadence & Tracking (Controllo di Qualità ≥92%) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [4. Cadence & Tracking (Controllo di Qualità ≥92%)](#a-034)

### Q: Cosa accade se 5. escalation & sicurezza non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 5. Escalation & Sicurezza fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [5. Escalation & Sicurezza](#a-035)

### Q: Cosa accade se 1. pricing attivo (dec-est-001) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 1. Pricing attivo (DEC-EST-001) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [1. Pricing attivo (DEC-EST-001)](#a-037)

### Q: Cosa accade se 2. funnel minimo vendibile non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2. Funnel minimo vendibile fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2. Funnel minimo vendibile](#a-038)

### Q: Cosa accade se 3 email (caricate nel checkout/esp il 22/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3 email (caricate nel checkout/ESP il 22/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3 email (caricate nel checkout/ESP il 22/07)](#a-040)

### Q: Cosa accade se 4. traffico questa settimana (ordine p4) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 4. Traffico questa settimana (ordine P4) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [4. Traffico questa settimana (ordine P4)](#a-042)

### Q: Cosa accade se 5. metriche non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 5. Metriche fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [5. Metriche](#a-043)

### Q: Cosa accade se parte a — s3 crea.illtuo_impero (22→26/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se PARTE A — S3 crea.illtuo_impero (22→26/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [PARTE A — S3 crea.illtuo_impero (22→26/07)](#a-045)

### Q: Cosa accade se a1. audit (21/07 — chiude g-05) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se A1. Audit (21/07 — chiude G-05) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [A1. Audit (21/07 — chiude G-05)](#a-046)

### Q: Cosa accade se a2. attivazione (22/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se A2. Attivazione (22/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [A2. Attivazione (22/07)](#a-047)

### Q: Cosa accade se a3. angoli caroselli (batch 1) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se A3. Angoli caroselli (batch 1) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [A3. Angoli caroselli (batch 1)](#a-048)

### Q: Cosa accade se b1. pipeline target (tutti anelli, nessun buco) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se B1. Pipeline target (tutti anelli, nessun buco) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [B1. Pipeline target (tutti anelli, nessun buco)](#a-050)

### Q: Cosa accade se b2. gate e2e (24/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se B2. Gate E2E (24/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [B2. Gate E2E (24/07)](#a-051)

### Q: Cosa accade se b3. monetizzazione breve (se e solo se on) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se B3. Monetizzazione breve (se e solo se ON) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [B3. Monetizzazione breve (se e solo se ON)](#a-052)

### Q: Cosa accade se metriche s3/s4 non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Metriche S3/S4 fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Metriche S3/S4](#a-053)

### Q: Cosa accade se 1. pipeline 9-stage ( empire studio ) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 1. Pipeline 9-stage ( Empire Studio ) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [1. Pipeline 9-stage ( Empire Studio )](#a-055)

### Q: Cosa accade se 2. render ladder (se gate-s5 🔴) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2. Render ladder (se Gate-S5 🔴) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2. Render ladder (se Gate-S5 🔴)](#a-056)

### Q: Cosa accade se 3. struttura directory di run (memory-first) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3. Struttura directory di run (memory-first) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3. Struttura directory di run (memory-first)](#a-057)

### Q: Cosa accade se 4. seo pack pubblicazione (yt-seo-publisher) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 4. SEO pack pubblicazione (yt-seo-publisher) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [4. SEO pack pubblicazione (yt-seo-publisher)](#a-058)

### Q: Cosa accade se 5. revenue path (verità, da p6) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 5. Revenue path (verità, da P6) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [5. Revenue path (verità, da P6)](#a-059)

### Q: Cosa accade se 1. identità (dopo veto) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 1. Identità (dopo veto) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [1. Identità (dopo veto)](#a-062)

### Q: Cosa accade se 2. promo-kit minimo (dod congelata) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2. Promo-kit minimo (DoD congelata) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2. Promo-kit minimo (DoD congelata)](#a-063)

### Q: Cosa accade se 3. modello commerciale non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3. Modello commerciale fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3. Modello commerciale](#a-064)

### Q: Cosa accade se 5. sinergie non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 5. Sinergie fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [5. Sinergie](#a-066)

### Q: Cosa accade se 6. metriche non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 6. Metriche fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [6. Metriche](#a-067)

### Q: Cosa accade se workflows.yaml non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se workflows.yaml fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [workflows.yaml](#a-068)

### Q: Cosa accade se ═══════════════════════════════════════════════════════════════════ non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ═══════════════════════════════════════════════════════════════════ fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [═══════════════════════════════════════════════════════════════════](#a-072)

### Q: Cosa accade se test_fliki_api(): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se test_fliki_api(): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [test_fliki_api():](#a-074)

### Q: Cosa accade se now(): return datetime.datetime.now().strftime("%y-%m-%d %h:%m:%s") non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")](#a-076)

### Q: Cosa accade se today(): return datetime.datetime.now().strftime("%y%m%d") non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se today(): return datetime.datetime.now().strftime("%Y%m%d") fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [today(): return datetime.datetime.now().strftime("%Y%m%d")](#a-077)

### Q: Cosa accade se nsure(): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se nsure(): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [nsure():](#a-078)

### Q: Cosa accade se next_id(kind): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se next_id(kind): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [next_id(kind):](#a-079)

### Q: Cosa accade se ug(t): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ug(t): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [ug(t):](#a-080)

### Q: Cosa accade se _index(kind, atom_id, title, path): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _index(kind, atom_id, title, path): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_index(kind, atom_id, title, path):](#a-081)

### Q: Cosa accade se tom(kind, title, body): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se tom(kind, title, body): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [tom(kind, title, body):](#a-082)

### Q: Cosa accade se md_init(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_init(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_init(a):](#a-083)

### Q: Cosa accade se md_checkpoint(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_checkpoint(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_checkpoint(a):](#a-084)

### Q: Cosa accade se md_decision(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_decision(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_decision(a):](#a-085)

### Q: Cosa accade se md_plan(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_plan(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_plan(a):](#a-086)

### Q: Cosa accade se md_brainstorm(a): atom("brainstorms", a.title, f"{a.note}\n") non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_brainstorm(a): atom("brainstorms", a.title, f"{a.note}\n") fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_brainstorm(a): atom("brainstorms", a.title, f"{a.note}\n")](#a-087)

### Q: Cosa accade se md_error(a):      atom("errors", f"{a.wf}-failure", f"- **wf:** {a.wf}\n- **erro non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_error(a):      atom("errors", f"{a.wf}-failure", f"- **WF:** {a.wf}\n- **Erro fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_error(a):      atom("errors", f"{a.wf}-failure", f"- **WF:** {a.wf}\n- **Erro](#a-088)

### Q: Cosa accade se md_metric(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_metric(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_metric(a):](#a-089)

### Q: Cosa accade se md_pattern(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_pattern(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_pattern(a):](#a-090)

### Q: Cosa accade se md_retro(a):      atom("checkpoints", "retro-" + a.note[:40], a.note) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_retro(a):      atom("checkpoints", "RETRO-" + a.note[:40], a.note) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_retro(a):      atom("checkpoints", "RETRO-" + a.note[:40], a.note)](#a-091)

### Q: Cosa accade se md_perf(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_perf(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_perf(a):](#a-092)

### Q: Cosa accade se md_feedback(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_feedback(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_feedback(a):](#a-093)

### Q: Cosa accade se md_search(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_search(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_search(a):](#a-094)

### Q: Cosa accade se md_status(a): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se md_status(a): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [md_status(a):](#a-095)

### Q: Cosa accade se main(): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se main(): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [main():](#a-096)

### Q: Cosa accade se carica .env senza dipendenza da python-dotenv non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Carica .env senza dipendenza da python-dotenv fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Carica .env senza dipendenza da python-dotenv](#a-097)

### Q: Cosa accade se _aggiungi_cta(corpo: str) -> str: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _aggiungi_cta(corpo: str) -> str: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_aggiungi_cta(corpo: str) -> str:](#a-098)

### Q: Cosa accade se deliverability: link vietato nella prima email fredda (attiva filtri antispam). non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se DELIVERABILITY: link VIETATO nella prima email fredda (attiva filtri antispam). fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [DELIVERABILITY: link VIETATO nella prima email fredda (attiva filtri antispam).](#a-099)

### Q: Cosa accade se il link va solo nel follow-up #2 (giorno 7). non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Il link va SOLO nel follow-up #2 (giorno 7). fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Il link va SOLO nel follow-up #2 (giorno 7).](#a-100)

### Q: Cosa accade se questa funzione ora è un no-op per la prima email. non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Questa funzione ora è un no-op per la prima email. fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Questa funzione ora è un no-op per la prima email.](#a-101)

### Q: Cosa accade se ─── cli args (opzionali, per backward compatibility) ───────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── CLI args (opzionali, per backward compatibility) ───────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── CLI args (opzionali, per backward compatibility) ─────────────────────────](#a-103)

### Q: Cosa accade se ─── mappatura settore → parola clienti/pazienti ───────────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── Mappatura settore → parola clienti/pazienti ───────────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── Mappatura settore → parola clienti/pazienti ─────────────────────────────](#a-104)

### Q: Cosa accade se _match(mapping: dict, nicchia: str, default: str) -> str: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _match(mapping: dict, nicchia: str, default: str) -> str: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_match(mapping: dict, nicchia: str, default: str) -> str:](#a-105)

### Q: Cosa accade se ─── costruisce il mini-dettaglio specifico per il prompt ──────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── Costruisce il mini-dettaglio specifico per il prompt ──────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── Costruisce il mini-dettaglio specifico per il prompt ────────────────────](#a-106)

### Q: Cosa accade se _nota_contesto(lead: dict) -> str: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _nota_contesto(lead: dict) -> str: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_nota_contesto(lead: dict) -> str:](#a-107)

### Q: Cosa accade se ─── user prompt per il writer ──────────────────────────────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── User prompt per il Writer ──────────────────────────────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── User prompt per il Writer ────────────────────────────────────────────────](#a-108)

### Q: Cosa accade se build_prompt(lead: dict) -> str: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se build_prompt(lead: dict) -> str: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [build_prompt(lead: dict) -> str:](#a-109)

### Q: Cosa accade se ─── helpers ───────────────────────────────────────────────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── Helpers ───────────────────────────────────────────────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── Helpers ─────────────────────────────────────────────────────────────────](#a-110)

### Q: Cosa accade se _parse_json(raw: str) -> dict | none: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _parse_json(raw: str) -> dict | None: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_parse_json(raw: str) -> dict | None:](#a-111)

### Q: Cosa accade se fallback regex non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Fallback regex fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Fallback regex](#a-112)

### Q: Cosa accade se _rx(text, key): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _rx(text, key): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_rx(text, key):](#a-113)

### Q: Cosa accade se oad_existing() -> tuple: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se oad_existing() -> tuple: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [oad_existing() -> tuple:](#a-114)

### Q: Cosa accade se oad_ready() -> dict: non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se oad_ready() -> dict: fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [oad_ready() -> dict:](#a-115)

### Q: Cosa accade se costruisce rotation e writer (per _sanitize_corpo) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Costruisce rotation e writer (per _sanitize_corpo) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Costruisce rotation e writer (per _sanitize_corpo)](#a-116)

### Q: Cosa accade se legge csv — deduplicazione per email non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Legge CSV — deduplicazione per email fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Legge CSV — deduplicazione per email](#a-117)

### Q: Cosa accade se always preserve sent/failed items; skip leads already done non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Always preserve sent/failed items; skip leads already done fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Always preserve sent/failed items; skip leads already done](#a-118)

### Q: Cosa accade se preserve all existing statuses (sent, ready, error) to avoid overwrites non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Preserve ALL existing statuses (sent, ready, error) to avoid overwrites fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Preserve ALL existing statuses (sent, ready, error) to avoid overwrites](#a-119)

### Q: Cosa accade se _flush(results: list): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _flush(results: list): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_flush(results: list):](#a-120)

### Q: Cosa accade se ─── multi-account round-robin ─────────────────────────────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── MULTI-ACCOUNT ROUND-ROBIN ─────────────────────────────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── MULTI-ACCOUNT ROUND-ROBIN ───────────────────────────────────────────────](#a-123)

### Q: Cosa accade se per ogni account gmail occorre una app password (non la password normale). non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Per ogni account Gmail occorre una App Password (NON la password normale). fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Per ogni account Gmail occorre una App Password (NON la password normale).](#a-124)

### Q: Cosa accade se come ottenerla: google account → sicurezza → verifica in due passaggi → app pass non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Come ottenerla: Google Account → Sicurezza → Verifica in due passaggi → App pass fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Come ottenerla: Google Account → Sicurezza → Verifica in due passaggi → App pass](#a-125)

### Q: Cosa accade se crea una app password con nome "mail" e copia le 16 lettere (es. "aaaa bbbb cccc non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Crea una App Password con nome "Mail" e copia le 16 lettere (es. "aaaa bbbb cccc fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Crea una App Password con nome "Mail" e copia le 16 lettere (es. "aaaa bbbb cccc](#a-126)

### Q: Cosa accade se sostituisci account2_email / account3_email con le email reali e le relative app non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Sostituisci ACCOUNT2_EMAIL / ACCOUNT3_EMAIL con le email reali e le relative App fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Sostituisci ACCOUNT2_EMAIL / ACCOUNT3_EMAIL con le email reali e le relative App](#a-127)

### Q: Cosa accade se solo account con email reale (esclude placeholder) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Solo account con email reale (esclude placeholder) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Solo account con email reale (esclude placeholder)](#a-128)

### Q: Cosa accade se deliverability: limite giornaliero per singola mailbox gmail. non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se DELIVERABILITY: limite giornaliero per singola mailbox Gmail. fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [DELIVERABILITY: limite giornaliero per singola mailbox Gmail.](#a-129)

### Q: Cosa accade se superare 50/giorno brucia la reputazione e causa "message blocked". non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Superare 50/giorno brucia la reputazione e causa "Message blocked". fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Superare 50/giorno brucia la reputazione e causa "Message blocked".](#a-130)

### Q: Cosa accade se per volumi maggiori: aggiungere più account gmail (round-robin orizzontale). non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Per volumi maggiori: aggiungere più account Gmail (round-robin orizzontale). fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Per volumi maggiori: aggiungere più account Gmail (round-robin orizzontale).](#a-131)

### Q: Cosa accade se ─── smtp ──────────────────────────────────────────────────────────────────── non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se ─── SMTP ──────────────────────────────────────────────────────────────────── fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [─── SMTP ────────────────────────────────────────────────────────────────────](#a-132)

### Q: Cosa accade se _invia(destinatario: str, oggetto: str, corpo: str, account_idx: int = 0) -> boo non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _invia(destinatario: str, oggetto: str, corpo: str, account_idx: int = 0) -> boo fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_invia(destinatario: str, oggetto: str, corpo: str, account_idx: int = 0) -> boo](#a-133)

### Q: Cosa accade se _flush(data: list): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se _flush(data: list): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [_flush(data: list):](#a-134)

### Q: Cosa accade se preview prime 3 non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Preview prime 3 fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Preview prime 3](#a-135)

### Q: Cosa accade se applica limite giornaliero non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Applica limite giornaliero fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Applica limite giornaliero](#a-136)

### Q: Cosa accade se wf-s1-concessionari.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-S1-CONCESSIONARI.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-S1-CONCESSIONARI.md](#a-027)

### Q: Cosa accade se 📱 variante a — lead caldi / già contattati (i 7 concessionari in lista) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 📱 Variante A — Lead Caldi / Già Contattati (I 7 Concessionari in lista) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [📱 Variante A — Lead Caldi / Già Contattati (I 7 Concessionari in lista)](#a-030)

### Q: Cosa accade se wf-s2-manuale.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-S2-MANUALE.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-S2-MANUALE.md](#a-036)

### Q: Cosa accade se wf-s3-s4-pagine-mentalita.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-S3-S4-PAGINE-MENTALITA.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-S3-S4-PAGINE-MENTALITA.md](#a-044)

### Q: Cosa accade se parte b — s4 mentalita.brutale (23→25/07) — hard rule non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se PARTE B — S4 mentalita.brutale (23→25/07) — HARD RULE fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [PARTE B — S4 mentalita.brutale (23→25/07) — HARD RULE](#a-049)

### Q: Cosa accade se wf-s5-youtube.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-S5-YOUTUBE.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-S5-YOUTUBE.md](#a-054)

### Q: Cosa accade se wf-s6-rebrand-promo.md non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se WF-S6-REBRAND-PROMO.md fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [WF-S6-REBRAND-PROMO.md](#a-061)

### Q: Cosa accade se 🤖 claude (esecuzione diretta, su comando — batch copy unico 21/07 sera) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 🤖 CLAUDE (esecuzione diretta, su comando — batch copy UNICO 21/07 sera) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [🤖 CLAUDE (esecuzione diretta, su comando — batch copy UNICO 21/07 sera)](#a-007)

### Q: Cosa accade se 3. argomentario obiezioni (ribaltamento con metodo andrei pascu) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3. Argomentario Obiezioni (Ribaltamento con Metodo Andrei Pascu) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3. Argomentario Obiezioni (Ribaltamento con Metodo Andrei Pascu)](#a-033)

### Q: Cosa accade se 3. setup tecnico (gael, 22/07) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 3. Setup tecnico (Gael, 22/07) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [3. Setup tecnico (Gael, 22/07)](#a-041)

### Q: Cosa accade se 📧 variante b — lead freddi da google maps (outreach email/linkedin) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 📧 Variante B — Lead Freddi da Google Maps (Outreach Email/LinkedIn) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [📧 Variante B — Lead Freddi da Google Maps (Outreach Email/LinkedIn)](#a-031)

### Q: Cosa accade se 4. sequenza outreach (a2, 3 email) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 4. Sequenza outreach (A2, 3 email) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [4. Sequenza outreach (A2, 3 email)](#a-065)

### Q: Cosa accade se fliki_youtube_test.py non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se fliki_youtube_test.py fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [fliki_youtube_test.py](#a-073)

### Q: Cosa accade se memory_manager.py non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se memory_manager.py fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [memory_manager.py](#a-075)

### Q: Cosa accade se lasciata per compatibilità con gli script che la chiamano. non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Lasciata per compatibilità con gli script che la chiamano. fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Lasciata per compatibilità con gli script che la chiamano.](#a-102)

### Q: Cosa accade se send_outreach_ready.py non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se send_outreach_ready.py fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [send_outreach_ready.py](#a-122)

### Q: Cosa accade se send_s1_whatsapp_auto.py non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se send_s1_whatsapp_auto.py fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [send_s1_whatsapp_auto.py](#a-137)

### Q: Cosa accade se regole di orchestrazione non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Regole di orchestrazione fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Regole di orchestrazione](#a-016)

### Q: Cosa accade se 4. regole di convivenza (con l'ecosistema v4) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 4. REGOLE DI CONVIVENZA (con l'ecosistema v4) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [4. REGOLE DI CONVIVENZA (con l'ecosistema v4)](#a-024)

### Q: Cosa accade se 2. script whatsapp in 3 messaggi + email (chiusura asincrona apsoc — score check non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2. Script WhatsApp in 3 messaggi + Email (Chiusura Asincrona APSOC — Score Check fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2. Script WhatsApp in 3 messaggi + Email (Chiusura Asincrona APSOC — Score Check](#a-029)

### Q: Cosa accade se 2-bis. script chiamata a freddo (cold call — formula cecchino apsoc, 60 secondi) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 2-bis. Script Chiamata a Freddo (Cold Call — Formula Cecchino APSOC, 60 secondi) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [2-bis. Script Chiamata a Freddo (Cold Call — Formula Cecchino APSOC, 60 secondi)](#a-032)

### Q: Cosa accade se landing — struttura (copy: cro-copy-architect apsoc, 21/07 sera) non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se Landing — struttura (copy: cro-copy-architect APSOC, 21/07 sera) fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [Landing — struttura (copy: cro-copy-architect APSOC, 21/07 sera)](#a-039)

### Q: Cosa accade se 6. regole non negoziabili non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se 6. Regole non negoziabili fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [6. Regole non negoziabili](#a-060)

### Q: Cosa accade se verify_apsoc(text): non viene eseguito a norma o fallisce in produzione?
**Risposta (Steel-manning P4)**: Se verify_apsoc(text): fallisce o non rispetta le soglie di validazione (es. APSOC < 92% o lock concorrenziale), il Conductor o lo script di errore intercetta l'eccezione, blocca il forward al cliente e innesca il fallback di notifica a Max per audit immediato.
- *Atomo di riferimento*: [verify_apsoc(text):](#a-138)
