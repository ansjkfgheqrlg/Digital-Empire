"use client";

import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";
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
            <div className="card-dark ring-1 ring-white/5 p-8 h-full flex flex-col">
              <span className="text-xs font-bold uppercase tracking-widest text-white/55 mb-4 block">Opzione A · Lo status quo</span>
              <h3 className="text-2xl font-bold text-white/80 mb-4">Continui come prima</h3>
              <p className="text-white/72 text-[15px] leading-relaxed">
                Chiudi questa pagina. Torni a fare outreach a mano, contenuti slide per slide, informazioni disperse
                ovunque. Tra 6 mesi sei esattamente dove sei oggi — mentre il tuo competitor che ha implementato
                il sistema ha già mandato 50.000 messaggi personalizzati.
              </p>
            </div>
          </Reveal>

          <Reveal delay={0.2}>
            <div className="card-dark border-orange-pure/30 bg-orange-pure/5 p-8 h-full flex flex-col relative overflow-hidden">
              <div className="absolute top-4 right-4 text-orange-pure opacity-20">
                <Target className="h-12 w-12" />
              </div>
              <span className="text-xs font-bold uppercase tracking-widest text-orange-pure mb-4 block">Opzione B</span>
              <h3 className="text-2xl font-bold text-silver-white mb-4">Implementi il sistema</h3>
              <p className="text-white/70 text-[15px] leading-relaxed">
                Prenoti una chiamata strategica gratuita. In 30 minuti capiamo insieme quale sistema ha il maggiore
                impatto sulla tua operatività. In 7 giorni è in produzione. Da quel momento lavora per te h24 —
                senza canoni mensili, senza dipendenze, con il codice in mano.
              </p>
            </div>
          </Reveal>
        </div>

        <div className="max-w-4xl mx-auto">
          <Reveal delay={0.3}>
            <h2 className="text-4xl md:text-6xl font-extrabold mb-8">
              <span className="text-silver-white">Pronto a far lavorare</span>
              <br />
              <span className="text-silver-orange">il sistema per te?</span>
            </h2>
          </Reveal>

          <Reveal delay={0.4}>
            <div className="flex flex-col gap-6 items-center">
              <div className="flex flex-col sm:flex-row gap-3 items-center justify-center">
                <CallCTA variant="dark" className="scale-110" />
              </div>
              <div className="flex items-center gap-2 text-sm font-semibold text-white/80">
                <Shield className="h-4 w-4 text-orange-pure" /> Chiamata gratuita · 30 minuti · Nessun impegno
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
