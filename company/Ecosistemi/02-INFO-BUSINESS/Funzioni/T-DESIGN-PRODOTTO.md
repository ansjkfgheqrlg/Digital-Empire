> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.1 (Team L4) + sez. 4a (WF-CORSO step 6)

# T-DESIGN-PRODOTTO — Team Design Prodotto

> Funzione L4 · Reparto: IB-R1-PRODOTTO · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Produrre tutti gli asset visivi del prodotto informativo: copertina ebook/corso,
slide di moduli, workbook scaricabile, certificato di completamento. Gli asset video
sono demandati a CONTENT-FACTORY tramite handoff; questo team gestisce i materiali
statici allegati al prodotto.

---

## Agente proprietario

Opera in handoff con `ib-prodotto-coordinator` e con CONTENT-FACTORY (03).
Non ha un agente L5 dedicato nel roster attuale: si appoggia agli agenti visual
della CONTENT-FACTORY via handoff contract (brief visual → consegna asset).

---

## Output per prodotto

| Asset | Formato | Destinazione |
|---|---|---|
| Copertina ebook | PNG/PDF alta risoluzione | Sales page, listing KDP |
| Slide moduli | PDF/Keynote branded | Caricamento piattaforma |
| Workbook | PDF interattivo | Incluso nel corso |
| Certificato | PDF template | Emesso automatico a completamento |

---

## Standard visivo

Brand: Mandato Empire — empire-premium-style (font, palette, layout).
Nessun asset esce senza verifica Brand-Voice Sentinel visivo (logo, colori, tono grafico).

---

## Handoff verso CONTENT-FACTORY

```json
{
  "from": "infobusiness/prodotto/design",
  "to": "content-factory/visual-design",
  "payload": { "tipo": "slide_moduli", "prodotto": "corso-skill-n1", "brand_kit": "empire-default" },
  "acceptance_criteria": ["empire-premium-style", "font approvato", "max 3 colori brand"]
}
```

---

## Connessioni

- [[IB-R1-PRODOTTO]] — reparto di appartenenza
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — fornitore video e asset visivi complessi
- [[T-PIATTAFORMA]] — destinatario degli asset per il caricamento
- [[WF-CORSO]] — workflow che include questa funzione come step 6
