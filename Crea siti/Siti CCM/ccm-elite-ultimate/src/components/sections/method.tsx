"use client";

import { Reveal } from "@/components/reveal";

const pillars = [
  { t: "Ingegneri, non artisti.", d: "L'eccellenza non è un atto, ma un'abitudine organizzativa. Ogni progetto segue un'architettura rigorosa." },
  { t: "Vendiamo Profitto, non like.", d: "Sfruttiamo l'AI in modo architettato per massimizzare i risultati. Non giochiamo con i prompt." },
  { t: "Creiamo Imperi, non siti.", d: "Un impero digitale è dinamico e scalabile. Non cerchiamo clienti, ma partner con cui scalare." }
];

const steps = [
  { id: "01", time: "Settimane 1 e 2", title: "FONDAMENTA", d: "Installi Claude Code e impari il framework I.C.R.O. (Identità, Contesto, Regole, Output)." },
  { id: "02", time: "Settimana 3", title: "SISTEMI", d: "Crei le tue prime Skill specializzate con il framework S.K.I.L.L. Trasformiamo Claude da generalista a esperto." },
  { id: "03", time: "Settimane 4 e 5", title: "PORTFOLIO", d: "Costruisci 3 progetti reali: Content System, Analisi Competitor, Business Automation." },
  { id: "04", time: "Settimana 6", title: "MONETIZZAZIONE", d: "Definisci offerta e pricing. Identifichi 10 prospect reali con il metodo DAN." }
];

export function Method() {
  return (
    <>
      <section className="bg-grey section section-border-t">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-24">
            <Reveal>
              <span className="bubble-orange mb-6 text-[10px]">Differenziazione radicale</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-4xl md:text-7xl font-black text-silver-black leading-tight tracking-tighter">
                Perché <span className="text-orange italic font-medium">Mastery?</span>
              </h2>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {pillars.map((p, i) => (
              <Reveal key={i} delay={0.1 * i}>
                <div className="card-paper h-full flex flex-col hover:border-orange/30 transition-colors group">
                   <div className="w-12 h-12 rounded-full border border-orange flex items-center justify-center mb-8 group-hover:bg-orange transition-colors">
                      <div className="w-2 h-2 rounded-full bg-orange group-hover:bg-white" />
                   </div>
                   <h3 className="text-2xl font-black mb-6 text-ink leading-tight">{p.t}</h3>
                   <p className="text-ink/60 leading-relaxed font-medium flex-1">{p.d}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <div className="text-center mb-24">
            <Reveal>
              <span className="bubble-ink mb-6">Il programma</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-4xl md:text-6xl font-black text-ink leading-tight tracking-tighter">
                Claude Code Mastery: <br />
                <span className="text-orange italic font-medium">la roadmap di 6 settimane.</span>
              </h2>
            </Reveal>
          </div>

          <div className="space-y-12">
            {steps.map((s, i) => (
              <Reveal key={i} delay={0.1 * i}>
                <div className="flex flex-col sm:flex-row gap-8 items-start card-paper p-10 bg-grey/20 border-ink/5">
                   <div className="step-num shrink-0 shadow-lg">{s.id}</div>
                   <div className="flex-1">
                      <div className="text-[10px] font-black uppercase tracking-[0.3em] text-orange mb-3">{s.time}</div>
                      <h3 className="text-2xl font-black text-ink mb-4 italic uppercase tracking-tighter">{s.title}</h3>
                      <p className="text-ink/60 leading-relaxed font-medium">{s.d}</p>
                   </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
