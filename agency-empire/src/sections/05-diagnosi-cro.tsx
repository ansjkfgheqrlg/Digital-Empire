"use client";

import { Reveal } from "@/components/reveal";
import { Inbox, Calendar, BellOff, AlertTriangle } from "lucide-react";

const DIAGNOSI = [
  {
    num: "01",
    icon: Inbox,
    title: "Outreach Manuale",
    body:
      "Ogni giorno cerchi contatti a mano, scrivi messaggi uno a uno, e il numero di lead non cresce mai abbastanza. Stai scambiando il tuo tempo con risultati che un sistema farebbe in 10 minuti.",
    label: "Il tuo tempo vale troppo per questo",
  },
  {
    num: "02",
    icon: Calendar,
    title: "Contenuti Irregolari",
    body:
      "Pubblichi quando riesci, cioè in modo discontinuo. L'algoritmo premia la costanza, tu non puoi permettertela perché non hai un sistema. Risultato: visibilità a singhiozzo.",
    label: "La costanza richiede un sistema, non volontà",
  },
  {
    num: "03",
    icon: BellOff,
    title: "Follow-up Dimenticati",
    body:
      "Il 80% delle vendite avviene dopo il 5° contatto. Quanti follow-up fai davvero? Quanti lead caldi stai perdendo perché non li hai ricontattati in tempo?",
    label: "I soldi sono nei follow-up che non fai",
  },
  {
    num: "04",
    icon: AlertTriangle,
    title: "Sei il Collo di Bottiglia",
    body:
      "Per far crescere il business devi fare di più. Ma non puoi fare di più perché sei già al limite. Non è un problema di capacità. È un problema di sistema: sei tu il limite della tua crescita.",
    label: "Finché fai tutto tu, non puoi scalare",
  },
];

const iconBoxStyle: React.CSSProperties = {
  background: "rgba(255,255,255,0.14)",
  border: "1px solid rgba(255,255,255,0.30)",
  boxShadow: "0 4px 12px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.20)",
};

export function DiagnosiCRO() {
  return (
    <section
      id="diagnosi"
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="diagnosi-h2"
    >
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Diagnosi operativa
            </span>
            <h2 id="diagnosi-h2" className="mt-6">
              <span className="text-silver-white">I 4 segnali che la tua operatività</span>{" "}
              <span className="text-silver-gold font-accent italic">
                ti sta costando clienti.
              </span>
            </h2>
            <p className="mt-5 text-[1.0625rem] text-white/90 leading-relaxed font-light">
              Non è colpa tua. È che nessuno ti ha ancora costruito i sistemi
              giusti. Se riconosci anche solo uno di questi segnali, hai un
              problema di operatività, non di prodotto.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-5">
          {DIAGNOSI.map((d, i) => {
            const Icon = d.icon;
            return (
              <Reveal key={i} delay={0.10 + i * 0.06}>
                <article className="card-silver-purple h-full flex flex-col">
                  <div className="flex items-start justify-between mb-5">
                    <span className="font-display text-[1.5rem] font-bold text-white tracking-[0.04em]" style={{ textShadow: "0 1px 0 rgba(0,0,0,0.4)" }}>
                      {d.num}
                    </span>
                    <span
                      className="grid place-items-center w-10 h-10 rounded-xl"
                      style={iconBoxStyle}
                    >
                      <Icon className="h-4 w-4 text-white" />
                    </span>
                  </div>
                  <h4 className="text-[1.125rem] font-bold mb-3 text-white">
                    {d.title}
                  </h4>
                  <p className="text-[0.92rem] leading-relaxed mb-5 flex-1 text-white/90">
                    {d.body}
                  </p>
                  <div
                    className="pt-4 border-t text-[0.7rem] uppercase tracking-[0.18em] font-bold"
                    style={{
                      borderColor: "rgba(255,255,255,0.20)",
                      color: "#ffffff",
                      opacity: 0.90,
                      textShadow: "0 1px 2px rgba(0,0,0,0.50)",
                    }}
                  >
                    {d.label}
                  </div>
                </article>
              </Reveal>
            );
          })}
        </div>
      </div>
    </section>
  );
}
