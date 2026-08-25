"use client";

import { Reveal } from "@/components/reveal";
import { ArrowRight } from "lucide-react";

const bonuses = [
  { id: "01", title: "15 Skill Pronte all'Uso", price: "€197", d: "Libreria di file SKILL.md per Content, Analisi e Business. Li apri e funzionano." },
  { id: "02", title: "Portfolio Kit 'Pronto'", price: "€147", d: "Template Notion duplicabile 3C + 3 Case Study pre-strutturati da personalizzare." },
  { id: "03", title: "Community & Live Q&A", price: "€297", d: "Accesso per 3 mesi alla community privata. Una call di gruppo al mese per feedback." },
  { id: "Session", title: "Sessione Strategica 1:1", price: "€197", d: "30 minuti privati con Max per impostare il tuo mercato target e posizionamento.", limited: "Solo Primi 7 Giorni" }
];

const faqs = [
  { q: "€397 è troppo, ci sono tutorial gratis.", a: "I tutorial ti insegnano un comando. Noi ti diamo un sistema architettonico. Se un solo lavoro ripaga il corso, qual è il vero rischio?" },
  { q: "Non so programmare. È per me?", a: "Claude Code scrive il codice per te. Tu devi imparare a dare istruzioni come un Architect. Se sai spiegare un concetto in italiano, sai usare Claude Code." },
  { q: "Claude cambia ogni mese — scadrà?", a: "I principi dell'ingegneria di contesto no. I framework I.C.R.O. e S.K.I.L.L. funzionano indipendentemente dalla versione del modello." },
  { q: "Come trovo davvero dei clienti?", a: "Il Modulo 6 è dedicato interamente a questo. Creiamo l'offerta, il portfolio, e contattiamo prospect con script ad alta conversione." }
];

export function Ecosystem() {
  return (
    <>
      {/* BONUSES */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-24">
            <Reveal>
              <span className="bubble-orange mb-6 text-[10px]">Vantaggio competitivo</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-4xl md:text-7xl font-black text-ink leading-tight tracking-tighter">
                L'ecosistema che <br />
                <span className="text-orange italic font-medium">ricevi subito.</span>
              </h2>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {bonuses.map((b, i) => (
              <Reveal key={i} delay={0.1 * i}>
                <div className={`card-paper flex flex-col h-full border-dashed ${b.limited ? "bg-orange/5 border-orange/20" : "bg-grey/10 border-ink/5"}`}>
                   <div className="flex justify-between items-start mb-10">
                      <div className="step-num bg-ink text-white scale-75 origin-top-left">{b.id}</div>
                      {b.limited && <span className="text-[9px] font-black uppercase tracking-widest text-orange bg-orange/10 px-2 py-1 rounded-full">{b.limited}</span>}
                   </div>
                   <h3 className="text-xl font-black text-ink mb-4 leading-tight uppercase tracking-tighter italic">{b.title}</h3>
                   <p className="text-sm text-ink/60 leading-relaxed font-semibold mb-10 flex-1">{b.d}</p>
                   <div className="text-3xl font-black text-ink/20 italic tracking-tighter border-t border-ink/5 pt-6">{b.price}</div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="bg-grey section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <div className="text-center mb-24">
            <Reveal>
              <span className="bubble-ink mb-6">Supporto & Chiarezza</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-4xl md:text-6xl font-black text-ink leading-tight tracking-tighter">
                Dubbi <span className="text-orange italic font-medium">Comuni.</span>
              </h2>
            </Reveal>
          </div>

          <div className="space-y-6">
            {faqs.map((f, i) => (
              <Reveal key={i} delay={0.05 * i}>
                <div className="card-paper p-10 bg-white/50 border-ink/5 group hover:border-orange/20 transition-all">
                  <h3 className="text-xl font-black text-ink mb-4 italic group-hover:text-orange transition-colors">{f.q}</h3>
                  <p className="text-ink/60 leading-relaxed font-medium">{f.a}</p>
                </div>
              </Reveal>
            ))}
          </div>

          <Reveal delay={0.4}>
            <div className="mt-24 p-12 bg-white rounded-[32px] border-2 border-orange border-dashed text-center">
               <h4 className="text-2xl font-black mb-4 text-ink italic">Garanzia "Builder o Rimborsato"</h4>
               <p className="text-ink/60 max-w-2xl mx-auto leading-relaxed">
                 Segui il corso per 30 giorni. Completa i primi 4 moduli. Se dopo aver costruito le tue Skill non senti di aver acquisito una competenza trasformativa, <strong className="text-orange">ti rimborsiamo tutto.</strong>
               </p>
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
