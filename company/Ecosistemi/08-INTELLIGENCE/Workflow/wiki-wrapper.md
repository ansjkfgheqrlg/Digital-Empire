# Wrapper L3 -- Wiki + Empire Studio (INTELLIGENCE)

> **Codice sorgente: `second-brain-vault/` + `SKILL & Agenti/Empire Studio Suite/`**

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | intelligence-wiki |
| Ecosistema | 08-INTELLIGENCE |
| Reparto L2 | Wiki + Ingestione |
| Stato | Wiki: ACTIVE / Empire Studio: EXPERIMENTAL |

## Cosa fa

### Wiki (`second-brain-vault/`)
- Fonte di verita' umana di Digital Empire
- Operazioni: INGEST, QUERY, LINT, SYNTHESIS, RESEARCH
- Log ogni operazione in `second-brain-vault/wiki/log.md`

### Empire Studio
- Ingestione video YouTube (frame densi + analisi Claude)
- Output: `video-analysis.md` + pattern di produzione in wiki
- **TASK 7.0 pendente**: ingestione @Legamidiamore + @dosementale (sessione dedicata)

## Handoff Contract -- Ingestione

```json
{
  "from": "qualsiasi ecosistema",
  "to": "intelligence-wiki",
  "payload": {
    "tipo": "ingest | query | research",
    "sorgente": "url | file | conversazione",
    "namespace_memory": "es: intelligence"
  },
  "acceptance_criteria": [
    "Pagina wiki creata/aggiornata",
    "Entry in wiki/log.md",
    "Cross-link ad almeno 2 pagine esistenti"
  ]
}
```
