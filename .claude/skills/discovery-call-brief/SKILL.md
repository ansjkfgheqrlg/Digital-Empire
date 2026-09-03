---
name: discovery-call-brief
description: "Da trascrizione o appunti di discovery call a brief strutturato per A3-PREVENTIVI. Usa questa skill quando hai note/trascrizione di una call con un prospect e devi preparare il dossier per generare un preventivo. Output: brief JSON con problema, awareness_level, stack attuale, vincoli server/ambiente, budget signal."
---

# Skill: discovery-call-brief

> Reparto: A3-PREVENTIVI | Team: T-discovery-brief | Tier: sonnet
> Kernel <=500 righe. Per il dettaglio tecnico: references/discovery-call-brief/

## Scopo

Trasformare trascrizione o appunti raw di una discovery call in un brief strutturato
pronto per T-problem-audit e T-proposal-writer (beast-preventivi).

## Input atteso

- Trascrizione testuale della call OPPURE appunti bullet-point
- Nome azienda + nicchia (da leads.db o confermato in call)
- Canale outreach che ha generato la call

## Output

Brief JSON:
```json
{
  "call_date": "YYYY-MM-DD",
  "lead_id": "string",
  "nome_azienda": "string",
  "nicchia": "string",
  "problema_principale": "descrizione in termini del cliente",
  "awareness_level": "aware | unaware",
  "dolore_quantificato": "se il cliente ha dato numeri o stime",
  "stack_attuale": "tool, CRM, piattaforme usate oggi",
  "ambiente_server": "OS, hosting, VPS, locale, cloud — con specifiche",
  "vincoli_noti": "antivirus, policy IT, permessi limitati",
  "budget_signal": "ha citato cifre? reaction al pricing?",
  "competitor_menzionati": [""],
  "domande_irrisolte": ["cose da chiarire prima del preventivo"],
  "prossimo_passo_concordato": "string",
  "trigger_evento": "l'evento specifico che ha spinto il prospect a prenotare ORA (cliente perso, obiettivo mancato, concorrente comparso). Se manca: campo vuoto, non inventato",
  "prossimo_passo_data_ora": "YYYY-MM-DD HH:MM | null se non fissata in call",
  "prossimo_passo_in_calendario": true
}
```

## Processo

1. Leggi trascrizione/appunti
2. Estrai ogni campo del brief (usa domande esplicite se un campo manca)
3. Classifica awareness_level: AWARE = sa di aver bisogno di AI/outreach; UNAWARE = descrive sintomi senza nominarli
4. Flag ogni affermazione del cliente che potra' diventare "prova reale" nel preventivo
5. Segnala domande irrisolte che bloccherebbero il Gate Preventivo

## Gate check pre-output

- ambiente_server compilato? Se no: il countdown delivery 7gg non puo' partire
- budget_signal presente? Se no: pricing a catalogo senza possibilita' di adattamento
- almeno 1 dolore quantificato? Se no: T-problem-audit dovra' stimarlo (segnala)
- `prossimo_passo_data_ora` compilato con data E ora precise, gia' messe nel calendario di
  entrambi? Se no: la discovery call NON e' chiusa (fonte: 5swDtQFyIws - Will Barron, 19:41-19:57,
  *"altrimenti la discovery call non e' stata completata"*). Non blocca la scrittura del brief, ma
  va segnalato come primo punto delle `domande_irrisolte`, perche' un "ti faccio sapere" senza data
  e' la causa piu' comune di trattative che muoiono da sole dopo una call andata bene.
- `trigger_evento` compilato? Se no: segnala. Senza il "perche' proprio ora" il preventivo non ha
  urgenza propria e T-proposal-writer dovra' costruirla dal nulla (fonte: 5swDtQFyIws, 17:28).

## Connessioni

- `company/01-agency/A3-PREVENTIVI/BACKBONE.md`
- Skill `proposal-gate` — usa questo brief per la checklist gate
- Skill `beast-preventivi` — consuma questo brief come input primario
- `Agenti/Agency/outreach/script_chiamata_freddo.md` — guida pre-call
