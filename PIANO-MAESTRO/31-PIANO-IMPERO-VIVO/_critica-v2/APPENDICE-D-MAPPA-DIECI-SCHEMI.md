# Appendice D — la mappa dei dieci schemi verso HC-v2

Sentinella indipendente (fable), 2026-09-10 — ricognizione in sola lettura.

> **Mandato:** chiudere V3 §9.4 (rilievo B-3 della Critica 2). V2 §12 ha congelato HC-v2 a
> undici campi avendo confrontato **un solo** schema sorgente su dieci (APEX-7). Qui si fa
> il confronto vero: i dieci schemi di comunicazione realmente esistenti sul disco, uno per
> uno, campo per campo, contro gli undici campi di HC-v2. Verdetto per ciascuno:
> **CONVERTIBILE** / **CONVERTIBILE CON ADATTATORE** / **ESCLUSIONE MOTIVATA**.
>
> **Metodo (L7):** ogni campo dichiarato qui viene da un file aperto in questa sessione, citato
> con percorso (e riga dove serve). Dove il censimento e il disco divergono, vince il disco.

## D.0 — Da dove viene l'elenco dei dieci (perché sono dieci schemi, non varianti)

`censimento-02d-sintesi-collegamenti.md` §C.1 dichiara *«dieci schemi di comunicazione diversi»*
ma **non li elenca nominalmente** — l'elenco nominale era il lavoro rimandato da V2 §13, mai fatto.
Questa appendice lo ricostruisce dai due censimenti che li contano:

- `censimento-02-collegamenti.md:51-54` — **tre schemi di handoff** diversi nello stesso Bus:
  HC-v1 (i 4 contratti veri), `empire-handoff-contract-v1` (il template), e il terzo schema
  mostrato solo nel README del Bus. *«Tre schemi diversi, nessun validatore.»*
- `censimento-02-collegamenti.md:350-353` — **tre formati di traccia** per la stessa cosa:
  Observability (13 campi), `empire/trace.py` (8 campi), `agency/trace.jsonl` (10 campi).
- `censimento-02-collegamenti.md:233-242` — il **passaggio fra step di `empire/flow`**:
  nessun payload, solo `depends:` + la struttura `Transition`. Un settimo modo di passare
  lavoro, che *«non sa nulla»* dei contratti HC.
- `censimento-02d` §A.2 Famiglia 2 — i **passaggi-come-dati del registro LANCI**
  (`registro.yaml` + INV-20): l'unico schema verificato da una macchina.
- `censimento-02d` §A.2 (righe #290-293) — i **contratti `HC-ME-*` della MEMORY**
  (`09-ECOSISTEMA-MEMORY.md`): il codice si usa 303 volte, il file di contratto non c'è.
- `censimento-02d` §B.3 — **APEX-7 pub/sub**, testualmente *«il decimo schema di comunicazione
  dell'Impero, e l'unico senza `from` e senza `to`»*.

3 + 3 + 1 + 1 + 1 + 1 = **10**. Il conto torna con il censimento, e la frase «il decimo schema»
riferita ad APEX-7 conferma che il DOOM BOT contava così. Sono schemi **distinti** e non varianti:
ciascuno ha (a) un file sorgente proprio, (b) un insieme di campi non sovrapponibile agli altri,
(c) uno scrittore/lettore diverso — le prove sono nelle dieci sezioni che seguono.

**Gli undici campi di HC-v2 (V2 §12), contro cui si confronta:**
`_instance_id` · `created_at` · `status` (pending→accepted→done→rejected) · `queue` (percorso) ·
`scope` (intra/inter) · `brand_kit`/`icp` · `note_correttive` (su reject) · `retry`/`escalation_count` ·
firma di chi ha accettato · criterio di accettazione valutabile a macchina · `cp_id`.
Nota strutturale usata in tutta l'appendice: HC-v2 è dichiarato come **estensione di HC-v1**
(V1 §9 → V2 §12: «ai dieci campi di V1 se ne aggiunge uno»), quindi il confronto assume che
HC-v2 porti anche l'ossatura di HC-v1 (`from`, `to`, `payload`, `acceptance_criteria`,
`failure_handling`) e non soltanto gli undici campi nuovi.

---
## Schema 1 — HC-v1 (i 4 contratti veri dell'AGENCY)

**Dove vive:** `company/01-agency/A1-RICERCA/handoffs/HC-A1-A2-leads.json` ·
`A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json` · `A3-PREVENTIVI/handoffs/HC-A3-A4-contratto.json` ·
`A4-DELIVERY/handoffs/HC-A4-A6-testimonianza.json` — 4 file JSON reali, creati 2026-06-11,
tutti `"status": "template"`. **File aperto per questa scheda:** `HC-A1-A2-leads.json`.

**I suoi campi (dal file, non dal censimento):** `_schema` · `_id` (id del *contratto*) ·
`_version` · `_created` · `description` · `from` `{ecosystem, reparto, agent, task_id}` ·
`to` `{ecosystem, reparto, agent, queue}` · `payload` `{type, data, files, context_refs}` ·
`acceptance_criteria` (lista di frasi italiane) · `failure_handling` `{on_reject, on_timeout}` ·
`metadata` `{priority, status, frequenza, pii}`.
Nota di precisione (L7): i dossier lo dichiarano a 4 campi — *«handoff contract
`{from, to, payload, acceptance_criteria}`»* (`PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:34`, citato in
`02d` §D.1) — ma il file reale ne ha **11 di primo livello**. La citazione parziale sottostima lo
schema vero; il confronto qui è fatto sul file.

**Verdetto: CONVERTIBILE** — per costruzione: HC-v2 è dichiarato come estensione di HC-v1
(V1 §9: *«i dieci campi che mancano»* a HC-v1; V2 §12 aggiunge `cp_id`).

**Mappa campo→campo:**

| HC-v1 | HC-v2 |
|---|---|
| `_id` | resta l'id del contratto/tipo; il messaggio prende il nuovo `_instance_id` |
| `_created` | resta data del contratto; il messaggio prende il nuovo `created_at` |
| `metadata.status` (costante `"template"`) | `status` mutabile `pending→accepted→done→rejected` |
| `to.queue` (nome: `"leads_ready"`) | `queue` come percorso (cambia il *valore*, il campo c'è) |
| `from.ecosystem` = `to.ecosystem` | `scope` = `intra` (derivabile a macchina dai due campi) |
| `payload.data.brand_kit`/`icp_cliente` (solo in HC-A3-A4, `censimento-02:79`) | `brand_kit`/`icp` promossi a campo proprio |
| `failure_handling.on_reject` (prosa) | resta; il rifiuto concreto compila `note_correttive` |
| `failure_handling.on_timeout` (prosa) | resta — **ma vedi il buco `due_at` in conclusione: HC-v2 non ha il campo che dice *quando* scatta il timeout** |
| `acceptance_criteria` (frasi italiane) | stesso campo, valori da riscrivere in forma valutabile a macchina (upgrade di contenuto, non di forma) |
| `_schema`, `_version`, `description`, `from.*`, `to.*`, `payload.*`, `metadata.priority/frequenza/pii` | invariati nella base HC-v1 che HC-v2 estende |
| — (assente) | `cp_id`, firma, `retry`/`escalation_count`: campi nuovi, nessun dato da migrare |

## Schema 2 — `empire-handoff-contract-v1` (il template del Bus)

**Dove vive:** `company/Backbone/Bus/contracts/HC-template.json` — l'unico contratto
INTER-ecosistema del repo (01-AGENCY → 04-MARKETING), mai istanziato. File aperto.

**I suoi campi (dal file):** `_schema` · `_doc` · `from` `{ecosystem, agent, task_id}` (senza
`reparto`) · `to` `{ecosystem, agent, queue}` (qui `queue` è già un percorso:
`"company/Backbone/Bus/handoffs/"`) · `payload` `{type, data, files, context_refs}` ·
`acceptance_criteria` · `metadata` `{created_at, due_at, priority, status}` con
`status: "pending | in_progress | completed | rejected"`.

**Perché è uno schema distinto da HC-v1 e non una variante:** `_schema` diverso dichiarato nel
file stesso; `from`/`to` senza `reparto`; `status` con enum diverso (`completed`, niente
`accepted`); e porta **due campi che HC-v1 non ha**: `created_at` e **`due_at`**
(`censimento-02:51-54`: *«tre schemi diversi, nessun validatore»*).

**Verdetto: CONVERTIBILE** — con un campo orfano dichiarato.

**Mappa campo→campo:**

| empire-handoff-contract-v1 | HC-v2 |
|---|---|
| `metadata.created_at` | `created_at` (già il campo giusto, sale di livello) |
| `metadata.status` (`completed`) | `status` (`completed` → `done`, rinomina di valore) |
| `to.queue` (percorso) | `queue` — già conforme |
| `from`/`to` senza `reparto` | `from`/`to` di HC-v1 (con `reparto`): il campo mancante si compila, non si inventa — il template già nomina ecosistema e agente |
| `metadata.priority`, `payload.*`, `acceptance_criteria` | invariati nella base |
| `_doc` | `description` di HC-v1 |
| **`metadata.due_at`** | **NESSUN POSTO negli 11 campi né nella base HC-v1.** È il primo dei tre avvistamenti del campo-scadenza (vedi conclusione) |

## Schema 3 — lo schema inline del README del Bus (il «terzo dialetto»)

**Dove vive:** `company/Backbone/Bus/README.md:25-48` (blocco JSON «Handoff Contract standard
(obbligatorio — Pattern #2)») + regole di validità alle righe 50-54. Mai esistito come file
istanza: la cartella `handoffs/` contiene solo `.gitkeep`. File aperto.

**I suoi campi (dal README):** `id` · `ts` · `scope` (`inter|intra`) · `from` e `to` come
**stringhe-percorso** (`"AGENCY/Acquisizione/WF-OUTREACH-EMAIL"`) · `priority` · **`type`**
(`directive | handoff | result | escalation`) · `payload` `{task, files, brand_kit, icp}` ·
`acceptance_criteria` · `status` (`pending|accepted|in_progress|done|rejected|escalated`).
Più tre regole: `rejected` DEVE avere `note_correttive`; 2 reject → escalation automatica;
`brand_kit` obbligatorio nell'inter.

**Perché è distinto:** è l'antenato diretto di HC-v2 — `id`/`ts`/`scope`/`status`/`brand_kit`/
`icp` e le regole su `note_correttive` ed escalation sono esattamente ciò che V1 §9 ha promosso
a campi — ma con `from`/`to` piatti e un campo che gli altri due HC non hanno: `type`.

**Verdetto: CONVERTIBILE CON ADATTATORE** — serve un posto per **`type`**.

**Mappa campo→campo:**

| README Bus | HC-v2 |
|---|---|
| `id` | `_instance_id` (è già un id di messaggio: `H-20260611-0042`) |
| `ts` | `created_at` |
| `scope` | `scope` — identico |
| `from`/`to` stringa `"ECO/Reparto/Task"` | `from`/`to` oggetto di HC-v1: conversione meccanica (split su `/`) |
| `priority` | `metadata.priority` |
| `payload.brand_kit`, `payload.icp` | `brand_kit`/`icp` |
| `status` (6 valori) | `status` (4 valori): `in_progress` e `escalated` non esistono in HC-v2 — `escalated` è ricostruibile da `escalation_count ≥ 1`; `in_progress` si perde o si aggiunge all'enum (decisione, non adattatore) |
| regola `note_correttive` | campo `note_correttive` |
| regola 2-reject→escalation | `retry`/`escalation_count` |
| **`type`** (`directive|handoff|result|escalation`) | **NESSUN POSTO.** Non è `payload.type` di HC-v1 (quello è il tipo del *carico*: `lead_batch`; questo è il tipo del *messaggio*). `escalation` si ricava da `escalation_count`, ma `directive`/`result` no: il «contratto di risposta» (es. MARKETING `{copy_finale, ...}`, Schema 9) viaggerebbe come `type: result` e HC-v2 non ha il campo per dirlo. Adattatore = un campo `type` in più, o la decisione dichiarata che le risposte sono handoff a ruoli invertiti |

