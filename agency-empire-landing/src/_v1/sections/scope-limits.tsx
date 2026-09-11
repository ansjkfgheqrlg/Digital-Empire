"use client";

import { Reveal } from "@/components/reveal";
import { Ban } from "lucide-react";

/** A6 — la restrizione di scopo e' la prova di competenza piu' economica che esista.
 *  Dire di no a cinque cose rende credibile il si' sulle tre che facciamo. */
const notUs = [
  {
    what: "Gestione campagne ads",
    why: "Non le compriamo e non le ottimizziamo. Ti mandiamo da chi lo fa di mestiere.",
  },
  {
    what: "Social media management",
    why: "Produciamo i contenuti col sistema. Pubblicarli e rispondere ai commenti resta a te.",
  },
  {
    what: "Siti vetrina e restyling grafici",
    why: "Costruiamo infrastruttura operativa, non pagine da guardare.",
  },
  {
    what: "Consulenza strategica senza implementazione",
    why: "Non vendiamo slide. Se non finisce in codice che gira, non è il nostro lavoro.",
  },
  {
    what: "Contratti a canone mensile",
    why: "Per scelta, non per prezzo. Il canone ci renderebbe utile la tua dipendenza.",
  },
];

export function ScopeLimits() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-12">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Ban className="h-3.5 w-3.5" /> Per scelta, non per limite
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-white">Facciamo tre cose. </span>
              <span className="text-orange-pure italic font-medium">Queste cinque no.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/75 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Un fornitore che sa fare tutto non sa fare niente abbastanza bene da garantirlo.
            </p>
          </Reveal>
        </div>

        <div className="flex flex-col gap-3">
          {notUs.map((n, i) => (
            <Reveal key={n.what} delay={0.2 + i * 0.06}>
              <div
                className="rounded-xl px-6 py-5 flex flex-col sm:flex-row sm:items-baseline gap-2 sm:gap-6"
                style={{
                  background: "rgba(249,249,249,0.03)",
                  border: "1px solid rgba(249,249,249,0.09)",
                }}
              >
                <span className="text-white/90 text-[15px] font-semibold sm:w-[280px] shrink-0">
                  {n.what}
                </span>
                <span className="text-white/60 text-[14px] leading-relaxed">{n.why}</span>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
