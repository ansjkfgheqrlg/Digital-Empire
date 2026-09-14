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

          {/* AGGIUNTA F5 (ordine 3 di Max, 14/09 notte) — foto di riferimento (10) accanto al titolo, piccola, con
              freccia hairline (mai a contatto) verso una nota letterale. Solo aggiunta, nessuna riga esistente
              toccata. Testo nuovo in brief/COPY-F5-gamma.md §3. CSS: f5-frecce.css (.f5-rif-*). */}
          <div className="f5-rif-foto f5-rif-foto--pensa">
            <figure className="f5-rif-fig">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/foto/rif-pensa.jpg" width={736} height={736} alt="" loading="lazy" decoding="async" />
            </figure>
            <svg className="f5-rif-arrow-desktop" viewBox="0 0 46 30" preserveAspectRatio="none" aria-hidden="true" focusable="false">
              <defs>
                <marker id="f5-rif-punta-pensa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M2,3 C18,3 30,20 43,26" fill="none" stroke="#fb4604" strokeWidth="1.2" markerEnd="url(#f5-rif-punta-pensa)" />
            </svg>
            <svg className="f5-rif-arrow-mobile" viewBox="0 0 16 30" aria-hidden="true" focusable="false">
              <defs>
                <marker id="f5-rif-punta-pensa-m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M8,2 L8,26" fill="none" stroke="#fb4604" strokeWidth="1.2" markerEnd="url(#f5-rif-punta-pensa-m)" />
            </svg>
            <p className="f5-rif-nota">Sta facendo i conti. Li facciamo insieme qui sotto: 12 mesi, due colonne.</p>
          </div>

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
