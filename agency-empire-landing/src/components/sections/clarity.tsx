"use client";

import { Reveal } from "@/components/reveal";
import { Phone, FileText, PenLine, Server, Rocket, HeadphonesIcon } from "lucide-react";

const steps = [
  {
    icon: Phone,
    time: "Giorno 0",
    title: "Chiamata Strategica gratuita",
    desc: "30 minuti per analizzare la tua operatività, capire dove perdi più tempo e quali sistemi hanno il maggiore impatto. Nessun impegno.",
  },
  {
    icon: FileText,
    time: "Entro 24 ore",
    title: "Proposta Tecnica personalizzata",
    desc: "Ricevi una proposta con stack esatto, tempi di consegna e investimento. Massima trasparenza, zero sorprese. Sei libero di accettare o no.",
  },
  {
    icon: PenLine,
    time: "Stesso giorno",
    title: "Contratto & onboarding",
    desc: "Accordo chiaro, firmato digitalmente. Raccogliamo i dati tecnici che ci servono: account, accessi, brand brief, ICP e obiettivi.",
  },
  {
    icon: Server,
    time: "Giorni 1–7",
    title: "Setup & installazione completa",
    desc: "Installiamo il sistema sui tuoi server, configuriamo proxy, account e workflow. Ogni componente testato in autonomia prima del go-live.",
  },
  {
    icon: Rocket,
    time: "Giorno 7",
    title: "Calibrazione & go-live",
    desc: "Addestriamo il sistema sul tuo brand, ICP e framework APSOC. Sessione di formazione sulla dashboard. Il sistema parte in produzione.",
  },
  {
    icon: HeadphonesIcon,
    time: "90 giorni",
    title: "Supporto tecnico dedicato",
    desc: "Accesso diretto a noi per i primi 90 giorni. Ogni problema risolto, ogni aggiornamento gestito. Poi il sistema gira da solo — per sempre.",
  },
];

export function Clarity() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Massima chiarezza // Zero zone grigie</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Cosa succede </span>
              <span className="text-orange-pure italic font-medium">esattamente</span>
              <span className="text-silver-black"> dopo la chiamata.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#2a2a2a]/75 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Dal primo contatto al sistema in produzione: 7 giorni. Ecco la sequenza precisa, passo per passo.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          {steps.map((s, i) => {
            const Icon = s.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.06}>
                <div className="card-paper rounded-2xl p-6 h-full flex gap-5 hover-lift">
                  <div
                    className="shrink-0 w-12 h-12 rounded-xl flex items-center justify-center"
                    style={{
                      background:
                        "radial-gradient(circle at 30% 30%, rgba(251,70,4,0.18), rgba(251,70,4,0.04) 65%, transparent 80%)",
                      border: "1px solid rgba(251,70,4,0.35)",
                    }}
                  >
                    <Icon className="h-5 w-5 text-orange-pure" strokeWidth={1.8} />
                  </div>
                  <div>
                    <div className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure mb-1">
                      {s.time}
                    </div>
                    <h3 className="text-lg font-black text-silver-black mb-2 leading-tight">
                      {s.title}
                    </h3>
                    <p className="text-[#2a2a2a]/78 text-sm leading-relaxed">{s.desc}</p>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>

        <Reveal delay={0.5}>
          <div className="mt-12 text-center">
            <p className="text-[13px] uppercase tracking-[0.2em] font-bold text-[#2a2a2a]/60">
              <span className="text-orange-pure">→</span> Codice sorgente tuo · Zero canoni mensili · Garanzia 30 giorni
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
