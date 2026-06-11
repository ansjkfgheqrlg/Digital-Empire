# Wrapper L3 -- Copy Workflow (MARKETING / Copywriting)

> **Codice sorgente: `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`**
> MOTORE COPY PRINCIPALE di Digital Empire. Gate APSOC >= 80 obbligatorio.

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | copy-workflow |
| Ecosistema | 04-MARKETING |
| Reparto L2 | Copywriting |
| Stato | ACTIVE -- motore principale |
| Codice sorgente | `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` |
| Manuale | `SKILL & Agenti/Copy-Workflow-manuale/Il+manuale+del+copywriting+V1.1.pdf` |

## Cosa fa

Pipeline copy completa basata su framework APSOC:
- **A1-A8**: Attenzione (8 tecniche headline + hook)
- **S1-S3**: Struttura (pagina vendita, email, post)
- Gate qualita' automatico: score APSOC >= 80 (>= 85 per pagine vendita)

## Handoff Contract (ingresso)

```json
{
  "from": "qualsiasi ecosistema",
  "to": "copy-workflow",
  "payload": {
    "tipo_copy": "email | pagina_vendita | post_social | script_video | ads",
    "prodotto": "",
    "icp": "",
    "pain_point": "",
    "obiettivo_cta": "",
    "lunghezza": "short | medium | long"
  },
  "acceptance_criteria": [
    "APSOC score >= 80",
    "Proof presente (no claim senza dato)",
    "Brand voice: diretto, provocatorio, trasparente"
  ]
}
```

## Handoff Contract (uscita)

```json
{
  "from": "copy-workflow",
  "to": "ecosistema_richiedente",
  "payload": {
    "copy_prodotto": "",
    "apsoc_score": 0,
    "revisioni_necessarie": [],
    "approvato": false
  }
}
```

## Script cold outreach

Script specifico per outreach: `SKILL & Agenti/Copy-Workflow-manuale/script-cold-outreach-digital-empire.md`

## Gate qualita' (CMO-001)

Prima di consegnare qualsiasi copy:
- [ ] P prima di S (Problema descritto prima della Soluzione)
- [ ] A8 score >= 80 (inserire nella nota del handoff)
- [ ] Zero claim senza prova
- [ ] Brand voice check: niente "canoni mensili", niente passivo, niente generico
