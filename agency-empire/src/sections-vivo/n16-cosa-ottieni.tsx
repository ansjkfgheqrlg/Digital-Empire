import { ArrowRight } from "lucide-react";

/* N16 — Cosa ottieni se prenoti (speedrun T28): checklist pre-CTA + il bottone col bagliore.
   E' la CTA principale della pagina. Copy: COPY-V2 §N16. */
const VOCI = [
  "Trenta minuti con chi costruisce il sistema, non con un venditore",
  "Il sistema vero che gira davanti a te: lead che entrano, contenuti che escono",
  "La diagnosi della tua operatività: cosa si automatizza per primo e cosa no",
  "Un numero: quante ore tue a settimana tornano indietro",
  'Il prezzo esatto per il tuo caso, detto in chiamata, non "a partire da"',
  "Zero impegno: se non fa per te, ti abbiamo fatto perdere trenta minuti e un caffè",
];

export function CosaOttieni() {
  return (
    <section id="cosa-ottieni" className="sv sv-ink-piatto sv-hair" aria-labelledby="ottieni-h2">
      <div className="container-tight py-16 md:py-20">
        <div className="rounded-[6px] p-7 md:p-10" style={{ border: "1px solid var(--sv-hair)", background: "rgba(255,255,255,.02)" }}>
          <h2 id="ottieni-h2" className="sv-h2 max-w-[16ch]">
            Cosa ottieni <span className="sv-it" style={{ color: "var(--sv-silver)" }}>se prenoti adesso.</span>
          </h2>
          <ul className="mt-8 grid gap-3 list-none p-0 m-0">
            {VOCI.map((v) => <li key={v} className="sv-check sv-body text-white">{v}</li>)}
          </ul>
          <div className="mt-9 flex flex-wrap items-center gap-4">
            <a href="/prenota" className="btn-gold btn-gold--lg" data-cta="cosa-ottieni">
              Prenota la chiamata <ArrowRight className="h-4 w-4" />
            </a>
            <span className="sv-mono" style={{ color: "var(--sv-silver-dim)" }}>30 minuti · Calendly · nessun canone, mai</span>
          </div>
        </div>
      </div>
    </section>
  );
}
