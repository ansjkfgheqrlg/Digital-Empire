# Wrapper L3 -- Outreach Workflow (AGENCY / Acquisizione)

> **SISTEMA ATTIVO -- ADR-003. Il codice resta in `Outreach/Outreach Workflow/`.**
> Questo file e' il punto di ingresso ufficiale per orchestrare il workflow.

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | outreach-workflow |
| Ecosistema | 01-AGENCY |
| Reparto L2 | Acquisizione |
| Stato | ACTIVE -- 300+ email/gg |
| Codice sorgente | `Outreach/Outreach Workflow/` |
| Dashboard | `Outreach/outreach-dashboard-premium/` |

## Cosa fa

Pipeline outreach automatizzata end-to-end:
1. Scraping lead (email da Maps + LinkedIn)
2. Segmentazione per settore/pain point
3. Invio email personalizzate (300+/gg)
4. Follow-up LinkedIn automatico
5. Instagram DM warm-up
6. Dashboard monitoraggio risposte

## Handoff Contract (ingresso)

```json
{
  "from": "CEO-001 / CRO-001",
  "to": "outreach-workflow",
  "payload": {
    "target_sector": "es: e-commerce, agenzie, coach",
    "pain_point": "es: bassa conversione sito",
    "daily_volume": 300,
    "linkedin_enabled": true,
    "instagram_enabled": true
  },
  "acceptance_criteria": [
    "Lista lead caricata nel DB",
    "Campagna email attiva",
    "Rate risposta >= benchmark precedente"
  ]
}
```

## Handoff Contract (uscita verso MARKETING)

```json
{
  "from": "outreach-workflow",
  "to": "04-MARKETING/Copywriting",
  "payload": {
    "tipo": "richiesta_copy_outreach",
    "pain_point_emerso": "",
    "settore": "",
    "template_da_aggiornare": ""
  }
}
```

## Istruzioni operative

1. **Token FB**: verificare scadenza prima di avviare campagne IG (blocker noto).
2. **Sessione LinkedIn**: `Outreach/linkedin_session.json` -- locale, non nel repo.
3. **Avvio**: `Outreach/AVVIA-EMAIL-LIVE.bat` (email) | `AVVIA-DASHBOARD.bat` (monitoraggio).
4. **Modifiche**: SOLO tramite ADR approvato. Non modificare codice live senza backup.

## Link skill correlate

- `skills-map.yaml` > `outreach-workflow`
- `company/Board-CSuite/CRO.md` (supervisor)
- `company/Backbone/Bus/contracts/HC-template.json` (schema handoff)
