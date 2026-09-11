import Link from "next/link";
import { Aura } from "@/components/vivo/aura";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";

/* N2 — Specchio + DM vero + i quattro segnali + voto (speedrun T6 + micro-sondaggio). Copy: COPY.md §N2.
   «Sì, mi ritrovo» va alla chiamata; «Non mi ritrovo» scende ad ASCOLTA BENE (N6). */
const SEGNALI: [string, string][] = [
  ["Rimandi il follow-up.", "Il lead di martedì lo ricontatti venerdì, se te lo ricordi."],
  ["Pubblichi quando riesci.", "Tre post una settimana, zero la successiva."],
  ["Copi e incolli.", "Lo stesso messaggio a trenta persone diverse. Loro se ne accorgono."],
  ["Sai tutto tu.", "Clienti, prezzi, processi: nella tua testa e in cinque cartelle Drive. Il giorno che manchi tu, manca l'azienda."],
];

export function Specchio() {
  return (
    <section id="specchio" className="sv sv-carta sv-section" aria-labelledby="specchio-h2">
      <div className="sv-container">
        <div className="due-col due-col--foto-sx">
          <Aura file="n2-specchio.webp" alt="Uomo in giacca seduto con la mano sul viso" riga="Ogni mattina. Trenta DM. A mano." tratt="carta" />
          <div>
            <h2 id="specchio-h2" className="sv-h2 max-w-[14ch]">
              Ti voglio bene, ma <span className="sv-it" style={{ color: "var(--sv-orange)" }}>lo stai facendo a mano.</span>
            </h2>
            <p className="sv-lead sv-muted mt-4 max-w-[52ch]">
              Non è colpa tua: nessuno ti ha mai mostrato il sistema. Ti hanno mostrato un tool, un abbonamento, un corso. Questo è
              quello che parte dal tuo telefono oggi:
            </p>
            <div className="dm mt-6 max-w-[460px]">
              <span className="sv-mono block mb-2">DM di oggi · concessionario, Veneto</span>
              <i>Ciao! Ho visto la tua concessionaria, complimenti 👏 Ti va se ti mando due info su come aumentare i contatti? 🚗</i>
              <em>
                — {FATTI.dmAMano} volte al giorno, {FATTI.minutiPerDm} minuti l&apos;uno: {FATTI.orePerDm.toLocaleString("it-IT")} ore.
                Sembra un template perché lo è.
              </em>
            </div>
          </div>
        </div>

        <div className="mt-14 md:mt-16">
          <h3 className="sv-h3">I quattro segnali. Ne basta uno.</h3>
          <ol className="mt-6 grid md:grid-cols-2 gap-x-10 gap-y-5 max-w-[900px]">
            {SEGNALI.map(([t, d], i) => (
              <li key={t} className="grid grid-cols-[28px_1fr] gap-3 items-start">
                <span className="sv-mono" style={{ color: "var(--sv-orange)" }}>{i + 1}</span>
                <p className="sv-body sv-muted">
                  <b style={{ color: "var(--sv-ink-1)" }}>{t}</b> {d}
                </p>
              </li>
            ))}
          </ol>
          <div className="mt-8 flex flex-wrap items-center gap-4">
            <span className="sv-body">
              <b>Ti ritrovi?</b> Quattro segnali: ne basta 1.
            </span>
            <Link href={prenotaDa("N2")} data-cta className="sv-btn">Sì, mi ritrovo →</Link>
            <a href="#ascolta-bene" className="sv-btn-ghost">Non mi ritrovo</a>
          </div>
        </div>
      </div>
    </section>
  );
}
