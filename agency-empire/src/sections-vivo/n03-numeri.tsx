/* N3 — Tre numeri, tre prove. Copy: COPY-V2 §N3. Nessun numero senza prova (V8):
   7 giorni, 300/giorno, 0 € sono i tre che stanno sul disco. */
const NUMERI = [
  {
    n: "7 giorni",
    t: "dal briefing al go-live delle due fabbriche standard. Su misura: 3-4 settimane, e te lo diciamo prima.",
  },
  {
    n: "300 / giorno",
    t: "messaggi che l'Outreach Factory manda da sola: email, DM Instagram, WhatsApp. Sessioni browser vere, non API che ti bannano.",
  },
  {
    n: "0 € al mese",
    t: "nessun canone. Il codice gira sui tuoi server ed è tuo. Se ci licenzi, resta lì.",
  },
];

export function Numeri() {
  return (
    <section id="numeri" className="sv sv-ink-piatto sv-hair" aria-labelledby="numeri-h2">
      <div className="container-default py-14 md:py-16">
        <p className="sv-eyebrow">Tre numeri, tre prove</p>
        <h2 id="numeri-h2" className="sv-h2 mt-3">
          Quello che installiamo, <span className="sv-it" style={{ color: "var(--sv-silver)" }}>misurato.</span>
        </h2>
        <div className="mt-10 grid md:grid-cols-3 gap-px" style={{ background: "var(--sv-hair)" }}>
          {NUMERI.map((x) => (
            <div key={x.n} className="p-6 md:p-7" style={{ background: "var(--sv-ink)" }}>
              <div className="sv-stat" style={{ color: "#fff" }}>{x.n}</div>
              <p className="sv-body sv-muted mt-3 max-w-[34ch]">{x.t}</p>
            </div>
          ))}
        </div>
        <p className="sv-small sv-muted mt-5">I numeri li vedi girare in chiamata, sul sistema vero, non su una slide.</p>
      </div>
    </section>
  );
}
