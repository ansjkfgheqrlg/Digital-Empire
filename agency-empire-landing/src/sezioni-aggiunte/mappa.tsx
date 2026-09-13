/* AGGIUNTA A16 (Dossier 38 v2, Atto V) — «La mappa»: l'albero di Digital Empire in HTML puro.
   Inserita dopo <DietroLeQuinte />. Superficie ink, h ≤ 600. 0 KB di JS.
   Radice «✦ Digital Empire», connettori tratteggiati, tre rami: Agency (bordo arancione, etichetta «◉ Tu sei qui» che sale e scende),
   Formazione, SaaS. Testo selezionabile, nessun href esterno (mai un dominio del corso: contatti.ts). */
const RAMI: { nome: string; qui?: boolean }[] = [
  { nome: "Agency", qui: true },
  { nome: "Formazione" },
  { nome: "SaaS" },
];

export function Mappa() {
  return (
    <div className="vivo">
      <section id="mappa" className="sv sv-ink sv-section mappa" aria-labelledby="mappa-h2">
        <div className="sv-container">
          <span className="sv-eyebrow">La mappa</span>
          <h2 id="mappa-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Tre rami. <span className="sv-it">Tu sei qui.</span>
          </h2>
          <div className="mappa-albero">
            <p className="mappa-radice m-0">
              <i aria-hidden="true">✦</i> Digital Empire
            </p>
            <span className="mappa-fusto" aria-hidden="true" />
            <ul className="mappa-rami">
              {RAMI.map((r) => (
                <li key={r.nome} className="mappa-ramo">
                  <div className={`mappa-card c-grana${r.qui ? " mappa-card--qui" : ""}`} aria-current={r.qui ? "location" : undefined}>
                    {r.qui && (
                      <span className="mappa-qui">
                        <span aria-hidden="true">◉</span> Tu sei qui
                      </span>
                    )}
                    <b>{r.nome}</b>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
}
