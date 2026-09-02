# tiktok-trend-scout - Playbook

## Flusso operativo
1. Elencare i video di un profilo/hashtag (extract_flat).
2. Filtrare per pertinenza al focus (descrizione/hashtag/engagement).
3. Prioritizzare demo pratiche e tutorial rispetto a intrattenimento puro.
4. Produrre la shortlist per il tiktok-ingester.

## Esempi
- Happy: input valido -> tiktok-trend-scout produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
