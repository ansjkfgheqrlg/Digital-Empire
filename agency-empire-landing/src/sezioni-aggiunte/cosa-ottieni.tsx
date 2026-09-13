import { BottonePrenota } from "./bottone";
import { FATTI } from "@/lib/fatti";

/* SEZIONE AGGIUNTA 3 — Cosa ottieni se prenoti (inserita prima di <FinalCTA />). Copy: COPY.md §N17. Tutto dentro <div class="vivo">.
   È la CTA PRINCIPALE della pagina (pattern pre-cassa).
   Rifatta il 13/09 sera (BRIEF F3 blocco C, 39A E42): via la card col bordo accento; la checklist è una tabella bordata
   (bordo 1 px, raggio 8, righe separate da filetti, spunta accento in cerchio), sotto UN bottone da 48 px con testo ink su
   arancio. Il testo è identico a prima: etichetta «Prenota la chiamata →» nel bottone, la riga «30 minuti · gratuita ·
   nessun canone, mai» in mono sotto. CSS: aggiunte-c.css (.co-*). */
const VOCI = [
  "Trenta minuti con chi costruisce il sistema, non con un venditore",
  "Il sistema vero che gira davanti a te: lead che entrano, contenuti che escono",
  "La diagnosi della tua operatività: cosa si automatizza per primo e cosa no",
  "Un numero: quante ore tue a settimana tornano indietro",
  "Il prezzo esatto per il tuo caso, detto in chiamata, non «a partire da»",
  "Zero impegno: se non fa per te, ti abbiamo fatto perdere trenta minuti e un caffè",
];

export function CosaOttieni() {
  return (
    <div className="vivo">
      <section id="cosa-ottieni" className="sv sv-ink sv-section" aria-labelledby="cosa-ottieni-h2">
        <div className="sv-container co-colonna">
          <h2 id="cosa-ottieni-h2" className="sv-h2 max-w-[14ch]">
            Cosa ottieni <span className="sv-it" style={{ color: "var(--sv-silver)" }}>se prenoti adesso.</span>
          </h2>
          <ul className="co-lista c-grana" aria-label="Cosa ottieni dalla chiamata">
            {VOCI.map((v) => (
              <li key={v} className="co-voce">
                <span className="co-spunta" aria-hidden="true">
                  <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M2 6.5 4.8 9.2 10 3.2" />
                  </svg>
                </span>
                <span>{v}</span>
              </li>
            ))}
          </ul>
          <div className="co-azione">
            <BottonePrenota da="cosa-ottieni" className="co-btn" />
            <p className="sv-mono co-sotto">{FATTI.minutiChiamata} minuti · gratuita · nessun canone, mai</p>
          </div>
        </div>
      </section>
    </div>
  );
}
