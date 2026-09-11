import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N1 — Hero a due colonne (Dossier 37, tavola 2). Copy: cantiere/COPY-V2.md §N1.
   ≤ 30 parole sopra il fold, zero bottoni sopra il fold: la CTA sta sotto il paragrafo.
   "EMPIRE" in due strati: pieno sotto la foto, contorno sopra (armageddon T1). */
export function Hero() {
  return (
    <section id="hero" className="sv sv-ink overflow-hidden pt-[72px]" aria-labelledby="hero-h1">
      {/* pt-[72px]: la navbar e' fissa e alta 72px (navbar.tsx:118) — il marquee deve stare sotto, non dietro */}
      {/* marquee metallico: nostro, resta. Arancione al 10% della lunghezza (C2.5) */}
      <div
        aria-hidden
        className="overflow-hidden py-[9px]"
        style={{
          background:
            "linear-gradient(90deg, #c8c4c0 0%, #ddd8d4 14%, #f0edec 28%, #ffffff 44%, rgba(251,70,4,0.9) 50%, #ffffff 56%, #f0edec 72%, #ddd8d4 86%, #c8c4c0 100%)",
          borderBottom: "1px solid rgba(251,70,4,0.22)",
        }}
      >
        <div
          className="marquee flex gap-10 whitespace-nowrap sv-mono font-extrabold"
          style={{ width: "max-content", color: "#1c1c1c", letterSpacing: ".28em" }}
        >
          {Array.from({ length: 8 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>AI Workflow Agency</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>Outreach Factory</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>Content Factory</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>by Digital Empire</span>
              <span style={{ color: "#fb4604" }}>✦</span>
            </span>
          ))}
        </div>
      </div>

      <div className="relative grid md:grid-cols-[46%_54%] min-h-[560px]">
        <div className="word word--pieno hidden md:block" aria-hidden>EMPIRE</div>

        <Aura
          file="n1-hero.webp"
          alt="Ritratto in luce di taglio, sguardo dritto — chi ha costruito il sistema"
          riga={'Ho costruito il primo sistema per me. Poi ho smesso di venderlo come "tool".'}
          rigaPos="sinistra"
          priority
          objectPosition="50% 20%"
          className="hero-foto min-h-[380px] md:min-h-0"
          segnaposto={{ nome: "Max", ruolo: "ritratto · luce AURA" }}
        />

        <div className="word word--contorno hidden md:block" aria-hidden>EMPIRE</div>

        <div className="relative z-[4] flex flex-col justify-center gap-6 px-[8%] py-[11%] md:py-[9%]">
          <p className="sv-eyebrow"><b>Agenzia</b> · sistemi AI che girano sui tuoi server</p>
          <h1 id="hero-h1" className="sv-h1 max-w-[15ch]">
            Ti costa uno stipendio
            <span className="sv-it block text-[1.02em]" style={{ color: "var(--sv-silver)" }}>
              un lavoro che si fa da solo.
            </span>
          </h1>
          <p className="sv-lead sv-muted max-w-[42ch]">
            Trenta DM a mano ogni mattina. Un carosello al giorno, a mano. Follow-up a memoria.
            Noi ti installiamo il sistema che li fa mentre dormi — e il codice resta tuo.
          </p>
          <p className="sv-eyebrow">↓ 300 messaggi al giorno · 0 canoni · 7 giorni</p>
          <div className="flex flex-wrap items-center gap-4 pt-2">
            <a href="/prenota" className="btn-gold" data-cta="hero">
              Prenota la chiamata <ArrowRight className="h-4 w-4" />
            </a>
            <span className="sv-small sv-muted">30 minuti · il sistema in live · niente slide</span>
          </div>
        </div>
      </div>
    </section>
  );
}
