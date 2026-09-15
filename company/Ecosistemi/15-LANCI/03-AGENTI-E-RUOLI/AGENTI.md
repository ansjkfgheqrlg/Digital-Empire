# AGENTI — indice ufficiale dell'ecosistema 15-LANCI

> **Regola di lettura:** questo file è un indice, non una fonte. Se una riga qui contraddice
> `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`, ha torto questa riga. Se un file `.md`
> qui elencato diverge dal registro, `SCR/scripts/verifica_agenti.py` lo dice e fallisce.

I quindici agenti ufficiali vivono in `.claude/agents/<id>.md`. Ognuno ha frontmatter YAML con
SOLO `name`, `description`, `model`, `color`, `tools` — un campo in più fa scartare l'agente in
silenzio (`.claude/agents/emperator.md` §6.6).

| id | grado | modello | produce | giudicato da | reparto | file |
|---|---|---|---|---|---|---|
| `lan-direttore` | doombot | `claude-opus-5` | — (orchestra, non produce) | — | `LAN-DIR` | `.claude/agents/lan-direttore.md` |
| `lan-gate` | sentinella | `claude-sonnet-5` | verbali (li scrive `stato_lancio.py`, non lui) | — (è lui il giudice) | `LAN-QLT` | `.claude/agents/lan-gate.md` |
| `lan-pub-censore` | sentinella | `claude-sonnet-5` | `ART-PUB` (`pubblico.json`) | `lan-gate` — `GATE-PUB-1` | `LAN-MER` | `.claude/agents/lan-pub-censore.md` |
| `lan-str-filtro` | scagnozzo | `claude-haiku-4-5-20251001` | `ART-DEC` (`decisione.json`) | `lan-gate` — `GATE-STR-1` | `LAN-STR` | `.claude/agents/lan-str-filtro.md` |
| `lan-prd-collaudatore` | sentinella | `claude-sonnet-5` | `ART-CRT` (`certificato.json`) | `lan-gate` — `GATE-PRD-1` | `LAN-PRD` | `.claude/agents/lan-prd-collaudatore.md` |
| `lan-int-analista` | sentinella | `claude-sonnet-5` | `ART-RIC` (`ricerca.json`) | `lan-gate` — `GATE-INT-1` | `LAN-MER` | `.claude/agents/lan-int-analista.md` |
| `lan-prv-modello` | scagnozzo | `claude-haiku-4-5-20251001` | `ART-PRV` (`previsione.json`) | `lan-gate` — `GATE-PRV-1` | `LAN-OFF` | `.claude/agents/lan-prv-modello.md` |
| `lan-off-conductor` | doombot | `claude-opus-5` | `ART-OFF` (`offerta.json`, mai il campo `firma`) | `lan-gate` — `GATE-OFF-1` | `LAN-OFF` | `.claude/agents/lan-off-conductor.md` |
| `lan-cpy-conductor` | doombot | `claude-opus-5` | `ART-CPY` (`copy/manifest.json`) | `lan-gate` — `GATE-CPY-1` | `LAN-CPY` | `.claude/agents/lan-cpy-conductor.md` |
| `lan-fnl-costruttore` | sentinella | `claude-sonnet-5` | `ART-FNL` (`funnel.json`) | `lan-gate` — `GATE-FNL-1` | `LAN-FNL` | `.claude/agents/lan-fnl-costruttore.md` |
| `lan-edt-pianificatore` | sentinella | `claude-sonnet-5` | `ART-EDT` (`editoriale.json`) | `lan-gate` — `GATE-EDT-1` | `LAN-EDT` | `.claude/agents/lan-edt-pianificatore.md` |
| `lan-tsr-contabile` | scagnozzo | `claude-haiku-4-5-20251001` | `ART-BDG` (`budget.json`) | `lan-gate` — `GATE-TSR-1` / `GATE-TSR-2` | `LAN-TSR` | `.claude/agents/lan-tsr-contabile.md` |
| `lan-reg-calendarista` | sentinella | `claude-sonnet-5` | `ART-APE` (`apertura.json`, mai `via_libera`) | `lan-gate` — `GATE-REG-1` | `LAN-REG` | `.claude/agents/lan-reg-calendarista.md` |
| `lan-reg-tracciatore` | scagnozzo | `claude-haiku-4-5-20251001` | `ART-CNS` (`consuntivo.json`) | `lan-gate` — `GATE-CNS-1` | `LAN-REG` | `.claude/agents/lan-reg-tracciatore.md` |
| `lan-mem-distillatore` | sentinella | `claude-sonnet-5` | `ART-DBR` (`debrief.json`, `controfirma` la scrive `lan-reg-calendarista`) | `lan-gate` — `GATE-MEM-1` | `LAN-MEM` | `.claude/agents/lan-mem-distillatore.md` |

## Due eccezioni dichiarate, non bug

- **`lan-off-conductor`** non scrive mai `offerta.json` né il suo campo `firma`: produce
  `offerta.PROPOSTA.json` + `offerta.PROPOSTA.sha256`. Il file `offerta.json` vero nasce solo con
  `lancio firma <id> --prezzo N --data gg/mm/aaaa` (solo Max, INV-10).
- **`lan-reg-calendarista`** scrive `apertura.json` ma non il sotto-oggetto `via_libera` (arriva
  da `lancio via-libera`, solo Max); come `reparto_ospite` di `WF-MEMORIA` fase `MM-4` scrive
  anche il solo campo `controfirma` di `debrief.json`, mai il resto del debrief.

## Come si verifica

```bash
cd company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS
PYTHONIOENCODING=utf-8 python scripts/verifica_agenti.py
```

Esce 0 solo se tutti e 15 gli agenti rispettano il registro: file esistente, `name` == id,
`model` e `tools` identici a `registro.yaml`, nessun campo di frontmatter oltre ai cinque
ammessi, `lan-gate` senza `Write`/`Edit` (INV-09), e il campo `produce` del registro coincide con
l'artefatto citato nel corpo di ogni agente (INV-22).

## Connessioni

- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml` — la fonte di verità, sezione `agenti`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/07-REPARTI-E-GERARCHIA.md` — chi risponde a chi, e perché
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/01-ARCHITETTURA.md` — il ponte `claude -p --agent <id>`
- `company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS/CONTRATTO-STATO.md` — dove ogni agente
  scrive, contro quale schema, chi lo giudica
- `.claude/agents/emperator.md` §6.6 — cosa rende un agente ufficiale
