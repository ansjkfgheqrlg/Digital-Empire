# 🏛️ PIANO-ECOSISTEMA-AGENTI — v1 (piano iniziale)
> Codename: **EMPIRE-OS** · 2026-07-21 · Status: PROPOSTA — da approvare prima della costruzione (fasi F1–F6)
> Diagnosi: il workshop ESTATE-2026 è una base solida di **file organizzati per categoria**. Non è ancora un **organismo funzionante**: manca gerarchia con autorità, comunicazione strutturata tra agenti (command board), mappatura exhaustiva skill→team e workflow→crew. Questo piano disegna quell'organismo.
> Regola anti-gonfiore (vincolante per i cicli v2/v3/v4): **ogni miglioramento deve guarire, non aggiungere** — per ogni elemento introdotto, uno va semplificato o rimosso.

---

## 0. L'obiettivo, come l'ho capito (checkpoint di comprensione)

| Cosa c'è ora (base) | Cosa deve diventare (organismo) |
|---|---|
| Cartelle con documenti | **Casta gerarchica** con autorità e mandati |
| Agenti = file di istruzioni isolati | Agenti che **si parlano** via command board con contratti |
| Skill elencate in un registry | Ogni skill ha un **team proprietario** che la opera |
| Workflow descritti | Ogni workflow ha una **crew assegnata** (operativi+verificatori+regolatori) |
| Controllo implicito | Verificatori indipendenti, regolatori che bloccano, osservatori esterni |
| Statico | **Self-healing**: il sistema diagnostica, guarisce e ottimizza sé stesso |

---

## 1. LE 6 CASTE (gerarchia con autorità)

```
                        👑 MAX — umano, veto finale su tutto
                          ▲  (lo raggiungi SOLO via DECISION-REQ con default+veto)
        ┌─────────────────┴─────────────────────────────┐
        │  ⚔️ CASTA 1 — COMANDANTI (autorità strategica) │
        │  EMPIRE-COMMANDER (supremo)                    │
        │  REVENUE-CMD · BUILD-CMD · TRUTH-CMD           │
        └───────┬──────────────────────────┬────────────┘
                │                          │
        ┌───────┴───────────┐     ┌────────┴───────────────────────┐
        │ 🎖️ CASTA 2 — DIRIGENTI │ 🛡️ CASTA 4 — VERIFICATORI      │
        │ (7 dept, missioni) │     │ (indipendenti: rispondono a   │
        │                    │     │  TRUTH-CMD, non al dirigente)│
        │ 🛠️ CASTA 3 — OPERATIVI│ ⚖️ CASTA 5 — REGOLATORI         │
        │ (team specialisti) │     │ (solo regole: micro-input     │
        │                    │     │  RULE-WARN / RULE-BLOCK)      │
        └────────────────────┘     └───────────────────────────────┘
                 👁️ CASTA 6 — OSSERVATORI ESTERNI (laterale, guarda tutto da fuori)
                 silent-observer · customer-simulator · devil-advocate · market-watcher
```

### Casta 1 — COMANDANTI (4, non di più: span di controllo pulito)
| Comandante | Mandato | Autorità | KPI proprio |
|---|---|---|---|
| **EMPIRE-COMMANDER** | La settimana vince. Esegue il MASTER PLAN (P7), orchestra gli altri comandanti, unico interfaccia verso Max | Override su qualsiasi dirigente; non può cambiare le regole (solo regolatori+Max) | € incassati |
| **REVENUE-CMD** | Ogni flusso porta a € | Prioritizza S1>S2>S6>S5; veto su attività a €/h negativo | €/h dell'ecosistema |
| **BUILD-CMD** (= chief-forge promosso) | Tutto ciò che viene costruito passa da qui | Code-freeze; rifiuto build fuori DoD | DoD rispettate, tempo di consegna |
| **TRUTH-CMD** (nuovo) | Verità, memoria, verifiche: niente esiste se non è tracciato (P12) | Blocca chiusure senza checkpoint; custode del Mandato Art.2 | % task con CP, zero violazioni |

> Norman-comandanti: un RULE-BLOCK di un regolatore verso un comandante scala **direttamente a Max**.

### Casta 2 — DIRIGENTI (7 department lead)
Traducono mandati in missioni, assegnano ai team, riportano ai comandanti via board. Non verificano il proprio lavoro (separazione: lo fanno i verificatori).
`revenue-ops-dir` · `forge-dir` (= chief-forge operativo sotto BUILD-CMD) · `content-dir` · `youtube-dir` · `acquisition-dir` (nuovo: A1/A2 + pagine social) · `memory-dir` (= memory-architect) · `strategy-dir`

### Casta 3 — OPERATIVI (specialisti nei team)
Fanno il lavoro. Regole: 2 tentativi autonomi → escalation al dirigente (mai soffrire in silenzio). Ogni consegna = handoff contract verso il verificatore.

### Casta 4 — VERIFICATORI (indipendenza garantita)
Verificano l'**output** contro la DoD **prima** che avanzi. Strutturalmente NON possono essere assegnati dallo stesso dirigente che ha prodotto il lavoro (sempre cross-dept).
`funnel-verifier` · `content-verifier` · `video-verifier` · `outreach-verifier` · `memory-auditor` · `delivery-verifier`

### Casta 5 — REGOLATORI (solo regole, solo micro-input)
Non guardano la qualità: guardano la **costituzione** (regole P7, ADR). Emittenti di soli due tipi di messaggio: `RULE-WARN` (correggi entro 1h) e `RULE-BLOCK` (fermo immediato + scala al comandante).
| Regolatore | Regola custodita |
|---|---|
| `secret-guard` | chiavi solo in .env; mai nei prompt/file |
| `anti-stub-guard` | zero stub, zero "TODO" spacciati per fatto |
| `swarm-quota-guard` | 1 swarm pesante alla volta (CP-20260711-002) |
| `scope-guard` | DoD congelate, niente superamento senza decisione |
| `cadence-guard` | EOD h19:00, code-freeze ven h20:00, gate puntualli |
| `constitution-guard` | ADR-EST-001..006, condizioni di Max (S4 solo se 100% auto) |

### Casta 6 — OSSERVATORI ESTERNI (laterali, prospettive esterne)
Non comandano nessuno: **guardano e scrivono sulla board** (canale OBS-FEED). Ogni settimana la loro sintesi alimenta il ciclo di miglioramento.
- `silent-observer`: drift — il sistema sta eseguendo il piano o sta divagando?
- `customer-simulator`: valuta ogni output come il concessionario/cliente finale lo vedrebbe
- `devil-advocate`: attacca le assunzioni ("perché credete che i 7 siano caldi DAVVERO?")
- `market-watcher`: competitor/prezzi esterni che cambiano le carte in tavola

---

## 2. I TEAM (unità operativa standard)

Ogni team = **1 dirigente + 2–5 operativi + 1 verificatore assegnato (cross) + regolatori trasversali**. Mai un agente solo: ogni ruolo operativo ha un **backup dichiarato** (base del self-healing: nessun single point of failure).

| Team | Dirigente | Operativi (principale · backup) | Verificatore cross |
|---|---|---|---|
| 💰 Revenue Team | revenue-ops-dir | pricing-cell · closer-a8 | delivery-verifier |
| 🔨 Forge Team | forge-dir | forge-builder · funnel-engineer · carousel-ops · case-study-forge | funnel-verifier |
| ✍️ Content Team | content-dir | content-forge-invoker · cro-copy-architect | content-verifier |
| 🎬 YouTube Team | youtube-dir | yt-ingester · yt-fliki-renderer · yt-seo-publisher · yt-analyzer · yt-scout | video-verifier |
| 📡 Acquisition Team | acquisition-dir | A1-scraper · A2-outreach · social-ops | outreach-verifier |
| 🧠 Memory Team | memory-dir | checkpoint-manager · indexer | memory-auditor |
| 🧭 Strategy Cell | strategy-dir | planner · retro-analyst | devil-advocate (observer) |

---

## 3. LA COMMAND BOARD (come si parlano) — `09-BOARD/`

Unico canale ufficiale. **Divieto di comunicazioni fuori board** (niente accordi "a voce": se non è nella board, non esiste — stessa legge della memoria).

```yaml
# Message schema (09-BOARD/messages/MSG-YYYYMMDD-NNN.yaml)
id: MSG-20260721-001
from: forge-dir            # agente, team, o SYSTEM
to: funnel-verifier        # agente | team | ALL | max
type: HANDOFF|REPORT|REQUEST|BLOCK|ALERT|DECISION-REQ|RULE-WARN|RULE-BLOCK|OBS-NOTE
ref: [WF-S2, CP-045]       # sempre ancorato a memoria (P12)
priority: P0..P3
payload: {artefatto: path, dod_check: bool, note: "..."}
status: open|acked|closed|escalated
thread: MSG-...-parent
```

**Tipi e chi li usa:**
- `HANDOFF` operativo→verificatore (con output contract) · `REPORT` dirigente→comandante · `REQUEST` tra pari (via dirigente se cross-team) · `BLOCK/ALERT` verificatori · `RULE-WARN/RULE-BLOCK` solo regolatori · `DECISION-REQ` verso Max (default+veto obbligatori) · `OBS-NOTE` solo osservatori (canale OBS-FEED)

**Escalation chain:** operativo (tentativo×2) → dirigente → comandante → Max. Ogni salto = status `escalated` + motivo nella payload. SLA: P0 ack ≤1h, P1 ≤4h, P2 EOD.

**Ritmi:** BOARD-SYNC h19:00 (ogni dirigente posta REPORT giornaliero, WF-MEM-EOD lo raccoglie) · COUNCIL domenicale (comandanti + osservatori → alimenta RETRO e il ciclo self-healing).

---

## 4. MAPPA COMPLETA: ogni skill → team proprietario

> Zero skill orfane: ogni motore ha UN owner operativo, UN backup, e UN verificatore per i suoi output.

| Skill / Motore | Team owner | Operativo primario | Backup | Verificatore |
|---|---|---|---|---|
| `content-forge2.0` (/forge) | Content | content-forge-invoker | cro-copy-architect | content-verifier |
| `master-build-architecture` | Strategy | planner | strategy-dir | devil-advocate |
| `ruflo` | Memory (L1) | checkpoint-manager | memory-architect | memory-auditor |
| `carousel-factory` | Forge | carousel-ops | forge-builder | content-verifier |
| `site-* (empire-premium-style)` | Forge | funnel-engineer | forge-builder | funnel-verifier |
| `case-study-forge` | Forge | case-study-forge | cro-copy-architect | delivery-verifier |
| `beast-preventivi / pricing` | Revenue | pricing-cell | closer-a8 | delivery-verifier |
| `cro-copy-architect (APSOC)` | Content | cro-copy-architect | content-forge-invoker | content-verifier |
| `A1-scrape / A2-outreach` | Acquisition | A1/A2 ops | social-ops | outreach-verifier |
| `PreventivoForge factory (/nuovo-concessionario, kill-switch)` | Forge | forge-builder | funnel-engineer | delivery-verifier |
| `Fliki API / YouTube Data API` | YouTube | yt-fliki-renderer · yt-seo-publisher | yt-ingester | video-verifier |
| `Meta Graph / Buffer` | Acquisition | social-ops | A2-outreach | outreach-verifier |
| `Stripe / Gumroad` | Forge | funnel-engineer | forge-dir | funnel-verifier |
| `memory_manager.py` | Memory | indexer | checkpoint-manager | memory-auditor |

## 5. MAPPA COMPLETA: ogni workflow → crew assegnata

| WF | Comandante sponsor | Dirigente | Crew operativa | Verificatore | Regolatori attivi | Observer |
|---|---|---|---|---|---|---|
| WF-S1 Concessionari | REVENUE-CMD | revenue-ops-dir | closer-a8, pricing-cell | delivery-verifier | scope, cadence | customer-simulator |
| WF-S2 Manuale | BUILD-CMD | forge-dir | funnel-engineer, cro-copy-architect | funnel-verifier | scope, secret | customer-simulator |
| WF-S3/S4 Pagine | REVENUE-CMD | acquisition-dir | social-ops, carousel-ops | outreach-verifier | constitution (S4 100% auto), cadence | silent-observer |
| WF-S5 YouTube | BUILD-CMD | youtube-dir | yt-* (5) | video-verifier | secret (Fliki), anti-stub | market-watcher |
| WF-S6 Rebrand | REVENUE-CMD | forge-dir | case-study-forge, funnel-engineer, A1/A2 | delivery-verifier | scope, constitution | devil-advocate |
| WF-MEM-EOD/RETRO | TRUTH-CMD | memory-dir | checkpoint-mgr, indexer | memory-auditor | tutti i 6 | silent-observer |
| WF-MASTER | EMPIRE-COMMANDER | — (coordina) | — | — | tutti | tutti |

---

## 6. MANDATI (forma canonica — uno per comandante/dirigente)

```yaml
agent: REVENUE-CMD
casta: comandante
mission: "nessun flusso senza path a € misurabile"
puo: [prioritizzare coda swarm, porre veto su task €/h<0, richiedere DECISION-REQ]
non_puo: [cambiare regole, chiudere un gate senza verificatore, parlare a Max senza board]
riporta_a: EMPIRE-COMMANDER · kpi: euro_incassati, euro_per_ora
backup: EMPIRE-COMMANDER   # self-healing: successione dichiarata
```

## 7. SELF-HEALING ENGINE (il cuore — progettato ora, attivato in F6)

**A. Self-audit strutturale (settimanale, nel COUNCIL):** l'ecosistema legge la board dei 7 giorni e produce diagnosi propria: colli di bottiglia, canali morti (mai usati), ruoli ridondanti, span of control rotti, skill senza traffico. Output: `HEAL-PLAN` a firma EMPIRE-COMMANDER.

**B. Self-healing runtime:**
- Agente fallisce 2× → **backup** prende il task (già dichiarato per ogni ruolo)
- Fallimento 3× sullo stesso task → **decomposizione automatica** del task + redesign proposto a BUILD-CMD
- Regolatore rileva violazione → RULE-WARN; recidivo → RULE-BLOCK + **mutation proposal** del system-prompt dell'agente colpevole
- Task marcio (bloccato >24h) → TRUTH-CMD lo riesuma in EOD-SYNC davanti a tutti

**C. Self-optimization (performance):** ogni agente ha 3 KPI propri (velocità consegna · % verifica passata al primo colpo · carico escalation). Il ReasoningBank decide: **promozione** (operativo→backup-dirigente), **affiancamento** (sotto 50% first-pass → partner repair), **pruning** (ruolo senza traffico 2 settimane → assorbito, mai accumulo).

**D. Mutation governance:** gli agenti possono proporre modifiche al proprio prompt/playbook (`update-proposer`), ma approva solo il comandante di casta; gli observers propongono mutazioni strutturali al COUNCIL.

---

## 8. PROTOCOLLO DEI 3 CICLI DI MIGLIORAMENTO (v2 → v4) — NON additivo

| Ciclo | Natura | Domanda guida | Output | Divieto |
|---|---|---|---|---|
| **v2 — SELF-AUDIT** | critica di sé | "Dove la v1 è ridondante/contradittoria/fragile?" | HEAL-PLAN: rimpasti, fusioni, rimozioni | vietato aggiungere agenti |
| **v3 — SELF-HEALING HARDENING** | stress-test | 5 scenari di failure simulati (agente morto, regolatore in loop, board intasata, comando in conflitto, Max assente): la rete deve auto-guarire | topologia resa anti-fragile (successioni, circuit-breaker, quorum) | vietato nuovo tooling |
| **v4 — SELF-OPTIMIZATION** | performance | KPI agente-by-agente: tagliare il lento, premiare il veloce, semplificare | topologia finale dimagrante + promotion paths | vietato aumentare il numero di messaggi/board-overhead |

Ogni ciclo produce: piano revisionato (full-replace, mai append) + atomi `HEAL-*` in memoria + diff-motivation (perché ogni cambio).

## 9. COSTRUZIONE (dopo approvazione v1 — fasi)

| Fase | Costruisce | Output fisico |
|---|---|---|
| F1 | Comando + mandati | `08-ECOSYSTEM/command/` (4 comandanti 7-file) |
| F2 | **Command Board runtime** | `09-BOARD/` + `board_router.py` (post/ack/route/escalate, anti-spam, SLA timer) |
| F3 | Dirigenti + team | 7 dirigenti 7-file + manifest operativi con backup |
| F4 | Verificatori + regolatori | `verification/` + `regulators/` con constitution.md |
| F5 | Loop runtime | orchestratore che legge board → attiva crew → avanza WF (integra ruflo se disponibile) |
| F6 | Self-healing ON | primo self-audit live + attivazione ciclo v2 |

## 10. DECISIONI APERTE PER MAX (30 secondi l'una)
- **DEC-EST-005**: numero comandanti → default **4** (Empire/Revenue/Build/Truth). Veto 48h.
- **DEC-EST-006**: i regolatori possono bloccare un comandante? → default **SÌ, ma scala a Max**. Veto 48h.
- **DEC-EST-007**: budget messaggi board (anti-rumore) → default **max 30 msg/giorno ecosistema**. Veto 48h.

---
⛓️ Trace P12: `PIANO-ECOSISTEMA-v1#estate-2026` · input: direttiva Max 21/07 · base: ESTATE-WORKSHOP (build completata CP-003) · metodo cicli: self-healing (non additivo)
