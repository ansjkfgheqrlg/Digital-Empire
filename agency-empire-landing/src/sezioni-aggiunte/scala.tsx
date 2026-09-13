import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A07 (Dossier 38 v2, Atto III) — I sette passi, dalla chiamata al sistema che gira da solo.
   Inserita dopo <FlowFramework />. Superficie carta.
   Rifatta il 13/09 sera (BRIEF F3 blocco C, 39B §2 r.14): via la scaletta diagonale e il verde. Sette righe piatte allineate
   a sinistra (numero mono 11, titolo 17, riga 15), separatori hairline, solo l'ultima con il bordo accento. Altezza ≈ 520.
   HTML puro, testo selezionabile, 0 KB di JS. Ogni numero viene da FATTI (§6/§8): minutiChiamata, giorniSetup,
   giorniMonitoraggio. Nessuna CTA di vendita (§15: Atto III). Il titolo è in voce di casa e si può cambiare.
   CSS: aggiunte-a.css (.sc-*). */
const PASSI: { t: string; d: string; fine?: boolean }[] = [
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
      <section id="scala" className="sv sv-carta sv-section sc-sezione" aria-labelledby="scala-h2">
        <div className="sv-container">
          <p className="sv-eyebrow">Il percorso, passo per passo</p>
          <h2 id="scala-h2" className="sv-h2 sc-h2 mt-3 max-w-[22ch]">
            Sette passi. <span className="sv-it">Nell&apos;ordine in cui li facciamo.</span>
          </h2>

          <ol className="sc-righe" role="list" aria-label="I sette passi, dalla chiamata al sistema che gira da solo">
            {PASSI.map((p, i) => (
              <li key={p.t} className={`sc-riga${p.fine ? " sc-fine" : ""}`}>
                <span className="sc-n">{String(i + 1).padStart(2, "0")}</span>
                <b className="sc-t">{p.t}</b>
                <span className="sc-d">{p.d}</span>
              </li>
            ))}
          </ol>
        </div>
      </section>
    </div>
  );
}
