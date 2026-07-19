---
Type: README
Status: Active
Tags: #scripts #automazione #partnership #referral #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# scripts/ — A9 Partnership & Referral

> Automazioni **deterministiche** del reparto. Uno script fa I/O e conta: **non giudica**.
> Ogni decisione (esito triage, PASS/FAIL del gate, routing) resta di un agente.

---

## Stato

Nessuno script implementato. Il reparto è greenfield v2: prima si stabilizzano i workflow a mano,
poi si automatizza ciò che si è dimostrato ripetitivo. **[DM]** su volumi e frequenza.

---

## Script previsti

| Script | Scopo | Owner | Stato |
|---|---|---|---|
| `nonicp_intake.py` | Legge il batch "scarta/nurture" da `agency/a1/leads`, crea i record `agency/a9/nonicp/{lead_ref}` con esito vuoto e apre il `run_id` | `AG-A9-QUALIFY` | [DM] |
| `zero_loss_check.py` | Conta `lead_totali` vs `lead_con_esito` su un batch; ritorna exit code ≠ 0 se copertura < 100% (Zero-Loss Gate, R5) | `AG-A9-QUALIFY` | [DM] |
| `consent_lint.py` | Valida che ogni referral abbia `consent:{flag,data,fonte}` completo e che **nessun campo contenga PII** (R3 + R4). Blocca il gate se fallisce | `AG-A9-QA` | [DM] |
| `commission_calc.py` | Data una `commissione_catalogo_id` + deal chiuso confermato, calcola l'importo. Rifiuta importi fuori catalogo (R6) | `AG-A9-MGMT` | [DM] |
| `partner_scorecard.py` | Aggrega per `partner_id`: referral inviati, PASS-rate al gate, chiusure, commissioni | `AG-A9-INTEL` | [DM] |

---

## Regole per gli script del reparto

1. **Nessun contatto esterno.** Nessuno script invia email, DM o messaggi a lead o partner.
   L'outreach è un atto umano/agentico tracciato, mai un cron.
2. **Nessuna PII** in input, output, log o file temporanei (R4). Gli script lavorano su
   `lead_ref` / `partner_id`.
3. **Idempotenti.** Rieseguire uno script sullo stesso `run_id` non duplica record e non
   sovrascrive un `gate_status` già scritto.
4. **Exit code parlanti.** `0` = OK, `1` = gate FAIL (blocco atteso), `2` = errore tecnico.
   Un gate FAIL **non** è un errore da ignorare: è l'output corretto.
5. **Zero stime** (R7). Se un dato manca, lo script scrive `[DM]`, non un valore plausibile.
6. **Read-only sui namespace altrui.** `agency/a1/*`, `agency/a2/*`, `agency/a8/*`, `agency/clients`
   sono in sola lettura per A9.

---

## Connessioni

- [[state/README]] · `state/README.md` — schema dati su cui operano gli script
- [[REGOLE]] · `regole/REGOLE.md` — R3, R4, R5, R6, R7 che gli script devono far rispettare
- [[SKILLS]] · `skills/SKILLS.md` — skill del reparto (livello superiore agli script)
