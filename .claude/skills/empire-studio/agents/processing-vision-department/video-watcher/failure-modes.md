# video-watcher - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Descrizioni inventate (allucinazione) | "Figma con 5 componenti" su un frame che non lo mostra | Regola NO-FINTO nel system-prompt; obbligo di Read del frame prima di descrivere | visual-verifier confronta descrizione vs frame; cerca claim non ancorati | Riscrivi guardando di nuovo il frame; marca le inferenze con `➕` |
| Descrizioni generiche | "mostra una UI", "si vede una schermata" | Playbook richiede elementi specifici (testo, pulsanti, valori) | Lint: frasi < 8 parole o senza sostantivi concreti | Re-watch del frame con prompt di dettaglio |
| Frame mancanti/illeggibili | Visual Timeline con buchi, frame nero | frame_extractor con seek robusto; controllo size>0 | manifest.json vs frame presenti; PNG ~0 byte | Richiedi a frame-extractor un frame a +/-2s; segnala "non leggibile" |
| Transcript assente | Solo visual, nessuna sincronia | yt_ingest scarica auto-subs; fallback a soli frame | ingest.json subs vuoto | Procedi con soli frame, dichiara la limitazione |
| Trace mancante (P12) | Atomi senza riferimento a frame/timestamp | Schema atoms.json obbligatorio con campo trace | coverage-controller conta atomi senza trace | Ri-emetti atoms con trace dal manifest |
| Video troppo lungo / troppi frame | Timeout, contesto saturo | Cap --max-frames; 1 per capitolo + intermedi; batch | durata > soglia | Riduci frame, processa per capitoli in piu' passaggi |
| Confonde capitoli | Frame attribuito al capitolo sbagliato | Usa start_time dei capitoli dal manifest | timestamp frame vs range capitolo | Ricalcola l'etichetta capitolo dal manifest |

Tutti i failure rilevati vengono loggati dal bug-error-tracker in `memory/bugs/`
o `memory/errors/` e il silent-observer ne tiene conto per il miglioramento.
