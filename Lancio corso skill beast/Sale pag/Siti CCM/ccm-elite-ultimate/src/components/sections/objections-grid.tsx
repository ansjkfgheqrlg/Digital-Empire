"use client";

import { Reveal } from "@/components/reveal";

const objections = [
  {
    q: "Non ho tempo per un altro corso...",
    responses: [
      { type: "claim", t: "MOLTIPLICATORE DI TEMPO.", d: "Ogni ora qui te ne ridà 10 indietro. Non è un peso, è il sistema per smettere di fare tutto il resto a mano.", w: "C" },
      { type: "proof", t: "AUTOMAZIONE 10X.", d: "Con W.O.R.K. riduci task da 4 ore a 12 minuti. Risultati tangibili fin dal Modulo 1.", w: "P" },
      { type: "benefit", t: "LIBERTÀ OPERATIVA.", d: "Claude lavora in background. Tu ti occupi della strategia e della vendita. Riprendi il controllo.", w: "B" },
    ]
  },
  {
    q: "Non sono un programmatore...",
    responses: [
      { type: "claim", t: "LOGICA DI SISTEMA.", d: "Tu sei la mente, Claude è il braccio. Non devi scrivere codice, devi progettarlo.", w: "C" },
      { type: "proof", t: "I.C.R.O. COME BUSSOLA.", d: "Risultati professionali senza conoscere Python o JS. È Context Engineering puro.", w: "P" },
      { type: "benefit", t: "ELITE ARCHITECT.", d: "Sei chi costruisce i sistemi proprietari, non chi si limita a chattare con un bot pubblico.", w: "B" },
    ]
  },
  {
    q: "Il prezzo è alto per un corso...",
    responses: [
      { type: "claim", t: "VALUE DI MERCATO.", d: "Un singolo sistema AI venduto a un cliente copre 2 volte l'investimento. Il resto è margine.", w: "C" },
      { type: "proof", t: "CASE STUDY RITORNO.", d: "I nostri Builder chiudono la prima commessa da €500+ prima della fine delle 6 settimane.", w: "P" },
      { type: "benefit", t: "SKILL PERPETUA.", d: "Compri la capacità di stampare valore on-demand in un mercato vergine che ha fame di AI reale.", w: "B" },
    ]
  }
];

export function ObjectionsGrid() {
  return (
    <section className="bg-ink py-32 section-border-t overflow-hidden">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-20">
          <Reveal>
            <h2 className="text-2xl md:text-5xl font-black text-white italic tracking-widest opacity-20 mb-6 uppercase">--- GESTIONE OBIEZIONI // ELITE BUILDER</h2>
          </Reveal>
          <Reveal delay={0.1}>
            <h3 className="text-4xl md:text-6xl font-black text-white">Sposta il tuo destino <br /><span className="text-silver-orange italic">in 45 minuti.</span></h3>
          </Reveal>
        </div>

        <div className="space-y-32">
          {objections.map((group, gIdx) => (
            <div key={gIdx} className="reveal">
              <div className="flex items-center gap-6 mb-12">
                <div className="h-px bg-white/10 flex-1" />
                <h4 className="text-2xl font-black text-orange uppercase tracking-tighter italic">{group.q}</h4>
                <div className="h-px bg-white/10 flex-1" />
              </div>

              <div className="grid md:grid-cols-3 gap-6">
                {group.responses.map((r, i) => (
                  <Reveal key={i} delay={i * 0.1}>
                    <div className="relative p-8 rounded-2xl border border-white/5 bg-white/[0.02] overflow-hidden group hover:border-orange/30 transition-all duration-500 h-full">
                      <div className="absolute -bottom-4 -right-2 text-9xl font-black italic text-white/[0.03] pointer-events-none group-hover:text-orange/[0.05] transition-colors">{r.w}</div>
                      <div className="text-[10px] font-black tracking-[0.3em] text-orange mb-4 uppercase">{r.type}</div>
                      <h5 className="text-xl font-bold text-white mb-4 tracking-tight leading-tight">{r.t}</h5>
                      <p className="text-sm text-white/50 leading-relaxed font-medium">
                        {r.d}
                      </p>
                    </div>
                  </Reveal>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
