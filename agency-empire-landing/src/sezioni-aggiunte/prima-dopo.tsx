import { LISTINO, SAAS_ANNO, eur } from "@/lib/listino";

/* AGGIUNTA A05 (Dossier 38 v2, Atto III) — Prima / dopo: la stessa cosa pagata in due modi.
   Inserita dopo <ListenUp />. h ≤ 700. Superficie ink, due colonne uguali.
   Sinistra: il canone barrato + una fattura RICOSTRUITA IN HTML e desaturata (grayscale) — non è lo screenshot di nessuno,
   e lo dice in didascalia. Destra: il prezzo una tantum + una pagina vera di un PDF PreventivoForge (pf-totale.webp,
   1191×1458, resa 380 px, §14: intera, mai cover, bordo arancione 1 px), intestazione del cliente ritagliata.
   Ogni cifra viene da LISTINO (§6/§8): saasMese, SAAS_ANNO, outreach. Nessuna CTA di vendita (§15: Atto III).
   Titolo della sezione: non è nel brief, è scritto qui in voce di casa e si può cambiare. CSS: aggiunte-a.css (.pd-*). */
const PDF_TOTALE = {
  src: "/aura/pf-totale.webp",
  width: 1191,
  height: 1458,
  alt: "Pagina del totale di un preventivo PDF generato dal nostro sistema PreventivoForge, con l'intestazione del cliente ritagliata.",
} as const;

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
              <div className="pd-fattura" aria-label="Fattura di un abbonamento, ricostruita in HTML">
                <span className="pd-timbro" aria-hidden="true">
                  ricorrente
                </span>
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

            {/* DOPO — il sistema tuo */}
            <div>
              <h3 className="pd-h4">
                {eur(LISTINO.outreach)} una volta. <span className="sv-it">Tuo.</span>
              </h3>
              <figure className="foto-intera pd-pdf" style={{ aspectRatio: `${PDF_TOTALE.width}/${PDF_TOTALE.height}` }}>
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={PDF_TOTALE.src}
                  width={PDF_TOTALE.width}
                  height={PDF_TOTALE.height}
                  alt={PDF_TOTALE.alt}
                  loading="lazy"
                  decoding="async"
                />
              </figure>
              <p className="foto-didascalia pd-did">PDF vero del nostro sistema · intestazione del cliente ritagliata</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
