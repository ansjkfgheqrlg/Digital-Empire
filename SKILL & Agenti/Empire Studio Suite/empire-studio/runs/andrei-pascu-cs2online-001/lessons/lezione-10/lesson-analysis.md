# Lezione 10 — Cliente manda audio Claude fa revisioni

**Corso:** Claude Speedrun 2 | **Sezione:** AI – per produttività e freelance (1/3)
**URL:** https://www.andrei-copy.com/cs2online/lezione-10-cliente-manda-audio-claude-fa-revisioni-zgc9x
**Video:** Vimeo `1174234472`, durata 5:48 (348s)
**Tipo:** PRATICA — confermata con 9 frame.
**Fonte:** panoramica + "Cosa hai imparato" ufficiali (14 bullet). Link "Scarica .md" presente ma rotto (punta alla pagina stessa, non a un file reale) — nota tecnica per Empire Studio.

---

## Mappa timeline (parziale)

| Tempo | Contenuto | Frame |
|---|---|---|
| 1:20 | **Demo**: telefono in mano, chat WhatsApp reale con messaggio audio da cliente | `frame-t1m20s...jpg` |
| 2:40 | **Demo**: ElevenLabs Speech-to-Text, dialog upload, selettore lingua, file reale "WhatsApp Audio 2026-03-18..." | `frame-t2m40s...jpg` |
| 4:00 | **Demo**: Claude.ai, file "WhatsApp_Audi..." allegato, prompt: "Ciao il mio cliente mi ha fatto una serie di richieste e modifiche, le allego al messaggio." | `frame-t4m00s...jpg` |

## Workflow completo (fonte primaria)

Scaricare audio WhatsApp sul Mac → caricare su ElevenLabs (selezionare lingua italiana) → ottenere trascrizione → esportare come .txt (rimuovere timestamp/speaker label se non servono; convertire in .md se serve via tool esterno) → allegare a Claude insieme al contesto (copy esistente, brand guidelines, business plan) dentro un Project dedicato al cliente → ottenere le modifiche richieste.

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Workflow completo audio-cliente→revisioni osservato: WhatsApp (scarica audio) → ElevenLabs Speech-to-Text (trascrizione, selezione lingua italiana) → pulizia testo (rimuovere timestamp/speaker) → Claude Project (allegato + contesto) → output revisioni. | Panoramica + frame t1m20s, t2m40s, t4m00s |
| KA-02 | Motivazione scelta ElevenLabs: dichiarato "più preciso di altri tool su punteggiatura e riconoscimento parole" — variante del principio "garbage in garbage out" applicata specificamente alla qualità della trascrizione, non solo del prompt. | "Cosa hai imparato" |
| KA-03 | Non è possibile allegare audio direttamente a Claude — va sempre trascritto in testo prima. | "Cosa hai imparato" |
| KA-04 | Principio "front loading del contesto" (già visto altrove nel corso) applicato specificamente all'inizio di un progetto cliente: investire ore all'inizio per costruire il miglior contesto possibile, poi riutilizzarlo (Project o cartella Cowork) in ogni conversazione futura senza ripartire da zero. | Panoramica |
| KA-05 | Lista alternative gratuite a ElevenLabs (dichiarate meno precise dall'autore): trucco YouTube auto-transcript (caricare audio su sfondo nero come "video"), Whisper (open source, forte su lingue/rumore/accenti), Buzz (app desktop basata su Whisper, esporta TXT/SRT/VTT), Handy STT (locale, no cloud), oTranscribe (manuale), MacWhisper (locale, solo Mac). | "Cosa hai imparato" (sezione alternative) |
| KA-06 | Memory per-Project confermata come vantaggio specifico: ogni Project ha memory separata, Claude "si ricorda cose specifiche di quel progetto" — coerente con lezione 9. | "Cosa hai imparato" |

## Nota tecnica per Empire Studio

Il link "Scarica .md" presente in questa pagina lezione punta all'URL della pagina stessa (non a un file Google Drive reale) — primo caso di risorsa "rotta" osservato nel run. Non un problema di pipeline nostra, limite della piattaforma corso. Contenuto comunque coperto adeguatamente da panoramica ufficiale + "Cosa hai imparato" (14 bullet, densi) + frame video.

## Connessione con Knowledge Base esistente

- KA-04 (front loading contesto) è la ennesima conferma dello stesso principio (lezioni 6, 7, 9) applicato ora al caso specifico "nuovo cliente" — nessuna nuova azione.
- KA-01 (workflow audio→trascrizione→Claude) è concettualmente simile a lezione 16 (video ads→trascrizione→Claude) — stesso pattern, dominio diverso (revisioni cliente vs ads).

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 9 frame visionati |
| NO-STUB | PASS — panoramica + bullet ufficiali completi |
| P12 traceability | PASS |
| Anomalia segnalata | PASS — link .md rotto dichiarato esplicitamente |

**Prossima lezione:** Lezione 11 — "Come organizzo la mia settimana con Claude"
