"use client";

import { Check, X } from "lucide-react";
import { Reveal } from "@/components/reveal";

const SENZA_WORKFLOW = [
  "Cerchi lead a mano ogni giorno, uguale a ieri",
  "Pubblichi contenuti quando riesci, cioè mai abbastanza",
  "I follow-up li fai quando ci ricordi",
  "Passi più tempo a fare che a vendere",
  "Risultato: sei tu il collo di bottiglia",
];

const CON_WORKFLOW = [
  "Sistema AI che trova e contatta lead H24 in autonomia",
  "Contenuti generati, schedulati e pubblicati in automatico",
  "Follow-up infiniti. Il sistema non dimentica mai.",
  "Tu fai solo le call con i lead già caldi",
  "Risultato: scala senza assumere nessuno",
];

export function Problema() {
  return (
    <section
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="problema-h2"
    >
      <div className="container-default">
        <Reveal>
          <div className="text-center mb-12 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Il problema
            </span>
            <h2 id="problema-h2" className="mt-6">
              <span className="text-silver-white">Il problema che blocca</span>{" "}
              <span className="text-silver-gold font-accent italic">
                il 90% dei business.
              </span>
            </h2>
            <p className="mt-5 text-[1.05rem] text-white/90 leading-relaxed font-light">
              Non è la motivazione. Non è la strategia. Non è il prodotto. È
              che{" "}
              <strong className="text-white/90 font-semibold">
                l&apos;operatività ti mangia il tempo
              </strong>{" "}
              e non riesci mai a scalare perché sei sempre in modalità esecuzione.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-5 max-w-5xl mx-auto">
          {/* LEFT — Senza workflow */}
          <Reveal delay={0.10}>
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
                  La tua giornata senza workflow
                </h3>
              </div>
              <ul className="flex flex-col gap-3.5">
                {SENZA_WORKFLOW.map((t, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-[0.96rem] text-white/90 leading-relaxed"
                  >
                    <X
                      className="h-4 w-4 mt-1 shrink-0 text-[#DC2F37]/80"
                      strokeWidth={2.5}
                    />
                    <span>{t}</span>
                  </li>
                ))}
              </ul>
              <p
                className="mt-6 pt-5 text-[0.85rem] uppercase tracking-[0.16em] font-semibold"
                style={{
                  borderTop: "1px solid rgba(220,47,55,0.20)",
                  color: "#DC2F37",
                }}
              >
                Risultato: sei il collo di bottiglia
              </p>
            </article>
          </Reveal>

          {/* RIGHT — Con workflow */}
          <Reveal delay={0.20}>
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
                  La tua giornata con i workflow
                </h3>
              </div>
              <ul className="flex flex-col gap-3.5">
                {CON_WORKFLOW.map((t, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-[0.96rem] text-[#0a0a0a]/90 leading-relaxed"
                  >
                    <Check
                      className="h-4 w-4 mt-1 shrink-0 text-[#fb4604]"
                      strokeWidth={3}
                    />
                    <span>{t}</span>
                  </li>
                ))}
              </ul>
              <p className="mt-6 pt-5 border-t border-black/15 text-[0.85rem] uppercase tracking-[0.16em] text-[#fb4604] font-semibold">
                Risultato: tempo libero, più clienti
              </p>
            </article>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
