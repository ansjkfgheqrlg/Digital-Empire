# yt-screening (L3 - youtube-department)

**Ruolo:** Filtra i video di un canale/playlist per pertinenza (focus, argomento, qualita') prima dell'ingestion pesante, per efficienza.
**Reparto:** youtube-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** skills/tier2-functional/yt-ingest-skill

**Responsabilita':**
- Ricevere la lista grezza dei video del canale (titolo/descrizione/durata/views).
- Applicare regole di screening: match focus su titolo/descrizione, soglia durata, recency.
- Produrre la shortlist di id da ingerire, ordinata per pertinenza.
- Spiegare il razionale di selezione (perche' inclusi/esclusi) per tracciabilita'.

**Input (handoff in):** videos.json grezzo dal channel-ingester + focus/strategia.
**Output (handoff out):** shortlist.json (id selezionati + score + motivo) per l'ingester.
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** risponde a 'screening di tutti i video del canale oppure dell'argomento'.
