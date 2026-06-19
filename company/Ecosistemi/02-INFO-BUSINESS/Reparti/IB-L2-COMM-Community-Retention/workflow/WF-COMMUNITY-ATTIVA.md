---
Type: CONCEPT
Status: Active
Tags: #workflow #infobusiness #community #engagement #social-proof #IB-L2-COMM
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COMMUNITY-ATTIVA — Community di Valore e Social Proof

> **Workflow:** WF-COMMUNITY-ATTIVA · **Reparto:** IB-L2-COMM Community & Retention
> **Trigger:** cadenza ricorrente (settimanale + bisettimanale + mensile)
> **Output:** community attiva, testimonianze raccolte, report mensile, segnali cross-sell
> **Gate di uscita:** G-COMM — nessuna testimonianza pubblicata senza metrica verificata
> **Nuovo:** TARGET-V2 (non presente in v1).

---

## Scopo

Gestire la community (WhatsApp/Discord previsto dal catalogo) come spazio di valore continuativo
con rituali settimanali, Q&A pianificati e un ciclo di engagement che riduce il churn passivo. La
community esiste per gli studenti, non per vendere: i rituali generano valore prima di chiedere.
Genera anche social proof reale e identifica segnali cross-sell, senza forzare nessuno dei due.

---

## Trigger

- **Settimanale:** lunedì / mercoledì / venerdì → rituali community (IB-COMM-ENGAGE).
- **Bisettimanale:** raccolta testimonianza a milestone (IB-COMM-SOCIAL).
- **Mensile:** report community + aggiornamento piano contenuti (IB-COMM-HEALTH → IB-COORD-COMMUNITY).

---

## Input (JSON)

```json
{
  "trigger": "rituale_settimanale | raccolta_testimonianza | report_mensile",
  "mese": "2026-07",
  "tema_mese": "primi risultati pratici",
  "canale": "whatsapp | discord",
  "piano_mese_path": "infobusiness/community/engagement/2026-07_community.md",
  "coorti_attive": ["lancio-2026-Q3-corso-X"]
}
```

---

## Pipeline (step + owner)

```
[Lunedì] Prompt discussione — owner: IB-COMM-ENGAGE
  → domanda aperta su applicazione pratica del corso (tema del mese)

[Mercoledì] Contenuto bonus — owner: IB-COMM-ENGAGE
  → snippet / tip / caso d'uso coerente col tema

[Venerdì] Q&A — owner: IB-COMM-ENGAGE
  → Q&A live 30min oppure risposta scritta alle top 3 domande della settimana
  → estrae spunti (segnali cross-sell, feedback prodotto) → IB-COMM-HEALTH

[ogni 2 settimane] Raccolta testimonianza — owner: IB-COMM-SOCIAL
  → studente a milestone (alert IB-COMM-HEALTH) → richiesta testimonianza + raccolta prova
  → GATE G-COMM (IB-COMM-QA): metrica reale verificata + consenso pubblicazione
  → SE PASS → archivia in testimonials/; SE FAIL → non pubblica

[ogni mese] Report community — owner: IB-COMM-HEALTH → IB-COORD-COMMUNITY
  → engagement rate, progress medio, segnali abbandono
  → IB-COORD-COMMUNITY aggiorna il piano contenuti del mese successivo
```

---

## Gate

| Gate | Owner | Criterio | Fallimento |
|---|---|---|---|
| **G-COMM** (testimonianze) | IB-COMM-QA | Metrica reale e verificabile + nessun claim non sostenuto (Art.2) + consenso pubblicazione | FAIL → testimonianza non pubblicata; feedback a IB-COMM-SOCIAL |
| **G-ENGAGE** (rituali) | IB-COMM-ENGAGE | Rituale pubblicato secondo piano, non duplicato | Engagement ≈0 per 2 settimane → segnala a IB-COORD-COMMUNITY (piano da rivedere) |

---

## Output (JSON)

```json
{
  "mese": "2026-07",
  "rituali_pubblicati": {"prompt": 4, "bonus": 4, "qa": 4},
  "engagement": {"studenti_attivi_settimana_media": "44%", "risposte_totali": 187},
  "testimonianze": {"raccolte": 5, "pass_g_comm": 4, "fail_g_comm": 1},
  "segnali_cross_sell": [{"studente_id": "stud-1183", "to": "IB-COMM-CROSSSELL"}],
  "report_mensile_path": "infobusiness/community/engagement/2026-07_community.md",
  "timestamp": "2026-07-31T18:00:00Z"
}
```

---

## Handoff

- **→ IB-COMM-CROSSSELL**: segnali cross-sell osservati in community (domande implementazione).
- **→ IB-COMM-SOCIAL**: alert milestone per raccolta testimonianza (via IB-COMM-HEALTH).
- **→ IB-L2-PRODUCT** (HC-COMM-PROD-01): domande ricorrenti / drop-off = feedback prodotto.
- **→ IB-COORD-COMMUNITY**: report mensile → piano contenuti mese successivo.

---

## Dry-run (esempio)

**Trigger:** mese di luglio 2026, tema "primi risultati pratici", canale Discord.

1. **Lunedì** — IB-COMM-ENGAGE pubblica: "Qual è il primo risultato concreto che hai ottenuto?".
   14 risposte, 11 studenti attivi. Spunto rilevato: 3 studenti chiedono "come lo faccio per la
   mia azienda" → inoltrato a IB-COMM-HEALTH → IB-COMM-CROSSSELL.
2. **Venerdì** — Q&A live; top 3 domande risposte. Una domanda ricorrente su un passaggio del
   modulo 3 → segnalata come possibile attrito prodotto a IB-L2-PRODUCT.
3. **Settimana 2** — IB-COMM-HEALTH segnala stud-1183 al 100%. IB-COMM-SOCIAL chiede testimonianza:
   "da 0 a 3 clienti in 6 settimane" + screenshot CRM. Sottoposta a G-COMM → IB-COMM-QA PASS →
   archiviata in testimonials/.
4. **Fine mese** — IB-COMM-HEALTH report: engagement medio 44%, 5 testimonianze (4 PASS, 1 FAIL
   per metrica non verificabile). IB-COORD-COMMUNITY pianifica agosto: tema "scalare i primi risultati".

**Output:** community attiva, 4 testimonianze pubblicabili, 1 segnale cross-sell qualificato in
pipeline, 1 feedback prodotto a IB-L2-PRODUCT.

---

## Connessioni

- [[ib-comm-engage]] · `agenti/ib-comm-engage.md`
- [[ib-comm-social]] · `agenti/ib-comm-social.md`
- [[ib-comm-qa]] · `agenti/ib-comm-qa.md`
- [[ib-comm-health]] · `agenti/ib-comm-health.md`
- [[WF-CROSSSELL-BRIDGE]] · `workflow/WF-CROSSSELL-BRIDGE.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — prove non promesse)
