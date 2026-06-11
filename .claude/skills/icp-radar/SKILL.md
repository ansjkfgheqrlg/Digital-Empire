---
name: icp-radar
description: "Crea o aggiorna il profilo ICP (Ideal Customer Profile) per una nicchia. Usa quando si entra in una nuova nicchia, quando il win rate cala per 2 cicli, o quando arrivano nuovi dati da 08-INTELLIGENCE. Output: scheda ICP strutturata con criteri di qualifica espliciti per A1-RICERCA."
---

# Skill: icp-radar

> Reparto: A1-RICERCA | Team: T-icp-profiler | Tier: sonnet

## Scopo

Definire o aggiornare il profilo ICP per una nicchia di mercato.
L'ICP determina la soglia di qualifica dei lead: senza ICP chiaro, qualifier.py non sa cosa cercare.

## Input atteso

- Nome nicchia (es: "dentisti privati nord Italia", "ecommerce moda <50 dipendenti")
- Dati di campo: conversazioni outreach, preventivi vinti/persi, obiezioni ricorrenti
- Report 08-INTELLIGENCE (se disponibile)
- Competitor analysis (se disponibile)

## Output — scheda ICP

```yaml
icp:
  nicchia: "string"
  versione: "1.0"
  aggiornato_at: "YYYY-MM-DD"

  criteri_qualifica:
    must_have:
      - "dimensione_azienda: 2-20 dipendenti"
      - "settore: [lista]"
      - "canale_presidiabile: email valida raggiungibile O linkedin attivo"
      - "problema_evidente: [descrizione del segnale da ricercare]"
    nice_to_have:
      - "strumenti_digitali_gia_in_uso: [lista]"
      - "budget_segnale: [indicatori indiretti]"
    esclusioni:
      - "grande azienda con IT department (procurement lento)"
      - "concorrente diretto"

  score_threshold: 70  # su 100; lead sotto non passa in A2

  scoring_matrix:
    - criterio: "email valida"
      peso: 30
    - criterio: "dimensione in range"
      peso: 25
    - criterio: "settore in target"
      peso: 25
    - criterio: "problema_evidente in testo sito/profilo"
      peso: 20

  angolo_outreach:
    problema_principale: "string"
    hook_di_attacco: "string (da passare a T-strategist)"
    prova_da_usare: "string (risultato reale DE o caso noto di settore)"

  obiezioni_tipiche_di_nicchia:
    - obiezione: "string"
      risposta_provata: "string | null"
```

## Come usare per aggiornare A1

1. Dopo ogni win/loss: aggiorna score_matrix con peso effettivo
2. Dopo 10 lead qualificati: confronta % closed con score; abbassa/alza threshold
3. Se FORGE segnala KPI A1 sotto soglia per 2 cicli: riscrivere angolo_outreach

## Connessioni

- `company/01-agency/A1-RICERCA/BACKBONE.md`
- `company/01-agency/A3-PREVENTIVI/BACKBONE.md` — win/loss alimentano aggiornamento ICP
- `Agenti/Agency/outreach/rules/03_qualifica_lead.md` — regola qualifica attuale
