"use client";

import { Reveal } from "@/components/reveal";
import { Check, X } from "lucide-react";

const PER_CHI = [
  "Fai outreach manualmente ogni giorno e vuoi automatizzarlo",
  "Pubblichi contenuti in modo irregolare per mancanza di tempo",
  "Hai un'offerta che funziona e vuoi l'operatività che tiene il passo",
  "Vuoi scalare il business senza assumere altra gente",
  "Sei pronto ad affidarti a un sistema, non a fare tutto tu",
];

const NON_PER_CHI = [
  "Stai ancora cercando cosa vendere (trova prima il prodotto)",
  "Vuoi qualcuno che faccia le cose al posto tuo ogni giorno",
  "Non sei disposto a mostrare i tuoi processi attuali (serve il contesto)",
  "Cerchi una soluzione istantanea senza un minimo di onboarding",
];

export function PerChi() {
  return (
    <section
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="perchi-h2"
    >
      <div className="container-default">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Onestà operativa
            </span>
            <h2 id="perchi-h2" className="mt-6">
              <span className="text-silver-white">Lavoriamo solo con</span>{" "}
              <span className="text-silver-gold font-accent italic">
                chi possiamo davvero aiutare.
              </span>
            </h2>
            <p className="mt-5 text-[1.05rem] text-white/90 leading-relaxed font-light">
              Non è una posa: è efficienza. Filtriamo a monte chi non è il
              match giusto, così entrambi non perdiamo tempo.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-5">
          {/* Per chi */}
          <Reveal delay={0.10}>
            <article className="card-silver-gold relative h-full">
              <div className="flex items-center gap-3 mb-6">
                <span
                  className="grid place-items-center w-11 h-11 rounded-xl"
                  style={{
                    background:
                      "linear-gradient(135deg, #fb4604 0%, #c93a0a 100%)",
                    boxShadow:
                      "0 4px 12px rgba(201,55,10,0.35), inset 0 1px 0 rgba(255,255,255,0.20)",
                  }}
                >
                  <Check className="h-5 w-5 text-white" strokeWidth={3} />
                </span>
                <h3 className="text-[1.25rem] font-bold text-[#0a0a0a]">
                  Lavoriamo con te se...
                </h3>
              </div>
              <ul className="flex flex-col gap-3.5">
                {PER_CHI.map((t, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-[0.96rem] text-[#0a0a0a]/85 leading-relaxed"
                  >
                    <Check
                      className="h-4 w-4 mt-1 shrink-0 text-[#fb4604]"
                      strokeWidth={3}
                    />
                    <span>{t}</span>
                  </li>
                ))}
              </ul>
            </article>
          </Reveal>

          {/* Non per chi */}
          <Reveal delay={0.20}>
            <article className="card-dark-red relative h-full">
              <div className="flex items-center gap-3 mb-6">
                <span
                  className="grid place-items-center w-11 h-11 rounded-xl"
                  style={{
                    background: "rgba(220,47,55,0.15)",
                    border: "1px solid rgba(220,47,55,0.25)",
                  }}
                >
                  <X className="h-5 w-5 text-[#DC2F37]" strokeWidth={2.5} />
                </span>
                <h3 className="text-[1.25rem] font-bold text-white">
                  Non lavoriamo con te se...
                </h3>
              </div>
              <ul className="flex flex-col gap-3.5">
                {NON_PER_CHI.map((t, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-[0.96rem] text-white/85 leading-relaxed"
                  >
                    <X
                      className="h-4 w-4 mt-1 shrink-0 text-[#DC2F37]/70"
                      strokeWidth={2.5}
                    />
                    <span>{t}</span>
                  </li>
                ))}
              </ul>
            </article>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
