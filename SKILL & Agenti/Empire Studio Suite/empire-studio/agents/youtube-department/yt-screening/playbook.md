# yt-screening - Playbook

## Flusso operativo
1. Ricevere la lista grezza dei video del canale (titolo/descrizione/durata/views).
2. Applicare regole di screening: match focus su titolo/descrizione, soglia durata, recency.
3. Produrre la shortlist di id da ingerire, ordinata per pertinenza.
4. Spiegare il razionale di selezione (perche' inclusi/esclusi) per tracciabilita'.

## Esempi
- Happy: input valido -> yt-screening produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
