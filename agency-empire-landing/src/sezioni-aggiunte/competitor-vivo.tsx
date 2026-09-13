import { FATTI } from "@/lib/fatti";

/* AGGIUNTA D4 (ordine di Max, 13/09 — Dossier 38 v2 §I) — «Hai competitor e non lo sai», la voleva ad ogni costo.
   Inserita dopo <Competitors />. h ≤ 700.
   Parte alta: sv-fascia (l'unico fondo pieno arancione della pagina, §12), titolo con «competitor» in bianco, a destra il
   paragrafo separato da un filetto. Parte bassa: sv-ink a due colonne — la silhouette intera al suo rapporto (949×1178,
   resa 300 px, §14: mai cover, mai grana sulla foto) con la riga SOTTO l'immagine; a destra l'asse a tre punti in HTML
   («A mano» — «Tu, sei qui» che pulsa — «Automatizzato»), fermo con prefers-reduced-motion.
   I numeri della nota vengono da FATTI (§6/§8). Nessuna CTA di vendita (§15: Atto II). CSS: aggiunte-a.css. */
const SILHOUETTE = {
  src: "/aura/silhouette.webp",
  width: 949,
  height: 1178,
  alt: "Una figura di spalle, controluce, davanti alle finestre di un ufficio: non ha un volto, ha un sistema.",
} as const;

export function CompetitorVivo() {
  return (
    <div className="vivo">
      <section id="competitor-vivo" className="competitor-vivo" aria-labelledby="competitor-vivo-h2">
        <div className="sv sv-fascia cv-alto">
          <div className="sv-container cv-alto-grid">
            <h2 id="competitor-vivo-h2" className="sv-h2 cv-h2">
              Hai <span className="cv-bianco">competitor</span> e non lo sai.
            </h2>
            <p className="sv-lead cv-testo">
              Un competitor non è chi fa il tuo mestiere. È chi i tuoi clienti potrebbero scegliere al posto tuo — e oggi sta
              installando un sistema che risponde prima di te.
            </p>
          </div>
        </div>

        <div className="sv sv-ink cv-basso">
          <div className="sv-container cv-basso-grid">
            <div className="cv-fig-col">
              <figure className="foto-intera cv-sil" style={{ aspectRatio: `${SILHOUETTE.width}/${SILHOUETTE.height}` }}>
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={SILHOUETTE.src}
                  width={SILHOUETTE.width}
                  height={SILHOUETTE.height}
                  alt={SILHOUETTE.alt}
                  loading="lazy"
                  decoding="async"
                />
              </figure>
              <p className="cv-riga">
                Non ha un nome. Ha un sistema. <span className="sv-it">E ha i tuoi clienti.</span>
              </p>
            </div>

            <div>
              <p className="sv-eyebrow">Dove sei adesso</p>
              <h3 className="sv-h3 cv-h3 mt-3">
                Stessi limiti tuoi. <span className="sv-it">Il primo che li risolve non lo raggiungi più.</span>
              </h3>

              <div className="cv-asse" role="list" aria-label="Dove sei sull'asse: a mano, tu, automatizzato">
                <div role="listitem">
                  <span className="cv-punto" aria-hidden="true" />
                  A mano
                </div>
                <div role="listitem" className="cv-tu">
                  <span className="cv-punto cv-tu-punto" aria-hidden="true" />
                  <b className="cv-tu-nome">Tu</b>
                  <small className="cv-tu-qui">sei qui</small>
                </div>
                <div role="listitem" className="cv-av">
                  <span className="cv-punto" aria-hidden="true" />
                  Automatizzato
                </div>
              </div>

              <p className="sv-small sv-muted cv-nota">
                Il punto «Tu» viene dagli stessi numeri del rail: {FATTI.dmAMano} messaggi a mano contro {FATTI.messaggiGiorno} del
                sistema.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
