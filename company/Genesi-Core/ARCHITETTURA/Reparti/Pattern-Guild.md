# Pattern-Guild — LIBRERIA PATTERN RIUSABILI
## Organo: ARCHITETTURA (Genesi Core) — guild trasversale

## Missione
Guild che taglia trasversalmente tutti i reparti L2: prima che ARCHITETTURA disegni *qualsiasi*
cosa da zero, la Guild cerca se esiste già un **pattern strutturale riusabile** e lo offre.
Confine netto: la Guild cataloga e propone *strutture-pattern* (forme ricorrenti) — NON produce
spec (L2.1), blueprint (L2.2) né contenuto (FORGE). È l'organo **anti-reinvenzione** dell'organo.

## Team (agenti)
| id | ruolo | tier |
|---|---|---|
| `arch-pattern-scout` | Pattern Scout: cerca pattern/strutture già esistenti da riusare PRIMA di disegnare | haiku |
| `arch-director` | conductor: decide riuso vs nuovo design quando il pattern è parziale | opus |

## Workflow di competenza
- **Nodo "cerca pattern" di WF-ARCH-DESIGN** — gira in *parallelo* a L2.1 (spec): mentre si
  scrive la spec, la Guild cerca strutture simili già esistenti.
- Alimenta L2.2 (blueprint) e L2.5 (org) con pattern riusabili, e L2.3 con candidati a schema.
- Distilla i buchi ricorrenti (da L2.4/RETRO) in nuovi pattern catalogati.

## Funzioni
1. **Ricerca pattern** — dato `{forma, scopo}`, cerca in `architettura/pattern` e nei motori reali
   strutture già esistenti che risolvono lo stesso problema strutturale.
2. **Catalogazione** — ogni pattern ha: nome, problema-che-risolve, struttura, quando-usarlo,
   quando-NON-usarlo, esempio reale. Mai un pattern senza "quando non usarlo".
3. **Match & score** — quanto il pattern esistente copre la richiesta (riuso totale/parziale/no).
4. **Anti-reinvenzione** — segnala ad `arch-director` se si sta per ridisegnare qualcosa che esiste.
5. **Distillazione** — buchi/soluzioni ricorrenti diventano nuovi pattern (loop con ReasoningBank).

## Handoff Contract (Input → Output → Gate)
- **Input:** `{ forma, scopo, vincoli }` (in parallelo all'intake di L2.1).
- **Output:** `pattern_match = { pattern_trovati[], copertura: totale|parziale|nessuna,
  struttura_riusabile, note_riuso }` offerto a L2.2/L2.5.
- **Gate:** se `copertura = totale` → si riusa il pattern (no design da zero); se `parziale` →
  L2.2 parte dal pattern e lo estende; se `nessuna` → design da zero + candidato a nuovo pattern.

## Flusso interno (passi reali)
```
{forma, scopo, vincoli}  (parallelo a L2.1)
  → arch-pattern-scout: query architettura/pattern + motori reali (skill/agent/org esistenti)
  → arch-pattern-scout: match & score copertura (totale/parziale/nessuna)
  → copertura totale  → propone riuso diretto → arch-director conferma → no design da zero
  → copertura parziale→ passa struttura_riusabile a L2.2 (estende, non reinventa)
  → copertura nessuna → segnala "novità" → dopo BUILD, candida la struttura a nuovo pattern
  ── loop: buchi ricorrenti da L2.4/RETRO → nuovo pattern catalogato + versionato
Output: pattern_match → consumato da L2.2/L2.5; nuovi pattern → architettura/pattern
```

## shared_state / memoria (namespace architettura/...)
- `architettura/pattern/<nome>` — libreria pattern riusabili: problema, struttura, quando-sì/no.
- `architettura/pattern/_index` — catalogo navigabile per forma/problema.
- `patterns` (ReasoningBank) — buchi/soluzioni ricorrenti che diventano nuovi pattern.
- Motore reale: ricerca su `skill-creator`, `architect-agent`, `org-design`, corpus skill esistenti.

## Gate / KPI
| KPI | Target |
|---|---|
| Design preceduti da ricerca pattern (anti-reinvenzione) | 100% |
| Pattern catalogati con "quando NON usarlo" | 100% |
| Riuso totale/parziale quando un pattern adatto esiste | trend ↑ |
| Reinvenzioni di strutture già esistenti | 0 (segnalate da Guild) |
| Buchi ricorrenti distillati in pattern entro 1 RETRO | trend ↑ |

## Connessioni
- [[14-DOSSIER-ARCHITETTURA]] §2 (Pattern Guild trasversale), §7 (namespace `architettura/pattern`)
- [[L2.1-Spec-Requirements]] — gira in parallelo all'intake/spec
- [[L2.2-Blueprint-Struttura]] — riceve struttura riusabile, estende invece di reinventare
- [[L2.3-Schemi-Canonici]] — pattern maturi candidati a diventare schema canonico
- [[L2.4-Validazione-Strutturale]] — i buchi ricorrenti del gate alimentano nuovi pattern
- [[L2.5-Progettazione-Ecosistemi]] — pattern organizzativi riusabili su scala org
