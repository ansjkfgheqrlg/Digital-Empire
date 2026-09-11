"use client";

import { Reveal } from "@/components/reveal";
import { Server, LayoutDashboard, Shield, Bot, Bell, BookOpen } from "lucide-react";

const assets = [
  {
    icon: Server,
    tag: "Core Engine",
    t: "Il sistema AI completo",
    d: "Il codice sorgente dell'automazione installato sui tuoi server. Outreach, Content Factory o Second Brain: è tuo, gira dove vuoi.",
  },
  {
    icon: LayoutDashboard,
    tag: "Dashboard Web",
    t: "Pannello di controllo custom",
    d: "Interfaccia React/Next.js per monitorare lead, status conversazioni e output. Configuri brief, scarichi contenuti, tutto in 30 secondi.",
  },
  {
    icon: Shield,
    tag: "Proxy Setup",
    t: "Configurazione proxy residenziali",
    d: "IP residenziali dedicati per ogni account Instagram. Setup completo incluso: nessun rischio ban, comportamento umano simulato.",
  },
  {
    icon: Bot,
    tag: "AI Copy Engine",
    t: "APSOC Framework calibrato",
    d: "L'engine copy addestrato sul tuo brand, ICP e framework APSOC. Ogni messaggio, ogni caption, ogni script — scritto su misura.",
  },
  {
    icon: Bell,
    tag: "CRM Notifiche",
    t: "Integrazione Slack / CRM",
    d: "Ogni lead qualificato dall'AI arriva direttamente su Slack o nel tuo CRM. Con profilo, contesto e score. Zero lavoro manuale.",
  },
  {
    icon: BookOpen,
    tag: "Documentazione + Supporto",
    t: "90 giorni di supporto dedicato",
    d: "Manuale tecnico completo del sistema + 90 giorni di accesso diretto a noi. Ogni problema viene risolto. Garantito per contratto.",
  },
];

export function PowerDeck() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.10) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-6xl mx-auto px-6 relative">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Cosa ricevi · Tutto incluso</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6">
              <span className="text-silver-white">Non solo il sistema. </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  letterSpacing: "-0.01em",
                }}
              >
                L'infrastruttura completa.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/82 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Ogni implementazione include <strong className="text-silver-orange">sei componenti distinti</strong> — non
              solo il codice, ma tutto quello che serve per far girare il sistema in autonomia dal giorno uno.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5">
          {assets.map((a, i) => {
            const Icon = a.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.06} variant="scale">
                <div
                  className="relative rounded-2xl p-6 h-full overflow-hidden hover-lift"
                  style={{
                    background:
                      "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                    border: "1px solid rgba(220,220,218,0.22)",
                    boxShadow:
                      "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                  }}
                >
                  <div
                    aria-hidden="true"
                    className="pointer-events-none absolute inset-0 rounded-2xl"
                    style={{
                      background:
                        "linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 40%, transparent 70%, rgba(251,70,4,0.08) 100%)",
                    }}
                  />
                  <div className="relative">
                    <div className="flex items-center gap-3 mb-5">
                      <div
                        className="w-11 h-11 rounded-xl flex items-center justify-center shrink-0"
                        style={{
                          background:
                            "radial-gradient(circle at 30% 30%, rgba(251,70,4,0.5), rgba(251,70,4,0.15) 60%, rgba(255,240,225,0.08) 90%)",
                          border: "1px solid rgba(251,70,4,0.5)",
                          boxShadow: "0 0 20px -6px rgba(251,70,4,0.5), inset 0 1px 0 rgba(255,255,255,0.2)",
                        }}
                      >
                        <Icon className="h-5 w-5 text-white" strokeWidth={1.8} />
                      </div>
                      <span className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure">
                        {a.tag}
                      </span>
                    </div>
                    <h3 className="text-[18px] md:text-[20px] font-black text-silver-white mb-3 leading-tight">
                      {a.t}
                    </h3>
                    <p className="text-[13.5px] text-white/70 leading-relaxed">{a.d}</p>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>

        <Reveal delay={0.5}>
          <p className="text-center text-white/82 text-[15px] max-w-2xl mx-auto mt-12 leading-relaxed">
            <span className="text-orange-pure">→</span> Tutto consegnato al completamento del setup.{" "}
            <span className="text-silver-orange font-semibold">Il sistema è tuo per sempre.</span>
          </p>
        </Reveal>
      </div>
    </section>
  );
}
