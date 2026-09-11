"use client";

import { Reveal } from "@/components/reveal";
import { ShieldCheck, Zap, Sparkles, Code2 } from "lucide-react";

const groups = [
  {
    icon: Zap,
    eyebrow: "Obiezione #01 · Il tool",
    title: "“ChatGPT fa già tutto questo, gratis.”",
    kicker: "ChatGPT è una chat. Questo è un sistema.",
    cards: [
      { kind: "CLAIM", t: "ChatGPT non manda 300 email al giorno.", d: "Una chat risponde a domande. Un sistema autentica account, gestisce proxy, calibra timing, qualifica risposte e notifica su Slack — in automatico, h24.", w: "C" },
      { kind: "PROOF", t: "Outreach reale vs prompt manuale.", d: "Un utente ChatGPT manda ancora i messaggi a mano, uno ad uno. Il nostro sistema manda 300+ messaggi personalizzati al giorno, con follow-up automatici.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Il sistema lavora mentre dormi.", d: "ChatGPT si ferma quando chiudi il browser. Il sistema AI proprietario gira h24 sui tuoi server, indipendentemente da te.", w: "B" },
    ],
  },
  {
    icon: ShieldCheck,
    eyebrow: "Obiezione #02 · Il rischio ban",
    title: "“Ma Instagram mi banna se automatizzo.”",
    kicker: "Proxy residenziali dedicati. Zero rischio.",
    cards: [
      { kind: "CLAIM", t: "Il sistema simula comportamento umano.", d: "Timing randomizzato, pause naturali, sequenze di azioni che replicano un utente reale. I detection system di Instagram non vedono un bot.", w: "C" },
      { kind: "PROOF", t: "Proxy residenziali per ogni account.", d: "Ogni profilo Instagram ha il suo IP residenziale dedicato. Stesso IP di un utente reale, nella stessa area geografica. Zero shared proxy.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Blindatura tecnica inclusa nel setup.", d: "Configurazione proxy, warm-up account progressivo, rate limiting intelligente. Il setup antidetection è parte integrante del sistema — non un extra.", w: "B" },
    ],
  },
  {
    icon: Sparkles,
    eyebrow: "Obiezione #03 · La qualità copy",
    title: "“Il copy generato dall’AI sembra robotico.”",
    kicker: "APSOC Framework calibrato sul tuo ICP.",
    cards: [
      { kind: "CLAIM", t: "Il problema non è l'AI. È il prompt.", d: "Un modello generico scrive in modo generico. Il nostro sistema usa APSOC Framework, addestrato sul tuo brand, il tuo ICP e il tuo tono di voce esatto.", w: "C" },
      { kind: "PROOF", t: "Calibrazione pre-go-live obbligatoria.", d: "Prima del lancio, addestriamo il copy engine su esempi reali del tuo settore. Il sistema scrive come se fossi tu a scriverlo — perché è esattamente il tuo stile.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Copy personalizzato su ogni lead.", d: "Ogni messaggio usa dati reali del prospect: nome, settore, profilo. Non un template con variabili — una scrittura contestuale generata in tempo reale.", w: "B" },
    ],
  },
  {
    icon: Code2,
    eyebrow: "Obiezione #04 · La dipendenza",
    title: "“Diventerei dipendente da voi per sempre.”",
    kicker: "Il codice è tuo. Zero dipendenza strutturale.",
    cards: [
      { kind: "CLAIM", t: "Consegniamo il codice sorgente completo.", d: "Non un accesso a un pannello che gestiamo noi. Ti diamo il codice sorgente commentato, la documentazione tecnica e la formazione su come gestirlo.", w: "C" },
      { kind: "PROOF", t: "90 giorni di supporto, poi sei libero.", d: "Il supporto dedicato dura 90 giorni. Dopo quel periodo il sistema gira da solo — e se hai bisogno di modifiche, puoi farle tu o ingaggiare qualsiasi sviluppatore.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Asset aziendale permanente.", d: "Un SaaS ti taglia fuori se smetti di pagare. Il tuo sistema AI gira finché vuoi, sui tuoi server, sotto il tuo controllo totale. Per sempre.", w: "B" },
    ],
  },
];

export function Objections() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-20">
          <Reveal>
            <span className="bubble-orange mb-6">Gestione Obiezioni // Risposta diretta</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Le 4 obiezioni che </span>
              <span className="text-orange-pure italic font-medium">demoliamo</span>
              <span className="text-silver-black"> prima di iniziare.</span>
            </h2>
          </Reveal>
        </div>

        {groups.map((g, gi) => {
          const Icon = g.icon;
          return (
            <div key={gi} className={gi !== 0 ? "mt-28" : ""}>
              <Reveal>
                <div className="relative max-w-3xl mx-auto mb-12">
                  <div
                    aria-hidden="true"
                    className="absolute -top-6 -left-2 md:-left-6 select-none pointer-events-none"
                    style={{
                      fontFamily: "var(--font-serif), Georgia, serif",
                      fontStyle: "italic",
                      fontSize: "140px",
                      lineHeight: 1,
                      color: "#fb4604",
                      opacity: 0.18,
                    }}
                  >
                    &ldquo;
                  </div>
                  <div className="relative text-center">
                    <div className="flex items-center justify-center gap-2 mb-4">
                      <Icon className="h-4 w-4 text-orange-pure" />
                      <span className="text-[11px] uppercase tracking-[0.25em] font-black text-orange-pure">
                        {g.eyebrow}
                      </span>
                    </div>
                    <h3
                      className="text-[22px] md:text-[32px] leading-tight text-[#1c1c1c] mb-4"
                      style={{
                        fontFamily: "var(--font-serif), Georgia, serif",
                        fontStyle: "italic",
                        fontWeight: 400,
                        letterSpacing: "-0.01em",
                      }}
                    >
                      {g.title}
                    </h3>
                    <p className="text-[15px] md:text-[16px] text-[#fb4604] font-bold uppercase tracking-[0.12em]">
                      → {g.kicker}
                    </p>
                  </div>
                </div>
              </Reveal>

              <div className="grid md:grid-cols-3 gap-5">
                {g.cards.map((c, i) => (
                  <Reveal key={i} delay={0.15 + i * 0.1}>
                    <div
                      className={`relative overflow-hidden p-8 rounded-2xl border h-full transition-all duration-300 hover:-translate-y-1.5 ${
                        c.isGold
                          ? "bg-gradient-to-br from-orange-pure/10 via-orange-pure/5 to-transparent border-orange-pure/40 shadow-[0_8px_30px_-12px_rgba(251,70,4,0.35)]"
                          : "bg-white/60 border-[#1c1c1c]/10 hover:border-[#1c1c1c]/25 shadow-[0_4px_20px_-8px_rgba(0,0,0,0.12)]"
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-6">
                        <span
                          className={`inline-block w-6 h-[2px] ${
                            c.isGold ? "bg-orange-pure" : "bg-[#1c1c1c]/40"
                          }`}
                        />
                        <span
                          className={`text-[11px] uppercase tracking-[0.18em] font-black ${
                            c.isGold ? "text-orange-pure" : "text-[#1c1c1c]/72"
                          }`}
                        >
                          0{i + 1} // {c.kind}
                        </span>
                      </div>
                      <h4 className="text-lg font-black text-silver-black mb-4 leading-tight">
                        {c.t}
                      </h4>
                      <p className="text-[#2a2a2a] text-sm leading-relaxed relative z-10">
                        {c.d}
                      </p>
                      <div className="absolute bottom-[-14px] right-1 text-[130px] font-black leading-none pointer-events-none select-none"
                        style={{
                          color: c.isGold ? "rgba(251,70,4,0.08)" : "rgba(28,28,28,0.035)",
                          fontFamily: "var(--font-serif), Georgia, serif",
                          fontStyle: "italic",
                        }}
                      >
                        {c.w}
                      </div>
                    </div>
                  </Reveal>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
