import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A10+A20 (Dossier 38 v2, Atto III) — «Due tipi di aziende» + «Le domande che non ci fate».
   Inserita dopo <ContentOutput />. Carta. Card gemelle (numero 81 px grigio chiaro; la seconda, quella giusta,
   col bordo arancione 2 px), poi filetto e tre domande ostili con risposta in una frase.
   Nessuna CTA di vendita: siamo sopra metà pagina (§15). Numeri solo da FATTI (§6/§8). 0 KB di JS.
   CSS: src/app/aggiunte-b.css (.dt-*). Grana locale sulle card (.gb-grana), mai sulle foto (qui non ce ne sono). */

const TIPI: { n: string; titolo: string; testo: string; giusta: boolean }[] = [
  {
    n: "1",
    titolo: "Chi affitta un tool",
    testo: "Paga ogni mese un abbonamento che non sa chi è. Se smette, sparisce tutto. Resta in affitto.",
    giusta: false,
  },
  {
    n: "2",
    titolo: "Chi possiede il sistema",
    testo: "Lo paga una volta. Gira sui suoi account, sul suo server. Se ci licenzia, resta lì e continua a girare.",
    giusta: true,
  },
];

const DOMANDE: [string, string][] = [
  [
    "Se funziona così bene, perché non lo tenete per voi?",
    "Lo teniamo: è l'Outreach Factory con cui probabilmente ti abbiamo trovato. Ne costruiamo altri perché il mestiere è quello.",
  ],
  [
    "Perché la chiamata è gratis?",
    `Perché in ${FATTI.minutiChiamata} minuti capiamo entrambi se il sistema ti serve. Se no, hai perso un caffè.`,
  ],
  [
    "Cosa ci guadagnate?",
    "Il prezzo scritto nel contratto, una volta. Niente canoni: non abbiamo interesse a tenerti in ostaggio.",
  ],
];

export function DueTipi() {
  return (
    <div className="vivo">
      <section id="due-tipi" className="sv sv-carta sv-section" aria-labelledby="due-tipi-h2">
        {/* F4 E2 — sfondo grana-fuoco di Max, layer assoluto z-index:0, mai la sezione resta "carta" */}
        <div className="dt-sfondo" aria-hidden="true" />
        <div className="sv-container">
          <h2 id="due-tipi-h2" className="sv-h2 max-w-[16ch]">
            Due tipi di aziende.
          </h2>

          <div className="dt-gemelle">
            {TIPI.map((t) => (
              <article key={t.n} className={`dt-card gb-grana${t.giusta ? " dt-card--giusta" : ""}`}>
                <span className="dt-num" aria-hidden="true">{t.n}.</span>
                <h3 className="sv-h3">{t.titolo}</h3>
                <p className="sv-body sv-muted">{t.testo}</p>
              </article>
            ))}
          </div>

          {/* F4 E1 — copy aggiuntivo, elegante, sotto le due card */}
          <p className="dt-riga">
            Il primo paga per sempre e non possiede nulla. Il secondo paga una volta e possiede tutto.
            Da qui in poi parliamo solo con il secondo.
          </p>

          <div className="sv-hair mt-14">
            <h3 className="sv-h3 pt-8">Le domande che non ci fate.</h3>
            <dl className="dt-domande">
              {DOMANDE.map(([q, a]) => (
                <div key={q}>
                  <dt>{q}</dt>
                  <dd>{a}</dd>
                </div>
              ))}
            </dl>
          </div>
        </div>
      </section>
    </div>
  );
}
