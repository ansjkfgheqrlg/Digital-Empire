/* AGGIUNTA F3 (BRIEF F3 blocco C, 13/09 sera — 39A E21 «frase barrata + frase vera») — l'apertura del problema.
   Va montata subito PRIMA di <Specchio /> (dopo <Problems />). Superficie ink, h ≤ 320. 0 KB di JS.
   Un gesto tipografico, zero componenti: la credenza barrata (line-through accento 3 px, colore dim) e sotto la frase vera,
   bianca, a --fs-h2; sottotitolo a 17. Copy in voce di casa, senza numeri. Nessuna CTA (§15: Atto I-II).
   CSS: aggiunte-c.css (.fb-*).

   RIFACIMENTO D1+D2+D3 (dossier 41, ordine di Max 15/09):
   D1 — la nota della smorfia ora si aggancia alla punta della freccia (non più al fondo del box in flusso
   normale): freccia+nota vivono in .d-freccia-wrap, posizionato ASSOLUTO, con svg e <p> ancorati in px alla
   stessa origine — la nota sta 8px sotto la punta e il suo bordo sinistro è allineato alla x della punta.
   D2 — testo nuovo della nota, coi numeri da FATTI (nessun numero scritto a mano — gate fatti).
   D3 — «Ti serve un altro tool.» torna sola (via .fb-barrata-sola, .fb-barrata smette di avere il gruppo
   uguale+ovvero); l'«= Ovvero: …» si sposta DENTRO l'h2, appeso a «senza di te.» sulla stessa riga se c'è
   spazio (inline, va sotto da solo altrimenti — nessuna media query, è il flusso naturale del testo).
   Testo dei titoli identico. CSS: f6-frecce.css (.d-freccia-*, override .fb-barrata/.fb-vera/.fb-ovvero). */
import { FATTI } from "@/lib/fatti";

export function FraseBarrata() {
  return (
    <div className="vivo">
      <section id="frase-barrata" className="sv sv-ink fb" aria-labelledby="frase-barrata-h2">
        <div className="sv-container">
          <p className="fb-barrata fb-barrata-sola">
            <s>Ti serve un altro tool.</s>
          </p>

          {/* AGGIUNTA F5 (ordine 3 di Max, 14/09 notte), rifatta D1/D2 (15/09) — foto di riferimento (10) a
              destra della riga barrata, piccola, con freccia hairline (mai a contatto) verso una nota
              letterale ancorata alla punta. CSS: f6-frecce.css (.d-freccia-*). */}
          <div className="f5-rif-foto f5-rif-foto--smorfia">
            <figure className="f5-rif-fig">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/foto/rif-smorfia.jpg" width={735} height={648} alt="" loading="lazy" decoding="async" />
            </figure>
            <div className="d-freccia-wrap">
              <svg className="d-freccia-svg" viewBox="0 0 50 50" aria-hidden="true" focusable="false">
                <defs>
                  <marker id="d-freccia-punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                    <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                  </marker>
                </defs>
                <path d="M10,0 C4,18 36,24 34,44" fill="none" stroke="#fb4604" strokeWidth="1.3" markerEnd="url(#d-freccia-punta)" />
              </svg>
              <p className="d-freccia-nota">
                La faccia di chi ha una nostra applicazione custom che gli sostituisce {FATTI.toolSostituiti} tool da{" "}
                {FATTI.toolEuroMese} € al mese ognuno.
              </p>
            </div>
          </div>

          <h2 id="frase-barrata-h2" className="sv-h2 fb-vera">
            Ti serve un sistema che gira <span className="sv-it">senza di te.</span>{" "}
            <span className="fb-ovvero">
              <span className="fb-uguale">=</span> <b>Ovvero:</b>{" "}
              <span className="sv-it">automatizzare un processo lungo e ripetitivo</span>
            </span>
          </h2>
          <p className="fb-sotto">Il tool lo affitti. Il sistema lo possiedi.</p>
        </div>
      </section>
    </div>
  );
}
