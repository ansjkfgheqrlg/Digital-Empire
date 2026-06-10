"use client";

import { Check, X } from "lucide-react";
import { Reveal } from "@/components/reveal";

const audience_yes = [
  "Sai che l'AI è il futuro, ma non sai da dove iniziare concretamente.",
  "Hai usato ChatGPT ma ti sei fermato al \"e poi?\" senza finalizzare nulla.",
  "Non sai programmare e pensi che questo ti tagli fuori dal mercato.",
  "Vuoi una competenza vendibile — non un altro corso da mettere nel cassetto.",
];

const audience_no = [
  "Sei già un developer esperto che cerca un corso avanzato di Python.",
  "Vuoi un trucchetto per \"fare soldi facili con l'AI\" senza lavorare.",
  "Non sei disposto a dedicare 3-5 ore a settimana per 6 settimane.",
];

export function Audience() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Il paradigma</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4">
              <span className="text-silver-white">Il tuo percorso in 6 settimane; </span>
              <span className="text-orange-pure italic font-medium">per te se:</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <Reveal delay={0.2}>
            <div className="card-dark h-full">
              <div className="bubble-orange mb-6">
                <Check className="h-3.5 w-3.5" /> Pienamente indicato per:
              </div>
              <ul className="space-y-4">
                {audience_yes.map((s, i) => (
                  <li key={i} className="flex gap-3 text-white/90 text-sm md:text-base leading-relaxed">
                    <Check className="h-5 w-5 text-orange-pure shrink-0 mt-0.5" />
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="card-dark h-full opacity-70">
              <div className="bubble-silver mb-6">
                <X className="h-3.5 w-3.5" /> NON è per te se:
              </div>
              <ul className="space-y-4">
                {audience_no.map((s, i) => (
                  <li key={i} className="flex gap-3 text-white/60 text-sm md:text-base leading-relaxed">
                    <X className="h-5 w-5 text-white/30 shrink-0 mt-0.5" />
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
