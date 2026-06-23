---
Type: STATE
Status: Active
Tags: #state #CF-R4 #testo #namespace #trace #amnesia-test #cf-text #cf-scripts #cf-captions
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — CF-R4 Produzione Testuale

> Ogni ordine testuale è ripartibile a freddo dal `state.json` + `trace.jsonl`.
> Regola amnesia test: se un agente si interrompe durante la redazione o il gate, il
> successivo riparte dalla fase indicata in state.json senza ripetere il lavoro già fatto.

---

## Namespace AgentDB

| Namespace | Contenuto | Owner | Operazioni |
|---|---|---|---|
| `cf/text` | Stato ordini testuali per tipo: `{order_id, formato, brand, fase_corrente, draft_path, gate_copy, gate_brand, pronto_per_cf_r6}` | CF-R4-COORD | store dopo ogni fase; retrieve per ripresa a freddo e per dashboard |
| `cf/scripts` | Script video prodotti: `{order_id, brand, formato_video, script_path, n_parole, durata_stimata_s, gate_copy, pronto_per_cf_r3, cf_r3_workflow_target}` | CF-R4-COORD | store al completamento WF-SCRIPT; retrieve da CF-R3 per handoff |
| `cf/captions` | Caption prodotte per derivato o per ordine diretto: `{order_id, brand, canale, caption_path, n_hashtag, oggetto_email (se newsletter), n_varianti}` | CF-R4-CAPTION | store a ogni produzione caption; retrieve da CF-R7-ADAPT per pubblicazione |

---

## Regole di integrità dei namespace

1. **Nessuna sovrascrittura silenziosamente**: ogni aggiornamento di un record in `cf/text`,
   `cf/scripts`, o `cf/captions` deve incrementare il campo `version` o aggiungere un
   timestamp. Mai sovrascrivere senza lasciare traccia della versione precedente.

2. **Namespace separati per brand**: i record di tenant diversi non si mescolano.
   Ogni `memory_store` include il campo `brand_slug` per garantire il filtraggio.
   `memory_search("cf/text", {brand_slug: "brand-agency"})` restituisce solo i record
   di quel brand.

3. **Stato `pronto_per_cf_r6` e `pronto_per_cf_r3` come flag booleani verificabili**:
   CF-R7 (per la pubblicazione) e CF-R3 (per la produzione video) leggono questi flag
   prima di procedere. Il flag è `true` solo se il gate interno (CF-R4-QA) è PASS;
   non viene mai impostato manualmente senza gate completato.

4. **Handoff pendente loggato**: quando WF-NEWSLETTER emette HC-MK-CF-01 e attende
   il blocco APSOC da 04-MARKETING, lo stato `cf/text` per quell'ordine deve avere
   `fase_corrente: "in_attesa_marketing"` con timestamp dell'emissione HC.
   CF-R4-COORD può fare `memory_search("cf/text", {fase_corrente: "in_attesa_marketing"})`
   per avere una vista aggregata dei blocchi pendenti.

5. **PII check prima di ogni store**: per ordini Agency (committente cliente esterno),
   eseguire `aidefence_has_pii` sul contenuto prima di `memory_store`. Se PII rilevata:
   blocco + notifica CF-R4-COORD. Non salvare contenuti con PII non anonimizzata.

---

## Schema state.json (per ordine)

Ogni ordine testuale ha il proprio `orders/<order_id>/state.json`. Struttura standard:

```json
{
  "order_id": "CF-2026-0101",
  "workflow": "WF-ARTICOLO | WF-NEWSLETTER | WF-SCRIPT | WF-REPURPOSING",
  "brand": "brand-agency",
  "formato": "articolo | newsletter | script | repurposing",
  "avviato_il": "2026-06-23T09:00:00Z",
  "fasi": {
    "00-dry-run": {
      "stato": "completato | in_corso | non_avviato",
      "ts": "2026-06-23T09:01:00Z",
      "outline_path": "orders/CF-2026-0101/02-copy/outline.json"
    },
    "01-draft": {
      "stato": "completato",
      "ts": "2026-06-23T09:12:00Z",
      "draft_path": "orders/CF-2026-0101/02-copy/articolo-draft.md",
      "word_count": 1387,
      "gap_dati": []
    },
    "02-seo": {
      "stato": "completato",
      "ts": "2026-06-23T09:18:00Z",
      "seo_path": "orders/CF-2026-0101/02-copy/articolo-seo.md",
      "keyword_density_pct": 1.73
    },
    "03-gate-copy": {
      "stato": "completato",
      "ts": "2026-06-23T09:20:00Z",
      "esito": "PASS | FAIL",
      "n_rework": 0,
      "campi_fail": []
    },
    "04-gate-brand": {
      "stato": "completato",
      "ts": "2026-06-23T09:22:00Z",
      "esito": "PASS | FAIL",
      "n_rework": 0
    },
    "05-output": {
      "stato": "completato",
      "ts": "2026-06-23T09:23:00Z",
      "final_md": "orders/CF-2026-0101/02-copy/articolo-final.md",
      "final_html": "orders/CF-2026-0101/02-copy/articolo-final.html"
    }
  },
  "handoff_marketing": {
    "richiesto": false,
    "handoff_id": null,
    "gate_copy_guild": null
  },
  "pronto_per_cf_r6": true,
  "pronto_per_cf_r3": false,
  "stato_finale": "completato | in_rework | in_attesa_marketing | bloccato"
}
```

---

## Schema trace.jsonl (append-only, ogni riga un evento)

Il file `orders/<order_id>/trace.jsonl` è append-only. Ogni passo significativo
(draft avviato, gate eseguito, handoff emesso, rework avviato) appende una riga:

```json
{"ts":"2026-06-23T09:01:00Z","agent":"cf-r4-write","event":"dry_run_outline","engine_id":null,"job_id":null,"crediti_stimati":0,"crediti_consumati":null,"nota":"outline.json prodotto; nessun draft avviato"}
{"ts":"2026-06-23T09:05:00Z","agent":"cf-r4-write","event":"draft_avviato","engine_id":"sonnet","job_id":null,"crediti_stimati":null,"crediti_consumati":null,"nota":"redazione avviata; angle gap-contenuto-conversione; hook domanda-provocatoria"}
{"ts":"2026-06-23T09:12:00Z","agent":"cf-r4-write","event":"draft_completato","engine_id":"sonnet","job_id":null,"crediti_stimati":null,"crediti_consumati":null,"nota":"articolo-draft.md 1387 parole; 0 gap dati; auto-verifica PASS"}
{"ts":"2026-06-23T09:18:00Z","agent":"cf-r4-seo","event":"seo_pass_completato","engine_id":"haiku","job_id":null,"crediti_stimati":null,"crediti_consumati":null,"nota":"keyword density 1.73%; meta aggiornata; articolo-seo.md prodotto"}
{"ts":"2026-06-23T09:20:00Z","agent":"cf-r4-qa","event":"gate_copy_pass","engine_id":null,"job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"7/7 campi PASS; n_rework 0"}
{"ts":"2026-06-23T09:22:00Z","agent":"cf-r4-qa","event":"gate_brand_pass","engine_id":null,"job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"tone campionato 5 campioni: PASS; parole_vietate: 0 occorrenze"}
{"ts":"2026-06-23T09:23:00Z","agent":"cf-r4-coord","event":"output_final","engine_id":null,"job_id":null,"crediti_stimati":0,"crediti_consumati":0,"nota":"articolo-final.md e .html depositati; pronto_per_cf_r6: true"}
```

---

## Ripresa a freddo (amnesia test)

Se CF-R4-WRITE si interrompe durante la redazione:
1. CF-R4-COORD legge state.json: fase `01-draft` → `stato: "in_corso"`.
2. Controlla trace.jsonl: c'è `draft_avviato` ma non `draft_completato`?
3. Sì → il draft è parziale o non esiste; ricomincia dal passo 1.
4. Se il file `articolo-draft.md` esiste ed è ≥50% del word_count target → considera
   il draft parziale come base; CF-R4-WRITE riprende dalla sezione non completata
   (identificata dal confronto parole rilevate vs word_count target).

Se CF-R4-QA si interrompe durante il gate:
1. CF-R4-COORD legge state.json: fase `03-gate-copy` → `stato: "in_corso"`.
2. Non c'è verdict.json: il gate non è completo. Lo riesegue da capo.
3. Il gate è idempotente: rieseguire non modifica il testo, solo emette il verdetto.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — dettaglio schema trace e regola ripresa a freddo
- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — owner state.json per ogni ordine
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — scrive in state.json dopo ogni gate
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · §9 namespace CF-R4 (`cf/text`, `cf/scripts`, `cf/captions`)
