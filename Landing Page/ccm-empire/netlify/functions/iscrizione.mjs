/**
 * iscrizione - l'iscrizione alla lista passa di qui, e la chiave resta qui.
 *
 * PERCHE' ESISTE (B-020, 2026-09-09). Fino a oggi il form chiamava
 * `api.brevo.com` direttamente dal browser, con la chiave scritta a riga 32 di
 * `src/app/page.tsx`. Una chiave in un bundle servito al pubblico non e' un
 * segreto: chiunque apra la pagina la legge nel sorgente. Il repository
 * pubblico era il secondo canale, non il primo, ed e' per questo che
 * *ruotarla* non bastava: la chiave nuova sarebbe tornata nello stesso bundle
 * il giorno dopo.
 *
 * Qui invece la chiave si legge da `process.env.BREVO_API_KEY`, che su Netlify
 * si imposta nel pannello (Site settings -> Environment variables) e non entra
 * mai nel codice ne' nel repository. Il browser manda solo nome ed email.
 *
 * Il sito e' un export statico (`output: "export"` in next.config.ts), quindi
 * una route API di Next non esiste: il posto giusto e' una funzione Netlify,
 * che gira accanto ai file statici.
 *
 * Risposte: 200 iscritto, 400 dati non validi, 500 errore nostro o di Brevo.
 * Il corpo non riporta mai il messaggio grezzo del fornitore: finirebbe in una
 * pagina pubblica.
 */

const LIST_ID = 3;
const GUIDA = "Claude Code Mastery";
const RE_EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function risposta(codice, corpo) {
  return new Response(JSON.stringify(corpo), {
    status: codice,
    headers: { "Content-Type": "application/json" },
  });
}

export default async (request) => {
  if (request.method !== "POST") {
    return risposta(405, { errore: "metodo non ammesso" });
  }

  // La chiave manca -> si fallisce subito e si dice quale variabile manca nei
  // log, invece di chiamare Brevo senza credenziale e ricevere un 401 che nel
  // browser sembra "errore di connessione".
  const chiave = process.env.BREVO_API_KEY;
  if (!chiave) {
    console.error(
      "BREVO_API_KEY non impostata: impostala nelle variabili d'ambiente del sito."
    );
    return risposta(500, { errore: "servizio non configurato" });
  }

  let dati;
  try {
    dati = await request.json();
  } catch {
    return risposta(400, { errore: "corpo non valido" });
  }

  const nome = String(dati?.nome ?? "").trim();
  const email = String(dati?.email ?? "").trim();

  // Si valida anche qui, non solo nel browser: la validazione del browser e'
  // una cortesia verso chi compila, non un controllo - chiunque puo' chiamare
  // questo indirizzo senza passare dal form.
  if (!nome) return risposta(400, { errore: "nome mancante" });
  if (!RE_EMAIL.test(email)) return risposta(400, { errore: "email non valida" });
  if (nome.length > 100 || email.length > 200) {
    return risposta(400, { errore: "dati troppo lunghi" });
  }

  let esito;
  try {
    esito = await fetch("https://api.brevo.com/v3/contacts", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "api-key": chiave,
      },
      body: JSON.stringify({
        email,
        attributes: { FIRSTNAME: nome, SELECTED_GUIDE: GUIDA },
        listIds: [LIST_ID],
        updateEnabled: true,
      }),
    });
  } catch (e) {
    console.error("Brevo non raggiungibile:", e);
    return risposta(500, { errore: "servizio non raggiungibile" });
  }

  if (esito.ok || esito.status === 204) {
    return risposta(200, { ok: true });
  }

  // Il dettaglio va nei log del sito, dove lo legge chi ci lavora. Al browser
  // torna solo che non ha funzionato.
  console.error("Brevo ha risposto", esito.status, await esito.text());
  return risposta(500, { errore: "iscrizione non riuscita" });
};

export const config = { path: "/api/iscrizione" };
