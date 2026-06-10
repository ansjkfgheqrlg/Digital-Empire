"use client";

import { ArrowRight, Shield, Sparkles } from "lucide-react";
import { Reveal } from "@/components/reveal";

const BOOKING_URL = "#offer";

export function Hero() {
  return (
    <section className="bg-ink relative overflow-hidden section border-b border-white/5">
      <div className="marquee-container absolute top-0 left-0 w-full z-10">
        <div className="marquee-inner">
          {Array.from({ length: 12 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>Claude Code Mastery 2026</span>
              <span className="text-orange">✦</span>
              <span>Tech-Lux Architecture</span>
              <span className="text-orange">✦</span>
              <span>Founding Members Only</span>
              <span className="text-orange">✦</span>
              <span>by Digital Empire</span>
              <span className="text-orange">✦</span>
            </span>
          ))}
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-6 py-24 md:py-48 text-center relative z-20">
        {/* Elite Chips */}
        <div className="hidden lg:block">
          <Reveal delay={0.8} variant="scale">
            <div className="silver-chip -rotate-3" style={{ top: "15%", left: "-5%" }}>
              <span className="dot" /> No-Code <strong>approach</strong>
            </div>
          </Reveal>
          <Reveal delay={1} variant="scale">
            <div className="silver-chip rotate-2" style={{ top: "25%", right: "-5%" }}>
              <span className="dot" /> Posti <strong>founding members</strong>
            </div>
          </Reveal>
          <Reveal delay={1.2} variant="scale">
            <div className="silver-chip rotate-6" style={{ bottom: "20%", left: "5%" }}>
              <span className="dot" /> <strong>30 giorni</strong> garanzia
            </div>
          </Reveal>
          <Reveal delay={1.4} variant="scale">
            <div className="silver-chip -rotate-1" style={{ bottom: "10%", right: "10%" }}>
              <span className="dot" /> <strong>Bonus 1:1</strong> incluso
            </div>
          </Reveal>
        </div>

        <Reveal>
          <span className="bubble-orange mb-10">
            <Sparkles className="h-4 w-4" /> Il primo percorso italiano su Claude Code
          </span>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="pre-headline mt-6">Digital Empire presenta · Mastery Series</div>
        </Reveal>

        <Reveal delay={0.2}>
          <h1 className="text-6xl md:text-8xl font-black leading-[1.02] tracking-tighter mb-10">
            <span className="text-silver-white">Da AI User a</span><br/>
            <span className="text-silver-orange">System Architect.</span>
          </h1>
        </Reveal>

        <Reveal delay={0.3}>
          <p className="text-xl md:text-2xl text-white/70 max-w-2xl mx-auto mb-14 leading-relaxed">
            Per chi vuole smettere di "chattare" con l'AI e iniziare a <strong className="text-silver-orange">costruire sistemi</strong> che generano profitto e liberano tempo. <span className="hl-block">In 6 settimane di formazione pura.</span>
          </p>
        </Reveal>

        <Reveal delay={0.4}>
          <div className="flex flex-col gap-6 items-center">
            <a href={BOOKING_URL} className="btn-orange btn-orange--lg group scale-110">
              Inizia il Percorso per €397
              <ArrowRight className="h-6 w-6 transition-transform group-hover:translate-x-1" />
            </a>
            <div className="flex items-center gap-6 text-[10px] uppercase font-bold tracking-[0.3em] text-white/30">
              <span className="flex items-center gap-2"><Shield className="h-3.5 w-3.5" /> Garanzia "Builder o Rimborsato"</span>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
