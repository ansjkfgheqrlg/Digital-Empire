# video-watcher - Evals (casi discriminanti)

Criterio trasversale: le descrizioni devono essere ANCORATE a frame reali e NON
generiche. Un output che dice "il video mostra una UI" senza dettagli specifici
e' un FAIL (e' esattamente cio' che faceva il watcher finto).

## EV-01 - Visione reale (happy)
- Input: run con 6+ frame estratti di un tutorial.
- Atteso: ogni voce della Visual Timeline cita frame+timestamp e descrive
  elementi SPECIFICI (testo leggibile, pulsanti, valori). >= 1 "key visual
  passage" che il transcript non contiene.
- Voto: PASS se 0 descrizioni generiche e ogni atomo ha trace. Target 9/10.

## EV-02 - No-finto (anti-allucinazione)
- Input: frame di un desktop generico senza Figma.
- Atteso: NON appare "Figma con 5 componenti". Descrive cio' che c'e' davvero.
  Inferenze marcate `➕`.
- Voto: FAIL se inventa contenuti non presenti nel frame.

## EV-03 - Sincronia testo/immagine
- Input: video con transcript + frame ai capitoli.
- Atteso: almeno un collegamento esplicito "a <ts> dice X mentre si vede Y".
- Voto: PASS se >= 1 sincronia corretta.

## EV-04 - Frame illeggibile (edge)
- Input: una run con un frame nero/transizione.
- Atteso: segnala "non leggibile", non inventa, eventuale richiesta di re-frame.
- Voto: FAIL se descrive un frame che non poteva vedere.

## EV-05 - Trace completa (P12)
- Input: qualunque run.
- Atteso: ogni atomo in atoms.json ha `trace: <id>#<ts> + frame-NNN.png` e flag
  `inferred`.
- Voto: PASS se 100% atomi tracciati.

## EV-06 - Video lungo (scala)
- Input: video > 30 min con capitoli.
- Atteso: frame >= 1 per capitolo, nessun capitolo saltato, analysis coerente.
- Voto: PASS se coverage capitoli >= 90%.

Benchmark vs baseline (solo transcript): il delta = i "key visual passages"
catturati, che la baseline non ha.
