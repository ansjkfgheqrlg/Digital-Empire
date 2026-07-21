# 🏛️ PIANO-ECOSISTEMA-AGENTI v4-MASTER — EMPIRE-OS (plan of record)
> 2026-07-21 · Esito dei cicli v2 (self-audit) → v3 (hardening) → v4 (optimization). **Sostituisce integralmente la v1.**
> Stato: guarito (10 findings chiusi), anti-fragile (5 scenari failure autogestiti), ottimizzato (43 ruoli, −4 vs v1, −40% rumore).
> In attesa di approvazione Max → poi costruzione F1..F6.

## 1. ORGANIGRAMMA FINALE

```
                     👑 MAX (umano: digest 1/giorno + veto su DECISION-REQ + PARKED)
                      ▲
        ⚔️ COMANDANTI (4) — quorum 2/3 se EC AWOL>24h · chain EC→REV→BUILD
        ┌─────────────┬───────────────┬────────────────┬──────────────┐
   EMPIRE-COMMANDER  REVENUE-CMD    BUILD-CMD         TRUTH-CMD
   (settimana vince) (ogni flusso→€)(tutto il build)  (verità+memoria)
        │              │              │                  │
        │        🎖️ DIRIGENTI (7)    │                  │
        │  revenue-ops-dir · forge-dir · content-dir · youtube-dir
        │  acquisition-dir · memory-dir · strategy-dir
        │              │              │                  │
        │        🛠️ OPERATIVI (17 in 7 team, backup+3-deep sui critici)
        │                                                     │
        └───────────────┬─────────────────────────┬──────────┘
               🛡️ VERIFICATORI (5, casta autonoma: veto NON revocabile.
                  memory-auditor→EC, audita anche TRUTH-CMD)
               ⚖️ REGOLATORI (6: secret·anti-stub·swarm-quota·scope·cadence·
                  constitution — solo RULE-WARN/BLOCK, quorum×2 su i BLOCK)
        👁️ OSSERVATORI (4): silent-observer · customer-simulator · devil-advocate · market-watcher
```

## 2. MANDATI COMANDANTI (finali)
| Cmd | KPI | Può | Non può |
|---|---|---|---|
| EMPIRE-COMMANDER | € incassati | override su dirigenti, arbitrato matrice P4 | cambiare regole; bloccare i verificatori |
| REVENUE-CMD | €/h ecosistema | priorità coda S1>S2>S6>S5, veto su task €/h<0 | spendere >50€ senza Max; sconti fuori termini |
| BUILD-CMD | % DoD rispettate 1° colpo | code-freeze, rifiuto build fuori DoD | superare DoD senza decisione registrata |
| TRUTH-CMD | % task con CP; violazioni=0 | blocco chiusure non tracciate | riscrivere/alterare atomi di memoria (solo memory-keeper scrive, lui certifica) |

## 3. COMMAND BOARD — specifica finale (`09-BOARD/` + `board_router.py`)
- **Tipi:** HANDOFF · REPORT · REQUEST · BLOCK · ALERT · DECISION-REQ · RULE-WARN · RULE-BLOCK · OBS-NOTE · HUMAN-TASK · OVERRIDE-REQ · TIP · RULE-NOTE · MUTATION-PROP (gli ultimi 3: solo dalla Performance Cell, vedi WF-PERF-LOOP)
- **Idempotenza:** `MSG-<data>-<from>-<hash(payload)>` → replay senza duplicati
- **Routing:** p2p tra operativi con `cc: dirigente`; cross-casta via comandanti; verso Max SOLO digest (HUMAN-TASK aggregato, 1/giorno) o P0
- **Quota:** 30 msg/giorno ecosistema (P0 esentati) · shed: P3→digest, P2 hold 4h
- **Stati:** open→acked→closed | escalated | rejected · SLA: P0 1h · P1 4h · P2 EOD
- **Degrado:** board down → `09-BOARD/emergency/` (flat files, stesso schema) → replay deduplicato
- **Router duties extra:** attiva DEC scadute→ATTIVA · heartbeat cast AWOL dopo 2 sync · riassegna task al backup → calcola KPI TTD/FPR/ESC per agente → compone EMPIRE-DIGEST e digest-Max · **a ogni azione chiusa scrive il PERF record (T1 del WF-PERF-LOOP, fuori quota msg)**

## 4. TEAM FINALI (operativi con naming a ruolo; backup · catena se critica)
| Team | Dirigente | Operativi | Verificatore (dominio disgiunto) |
|---|---|---|---|
| 💰 Revenue | revenue-ops-dir | `pricing-ops` · `closer-ops` ⚡catena: pricing→closer→dir | funnel-verifier (contratti/pagamenti) |
| 🔨 Forge | forge-dir | `forge-builder` ⚡→`funnel-engineer`→dir · `site-ops` · `carousel-ops` · `casestudy-ops` | funnel-verifier (web/checkout/factory) |
| ✍️ Content | content-dir | `forge-invoker-ops` · `copy-ops` | content-verifier (copy/carousel/case-study) |
| 🎬 YouTube | youtube-dir | `yt-ingester` · `yt-render-ops` · `yt-publish-ops` · `yt-analytics-ops` · `yt-scout-ops` | video-verifier |
| 📡 Acquisition | acquisition-dir | `scrape-ops` · `outreach-ops` · `social-ops` | outreach-verifier (campagne/social) |
| 🧠 Memory | memory-dir | `memory-keeper` (backup: memory-dir stesso) | memory-auditor (→EC, audita anche TRUTH-CMD) |
| ⚡ Performance Cell | memory-dir (sponsor TRUTH-CMD) | `perf-collector` · `perf-analyst` · `feedback-dispatcher` (backup incrociati) | nessun gate: migliora, non blocca (WF-PERF-LOOP) |
| 🧭 Strategy | strategy-dir | `planner-ops` · `retro-ops` | memory-auditor (Art.2 aderenza piani) |

## 5. SKILL → OWNER (14 motori, zero orfani; skill=nome motore, agente=ruolo)
content-forge2.0→Content(forge-invoker-ops) · master-build-architecture→Strategy(planner-ops) · ruflo→Memory(memory-keeper) · carousel-factory→Forge(carousel-ops) · site-*/empire-premium-style→Forge(site-ops) · case-study-forge→Forge(casestudy-ops) · beast-preventivi+pricing→Revenue(pricing-ops) · cro-copy-architect→Content(copy-ops) · A1-scrape→Acquisition(scrape-ops) · A2-outreach→Acquisition(outreach-ops) · PreventivoForge-factory(/nuovo-concessionario+kill-switch)→Forge(preventa-factory-ops=forge-builder) · Fliki+YouTubeDataAPI→YouTube(yt-render/publish-ops) · MetaGraph/Buffer→Acquisition(social-ops) · Stripe/Gumroad→Forge(funnel-engineer)

## 6. WORKFLOW → CREW (finale)
| WF | Cmd sponsor | Dir | Crew | Verificatore | Regolatori | Observer |
|---|---|---|---|---|---|---|
| WF-S1 | REVENUE-CMD | revenue-ops-dir | closer-ops, pricing-ops | funnel-verifier | scope, cadence | customer-simulator |
| WF-S2 | BUILD-CMD | forge-dir | funnel-engineer, copy-ops, site-ops | funnel-verifier | secret, scope | customer-simulator |
| WF-S3/S4 | REVENUE-CMD | acquisition-dir | social-ops, carousel-ops | outreach-verifier | constitution (S4 solo 100% auto), cadence | silent-observer |
| WF-S5 | BUILD-CMD | youtube-dir | yt-* (5) | video-verifier | secret, anti-stub | market-watcher |
| WF-S6 | REVENUE-CMD | forge-dir | casestudy-ops, site-ops, scrape-ops, outreach-ops | funnel-verifier | scope, constitution | devil-advocate |
| WF-MEM-* | TRUTH-CMD | memory-dir | memory-keeper | memory-auditor | tutti | silent-observer |
| WF-MASTER | EMPIRE-COMMANDER | — | — | — | tutti | tutti |
| WF-PERF-LOOP | TRUTH-CMD | memory-dir | perf-collector, perf-analyst, feedback-dispatcher | (trasversale: gira dopo OGNI azione di TUTTI i WF) | cadence, constitution | silent-observer |

## 7. SELF-HEALING RUNTIME (dalle patch H1..H5, ora legge)
1. **Heartbeat+AWOL**: 2 sync mancati → AWOL → router riassegna al backup; ruoli critici: catena 3-deep
2. **Regolatori**: BLOCK persistente = co-firma 2° regolatore entro 1h; 3 falsi positivi/h → FROZEN + arbitro constitution-guard; appello OVERRIDE-REQ con timer 4h su P0
3. **Board**: idempotenza + emergency-mode + replay deduplicato
4. **Comando**: matrice P4 (€/h) → timer 4h → EC → quorum 3/4 → Max; **default = esegui il piano com'è** ("fermo il dibattito, mai il flusso")
5. **Max assente**: default ATTIVI, ma spend>50€ / fuori-standard / costituzione → **PARKED** ("il sistema procede, non firma")
6. **Performance loop**: KPI TTD/FPR/ESC per agente → pairing repair, mutation proposal, promotion ladder, pruning anti-accumulo
7. **Mutation governance:** ogni agente può proporre il cambio del proprio prompt; approva il comandante di casta; i cambi strutturali passano dal COUNCIL con log pubblico
8. **P-LOOP (performance loop confermato):** ogni azione chiusa → PERF record (T1) → analisi 5D (T2) → pattern/feedback (T3-T4) → **conferma alla performance successiva (T5)**. Un miglioramento esiste solo quando T5 lo conferma; altrimenti è solo un suggerimento (spec: `03-WORKFLOWS/WF-PERF-LOOP.md`, agenti: `04-AGENTS/PERFORMANCE-CELL.md`)

## 8. COSTRUZIONE (fasi — invariate dalla v1, ora specifica v4)
| F | Output | Contenuto v4 |
|---|---|---|
| F1 | `08-ECOSYSTEM/command/` | 4 comandanti 7-file con mandati §2 + succession chain |
| F2 | `09-BOARD/` + `board_router.py` | spec §3 completa (idempotenza, shed, digest, KPI-calc, AWOL) |
| F3 | `08-ECOSYSTEM/departments/` | 7 dirigenti 7-file + manifest operativi §4 |
| F4 | `08-ECOSYSTEM/verification/` + `regulators/` | 5 verificatori (domini §4) + 6 regolatori (quorum, circuit-breaker, appelli) + `constitution.md` |
| F5 | `08-ECOSYSTEM/runtime/` | loop: board → crew → WF advance (file-based; ruflo quando disponibile) |
| F6 | Self-healing ON | heartbeat, audit live settimanale, primo COUNCIL → primo HEAL reale |

## 9. VERITÀ (Art.2)
La v4 è **progetto validato a simulazione**, non a runtime: la prova reale arriva con F6 (primo self-audit su dati veri di board). Ogni azione dei cicli ha rollback atomico (diff riga-per-riga nei documenti di ciclo). Nulla di quanto esiste nel workshop ESTATE-2026 viene buttato: i WF, le skill, i planning P1–P7 restano — l'ecosistema è lo strato vivo che li fa correre.

---
⛓️ Trace P12: `PIANO-ECOSISTEMA-v4#estate-2026` · serie: v1 → CICLO-v2 → CICLO-v3 → CICLO-v4 → v4-MASTER · memory attesa: HEAL-R1..R10, H1..H5, O1..O6
