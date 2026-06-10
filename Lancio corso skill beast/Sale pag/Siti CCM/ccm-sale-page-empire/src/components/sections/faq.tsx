"use client";

import { Reveal } from "@/components/reveal";

const faqs = [
  { q: "Serve saper programmare?", a: "No. Il corso è progettato per chi vuole usare l'AI come braccio operativo. Imparerai l'architettura, non la sintassi." },
  { q: "Quanto tempo devo dedicare?", a: "Consigliamo almeno 3-5 ore a settimana per seguire le lezioni e applicare i workflow sul tuo caso reale." },
  { q: "Cosa succede se mi fermo?", a: "Avrai accesso a vita alla piattaforma e a tutti gli aggiornamenti futuri. L'AI corre veloce, noi corriamo con lei." },
  { q: "C'è una garanzia?", a: "Sì, 30 giorni 'Builder o Rimborsato'. Se dopo 4 settimane non senti di aver acquisito una competenza trasformativa, ti rimborsiamo l'intero importo." },
];

export function FAQ() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-3xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">FAQ</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              Domande frequenti.
            </h2>
          </Reveal>
        </div>

        <div className="space-y-4">
          {faqs.map((f, i) => (
            <Reveal key={i} delay={0.2 + i * 0.05}>
              <div className="border-b border-ink/10 py-6">
                <h3 className="text-xl font-bold text-orange-pure mb-2">{f.q}</h3>
                <p className="text-ink/70 leading-relaxed font-medium">{f.a}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
