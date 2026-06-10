"use client";

import { Reveal } from "@/components/reveal";

const groups = [
  {
    title: "\"NON HO TEMPO PER UN ALTRO CORSO...\"",
    cards: [
      { t: "L'AI È IL TUO MOLTIPLICATORE.", d: "Non è un'altra cosa da fare, è il sistema definitivo per smettere di fare tutto il resto manualmente.", w: "C" },
      { t: "FRAMEWORK W.O.R.K. 10X.", d: "Applichi processi deterministici che riducono task di 4 ore a soli 12 minuti di esecuzione AI.", w: "P", isGold: true },
      { t: "LIBERTÀ OPERATIVA TOTALE.", d: "Claude Code lavora in background mentre tu ti occupi della strategia e della vendita.", w: "B" },
    ],
  },
  {
    title: "\"NON SONO UN PROGRAMMATORE, È TROPPO TECNICO...\"",
    cards: [
      { t: "DALLA SINTASSI ALLA LOGICA.", d: "Non devi scrivere codice, devi imparare a progettarlo. Claude è il tuo braccio operativo.", w: "C" },
      { t: "FRAMEWORK I.C.R.O. BUSSOLA.", d: "Forniamo i binari per ottenere risultati pro senza conoscere una riga di Python o Javascript.", w: "P", isGold: true },
      { t: "POSIZIONAMENTO ELITE.", d: "Ti posizioni sopra il 99% degli utenti. Diventi chi costruisce sistemi, non chi chatta.", w: "B" },
    ],
  },
  {
    title: "\"IL PREZZO È TROPPO ALTO PER UN CORSO...\"",
    cards: [
      { t: "VALORE DI UN SINGOLO ASSET.", d: "Un solo sistema AI venduto a un cliente copre 2 volte l'investimento totale del corso.", w: "C" },
      { t: "CASE STUDY RITORNO IMMEDIATO.", d: "Molti Builder chiudono la prima commessa da €500 prima della fine delle 6 settimane.", w: "P", isGold: true },
      { t: "UNA SKILL PERPETUA.", d: "Non compri un video-corso, compri la capacità di stampare valore on-demand in un mercato vergine.", w: "B" },
    ],
  },
];

export function Objections() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        {groups.map((g, gi) => (
          <div key={gi} className={gi !== 0 ? "mt-32" : ""}>
            <div className="text-center mb-12">
              <Reveal>
                <span className="bubble-orange mb-6">Gestione Obiezioni // Elite Builder</span>
              </Reveal>
              <Reveal delay={0.1}>
                <h2 className="text-[28px] md:text-[40px] font-bold leading-tight mt-6 max-w-3xl mx-auto">
                  <span className="text-silver-black">{g.title}</span>
                </h2>
              </Reveal>
            </div>

            <div className="grid md:grid-cols-3 gap-5">
              {g.cards.map((c, i) => (
                <Reveal key={i} delay={0.15 + i * 0.1}>
                  <div className={`relative overflow-hidden p-8 rounded-2xl border ${
                    c.isGold 
                      ? "bg-gradient-to-br from-orange-pure/10 to-transparent border-orange-pure/30" 
                      : "bg-[#1c1c1c]/5 border-[#1c1c1c]/10"
                  }`}>
                    <span className="text-[10px] uppercase tracking-widest font-black text-orange-pure/40 mb-6 block">
                      0{i + 1} // {i === 0 ? "CLAIM" : i === 1 ? "PROOF" : "BENEFIT"}
                    </span>
                    <h3 className="text-lg font-black text-silver-black mb-4 leading-tight">
                      {c.t}
                    </h3>
                    <p className="text-[#3a3a3a] text-sm leading-relaxed relative z-10">
                      {c.d}
                    </p>
                    <div className="absolute bottom-[-10px] right-0 text-[120px] font-black text-[#1c1c1c]/[0.02] leading-none pointer-events-none select-none">
                      {c.w}
                    </div>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
