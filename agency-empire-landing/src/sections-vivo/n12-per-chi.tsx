import { Aura } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";

/**
 * N12 — Per chi lavoriamo / cosa non facciamo (COPY.md §N12). due-col--foto-sx: foto a sinistra,
 * testo a destra. Decisione: nel COPY nessuna delle voci [sì]/[no]/[nf] porta un grassetto, quindi
 * restano testo piatto — solo i tre titoli di lista usano sv-mono, come le etichette di sezione.
 */
const SI = [
  "Hai un'offerta che vende e l'operatività non tiene il passo",
  "Fai outreach a mano ogni giorno e vuoi smettere senza smettere di farlo",
  "Pubblichi quando riesci e vuoi pubblicare ogni giorno",
  "Vuoi crescere senza assumere altre persone per fare cose ripetitive",
  "Lavori da solo? Vale lo stesso: i 30 DM al giorno li mandi tu. Al posto del team, il collo di bottiglia sei tu.",
];

const NO = [
  "Stai ancora cercando cosa vendere: il sistema amplifica, non inventa",
  "Vuoi qualcuno che faccia le cose al posto tuo ogni giorno senza voler capire come funzionano",
  "Non sei disposto a mostrarci come lavori oggi: senza il contesto il sistema è cieco",
  "Cerchi la soluzione istantanea: sette giorni sono sette giorni",
];

const NON_FACCIAMO = [
  "Gestione social «chiavi in mano» ogni giorno al posto tuo",
  "Ads e media buying",
  "Sviluppo software generico su commessa",
  "Consulenza senza installare niente",
  "Promesse di fatturato",
];

export function PerChi() {
  return (
    <section id="per-chi" className="sv sv-ink sv-section" aria-labelledby="per-chi-h2">
      <div className="sv-container">
        <div className="due-col due-col--foto-sx">
          <Aura
            file="n12-per-chi.webp"
            alt="uomo in camicia a righe e bretelle, mani giunte, ufficio"
            riga="«Se vuoi delegare senza capire, non siamo noi. Sul serio.»"
          />

          <div>
            <h2 id="per-chi-h2" className="sv-h2 max-w-[20ch]">
              Lavoriamo solo con chi{" "}
              <span className="sv-it" style={{ color: "var(--sv-silver)" }}>
                ha già qualcosa che funziona.
              </span>
            </h2>

            <div className="mt-8 grid gap-8 md:grid-cols-2">
              <div>
                <p className="sv-mono" style={{ color: "var(--sv-orange)" }}>
                  È per te se
                </p>
                <ul className="mt-4 grid gap-3" style={{ listStyle: "none", margin: 0, padding: 0 }}>
                  {SI.map((t) => (
                    <li key={t} className="sv-check sv-body">
                      {t}
                    </li>
                  ))}
                </ul>
              </div>
              <div>
                <p className="sv-mono" style={{ color: "var(--sv-silver-dim)" }}>
                  Non è per te se
                </p>
                <ul className="mt-4 grid gap-3" style={{ listStyle: "none", margin: 0, padding: 0 }}>
                  {NO.map((t) => (
                    <li key={t} className="sv-x sv-body sv-muted">
                      {t}
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="mt-8">
              <p className="sv-mono" style={{ color: "var(--sv-silver-dim)" }}>
                Facciamo tre cose. Queste no.
              </p>
              <ul className="mt-4 grid gap-3" style={{ listStyle: "none", margin: 0, padding: 0 }}>
                {NON_FACCIAMO.map((t) => (
                  <li key={t} className="sv-x sv-body sv-muted">
                    {t}
                  </li>
                ))}
              </ul>
            </div>

            <CallCTA da="N12" label="Se sei nella prima colonna, prenota →" className="mt-8" />
          </div>
        </div>
      </div>
    </section>
  );
}
