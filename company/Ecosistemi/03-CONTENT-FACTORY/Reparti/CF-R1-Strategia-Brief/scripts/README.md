---
Type: SCRIPTS
Status: Active
Tags: #scripts #content-factory #CF-R1 #automazione #deterministico
Created: 2026-06-19
Last updated: 2026-06-19
---

# Scripts — CF-R1 Strategia & Brief

> **Reparto:** CF-R1 Strategia & Brief · **Ecosistema:** 03-CONTENT-FACTORY
> Questi script sono deterministici: dato lo stesso input producono sempre lo stesso
> output verificabile. Nessuno script esegue chiamate a engine esterni o spende crediti.

---

## Script target

### 1. `brief-validator` — Validatore brief offline

**Scopo:** Verifica un `brief.json` o `brief-draft.json` contro la checklist gate CF-R1-QA
senza avviare l'intero workflow. Utile per debug, test di regressione, e verifica manuale.

**Interfaccia:**
```
python scripts/brief-validator.py --order-id CF-2026-0042
python scripts/brief-validator.py --file orders/CF-2026-0042/01-brief/brief-draft.json
```

**Output:**
```json
{
  "file": "orders/CF-2026-0042/01-brief/brief-draft.json",
  "gate": "PASS | FAIL",
  "campi_verificati": 7,
  "campi_validi": 7,
  "campi_mancanti": []
}
```

**Dipendenze:** nessuna dipendenza da engine esterni; legge solo file locali.
**Status:** target — da implementare in fase V2-6 build effettiva.

---

### 2. `calendar-builder` — Costruttore piano editoriale da riga di comando

**Scopo:** Genera il piano editoriale settimanale per una lista di brand_slug senza
dover avviare il workflow completo. Legge i brand_kit dal repository e i trend attivi
da `cf/patterns/`; produce il piano in `cf/calendars/`.

**Interfaccia:**
```
python scripts/calendar-builder.py --week 2026-W26 --brands mentalita-brutale brand-agency
python scripts/calendar-builder.py --week 2026-W26 --all-active
```

**Output:** `cf/calendars/settimana-2026-W26.json` con lo stesso schema del WF-CALENDAR.

**Dipendenze:** accesso ai file `brands/*/brand-kit.json`; accesso a `cf/patterns/`;
nessuna dipendenza da engine.
**Status:** target — da implementare in fase V2-6 build effettiva.

---

### 3. `trend-intake` — Validatore e registratore trend da riga di comando

**Scopo:** Processa manualmente un brief trend (utile per testing di WF-TREND-BRIEF senza
attendere il ciclo automatico di 08-INTELLIGENCE). Verifica l'età del trend e — se valido —
lo deposita in `cf/patterns/<brand_slug>/trend-attivi.json`.

**Interfaccia:**
```
python scripts/trend-intake.py --file cf/briefs/trend/TREND-2026-0089.json
python scripts/trend-intake.py --topic "Creator economy Q2" --brand mentalita-brutale --data-trend "2026-06-18T14:00:00Z"
```

**Output:**
```json
{
  "trend_id": "TREND-2026-0089",
  "validita": "OK | SCARTATO",
  "eta_ore": 18.5,
  "depositato_in": "cf/patterns/mentalita-brutale/trend-attivi.json"
}
```

**Dipendenze:** nessuna dipendenza da engine; legge/scrive solo file locali.
**Status:** target — da implementare in fase V2-6 build effettiva.

---

## Principi degli script

- **Deterministici:** lo stesso input produce sempre lo stesso output; nessun elemento
  casuale o dipendente dallo stato runtime degli agenti.
- **Zero crediti:** nessuno script effettua chiamate a modelli LLM o engine a pagamento.
- **Idempotenti:** rieseguire lo stesso script con lo stesso input non causa danni;
  sovrascrive lo stesso output senza effetti collaterali.
- **Dry-run disponibile:** ogni script supporta `--dry-run` che stampa l'output atteso
  senza scrivere su disco.

---

## Connessioni

- [[WF-BRIEF]] · `workflow/WF-BRIEF.md` — brief-validator ne testa il gate
- [[WF-CALENDAR]] · `workflow/WF-CALENDAR.md` — calendar-builder ne implementa la logica
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md` — trend-intake ne testa il STEP 1
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
