"use client";

import { Zap, FileText, Layers, Check, ArrowRight } from "lucide-react";
import { Reveal } from "@/components/reveal";

const OUTREACH_FEATURES = [
  "Prospecting AI: trova lead qualificati in automatico",
  "Sequenze email multi-step personalizzate con AI",
  "Follow-up automatico basato sul comportamento",
  "Qualificazione lead AI: filtra solo i caldi",
  "Sync automatico CRM + report settimanali",
];

const CONTENT_FEATURES = [
  "Calendar editoriale AI generato ogni settimana",
  "Scrittura automatica post LinkedIn, Instagram, email",
  "Repurposing: un contenuto verso 5 formati diversi",
  "Publish schedulato H24 senza intervento manuale",
  "Analytics report: capisci cosa converte davvero",
];

const LANDING_FEATURES = [
  "Audit conversion + analisi competitor",
  "Copy scientifico framework APSOC",
  "Dev pixel-perfect Next.js / Webflow",
];

const GRAIN = (seed: string, freq = "1.35") =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='${freq}' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.90 0 0 0 0 0.88 0 0 0 0 0.86 0 0 0 0.28 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

/* Card base styles */
const cardBase = {
  position: "relative" as const,
  isolation: "isolate" as const,
  borderRadius: 22,
  padding: "2rem 1.85rem",
  border: "1px solid rgba(251,70,4,0.35)",
  color: "#ffffff",
  backgroundSize: "200px 200px, 100% 100%, 100% 100%",
  backgroundBlendMode: "screen, normal, normal",
  boxShadow: [
    "0 60px 110px -28px rgba(0,0,30,0.88)",
    "0 2px 0 rgba(255,255,255,0.32) inset",
    "0 -2px 0 rgba(0,0,20,0.60) inset",
    "0 0 0 1px rgba(251,70,4,0.14)",
  ].join(", "),
  transition: "transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s",
};

export function Servizi() {
  return (
    <section
      id="servizi"
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="servizi-h2"
    >
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              I nostri workflow
            </span>
            <h2 id="servizi-h2" className="mt-6">
              <span className="text-silver-white">Due workflow. Un solo obiettivo:</span>{" "}
              <span className="text-silver-gold font-accent italic">
                liberarti dall&apos;operatività.
              </span>
            </h2>
            <p className="mt-5 text-[1.0625rem] text-white/85 leading-relaxed font-light">
              Non vendiamo strumenti. Costruiamo sistemi AI chiavi in mano che
              girano H24 in autonomia. Tu scala il business, il workflow fa il resto.
            </p>
          </div>
        </Reveal>

        {/* TOP ROW — 2 primary workflows */}
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-5 items-stretch mb-5">

          {/* CARD 1 — OUTREACH WORKFLOW (primary, 60%) */}
          <Reveal delay={0.10} className="lg:col-span-3">
            <article
              style={{
                ...cardBase,
                background: [
                  GRAIN("11"),
                  "radial-gradient(75% 55% at 5% 8%, rgba(255,255,255,0.32) 0%, transparent 48%)",
                  "linear-gradient(145deg, #1a0800 0%, #2d1200 18%, #6a2200 40%, #b83800 65%, #041004 100%)",
                ].join(", "),
              }}
              className="h-full flex flex-col"
            >
              <div className="flex items-start justify-between gap-4 mb-6">
                <span
                  className="grid place-items-center w-14 h-14 rounded-2xl flex-shrink-0"
                  style={{
                    background: "linear-gradient(135deg, rgba(251,70,4,0.30) 0%, rgba(201,55,10,0.40) 100%)",
                    border: "1px solid rgba(251,70,4,0.45)",
                    boxShadow: "0 8px 24px rgba(100,20,0,0.45), inset 0 1px 0 rgba(251,70,4,0.25)",
                  }}
                >
                  <Zap className="h-6 w-6 text-gold-pure" />
                </span>
                <span className="bubble-gold !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                  Servizio primario
                </span>
              </div>

              <h3 className="text-[1.875rem] md:text-[2.25rem] font-bold leading-[1.10] tracking-tight text-white mb-2">
                Outreach Workflow
              </h3>
              <p className="font-accent italic text-[1.05rem] text-white/70 mb-5">
                Il tuo sales team che lavora mentre dormi.
              </p>
              <p className="text-[0.96rem] leading-relaxed text-white/85 mb-7 font-light">
                Un sistema AI che trova lead qualificati, li contatta, fa
                follow-up automatico e ti consegna solo quelli pronti a parlare.
                Zero intervento manuale. Solo clienti caldi in arrivo.
              </p>

              <ul className="flex flex-col gap-3 mb-8">
                {OUTREACH_FEATURES.map((f, i) => (
                  <li key={i} className="flex items-start gap-3 text-[0.95rem] text-white/90">
                    <span
                      className="grid place-items-center w-5 h-5 rounded-full mt-0.5 shrink-0"
                      style={{
                        background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
                        boxShadow: "0 0 8px rgba(251,70,4,0.30)",
                      }}
                    >
                      <Check className="h-3 w-3 text-[#0a0a0a]" strokeWidth={3} />
                    </span>
                    <span>{f}</span>
                  </li>
                ))}
              </ul>

              <a
                href="#processo"
                className="inline-flex items-center gap-2 text-[0.95rem] font-semibold text-gold-pure mt-auto group hover:gap-3 transition-all"
              >
                Vedi come si costruisce
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
              </a>
            </article>
          </Reveal>

          {/* CARD 2 — CONTENT WORKFLOW (primary, 40%) */}
          <Reveal delay={0.20} className="lg:col-span-2">
            <article
              style={{
                ...cardBase,
                border: "1px solid rgba(251,70,4,0.38)",
                background: [
                  GRAIN("13"),
                  "radial-gradient(75% 55% at 5% 8%, rgba(255,255,255,0.28) 0%, transparent 48%)",
                  "linear-gradient(145deg, #1a1000 0%, #2d2000 18%, #5a3800 40%, #8a5200 65%, #041004 100%)",
                ].join(", "),
                boxShadow: [
                  "0 60px 110px -28px rgba(0,0,30,0.85)",
                  "0 2px 0 rgba(255,255,255,0.30) inset",
                  "0 -2px 0 rgba(0,0,20,0.60) inset",
                  "0 0 0 1px rgba(251,70,4,0.15)",
                ].join(", "),
              }}
              className="h-full flex flex-col"
            >
              <div className="flex items-start justify-between gap-4 mb-6">
                <span
                  className="grid place-items-center w-12 h-12 rounded-xl flex-shrink-0"
                  style={{
                    background: "linear-gradient(135deg, rgba(251,70,4,0.28) 0%, rgba(201,55,10,0.45) 100%)",
                    border: "1px solid rgba(251,70,4,0.38)",
                    boxShadow: "0 6px 18px rgba(100,20,0,0.40), inset 0 1px 0 rgba(255,255,255,0.20)",
                  }}
                >
                  <FileText className="h-5 w-5 text-white" />
                </span>
                <span className="bubble-gold !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                  Servizio primario
                </span>
              </div>

              <h3 className="text-[1.5rem] md:text-[1.75rem] font-bold leading-[1.10] tracking-tight text-white mb-2">
                Content Workflow
              </h3>
              <p className="font-accent italic text-[0.96rem] text-white/65 mb-4">
                Pubblica ogni giorno senza toccare niente.
              </p>
              <p className="text-[0.92rem] leading-relaxed text-white/85 mb-6 font-light">
                Sistema AI che genera, schedula e pubblica i tuoi contenuti in
                automatico. Da una sola idea verso 5 post su 5 canali, pronti.
              </p>

              <ul className="flex flex-col gap-3 mb-7">
                {CONTENT_FEATURES.map((f, i) => (
                  <li key={i} className="flex items-start gap-2.5 text-[0.92rem] text-white/90">
                    <Check className="h-4 w-4 mt-0.5 shrink-0 text-[#90c0ff]" strokeWidth={2.5} />
                    <span>{f}</span>
                  </li>
                ))}
              </ul>

              <a
                href="#processo"
                className="inline-flex items-center gap-2 text-[0.92rem] font-semibold text-white/85 mt-auto group hover:gap-3 transition-all"
              >
                Vedi il processo
                <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" />
              </a>
            </article>
          </Reveal>
        </div>

        {/* BOTTOM ROW — Landing page */}
        <Reveal delay={0.30}>
          <article
            style={{
              ...cardBase,
              border: "1.5px solid rgba(168,85,247,0.45)",
              background: [
                GRAIN("6"),
                "radial-gradient(75% 55% at 5% 8%, rgba(255,255,255,0.30) 0%, transparent 48%)",
                "linear-gradient(145deg, #c090f0 0%, #a060d8 16%, #7830c8 34%, #5818b0 54%, #3a0888 76%, #200555 100%)",
              ].join(", "),
              boxShadow: [
                "0 55px 100px -28px rgba(58,8,136,0.75)",
                "0 2px 0 rgba(255,255,255,0.24) inset",
                "0 -2px 0 rgba(0,0,30,0.58) inset",
                "0 0 0 1px rgba(168,85,247,0.18)",
              ].join(", "),
              display: "flex",
              flexDirection: "column" as const,
            }}
            className="md:flex-row md:items-center gap-6 p-6 md:p-8"
          >
            <div className="flex items-center gap-4 md:shrink-0">
              <span
                className="grid place-items-center w-11 h-11 rounded-xl"
                style={{
                  background: "linear-gradient(135deg, rgba(168,85,247,0.35) 0%, rgba(90,24,184,0.55) 100%)",
                  border: "1px solid rgba(168,85,247,0.50)",
                  boxShadow: "0 4px 14px rgba(90,24,184,0.45), inset 0 1px 0 rgba(255,255,255,0.18)",
                }}
              >
                <Layers className="h-5 w-5 text-purple-bright" />
              </span>
              <div>
                <span className="text-[0.7rem] uppercase tracking-[0.18em] font-semibold text-purple-bright/85 block mb-0.5">
                  Servizio complementare
                </span>
                <h3 className="text-[1.25rem] font-bold text-white leading-tight">
                  Landing Page Premium + CRO Engineering
                </h3>
              </div>
            </div>
            <p className="text-[0.92rem] text-white/85 leading-relaxed font-light md:flex-1">
              Hai già l&apos;operatività sotto controllo e vuoi una landing che converte?
              Audit, design, copy e dev in un ecosistema integrato. Disponibile come servizio aggiuntivo ai workflow o standalone.
            </p>
            <ul className="flex flex-col gap-2 md:shrink-0">
              {LANDING_FEATURES.map((f, i) => (
                <li key={i} className="flex items-center gap-2 text-[0.85rem] text-white/90">
                  <Check className="h-3.5 w-3.5 shrink-0 text-purple-bright" strokeWidth={2.5} />
                  <span>{f}</span>
                </li>
              ))}
            </ul>
          </article>
        </Reveal>
      </div>
    </section>
  );
}
