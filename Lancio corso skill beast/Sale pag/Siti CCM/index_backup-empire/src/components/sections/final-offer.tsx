"use client";

import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";
import { ArrowRight, Check, Sparkles, Zap, Bot, Cpu, Workflow, Terminal } from "lucide-react";

const features = [
  "20+ ore di lezioni operative",
  "Asset Vault completo (prompt, skill, agenti)",
  "Accesso a vita + aggiornamenti",
  "Community privata di Builder",
  "Garanzia 30 giorni · Builder o Rimborsato",
];

export function FinalOffer() {
  return (
    <section className="bg-ink-2 section relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 50%, rgba(251,70,4,0.10) 0%, transparent 60%)",
        }}
      />

      <div className="max-w-[1400px] mx-auto px-4 md:px-6 relative">
        <Reveal>
          <div
            className="relative rounded-[28px] p-[3px] overflow-hidden"
            style={{
              background:
                "linear-gradient(135deg, #f5f0e6 0%, #c9c1b3 20%, #fb4604 45%, #ffb488 60%, #c9c1b3 80%, #6a6258 100%)",
              boxShadow:
                "0 0 0 1px rgba(255,255,255,0.15), 0 30px 80px -20px rgba(0,0,0,0.65), 0 0 60px -10px rgba(251,70,4,0.25)",
            }}
          >
          <div
            className="relative rounded-[25px] p-8 md:p-14 overflow-hidden"
            style={{
              background:
                "linear-gradient(135deg, #fbf7f0 0%, #f3ece0 18%, #efe3d0 32%, #f5d9b8 48%, #ffc89c 60%, #f0d9c2 75%, #e8ddd0 88%, #ddd5c8 100%)",
              boxShadow:
                "inset 0 1px 0 rgba(255,255,255,0.85), inset 0 -1px 0 rgba(0,0,0,0.12)",
            }}
          >
            <div
              aria-hidden="true"
              className="pointer-events-none absolute inset-0 rounded-3xl"
              style={{
                background:
                  "radial-gradient(ellipse at 85% 100%, rgba(251,70,4,0.22) 0%, transparent 55%), radial-gradient(ellipse at 15% 0%, rgba(255,255,255,0.5) 0%, transparent 50%)",
              }}
            />
            <div
              aria-hidden="true"
              className="pointer-events-none absolute inset-0 rounded-3xl opacity-[0.18] mix-blend-overlay"
              style={{
                backgroundImage:
                  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.55 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
              }}
            />
            {/* Logo + eyebrow */}
            <Reveal delay={0.1}>
              <div className="flex flex-col items-center text-center mb-10">
                <div
                  className="w-14 h-14 rounded-2xl flex items-center justify-center mb-5"
                  style={{
                    background:
                      "radial-gradient(circle at 30% 30%, #1c1c1c 0%, #0a0a0a 70%)",
                    border: "1px solid rgba(255,255,255,0.25)",
                    boxShadow:
                      "inset 0 1px 0 rgba(255,255,255,0.15), 0 6px 20px -6px rgba(0,0,0,0.5)",
                  }}
                >
                  <Sparkles className="h-6 w-6 text-orange-pure" strokeWidth={1.8} />
                </div>
                <div className="text-[10px] uppercase tracking-[0.3em] font-black text-ink/55 mb-3">
                  Claude Code Mastery
                </div>
                <p className="text-ink/85 text-[17px] md:text-[19px] max-w-xl leading-relaxed font-medium">
                  Avvia (in autonomia) la tua carriera come{" "}
                  <strong className="text-ink">System Architect</strong> per costruire il
                  business che lavora mentre tu dormi.
                </p>
              </div>
            </Reveal>

            {/* Dark visual block */}
            <Reveal delay={0.2}>
              <div
                className="relative rounded-2xl overflow-hidden mb-10 aspect-[4/3] md:aspect-[16/7] flex items-center justify-center"
                style={{
                  background:
                    "linear-gradient(135deg, #1c1a17 0%, #0a0908 100%)",
                  border: "1px solid rgba(0,0,0,0.4)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.05), 0 10px 30px -10px rgba(0,0,0,0.5)",
                }}
              >
                <div
                  aria-hidden="true"
                  className="absolute inset-0"
                  style={{
                    background:
                      "radial-gradient(ellipse at 50% 60%, rgba(251,70,4,0.35) 0%, transparent 60%)",
                  }}
                />
                <div
                  aria-hidden="true"
                  className="absolute inset-0"
                  style={{
                    backgroundImage:
                      "linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px)",
                    backgroundSize: "40px 40px",
                  }}
                />
                {/* corner brackets */}
                <div className="absolute top-3 left-3 w-5 h-5 border-l-2 border-t-2 border-white/25 rounded-tl" />
                <div className="absolute top-3 right-3 w-5 h-5 border-r-2 border-t-2 border-white/25 rounded-tr" />
                <div className="absolute bottom-3 left-3 w-5 h-5 border-l-2 border-b-2 border-white/25 rounded-bl" />
                <div className="absolute bottom-3 right-3 w-5 h-5 border-r-2 border-b-2 border-white/25 rounded-br" />

                {/* floating glyph icons */}
                <Bot className="hidden md:block absolute top-6 left-10 h-4 w-4 text-white/25" strokeWidth={1.5} />
                <Cpu className="hidden md:block absolute top-8 right-12 h-4 w-4 text-orange-pure/60" strokeWidth={1.5} />
                <Workflow className="hidden md:block absolute bottom-7 left-12 h-4 w-4 text-orange-pure/55" strokeWidth={1.5} />
                <Terminal className="hidden md:block absolute bottom-6 right-10 h-4 w-4 text-white/25" strokeWidth={1.5} />
                <Zap className="hidden md:block absolute top-1/2 left-6 h-3.5 w-3.5 text-white/20 -translate-y-1/2" strokeWidth={1.5} />
                <Sparkles className="hidden md:block absolute top-1/2 right-6 h-3.5 w-3.5 text-white/20 -translate-y-1/2" strokeWidth={1.5} />

                {/* top tag */}
                <div className="absolute top-3 left-1/2 -translate-x-1/2 text-[9px] uppercase tracking-[0.35em] font-black text-white/40 flex items-center gap-2">
                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-orange-pure animate-pulse" />
                  System Online
                </div>

                {/* bottom tag */}
                <div className="absolute bottom-3 left-1/2 -translate-x-1/2 text-[9px] uppercase tracking-[0.35em] font-black text-orange-pure/70">
                  v1.0 · Claude Code
                </div>

                <h3
                  className="relative text-[40px] md:text-[88px] font-black tracking-tight leading-none"
                  style={{
                    background:
                      "linear-gradient(180deg, #ffffff 0%, #d9d6cf 40%, #fb4604 100%)",
                    WebkitBackgroundClip: "text",
                    WebkitTextFillColor: "transparent",
                    backgroundClip: "text",
                    letterSpacing: "-0.04em",
                  }}
                >
                  System Architect
                </h3>
              </div>
            </Reveal>

            {/* Features + price row */}
            <div className="grid md:grid-cols-2 gap-8 md:gap-10 items-center">
              <Reveal delay={0.3}>
                <ul className="space-y-3">
                  {features.map((f, i) => (
                    <li key={i} className="flex items-start gap-3 text-ink/85 text-[15px] font-medium">
                      <div
                        className="shrink-0 w-5 h-5 rounded-full flex items-center justify-center mt-0.5"
                        style={{
                          background: "#1c1c1c",
                          boxShadow: "inset 0 1px 0 rgba(255,255,255,0.2)",
                        }}
                      >
                        <Check className="h-3 w-3 text-orange-pure" strokeWidth={3} />
                      </div>
                      <span>{f}</span>
                    </li>
                  ))}
                </ul>
              </Reveal>

              <Reveal delay={0.4}>
                <div
                  className="relative rounded-2xl p-7 text-center overflow-hidden"
                  style={{
                    background:
                      "linear-gradient(160deg, #1c1a17 0%, #0a0908 100%)",
                    border: "1px solid rgba(255,255,255,0.15)",
                    boxShadow:
                      "inset 0 1px 0 rgba(255,255,255,0.1), 0 15px 40px -10px rgba(0,0,0,0.5)",
                  }}
                >
                  <div className="text-[10px] uppercase tracking-[0.28em] font-black text-white/40 mb-3">
                    Valore totale · €2.338
                  </div>
                  <div
                    className="text-[56px] md:text-[68px] font-black leading-none mb-2"
                    style={{
                      background:
                        "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #fb4604 100%)",
                      WebkitBackgroundClip: "text",
                      WebkitTextFillColor: "transparent",
                      backgroundClip: "text",
                      letterSpacing: "-0.03em",
                    }}
                  >
                    €397
                  </div>
                  <div className="text-[10px] uppercase tracking-[0.28em] font-black text-white/50 mb-6">
                    Pagamento unico
                  </div>
                  <a
                    href="https://buy.stripe.com/aFafZj9bU0J25sj9MDdby00"
                    className="btn-orange w-full justify-center"
                  >
                    Sblocca il Mio Vantaggio Ora
                    <ArrowRight className="h-4 w-4" />
                  </a>
                  <div className="mt-3 w-full flex justify-center">
                    <CallCTA variant="dark" className="w-full justify-center" />
                  </div>
                  <div className="mt-4 text-[10px] uppercase tracking-[0.22em] font-black text-white/40">
                    Garanzia 30 giorni · 2 rate da €199 disponibili
                  </div>
                </div>
              </Reveal>
            </div>
          </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
