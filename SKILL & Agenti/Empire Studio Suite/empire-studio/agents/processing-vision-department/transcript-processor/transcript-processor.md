# transcript-processor (L3 - processing-vision-department)

**Ruolo:** Pulisce e struttura il transcript (rimuove timestamp/duplicati/filler), lo allinea ai frame per la sincronia testo-immagine.
**Reparto:** processing-vision-department · **Livello:** L3 · **Lead:** department-lead
**Skill usate:** (usa i tool del reparto)

**Responsabilita':**
- Parsare i file .vtt/.srt scaricati da yt_ingest.
- Rimuovere ridondanze, tag, righe duplicate; ricostruire frasi leggibili.
- Allineare i segmenti di testo ai timestamp dei frame (per il video-watcher).
- Segnalare le parti dove il transcript e' assente/povero (servira' la visione).

**Input (handoff in):** runs/<run-id>/<id>.<lang>.vtt
**Output (handoff out):** runs/<run-id>/transcript.clean.md (testo pulito + ancore temporali).
**Quando si attiva:** su handoff dal lead del reparto

**Trace (P12):** supporta 'trascrive tutto completamente' + la sincronia con la visione.
