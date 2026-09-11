import { Aura } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";

/**
 * N15 — Garanzia (COPY.md §N15). due-col standard (non foto-sx): testo a sinistra, l'elmo a destra
 * in trattamento "acciaio". I giorni di garanzia vengono da FATTI.giorniGaranzia, mai da un
 * letterale — "5 giorni" e "20 domande" restano testo piatto: sono l'esempio negativo retorico
 * dell'obiezione, non un fatto dell'azienda.
 */
export function Garanzia() {
  return (
    <section id="garanzia" className="sv sv-carta sv-section" aria-labelledby="garanzia-h2">
      <div className="sv-container">
        <div className="due-col">
          <div>
            <p className="sv-eyebrow">
              <b>Garanzia</b> · una frase, una condizione
            </p>
            <h2 id="garanzia-h2" className="sv-h2 mt-3 max-w-[18ch]">
              Funziona come scritto nel contratto,{" "}
              <span className="sv-it" style={{ color: "var(--sv-orange)" }}>
                o lo sistemiamo noi.
              </span>
            </h2>
            <p className="sv-body sv-muted mt-5 max-w-[52ch]">
              {FATTI.giorniGaranzia} giorni di monitoraggio dopo il go-live, dashboard aperta, alert automatici. Se
              un risultato scritto nel contratto — messaggi mandati, contenuti pubblicati, lead nel CRM — non
              arriva, il lavoro per farlo arrivare è nostro e non costa niente. Se non è risolvibile, rimborso
              integrale. Senza «dammi altri 5 giorni», senza questionari da 20 domande.
            </p>
            <p className="sv-small mt-4">Ti garantiamo che funziona come scritto. Chi ti garantisce i clienti, diffidane.</p>
            <CallCTA da="N15" label="Va bene, vediamolo →" className="mt-8" />
          </div>

          <Aura
            file="n15-garanzia.webp"
            alt="elmo da cavaliere medievale, visiera, luce laterale"
            riga={`«Se il sistema non gira come scritto, lo rifacciamo. Non "ti richiamiamo".»`}
            tratt="acciaio"
          />
        </div>
      </div>
    </section>
  );
}
