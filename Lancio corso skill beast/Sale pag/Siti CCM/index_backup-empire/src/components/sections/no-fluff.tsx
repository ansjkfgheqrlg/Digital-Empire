"use client";

import { Reveal } from "@/components/reveal";
import { X, Check, FastForward } from "lucide-react";

const out = [
  "50 video su \u201Ccome scrivere il prompt perfetto\u201D",
  "2 ore per spiegarti come si installa Claude Desktop",
  "Teoria accademica sul funzionamento dei Large Language Models",
  "Ore di storytelling su \u201Ccosa è l'AI\u201D e \u201Ccome siamo arrivati qui\u201D",
  "Prompt-engineering travestito da corso avanzato",
];

const inList = [
  "Basi tecniche (installazione, prompting, account) condensate e velocissime \u2014 zero passaggi saltati, zero minuti sprecati",
  "Architettura di System AI deterministici dal Modulo 1",
  "Orchestrazione di Agenti, Skill e System Prompt su casi reali",
  "Framework proprietari I.C.R.O. · S.K.I.L.L. · M.A.P. · W.O.R.K. · D.A.N.",
  "Come vendere i tuoi System AI a €500\u2013€2.000 per progetto",
];

export function NoFluff() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">
              <FastForward className="h-3.5 w-3.5" /> Zero fluff // Massima densità
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Non perdiamo tempo con le </span>
              <span className="text-orange-pure italic font-medium">basi infinite.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#2a2a2a]/78 text-lg max-w-3xl mx-auto mt-6 leading-relaxed">
              Installazione, account, prompting base: li vediamo{" "}
              <strong className="text-silver-black">nei minimi dettagli, senza saltare un passaggio</strong>, ma in modo
              rapido e chirurgico. Poi si entra subito nel vero valore: architettura, orchestrazione, monetizzazione.{" "}
              <span className="text-orange-pure font-semibold">Qui non si chiacchiera. Si costruisce.</span>
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          <Reveal delay={0.2}>
            <div
              className="rounded-2xl p-7 h-full"
              style={{
                background: "linear-gradient(160deg, #ffffff 0%, #f1ede6 100%)",
                border: "1px solid rgba(28,28,28,0.12)",
                boxShadow: "0 10px 30px -15px rgba(0,0,0,0.15)",
              }}
            >
              <div className="flex items-center gap-2 mb-5">
                <span className="inline-block w-6 h-[2px] bg-[#1c1c1c]/40" />
                <span className="text-[10px] uppercase tracking-[0.22em] font-black text-[#1c1c1c]/55">
                  Quello che NON trovi qui
                </span>
              </div>
              <ul className="space-y-3">
                {out.map((o, i) => (
                  <li key={i} className="flex items-start gap-3 text-[#2a2a2a]/80 text-[14px] leading-relaxed">
                    <X className="h-4 w-4 text-[#1c1c1c]/40 shrink-0 mt-[3px]" />
                    <span className="line-through decoration-[#1c1c1c]/25">{o}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div
              className="rounded-2xl p-7 h-full"
              style={{
                background:
                  "linear-gradient(160deg, rgba(251,70,4,0.08) 0%, rgba(251,70,4,0.02) 60%, transparent 100%)",
                border: "1px solid rgba(251,70,4,0.4)",
                boxShadow: "0 10px 30px -12px rgba(251,70,4,0.25)",
              }}
            >
              <div className="flex items-center gap-2 mb-5">
                <span className="inline-block w-6 h-[2px] bg-orange-pure" />
                <span className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure">
                  Quello che trovi dal Modulo 1
                </span>
              </div>
              <ul className="space-y-3">
                {inList.map((o, i) => (
                  <li key={i} className="flex items-start gap-3 text-[#1c1c1c] text-[14px] leading-relaxed font-medium">
                    <Check className="h-4 w-4 text-orange-pure shrink-0 mt-[3px]" />
                    <span>{o}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>

        <Reveal delay={0.45}>
          <p className="text-center mt-12 text-[13px] uppercase tracking-[0.22em] font-black text-[#1c1c1c]/60">
            <span className="text-orange-pure">→</span> Formazione di vero valore. Densa. Operativa. Senza riempitivi.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
