"use client";

import { Reveal } from "@/components/reveal";
import {
  DollarSign,
  Zap,
  ShieldCheck,
  Clock,
  RefreshCcw,
  CheckCircle2,
  BarChart3,
  TrendingUp,
  Users,
  Settings2,
} from "lucide-react";
import type { LucideIcon } from "lucide-react";

type Card = {
  kind: "CLAIM" | "PROOF" | "BENEFIT";
  icon: LucideIcon;
  title: string;
  body: string;
  watermark: "C" | "P" | "B";
  highlight?: boolean;
};

type Group = {
  icon: LucideIcon;
  eyebrow: string;
  title: string;
  italic: string;
  trail: string;
  kicker: string;
  cards: [Card, Card, Card];
};

const GROUPS: Group[] = [
  {
    icon: DollarSign,
    eyebrow: "Obiezione #01 · Il prezzo",
    title: "\u201CCosta",
    italic: "troppo",
    trail: "per quello che fa.\u201D",
    kicker: "Un workflow da 7.000€ si ripaga al primo cliente.",
    cards: [
      {
        kind: "CLAIM",
        icon: DollarSign,
        title: "Il costo reale è non averlo.",
        body: "Quante ore al mese passi a fare outreach manuale, scrivere post, mandare follow-up? Moltiplica quelle ore per il tuo costo orario. Hai già il ROI del workflow nel primo trimestre.",
        watermark: "C",
      },
      {
        kind: "PROOF",
        icon: BarChart3,
        title: "3 nuovi clienti = workflow pagato.",
        body: "Per la maggior parte dei nostri clienti, l'Outreach Workflow porta 3-5 clienti nuovi nel primo mese. Con un ticket medio di 3.000€, il sistema si ripaga da solo prima che tu abbia finito di usarlo.",
        watermark: "P",
        highlight: true,
      },
      {
        kind: "BENEFIT",
        icon: TrendingUp,
        title: "Non è una spesa. È un moltiplicatore.",
        body: "Un workflow che gira H24 senza intervento manuale è un asset permanente. Non paghi ogni mese: lo costruiamo una volta, gira per anni. Ogni mese successivo è puro profitto.",
        watermark: "B",
      },
    ],
  },
  {
    icon: Zap,
    eyebrow: "Obiezione #02 · L'AI",
    title: "\u201CHo già provato strumenti AI,",
    italic: "non funzionano",
    trail: "davvero.\u201D",
    kicker: "Gli strumenti da soli non funzionano. Il sistema sì.",
    cards: [
      {
        kind: "CLAIM",
        icon: Zap,
        title: "Gli strumenti AI da soli sono inutili.",
        body: "ChatGPT, Apollo, Instantly, Make: li conosci tutti. Il problema non è lo strumento. È che qualcuno deve progettare la logica che li fa lavorare insieme. Senza architettura, sono solo tab aperti.",
        watermark: "C",
      },
      {
        kind: "PROOF",
        icon: Settings2,
        title: "Il workflow è l'architettura che mancava.",
        body: "Noi non vendiamo accesso a strumenti. Progettiamo il sistema che li connette, configura i trigger, gestisce gli errori, ottimizza l'output. È come la differenza tra avere degli ingredienti e avere uno chef.",
        watermark: "P",
        highlight: true,
      },
      {
        kind: "BENEFIT",
        icon: CheckCircle2,
        title: "Da strumenti sparsi a macchina unica.",
        body: "Il risultato non è un altro tool. È un sistema unico che capisce il tuo business, usa i dati reali dei tuoi lead, e migliora ogni settimana. Gli strumenti che hai già diventano finalmente utili.",
        watermark: "B",
      },
    ],
  },
  {
    icon: ShieldCheck,
    eyebrow: "Obiezione #03 · La fiducia",
    title: "\u201CNon vi",
    italic: "conosco",
    trail: "abbastanza per fidarmi.\u201D",
    kicker: "Giusto. Per questo la prima call è una demo live.",
    cards: [
      {
        kind: "CLAIM",
        icon: ShieldCheck,
        title: "La fiducia si guadagna con i fatti.",
        body: "Non ti chiediamo di fidarti delle nostre parole. Ti chiediamo 30 minuti: ti mostriamo un workflow attivo, in live, su dati reali. Non slides, non mockup. Il sistema che gira davvero.",
        watermark: "C",
      },
      {
        kind: "PROOF",
        icon: BarChart3,
        title: "Demo live su workflow già operativi.",
        body: "In ogni demo ti mostriamo workflow attivi per clienti del tuo settore: quanti lead ha generato, quante email ha mandato, quale conversion rate sta ottenendo. Numeri reali, tracciati, verificabili.",
        watermark: "P",
        highlight: true,
      },
      {
        kind: "BENEFIT",
        icon: Users,
        title: "Senza impegno, senza pressione.",
        body: "La demo è gratuita. Se dopo averla vista non sei convinto, niente firmato, niente pagato, niente perso. Ma il 90% di chi vede il sistema in live vuole iniziare la settimana dopo.",
        watermark: "B",
      },
    ],
  },
  {
    icon: Clock,
    eyebrow: "Obiezione #04 · Il tempo",
    title: "\u201CNon ho tempo per",
    italic: "implementare",
    trail: "qualcosa di nuovo.\u201D",
    kicker: "Non implementi niente tu. Arriva chiavi in mano.",
    cards: [
      {
        kind: "CLAIM",
        icon: Clock,
        title: "Il tuo unico impegno: 1 ora.",
        body: "Costruiamo, testiamo e integriamo tutto noi. L'unica cosa che ti chiediamo è 1 ora di formazione al go-live per capire come monitorare il sistema. Dopo, gira da solo.",
        watermark: "C",
      },
      {
        kind: "PROOF",
        icon: Zap,
        title: "Done-for-you dall'inizio alla fine.",
        body: "Blueprint, sviluppo, test, integrazione CRM, setup tool, go-live: gestiamo ogni fase. Non hai briefing interminabili, non hai file da rincorrere, non hai decisioni tecniche da prendere. Solo review di alto livello.",
        watermark: "P",
        highlight: true,
      },
      {
        kind: "BENEFIT",
        icon: TrendingUp,
        title: "3 settimane di lavoro. Anni di autonomia.",
        body: "L'investimento di tempo è minimo e concentrato nelle prime 3 settimane. Dopo il go-live, il workflow gira da solo per mesi e anni senza che tu ci metta altro tempo.",
        watermark: "B",
      },
    ],
  },
  {
    icon: RefreshCcw,
    eyebrow: "Obiezione #05 · L'affidabilità",
    title: "\u201CE se il workflow",
    italic: "smette di funzionare",
    trail: "dopo 2 mesi?\u201D",
    kicker: "30 giorni di supporto incluso. E poi si mantiene.",
    cards: [
      {
        kind: "CLAIM",
        icon: RefreshCcw,
        title: "I sistemi si aggiornano, non si buttano.",
        body: "I workflow che costruiamo sono modulari: se cambia un tool, si aggiorna il modulo. Se cambia un'API, si aggiusta il connettore. Non si butta tutto e si ricomincia da zero.",
        watermark: "C",
      },
      {
        kind: "PROOF",
        icon: BarChart3,
        title: "30 giorni di supporto attivo post go-live.",
        body: "Il primo mese monitoriamo le performance in tempo reale. Interveniamo su ogni imprevisto entro 24h. Ottimizziamo i flussi basandoci sui dati reali. Il workflow migliora nel primo mese, non peggiora.",
        watermark: "P",
        highlight: true,
      },
      {
        kind: "BENEFIT",
        icon: CheckCircle2,
        title: "Manutenzione mensile disponibile.",
        body: "Dopo i 30 giorni inclusi, offriamo piani di manutenzione mensile per chi vuole continuità garantita. Non è obbligatorio. Ma i clienti che lo attivano non se ne pentono mai.",
        watermark: "B",
      },
    ],
  },
];

export function Objections() {
  return (
    <section
      id="obiezioni"
      className="bg-paper section-airy relative overflow-hidden"
      aria-labelledby="obiezioni-h2"
    >
      <div className="container-default">
        <div className="text-center mb-10 md:mb-20 max-w-3xl mx-auto">
          <Reveal>
            <span className="bubble-gold">
              <ShieldCheck className="h-3.5 w-3.5" />
              Gestione Obiezioni &middot; Protocollo C&middot;P&middot;B
            </span>
          </Reveal>
          <Reveal delay={0.10}>
            <h2 id="obiezioni-h2" className="mt-6">
              <span className="text-brand-navy">Le 5 obiezioni che </span>
              <span className="text-brand-accent font-accent italic">demoliamo</span>
              <span className="text-brand-navy"> prima di iniziare.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.20}>
            <p className="mt-5 text-[1.0625rem] text-[#1c1c1c]/70 leading-relaxed font-light">
              Le 5 obiezioni più comuni che riceviamo da imprenditori prima di
              firmare. Affrontate con Claim, Proof e Benefit. Niente sales
              pitch: solo logica, dati e prova.
            </p>
          </Reveal>
        </div>

        {GROUPS.map((g, gi) => {
          const HeadIcon = g.icon;
          return (
            <div key={gi} className={gi !== 0 ? "mt-14 md:mt-28" : ""}>
              <Reveal>
                <div className="relative max-w-3xl mx-auto mb-7 md:mb-12">
                  <div
                    aria-hidden
                    className="hidden sm:block absolute -top-8 -left-2 md:-left-8 select-none pointer-events-none font-accent italic"
                    style={{
                      fontSize: "150px",
                      lineHeight: 1,
                      color: "#fb4604",
                      opacity: 0.06,
                    }}
                  >
                    &ldquo;
                  </div>

                  <div className="relative text-center">
                    <div className="flex items-center justify-center gap-2 mb-4">
                      <HeadIcon className="h-4 w-4 text-[#fb4604]" />
                      <span className="text-[0.70rem] uppercase tracking-[0.25em] font-bold text-[#fb4604]/80">
                        {g.eyebrow}
                      </span>
                    </div>

                    <h3
                      className="text-[1.35rem] md:text-[1.8rem] leading-[1.20] mb-4 text-[#1c1c1c]"
                      style={{
                        letterSpacing: "-0.01em",
                        fontWeight: 600,
                      }}
                    >
                      {g.title}{" "}
                      <span className="font-accent italic font-medium text-brand-accent">
                        {g.italic}
                      </span>{" "}
                      {g.trail}
                    </h3>

                    <p className="text-[0.92rem] md:text-[0.96rem] uppercase tracking-[0.14em] font-bold text-[#fb4604]/90">
                      &rarr; {g.kicker}
                    </p>
                  </div>
                </div>
              </Reveal>

              <div className="grid md:grid-cols-3 gap-5">
                {g.cards.map((c, i) => {
                  const CIcon = c.icon;
                  return (
                    <Reveal key={i} delay={0.15 + i * 0.10}>
                      <article
                        className={`relative h-full overflow-hidden ${
                          c.highlight ? "card-cpb-highlight" : "card-cpb"
                        }`}
                      >
                        <span
                          aria-hidden
                          className="absolute top-0 left-0 right-0 h-px"
                          style={{
                            background:
                              "linear-gradient(90deg, transparent, rgba(251,70,4,0.18) 50%, transparent)",
                          }}
                        />

                        <div className="flex items-center gap-3 mb-6 relative z-10">
                          <span
                            className="grid place-items-center w-11 h-11 rounded-xl"
                            style={
                              c.highlight
                                ? {
                                    background:
                                      "linear-gradient(135deg, #fb4604 0%, #c93a0a 100%)",
                                    boxShadow:
                                      "0 6px 18px -8px rgba(201,55,10,0.55), inset 0 1px 0 rgba(255,255,255,0.30), inset 0 -1px 0 rgba(0,0,30,0.30)",
                                  }
                                : {
                                    background:
                                      "linear-gradient(135deg, #ffffff 0%, #ece7f0 100%)",
                                    border: "1px solid rgba(251,70,4,0.18)",
                                    boxShadow:
                                      "inset 0 1px 0 rgba(255,255,255,0.95), 0 4px 10px -6px rgba(201,55,10,0.20)",
                                  }
                            }
                          >
                            <CIcon
                              className="h-5 w-5"
                              style={{
                                color: c.highlight ? "#ffffff" : "#fb4604",
                              }}
                            />
                          </span>

                          <span
                            className="text-[0.66rem] uppercase tracking-[0.22em] font-bold"
                            style={{
                              color: "rgba(251,70,4,0.75)",
                            }}
                          >
                            0{i + 1} // {c.kind}
                          </span>
                        </div>

                        <h4 className="text-[1.05rem] md:text-[1.10rem] font-bold leading-[1.30] mb-3 text-[#0a0a0a] relative z-10">
                          {c.title}
                        </h4>

                        <p className="text-[0.92rem] leading-[1.65] text-[#1c1c1c]/80 relative z-10">
                          {c.body}
                        </p>

                        <span
                          aria-hidden
                          className="absolute bottom-[-22px] right-2 font-accent italic font-bold pointer-events-none select-none"
                          style={{
                            fontSize: "138px",
                            lineHeight: 1,
                            color: "rgba(251,70,4,0.06)",
                          }}
                        >
                          {c.watermark}
                        </span>
                      </article>
                    </Reveal>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
