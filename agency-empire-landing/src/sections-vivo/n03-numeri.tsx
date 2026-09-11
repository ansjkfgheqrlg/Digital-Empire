import { FATTI } from "@/lib/fatti";

/* N3 — Tre numeri veri. Copy: COPY.md §N3. Sfondo ink, nessuna foto, nessuna CTA.
   Ogni cifra viene da FATTI (V8: zero numeri senza prova). */
const NUMERI = [
  {
    n: `${FATTI.giorniSetup} giorni`,
    t: `— lavorativi, dal contratto firmato al go-live. Se il tuo caso è su misura te lo diciamo prima di firmare, non dopo.`,
  },
  {
    n: `${FATTI.messaggiGiorno} al giorno`,
    t: `— messaggi che l'Outreach Factory manda da sola: email e DM Instagram, da sessioni browser vere. Non API che ti fanno bannare.`,
  },
  {
    n: `${FATTI.canoneMese} € al mese`,
    t: `— nessun canone. Il codice gira sul tuo server (${FATTI.vpsMeseMin}-${FATTI.vpsMeseMax} € al mese, tuo) ed è tuo. Se ci licenzi, resta lì.`,
  },
];

export function Numeri() {
  return (
    <section id="numeri" className="sv sv-ink sv-section" aria-labelledby="numeri-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">Tre numeri, tre prove</p>
        <h2 id="numeri-h2" className="sv-h2 mt-3">
          Quello che installiamo, <span className="sv-it" style={{ color: "var(--sv-silver)" }}>misurato.</span>
        </h2>
        <div className="mt-10 grid md:grid-cols-3 gap-6">
          {NUMERI.map((x) => (
            <div key={x.n} className="prova">
              <b className="sv-stat">{x.n}</b>
              <p className="sv-body sv-muted mt-2">{x.t}</p>
            </div>
          ))}
        </div>
        <p className="sv-small sv-muted mt-6">I numeri li vedi girare in chiamata, sul sistema vero, non su una slide.</p>
      </div>
    </section>
  );
}
