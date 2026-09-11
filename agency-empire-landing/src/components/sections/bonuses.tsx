"use client";

import { Reveal } from "@/components/reveal";

const ecosystem = [
  {
    n: "01",
    title: "Il sistema AI completo installato",
    desc: "Il codice sorgente funzionante, deployato sui tuoi server, testato e pronto a girare in produzione dal giorno del go-live. Non un prototipo: un sistema reale.",
  },
  {
    n: "02",
    title: "Dashboard web custom",
    desc: "Interfaccia React/Next.js dedicata per monitorare lead, configurare brief contenuti e scaricare output. Costruita su misura per la tua operatività.",
  },
  {
    n: "03",
    title: "APSOC Framework calibrato sul tuo brand",
    desc: "Il copy engine AI addestrato sul tuo ICP, tono di voce e framework copywriting. Ogni messaggio, ogni caption, ogni script — scritto come se lo scrivessi tu.",
  },
];

const bonuses = [
  {
    label: "Incluso nel setup",
    title: "Configurazione proxy residenziali",
    desc: "IP residenziali dedicati per blindare ogni account. Setup completo incluso senza costi aggiuntivi.",
    value: "Valore €350",
    isGold: false,
  },
  {
    label: "Incluso nel setup",
    title: "Integrazione Slack / CRM",
    desc: "Notifiche real-time per ogni lead qualificato. Arriva direttamente dove lavora il tuo team.",
    value: "Valore €200",
    isGold: false,
  },
  {
    label: "90 giorni inclusi",
    title: "Supporto tecnico dedicato",
    desc: "Accesso diretto a noi per 90 giorni dopo il go-live. Ogni problema risolto, ogni aggiornamento gestito.",
    value: "Valore €500",
    isGold: false,
  },
  {
    label: "Solo prime 3 implementazioni",
    title: "Formazione team inclusa",
    desc: "Sessione di formazione dal vivo con il tuo team su come usare la dashboard, leggere i lead e gestire i brief contenuti.",
    value: "Valore €300",
    isGold: true,
  },
];

export function Bonuses() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Cosa è incluso</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-black">Non solo il codice. </span>
              <span className="text-orange-pure italic font-medium">L&apos;infrastruttura</span>
              <br />
              <span className="text-silver-black">pronta a </span>
              <span className="text-orange-pure italic font-medium">girare da sola.</span>
            </h2>
          </Reveal>
        </div>

        <div className="max-w-3xl mx-auto mb-20 space-y-12">
          {ecosystem.map((item, i) => (
            <Reveal key={i} delay={0.1 + i * 0.1}>
              <div className="flex gap-8 items-start">
                <div className="text-2xl font-black text-orange-pure/40 lining-nums">
                  {item.n}
                </div>
                <div>
                  <h4 className="text-xl md:text-2xl font-bold text-[#0a0a0a] mb-2">
                    {item.title}
                  </h4>
                  <p className="text-[#2a2a2a] leading-relaxed">
                    {item.desc}
                  </p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-5">
          {bonuses.map((b, i) => (
            <Reveal key={i} delay={0.1 + i * 0.1}>
              <div className="card-silver-orange h-full flex flex-col !p-6">
                <span className="text-[10px] font-extrabold uppercase tracking-widest mb-4 block text-[#6a2c10]">
                  {b.label}
                </span>
                <h3 className="text-lg font-bold mb-3 text-[#0a0a0a]">
                  {b.title}
                </h3>
                <p className="text-[#1c1c1c]/85 text-sm leading-relaxed mb-6 flex-1 font-medium">
                  {b.desc}
                </p>
                <div className="text-xs font-black uppercase tracking-wider text-[#fb4604]">
                  {b.value}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
