/**
 * Prova della funzione di iscrizione, senza rete e senza Brevo.
 *
 * PERCHE' ESISTE. Questa funzione e' l'unico posto in cui vive la chiave di
 * Brevo dopo B-020, ed e' anche l'unico punto in cui il sito raccoglie
 * contatti: se si rompe, il form smette di funzionare in silenzio e non se ne
 * accorge nessuno finche' non mancano gli iscritti. `node --check` dice solo
 * che il file e' JS valido, che non e' la stessa cosa.
 *
 *   node netlify/functions/iscrizione.test.mjs
 *
 * Esce 0 se passa tutto, 1 al primo caso fallito.
 */
import iscrizione from "./iscrizione.mjs";

let falliti = 0;
const fetchVero = globalThis.fetch;

function verifica(nome, condizione, dettaglio = "") {
  if (condizione) {
    console.log("  ok   " + nome);
  } else {
    console.log("  NO   " + nome + (dettaglio ? "  -> " + dettaglio : ""));
    falliti += 1;
  }
}

function richiesta(corpo, metodo = "POST") {
  return new Request("https://esempio.test/api/iscrizione", {
    method: metodo,
    headers: { "Content-Type": "application/json" },
    body: metodo === "POST" ? JSON.stringify(corpo) : undefined,
  });
}

/** Sostituisce fetch e registra come e' stata chiamata Brevo. */
function finto(risposta) {
  const chiamate = [];
  globalThis.fetch = async (url, opzioni) => {
    chiamate.push({ url, opzioni });
    return risposta;
  };
  return chiamate;
}

console.log("iscrizione.mjs");

// --- la chiave non e' configurata ------------------------------------------
delete process.env.BREVO_API_KEY;
{
  const r = await iscrizione(richiesta({ nome: "Max", email: "max@esempio.it" }));
  verifica("senza BREVO_API_KEY risponde 500 e non chiama Brevo", r.status === 500,
           "ha risposto " + r.status);
}

process.env.BREVO_API_KEY = "chiave-di-prova";

// --- validazione ------------------------------------------------------------
{
  const chiamate = finto(new Response("", { status: 201 }));
  const r = await iscrizione(richiesta({ nome: "", email: "max@esempio.it" }));
  verifica("nome vuoto -> 400", r.status === 400, "ha risposto " + r.status);
  verifica("nome vuoto non arriva mai a Brevo", chiamate.length === 0);
}
{
  const chiamate = finto(new Response("", { status: 201 }));
  const r = await iscrizione(richiesta({ nome: "Max", email: "non-una-email" }));
  verifica("email non valida -> 400", r.status === 400, "ha risposto " + r.status);
  verifica("email non valida non arriva mai a Brevo", chiamate.length === 0);
}
{
  // Chiunque puo' chiamare l'indirizzo senza passare dal form: il limite di
  // lunghezza e' qui, non nel browser.
  const r = await iscrizione(richiesta({ nome: "x".repeat(101), email: "max@esempio.it" }));
  verifica("nome lunghissimo -> 400", r.status === 400, "ha risposto " + r.status);
}
{
  const r = await iscrizione(richiesta({}, "GET"));
  verifica("GET -> 405", r.status === 405, "ha risposto " + r.status);
}

// --- il caso buono ----------------------------------------------------------
{
  const chiamate = finto(new Response("", { status: 201 }));
  const r = await iscrizione(richiesta({ nome: "Max", email: "max@esempio.it" }));
  verifica("iscrizione valida -> 200", r.status === 200, "ha risposto " + r.status);
  verifica("chiama Brevo una volta sola", chiamate.length === 1);

  const c = chiamate[0];
  verifica("chiama l'indirizzo giusto", c.url === "https://api.brevo.com/v3/contacts");
  verifica("manda la chiave nell'intestazione", c.opzioni.headers["api-key"] === "chiave-di-prova");

  const inviato = JSON.parse(c.opzioni.body);
  verifica("manda l'email", inviato.email === "max@esempio.it");
  verifica("manda il nome come FIRSTNAME", inviato.attributes.FIRSTNAME === "Max");
  verifica("manda la lista 3", Array.isArray(inviato.listIds) && inviato.listIds[0] === 3);
}
{
  // Brevo risponde 204 quando il contatto esiste gia': e' un successo.
  // Il corpo dev'essere null, non "": un 204 con corpo non e' costruibile.
  finto(new Response(null, { status: 204 }));
  const r = await iscrizione(richiesta({ nome: "Max", email: "max@esempio.it" }));
  verifica("204 di Brevo (contatto gia' presente) -> 200", r.status === 200,
           "ha risposto " + r.status);
}

// --- la chiave non deve mai uscire ------------------------------------------
{
  finto(new Response("chiave-di-prova non valida", { status: 401 }));
  const r = await iscrizione(richiesta({ nome: "Max", email: "max@esempio.it" }));
  const corpo = await r.text();
  verifica("errore di Brevo -> 500", r.status === 500, "ha risposto " + r.status);
  verifica("la chiave non finisce MAI nella risposta al browser",
           !corpo.includes("chiave-di-prova"), corpo);
}
{
  globalThis.fetch = async () => { throw new Error("rete giu'"); };
  const r = await iscrizione(richiesta({ nome: "Max", email: "max@esempio.it" }));
  verifica("Brevo irraggiungibile -> 500, non un'eccezione", r.status === 500);
}

globalThis.fetch = fetchVero;
console.log(falliti === 0 ? "\ntutti i casi passati" : "\n" + falliti + " casi falliti");
process.exit(falliti === 0 ? 0 : 1);
