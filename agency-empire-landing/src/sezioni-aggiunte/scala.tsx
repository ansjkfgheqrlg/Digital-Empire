import type { CSSProperties } from "react";
import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A07 (Dossier 38 v2, Atto III) — La scala a 7 gradini: dalla chiamata al sistema che gira da solo.
   Inserita dopo <FlowFramework />. h ≤ 900. Superficie carta.
   Sette card bianche sfalsate (raggio 24, bordo, connettori tratteggiati a gomito in ::before), l'ultima verde #2d7a4f:
   l'unico verde della pagina. Meccanismo in HTML puro, testo selezionabile, 0 KB di JS. Su mobile in colonna, senza
   sfalsamento, con il connettore verticale. Ogni numero viene da FATTI (§6/§8): minutiChiamata, giorniSetup,
   giorniMonitoraggio. Nessuna CTA di vendita (§15: Atto III). Titolo: non è nel brief, è in voce di casa e si può cambiare.
   CSS: aggiunte-a.css (.sc-*). */
const GRADINI: { t: string; d: string; fine?: boolean }[] = [
  { t: "Chiamata", d: `${FATTI.minutiChiamata} minuti: vedi il sistema che gira` },
  { t: "Proposta", d: "prezzo esatto, scritto" },
  { t: "Contratto", d: "cosa fa il sistema, entro quando" },
  { t: "Setup", d: `${FATTI.giorniSetup} giorni sul tuo server` },
  { t: "Go-live", d: "i primi messaggi veri davanti a te" },
  { t: `${FATTI.giorniMonitoraggio} giorni di guardia`, d: "dashboard aperta, alert, correzioni" },
  { t: "Gira da solo", d: "codice tuo. Per sempre.", fine: true },
];

export function Scala() {
  return (
    <div className="vivo">
      <section id="scala" className="sv sv-carta sv-section" aria-labelledby="scala-h2">
        <div className="sv-container">
          <p className="sv-eyebrow">Come si arriva al sistema</p>
          <h2 id="scala-h2" className="sv-h2 sc-h2 mt-3 max-w-[20ch]">
            Sette gradini. <span className="sv-it">Poi gira da solo.</span>
          </h2>

          <ol className="sc-scala" aria-label="I sette passi, dalla chiamata al sistema che gira da solo">
            {GRADINI.map((g, i) => (
              <li
                key={g.t}
                className={`sc-gradino${g.fine ? " sc-fine" : ""}`}
                style={{ ["--i" as string]: i } as CSSProperties}
              >
                <span className="sc-n">{String(i + 1).padStart(2, "0")}</span>
                <b className="sc-t">{g.t}</b>
                <span className="sc-d">{g.d}</span>
              </li>
            ))}
          </ol>
        </div>
      </section>
    </div>
  );
}
