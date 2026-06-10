"use client";

import { Reveal } from "@/components/reveal";
import { Check } from "lucide-react";

const ecosystem = [
  {
    n: "01",
    title: "Il Percorso Formativo Master",
    desc: "6 Moduli + Modulo 0 Setup. 21 video-lezioni ed esercizi pratici per un totale di 11 ore di documentazione tecnica ad alta densità.",
  },
  {
    n: "02",
    title: "I 4 Framework Proprietari",
    desc: "Metodologie originali per il controllo del flusso: I.C.R.O. per le istruzioni, S.K.I.L.L. per le entità, W.O.R.K. per i processi e DAN per l'outreach commerciale.",
  },
  {
    n: "03",
    title: "18 Template e Asset Scaricabili",
    desc: "Non devi inventare nulla. Ti diamo i file di configurazione e gli esempi compilati pronti da importare nel tuo ambiente di lavoro.",
  },
];

const bonuses = [
  {
    label: "Bonus #01",
    title: "15 Skill Pronte all'Uso",
    desc: "Libreria di file SKILL.md per Content, Analisi e Business. Li apri e funzionano. Risparmi 20+ ore di lavoro.",
    value: "Valore €197",
    isGold: false,
  },
  {
    label: "Bonus #02",
    title: "Kit Portfolio \"Pronto in 1 Ora\"",
    desc: "Template Notion duplicabile 3C + 3 Case Study pre-strutturati da personalizzare per i tuoi clienti.",
    value: "Valore €147",
    isGold: false,
  },
  {
    label: "Bonus #03",
    title: "Community & Live Q&A",
    desc: "Accesso per 3 mesi alla community privata. Una call di gruppo al mese per feedback diretto sui tuoi progetti.",
    value: "Valore €297",
    isGold: false,
  },
  {
    label: "Solo Primi 7 Giorni",
    title: "Sessione Strategica 1:1",
    desc: "30 minuti privati con me per impostare il tuo mercato target e il tuo posizionamento unico.",
    value: "Valore €197",
    isGold: true,
  },
];

export function Bonuses() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Vantaggio competitivo</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-white">Ecco l'</span>
              <span className="text-silver-orange">ecosistema</span>
              <br />
              <span className="text-silver-white">che ricevi </span>
              <span className="text-silver-orange">subito</span>
            </h2>
          </Reveal>
        </div>

        <div className="max-w-3xl mx-auto mb-20 space-y-12">
          {ecosystem.map((item, i) => (
            <Reveal key={i} delay={0.1 + i * 0.1}>
              <div className="flex gap-8 items-start">
                <div className="text-2xl font-black text-white/20 lining-nums">
                  {item.n}
                </div>
                <div>
                  <h4 className="text-xl md:text-2xl font-bold text-silver-white mb-2">
                    {item.title}
                  </h4>
                  <p className="text-white/60 leading-relaxed">
                    {item.desc}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-5">
          {bonuses.map((b, i) => (
            <Reveal key={i} delay={0.1 + i * 0.1}>
              <div className={`h-full flex flex-col p-6 rounded-2xl border ${
                b.isGold 
                  ? "bg-gradient-to-br from-[#FFD700]/10 to-[#B8860B]/20 border-[#FFD700]/30" 
                  : "bg-white/5 border-white/10"
              }`}>
                <span className={`text-[10px] font-bold uppercase tracking-widest mb-4 block ${
                  b.isGold ? "text-[#FFD700]" : "text-white/40"
                }`}>
                  {b.label}
                </span>
                <h3 className={`text-lg font-bold mb-3 ${b.isGold ? "text-white" : "text-silver-white"}`}>
                  {b.title}
                </h3>
                <p className="text-white/50 text-sm leading-relaxed mb-6 flex-1">
                  {b.desc}
                </p>
                <div className={`text-xs font-black uppercase tracking-wider ${
                  b.isGold ? "text-silver-orange" : "text-orange-pure"
                }`}>
                  {b.value}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
