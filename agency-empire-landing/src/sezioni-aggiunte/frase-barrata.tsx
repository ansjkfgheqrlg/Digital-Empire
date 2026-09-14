/* AGGIUNTA F3 (BRIEF F3 blocco C, 13/09 sera — 39A E21 «frase barrata + frase vera») — l'apertura del problema.
   Va montata subito PRIMA di <Specchio /> (dopo <Problems />). Superficie ink, h ≤ 320. 0 KB di JS.
   Un gesto tipografico, zero componenti: la credenza barrata (line-through accento 3 px, colore dim) e sotto la frase vera,
   bianca, a --fs-h2; sottotitolo a 17. Copy in voce di casa, senza numeri. Nessuna CTA (§15: Atto I-II).
   CSS: aggiunte-c.css (.fb-*). */
export function FraseBarrata() {
  return (
    <div className="vivo">
      <section id="frase-barrata" className="sv sv-ink fb" aria-labelledby="frase-barrata-h2">
        <div className="sv-container">
          <p className="fb-barrata">
            <s>Ti serve un altro tool.</s>
            <span className="fb-uguale">=</span>
            <span className="fb-ovvero">
              <b>Ovvero:</b> <span className="sv-it">è un processo lungo e ripetitivo</span>
            </span>
          </p>

          {/* AGGIUNTA F5 (ordine 3 di Max, 14/09 notte) — foto di riferimento (09/10) a destra della riga barrata,
              piccola, con freccia hairline (mai a contatto) verso una nota letterale. Solo aggiunta, nessuna riga
              esistente toccata. Testo nuovo in brief/COPY-F5-gamma.md §3. CSS: f5-frecce.css (.f5-rif-*). */}
          <div className="f5-rif-foto f5-rif-foto--smorfia">
            <figure className="f5-rif-fig">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/foto/rif-smorfia.jpg" width={735} height={648} alt="" loading="lazy" decoding="async" />
            </figure>
            <svg className="f5-rif-arrow-desktop" viewBox="0 0 46 30" preserveAspectRatio="none" aria-hidden="true" focusable="false">
              <defs>
                <marker id="f5-rif-punta-smorfia" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M2,3 C18,3 30,20 43,26" fill="none" stroke="#fb4604" strokeWidth="1.2" markerEnd="url(#f5-rif-punta-smorfia)" />
            </svg>
            <svg className="f5-rif-arrow-mobile" viewBox="0 0 16 30" aria-hidden="true" focusable="false">
              <defs>
                <marker id="f5-rif-punta-smorfia-m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M8,2 L8,26" fill="none" stroke="#fb4604" strokeWidth="1.2" markerEnd="url(#f5-rif-punta-smorfia-m)" />
            </svg>
            <p className="f5-rif-nota">La faccia di chi ha appena pagato il terzo abbonamento del mese.</p>
          </div>

          <h2 id="frase-barrata-h2" className="sv-h2 fb-vera">
            Ti serve un sistema che gira <span className="sv-it">senza di te.</span>
          </h2>
          <p className="fb-sotto">Il tool lo affitti. Il sistema lo possiedi.</p>
        </div>
      </section>
    </div>
  );
}
