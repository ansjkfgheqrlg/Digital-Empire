import { LISTINO, SAAS_ANNO, eur } from "@/lib/listino";

/* N7 — La scala: tre modi di fare la stessa cosa. Copy: COPY.md §N7.
   Sfondo carta, nessuna foto, nessuna CTA. Le due cifre del SaaS vengono dal listino,
   mai scritte a mano (gate grep prezzi). */
export function Scala() {
  return (
    <section id="scala" className="sv sv-carta sv-section" aria-labelledby="scala-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">Tre modi di fare la stessa cosa</p>
        <h2 id="scala-h2" className="sv-h2 mt-3">
          A mano, con un tool, <span className="sv-it" style={{ color: "var(--sv-orange)" }}>con un sistema tuo.</span>
        </h2>

        <div className="mt-10 grid md:grid-cols-3 gap-8">
          <div>
            <h3 className="sv-h3">A mano</h3>
            <p className="sv-body sv-muted mt-3">
              Trenta DM la mattina, un carosello il pomeriggio, il follow-up quando te lo ricordi. Funziona finché sei
              tu a farlo. Cioè finché hai tempo.
            </p>
          </div>
          <div>
            <h3 className="sv-h3">Con un tool (SaaS)</h3>
            <p className="sv-body sv-muted mt-3">
              Un abbonamento che non sa chi sei, un template uguale per tutti, un canone per sempre: {eur(LISTINO.saasMese)}{" "}
              al mese sono {eur(SAAS_ANNO)} l&apos;anno, e non è mai tuo.
            </p>
          </div>
          <div>
            <h3 className="sv-h3">Con un sistema tuo</h3>
            <p className="sv-body sv-muted mt-3">
              Costruito sul tuo processo, sui tuoi account, sul tuo server. Lo paghi una volta. Se ci licenzi, resta lì
              e continua a girare.
            </p>
          </div>
        </div>

        <p className="sv-lead mt-10">I tool si pagano. I sistemi si possiedono.</p>
      </div>
    </section>
  );
}
