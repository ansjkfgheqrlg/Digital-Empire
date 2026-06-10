"use client";

import { Reveal } from "@/components/reveal";
import { ArrowRight, Shield } from "lucide-react";

export function FinalCTA() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div className="corner-bracket corner-tl opacity-30" />
      <div className="corner-bracket corner-tr opacity-30" />
      <div className="corner-bracket corner-bl opacity-30" />
      <div className="corner-bracket corner-br opacity-30" />

      <div className="max-w-4xl mx-auto px-6 text-center relative z-10">
        <Reveal>
          <span className="bubble-orange mb-10">Founding Member Offer</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2 className="text-5xl md:text-8xl font-black mb-12 leading-tight tracking-tighter">
            <span className="text-silver-white">Adesso hai</span><br />
            <span className="text-silver-orange italic">due opzioni.</span>
          </h2>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-8 mb-20 text-left">
          <Reveal delay={0.2}>
            <div className="card-dark opacity-40 grayscale h-full border-dashed">
               <div className="text-[10px] font-black uppercase tracking-[0.3em] text-white/30 mb-8 underline decoration-orange decoration-2">Opzione A</div>
               <h4 className="text-2xl font-black text-white mb-6">Routine Stagnante</h4>
               <p className="text-sm text-white/50 leading-relaxed font-medium">Chiudi questa pagina. Torni a usare l'AI in modo casuale. Tra 6 mesi sei esattamente dove sei oggi, mentre altri hanno già conquistato il mercato.</p>
            </div>
          </Reveal>
          <Reveal delay={0.3}>
            <div className="card-dark border-orange/40 bg-orange/5 h-full">
               <div className="text-[10px] font-black uppercase tracking-[0.3em] text-orange mb-8 underline decoration-orange decoration-2 underline-offset-4">Opzione B</div>
               <h4 className="text-2xl font-black text-white mb-6">Elite Architecture</h4>
               <p className="text-sm text-white/90 leading-relaxed font-medium">Entri in Mastery. Tra 6 settimane hai una competenza che vale €500+ per progetto, un portfolio reale e una skill che l'AI non può rimpiazzare.</p>
            </div>
          </Reveal>
        </div>

        <Reveal delay={0.4}>
          <div className="flex flex-col gap-8 items-center">
            <a href="#offer" className="btn-orange btn-orange--lg group scale-110">
              Deciso. Iniziamo per €397
              <ArrowRight className="h-6 w-6 transition-transform group-hover:translate-x-1" />
            </a>
            <div className="flex flex-col gap-4 text-center">
              <div className="flex items-center justify-center gap-3 text-[11px] uppercase font-bold tracking-[0.3em] text-white/30">
                <Shield className="h-4 w-4" /> Pagamento sicuro · Protocollo SSL
              </div>
              <p className="text-[10px] text-orange/60 font-black uppercase tracking-widest italic">Valore Totale Asset: €2.338</p>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
