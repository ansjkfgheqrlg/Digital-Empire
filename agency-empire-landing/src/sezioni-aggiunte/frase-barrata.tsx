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
          <h2 id="frase-barrata-h2" className="sv-h2 fb-vera">
            Ti serve un sistema che gira <span className="sv-it">senza di te.</span>
          </h2>
          <p className="fb-sotto">Il tool lo affitti. Il sistema lo possiedi.</p>
        </div>
      </section>
    </div>
  );
}
