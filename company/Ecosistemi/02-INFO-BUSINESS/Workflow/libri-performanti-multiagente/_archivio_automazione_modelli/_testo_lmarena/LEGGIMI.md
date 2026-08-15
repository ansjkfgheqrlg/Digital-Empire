# Archivio — scrittura del testo via LM Arena (non più in uso)

**Archiviato il 2026-08-10. Non cancellato: è codice funzionante, solo su una strada
che si è rivelata sbagliata.**

## Cosa c'è qui

`book_writer.py` — generava outline e capitoli pilotando LM Arena con Playwright.

## Perché non si usa più

Due giorni di lavoro reale hanno dimostrato che LM Arena non regge una generazione lunga
in serie: il captcha "Security Verification" scatta dopo poche richieste per sessione,
anche con profilo persistente, chat nuove e pause fra gli invii. Un libro ne richiede 24+.
Non è aggirabile e non va aggirato — è un controllo di sicurezza.

La cronaca completa (con i bug veri trovati e risolti lungo la strada) è in
[PIANO-KDP-67.md](../PIANO-KDP-67.md) e nei checkpoint CP-20260806-003 / CP-20260807-001.

## Cosa si usa al suo posto

I capitoli li scrive Claude in sessione seguendo [SOP-SCRIVERE-UN-LIBRO.md](../SOP-SCRIVERE-UN-LIBRO.md),
salvandoli come file; `engine/book_project.py` fa da ponte verso il motore di
impaginazione. Zero costi esterni, zero captcha.

## Cosa NON è archiviato (e funziona benissimo)

`engine/lmarena_client.py` e `engine/cover_generator.py` restano in uso **per le
copertine**: lì LM Arena fa una sola richiesta per libro e non ha mai dato problemi.
Il codice qui archiviato importa `lmarena_client`, quindi non gira più così com'è: se un
giorno servisse, va riadattato.
