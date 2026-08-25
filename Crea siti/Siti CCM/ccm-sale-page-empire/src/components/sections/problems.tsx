"use client";

import { X, Check } from "lucide-react";
import { Reveal } from "@/components/reveal";

export function Problems() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Il vero problema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              Il problema non è saper programmare.<br />
              <span className="text-orange-pure italic font-medium">È saper Architekturare.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <Reveal delay={0.2}>
            <div className="card-paper h-full">
              <div className="flex items-center gap-3 mb-6">
                <X className="h-5 w-5 text-[#b8b8b8]" />
                <h3 className="text-xl font-bold text-ink">L'approccio "Chat"</h3>
              </div>
              <ul className="space-y-4 text-ink/70">
                <li>Apri Claude, chiedi una cosa, speri che funzioni.</li>
                <li>Ricevi codice che non capisci e non sai dove incollare.</li>
                <li>Se si rompe qualcosa, torni nel loop del "Riprova".</li>
                <li>Risultato: <span className="font-bold">Frustrazione e tempo perso.</span></li>
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="card-orange h-full">
              <div className="flex items-center gap-3 mb-6">
                <Check className="h-5 w-5" />
                <h3 className="text-xl font-bold">L'approccio "Engineer"</h3>
              </div>
              <ul className="space-y-4">
                <li>Usi Claude Code per operare direttamente sul file system.</li>
                <li>Costruisci Agenti che sanno *cosa* fare e *come* farlo.</li>
                <li>Validazione deterministica: il sistema non sbaglia.</li>
                <li>Risultato: <span className="font-bold">Sistemi pronti per il mercato.</span></li>
              </ul>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
