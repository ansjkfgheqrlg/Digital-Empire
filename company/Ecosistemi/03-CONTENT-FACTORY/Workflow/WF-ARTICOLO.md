> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 4c (WF-ARTICOLO / WF-NEWSLETTER)

# WF-ARTICOLO / WF-NEWSLETTER — Workflow Produzione Testuale

> Livello: L3 · Reparto: CF-R3 PRODUZIONE TESTUALE · Coordinatore: `CF-R3-A01-text-lead`
> Fonte: dossier 03 §4c.
> Ecosistema: `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID workflow | WF-ARTICOLO / WF-NEWSLETTER / WF-SCRIPT |
| Ecosistema | 03-CONTENT-FACTORY |
| Reparto L2 | CF-R3 PRODUZIONE TESTUALE |
| Stato | SCAFFOLD (ready to run con agenti testo) |
| Dipende da | WF-BRIEF (brief.json + keyword/topic/icp) |
| Handoff in uscita verso | CF-QA-A01 (gate) → CF-R5 o CF-R2 (script) |

---

## WF-ARTICOLO

### Pipeline

```
ordine → brief (keyword, topic, icp, formato, canale, lunghezza target)
  → CF-R3-A02 outline (heading H2/H3, fonti, claim da verificare)
  → approvazione committente se richiesta (step opzionale nel contratto)
  → CF-R3-A02 draft completo (segue brand_kit.voice, heading structure, zero genericità)
  → CF-R3-A03 SEO/AI-SEO pass:
      keyword density, meta-description ≤160chr, schema markup, AI-SEO (E-E-A-T signals)
  → GATE-COPY (struttura valida, claim verificabili, zero genericità, hook in apertura)
  → GATE-BRAND (tone vs brand_kit.voice.esempi_sì/no, parole vietate assenti)
  → formato output: md (blog) | html (piattaforma) | email-ready (newsletter plugin)
  → delivery a committente | publish via 06-PLATFORM se blog DE
```

### Dry-run

Produce: outline + stima lunghezza per sezione + tier token stimato.
Zero testo lungo senza outline approvato (efficienza e riduzione rework).

---

## WF-NEWSLETTER

### Pipeline

```
ordine → brief (topic, icp, obiettivo CTA, brand, frequenza)
  → CF-R3-A02 struttura: hook apertura + sezioni valore + blocco CTA (placeholder)
  → draft corpo newsletter (segue voice brand_kit)
  → HANDOFF a 04-MARKETING/WF-COPY-EMAIL → blocco APSOC validato per la CTA
  → assembla: corpo + blocco CTA → email-ready (formato .html o .mjml)
  → GATE-COPY (hook primo paragrafo, problema/soluzione presenti, CTA unica e misurabile)
  → GATE-BRAND (tone, palette colori email se template brand)
  → delivery: file email-ready + caption canali social per distribuzione
```

**Regola di confine:** CF scrive il corpo, Marketing scrive la CTA. Pezzi ibridi con
più CTA → escalation al Conductor per arbitrato (il brief deve dichiarare l'obiettivo
primario).

---

## WF-SCRIPT (script per CF-R2)

### Pipeline

```
ordine video (da WF-VIDEO) → brief video (durata, tipo engine, canale, brand)
  → CF-R3-A02 script strutturato:
      hook nei primi 3 secondi (formule hook-formulas di carousel-factory)
      + corpo (educativo/narrativo/testimonial per formato)
      + CTA finale (con misurazione click/link)
  → se VSL/video di conversione: blocco APSOC completo da 04-MARKETING/WF-COPY-VSL
  → GATE-COPY (hook 3s, struttura narrativa, CTA presente)
  → output: script.md in orders/<id>/02-copy/ → input per CF-R2/WF-VIDEO
```

---

## Handoff contract (ingresso)

```json
{
  "from": "CF-R1/WF-BRIEF",
  "to": "CF-R3/WF-ARTICOLO",
  "order_id": "CF-2026-XXXX",
  "payload": {
    "brief_path": "orders/<id>/01-brief/brief.json",
    "keyword_primaria": "esempio keyword",
    "lunghezza_target": "800-1200",
    "formato_output": "md | html | email-ready",
    "canale": "blog-DE | newsletter | social-thread",
    "seo_pass": true
  },
  "acceptance_criteria": [
    "brief.json completo con keyword e icp",
    "formato output dichiarato"
  ]
}
```

---

## Failure handling

| Evento | Azione |
|---|---|
| brief senza keyword/icp | → 1 richiesta strutturata di chiarimento via CF-A00 |
| outline respinto dal committente | → 1 revisione mirata, poi escalation se 2° rifiuto |
| gate-copy rosso (claim non verificabili) | → CF-R3-A02 sostituisce claim con dato reale o rimuove; mai inventare prove |
| handoff APSOC da MKT non arriva entro deadline | → Conductor allerta MKT; la newsletter esce senza CTA di conversione o si posticipa |

---

## Connessioni

- `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md` — organigramma completo
- `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md` — namespace memoria, topologia
- `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/Produzione-Testuale/README.md`
- `company/Ecosistemi/04-MARKETING/Workflow/copy-workflow-wrapper.md` — blocco APSOC per CTA
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §4c

*Fonte: dossier 03 §4c · Aggiornato: 2026-06-11*
