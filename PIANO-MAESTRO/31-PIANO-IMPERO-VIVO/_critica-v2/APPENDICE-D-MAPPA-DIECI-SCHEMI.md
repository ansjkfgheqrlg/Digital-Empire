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

## Schema 4 — la traccia dell'AGENCY (`agency/trace.jsonl`, 10 campi)

**Dove vive:** `company/Memory/state/agency/trace.jsonl` (22 righe, tutte del 2026-06-11,
tutte del ciclo dry-run `CY-20260611-001`), scritto da `scripts/agency-trace.ps1` a mano.
File aperto: le prime righe confermano i campi.

**I suoi campi (dal file):** `ts` · `cycle_id` · `step` · `event`
(`started`/`completed`/`handoff_sent`/`handoff_received`/`gate_passed`) · `from_reparto` ·
`to_reparto` · `hc` (l'id del contratto: `HC-A1-A2-leads`) · `agent` · `payload_summary` · `notes`.

**Perché è distinto:** non è un contratto ma il **diario di vita** dei contratti — l'unico posto
dell'Impero dove un handoff sia mai stato *percorso* (4 `handoff_sent` + 4 `handoff_received`).
Nessuno dei suoi campi coincide per nome con HC-v1, e `cp_id` non c'è (è il fatto che invalida i
328 per la legge MEMORY, `02d` §D.5).

**Verdetto: CONVERTIBILE CON ADATTATORE** — l'adattatore è già deciso da V1 §10: le tracce
diventano **viste** del contratto unico. Ogni riga del jsonl è una transizione di stato di
un'istanza HC-v2, non un documento a sé. Più un campo senza casa: `cycle_id`.

**Mappa campo→campo (riga di traccia → istanza HC-v2):**

| trace.jsonl | HC-v2 |
|---|---|
| `hc` | `_id` del contratto; la riga individua l'istanza (`_instance_id`) |
| `ts` | timestamp della transizione di `status` (il primo = `created_at`) |
| `event: handoff_sent` / `handoff_received` | `status: pending` / `accepted` |
| `event: gate_passed` | esito del criterio di accettazione valutato |
| `from_reparto` / `to_reparto` | `from.reparto` / `to.reparto` |
| `agent` (chi ha agito) | **firma di chi ha accettato** — la mappa più pulita delle dieci sezioni |
| `payload_summary` | riassunto del `payload` (vista, non sorgente) |
| `notes` | `note_correttive` quando l'evento è un rifiuto; altrimenti contesto libero |
| **`cycle_id`** (`CY-20260611-001`) | **NESSUN POSTO**: è l'id di correlazione che lega i 4 handoff di un ciclo. Non è `_instance_id` (id del singolo messaggio), non è `cp_id` (puntatore MEMORY), non è `from.task_id` (id del workflow, non della corsa). Vedi conclusione |

## Schema 5 — le 5 tracce di `empire/trace.py` (8 campi)

**Dove vive:** `empire/trace.py` (219 righe), dataclass `Traccia`, righe 57-66. File aperto.
Scrive JSON in `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/{decisions,errors,performances,reasoning-bank,sessions}/` — 25 file reali (`censimento-02:285-292`).

**I suoi campi (dal codice):** `tipo` (`decisione|errore|prestazione|lezione|sessione`) ·
`titolo` · `autore` · `prova` · `quando` · `contesto` · `tags` · `id` — 8, come il censimento
conta. Due regole cablate: `autore` vuoto → `ValueError`; `prova` vuota → `ValueError`
(`trace.py:92-95`).

**Perché è distinto:** non ha `from` né `to` né payload: registra **fatti unilaterali** con un
autore e una prova. È l'unico dei dieci con validazione d'obbligo *eseguita* (le due ValueError)
e l'unico con idempotenza (stesso tipo+titolo+giorno non duplica, `trace.py:102`).

**Verdetto: CONVERTIBILE CON ADATTATORE** — e solo per la parte che è davvero comunicazione.

**Mappa campo→campo:**

| trace.py | HC-v2 |
|---|---|
| `quando` | `created_at` |
| `id` | `_instance_id` (già id d'istanza, generato per messaggio) |
| `autore` | firma (semantica compatibile: chi risponde dell'atto) |
| `prova` | l'evidenza che il criterio di accettazione valutato a macchina deve produrre |
| `titolo` / `contesto` | `description` / `payload.context_refs` della base HC-v1 |
| `tags` | metadata (la base HC-v1 ha già un blocco `metadata` estendibile) |
| `tipo: prestazione` | la transizione `status: done` di un HC-v2 (una fase chiusa = una consegna chiusa) |
| `tipo: errore` | la transizione `status: rejected` + `note_correttive` |
| `tipo: decisione`, `lezione`, `sessione` | **fuori perimetro dichiarato**: non sono comunicazioni fra due parti, sono memoria. Non chiedono un posto in HC-v2 e non lo ricevono — restano tracce |

**L'adattatore, esplicito:** la chiamata a `trace.scrivi()` dentro il ciclo di stato di HC-v2
(quando uno `status` passa a `done`/`rejected`) — è esattamente il «punto di aggancio» già
diagnosticato in `censimento-02` §4.5 punto 1. Senza, i due archivi restano paralleli
(2 transizioni da una parte, 25 tracce dall'altra, nessun ponte).

## Schema 6 — l'evento Observability (13 campi, 9 tipi)

**Dove vive:** `company/Backbone/Observability/README.md:14-31` («Schema evento standard») —
destinazione dichiarata `company/metrics/runs.jsonl`, che **non esiste** (la cartella
`company/metrics/` non esiste; zero emettitori nel repo, `censimento-02` §4.4). File aperto.

**I suoi campi (dal README):** `ts` · `tipo` (9 valori: `run_done`, `gate_passed`, `gate_failed`,
`handoff_rejected`, `swarm_done`, `lead_generated`, `content_published`, `sale_closed`,
`evolution`) · `eco` · `reparto` · `team` · `agente` · `brand_kit` · `tier_modello` ·
`costo_usd` · `durata_sec` · `output_size` · `gate_result` · `note` — 13, come il censimento conta.

**Perché è distinto:** è telemetria, non contratto — ha un solo lato (`eco/reparto/team/agente`
sono *chi ha agito*, non mittente→destinatario) e porta quattro campi di misura che nessun altro
schema dei dieci ha: `costo_usd`, `durata_sec`, `tier_modello`, `output_size`.

**Verdetto: CONVERTIBILE CON ADATTATORE** — nel senso di V1 §10 (vista del formato unico), con
un avviso pesante sul costo.

**Mappa campo→campo:**

| Observability | HC-v2 |
|---|---|
| `ts` | timestamp della transizione |
| `tipo: handoff_rejected` | `status: rejected` (+ `note` → `note_correttive`) |
| `tipo: gate_passed`/`gate_failed` | esito del criterio di accettazione valutabile a macchina |
| `eco`/`reparto`/`team`/`agente` | `from.{ecosystem,reparto,agent}` (+ firma per chi accetta) |
| `brand_kit` | `brand_kit` — identico |
| `gate_result` | ridondante col `tipo`, si fonde nell'esito del criterio |
| `note` | contesto libero / `note_correttive` |
| `tipo: run_done`, `swarm_done`, `lead_generated`, `content_published`, `sale_closed`, `evolution` | **non sono handoff**: sono eventi di lavoro e di business. Restano nel formato-evento; l'adattatore è l'emettitore che li deriva (per i 3 tipi-handoff) dalle transizioni HC-v2 |
| **`costo_usd` · `durata_sec` · `tier_modello` · `output_size`** | **NESSUN POSTO** negli 11 né nella base HC-v1. Fintanto che l'evento resta un formato separato non è un difetto di HC-v2 — ma vedi conclusione: la legge MEMORY (`HC-ME-POST.costi`, Schema 7) pretende che il *costo* viaggi anche nel contratto, e lì il posto non c'è |

