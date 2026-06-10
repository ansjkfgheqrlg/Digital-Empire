"use client";

import { Reveal } from "@/components/reveal";

const STEPS = [
  {
    letter: "F",
    title: "Flusso. Mappiamo tutto.",
    body:
      "Analizziamo ogni task ripetitivo del tuo business: outreach, follow-up, content, report. Mappiamo i flussi esistenti, identifichiamo i colli di bottiglia e decidiamo cosa automatizzare prima.",
  },
  {
    letter: "L",
    title: "Logica. Progettiamo il sistema.",
    body:
      "Costruiamo la logica AI: quali trigger attivano cosa, come si comporta il sistema in ogni scenario, quali dati usa per prendere decisioni. Niente black box. Ogni scelta è trasparente e documentata.",
  },
  {
    letter: "O",
    title: "Output. Costruiamo e testiamo.",
    body:
      "Sviluppiamo il workflow su dati reali del tuo business. Lo testiamo su lead reali, contenuti reali, flussi reali. Iteriamo finché non gira come deve. Niente consegne half-baked.",
  },
  {
    letter: "W",
    title: "Watch. Monitoriamo e ottimizziamo.",
    body:
      "Dopo il go-live monitoriamo le performance per 30 giorni. Dashboard in tempo reale, alert automatici, ottimizzazioni incluse. Il workflow migliora con il tempo, non peggiora.",
  },
];

export function MetodoAPSOC() {
  return (
    <section
      id="metodo"
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="metodo-h2"
    >
      <div className="container-default">
        <Reveal>
          <div className="text-center mb-16 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Il metodo
            </span>
            <h2 id="metodo-h2" className="mt-6">
              <span className="text-silver-white">Framework</span>{" "}
              <span className="text-silver-gold font-accent italic">F.L.O.W.</span>
            </h2>
            <p className="mt-5 text-[1.05rem] text-white/90 leading-relaxed font-light">
              Quattro fasi che ogni workflow che costruiamo attraversa in ordine.
              Niente improvvisazione: un processo testato su decine di
              automazioni reali.
            </p>
          </div>
        </Reveal>

        {/* Timeline */}
        <div className="relative max-w-3xl mx-auto">
          {/* Linea verticale */}
          <div
            className="absolute left-[1.5rem] top-2 bottom-2 w-px hidden md:block"
            style={{
              background:
                "linear-gradient(180deg, rgba(251,70,4,0) 0%, rgba(251,70,4,0.4) 12%, rgba(251,70,4,0.4) 88%, rgba(251,70,4,0) 100%)",
            }}
            aria-hidden
          />

          <ol className="flex flex-col gap-10 md:gap-12">
            {STEPS.map((s, i) => (
              <Reveal key={i} delay={i * 0.08}>
                <li className="flex items-start gap-5 md:gap-6 relative">
                  <span className="step-num">{s.letter}</span>
                  <div className="flex-1 pt-1.5">
                    <h3 className="text-[1.25rem] md:text-[1.40rem] font-bold text-white mb-2 leading-tight">
                      {s.title}
                    </h3>
                    <p className="text-[0.96rem] leading-relaxed text-white/90 font-light">
                      {s.body}
                    </p>
                  </div>
                </li>
              </Reveal>
            ))}
          </ol>
        </div>
      </div>
    </section>
  );
}
