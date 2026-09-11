import { Aura } from "@/components/vivo/aura";
import { FATTI } from "@/lib/fatti";
import { LISTINO, eur } from "@/lib/listino";

/* N16 — Le sei obiezioni «No.» (V4, V7). Copy: COPY.md §N16. */
const OBIEZIONI: { q: string; r: "No." | "Giusto."; a: React.ReactNode }[] = [
  {
    q: "Quindi c'è un canone mensile.",
    r: "No.",
    a: <>Il codice è tuo. Il server è tuo ({FATTI.vpsMeseMin}-{FATTI.vpsMeseMax} € al mese, a te). Fai tu il conto: 12 × quello che paghi oggi al tool che non sa chi sei, per ogni anno che lo tieni.</>,
  },
  {
    q: "Costa troppo per quello che fa.",
    r: "No.",
    a: <>Un Outreach Factory da <span data-prezzo="outreach">{eur(LISTINO.outreach)}</span> manda {FATTI.messaggiGiorno} messaggi al giorno per anni. Fai tu il conto: quante ore al mese passi a fare outreach a mano, per il tuo costo orario.</>,
  },
  {
    q: "Ho già provato gli strumenti AI, non funzionano.",
    r: "Giusto.",
    a: <>Gli strumenti da soli sono tab aperti. Quello che manca è la logica che li fa lavorare insieme, i trigger, la gestione degli errori. È quello che costruiamo. Lo strumento non è il sistema.</>,
  },
  {
    q: "Poi dipendo da voi per sempre.",
    r: "No.",
    a: <>Siamo l&apos;agenzia progettata per essere licenziata: {FATTI.giorniSupporto} giorni di supporto, poi cammini da solo. Se ci richiami è perché vuoi il secondo sistema, non perché il primo si è rotto.</>,
  },
  {
    q: "Non vi conosco abbastanza per fidarmi.",
    r: "Giusto.",
    a: <>Per questo la prima chiamata è il sistema in live, non una presentazione. Niente slide. Niente demo finta. Niente «ti richiamiamo». Trenta minuti, e decidi con quello che hai visto.</>,
  },
  {
    q: "ChatGPT lo faccio da solo.",
    r: "No.",
    a: <>Una chat risponde a domande. Un sistema apre un browser, manda {FATTI.messaggiGiorno} messaggi al giorno con il tuo account, fa i follow-up e ti mette i lead nel CRM. Un utente ChatGPT manda ancora i messaggi a mano, uno alla volta.</>,
  },
];

export function Obiezioni() {
  return (
    <section id="obiezioni" className="sv sv-ink sv-section" aria-labelledby="obiezioni-h2">
      <div className="sv-container">
        <div className="due-col due-col--foto-sx">
          <Aura file="n16-obiezioni.webp" alt="Uomo in maglione scuro, sguardo dritto, fondo nero" riga="Ci licenzi quando vuoi. Il codice resta tuo. Ciao." />
          <div>
            <h2 id="obiezioni-h2" className="sv-h2 max-w-[16ch]">
              Le sei cose che stai pensando. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>In ordine.</span>
            </h2>
            <ol className="mt-8 space-y-6 max-w-[60ch]">
              {OBIEZIONI.map((o) => (
                <li key={o.q}>
                  <p className="sv-body" style={{ color: "var(--sv-silver)" }}>«{o.q}»</p>
                  <p className="sv-body sv-muted mt-1">
                    <b className="text-white" style={o.r === "No." ? { color: "var(--sv-orange)" } : undefined}>{o.r}</b> {o.a}
                  </p>
                </li>
              ))}
            </ol>
          </div>
        </div>
      </div>
    </section>
  );
}
