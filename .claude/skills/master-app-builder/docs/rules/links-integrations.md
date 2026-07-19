# Regole — Collegamenti, navigazione e integrazioni

1. Ogni link ha destinazione, testo descrittivo e comportamento prevedibile; non usare “clicca qui” senza contesto.
2. I link esterni sono riconoscibili; aprire una nuova finestra solo se necessario e dichiararlo in modo accessibile.
3. Controlla regolarmente link rotti, redirect, anchor e deep link dei flussi core.
4. Link o URL generati da utenti devono essere validati/sanitizzati. Non usare redirect aperti.
5. Le integrazioni esterne hanno owner, contratto/versione, timeout, retry, fallback, limiti quota e monitoraggio.
6. Webhook e callback verificano firma/autenticità, idempotenza e replay protection.
7. API e UI non devono dipendere da URL o schema di terze parti non documentati in `docs/references/` e `docs/memory/architecture_map.md`.
8. Ogni integrazione critica ha un test di contratto e una procedura di degrado.
