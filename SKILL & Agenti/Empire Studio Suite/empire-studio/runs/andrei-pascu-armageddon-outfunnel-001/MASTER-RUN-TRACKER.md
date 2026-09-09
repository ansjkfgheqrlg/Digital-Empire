# MASTER RUN TRACKER — andrei-pascu-armageddon-outfunnel-001
## Corso a pagamento: "outFunnel" (dentro Armageddon Bundle, Andrei Pascu, andrei-copy.com)
**Run creato:** 2026-09-09 | **Pipeline:** Empire Studio Suite v2.0 (adattata a corso membership, non YouTube) — stessa famiglia di `andrei-pascu-cs2online-001`

---

## SCOPE (Max, 2026-09-09)

Max ha comprato l'**Armageddon Bundle** (199 €, 4 corsi: outFunnel, outHeadline, outEmail,
outViral 2) e ha ordinato l'ingestione totale: *"mangiarli, prendere tutta la formazione, tutta
la conoscenza, analizzare ogni singolo atomo, ogni singolo millimetro del corso, seguire tutte le
lezioni, tutto"* — partendo da **outFunnel**. Motivo dichiarato: migliorare il progetto, l'azienda,
i processi, gli ecosistemi, le infrastrutture AI (non solo studio del concorrente).

Ordine di lavoro: **outFunnel → outHeadline → outEmail → outViral 2** (i 4 corsi del bundle).
Questo tracker copre solo outFunnel; ogni corso avra' il proprio run (stessa convenzione).

**URL corso:** `https://www.andrei-copy.com/bjrkfv9` (slug offuscato, dietro l'area membri
Squarespace nativa — diverso da `cs2online`, che era su piattaforma tipo Podia/simile).
**Totale lezioni: 20**, in 4 sezioni (confermato via enumerazione DOM autenticata).

---

## SICUREZZA CREDENZIALI (stesso standard di `cs2online-001`, corretto in corsa)

- Credenziali fornite da Max in chat (email `max.infoproducer@gmail.com`).
- **Errore fatto e corretto nello stesso turno**: la password era stata scritta per un momento nel
  `.env` di root — rimossa subito dopo aver trovato questo tracker precedente. Regola vincolante:
  **password mai su file salvato nel repo**, solo variabile d'ambiente di sessione.
- Sessione autenticata (`storage_state.json` di Playwright) vive in scratchpad locale della sessione
  Claude Code corrente, MAI nel repo (nemmeno gitignorato — proprio fuori dall'albero del progetto).
  `%LOCALAPPDATA%\empire-studio\storage_state.json` (usato da `cs2online`) non e' scrivibile da
  questa sandbox — fallback accettato: scratchpad di sessione, re-login ad ogni nuova sessione
  Claude Code (stesso comportamento di fallback gia' previsto dal tracker `cs2online`).
- Script di login: `competitor/Andrei Pascu/site-study/scripts/login_member_area.py` (nel repo,
  nessun segreto dentro — legge solo `ANDREI_COPY_EMAIL`/`ANDREI_COPY_PASSWORD` da env var).

---

## DIFFERENZE STRUTTURALI vs cs2online (da non confondere)

- **Login**: qui e' un modal diretto sulla pagina (`/armageddon-dashboard`, bottone "Accedi" →
  campi `E-mail`/`Password` visibili, niente iframe). cs2online usava un iframe con
  `#login-email`/`#login-password`.
- **Ogni lezione ha gia' un "Riassunto lezione" ufficiale strutturato** scritto in pagina (non solo
  panoramica breve + bullet): definizioni, esempi, termini chiave — verificato su Lezione 1.
  Riduce il bisogno di trascrizione separata rispetto a cs2online.
- Video: stesso meccanismo, Vimeo privato via iframe (`player.vimeo.com/video/<id>`).

---

## STATO GLOBALE

| Sezione | Lezioni | Fatte | Pending |
|---|---|---|---|
| Sezione 1 - Le basi | 8 (L1-L8) | 8 | 0 |
| Sezione 2 - Esempi strategici | 3 (L9-L11) | 3 | 0 |
| Sezione 3 - Strategie avanzate | 5 (L12-L16) | 5 | 0 |
| Sezione 4 - Esempi di Funnel completi | 4 (L17-L20) | 4 | 0 |
| **TOTALE** | **20** | **20** | **0** |

**✅ CORSO outFunnel COMPLETO — 2026-09-09.** 20/20 lezioni: testo ufficiale catturato, tutte
classificate TEORIA (verificato lezione per lezione, non solo dal titolo), `lesson-analysis.md`
scritto per ognuna (114 knowledge atom totali), Memory Empire attivato per tutte e 20
(`.claude/skills/empire-studio/memory-empire/knowledge/outfunnel-lezione-01..20/`, schema a 4
file identico a cs2online), 1 pagina wiki di sintesi
(`second-brain-vault/wiki/sources/Source_OutFunnel_Corso_Completo.md`).

**Cattura testo grezzo: tutte e 20 le lezioni, fatta** (`scrape_batch.py`, 19/20 al primo giro,
lezione 20 recuperata con `domcontentloaded` invece di `networkidle`). **Classificazione: tutte
e 20 confermate TEORIA** per lettura integrale del "Riassunto lezione" ufficiale — corso di puro
framework/strategia, zero linguaggio da demo schermo in nessuna delle 20 (verifica extra fatta
sui titoli a rischio: 5, 17-20). Tentata verifica aggiuntiva via durata/frame-campione (yt-dlp)
ma bloccata da rate-limit/blocco TLS di Vimeo dopo la raffica di 20 richieste — non riprovata,
l'evidenza testuale e' gia' sufficiente per la classificazione.

**RIPRESA DA:** nulla su outFunnel — chiuso. Prossimo corso del bundle: **outHeadline**
(`/outheadlinedash-1` dalla dashboard). Stessa pipeline: `scrape_batch.py` adattato al nuovo slug,
classificazione teoria/pratica lezione per lezione (non assumere dal titolo), `lesson-analysis.md`,
`genera_memory_empire.py` adattato, 1 pagina wiki di sintesi. Poi outEmail, poi outViral 2.

---

## LISTA COMPLETA 20 LEZIONI (URL reali, verificati via DOM autenticato)

Tutti gli URL vanno prefissati con `https://www.andrei-copy.com/bjrkfv9/`.

### Sezione 1 - Le basi (8 lezioni)
| # | Titolo | Slug URL | Tipo (stimato da titolo) | Status |
|---|---|---|---|---|
| 1 | Cos'è un funnel | `lezione-1-cos-un-funnel-4pxk3` | TEORIA | pending |
| 2 | Livelli di consapevolezza | `lezione-2-livelli-di-consapevolezza-nxly7` | TEORIA | pending |
| 3 | Obiettivi che un funnel può avere | `lezione-3-obiettivi-che-un-funnel-puo-avere-9zlsg` | TEORIA | pending |
| 4 | Come creare un funnel | `lezione-4-come-creare-un-funnel-3erfw` | da verificare (potrebbe essere PRATICA) | pending |
| 5 | Funnel reali: la situazione interessante delle vere pubblicità | `lezione-5-funnel-reali-la-situazione-interessante-delle-vere-pubblicita-x8pza` | da verificare (probabile PRATICA — esempi reali) | pending |
| 6 | Tipi di funnel | `lezione-6-tipi-di-funnel-73ctz` | TEORIA | pending |
| 7 | Pezzi del puzzle | `lezione-7-pezzi-del-puzzle-yrf2p` | TEORIA | pending |
| 8 | Step di un funnel completo | `lezione-8-step-di-un-funnel-completo-jby8b` | TEORIA | pending |

### Sezione 2 - Esempi strategici (3 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 9 | Opzioni per il lead magnet | `lezione-9-opzioni-per-il-lead-magnet-49ryz` | TEORIA | pending |
| 10 | Tipi di sequenze automatiche e come fare follow up | `lezione-10-tipi-di-sequenze-automatiche-e-come-fare-follow-up-kb6gj` | TEORIA | pending |
| 11 | Opzioni per upsell/xell base | `lezione-11-opzioni-per-upsellxell-base-kwx9z` | TEORIA | pending |

### Sezione 3 - Strategie avanzate (5 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 12 | Considerazioni tra gli step del funnel | `lezione-12-considerazioni-tra-gli-step-del-funnel-fyh26` | TEORIA | pending |
| 13 | Quello che non misuri, non cresce: funnel troubleshooting | `lezione-13-quello-che-non-misuri-non-cresce-funnel-troubleshooting-p4lg8` | da verificare | pending |
| 14 | KPIs | `lezione-14-kpis-3jzth` | TEORIA | pending |
| 15 | Segmentazione Audience | `lezione-15-segmentazione-audience-9h4at` | TEORIA | pending |
| 16 | Come i funnel si evolvono col tempo | `lezione-16-come-i-funnel-si-evolvono-col-tempo-dhxde` | TEORIA | pending |

### Sezione 4 - Esempi di Funnel completi (4 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 17 | Funnel base: Lead Magnet Funnel | `lezione-17-funnel-base-lead-magnet-funnel-eypsa` | da verificare (probabile PRATICA — esempio completo) | pending |
| 18 | Funnel base: Sales Page Funnel | `lezione-18-funnel-base-sales-page-funnel-srwss` | da verificare (probabile PRATICA) | pending |
| 19 | High-price sales team Funnel | `lezione-19-highprice-sales-team-funnel-sb4tz` | da verificare (probabile PRATICA) | pending |
| 20 | Full funnel example | `lezione-20-full-funnel-example-kz4t6` | da verificare (probabile PRATICA — esempio completo) | pending |

**Nota sulla classificazione**: outFunnel è un corso di strategia/framework (non un tutorial
software passo-passo come CS2), quindi la maggioranza delle lezioni e' probabilmente TEORIA. Le
lezioni "Sezione 4 - Esempi di Funnel completi" e le lezioni con "esempi reali" nel titolo sono le
candidate piu' probabili a contenere screenshot/demo reali da trattare come PRATICA — da
confermare aprendo ogni video, non assumere dal titolo (stessa regola di cs2online).

---

## OUTPUT PER LEZIONE (stessa struttura di cs2online-001)

```
runs/andrei-pascu-armageddon-outfunnel-001/lessons/lezione-NN/
├── _page_raw.txt            (testo integrale della pagina, cattura grezza)
├── _scrape_meta.json        (url, vimeo-id, risorse esterne trovate)
├── ingest.json              (metadata: slug, url, vimeo-id, tipo teoria/pratica, risorse)
├── lesson-analysis.md       (panoramica ufficiale + riassunto ufficiale + knowledge atoms + [frame-by-frame SOLO se pratica])
├── resources/                (materiali scaricabili, se presenti)
└── frames/                  (SOLO lezioni pratiche — screenshot ogni ~2s del video)

memory-empire/knowledge/outfunnel-lezione-NN/   (stesso schema 4-file del run cs2online)
```

---

## SOP PER OGNI SESSIONE FUTURA

1. Leggi questo tracker, trova prossima lezione "pending".
2. Se manca la sessione: chiedi a Max email+password (mai cercarle salvate — non ci sono per
   scelta), imposta come env var, esegui `competitor/Andrei Pascu/site-study/scripts/login_member_area.py`.
3. `scrape_batch.py` per il testo grezzo (gia' fatto per tutte le 20, se non e' stato invalidato).
4. Apri `_page_raw.txt` → classifica TEORIA/PRATICA REALE (correggi la tabella se lo stimato era
   sbagliato) → se PRATICA, apri il video (frame reali, visione Claude) prima di scrivere l'analisi.
5. Scarica risorse esterne elencate in `_scrape_meta.json` (Google Drive, PDF, immagini).
6. Scrivi `lesson-analysis.md` con knowledge atoms (stesso standard P12 traceability di cs2online).
7. Attiva Memory Empire: `memory-empire/knowledge/outfunnel-lezione-NN/` (4 file), enrichment-report
   confronto con skill esistenti (in particolare `cro-copy-architect`, `cro`, `ab-testing`, `funnel`
   se esiste, `preventivo-auto`... — verificare quali skill dell'Impero trattano funnel/lead magnet).
8. Aggiorna wiki (`second-brain-vault/wiki/sources/Source_OutFunnel_Lezione_NN_*.md`).
9. Aggiorna questo tracker (status → DONE) + `company/Memory/STATO-EMPIRE.md` con percentuale reale.

---

## Connessioni
- `runs/andrei-pascu-cs2online-001/` — il run gemello, stessa famiglia di pipeline, precedente
  di riferimento per formato e regole di sicurezza
- `competitor/Andrei Pascu/site-study/` — lo studio landing/funnel/copy dello stesso ecosistema
  (pre-acquisto); questo run copre il POST-acquisto (contenuto del corso vero e proprio)
- `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` — PARTE XI cita gia' il meccanismo di consegna
  (Member Areas) di cui questo corso e' il contenuto
