# Mentalità Brutale Social Operating System (MB-OS)

Sistema API-first, memory-first e gate-first per portare `@mentalita.brutale` da asset sparsi a operatività automatizzata:

```text
Intelligence → Strategy → Production → QA → Scheduler → Meta Publish → Insights → Learning → FORGE
```

## Stato reale

| Capability | Stato |
|---|---|
| Architettura e reparti | ✅ costruiti |
| Runtime dry-run + coda + idempotenza | ✅ costruito/testabile |
| Graph API publish/insights | ✅ implementato, non chiamato senza token |
| Segreti hard-coded nel vecchio publisher | ✅ rimossi dai file correnti; **password da ruotare** |
| OAuth Meta dell'account | ⬜ da completare dall'owner |
| Staging HTTPS pubblico | ⬜ da configurare |
| Canary live | ⬜ non eseguito |
| Full auto | ⬜ target `CERTIFIED_AUTO`; oggi `SHADOW` |
| Reverse engineering video | ⚠️ sorgente video non presente nel checkout |

La distinzione è intenzionale: “implementato” non significa “certificato live”.

## Quick start

```bash
cd "Page IG - Mentalità Brutale/OPERATING-SYSTEM"
python runtime/scripts/mbctl.py init
python runtime/scripts/mbctl.py doctor
python runtime/scripts/mbctl.py validate --manifest examples/carousel.example.json
python runtime/scripts/mbctl.py plan --manifest examples/carousel.example.json
python -m unittest discover runtime/tests -v
```

## Navigazione

- `MASTER-KNOWLEDGE-DOCUMENT.md` — conoscenza forgiata, brand, strategia, failure modes.
- `00-SPEC-PREMORTEM.md` — DONE WHEN e rischi del ciclo.
- `architecture/01-BLUEPRINT.md` — workflow business e architettura tecnica.
- `architecture/02-AUTHORIZATION-META.md` — autorizzazione Meta v25.0.
- `architecture/03-DEPARTMENTS-ACTIVATION.md` — reparti Social Empire e RACI.
- `architecture/04-STRATEGY-28-DAYS.md` — 28 post/28 giorni, test bilanciato.
- `architecture/05-VIDEO-FORENSICS.md` — come vedere davvero i video senza inventare.
- `architecture/06-RUNBOOK.md` — setup, OAuth, canary, certification, incidenti.
- `config/` — brand-kit, policy, quality gates, esperimento.
- `examples/` — manifest completi.
- `runtime/mb_os/` — client Graph API, staging, gate, scheduler, memoria, analytics.
- `memory/` — stato/ripresa locale del progetto.

## Contratto di sicurezza

- dry-run è il default;
- niente password/token nel codice;
- `.env` locale è ignorato;
- live richiede flag env + mode + kill switch + gate + token + quota;
- scheduler auto richiede `CERTIFIED_AUTO`;
- content hash impedisce doppio publish;
- `pause` ferma immediatamente side effect futuri;
- browser automation legacy resta fallback e non viene considerata certificata.

## Comandi

```text
init                              inizializza SQLite e controlli
 doctor [--online]                 readiness statica/Meta
 auth-url                          genera URL OAuth + CSRF state
 exchange-code --code ...          short→long-lived token
 refresh-token                     rinnova long-lived token
 validate --manifest FILE          esegue gate
 plan --manifest FILE              piano dry-run senza rete
 enqueue --manifest FILE           coda idempotente
 run --manifest FILE               dry-run
 run --manifest FILE --live ...    canary/live con guard
 run-due [--live]                  scheduler
 pause/resume/status               kill switch e stato
 certify --evidence FILE           abilita CERTIFIED_AUTO
 collect/report                    Insights e reporting
```

Per i dettagli live usare esclusivamente `architecture/06-RUNBOOK.md`.
