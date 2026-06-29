---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #agency #copywriting #A5
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — A5 Copywriting Interno

> Definizione dei namespace memoria del reparto, struttura dei file di stato, regole di
> integrità e lifecycle. **Nessuna PII negli schemi:** le obiezioni sono anonimizzate a monte
> (HC-AG-IN-01). Le baseline KPI sono `[DM]` finché non misurate.

---

## Namespace memoria del reparto — `agency/a5/...`

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Templates | `agency/a5/templates/` | Template attivi per canale + versione + esito Gate Bibbia + stato refresh | AG-A5-WRITE | AG-A5-COORD, AG-A5-QA, A2 |
| Performance | `agency/a5/performance/` | Reply rate per variante, verdetto A/B, decisione adozione/scarto | AG-A5-LEARN | AG-A5-COORD, AG-A5-WRITE |
| Obiezioni | `agency/a5/obiezioni/` | Libreria obiezioni reali (anonimizzate) → risposta provata → prova → stato | AG-A5-OBJ | AG-A5-WRITE, AG-A5-SCRIPT, AG-A5-QA |
| Script | `agency/a5/script/` | Script discovery/chiusura per nicchia, esito gate, consegna A8 | AG-A5-SCRIPT | AG-A5-COORD, AG-A5-QA |

Nota: lo state runtime del motore di outreach (`leads.db`, esiti invio) resta in
`Outreach/Outreach Workflow/` e in `agency/outreach`; A5 lo legge, NON lo duplica qui.

---

## Struttura file di stato

### Refresh state (`agency/a5/templates/{refresh_id}/state.json`)

```json
{
  "refresh_id": "REFRESH-A5-001",
  "canale": "email | linkedin | instagram",
  "template_origine": "EMAIL-V3",
  "elemento_variato": "hero | problema | soluzione | obiezione | cta",
  "data_avvio": "YYYY-MM-DD",
  "varianti": [
    {"variante": "V1", "gate_bibbia": "pending | PASS | FAIL", "fail_check": "1_apsoc | 2_cta | 3_dependency | null"},
    {"variante": "V2", "gate_bibbia": "PASS", "fail_check": null}
  ],
  "ab_status": "non_avviato | in_corso | verdetto",
  "verdetto_ab": "winner_V2 | winner_controllo | inconclusivo | null",
  "variante_adottata": "V2 | null",
  "stato": "in_progress | chiuso",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Obiezione state (`agency/a5/obiezioni/{obiezione_id}.json`)

```json
{
  "obiezione_id": "OBJ-A5-001",
  "tipo": "tempo | prezzo | fiducia | rischio | timing",
  "testo_anonimizzato": "non ho tempo per gestire un'altra cosa",
  "nicchia": "freelance digitali | e-commerce | ...",
  "risposta_provata": "rif. risposta testata",
  "prova": "rif. conversazione reale / esito A/B / case study A6",
  "stato": "validata | non_validata",
  "frequenza": "[DM]",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Script state (`agency/a5/script/{script_id}.json`)

```json
{
  "script_id": "SCRIPT-A5-001",
  "tipo": "discovery | chiusura",
  "nicchia": "e-commerce",
  "offerta": "sprint CRO pay-on-performance",
  "next_step": "firma | call_successiva | invio_preventivo",
  "obiezioni_provate": ["OBJ-A5-001", "OBJ-A5-004"],
  "gate_bibbia": "pending | PASS | FAIL",
  "consegnato_a8": false,
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Regole di integrità dei namespace

1. **Gate prima del rilascio** — nessun template in `agency/a5/templates/` passa al rollout e
   nessuno script in `agency/a5/script/` va ad A8 senza `gate_bibbia: "PASS"` (REGOLE R1).

2. **Obiezione senza prova = non_validata** — un record in `agency/a5/obiezioni/` con `prova`
   vuoto deve avere `stato: "non_validata"` e non può essere usato in copy rilasciato (REGOLE R4).

3. **Verdetto A/B obbligatorio alla chiusura** — un refresh in stato `chiuso` deve avere
   `verdetto_ab` popolato. Nessuna `variante_adottata` senza verdetto su campione sufficiente (R3).

4. **No PII negli schemi** — le obiezioni sono anonimizzate a monte (HC-AG-IN-01); nessun nome,
   email o handle in chiaro nei file di stato.

5. **Ripartibilità a freddo** — tutti gli state hanno `last_updated`. Un refresh o uno script
   interrotto riprende dallo step esatto leggendo lo state, senza riestrarre il contesto.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Refresh state | STEP 2 WF-COPY-REFRESH | Ad ogni step del workflow | Dopo chiusura con verdetto; non eliminato |
| Obiezione state | Prima raccolta da HC-AG-IN-01 | Quando arriva una nuova prova (non_validata → validata) | Mantenuto come libreria viva |
| Script state | STEP 5 WF-SCRIPT-CALL | Dal feedback loop di A8 (nuove prove) | Archiviato dopo consegna; linkato alle obiezioni usate |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4-6` — namespace e ripartibilità
- [[WF-COPY-REFRESH]] · `workflow/WF-COPY-REFRESH.md` — produce refresh state
- [[WF-SCRIPT-CALL]] · `workflow/WF-SCRIPT-CALL.md` — produce script state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi state
