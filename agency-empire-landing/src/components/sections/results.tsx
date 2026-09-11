"use client";

import { Reveal } from "@/components/reveal";
import {
  Code2,
  LifeBuoy,
  ShieldCheck,
  Rocket,
  BadgeEuro,
  PlayCircle,
  Quote,
  ArrowRight,
} from "lucide-react";

/* ────────────────────────────────────────────────────────────────────────
   SCAFFOLDING PER PROVE REALI — onestà assoluta.
   Questi array sono VUOTI di proposito. Finché restano vuoti, la sezione
   mostra SOLO i trust pillars (fatti già dichiarati altrove) e l'invito
   alla demo. NESSUN risultato finto viene mostrato.

   // TODO: incollare qui case study e testimonianze REALI

   Quando li compilerai con dati veri, le card appariranno automaticamente.

   Forma di un case study:
   @typedef {Object} CaseStudy
   @property {string} cliente   - Nome cliente o "Azienda nel settore X" se sotto NDA
   @property {string} settore   - Es. "E-commerce moda", "Studio legale"
   @property {string} problema  - Il problema concreto prima del sistema
   @property {string} sistema   - Quale sistema è stato installato
   @property {string} risultato - Risultato MISURABILE e VERO (niente numeri inventati)

   Forma di una testimonianza:
   @typedef {Object} Testimonial
   @property {string} quote   - Frase testuale del cliente (vera, non parafrasata)
   @property {string} autore  - Nome (o iniziali se preferisce l'anonimato)
   @property {string} ruolo   - Ruolo / azienda
─────────────────────────────────────────────────────────────────────────── */

/** @type {Array<{cliente:string,settore:string,problema:string,sistema:string,risultato:string}>} */
const caseStudies: {
  cliente: string;
  settore: string;
  problema: string;
  sistema: string;
  risultato: string;
}[] = [
  // Esempio di forma (NON è un dato reale — lascialo commentato finché non hai il vero):
  // {
  //   cliente: "Nome Cliente",
  //   settore: "E-commerce moda",
  //   problema: "Outreach manuale, 0 lead qualificati al giorno",
  //   sistema: "Outreach Factory",
  //   risultato: "Risultato reale e verificabile",
  // },
];

/** @type {Array<{quote:string,autore:string,ruolo:string}>} */
const testimonials: {
  quote: string;
  autore: string;
  ruolo: string;
}[] = [
  // Esempio di forma (NON è un dato reale — lascialo commentato finché non hai il vero):
  // {
  //   quote: "Frase testuale del cliente.",
  //   autore: "Nome Cognome",
  //   ruolo: "CEO, Azienda",
  // },
];

/* ── BLOCCO 1 — Trust pillars VERITIERI ──
   Usano SOLO fatti già dichiarati altrove nel sito (codice consegnato,
   zero canoni, go-live in 7 giorni, ecc.). Nessuna promessa inventata. */
const pillars = [
  {
    icon: Code2,
    title: "Codice sorgente consegnato",
    desc: "Il sistema è tuo, per sempre. Gira sui tuoi server — nessun lock-in, nessuna scatola nera.",
  },
  {
    icon: LifeBuoy,
    title: "90 giorni di supporto dedicato",
    desc: "Dopo il go-live restiamo al tuo fianco per tre mesi: fix, tuning e formazione del team.",
  },
  {
    icon: ShieldCheck,
    title: "Garanzia 30 giorni",
    desc: "Se nei primi 30 giorni il sistema non fa quello per cui l'hai preso, il rischio è nostro.",
  },
  {
    icon: Rocket,
    title: "Setup in 7 giorni",
    desc: "Dal via libera al primo go-live in una settimana. Niente onboarding infiniti.",
  },
  {
    icon: BadgeEuro,
    title: "Zero canoni mensili",
    desc: "Niente abbonamenti SaaS, niente dipendenza. Installiamo, formiamo, consegniamo. Poi sei libero.",
  },
];

export function Results() {
  const hasProof = caseStudies.length > 0 || testimonials.length > 0;

  return (
    <section
      id="risultati"
      className="bg-ink-2 section section-border-t relative overflow-hidden"
    >
      <style>{`
        .res-card {
          transition: transform 0.4s cubic-bezier(0.22,1,0.36,1), border-color 0.3s ease, background 0.3s ease;
        }
        .res-card:hover {
          transform: translateY(-4px);
          border-color: rgba(251,70,4,0.42) !important;
          background: rgba(255,255,255,0.05) !important;
        }
      `}</style>

      {/* Ambient glow */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(ellipse 80% 40% at 50% 0%, rgba(251,70,4,0.07) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-6xl mx-auto px-6 relative z-10">
        {/* ── Section header ── */}
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">Prova · non promesse</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[28px] md:text-[48px] font-bold leading-[1.15] mt-6 text-white">
              Fatti,{" "}
              <span
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  color: "#fb4604",
                }}
              >
                non slogan.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.18}>
            <p className="text-white/80 mt-5 text-[1.05rem] md:text-[1.15rem] max-w-2xl mx-auto leading-relaxed font-medium">
              Non ti chiediamo di crederci sulla parola. Ti diamo motivi concreti
              per fidarti — e ti mostriamo il sistema{" "}
              <strong className="text-silver-orange font-semibold">dal vivo</strong>,
              prima di qualsiasi impegno.
            </p>
          </Reveal>
        </div>

        {/* ── BLOCCO 1 — Trust pillars ── */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {pillars.map((p, i) => {
            const Icon = p.icon;
            return (
              <Reveal key={p.title} delay={0.12 + i * 0.07}>
                <div
                  className="res-card h-full rounded-2xl px-6 py-6"
                  style={{
                    background: "rgba(255,255,255,0.035)",
                    border: "1px solid rgba(255,255,255,0.10)",
                    boxShadow: "0 18px 44px -22px rgba(0,0,0,0.6)",
                  }}
                >
                  <div
                    className="inline-flex items-center justify-center w-11 h-11 rounded-xl mb-4"
                    style={{
                      background:
                        "linear-gradient(135deg, rgba(251,70,4,0.22) 0%, rgba(180,36,0,0.42) 100%)",
                      border: "1px solid rgba(251,80,4,0.40)",
                    }}
                  >
                    <Icon
                      className="h-5 w-5"
                      style={{ color: "#ffaa88" }}
                      strokeWidth={2.2}
                    />
                  </div>
                  <h3 className="text-[17px] font-bold text-white leading-snug mb-2">
                    {p.title}
                  </h3>
                  <p className="text-[13.5px] text-white/80 leading-relaxed">
                    {p.desc}
                  </p>
                </div>
              </Reveal>
            );
          })}

          {/* CTA tile che chiude la griglia dei pillar */}
          <Reveal delay={0.12 + pillars.length * 0.07}>
            <a
              href="#prenota"
              className="res-card h-full rounded-2xl px-6 py-6 flex flex-col justify-between group"
              style={{
                background:
                  "linear-gradient(150deg, rgba(251,70,4,0.16) 0%, rgba(124,32,0,0.22) 100%)",
                border: "1px solid rgba(251,80,4,0.40)",
                boxShadow: "0 18px 44px -22px rgba(150,35,0,0.55)",
              }}
            >
              <div>
                <span className="text-[11px] font-bold uppercase tracking-[0.18em] text-silver-orange">
                  Il rischio è nostro
                </span>
                <p className="text-[17px] font-bold text-white leading-snug mt-3">
                  Garanzia, codice tuo, zero canoni. Cosa ti trattiene?
                </p>
              </div>
              <span className="mt-5 inline-flex items-center gap-1.5 text-[12px] font-black uppercase tracking-[0.12em] text-white">
                Prenota una chiamata
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </span>
            </a>
          </Reveal>
        </div>

        {/* ── BLOCCO 2 — Demo onesta ── */}
        <Reveal delay={0.2}>
          <div className="mt-8 grid grid-cols-1 lg:grid-cols-2 gap-6 items-center">
            {/* Copy invito */}
            <div>
              <span className="text-[11px] font-bold uppercase tracking-[0.18em] text-silver-orange">
                Vedilo in azione
              </span>
              <h3 className="text-[24px] md:text-[30px] font-bold text-white leading-[1.15] mt-3">
                Vuoi vederlo dal vivo?
              </h3>
              <p className="text-white/80 mt-4 text-[1rem] leading-relaxed max-w-md">
                In chiamata ti mostriamo il sistema che gira{" "}
                <strong className="text-silver-white font-semibold">
                  in 5 minuti
                </strong>{" "}
                — lead reali che entrano, contenuti che si generano, la dashboard
                live. Niente slide: il prodotto vero, davanti a te.
              </p>
              <a
                href="#prenota"
                className="mt-6 inline-flex items-center gap-2 text-[13px] font-black uppercase tracking-[0.10em] text-white group"
              >
                <PlayCircle className="h-5 w-5 text-orange-pure" strokeWidth={2.2} />
                Prenota la demo
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </a>
            </div>

            {/* Area video 16:9 placeholder.
                ── COME INSERIRE IL VIDEO REALE ──
                Sostituisci l'intero blocco <div ...placeholder...> qui sotto con un
                iframe Loom / YouTube, ad esempio:

                <iframe
                  src="https://www.loom.com/embed/IL_TUO_ID_LOOM"
                  className="absolute inset-0 w-full h-full"
                  frameBorder="0"
                  allowFullScreen
                />

                Tienilo dentro al wrapper "aspect-video" qui sotto per mantenere il 16:9. */}
            <div
              className="relative w-full aspect-video rounded-2xl overflow-hidden"
              style={{
                border: "1.5px solid rgba(251,80,4,0.50)",
                background:
                  "linear-gradient(150deg, #2a0c00 0%, #150600 60%, #0c0400 100%)",
                boxShadow:
                  "0 0 48px -16px rgba(150,35,0,0.45), 0 22px 56px -20px rgba(0,0,0,0.7)",
              }}
            >
              {/* PLACEHOLDER — nessun video inventato. Centro: icona play + label */}
              <div className="absolute inset-0 flex flex-col items-center justify-center gap-3">
                <div
                  className="flex items-center justify-center w-16 h-16 rounded-full"
                  style={{
                    background:
                      "linear-gradient(135deg, rgba(251,70,4,0.30) 0%, rgba(180,36,0,0.55) 100%)",
                    border: "1px solid rgba(251,80,4,0.55)",
                  }}
                >
                  <PlayCircle className="h-8 w-8 text-white" strokeWidth={1.8} />
                </div>
                <span className="text-[11px] font-bold uppercase tracking-[0.20em] text-white/85">
                  Demo del sistema
                </span>
              </div>
              {/* Label angolo */}
              <span
                className="absolute top-3 left-3 text-[10px] font-black uppercase tracking-[0.16em] px-2.5 py-1 rounded-md text-white"
                style={{
                  background: "rgba(0,0,0,0.45)",
                  border: "1px solid rgba(255,255,255,0.18)",
                }}
              >
                16:9 · placeholder
              </span>
            </div>
          </div>
        </Reveal>

        {/* ── BLOCCO 3 — Prove reali (case study + testimonianze) ──
            Renderizzato SOLO se gli array contengono dati veri.
            Finché sono vuoti, qui non appare NULLA di finto. */}
        {hasProof && (
          <div className="mt-16">
            {/* Case studies */}
            {caseStudies.length > 0 && (
              <>
                <Reveal>
                  <div className="text-center mb-10">
                    <span className="bubble-orange mb-5">Case study reali</span>
                    <h3 className="text-[24px] md:text-[36px] font-bold text-white leading-[1.15] mt-5">
                      Cosa è successo,{" "}
                      <span
                        style={{
                          fontFamily: "var(--font-serif), Georgia, serif",
                          fontStyle: "italic",
                          fontWeight: 400,
                          color: "#fb4604",
                        }}
                      >
                        per davvero.
                      </span>
                    </h3>
                  </div>
                </Reveal>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                  {caseStudies.map((c, i) => (
                    <Reveal key={i} delay={0.1 + i * 0.08}>
                      <article
                        className="res-card h-full rounded-2xl px-6 py-6 flex flex-col"
                        style={{
                          background: "rgba(255,255,255,0.035)",
                          border: "1px solid rgba(255,255,255,0.10)",
                          boxShadow: "0 18px 44px -22px rgba(0,0,0,0.6)",
                        }}
                      >
                        <div className="flex items-center justify-between mb-4">
                          <span className="text-[16px] font-bold text-white leading-tight">
                            {c.cliente}
                          </span>
                          <span
                            className="text-[10px] font-bold uppercase tracking-[0.12em] px-2.5 py-1 rounded-md shrink-0"
                            style={{
                              border: "1px solid rgba(255,255,255,0.22)",
                              color: "rgba(255,255,255,0.85)",
                              background: "rgba(255,255,255,0.08)",
                            }}
                          >
                            {c.settore}
                          </span>
                        </div>

                        <div className="mb-3">
                          <div className="text-[10.5px] uppercase tracking-[0.18em] font-black text-silver-orange mb-1">
                            Il problema
                          </div>
                          <p className="text-[13.5px] text-white/80 leading-relaxed">
                            {c.problema}
                          </p>
                        </div>

                        <div className="mb-4">
                          <div className="text-[10.5px] uppercase tracking-[0.18em] font-black text-silver-orange mb-1">
                            Il sistema
                          </div>
                          <p className="text-[13.5px] text-white/90 font-semibold leading-relaxed">
                            {c.sistema}
                          </p>
                        </div>

                        <div
                          className="mt-auto pt-4"
                          style={{ borderTop: "1px solid rgba(255,255,255,0.10)" }}
                        >
                          <div className="text-[10.5px] uppercase tracking-[0.18em] font-black text-silver-orange mb-1.5">
                            Il risultato
                          </div>
                          <p
                            className="text-[16px] font-extrabold italic text-white leading-snug"
                            style={{
                              fontFamily: "var(--font-serif), Georgia, serif",
                            }}
                          >
                            {c.risultato}
                          </p>
                        </div>
                      </article>
                    </Reveal>
                  ))}
                </div>
              </>
            )}

            {/* Testimonianze */}
            {testimonials.length > 0 && (
              <div className={caseStudies.length > 0 ? "mt-12" : ""}>
                <Reveal>
                  <div className="text-center mb-10">
                    <span className="bubble-orange mb-5">Parole dei clienti</span>
                  </div>
                </Reveal>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
                  {testimonials.map((t, i) => (
                    <Reveal key={i} delay={0.1 + i * 0.08}>
                      <figure
                        className="res-card h-full rounded-2xl px-6 py-6 flex flex-col"
                        style={{
                          background: "rgba(255,255,255,0.035)",
                          border: "1px solid rgba(255,255,255,0.10)",
                          boxShadow: "0 18px 44px -22px rgba(0,0,0,0.6)",
                        }}
                      >
                        <Quote
                          className="h-6 w-6 mb-3 text-orange-pure shrink-0"
                          strokeWidth={2}
                        />
                        <blockquote
                          className="text-[15px] text-white/90 leading-relaxed italic flex-1"
                          style={{
                            fontFamily: "var(--font-serif), Georgia, serif",
                          }}
                        >
                          &ldquo;{t.quote}&rdquo;
                        </blockquote>
                        <figcaption
                          className="mt-5 pt-4"
                          style={{ borderTop: "1px solid rgba(255,255,255,0.10)" }}
                        >
                          <div className="text-[14px] font-bold text-white leading-tight">
                            {t.autore}
                          </div>
                          <div className="text-[12px] text-white/70 font-medium mt-0.5">
                            {t.ruolo}
                          </div>
                        </figcaption>
                      </figure>
                    </Reveal>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </section>
  );
}
