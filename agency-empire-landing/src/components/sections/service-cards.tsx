"use client";

import { Zap, FileText, Brain, Check, ArrowRight } from "lucide-react";
import { Reveal } from "@/components/reveal";

const OUTREACH_FEATURES = [
  "Script automazione Gmail: 300+ email personalizzate/giorno con APSOC",
  "Instagram DM safe: comportamento umano, proxy residenziali dedicati",
  "Qualificazione semantica AI: estrae i lead caldi, notifica su Slack o CRM",
  "Follow-up automatico fino a 3 touchpoint per ogni prospect",
  "Dashboard web custom per monitorare lead, status e conversazioni",
];

const CONTENT_FEATURES = [
  "Caroselli Instagram APSOC-optimized: copy CRO per ogni slide",
  "Script Reels: hook, corpo, CTA in formato 30-60 secondi",
  "Caption + hashtag strategici per massimizzare reach organico",
  "Costruzione automatica delle grafiche tramite browser automation",
  "Upload organizzato su Google Drive per argomento e data",
];

const BRAIN_FEATURES = [
  "Wiki strutturata su misura: prodotti, processi, clienti, decisioni",
  "AI che risponde in tempo reale a qualsiasi domanda sulla knowledge base",
  "Aggiornamento continuo: ogni nuova info archiviata e resa ricercabile",
  "Connessione a Notion, Google Drive, Obsidian o sistema personalizzato",
  "Accesso team: ogni membro trova ciò che cerca in secondi",
];

const GRAIN = (seed: string, freq = "1.35") =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='${freq}' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.94 0 0 0 0 0.92 0 0 0 0 0.90 0 0 0 0.35 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

// Silver border: 2px solid, luminoso e professionale
const SILVER = "2px solid rgba(214,222,234,0.62)";

const cardBase = {
  position: "relative" as const,
  isolation: "isolate" as const,
  borderRadius: 22,
  padding: "2rem 1.85rem",
  border: SILVER,
  color: "#ffffff",
  backgroundSize: "200px 200px, 100% 100%, 100% 100%",
  backgroundBlendMode: "screen, normal, normal" as const,
  boxShadow: [
    "0 60px 120px -28px rgba(0,0,28,0.90)",
    "0 2px 0 rgba(255,255,255,0.48) inset",
    "0 -2px 0 rgba(0,0,18,0.65) inset",
    "0 0 0 1px rgba(255,255,255,0.12) inset",
    "0 0 36px -10px rgba(210,222,238,0.22)",
  ].join(", "),
  transition: "transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease",
};

export function ServiceCards() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <style>{`
        .sc-card {
          transition: transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease;
        }
        .sc-card:hover {
          transform: translateY(-5px) scale(1.006);
          box-shadow:
            0 80px 140px -28px rgba(0,0,28,0.94),
            0 2px 0 rgba(255,255,255,0.55) inset,
            0 -2px 0 rgba(0,0,18,0.65) inset,
            0 0 0 1px rgba(255,255,255,0.14) inset,
            0 0 60px -8px rgba(214,222,238,0.38);
        }
        .sc-card-brain:hover {
          transform: translateY(-5px) scale(1.006);
          box-shadow:
            0 80px 140px -28px rgba(0,18,60,0.92),
            0 2px 0 rgba(255,255,255,0.40) inset,
            0 -2px 0 rgba(0,0,30,0.65) inset,
            0 0 0 1px rgba(255,255,255,0.12) inset,
            0 0 70px -8px rgba(144,192,255,0.38),
            0 0 36px -10px rgba(214,222,238,0.28);
        }
      `}</style>

      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.08) 0%, transparent 55%)",
        }}
      />
      <div className="max-w-6xl mx-auto px-6 relative">

        {/* TOP ROW — Outreach (3 cols) + Content (2 cols) */}
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-5 items-stretch mb-5">

          {/* OUTREACH FACTORY */}
          <Reveal delay={0.1} className="lg:col-span-3">
            <article
              className="sc-card h-full flex flex-col"
              style={{
                ...cardBase,
                background: [
                  GRAIN("11"),
                  "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.48) 0%, transparent 54%)",
                  "linear-gradient(145deg, #321000 0%, #521e00 18%, #922e00 40%, #cc4800 62%, #0d0a04 100%)",
                ].join(", "),
              }}
            >
              <div className="flex items-start justify-between gap-4 mb-6">
                <span
                  className="grid place-items-center w-14 h-14 rounded-2xl flex-shrink-0"
                  style={{
                    background: "linear-gradient(135deg, rgba(251,70,4,0.38) 0%, rgba(201,55,10,0.52) 100%)",
                    border: "1px solid rgba(251,70,4,0.52)",
                    boxShadow: "0 8px 24px rgba(100,20,0,0.50), inset 0 1px 0 rgba(251,70,4,0.30)",
                  }}
                >
                  <Zap className="h-6 w-6 text-orange-pure" />
                </span>
                <span className="bubble-orange !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                  Servizio primario
                </span>
              </div>

              <h3 className="text-[1.875rem] md:text-[2.25rem] font-bold leading-[1.10] tracking-tight text-white mb-2">
                Outreach Factory
              </h3>
              <p
                className="text-[1.05rem] text-white/80 mb-5"
                style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic" }}
              >
                Il tuo sales team che lavora mentre dormi.
              </p>
              <p className="text-[0.96rem] leading-relaxed text-white/90 mb-7 font-normal">
                300+ messaggi personalizzati al giorno su Gmail e Instagram. Qualificazione AI,
                follow-up automatico, dashboard web. Zero intervento manuale.
              </p>

              <ul className="flex flex-col gap-3 mb-8">
                {OUTREACH_FEATURES.map((f, i) => (
                  <li key={i} className="flex items-start gap-3 text-[0.95rem] text-white">
                    <span
                      className="grid place-items-center w-5 h-5 rounded-full mt-0.5 shrink-0"
                      style={{
                        background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
                        boxShadow: "0 0 10px rgba(251,70,4,0.38)",
                      }}
                    >
                      <Check className="h-3 w-3 text-white" strokeWidth={3} />
                    </span>
                    <span>{f}</span>
                  </li>
                ))}
              </ul>

              <a
                href="#prenota"
                className="inline-flex items-center gap-2 text-[0.95rem] font-semibold text-orange-pure mt-auto group hover:gap-3 transition-all"
              >
                Prenota una chiamata
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
              </a>
            </article>
          </Reveal>

          {/* CONTENT FACTORY */}
          <Reveal delay={0.2} className="lg:col-span-2">
            <article
              className="sc-card h-full flex flex-col"
              style={{
                ...cardBase,
                background: [
                  GRAIN("13"),
                  "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.44) 0%, transparent 54%)",
                  "linear-gradient(145deg, #2e1a00 0%, #4e3000 18%, #7e5200 40%, #aa7000 62%, #0d0a04 100%)",
                ].join(", "),
              }}
            >
              <div className="flex items-start justify-between gap-4 mb-6">
                <span
                  className="grid place-items-center w-12 h-12 rounded-xl flex-shrink-0"
                  style={{
                    background: "linear-gradient(135deg, rgba(251,70,4,0.32) 0%, rgba(201,55,10,0.50) 100%)",
                    border: "1px solid rgba(251,70,4,0.44)",
                    boxShadow: "0 6px 18px rgba(100,20,0,0.45), inset 0 1px 0 rgba(255,255,255,0.22)",
                  }}
                >
                  <FileText className="h-5 w-5 text-white" />
                </span>
                <span className="bubble-orange !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                  Servizio primario
                </span>
              </div>

              <h3 className="text-[1.5rem] md:text-[1.75rem] font-bold leading-[1.10] tracking-tight text-white mb-2">
                Content Factory
              </h3>
              <p
                className="text-[0.96rem] text-white/78 mb-4"
                style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic" }}
              >
                Pubblica ogni giorno senza toccare niente.
              </p>
              <p className="text-[0.92rem] leading-relaxed text-white/90 mb-6 font-normal">
                Caroselli APSOC, script Reels, caption e hashtag generati su richiesta. Upload automatico
                su Drive. Un brief → contenuti pronti in 30 secondi.
              </p>

              <ul className="flex flex-col gap-3 mb-7">
                {CONTENT_FEATURES.map((f, i) => (
                  <li key={i} className="flex items-start gap-2.5 text-[0.92rem] text-white">
                    <Check className="h-4 w-4 mt-0.5 shrink-0 text-orange-pure" strokeWidth={2.5} />
                    <span>{f}</span>
                  </li>
                ))}
              </ul>

              <a
                href="#prenota"
                className="inline-flex items-center gap-2 text-[0.92rem] font-semibold text-white/90 mt-auto group hover:gap-3 transition-all"
              >
                Prenota una chiamata
                <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
              </a>
            </article>
          </Reveal>
        </div>

        {/* BOTTOM ROW — Second Brain (wide) */}
        <Reveal delay={0.3}>
          <article
            className="sc-card-brain flex flex-col md:flex-row md:items-center gap-8"
            style={{
              ...cardBase,
              border: "2px solid rgba(190,215,250,0.55)",
              background: [
                GRAIN("6"),
                "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.36) 0%, transparent 54%)",
                "linear-gradient(145deg, #001e44 0%, #003270 18%, #004898 38%, #003878 60%, #001840 100%)",
              ].join(", "),
              boxShadow: [
                "0 55px 110px -28px rgba(0,18,60,0.80)",
                "0 2px 0 rgba(255,255,255,0.35) inset",
                "0 -2px 0 rgba(0,0,30,0.60) inset",
                "0 0 0 1px rgba(255,255,255,0.10) inset",
                "0 0 36px -10px rgba(190,215,250,0.22)",
              ].join(", "),
              transition: "transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease",
              padding: "2rem 2.5rem",
            }}
          >
            <div className="flex items-start gap-5 md:shrink-0 md:max-w-xs">
              <span
                className="grid place-items-center w-14 h-14 rounded-2xl flex-shrink-0"
                style={{
                  background: "linear-gradient(135deg, rgba(100,180,255,0.32) 0%, rgba(30,80,180,0.55) 100%)",
                  border: "1px solid rgba(100,180,255,0.48)",
                  boxShadow: "0 6px 20px rgba(0,30,100,0.55), inset 0 1px 0 rgba(255,255,255,0.22)",
                }}
              >
                <Brain className="h-6 w-6 text-[#90c0ff]" />
              </span>
              <div>
                <span className="text-[0.7rem] uppercase tracking-[0.18em] font-semibold text-[#90c0ff]/90 block mb-1">
                  Servizio primario
                </span>
                <h3 className="text-[1.5rem] md:text-[1.75rem] font-bold text-white leading-tight mb-1">
                  Second Brain
                </h3>
                <p
                  className="text-[0.92rem] text-white/72"
                  style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic" }}
                >
                  La tua azienda sa tutto. Sempre.
                </p>
              </div>
            </div>

            <p className="text-[0.94rem] text-white/88 leading-relaxed font-normal md:flex-1">
              Knowledge base aziendale AI: documenti, processi, clienti, decisioni — tutto indicizzato. L&apos;AI
              risponde in tempo reale a qualsiasi domanda sulla tua operatività. Zero dispersione, zero memoria
              persa.
            </p>

            <ul className="flex flex-col gap-2.5 md:shrink-0">
              {BRAIN_FEATURES.map((f, i) => (
                <li key={i} className="flex items-start gap-2.5 text-[0.875rem] text-white">
                  <Check className="h-4 w-4 mt-0.5 shrink-0 text-[#90c0ff]" strokeWidth={2.5} />
                  <span>{f}</span>
                </li>
              ))}
            </ul>
          </article>
        </Reveal>
      </div>
    </section>
  );
}
