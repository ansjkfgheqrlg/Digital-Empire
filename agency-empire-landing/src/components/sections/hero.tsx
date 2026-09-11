"use client";

import { ArrowRight, Shield, Sparkles } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CALL_URL } from "@/components/call-cta";
import { cn } from "@/lib/utils";

function CTA({
  large = false,
  label = "Prenota una Chiamata Gratuita",
}: { large?: boolean; label?: string }) {
  return (
    <a
      href={CALL_URL}
      target="_blank"
      rel="noopener noreferrer"
      className={cn("btn-orange group", large && "btn-orange--lg")}
    >
      {label}
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}

export function Hero() {
  return (
    <section className="bg-ink relative overflow-hidden section-border-t">
      {/* Marquee */}
      <div
        className="overflow-hidden py-3 relative"
        style={{
          background: "linear-gradient(90deg, #d9d4d0 0%, #f4f1ee 18%, #ffffff 35%, #ffd9c2 55%, #fb4604 75%, #f4f1ee 92%, #d9d4d0 100%)",
          borderTop: "1px solid rgba(255,255,255,0.7)",
          borderBottom: "1px solid rgba(251,70,4,0.35)",
          boxShadow: "inset 0 1px 0 rgba(255,255,255,0.9), 0 6px 24px -12px rgba(251,70,4,0.5)",
        }}
      >
        <div className="marquee flex gap-10 whitespace-nowrap text-[11px] uppercase tracking-[0.28em] font-extrabold text-[#0a0a0a]" style={{ width: "max-content", textShadow: "0 1px 0 rgba(255,255,255,0.6)" }}>
          {Array.from({ length: 8 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>Digital Empire</span>
              <span className="text-[#fb4604]">✦</span>
              <span>Outreach Factory</span>
              <span className="text-[#fb4604]">✦</span>
              <span>Content Factory · Second Brain · AI Proprietaria</span>
              <span className="text-[#fb4604]">✦</span>
              <span>Implementazioni AI · 2026</span>
              <span className="text-[#fb4604]">✦</span>
            </span>
          ))}
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-6 py-24 md:py-32 text-center relative">
        {/* Silver Chips */}
        <span className="silver-chip float-a hidden md:inline-flex" style={{ top: "10%", left: "-2%" }}>
          <span className="dot" /> <strong>7 giorni</strong> · setup completo
        </span>
        <span className="silver-chip float-b hidden md:inline-flex" style={{ top: "20%", right: "-4%" }}>
          <span className="dot" /> <strong>€0</strong> canoni mensili
        </span>
        <span className="silver-chip float-c hidden md:inline-flex" style={{ bottom: "15%", left: "-3%" }}>
          <span className="dot" /> <strong>300+</strong> email al giorno
        </span>
        <span className="silver-chip float-d hidden md:inline-flex" style={{ bottom: "10%", right: "-2%" }}>
          <span className="dot" /> <strong>Codice</strong> tuo per sempre
        </span>

        <Reveal>
          <span className="bubble-orange mb-8">
            <Sparkles className="h-3.5 w-3.5" /> Automazione AI Proprietaria · 2026
          </span>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="pre-headline mb-6">Digital Empire · Agency · Automazione AI Proprietaria</div>
        </Reveal>

        <Reveal delay={0.2}>
          <h1 className="mb-10 text-center" style={{ letterSpacing: 0 }}>
            {/* Intro line — stesso colore di operatività */}
            <span
              className="block font-semibold text-silver-white"
              style={{
                fontSize: "clamp(22px, 3.2vw, 42px)",
                letterSpacing: "-0.02em",
                lineHeight: 1.2,
                marginBottom: "0.02em",
              }}
            >
              Automatizziamo la tua
            </span>

            {/* Hero word — MASSICCIO, fulcro visivo */}
            <span
              className="block font-black text-silver-white"
              style={{
                fontSize: "clamp(82px, 13.5vw, 148px)",
                letterSpacing: "-0.05em",
                lineHeight: 0.88,
              }}
            >
              operatività
            </span>

            {/* Accent line — grande, colorata */}
            <span
              className="block font-extrabold text-silver-orange"
              style={{
                fontSize: "clamp(44px, 7vw, 88px)",
                letterSpacing: "-0.035em",
                lineHeight: 1.0,
                marginTop: "0.03em",
              }}
            >
              con AI Workflows.
            </span>
          </h1>
        </Reveal>

        <Reveal delay={0.3}>
          <p className="text-lg md:text-xl text-white/70 max-w-3xl mx-auto mb-10 leading-relaxed">
            Ogni giorno ripeti gli stessi task: cerchi lead a mano, pubblichi contenuti uno a uno, scrivi email di follow-up.{" "}
            <strong className="text-white/90 font-semibold">Sei tu il collo di bottiglia del tuo business.</strong>{" "}
            Noi costruiamo sistemi AI che girano H24 senza di te:{" "}
            <strong className="text-silver-orange font-semibold">Outreach Factory e Content Factory</strong>.{" "}
            Non ti vendiamo uno strumento.{" "}
            <span className="hl-block">Ti consegniamo un sistema <span style={{ whiteSpace: "nowrap" }}>già funzionante.</span></span>
          </p>
        </Reveal>

        <Reveal delay={0.4}>
          <div className="flex flex-col gap-5 items-center">
            <div className="flex flex-col sm:flex-row gap-3 items-center justify-center">
              <CTA large />
            </div>
            <a
              href="#prenota"
              className="text-sm font-medium text-white/70 hover:text-white transition-colors"
            >
              Vedi prezzi e pacchetti ↓
            </a>
            <div className="flex items-center gap-4 text-xs uppercase tracking-widest text-white/75 font-semibold">
              <span className="flex items-center gap-1.5"><Shield className="h-3.5 w-3.5 text-orange-pure" /> Setup in 7 giorni · Garanzia di funzionamento · Zero dipendenze</span>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
