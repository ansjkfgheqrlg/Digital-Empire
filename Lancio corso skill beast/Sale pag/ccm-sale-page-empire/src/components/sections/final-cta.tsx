"use client";

import { Reveal } from "@/components/reveal";
import { ArrowRight, Shield } from "lucide-react";

export function FinalCTA() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div className="corner-bracket corner-tl" />
      <div className="corner-bracket corner-tr" />
      <div className="corner-bracket corner-bl" />
      <div className="corner-bracket corner-br" />

      <div className="max-w-4xl mx-auto px-6 text-center relative z-10">
        <Reveal>
          <span className="bubble-orange mb-8 text-sm">Founding Member Offer</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2 className="text-4xl md:text-6xl font-extrabold mb-8">
            <span className="text-silver-white">Pronto a diventare un</span>
            <br />
            <span className="text-silver-orange">System Architect?</span>
          </h2>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="text-xl text-white/70 mb-12 max-w-2xl mx-auto">
            Accedi ora a <strong className="text-silver-orange">Claude Code Mastery</strong> con lo sconto Early Bird riservato ai primi 20 membri.
          </p>
        </Reveal>

        <Reveal delay={0.3}>
          <div className="flex flex-col gap-6 items-center">
            <a href="#offer" className="btn-orange btn-orange--lg group scale-110">
              Assicura il Tuo Posto per €397
              <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
            </a>
            <div className="flex items-center gap-2 text-sm text-white/40">
              <Shield className="h-4 w-4" /> Pagamento sicuro · Garanzia 30 Giorni
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
