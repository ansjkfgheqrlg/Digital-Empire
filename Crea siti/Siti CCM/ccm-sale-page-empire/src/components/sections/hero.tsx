"use client";

import { ArrowRight, Shield, Sparkles } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { cn } from "@/lib/utils";

const BOOKING_URL = "#pricing";

function CTA({ 
  large = false, 
  label = "Inizia il Percorso per €397" 
}: { large?: boolean; label?: string }) {
  return (
    <a href={BOOKING_URL} className={cn("btn-orange group", large && "btn-orange--lg")}>
      {label}
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}

export function Hero() {
  return (
    <section className="bg-ink relative overflow-hidden section-border-t">
      {/* Marquee */}
      <div className="border-b border-white/10 overflow-hidden py-3">
        <div className="marquee flex gap-10 whitespace-nowrap text-[10px] uppercase tracking-[0.25em] text-white/30" style={{ width: "max-content" }}>
          {Array.from({ length: 8 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>Claude Code Mastery</span>
              <span className="text-orange-pure">✦</span>
              <span>Tech-Lux Edition</span>
              <span className="text-orange-pure">✦</span>
              <span>Inizio Coorte 2026</span>
              <span className="text-orange-pure">✦</span>
              <span>by Digital Empire</span>
              <span className="text-orange-pure">✦</span>
            </span>
          ))}
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-6 py-24 md:py-32 text-center relative">
        {/* Silver Chips */}
        <span className="silver-chip float-a" style={{ top: "10%", left: "-2%" }}>
          <span className="dot" /> No-Code <strong>approach</strong>
        </span>
        <span className="silver-chip float-b" style={{ top: "20%", right: "-4%" }}>
          <span className="dot" /> Posti <strong>limitati</strong>
        </span>
        <span className="silver-chip float-c" style={{ bottom: "15%", left: "-3%" }}>
          <span className="dot" /> <strong>30 giorni</strong> garanzia
        </span>
        <span className="silver-chip float-d" style={{ bottom: "10%", right: "-2%" }}>
          <span className="dot" /> <strong>Bonus 1:1</strong> incluso
        </span>

        <Reveal>
          <span className="bubble-orange mb-8">
            <Sparkles className="h-3.5 w-3.5" /> Il primo percorso italiano su Claude Code
          </span>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="pre-headline mb-6">Digital Empire presenta · Mastery 2026</div>
        </Reveal>

        <Reveal delay={0.2}>
          <h1 className="text-[44px] md:text-[72px] font-extrabold leading-[1.05] tracking-tight mb-8">
            <span className="text-silver-white">Da AI User a</span>
            <br />
            <span className="text-silver-orange">System Architect.</span>
          </h1>
        </Reveal>

        <Reveal delay={0.3}>
          <p className="text-lg md:text-xl text-white/70 max-w-2xl mx-auto mb-12 leading-relaxed">
            Per chi vuole smettere di "chattare" con l'AI e iniziare a <strong className="text-silver-orange font-semibold">costruire sistemi</strong> che generano profitto e liberano tempo. In <span className="hl-block">6 settimane di formazione pura</span>.
          </p>
        </Reveal>

        <Reveal delay={0.4}>
          <div className="flex flex-col gap-5 items-center">
            <CTA large />
            <div className="flex items-center gap-4 text-xs uppercase tracking-widest text-white/40">
              <span className="flex items-center gap-1.5"><Shield className="h-3.5 w-3.5" /> Garanzia "Builder o Rimborsato"</span>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
