import { FATTI } from "@/lib/fatti";
import { RITRATTI } from "@/lib/media";

/* AGGIUNTA A19 (Dossier 38 v2, Atto VI) — «Se non funziona»: la garanzia in una frase e una condizione, due quadri Se/Allora.
   Inserita dopo <MyPromise />. Superficie carta, h ≤ 600. 0 KB di JS.
   Colonna immagine: il ritratto RITRATTI.maxGaranzia se c'è (gesto di Max), altrimenti l'oggetto: elmo.webp intero a 280 px (§14, nativo 736×1308). */
const ELMO = { src: "/aura/elmo.webp", width: 736, height: 1308, alt: "Un elmo d'acciaio, di profilo, su fondo scuro" } as const;

export function SeNonFunziona() {
  const ritratto = RITRATTI.maxGaranzia;
  const img = ritratto ?? ELMO;
  const didascalia = ritratto ? null : "acciaio: la parola scritta vale come il metallo";
  return (
    <div className="vivo">
      <section id="se-non-funziona" className="sv sv-carta sv-section se-non-funziona" aria-labelledby="snf-h2">
        <div className="sv-container snf-grid">
          <div>
            <span className="sv-eyebrow">Garanzia · una frase, una condizione</span>
            <h2 id="snf-h2" className="sv-h2 mt-3 max-w-[18ch]">
              Funziona come scritto nel contratto, <span className="sv-it" style={{ color: "var(--sv-orange)" }}>o lo sistemiamo noi.</span>
            </h2>
            <div className="snf-quadri">
              <div className="snf-quadro c-grana c-grana--chiara">
                <span className="sv-eyebrow">Se</span>
                <p className="sv-body sv-muted">
                  un risultato scritto nel contratto — messaggi mandati, contenuti pubblicati, lead nel CRM — non arriva entro{" "}
                  {FATTI.giorniGaranzia} giorni dal go-live
                </p>
              </div>
              <div className="snf-quadro snf-quadro--allora c-grana c-grana--chiara">
                <span className="sv-eyebrow">Allora</span>
                <p className="sv-body sv-muted">
                  il lavoro per farlo arrivare è nostro e non costa niente. Se non è risolvibile: <b style={{ color: "#1c1c1c" }}>rimborso integrale.</b>
                </p>
              </div>
            </div>
          </div>

          <figure className="foto-intera snf-foto" style={{ aspectRatio: `${img.width}/${img.height}` }}>
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={img.src} width={img.width} height={img.height} alt={img.alt} loading="lazy" decoding="async" />
            {didascalia && <figcaption>{didascalia}</figcaption>}
          </figure>
        </div>
      </section>
    </div>
  );
}
