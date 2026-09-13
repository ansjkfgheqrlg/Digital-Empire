import { FATTI } from "@/lib/fatti";

/* AGGIUNTA F3 (BRIEF F3 blocco C, 13/09 sera — 39A E06 «griglia 01-04 in mono con colonna accesa») — il meccanismo in quattro passi.
   Va montata DOPO <Pillars />. Superficie ink, h ≤ 420. 0 KB di JS.
   Quattro colonne uguali separate da filetti, numero mono in alto, filetto, titolo, una riga; UNA sola colonna accesa e fissa
   (l'ultima: bordo accento + velo + grana locale). Numeri da FATTI (§6/§8): minutiChiamata, giorniSetup, messaggiGiorno.
   Nessuna CTA (§15: Atto II). Mobile 2×2. CSS: aggiunte-c.css (.g4-*). */
const PASSI: { n: string; t: string; d: string; acceso?: boolean }[] = [
  { n: "01", t: "Chiamata", d: `${FATTI.minutiChiamata} minuti, il sistema in live` },
  { n: "02", t: "Setup", d: `${FATTI.giorniSetup} giorni sul tuo server` },
  { n: "03", t: "Go-live", d: "i primi messaggi veri davanti a te" },
  { n: "04", t: "Gira da solo", d: `${FATTI.messaggiGiorno} al giorno, codice tuo`, acceso: true },
];

export function Griglia0104() {
  return (
    <div className="vivo">
      <section id="griglia-01-04" className="sv sv-ink g4" aria-labelledby="griglia-01-04-h2">
        <div className="sv-container">
          <p className="sv-eyebrow">Come si arriva al sistema</p>
          <h2 id="griglia-01-04-h2" className="sv-h2 mt-3 max-w-[20ch]">
            Quattro passi. <span className="sv-it">Poi gira da solo.</span>
          </h2>

          <ol className="g4-griglia" role="list" aria-label="I quattro passi, dalla chiamata al sistema che gira da solo">
            {PASSI.map((p) => (
              <li key={p.n} className={`g4-col${p.acceso ? " g4-col--accesa c-grana" : ""}`} aria-current={p.acceso ? "step" : undefined}>
                <span className="g4-n">{p.n}</span>
                <b className="g4-t">{p.t}</b>
                <span className="g4-d">{p.d}</span>
              </li>
            ))}
          </ol>
        </div>
      </section>
    </div>
  );
}
