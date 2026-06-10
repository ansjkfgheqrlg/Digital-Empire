"use client";

import { Reveal } from "@/components/reveal";
import { ArrowRight, Shield, Target } from "lucide-react";

export function FinalCTA() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div className="corner-bracket corner-tl" />
      <div className="corner-bracket corner-tr" />
      <div className="corner-bracket corner-bl" />
      <div className="corner-bracket corner-br" />

      <div className="max-w-5xl mx-auto px-6 relative z-10 text-center">
        <Reveal>
          <span className="bubble-orange mb-12">Adesso hai due opzioni.</span>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-6 mb-20 text-left">
          <Reveal delay={0.1}>
            <div className="card-dark ring-1 ring-white/5 opacity-50 p-8 h-full flex flex-col">
              <span className="text-xs font-bold uppercase tracking-widest text-white/30 mb-4 block">Opzione A</span>
              <h3 className="text-2xl font-bold text-white mb-4">La routine</h3>
              <p className="text-white/40 text-[15px] leading-relaxed">
                Chiudi questa pagina. Torni alla tua routine. Continui a usare l'AI in modo casuale e tra 6 mesi sei esattamente dove sei oggi, mentre altri hanno già conquistato il mercato.
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.2}>
            <div className="card-dark border-orange-pure/30 bg-orange-pure/5 p-8 h-full flex flex-col relative overflow-hidden">
              <div className="absolute top-4 right-4 text-orange-pure opacity-20">
                <Target className="h-12 w-12" />
              </div>
              <span className="text-xs font-bold uppercase tracking-widest text-orange-pure mb-4 block">Opzione B</span>
              <h3 className="text-2xl font-bold text-silver-white mb-4">Il salto</h3>
              <p className="text-white/70 text-[15px] leading-relaxed">
                Entri in Claude Code Mastery. Tra 6 settimane hai una competenza che vale €500 o €800 per progetto, un portfolio reale e una skill che l'AI non può rimpiazzare, perché sei tu a controllarla.
              </p>
            </div>
          </Reveal>
        </div>

        <div className="max-w-4xl mx-auto">
          <Reveal delay={0.3}>
            <h2 className="text-4xl md:text-6xl font-extrabold mb-8">
              <span className="text-silver-white">Pronto a diventare un</span>
              <br />
              <span className="text-silver-orange">System Architect?</span>
            </h2>
          </Reveal>

          <Reveal delay={0.4}>
            <div className="flex flex-col gap-6 items-center">
              <a href="#offer" className="btn-orange btn-orange--lg group scale-110">
                Deciso. Iniziamo.
                <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
              </a>
              <div className="flex items-center gap-2 text-sm text-white/40">
                <Shield className="h-4 w-4" /> Founding Members limitati · Posti in esaurimento
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
