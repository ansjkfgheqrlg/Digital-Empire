import { FATTI } from "@/lib/fatti";
import { LISTINO, SAAS_ANNO, eur } from "@/lib/listino";

/* AGGIUNTA A05 (Dossier 38 v2, Atto III) — Prima / dopo: la stessa cosa pagata in due modi.
   Inserita dopo <ListenUp />. Superficie ink, due colonne uguali.
   Rifatta il 13/09 sera (BRIEF F3 blocco C, 39B §2 r.10): via il timbro; a destra, al posto del PDF (che resta nella 26),
   una seconda scheda HTML «4.000 € una volta» SIMMETRICA alla prima: Setup una volta / Canone 0 € / Proprietà del codice: tua /
   Totale a 12 mesi. Sinistra: la fattura dell'abbonamento, ricostruita in HTML e desaturata. Titolo con --fs-h2 (sv-h2).
   Ogni cifra viene da LISTINO/FATTI (§6/§8): saasMese, SAAS_ANNO, outreach, canoneMese. Nessuna CTA di vendita (§15: Atto III).
   CSS: aggiunte-a.css (.pd-*). Altezza ≈ 520 px. */
export function PrimaDopo() {
  return (
    <div className="vivo">
      <section id="prima-dopo" className="sv sv-ink pd-sezione" aria-labelledby="prima-dopo-h2">
        <div className="sv-container">
          <p className="sv-eyebrow">Prima / dopo</p>
          <h2 id="prima-dopo-h2" className="sv-h2 mt-3 max-w-[22ch]">
            La stessa cosa, <span className="sv-it" style={{ color: "var(--sv-orange)" }}>pagata in due modi.</span>
          </h2>

          <div className="pd-grid">
            {/* PRIMA — il canone */}
            <div>
              <h3 className="pd-h4">
                <span className="pd-barrato">{eur(LISTINO.saasMese)} al mese, per sempre</span>
              </h3>
              <div className="pd-foglio pd-fattura" aria-label="Fattura di un abbonamento, ricostruita in HTML">
                <div className="pd-int">
                  <b>Abbonamento outreach</b>
                  <span>Piano Pro</span>
                </div>
                <ul className="pd-righe">
                  <li>
                    <span>Canone mensile</span>
                    <span>{eur(LISTINO.saasMese)}</span>
                  </li>
                  <li>
                    <span>Rinnovo</span>
                    <span>automatico</span>
                  </li>
                  <li>
                    <span>Proprietà del codice</span>
                    <span>—</span>
                  </li>
                  <li className="pd-tot">
                    <span>Totale a 12 mesi</span>
                    <span>{eur(SAAS_ANNO)}</span>
                  </li>
                </ul>
              </div>
              <p className="foto-didascalia pd-did">ricostruita in HTML — non uno screenshot altrui</p>
            </div>

            {/* DOPO — il sistema tuo: la stessa scheda, con i nostri numeri */}
            <div>
              <h3 className="pd-h4">
                <span data-prezzo="outreach">{eur(LISTINO.outreach)}</span> una volta. <span className="sv-it">Tuo.</span>
              </h3>
              <div className="pd-foglio pd-scheda" aria-label="Il sistema pagato una volta, stessa scheda">
                <div className="pd-int">
                  <b>Sistema outreach</b>
                  <span>Codice tuo</span>
                </div>
                <ul className="pd-righe">
                  <li>
                    <span>Setup, una volta</span>
                    <span data-prezzo="outreach">{eur(LISTINO.outreach)}</span>
                  </li>
                  <li>
                    <span>Canone</span>
                    <span>{eur(FATTI.canoneMese)}</span>
                  </li>
                  <li>
                    <span>Proprietà del codice</span>
                    <span>tua</span>
                  </li>
                  <li className="pd-tot">
                    <span>Totale a 12 mesi</span>
                    <span data-prezzo="outreach">{eur(LISTINO.outreach)}</span>
                  </li>
                </ul>
              </div>
              <p className="foto-didascalia pd-did">stessa scheda, i numeri del listino — niente canoni dopo</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
