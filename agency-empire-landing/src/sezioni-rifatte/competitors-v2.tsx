/* RIFATTA 07 — Competitors «Mentre leggi questa pagina» (BRIEF F3, blocco B; 39B §2 r.07).
   Sostituisce <Competitors /> in page.tsx (lo scambio lo fa Emperator). Il TESTO è copiato parola per parola
   da src/components/sections/competitors.tsx, nello stesso ordine di lettura (eyebrow → h2 → lead → 4 voci
   [titolo, etichetta, testo] → citazione → «→ E tu…» → chiusura). Cambia solo la forma: ink, lista a 2 colonne
   senza card (filetti hairline), «Stessi colli di bottiglia» non più tagliato, citazione in una riga serif,
   niente gradienti argento né testo sfumato, niente icone. Nessuna CTA (giugno non ne aveva). 0 KB di JS.
   Obiettivo ≤ 600 px. CSS: src/app/rifatte-b.css (.rb-cp*). */

const facts = [
  {
    big: "Stessi colli di bottiglia",
    label: "La maggior parte dei competitor",
    desc: "Condivide i tuoi stessi limiti operativi. Il primo che li risolve con l'AI guadagna un vantaggio difficile da recuperare.",
  },
  {
    big: "Adozione in crescita",
    label: "AI nel tuo settore",
    desc: "Sempre più aziende stanno integrando automazioni AI nei processi interni. Mentre tu leggi questa frase.",
  },
  {
    big: "Margine eroso",
    label: "Nel medio periodo",
    desc: "Chi non automatizza tende a erodere margine contro chi ha sistemi AI proprietari che lavorano h24. È una traiettoria, non un'opinione.",
  },
  {
    big: "Adesso",
    label: "La finestra per posizionarti",
    desc: "Posizionarti PRIMA che il mercato saturi è un vantaggio. Dopo, entri come commodity. La finestra si sta chiudendo.",
  },
];

export function CompetitorsV2() {
  return (
    <div className="vivo">
      <section id="competitor" className="sv sv-ink-piatto sv-section rb-cp" aria-labelledby="competitor-h2">
        <div className="sv-container">
          <header className="rb-cp-testa">
            <span className="sv-eyebrow"><b>La verità scomoda // Competitor</b></span>
            <h2 id="competitor-h2" className="sv-h2 mt-3">
              Mentre leggi questa pagina, <span className="sv-it rb-accento">un tuo competitor sta automatizzando.</span>
            </h2>
            <p className="sv-lead sv-muted rb-cp-lead">
              Non esiste mercato senza concorrenza. Esistono solo competitor visibili e competitor nascosti. E oggi i competitor che contano{" "}
              <strong>stanno installando sistemi AI proprietari</strong> mentre tu sei ancora a mandare DM a mano.
            </p>
          </header>

          <ul className="rb-cp-lista">
            {facts.map((f) => (
              <li key={f.big}>
                <h3>{f.big}</h3>
                <span className="sv-mono">{f.label}</span>
                <p>{f.desc}</p>
              </li>
            ))}
          </ul>

          <blockquote className="rb-cp-cit">
            <p className="sv-it">
              Il tuo competitor non ha bisogno di essere più bravo di te. Gli basta avere un sistema AI che <b>lavora mentre lui dorme</b>.
            </p>
            <p className="sv-mono rb-accento">→ E tu cosa stai facendo adesso?</p>
          </blockquote>

          <p className="rb-cp-coda sv-muted">
            Puoi ignorarlo. Oppure puoi diventare tu quel competitor che gli altri rincorrono.{" "}
            <span className="rb-cp-forte">La finestra è aperta per altri 12 mesi. Dopo è chiusa.</span>
          </p>
        </div>
      </section>
    </div>
  );
}
