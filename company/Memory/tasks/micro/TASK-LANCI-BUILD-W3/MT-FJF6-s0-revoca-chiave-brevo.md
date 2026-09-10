# MT-FJF6 — S0.0 - revocare la chiave Brevo sul servizio (mani umane)

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 1

## Cosa fa

Revocare **sul servizio Brevo** la chiave che e' in chiaro su repository pubblico
(B-020) ed emetterne una nuova. E' il gesto 0 di S0 in `04-COSTRUZIONE.md`, e ADR-025 lo
mette prima della cartella dell'ecosistema: *"e' l'unico gesto dell'intero piano che costa
meno di quanto costa rimandarlo di un giorno"*.

**Mani umane: serve l'accesso al pannello Brevo. Nessuna sessione puo' farlo.**

Attenzione, e questo cambia il lavoro rispetto a come e' scritto nel piano. La chiave non
e' solo su GitHub: sta a **riga 32 di `Landing Page/ccm-empire/src/app/page.tsx`** e la
chiamata parte dal **browser del visitatore** (`fetch` a `api.brevo.com` con header
`api-key`, righe 63-68). Quindi:

- toglierla dal repository non basta, perche' chi apre la landing la legge nel sorgente;
- **ruotarla non basta**, perche' la chiave nuova finisce nello stesso bundle e riparte
  esposta il giorno dopo.

Il rimedio completo e' spostare la chiamata **lato server** (funzione Netlify o route API)
e lasciare al browser solo il form. Sono 5 file, di cui `Landing Page/ccm-dist/index.html`
e' output di build e va rigenerato, non modificato a mano.

## Gate di chiusura

La vecchia chiave non risponde piu' **sul pannello Brevo**, e nessun file servito al browser contiene una chiave d'API.

## Output

## Stato

**Lato codice: chiuso il 2026-09-10** (CP-20260910-9VWK). Zero file di codice nel repository contengono ancora la chiave intera; la chiamata a Brevo passa da una funzione Netlify su tre siti, 18 casi di prova ciascuno.

**Resta aperta la parte umana, e senza quella B-020 non e' chiuso:** revocare la vecchia chiave sul pannello Brevo, impostare `BREVO_API_KEY` sui tre siti, ripubblicare.
