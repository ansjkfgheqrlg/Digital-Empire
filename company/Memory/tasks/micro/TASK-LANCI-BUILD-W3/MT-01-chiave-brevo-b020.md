# MT-01 — Sostituire la chiave Brevo esposta (B-020, gesto 0 di S0)

- **Padre:** TASK-LANCI-BUILD-W3
- **Onda:** 1
- **Stato:** APERTA
- **Data:** 2026-09-08
- **Dipende da:** —
- **Scope (percorsi che tocca — controllo di sovrapposizione):**
  - Crea siti/Siti CCM/index.html
  - Lancio corso skill beast/Leanding Page CCM/index.html
  - Lancio corso skill beast/Sale pag/Siti CCM/icro-empire/src/components/optin-form.tsx

## Cosa fa

È il gesto 0 di S0 (`04-COSTRUZIONE.md`), e per ADR-025 viene prima di ogni altra riga di
codice: la chiave Brevo (`xkeysib-1b440a32…`, form opt-in newsletter) è in chiaro su repo
**pubblico** dal commit iniziale (B-020 in `BACKLOG.md`).

1. Revocare e rigenerare la chiave su Brevo (dashboard account).
2. Spostarla in `.env` (già gitignorato) nei 3 file dello scope.
3. Decidere se il form deve chiamare un endpoint server invece di esporre la chiave in JS
   client-side — una chiave Brevo dà accesso all'intero account, non solo alla lista.
4. Verificare che la vecchia chiave, ancora leggibile nella storia git pubblica, **non
   funzioni più sul servizio** (è il segnale di chiusura, non la rimozione dal codice).

## Gate di chiusura

La vecchia chiave restituisce un errore di autenticazione se interrogata su Brevo. I 3 file
dello scope non contengono più la chiave in chiaro. B-020 chiuso in `BACKLOG.md`.

## Output

Chiave nuova in `.env`, 3 file aggiornati, B-020 chiuso.
