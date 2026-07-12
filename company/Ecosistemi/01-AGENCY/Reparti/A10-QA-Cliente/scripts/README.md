---
Type: TOOL
Status: Experimental
Tags: #scripts #agency #qa #automazione #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# scripts/ — A10 QA-Cliente

> Automazioni **di supporto all'audit**. Nessuno script di A10 modifica un artefatto di delivery:
> gli script osservano, campionano, contano (R1). Se uno script è tentato di riparare, è il progetto
> dello script a essere sbagliato.

---

## Stato

Cartella predisposta. Nessuno script implementato: il reparto parte in modalità manuale-assistita
(gli agenti eseguono i check con le skill). Gli script si scrivono **dopo** aver visto 3-5 review
reali — automatizzare un check che non hai ancora eseguito a mano è come ottimizzare un collo di
bottiglia che non hai misurato.

---

## Automazioni previste

| Script | Scopo | Owner | Priorità |
|---|---|---|---|
| `scan-de-dependencies.py` | Grep del runtime cliente per credenziali / endpoint / path / cron di DE → alimenta G2 | AG-A10-REVIEW | Alta |
| `check-brand-injection.py` | Campiona gli output della run reale e confronta i campi col `brand_kit` atteso → alimenta G3 | AG-A10-BRAND | Alta |
| `handover-checklist.py` | Verifica presenza + leggibilità delle voci del pacchetto (README, codice, credenziali, licenza) → alimenta G4 | AG-A10-HANDOVER | Media |
| `qa-timer.py` | Calcola il **tempo QA** (`ts_verdetto − ts_handoff_in`) per ogni review → alimenta i KPI | AG-A10-COORD | Media |
| `defect-rollup.py` | Aggrega i difetti per categoria/severità/step e conta le occorrenze → base del report mensile | AG-A10-LEARN | Media |
| `escaped-defects.py` | Incrocia i ticket 90gg di `agency/a4/support` con `agency/a10/defects` → difetti **sfuggiti al gate** | AG-A10-LEARN | Alta |

---

## Vincoli per ogni script di questo reparto

1. **Read-only sugli artefatti auditati.** Uno script A10 non ha mai permessi di scrittura sul
   repo del cliente né su `agency/a4/*`. Legge, campiona, conta (R1).
2. **Scrive solo in `agency/a10/*`.** Nessun altro namespace, mai (R8).
3. **Niente PII, niente segreti nell'output.** Gli script emettono riferimenti e conteggi,
   non contenuti (R6). Un dump di output cliente in un log è un incidente.
4. **Nessuna metrica derivata senza fonte.** Ogni numero prodotto porta con sé la chiave di stato
   di origine; baseline assente → `[DM]`, mai un default plausibile (R7).
5. **Idempotenti.** Ri-eseguire uno script sulla stessa review non duplica i difetti: chiave
   `{delivery_id}/{check}` come identità.
6. **Il verdetto resta umano-agentico.** Nessuno script emette PASS/FAIL da solo: produce evidenze,
   il verdetto lo firma `AG-A10-COORD` (R2, R3).

---

## Connessioni

- [[REGOLE]] · `../regole/REGOLE.md` — R1, R6, R7, R8: i vincoli che questi script devono rispettare
- [[state]] · `../state/README.md` — le chiavi che gli script leggono e scrivono
- [[KPI]] · `../kpi/KPI.md` — i KPI che queste automazioni alimentano
