---
name: icp-radar
description: "Crea o aggiorna il profilo ICP (Ideal Customer Profile) per una nicchia. Usa quando si entra in una nuova nicchia, quando il win rate cala per 2 cicli, o quando arrivano nuovi dati da 08-INTELLIGENCE. Output: scheda ICP strutturata con criteri di qualifica espliciti per A1-RICERCA."
---

# Skill: icp-radar

> Reparto: A1-RICERCA | Team: T-icp-profiler | Tier: sonnet

## Scopo

Definire o aggiornare il profilo ICP per una nicchia di mercato.
L'ICP determina la soglia di qualifica dei lead: senza ICP chiaro, qualifier.py non sa cosa cercare.

**Principio guida**: un'audience piccola e precisa batte una grande e generica — 92% di ICP match su 31.000 follower concentrati contro 2% su un'audience generica di 200.000. La metrica che conta non è la dimensione del pubblico/database, è la concentrazione di buyer reali al suo interno (fonte: -gq8euRvNR4 — Paolo Trivellato, 01:20-03:10).

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

  trigger_evento:   # (fonte: 5swDtQFyIws - Will Barron, 05:34-07:14 e 17:28)
    # L'evento che ha spinto il cliente ad agire ORA. Non si indovina: si ricava dai clienti
    # gia' vinti, chiedendosi per ognuno "cosa e' successo poco prima che ci cercasse?".
    # Un ICP senza trigger dice CHI e' il cliente ma non QUANDO e' comprabile.
    lista_trigger_osservati:
      - "esempio: ha perso un cliente importante nell'ultimo trimestre"
      - "esempio: ha mancato un obiettivo di fatturato dichiarato"
      - "esempio: e' comparso un concorrente diretto sul suo mercato"
    segnale_ricercabile: "come quel trigger si riconosce da fuori (sito, annunci di lavoro, LinkedIn, recensioni recenti)"
    dolore_specifico: "il dolore comune ai clienti gia' vinti, nelle LORO parole, non nelle nostre"

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

## Test del riconoscimento in 1 secondo (fonte: 5swDtQFyIws - Will Barron, 03:24-05:34)

Un ICP e' scritto bene se il prospect, leggendo il messaggio che ne deriva, pensa "questo sono io"
entro un secondo. Il modo di verificarlo e' scrivere le due versioni del messaggio e confrontarle:

- **Versione generica (da scartare)**: "aiuto gli imprenditori ad aumentare il fatturato".
  Equivale alla frase-sintomo mostrata nel video come errore capitale: *"lavoriamo con chiunque
  abbia bisogno di quello che facciamo"* - sembra tenere aperte le opzioni, in realta' non parla
  a nessuno.
- **Versione operativa (da tenere)**: segmento + fascia numerica + risultato con tempo +
  meccanismo + dolore riconoscibile. Esempio reale mostrato a schermo nel video: *"aiuto titolari
  di aziende di servizi che fatturano tra $20.000 e $200.000 al mese a trovare e chiudere piu'
  contratti nei prossimi 30 giorni, o ti restituisco i soldi. Lo facciamo con un sistema di
  vendita semplice che elimina le montagne russe del fatturato su cui probabilmente sei adesso."*

Se la scheda ICP non permette di scrivere la seconda versione, mancano dei campi: quasi sempre
`trigger_evento` o `dolore_specifico`. Vanno riempiti prima di passare la scheda ad A1-RICERCA.

## Connessioni

- `company/01-agency/A1-RICERCA/BACKBONE.md`
- `company/01-agency/A3-PREVENTIVI/BACKBONE.md` — win/loss alimentano aggiornamento ICP
- `Agenti/Agency/outreach/rules/03_qualifica_lead.md` — regola qualifica attuale
