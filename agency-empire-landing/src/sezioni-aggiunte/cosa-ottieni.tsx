import { BottonePrenota } from "./bottone";
import { FATTI } from "@/lib/fatti";

/* SEZIONE AGGIUNTA 3 — Cosa ottieni se prenoti (inserita prima di <FinalCTA />). Copy: COPY.md §N17. Tutto dentro <div class="vivo">.: la checklist + il bottone a bagliore. È la CTA PRINCIPALE della pagina
   (pattern pre-cassa). Copy: COPY.md §N17. */
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
      <div className="sv-container">
        <div className="sv-card sv-card--engine max-w-[760px] mx-auto md:p-12">
          <h2 id="cosa-ottieni-h2" className="sv-h2 max-w-[14ch]">
            Cosa ottieni <span className="sv-it" style={{ color: "var(--sv-silver)" }}>se prenoti adesso.</span>
          </h2>
          <ul className="mt-8 space-y-3">
            {VOCI.map((v) => (
              <li key={v} className="sv-check sv-body sv-muted">{v}</li>
            ))}
          </ul>
          <div className="mt-10">
            <BottonePrenota da="cosa-ottieni" principale sublabel={`${FATTI.minutiChiamata} minuti · gratuita · nessun canone, mai`} />
          </div>
        </div>
      </div>
    </section>
    </div>
  );
}
