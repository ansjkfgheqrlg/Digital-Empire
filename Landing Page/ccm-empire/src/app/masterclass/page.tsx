"use client";

import {
  ArrowUpRight,
  CalendarCheck,
  GraduationCap,
  KeyRound,
  PhoneCall,
  Play,
  Sparkles,
} from "lucide-react";
import { Reveal } from "@/components/reveal";

const CALL_URL = "https://chiamata-formazione.netlify.app/";
const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";

const MODULES = [
  { n: "01", t: "Setup & Prime Mosse", d: "Installazione, configurazione, autenticazione, IDE." },
  { n: "02", t: "Slash Command & Skill", d: "Comandi custom e skill modulari in azione." },
  { n: "03", t: "Sub-Agent", d: "Delegare lavoro in parallelo con agent specializzati." },
  { n: "04", t: "Hook", d: "Automazioni deterministiche su eventi di sessione." },
  { n: "05", t: "MCP Server", d: "Collegare Claude a tool esterni e API reali." },
  { n: "06", t: "CLAUDE.md & Memory", d: "Identità operativa, memoria persistente, policy." },
  { n: "07", t: "Settings & Permessi", d: "settings.json, env var, policy di sicurezza." },
  { n: "08", t: "Workflow Git & PR", d: "Commit puliti, review di pull request, reviewer senior." },
  { n: "09", t: "Performance & Context", d: "Context window, caching, compaction, parallel tool." },
];

export default function MasterclassPage() {
  return (
    <main className="relative z-10 pb-16 bg-[#1c1c1c] min-h-screen">
      {/* HERO */}
      <section className="max-w-5xl mx-auto px-6 pt-14 md:pt-20 text-center">
        <Reveal>
          <span className="bubble-orange mb-6">
            <KeyRound className="h-3.5 w-3.5" /> Accesso Confermato
          </span>
        </Reveal>
        <Reveal delay={0.05}>
          <div className="pre-headline mt-2 mb-4">
            Claude Code Mastery · Masterclass
          </div>
        </Reveal>
        <Reveal delay={0.1}>
          <h1 className="text-4xl md:text-6xl font-bold leading-[1.05] mb-6">
            <span className="text-silver-white">Benvenuto nella</span>
            <br />
            <span className="text-silver-orange">Masterclass Pratica.</span>
          </h1>
        </Reveal>
        <Reveal delay={0.15}>
          <p className="text-white/65 text-lg max-w-2xl mx-auto font-light leading-relaxed mb-10">
            <strong className="text-silver-orange font-semibold">
              3+ ore di formazione applicata
            </strong>{" "}
            su Claude Code. Ogni capitolo dell&apos;ebook,{" "}
            <span className="hl-block">mostrato a schermo, step by step</span>.
          </p>
        </Reveal>
      </section>

      {/* VIDEO PLACEHOLDER */}
      <section className="max-w-5xl mx-auto px-6 mb-14">
        <Reveal delay={0.2} variant="scale">
          <div
            className="relative w-full overflow-hidden flex items-center justify-center"
            style={{
              aspectRatio: "16/9",
              borderRadius: "18px",
              border: "1px solid rgba(255,255,255,0.12)",
              background:
                "radial-gradient(ellipse at center, #1a1a1a 0%, #0a0a0a 100%)",
              boxShadow:
                "0 50px 100px -30px rgba(0,0,0,0.9), 0 0 0 1px rgba(251,70,4,0.1)",
            }}
          >
            <div
              className="absolute inset-0 pointer-events-none"
              style={{
                background:
                  "radial-gradient(ellipse at center, rgba(251,70,4,0.1) 0%, transparent 60%)",
              }}
            />
            <div className="relative z-10 text-center p-8">
              <div className="w-20 h-20 mx-auto rounded-full bg-[#fb4604]/20 border border-[#fb4604]/40 flex items-center justify-center mb-6 shadow-[0_0_40px_rgba(251,70,4,0.3)]">
                <Play className="w-8 h-8 text-[#ff6a2e] ml-1" fill="currentColor" />
              </div>
              <h2 className="text-2xl md:text-3xl font-bold text-silver-white mb-3">
                Il video sarà caricato qui
              </h2>
              <p className="text-white/55 text-sm max-w-md mx-auto leading-relaxed">
                Sostituisci questo placeholder con l&apos;embed del video (Vimeo,
                YouTube unlisted, Wistia o hosting privato). La masterclass è
                pronta.
              </p>
            </div>
          </div>
        </Reveal>
      </section>

      {/* MODULI */}
      <section className="max-w-5xl mx-auto px-6 mb-20">
        <Reveal>
          <div className="text-center mb-10">
            <span className="bubble-silver text-xs mb-4">
              Contenuto della Masterclass
            </span>
            <h2 className="text-3xl md:text-4xl font-bold leading-tight mt-4">
              <span className="text-silver-white">
                Ogni capitolo dell&apos;ebook,
              </span>
              <br />
              <span className="text-silver-orange">
                in pratica a schermo condiviso.
              </span>
            </h2>
          </div>
        </Reveal>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {MODULES.map((m, i) => (
            <Reveal key={i} delay={(i % 3) * 0.08}>
              <div className="card-dark h-full" style={{ padding: "1.5rem" }}>
                <div className="text-[11px] uppercase tracking-[0.22em] text-[#ff6a2e] font-bold mb-2">
                  Modulo {m.n}
                </div>
                <h3 className="text-lg font-bold text-white mb-1">{m.t}</h3>
                <p className="text-white/60 text-sm font-light leading-relaxed">
                  {m.d}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* DIVIDER */}
      <div className="max-w-xs mx-auto my-14 flex items-center gap-4">
        <div className="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />
        <PhoneCall className="w-4 h-4 text-[#ff6a2e]" />
        <div className="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />
      </div>

      {/* CALL PROMO */}
      <section className="max-w-4xl mx-auto px-6">
        <Reveal>
          <div className="card-dark relative overflow-hidden">
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,rgba(251,70,4,0.2)_0%,transparent_60%)] pointer-events-none" />
            <div className="relative z-10 grid md:grid-cols-[1.2fr_auto] gap-8 items-center">
              <div>
                <span className="bubble-silver mb-4 text-xs">
                  <Sparkles className="w-3 h-3" /> Il prossimo passo
                </span>
                <h3 className="text-2xl md:text-3xl font-bold leading-tight mt-4 mb-4">
                  <span className="text-silver-white">Pronto a passare da</span>
                  <br />
                  <span className="text-silver-orange">
                    AI User a System Architect?
                  </span>
                </h3>
                <p className="text-white/70 font-light leading-relaxed text-[15px] md:text-base mb-2">
                  Se la masterclass ti sta aprendo la mente,{" "}
                  <strong className="text-silver-orange font-semibold">
                    il salto successivo
                  </strong>{" "}
                  è il corso completo. Prenota una{" "}
                  <strong className="text-white">
                    chiamata strategica gratuita
                  </strong>{" "}
                  per capire se fa al caso tuo.
                </p>
              </div>
              <div className="flex flex-col gap-3 w-full md:w-auto md:min-w-[240px]">
                <a
                  href={CALL_URL}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-orange justify-center whitespace-nowrap"
                >
                  <CalendarCheck className="w-4 h-4" />
                  Prenota la chiamata
                </a>
                <a
                  href={COURSE_URL}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-ghost justify-center whitespace-nowrap text-sm py-3 px-6"
                >
                  <GraduationCap className="w-4 h-4" />
                  Vedi il corso
                </a>
              </div>
            </div>
          </div>
        </Reveal>
      </section>

      <footer className="py-10 mt-20 text-center text-white/30 text-xs tracking-widest uppercase font-medium border-t border-white/5">
        © 2026 Digital Empire Labs
      </footer>
    </main>
  );
}
