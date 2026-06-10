"use client";

import { Reveal } from "@/components/reveal";
import { FAQAccordion } from "@/components/faq-accordion";

const FAQS = [
  {
    q: "Devo avere conoscenze tecniche per usare i workflow?",
    a: "Zero. Consegniamo tutto funzionante, integrato con i tuoi strumenti esistenti. Ti formiamo in 1 ora: come monitorare, come leggere i dati, cosa fare se qualcosa non va. Il resto gira da solo.",
  },
  {
    q: "In quanto tempo è pronto il workflow?",
    a: "3-4 settimane dalla firma. Discovery call → Blueprint → Build → Go Live. Non promettiamo 'in 48 ore' perché costruiamo sistemi reali, non template. Il tempo è investimento, non spreco.",
  },
  {
    q: "Quanto costa?",
    a: "Si parte da 5.000€ per workflow. I più complessi (multi-canale, CRM avanzato, integrazioni custom) arrivano a 15.000€. La demo è gratuita. In 30 minuti ti mostro cosa si può fare con il tuo budget specifico.",
  },
  {
    q: "Funziona davvero al 100% senza che io tocchi niente?",
    a: "Sì, per i task che definiamo insieme in fase di blueprint. Tu decidi quali attività automatizzare, noi le costruiamo. Quello che esula dai confini del workflow resta manuale. Il resto gira da solo.",
  },
  {
    q: "E se il workflow smette di funzionare?",
    a: "30 giorni di supporto incluso dopo il go-live. Monitoriamo le performance, gestiamo gli imprevisti, ottimizziamo. Dopo i 30 giorni, offriamo piani di manutenzione mensile se vuoi continuità.",
  },
  {
    q: "Fate ancora landing page?",
    a: "Sì, come servizio complementare. Ma se stai cercando il modo più efficace per scalare, un workflow fa 10x il lavoro di una landing page. Perché risolve il problema più grande: l'operatività che ti blocca.",
  },
];

export function FAQSection() {
  return (
    <section
      id="faq"
      className="bg-paper section relative overflow-hidden"
      aria-labelledby="faq-h2"
    >
      <div className="container-tight">
        <Reveal>
          <div className="text-center mb-12 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604" }} />
              Domande frequenti
            </span>
            <h2 id="faq-h2" className="mt-6">
              <span className="text-brand-navy">Quello che</span>{" "}
              <span className="text-brand-accent font-accent italic">
                ci chiedono.
              </span>
            </h2>
          </div>
        </Reveal>

        <Reveal delay={0.10}>
          <FAQAccordion items={FAQS} />
        </Reveal>
      </div>
    </section>
  );
}
