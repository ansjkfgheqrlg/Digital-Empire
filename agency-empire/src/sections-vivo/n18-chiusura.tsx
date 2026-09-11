import { ArrowRight } from "lucide-react";
import { Dashboard } from "./n04-fabbriche";

/* N18 — Chiusura: la dashboard (oggetto-icona di N4) torna in controluce (speedrun T20 / tavola 9).
   L'unica sezione centrata della pagina: va guardata, non letta (armageddon T5). Copy: COPY-V2 §N18. */
export function Chiusura() {
  return (
    <section id="prenota" className="sv sv-chiusura overflow-hidden" aria-labelledby="chiusura-h2">
      <div className="container-default relative py-20 md:py-24 text-center min-h-[420px] grid place-items-center">
        <div
          className="absolute left-1/2 -translate-x-1/2 bottom-[-40px] w-[min(760px,90%)] pointer-events-none"
          style={{ opacity: 0.14, filter: "grayscale(1) contrast(1.3)" }}
          aria-hidden
        >
          <Dashboard />
        </div>
        <div className="relative grid gap-5 justify-items-center">
          <p className="sv-mono" style={{ color: "var(--sv-silver-dim)" }}>Cinque minuti · niente slide</p>
          <h2 id="chiusura-h2" className="sv-h2 max-w-[14ch]" style={{ fontSize: "clamp(30px,4vw,54px)" }}>
            In chiamata <span className="sv-it" style={{ color: "var(--sv-silver)" }}>la vedi girare.</span>
          </h2>
          <p className="sv-lead sv-muted max-w-[44ch]">
            Lead veri che entrano, contenuti che si generano, la dashboard aperta. Poi decidi tu. Se non fa per te,
            ti abbiamo fatto perdere trenta minuti e un caffè.
          </p>
          <a href="/prenota" className="btn-gold btn-gold--lg" data-cta="chiusura">
            Prenota la chiamata <ArrowRight className="h-4 w-4" />
          </a>
          <p className="sv-mono" style={{ color: "var(--sv-silver-dim)" }}>Calendly · 30 minuti · zero canoni, mai</p>
        </div>
      </div>
    </section>
  );
}
