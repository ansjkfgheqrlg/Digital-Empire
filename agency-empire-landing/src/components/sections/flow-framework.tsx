"use client";

import { Reveal } from "@/components/reveal";

const steps = [
  {
    letter: "F",
    title: "Flusso. Mappiamo tutto.",
    desc: "Analizziamo ogni task ripetitivo del tuo business: outreach, follow-up, content, report. Mappiamo i flussi esistenti, identifichiamo i colli di bottiglia e decidiamo cosa automatizzare prima.",
  },
  {
    letter: "L",
    title: "Logica. Progettiamo il sistema.",
    desc: "Costruiamo la logica AI: quali trigger attivano cosa, come si comporta il sistema in ogni scenario, quali dati usa per prendere decisioni. Niente black box. Ogni scelta è trasparente e documentata.",
  },
  {
    letter: "O",
    title: "Output. Costruiamo e testiamo.",
    desc: "Sviluppiamo il workflow su dati reali del tuo business. Lo testiamo su lead reali, contenuti reali, flussi reali. Iteriamo finché non gira come deve. Niente consegne half-baked.",
  },
  {
    letter: "W",
    title: "Watch. Monitoriamo e ottimizziamo.",
    desc: "Dopo il go-live monitoriamo le performance per 30 giorni. Dashboard in tempo reale, alert automatici, ottimizzazioni incluse. Il workflow migliora nel tempo, non peggiora.",
  },
];

export function FlowFramework() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.08) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-3xl mx-auto px-6 relative">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Il metodo</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6">
              <span className="text-silver-white">Framework </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  letterSpacing: "0.04em",
                }}
              >
                F.L.O.W.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/80 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Quattro fasi che ogni workflow che costruiamo attraversa in ordine. Niente
              improvvisazione: un processo testato su decine di automazioni reali.
            </p>
          </Reveal>
          {/* AGGIUNTA G2 (dossier 41, ordine di Max 15/09) — sotto il sottotitolo, una freccia sottile
              ferma che scende verso il basso-destra fino a una nota, sullo spazio vuoto a destra della
              colonna (il gutter della section, visibile solo da 1024px). Solo riga aggiunta: nessuna riga
              di giugno toccata. Testo in brief/COPY-F6-beta.md §G2. CSS: f6-frecce.css (.fl-nota*). */}
          <div className="fl-nota" aria-hidden="true">
            <svg className="fl-nota-svg" viewBox="0 0 60 56" focusable="false">
              <defs>
                <marker id="fl-nota-punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M4,2 C24,2 40,30 52,48" fill="none" stroke="#fb4604" strokeWidth="1.3" markerEnd="url(#fl-nota-punta)" />
            </svg>
            <p className="fl-nota-testo">
              Questo è un framework generico e sintetico: serve a far capire, in modo vago, come lavoriamo.
              Ogni lavoro è personalizzato e diverso — F.L.O.W. è uno slogan, non il progetto.
            </p>
          </div>
        </div>

        <div className="relative">
          {/* Vertical connector line */}
          <div
            aria-hidden="true"
            className="absolute left-[22px] top-8 bottom-8 w-px"
            style={{
              background:
                "linear-gradient(180deg, transparent 0%, rgba(251,70,4,0.4) 10%, rgba(251,70,4,0.4) 90%, transparent 100%)",
            }}
          />

          <div className="space-y-10">
            {steps.map((s, i) => (
              <Reveal key={i} delay={0.15 + i * 0.1}>
                <div className="flex gap-6 items-start">
                  {/* Letter icon */}
                  <div
                    className="shrink-0 w-11 h-11 rounded-xl flex items-center justify-center text-white font-black text-[18px] relative z-10"
                    style={{
                      background:
                        "radial-gradient(circle at 30% 30%, #fb4604, #8f2a02 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.25), 0 4px 20px -4px rgba(251,70,4,0.6)",
                    }}
                  >
                    {s.letter}
                  </div>

                  <div className="pt-1.5">
                    <h3 className="text-[20px] md:text-[24px] font-bold text-silver-white mb-2 leading-tight">
                      {s.title}
                    </h3>
                    <p className="text-white/82 text-[15px] leading-relaxed">
                      {s.desc}
                    </p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
