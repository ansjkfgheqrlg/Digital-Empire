# Playbook — op-translator-copy

## Flusso standard
1. Verifica che `listing.json` esista e sia valido (Gate A già passato).
2. Esegui `translate(ctx, dealer)`.
3. Ispeziona il log: n. optional tradotti, n. specs, warning residui tedeschi.
4. Se il warning segnala residui → apri `glossary_de_it.py`, aggiungi i termini, ri-esegui.
5. Consegna a S4 (pricing) → poi Gate B verifica.

## Come tradurre un optional nuovo
1. Cerca il termine su un annuncio reale mobile.de (forma esatta, con umlaut).
2. Aggiungi a `PHRASES` se è composto (es. `"adaptiver tempomat": "cruise control adattivo"`),
   a `WORDS` se singola parola.
3. Preferisci sempre la voce PHRASES per i termini composti (match prioritario).

## Esempio (BMW 320d)
IN `equipment_de`: `["LED-Scheinwerfer", "Standheizung", "Anhaengerkupplung", ...]`
OUT `equipment_it`: `["Fari LED", "Riscaldamento autonomo", "Gancio traino", ...]`
`title_it`: "BMW 320d Touring xDrive M Sport" · `description_it`: composta dai fatti.

## Quando fermarsi / escalation
- Gate B rosso per residui dopo 2 estensioni del glossario → segnala a Gael (termine ambiguo).
- Se `description_de` richiede davvero traduzione di prosa libera e la fedeltà è critica →
  valutare con Max l'attivazione del backend LLM (spesa) — mai di iniziativa.
