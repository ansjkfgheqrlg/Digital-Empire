"use client";

import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";
import { ArrowRight, Shield, TrendingUp } from "lucide-react";

export function PricingROI() {
  return (
    <section className="bg-ink section section-border-t" id="pricing">
      <div className="max-w-5xl mx-auto px-6 text-center">
        <Reveal>
          <span className="bubble-orange mb-6">L'investimento</span>
        </Reveal>
        <Reveal delay={0.1}>
          <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-16 mt-6">
            <span className="text-silver-white">Il valore reale di una </span>
            <span className="text-silver-orange">skill perpetua</span>
          </h2>
        </Reveal>

        <div className="max-w-4xl mx-auto">
          <Reveal delay={0.2}>
            <div className="card-silver-orange p-12 md:p-16 relative overflow-hidden text-center mb-12">
              <div className="absolute top-0 right-10 translate-y-[-50%] bg-orange-pure text-white text-[10px] uppercase font-black px-6 py-2 rounded-full tracking-[0.3em]">
                Founding Member Offer
              </div>
              
              <div className="text-sm uppercase tracking-[0.2em] text-[#2a2a2a]/60 mb-4 line-through">
                Valore Totale: € 2338
              </div>
              
              <div className="flex flex-col items-center justify-center mb-10">
                <span className="text-[80px] md:text-[120px] font-black leading-none text-silver-black lining-nums">
                  €397
                </span>
                <span className="text-xs uppercase tracking-[0.25em] text-[#fb4604] font-bold mt-4">
                  Pagamento Unico
                </span>
              </div>

              <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-10">
                <a href="https://buy.stripe.com/aFafZj9bU0J25sj9MDdby00" className="btn-orange btn-orange--lg group min-w-[300px]">
                  Sblocca il Mio Vantaggio Ora
                  <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
                </a>
                <CallCTA variant="dark" />
              </div>

              <div className="flex justify-center items-center gap-8 text-xs font-bold uppercase tracking-widest text-[#2a2a2a]/40">
                <span className="flex items-center gap-2">
                  <Shield className="h-4 w-4" /> Garanzia 30 Giorni
                </span>
                <span className="hidden sm:block">•</span>
                <span className="flex items-center gap-2 text-ink">
                  2 rate da €199 disponibili
                </span>
              </div>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="card-dark border-green-500/20 bg-green-500/5 p-8 text-left">
              <div className="flex items-start gap-6">
                <div className="w-12 h-12 rounded-full bg-green-500/10 flex items-center justify-center shrink-0">
                  <TrendingUp className="h-6 w-6 text-green-500" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white mb-2">Il Calcolo del R.O.I.</h3>
                  <p className="text-white/60 leading-relaxed text-[15px]">
                    Se nel Modulo 6 trovi anche solo <strong className="text-white font-bold underline decoration-orange-pure decoration-2 underline-offset-4 text-silver-white">un singolo cliente da €500</strong> (e ti insegno esattamente come), il corso è già ripagato. Tutto quello che viene dopo è profitto puro basato su una competenza che non scade mai.
                  </p>
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
