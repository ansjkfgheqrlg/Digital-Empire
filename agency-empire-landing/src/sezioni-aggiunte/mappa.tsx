/* AGGIUNTA A16 (Dossier 38 v2, Atto V) — «La mappa»: dove sta l'agency dentro Digital Empire.
   Inserita dopo <DietroLeQuinte />. Superficie ink. 0 KB di JS.
   Rifatta il 13/09 sera (BRIEF F3 blocco C, 39B §2 r.34): via l'organigramma con i box e il pill che copriva l'angolo.
   Una riga sola: «Digital Empire → Agency · Formazione · SaaS», Agency in bianco con il punto accento e «sei qui» in mono.
   Testo selezionabile, nessun href (mai un dominio del corso: contatti.ts). Altezza ≤ 200 px. CSS: aggiunte-c.css (.mappa-*). */
export function Mappa() {
  return (
    <div className="vivo">
      <section id="mappa" className="sv sv-ink mappa" aria-label="La mappa: dove sei dentro Digital Empire">
        <div className="sv-container">
          <p className="mappa-riga">
            <span className="mappa-radice">Digital Empire</span>
            <span className="mappa-freccia" aria-hidden="true">
              →
            </span>
            <span className="mappa-qui" aria-current="location">
              <i className="mappa-punto" aria-hidden="true" />
              <b>Agency</b>
              <small className="sv-mono">sei qui</small>
            </span>
            <span className="mappa-sep" aria-hidden="true">
              ·
            </span>
            <span className="mappa-ramo">Formazione</span>
            <span className="mappa-sep" aria-hidden="true">
              ·
            </span>
            <span className="mappa-ramo">SaaS</span>
          </p>
        </div>
      </section>
    </div>
  );
}
