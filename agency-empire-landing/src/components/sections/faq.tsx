"use client";

import { Reveal } from "@/components/reveal";

const faqs = [
  { q: "In quanto tempo il sistema è operativo?", a: "7 giorni lavorativi dal contratto firmato. Giorno 7 il sistema è in produzione, testato e calibrato sul tuo brand. Non un prototipo: gira in autonomia dal primo giorno." },
  { q: "Ho bisogno di un server dedicato?", a: "No. Usiamo VPS cloud (DigitalOcean, Hetzner, AWS) con costi mensili minimi — di solito €5-20/mese. L'importante è che il server sia tuo: nessun lock-in sulla nostra infrastruttura." },
  { q: "Cosa succede se Instagram cambia qualcosa?", a: "Il sistema viene aggiornato. Per i 90 giorni di supporto inclusi, ogni aggiornamento di platform, API o detection viene gestito da noi senza costi aggiuntivi." },
  { q: "Posso acquistare un solo sistema invece di tutti e tre?", a: "Sì. Ogni implementazione (Outreach Factory, Content Factory, Second Brain) è acquistabile singolarmente. Molti clienti partono da uno e aggiungono gli altri dopo aver visto i risultati." },
  { q: "C'è una garanzia?", a: "Sì. 30 giorni: se il sistema non funziona come concordato entro quel periodo, lo sistemiamo noi senza costi aggiuntivi. Se il problema non è risolvibile, rimborso integrale. Il rischio è tutto nostro." },
];

export function FAQ() {
  return (
    <section className="bg-paper section">
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
