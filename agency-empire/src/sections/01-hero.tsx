"use client";

import { Sparkles, ArrowRight, Shield } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { MagneticButton } from "@/components/magnetic-button";

export function Hero() {
  return (
    <section
      className="bg-ink relative overflow-hidden"
      aria-labelledby="hero-h1"
    >
      {/* ── MARQUEE BAR CCM-style ── barra metallica silver-orange */}
      <div
        aria-hidden
        className="overflow-hidden py-[10px] relative"
        style={{
          background:
            "linear-gradient(90deg, #c8c4c0 0%, #ddd8d4 14%, #f0edec 28%, #ffffff 38%, rgba(251,70,4,0.90) 50%, #ffffff 62%, #f0edec 72%, #ddd8d4 86%, #c8c4c0 100%)",
          borderTop: "1px solid rgba(255,255,255,0.65)",
          borderBottom: "1px solid rgba(251,70,4,0.28)",
          boxShadow:
            "inset 0 1px 0 rgba(255,255,255,0.88), 0 6px 24px -12px rgba(251,70,4,0.25)",
        }}
      >
        <div
          className="marquee flex gap-10 whitespace-nowrap text-[11px] uppercase tracking-[0.28em] font-extrabold"
          style={{
            width: "max-content",
            color: "#1c1c1c",
            textShadow: "0 1px 0 rgba(255,255,255,0.7)",
          }}
        >
          {Array.from({ length: 10 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>AI Workflow Agency</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>Outreach Workflow</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>Content Workflow</span>
              <span style={{ color: "#fb4604" }}>✦</span>
              <span>by Digital Empire</span>
              <span style={{ color: "#fb4604" }}>✦</span>
            </span>
          ))}
        </div>
      </div>

      {/* Glow radiale orange centrale */}
      <div
        aria-hidden
        className="pointer-events-none absolute z-0"
        style={{
          width: 800,
          height: 600,
          left: "50%",
          top: "45%",
          transform: "translate(-50%, -50%)",
          background:
            "radial-gradient(ellipse, rgba(251,70,4,0.15) 0%, rgba(201,55,10,0.06) 40%, transparent 70%)",
          filter: "blur(70px)",
        }}
      />
      {/* Glow orange in basso a destra */}
      <div
        aria-hidden
        className="pointer-events-none absolute z-0"
        style={{
          width: 500,
          height: 400,
          right: "5%",
          bottom: "-8%",
          background:
            "radial-gradient(circle, rgba(251,70,4,0.10) 0%, transparent 70%)",
          filter: "blur(60px)",
        }}
      />

      {/* SILVER CHIPS */}
      <span className="silver-chip float-a" style={{ top: "22%", left: "4%" }}>
        <span className="dot" /> <strong>40+</strong> automazioni
      </span>
      <span className="silver-chip float-b" style={{ top: "30%", right: "4%" }}>
        <span className="dot" /> <strong>H24</strong> autonomia
      </span>
      <span className="silver-chip float-c" style={{ bottom: "35%", left: "3%" }}>
        <span className="dot" /> <strong>100%</strong> automatizzato
      </span>
      <span className="silver-chip float-d" style={{ bottom: "22%", right: "3%" }}>
        <span className="dot" /> Demo <strong>gratuita</strong>
      </span>

      <div className="container-default text-center relative z-[2] pt-24 pb-12 md:pt-40 md:pb-32 lg:pt-44 lg:pb-36">

        {/* BUBBLE */}
        <Reveal delay={0.10}>
          <span className="bubble-gold">
            <Sparkles className="h-3.5 w-3.5" />
            AI Workflow Agency · Outreach · Content · Digital Empire
          </span>
        </Reveal>

        {/* H1 */}
        <Reveal delay={0.25}>
          <h1 id="hero-h1" className="mt-8 mb-8">
            <span
              className="text-silver-white block"
              style={{ fontSize: "clamp(1.85rem, 4vw, 3.25rem)" }}
            >
              Automatizziamo la tua operatività
            </span>
            <span
              className="text-silver-gold font-accent italic block"
              style={{ fontSize: "clamp(3rem, 7.2vw, 5.8rem)", lineHeight: 1.05 }}
            >
              con AI Workflows.
            </span>
          </h1>
        </Reveal>

        {/* SUBHEAD */}
        <Reveal delay={0.50}>
          <p className="text-[1.05rem] md:text-[1.125rem] text-white/90 max-w-[58ch] mx-auto mb-11 leading-[1.80] font-light">
            Ogni giorno ripeti gli stessi task: cerchi lead a mano, pubblichi
            contenuti uno a uno, scrivi email di follow-up.{" "}
            <strong
              className="font-semibold"
              style={{
                background: "linear-gradient(135deg, #ffffff 0%, #e8e3ef 30%, #ffd0b0 58%, #ff8a4a 88%)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
                backgroundClip: "text",
              }}
            >
              Sei tu il collo di bottiglia del tuo business.
            </strong>{" "}
            Noi costruiamo{" "}
            <strong
              className="font-semibold"
              style={{
                background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 45%, #ff8a4a 80%, #ffffff 100%)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
                backgroundClip: "text",
              }}
            >
              sistemi AI che girano H24 in autonomia
            </strong>
            : Outreach Workflow e Content Workflow. Non ti vendiamo uno strumento.{" "}
            <span className="hl-block">
              Ti consegniamo un sistema già funzionante.
            </span>
          </p>
        </Reveal>

        {/* CTAs */}
        <Reveal delay={0.65}>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <MagneticButton href="#cta-finale" intensity={0.18}>
              <span className="btn-gold btn-gold--lg group">
                Prenota una demo
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </span>
            </MagneticButton>
            <a href="#servizi" className="btn-ghost group">
              Vedi come funziona
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
          </div>
        </Reveal>

        {/* SHIELD */}
        <Reveal delay={0.80}>
          <p className="mt-5 text-[0.875rem] text-white/60 inline-flex items-center gap-2">
            <Shield className="h-4 w-4 text-white/60" />
            Demo gratuita &nbsp;·&nbsp; Nessun impegno &nbsp;·&nbsp; Risposta entro 24h &nbsp;·&nbsp; Zero pitch
          </p>
        </Reveal>
      </div>
    </section>
  );
}
