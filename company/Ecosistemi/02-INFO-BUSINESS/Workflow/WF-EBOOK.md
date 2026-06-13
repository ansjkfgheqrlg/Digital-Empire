# WF-EBOOK — Produzione Ebook End-to-End

## Reparto: L2-PRODOTTO
## Owner: IB-PM-product-manager + IB-MKD-forger + IB-CURRIC-designer

## Trigger
Brief validato da WF-VALIDAZIONE (score ≥60) oppure riposizionamento di materiale corso esistente in formato ebook. Caso speciale: Manuale Claude Code (203pp) — già pronto, richiede solo gate B1 (decisione prezzo/ruolo).

## Input (payload)
```json
{
  "prodotto": "titolo-ebook",
  "cartella_raw": "path cartella sorgente",
  "brief_validato": "path brief",
  "icp": "target reader",
  "outcome_primario": "trasformazione promessa al lettore",
  "ruolo_funnel": "lead-magnet-gratuito | prodotto-a-pagamento | upsell",
  "formato_output": "PDF | ePub | entrambi",
  "lunghezza_target": "numero pagine orientativo"
}
```

## Pipeline

1. **IB-MKD-forger** — `content-forge` su materiale raw → MKD
   - Per Manuale Claude Code: fonte già pronta (`Formazzione/Claude code/MANUALE COMPLETO DI CLAUDE CODE PER IL BUSINESS.md`)
   - GATE: 100% atomi coperti, ogni sezione tracciata alla fonte

2. **IB-CURRIC-designer** — MKD → struttura capitoli ebook: titoli, sommario, progressione logica
   - Per ebook il "curriculum" è la struttura narrativa: problema → soluzione → implementazione → risultato
   - GATE: struttura approvata da IB-PM; ogni capitolo ha un'idea principale

3. **Stesura capitoli** — workflow leggero: IB-PM assegna a worker Sonnet per stesura da struttura + MKD
   - Stile: brand voice Empire — diretto, pratico, senza fluff; citazioni e esempi reali DE
   - GATE: brand voice conforme; zero contenuto generico

4. **T-DESIGN-PRODOTTO** — impaginazione: copertina premium, layout interno, TOC, intestazioni capitolo
   - Prototipo: Manuale Claude Code 203pp è il benchmark visivo
   - GATE: copertina in stile Empire; PDF leggibile su mobile e desktop

5. **Sales asset** — dall'ebook si estraggono: estratto gratuito (lead magnet), punti chiave per sales page, testimonial potenziali
   - GATE: estratto non svela il 100% del valore → incentiva all'acquisto

6. **Decisione ruolo funnel** (gate B1 per Manuale Claude Code):
   - Lead magnet gratuito → opt-in page (WF-FUNNEL-EVERGREEN step 1)
   - Prodotto a pagamento → offer stack + sales page (IB-SALES-funnel)
   - GATE: decisione scritta nel catalogo con data e rationale

## Gate (soglie)
| Gate | Criterio pass |
|---|---|
| Gate MKD | 100% atomi coperti |
| Gate struttura | ICP può seguire la progressione; ogni capitolo ha 1 idea principale |
| Gate brand voice | Revisione IB-PM: diretto, pratico, zero fluff |
| Gate B1 | Ruolo nel funnel deciso e scritto nel catalogo (prezzo se a pagamento) |

## Output
Ebook PDF/ePub + copertina + estratto gratuito + punti chiave per copy → handoff a IB-SALES-funnel (se prodotto) o a CONTENT-FACTORY (se lead magnet da distribuire).

## Dry-run: come si esegue
1. IB-PM legge estratto (20% contenuto) e valuta se promessa è mantenuta
2. Revisione copertina in anteprima su mobile + stampa (se prevista)
3. Stima costi impaginazione

## Handoff in uscita
```json
{
  "from": "infobusiness/prodotto",
  "to": "infobusiness/vendite-funnel",
  "payload": {
    "ebook": "titolo",
    "file_pdf": "path PDF finale",
    "estratto": "path estratto gratuito",
    "punti_chiave_copy": "path markdown per sales page",
    "ruolo_funnel": "lead-magnet | prodotto",
    "prezzo": "X EUR | gratuito"
  },
  "acceptance_criteria": ["catalogo aggiornato", "estratto approvato", "copertina in stile Empire"]
}
```
