# Shared State — Outreach Message Team

Lo stato condiviso vive su **filesystem**, un JSON per lead, per coerenza con il resto
dell'ecosistema Outreach di Digital Empire (stesso pattern di `EmpireDesk/state/*.json`
usato da Areus/preventa-maps-scraper — vedi `company/Memory/checkpoints/CP-20260728-002.md`).

## Percorso canonico
```
Outreach/knowledge/outreach-message-team-state/<lead_id>.json
```

## Schema di un lead-state

```json
{
  "lead_id": "str (univoco, es. normalizza_telefono o slug nome+azienda)",
  "canale": "linkedin | whatsapp | email",
  "nicchia": "str (es. 'concessionario-auto-import', 'video-editor', 'saas-founder')",
  "variabili_nicchia": ["str", "..."],
  "dati_lead": {
    "nome": "str",
    "azienda": "str | null",
    "riferimento_specifico": "str | null (es. link al video/annuncio/prodotto del lead)"
  },
  "value_offer": {
    "prodotta_da": "case-study-forge",
    "tipo": "artificial_case_study | real_case_study",
    "descrizione": "str",
    "asset_prodotto": "str | null (link/path al lavoro gratuito consegnato)"
  },
  "stage": "nuovo | value_offer_pronta | draft_scritto | validato | inviato | in_attesa | risposto | archiviato",
  "tentativo_numero": "int (1, 2 o 3)",
  "storico_messaggi": [
    {
      "tentativo": "int",
      "testo": "str",
      "gancio_usato": "str (rif. a un atomo/pilastro della Bibbia)",
      "esito_validazione": "approvato | respinto",
      "motivo_respinto": "str | null",
      "inviato_il": "ISO-datetime | null",
      "risposta_ricevuta": "bool",
      "data_risposta": "ISO-datetime | null"
    }
  ],
  "validazione_corrente": {
    "validato_da": "rule-keeper",
    "checklist": {
      "pilastro_1_personalizzazione": "bool",
      "pilastro_2_chiarezza_3sec": "bool",
      "pilastro_3_valore_anticipato": "bool",
      "pilastro_4_microcommitment": "bool",
      "pilastro_5_basso_attrito": "bool"
    },
    "esito": "approvato | respinto",
    "note": "str"
  },
  "aggiornato_il": "ISO-datetime"
}
```

## Chi legge/scrive cosa

| Campo | Scrive | Legge |
|---|---|---|
| `dati_lead`, `nicchia` | Chi avvia il ciclo (Max o uno scraper a monte, es. Preventa) | Tutti |
| `value_offer` | case-study-forge | message-writer, rule-keeper |
| `storico_messaggi[].testo`, `gancio_usato` | message-writer | rule-keeper, followup-sequencer |
| `validazione_corrente` | rule-keeper | message-writer (per il loop di correzione), followup-sequencer |
| `stage`, `tentativo_numero` | rule-keeper (dopo approvazione) + followup-sequencer (dopo invio/risposta) | Tutti |

## Regola di concorrenza

Un solo lead-state file per lead, letto-modificato-scritto per intero ad ogni
transizione (stesso pattern read-modify-write già in uso in `areus.py` di questo repo).
Nessuna scrittura parziale/patch: chi scrive rilegge sempre il file intero prima di
modificarlo, per evitare di sovrascrivere aggiornamenti di un altro agente nello stesso
ciclo (nella pratica il flusso è sequenziale, quindi il rischio di race condition è basso,
ma la regola resta per sicurezza se in futuro più lead girano in parallelo).
