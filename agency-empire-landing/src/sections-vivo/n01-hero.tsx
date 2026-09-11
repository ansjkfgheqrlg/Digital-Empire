import Link from "next/link";
import { Aura, auraPresente } from "@/components/vivo/aura";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";

/* N1 — Hero a due composizioni (Dossier 37 v2, decisione «hero a due composizioni»).
   A: due colonne col ritratto di Max (posto 1) — B: una colonna, la parola EMPIRE in due strati.
   ≤ 30 parole sopra il fold (eyebrow + H1 + riga), una CTA sotto il paragrafo. Copy: COPY.md §N1. */
const VOCI = ["Digital Empire", "Outreach Factory", "Content Factory", "Second Brain", "sistemi AI sui tuoi server"];

export function Hero() {
  const conFoto = auraPresente("n1-hero.webp");
  return (
    <section id="hero" className="sv sv-ink overflow-hidden" aria-labelledby="hero-h1">
      {/* marquee: argento, arancione solo nei separatori (C2.5 v1: colore dell'azione < 10%) */}
      <div aria-hidden className="overflow-hidden py-[9px]" style={{ background: "var(--sv-silver)", borderBottom: "1px solid var(--sv-hair)" }}>
        <div className="marquee flex gap-10 whitespace-nowrap sv-mono font-extrabold" style={{ width: "max-content", color: "var(--sv-ink-1)", letterSpacing: ".28em" }}>
          {Array.from({ length: 6 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              {VOCI.map((v) => (
                <span key={v} className="flex items-center gap-10">
                  <span>{v}</span>
                  <span style={{ color: "var(--sv-orange)" }}>✦</span>
                </span>
              ))}
            </span>
          ))}
        </div>
      </div>

      <div className={conFoto ? "relative grid md:grid-cols-[46%_54%] min-h-[560px]" : "relative min-h-[520px]"}>
        <div className={`word word--pieno hidden md:block ${conFoto ? "" : "word--dx"}`} aria-hidden>EMPIRE</div>
        {conFoto && (
          <Aura
            file="n1-hero.webp"
            alt="Maximilian, fondatore — ritratto, luce di taglio da sinistra, fondo ink"
            riga="Il primo sistema l'ho costruito per me."
            rigaPos="sinistra"
            priority
            objectPosition="50% 20%"
            className="hero-foto min-h-[380px] md:min-h-0"
          />
        )}
        <div className={`word word--contorno hidden md:block ${conFoto ? "" : "word--dx"}`} aria-hidden>EMPIRE</div>

        <div className={`relative z-[4] flex flex-col justify-center gap-6 py-[11%] md:py-[9%] ${conFoto ? "px-[8%]" : "sv-container"}`}>
          <p className="sv-eyebrow">Tre sistemi AI sui tuoi server</p>
          <h1 id="hero-h1" className="sv-h1 max-w-[15ch]">
            Ti costa uno stipendio
            <span className="sv-it block text-[1.02em]" style={{ color: "var(--sv-silver)" }}>un lavoro che si fa da solo.</span>
          </h1>
          {!conFoto && (
            <p className="sv-lead" style={{ color: "var(--sv-silver)" }}>«Il primo sistema l&apos;ho costruito per me.»</p>
          )}
          <p className="sv-lead sv-muted max-w-[42ch]">
            Trenta DM a mano ogni mattina. Un carosello al giorno, a mano. Follow-up a memoria. Ti installiamo il sistema che li fa
            mentre dormi — e il codice resta tuo.
          </p>
          <p className="sv-eyebrow">↓ {FATTI.messaggiGiorno} messaggi al giorno · {FATTI.canoneMese} canoni · {FATTI.giorniSetup} giorni</p>
          <div className="flex flex-wrap items-center gap-4 pt-2">
            <Link href={prenotaDa("N1")} data-cta className="sv-btn">Prenota la chiamata →</Link>
            <span className="sv-small sv-muted">{FATTI.minutiChiamata} minuti · il sistema in live · niente slide</span>
          </div>
        </div>
      </div>
    </section>
  );
}
