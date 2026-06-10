"use client";

import { Check, X } from "lucide-react";
import { Reveal } from "@/components/reveal";

export function Overview() {
  return (
    <>
      {/* AUDIENCE */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center mb-24">
            <Reveal>
              <span className="bubble-orange mb-6">Il paradigma</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-4xl md:text-7xl font-black text-white leading-tight tracking-tighter">
                Il tuo percorso in 6 settimane; <br />
                <span className="text-orange italic font-medium">per te se:</span>
              </h2>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            <Reveal delay={0.2}>
              <div className="card-dark h-full">
                <div className="bubble-orange mb-10"><Check className="h-4 w-4" /> Pienamente indicato per:</div>
                <ul className="space-y-6 text-white/90 text-[17px] leading-relaxed font-medium">
                  {["Sai che l'AI è il futuro, ma non sai da dove iniziare concretamente.", "Hai usato ChatGPT ma ti sei fermato al 'e poi?' senza finalizzare nulla.", "Non sai programmare e pensi che questo ti tagli fuori dal mercato.", "Vuoi una competenza vendibile — non un altro corso nel cassetto."].map((s, i) => (
                    <li key={i} className="flex gap-4">
                      <Check className="h-6 w-6 text-orange shrink-0 mt-0.5" />
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>

            <Reveal delay={0.3}>
              <div className="card-dark h-full opacity-60 grayscale-[0.5]">
                <div className="bubble-silver mb-10"><X className="h-4 w-4" /> NON è per te se:</div>
                <ul className="space-y-6 text-white/60 text-[17px] leading-relaxed font-medium">
                  {["Sei già un developer esperto che cerca un corso avanzato di Python.", "Vuoi un trucchetto per 'fare soldi facili' senza lavorare.", "Non sei disposto a dedicare 3-5 ore a settimana per 6 settimane."].map((s, i) => (
                    <li key={i} className="flex gap-4">
                      <X className="h-6 w-6 text-white/20 shrink-0 mt-0.5" />
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* PROBLEMS */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center mb-20 reveal">
            <span className="bubble-orange mb-6">Il vero collo di bottiglia</span>
            <h2 className="text-4xl md:text-6xl font-black text-ink mb-10 leading-tight">Il problema non è l'AI. È che tutti ne parlano e <span className="text-orange italic font-medium">nessuno ti dice cosa FARE.</span></h2>
            <p className="text-xl text-ink/60 max-w-3xl mx-auto leading-relaxed">Apri LinkedIn: "L'AI cambierà tutto." Apri YouTube: "10 tool AI che devi conoscere." E poi? Tu hai provato ChatGPT. Hai fatto qualche domanda. E ti sei fermato.</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { t: "L'illusione del Prompt Manuale", d: "Tra 'usare l'app' e avere una competenza vendibile c'è un canyon. Non lo chiudi guardando video gratuiti." },
              { t: "La paralisi della scelta", d: "Compri corsi generici che ti mostrano 15 tool, ma nessuno ti insegna a costruire un sistema reale." },
              { t: "Risultati inconsistenti", d: "Provi a usare l'AI per lavoro ma i risultati sono mediocri e non presentabili a un cliente pagante." },
              { t: "L'onda che passa", d: "Il tempo passa. Chi impara ADESSO si posiziona come Architect. Chi aspetta, rincorrerà per sempre." },
            ].map((p, i) => (
              <Reveal key={i} delay={0.1 * i}>
                <div className="card-paper flex flex-col h-full bg-grey/20 border-ink/5 p-8">
                   <div className="text-orange font-black text-xl mb-4 italic tracking-tight">0{i+1}</div>
                   <h3 className="text-xl font-bold text-ink mb-4 leading-tight">{p.t}</h3>
                   <p className="text-sm text-ink/60 leading-relaxed font-medium">{p.d}</p>
                </div>
              </Reveal>
            ))}
          </div>

          <Reveal delay={0.4}>
            <div className="mt-24 p-10 md:p-16 bg-ink text-white rounded-[32px] relative overflow-hidden">
               <div className="corner-bracket corner-tl scale-75 opacity-20" />
               <div className="corner-bracket corner-br scale-75 opacity-20" />
               <div className="max-w-3xl relative z-10">
                 <h4 className="text-3xl md:text-5xl font-black mb-8 italic leading-tight">Il <span className="text-silver-orange">vero problema?</span></h4>
                 <p className="text-lg md:text-xl text-white/70 leading-relaxed mb-10">
                   Nessuno ti ha insegnato a <strong className="text-white">COSTRUIRE CON</strong> l'AI. C'è una differenza enorme tra chiedere qualcosa a ChatGPT e progettare un sistema che lavora per te.
                 </p>
                 <div className="text-silver-orange font-black italic text-lg uppercase tracking-widest border-t border-white/10 pt-8 inline-block">Quella differenza si chiama Claude Code.</div>
               </div>
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
