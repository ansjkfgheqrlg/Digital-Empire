"use client";

import { Reveal } from "@/components/reveal";
import { Crown, Users, Zap, ArrowRight } from "lucide-react";

/* ─────────────────────────────────────────────────────────
   Chi Siamo — Digital Empire Team
   Adattato dal pattern CCM about-story con colori brand navy/cream
   ───────────────────────────────────────────────────────── */

export function ChiSiamo() {
  return (
    <>
      {/* ── 1. INTRO ── bg-paper */}
      <section
        className="bg-paper section relative overflow-hidden"
        aria-labelledby="chisiamo-h2"
      >
        <div className="container-default text-center relative">
          <Reveal>
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Il team · Chi costruisce il tuo workflow
            </span>
          </Reveal>

          <Reveal delay={0.1}>
            <h2 id="chisiamo-h2" className="mt-6">
              <span className="text-silver-black">Siamo Digital Empire.</span>{" "}
              <span className="text-brand-accent font-accent italic">
                Costruiamo, non promettiamo.
              </span>
            </h2>
          </Reveal>

          <Reveal delay={0.2}>
            <p className="mt-5 text-[1.0625rem] text-[#1c1c1c]/70 leading-relaxed font-light max-w-2xl mx-auto">
              Un team specializzato in AI Workflow. Niente sales junior, niente account manager —
              quando lavori con noi parli con chi ha le mani sui sistemi e costruisce ogni giorno.
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="mt-10 flex flex-wrap justify-center gap-3">
              {["Trasparenti", "Operativi", "Senza fuffa", "In prima linea"].map((t, i) => (
                <span
                  key={i}
                  className="px-4 py-2 rounded-full text-[11px] uppercase tracking-[0.22em] font-bold"
                  style={{
                    color: "rgba(251,70,4,0.90)",
                    background: "rgba(251,70,4,0.08)",
                    border: "1px solid rgba(251,70,4,0.20)",
                  }}
                >
                  {t}
                </span>
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      {/* ── 2. TEAM CARDS ── bg-ink-2 */}
      <section className="bg-ink-2 section relative overflow-hidden">
        {/* Ambient glow navy */}
        <div
          aria-hidden
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.10) 0%, transparent 55%)",
          }}
        />

        <div className="container-wide relative">
          <div className="text-center mb-14">
            <Reveal>
              <span className="bubble-gold">
                <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
                Le persone · 3 + zero rumore
              </span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="mt-6">
                <span className="text-silver-white">Tre persone.</span>{" "}
                <span className="text-silver-gold font-accent italic">
                  Zero filtri tra te e chi costruisce.
                </span>
              </h2>
            </Reveal>
            <Reveal delay={0.2}>
              <p className="mt-5 text-white/60 text-[1rem] max-w-2xl mx-auto leading-relaxed">
                Niente sales junior. Niente account manager. Quando lavori con noi,{" "}
                <strong className="text-silver-gold">parli con chi ha le mani sui workflow.</strong>
              </p>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-3 gap-5">
            {/* MAX — Founder */}
            <Reveal delay={0.15}>
              <div
                className="relative rounded-2xl p-7 h-full"
                style={{
                  background:
                    "linear-gradient(160deg, #1a0800 0%, #0e0600 50%, #060200 100%)",
                  border: "1.5px solid rgba(251,70,4,0.38)",
                  boxShadow:
                    "inset 0 1px 0 rgba(251,70,4,0.14), 0 20px 55px -18px rgba(100,20,0,0.70)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0"
                    style={{
                      background:
                        "linear-gradient(135deg, #fb4604 0%, #ff6a2e 55%, #c93a0a 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.28), 0 4px 16px -4px rgba(201,55,10,0.60)",
                    }}
                  >
                    <Crown className="h-5 w-5 text-white" strokeWidth={1.8} />
                  </div>
                  <span
                    className="text-[10px] uppercase tracking-[0.28em] font-black"
                    style={{ color: "rgba(251,70,4,0.90)" }}
                  >
                    Founder
                  </span>
                </div>
                <h3 className="text-[1.5rem] font-bold text-silver-white mb-3 leading-tight">
                  Maximilian
                </h3>
                <p className="text-white/70 text-[0.9rem] leading-relaxed">
                  Sei anni di marketing. Tre di AI a tempo pieno. Architetto dei workflow, voce del
                  copy, ossessionato dai dettagli che fanno la differenza tra un sistema che gira e
                  uno che si rompe.
                </p>
              </div>
            </Reveal>

            {/* GAEL — Socio */}
            <Reveal delay={0.25}>
              <div
                className="relative rounded-2xl p-7 h-full"
                style={{
                  background:
                    "linear-gradient(160deg, #1c1e28 0%, #14161e 50%, #0c0e16 100%)",
                  border: "1px solid rgba(255,255,255,0.12)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.07), 0 14px 45px -18px rgba(0,0,0,0.75)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0"
                    style={{
                      background: "linear-gradient(160deg, #d9d6cf 0%, #8a8378 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.5), 0 4px 14px -2px rgba(0,0,0,0.4)",
                    }}
                  >
                    <Users className="h-5 w-5 text-[#0a0a0a]" strokeWidth={2} />
                  </div>
                  <span
                    className="text-[10px] uppercase tracking-[0.28em] font-black"
                    style={{ color: "rgba(255,255,255,0.50)" }}
                  >
                    Socio · Pari grado
                  </span>
                </div>
                <h3 className="text-[1.5rem] font-bold text-silver-white mb-3 leading-tight">
                  Gael
                </h3>
                <p className="text-white/70 text-[0.9rem] leading-relaxed">
                  Il mio socio alla pari. La persona con cui mi confronto su ogni decisione che
                  conta. Le partnership migliori nascono lontano dagli uffici — la nostra non fa
                  eccezione.
                </p>
              </div>
            </Reveal>

            {/* LEONARDO — Team */}
            <Reveal delay={0.35}>
              <div
                className="relative rounded-2xl p-7 h-full"
                style={{
                  background:
                    "linear-gradient(160deg, #1c1e28 0%, #14161e 50%, #0c0e16 100%)",
                  border: "1px solid rgba(255,255,255,0.12)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.07), 0 14px 45px -18px rgba(0,0,0,0.75)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center flex-shrink-0"
                    style={{
                      background: "linear-gradient(160deg, #d9d6cf 0%, #8a8378 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.5), 0 4px 14px -2px rgba(0,0,0,0.4)",
                    }}
                  >
                    <Zap className="h-5 w-5 text-[#0a0a0a]" strokeWidth={2} />
                  </div>
                  <span
                    className="text-[10px] uppercase tracking-[0.28em] font-black"
                    style={{ color: "rgba(255,255,255,0.50)" }}
                  >
                    Team Empire
                  </span>
                </div>
                <h3 className="text-[1.5rem] font-bold text-silver-white mb-3 leading-tight">
                  Leonardo
                </h3>
                <p className="text-white/70 text-[0.9rem] leading-relaxed">
                  Una delle tre teste di Digital Empire. Energia, esecuzione, presenza costante.
                  Quando entri in Empire, anche lui è uno di quelli con cui costruirai il tuo
                  workflow.
                </p>
              </div>
            </Reveal>
          </div>

          <Reveal delay={0.45}>
            <p className="text-center text-white/45 text-sm max-w-2xl mx-auto mt-12 leading-relaxed">
              <span className="text-gold-pure">→</span> Tre persone, una visione, zero burocrazia.{" "}
              <strong className="text-silver-white">Per scelta, non per limite.</strong>
            </p>
          </Reveal>
        </div>
      </section>

      {/* ── 3. MISSIONE ── bg-paper */}
      <section className="bg-paper section relative overflow-hidden">
        <div className="container-default text-center relative">
          <Reveal>
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              La nostra missione
            </span>
          </Reveal>

          <Reveal delay={0.15}>
            <div
              className="mt-10 max-w-3xl mx-auto rounded-2xl p-10 md:p-12"
              style={{
                background:
                  "linear-gradient(155deg, #fff0e8 0%, #f5d5c0 45%, #e8b090 100%)",
                border: "1px solid rgba(255,255,255,0.65)",
                boxShadow:
                  "inset 0 1px 0 rgba(255,255,255,0.80), 0 22px 55px -18px rgba(201,55,10,0.25)",
              }}
            >
              <p
                className="text-[1.35rem] md:text-[1.85rem] font-bold text-[#1c1c1c] leading-[1.3]"
                style={{ letterSpacing: "-0.022em" }}
              >
                L&apos;agenzia progettata per{" "}
                <span className="font-accent italic text-brand-accent">
                  essere licenziata.
                </span>
              </p>
              <p className="mt-5 text-[#1c1c1c]/65 text-[0.96rem] leading-relaxed max-w-xl mx-auto font-light">
                Non vogliamo dipendenza. Vogliamo che tu sia così autonomo da non aver più bisogno
                di noi. Un sistema davvero buono ti libera — non ti incatena.
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.25}>
            <a
              href="#cta-finale"
              className="mt-8 inline-flex items-center gap-2 text-[0.9rem] font-semibold text-[#fb4604] group hover:gap-3 transition-all"
            >
              Prenota la demo gratuita
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </a>
          </Reveal>
        </div>
      </section>
    </>
  );
}
