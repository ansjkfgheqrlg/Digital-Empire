"use client";

import { Reveal } from "@/components/reveal";

const services = [
  {
    n: "01",
    label: "Outreach Factory",
    title: "Acquisizione clienti su pilota automatico",
    items: [
      "Script di automazione Gmail: 300+ email personalizzate al giorno con APSOC framework",
      "Instagram DM safe: comportamento umano, proxy residenziali dedicati, zero rischio ban",
      "Qualificazione semantica AI: estrae i lead caldi e li notifica su Slack o CRM",
      "Follow-up automatico fino a 3 touchpoint per ogni prospect",
      "Dashboard web custom per monitorare lead, status e conversazioni",
      "Codice sorgente in chiaro + documentazione completa",
    ],
  },
  {
    n: "02",
    label: "Content Factory",
    title: "Fabbrica di contenuti social su richiesta",
    items: [
      "Generazione AI di caroselli Instagram (copy CRO-ottimizzato con APSOC per ogni slide)",
      "Script video per Reels: hook, corpo, CTA in formato 30-60 secondi",
      "Caption + hashtag strategici per massimizzare reach organico",
      "Grafiche visive dei caroselli costruite in automatico — pronte da pubblicare",
      "Upload organizzato su Google Drive per argomento e data",
      "Interfaccia web per configurare brief e scaricare output in 30 secondi",
    ],
  },
  {
    n: "03",
    label: "Second Brain",
    title: "Knowledge base aziendale intelligente",
    items: [
      "Sistema wiki strutturato su misura per il tuo business: prodotti, processi, clienti, decisioni",
      "Integrazione AI che risponde in tempo reale a qualsiasi domanda sulla tua knowledge base",
      "Aggiornamento continuo: ogni nuova informazione viene archiviata e resa ricercabile",
      "Elimina il caos di note disperse, chat perdute e memoria aziendale non strutturata",
      "Connessione a Notion, Google Drive, Obsidian o sistema personalizzato",
      "Accesso team: ogni membro trova ciò che cerca in secondi",
    ],
  },
];

export function MasteryMap() {
  return (
    <section className="bg-grey section section-border-t" id="servizi">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Cosa include · Ogni sistema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-black">Tre implementazioni. </span>
              <span className="text-orange-pure italic font-medium">Un&apos;operatività <span style={{ whiteSpace: "nowrap" }}>trasformata.</span></span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#3a3a3a] text-lg max-w-2xl mx-auto">
              Ogni servizio è un sistema AI completo — installato, testato e calibrato sul tuo brand. Acquisti solo ciò che ti serve.
            </p>
          </Reveal>
        </div>

        <div className="space-y-0 relative">
          {services.map((m, i) => (
            <Reveal key={i} delay={i * 0.05}>
              <div className="flex gap-6 py-10 border-b border-[#131313]/10 last:border-b-0 group">
                <div className="step-num shrink-0 group-hover:bg-orange-pure group-hover:text-white transition-colors duration-300">
                  {m.n}
                </div>
                <div>
                  <span className="text-xs font-bold uppercase tracking-[0.2em] text-orange-pure mb-2 block">
                    {m.label}
                  </span>
                  <h3 className="text-2xl md:text-3xl font-bold mb-4 text-silver-black">
                    {m.title}
                  </h3>
                  <ul className="space-y-2">
                    {m.items.map((item, idx) => (
                      <li key={idx} className="flex gap-3 text-[#3a3a3a] text-[15px]">
                        <span className="text-orange-pure mt-1">→</span>
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
