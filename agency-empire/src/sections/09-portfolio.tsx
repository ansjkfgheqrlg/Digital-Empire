"use client";

import { Reveal } from "@/components/reveal";
import { TrendingUp, ArrowUpRight, Lock } from "lucide-react";

type RealCase = {
  status: "live";
  settore: string;
  cliente: string;
  positioning: string;
  risultato: string;
  metric: string;
  body: string;
  tags: string[];
  href?: string;
};

type ComingCase = {
  status: "soon";
  settore: string;
  initials: string;
  cliente: string;
  body: string;
};

type CaseStudy = RealCase | ComingCase;

const CASES: CaseStudy[] = [
  {
    status: "live",
    settore: "Info-business · Formazione AI",
    cliente: "Claude Code Mastery",
    positioning: "Da AI User a System Architect",
    risultato: "Sales page",
    metric: "lanciata su 4 varianti A/B",
    body:
      "Sales page completa per il primo percorso italiano sull'ecosistema Claude. Hero shimmer silver-orange, 25+ sezioni, framework APSOC integrato, gestione obiezioni C·P·B, garanzia Builder o Rimborsato e checkout Stripe diretto. Stack Next.js 16 + Tailwind v4 + Framer Motion + Lenis + GSAP.",
    tags: ["Sales page", "Copy APSOC", "Stripe", "Next.js 16"],
    href: "https://formazione-systemarchitect.netlify.app/",
  },
  {
    status: "soon",
    settore: "Outreach Workflow · Case study in arrivo",
    initials: "··",
    cliente: "Workflow Outreach · Cliente B2B",
    body:
      "Outreach Workflow consegnato per agenzia B2B: 240+ lead qualificati automatizzati nel primo mese. Pubblichiamo i dati completi a 60 giorni dal go-live.",
  },
  {
    status: "soon",
    settore: "Content Workflow · Case study in arrivo",
    initials: "··",
    cliente: "Workflow Content · Creator",
    body:
      "Content Workflow per creator con 50k+ follower: da 3 ore/giorno a 20 minuti di review settimanale. Numeri verificabili in pubblicazione a breve.",
  },
];

function LiveCard({ c }: { c: RealCase }) {
  const Wrapper = c.href ? "a" : "article";
  const wrapperProps = c.href
    ? {
        href: c.href,
        target: "_blank" as const,
        rel: "noopener noreferrer" as const,
      }
    : {};

  return (
    <Wrapper
      {...wrapperProps}
      className="card-brand-portfolio h-full flex flex-col group"
    >
      {/* Logo plate — silver-cream con iniziali */}
      <div
        className="aspect-[16/10] rounded-xl mb-5 grid place-items-center relative overflow-hidden"
        style={{
          background:
            "linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(251,70,4,0.20) 50%, rgba(255,200,150,0.50) 100%)",
          border: "1px solid rgba(255,255,255,0.55)",
          boxShadow:
            "inset 0 1px 0 rgba(255,255,255,0.85), inset 0 -1px 0 rgba(201,55,10,0.10)",
        }}
      >
        <span
          className="font-display text-[3rem] font-bold text-[#c93a0a] tracking-tight"
          style={{ textShadow: "0 1px 0 rgba(255,255,255,0.6)" }}
        >
          {c.cliente
            .split(" ")
            .filter((w) => w.length > 0)
            .slice(0, 3)
            .map((w) => w[0])
            .join("")}
        </span>
        <span
          className="absolute top-3 right-3 text-[0.62rem] uppercase tracking-[0.20em] font-semibold"
          style={{ color: "#fb4604", opacity: 0.75 }}
        >
          case study
        </span>
        <span
          className="absolute bottom-3 left-3 text-[0.6rem] uppercase tracking-[0.18em] font-bold inline-flex items-center gap-1.5"
          style={{ color: "#fb4604" }}
        >
          <span
            className="inline-block w-1.5 h-1.5 rounded-full"
            style={{
              background: "#fb4604",
              boxShadow: "0 0 8px rgba(251,70,4,0.55)",
            }}
          />
          live
        </span>
      </div>

      <div
        className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold mb-2"
        style={{ color: "#fb4604", textShadow: "0 1px 0 rgba(0,0,30,0.45)" }}
      >
        {c.settore}
      </div>

      <h4
        className="text-[1.20rem] font-bold text-white mb-1"
        style={{ textShadow: "0 1px 0 rgba(0,0,30,0.40)" }}
      >
        {c.cliente}
      </h4>
      <p
        className="font-accent italic text-[0.92rem] mb-4"
        style={{ color: "#ff8a4a", textShadow: "0 1px 0 rgba(0,0,30,0.40)" }}
      >
        {c.positioning}
      </p>

      <div className="flex items-baseline gap-2 mb-4">
        <span
          className="font-display text-[1.55rem] font-bold leading-none"
          style={{
            color: "#fb4604",
            textShadow: "0 1px 0 rgba(0,0,30,0.50)",
          }}
        >
          {c.risultato}
        </span>
        <span className="text-[0.82rem] text-white/85">{c.metric}</span>
      </div>

      <p className="text-[0.90rem] leading-relaxed text-white/85 mb-5 flex-1">
        {c.body}
      </p>

      <div className="flex flex-wrap items-center gap-2 pt-4 border-t border-white/25">
        {c.tags.map((t) => (
          <span
            key={t}
            className="text-[0.7rem] uppercase tracking-[0.14em] text-white/80 px-2 py-1 rounded-md border border-white/25"
          >
            {t}
          </span>
        ))}
        <ArrowUpRight
          className="h-4 w-4 ml-auto transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
          style={{ color: "#fb4604" }}
        />
      </div>
    </Wrapper>
  );
}

function ComingCard({ c }: { c: ComingCase }) {
  return (
    <article className="card-brand-portfolio-soon h-full flex flex-col">
      <div
        className="aspect-[16/10] rounded-xl mb-5 grid place-items-center relative overflow-hidden"
        style={{
          background:
            "linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%)",
          border: "1px dashed rgba(255,255,255,0.18)",
        }}
      >
        <Lock className="h-7 w-7 text-white/35" strokeWidth={1.6} />
        <span
          className="absolute top-3 right-3 text-[0.62rem] uppercase tracking-[0.20em] font-semibold text-white/40"
        >
          in arrivo
        </span>
      </div>

      <div className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-white/45 mb-2">
        {c.settore}
      </div>
      <h4 className="text-[1.20rem] font-bold text-white/65 mb-3">{c.cliente}</h4>

      <p className="text-[0.90rem] leading-relaxed text-white/55 mb-5 flex-1">
        {c.body}
      </p>

      <div className="pt-4 border-t border-white/10 text-[0.7rem] uppercase tracking-[0.14em] text-white/40">
        Pubblicazione prevista · Q2 2026
      </div>
    </article>
  );
}

export function Portfolio() {
  return (
    <section
      id="lavori"
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="portfolio-h2"
    >
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <TrendingUp className="h-3.5 w-3.5" />
              Casi reali · Lavori live
            </span>
            <h2 id="portfolio-h2" className="mt-6">
              <span className="text-silver-white">Non solo teoria.</span>{" "}
              <span className="text-silver-gold font-accent italic">
                Lavori reali.
              </span>
            </h2>
            <p className="mt-5 text-[1.0625rem] text-white/90 leading-relaxed font-light">
              Pubblichiamo solo case study con numeri verificabili. Workflow
              live, metriche reali, zero marketing. I prossimi arrivano
              man mano che i dati post go-live si consolidano.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-3 gap-6">
          {CASES.map((c, i) => (
            <Reveal key={i} delay={0.10 + i * 0.08}>
              {c.status === "live" ? <LiveCard c={c} /> : <ComingCard c={c} />}
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
