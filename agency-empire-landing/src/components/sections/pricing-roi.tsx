"use client";

import { Reveal } from "@/components/reveal";
import { CallCTA, CALL_URL } from "@/components/call-cta";
import { Zap, Brain, FileText, Layers, Check, ArrowRight, Shield, TrendingUp } from "lucide-react";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.96 0 0 0 0 0.95 0 0 0 0 0.94 0 0 0 0.30 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const SILVER_BORDER = "2px solid rgba(210,218,232,0.65)";

const services = [
  {
    n: "01",
    icon: Zap,
    name: "Outreach Factory",
    tagline: "Il tuo sales team che non dorme mai.",
    desc: "300+ messaggi personalizzati al giorno su Gmail e Instagram. Qualificazione AI, follow-up automatico, dashboard web. Zero intervento manuale.",
    features: [
      "Script Gmail: 300+ email/gg con APSOC framework",
      "Instagram DM safe — proxy residenziali dedicati",
      "Qualificazione AI + notifica lead caldi su Slack",
      "Dashboard web custom per lead management",
      "90gg supporto post-setup incluso",
    ],
    price: "€4.000",
    terms: "Pagamento unico · 50% acconto, 50% consegna",
    cta: "Installa l'Outreach →",
    seed: "11",
    bgLayers: [
      "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.46) 0%, transparent 52%)",
      "linear-gradient(145deg, #321000 0%, #521e00 18%, #922e00 40%, #cc4800 62%, #0d0a04 100%)",
    ],
    iconBg: "linear-gradient(135deg, rgba(251,70,4,0.40) 0%, rgba(201,55,10,0.55) 100%)",
    iconBorder: "rgba(251,70,4,0.55)",
    iconColor: "#fb4604",
    labelColor: "#ff8855",
    priceGlow: "rgba(251,70,4,0.45)",
    ctaColor: "#fb7040",
  },
  {
    n: "02",
    icon: Brain,
    name: "Second Brain",
    tagline: "La tua azienda sa tutto. Sempre.",
    desc: "Knowledge base aziendale AI: documenti, processi, clienti, decisioni — tutto indicizzato. L'AI risponde in tempo reale a qualsiasi domanda sulla tua operatività.",
    features: [
      "Wiki aziendale a grafo relazionale su misura",
      "AI risponde in tempo reale sulla knowledge base",
      "Integrazione LLM personalizzata sul tuo brand",
      "Workflow di aggiornamento continuo automatico",
      "90gg supporto post-setup incluso",
    ],
    price: "€2.500",
    terms: "Pagamento unico · 50% acconto, 50% consegna",
    cta: "Installa il Second Brain →",
    seed: "6",
    bgLayers: [
      "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.34) 0%, transparent 52%)",
      "linear-gradient(145deg, #001e44 0%, #003270 18%, #004898 38%, #003878 60%, #001840 100%)",
    ],
    iconBg: "linear-gradient(135deg, rgba(100,180,255,0.35) 0%, rgba(30,80,180,0.55) 100%)",
    iconBorder: "rgba(100,180,255,0.50)",
    iconColor: "#90c0ff",
    labelColor: "#90c0ff",
    priceGlow: "rgba(60,130,255,0.38)",
    ctaColor: "#90c0ff",
  },
  {
    n: "03",
    icon: FileText,
    name: "Content Factory",
    tagline: "Pubblica ogni giorno senza toccare niente.",
    desc: "Caroselli APSOC, script Reels, caption e hashtag generati su richiesta. Upload automatico su Drive. Un brief → contenuti pronti in 30 secondi.",
    features: [
      "Caroselli IG con copy CRO-ottimizzato APSOC",
      "Script video Reels / TikTok / YouTube",
      "Caption + hashtag strategici per reach organico",
      "Upload automatico su Google Drive organizzato",
      "90gg supporto post-setup incluso",
    ],
    price: "€3.500",
    terms: "Pagamento unico · 50% acconto, 50% consegna",
    cta: "Installa la Content Factory →",
    seed: "13",
    bgLayers: [
      "radial-gradient(82% 62% at 4% 5%, rgba(255,255,255,0.42) 0%, transparent 52%)",
      "linear-gradient(145deg, #2e1a00 0%, #4e3000 18%, #7e5200 40%, #aa7000 62%, #0d0a04 100%)",
    ],
    iconBg: "linear-gradient(135deg, rgba(220,160,20,0.38) 0%, rgba(160,100,0,0.55) 100%)",
    iconBorder: "rgba(220,160,20,0.52)",
    iconColor: "#f0c060",
    labelColor: "#f0c060",
    priceGlow: "rgba(200,130,0,0.40)",
    ctaColor: "#f0c060",
  },
];

const engineRoomFeatures = [
  "Tutto di Outreach Factory incluso",
  "Tutto di Second Brain incluso",
  "Tutto di Content Factory incluso",
  "Dashboard unificata — i 3 sistemi comunicano in tempo reale",
  "Sessione strategica di mappatura funnel",
  "60gg supporto prioritario + formazione team",
];

export function PricingROI() {
  return (
    <section className="bg-ink section section-border-t" id="prenota">
      <div className="max-w-6xl mx-auto px-6">

        {/* Header */}
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Prezzi · Nessuna sorpresa</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6">
              <span className="text-silver-white">Un sistema AI proprietario. </span>
              <span className="text-silver-orange">Un asset permanente.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/80 text-lg max-w-2xl mx-auto mt-5 leading-relaxed">
              Scegli uno o più sistemi. Con Engine Room prendi tutto insieme e risparmi €2.000 sul totale.
            </p>
          </Reveal>
        </div>

        {/* 3 service cards */}
        <div className="grid md:grid-cols-3 gap-5 mb-5">
          {services.map((s, i) => {
            const Icon = s.icon;
            return (
              <Reveal key={i} delay={0.1 + i * 0.08}>
                <article
                  className="flex flex-col h-full rounded-[22px] p-7"
                  style={{
                    backgroundImage: [GRAIN(s.seed), ...s.bgLayers].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal",
                    border: SILVER_BORDER,
                    boxShadow: [
                      `0 0 50px -18px ${s.priceGlow}`,
                      "0 30px 70px -24px rgba(0,0,0,0.80)",
                      "0 2px 0 rgba(255,255,255,0.18) inset",
                      "0 -1px 0 rgba(0,0,0,0.40) inset",
                    ].join(", "),
                    color: "#ffffff",
                    transition: "transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease",
                  }}
                >
                  {/* Top: icon + motore label */}
                  <div className="flex items-center justify-between mb-5">
                    <span
                      className="grid place-items-center w-12 h-12 rounded-xl flex-shrink-0"
                      style={{
                        background: s.iconBg,
                        border: `1px solid ${s.iconBorder}`,
                        boxShadow: `0 6px 20px ${s.priceGlow}, inset 0 1px 0 rgba(255,255,255,0.22)`,
                      }}
                    >
                      <Icon className="h-5 w-5" style={{ color: s.iconColor }} />
                    </span>
                    <span
                      style={{
                        fontSize: "0.62rem",
                        fontWeight: 800,
                        letterSpacing: "0.24em",
                        textTransform: "uppercase",
                        color: s.labelColor,
                        opacity: 0.90,
                      }}
                    >
                      [ MOTORE {s.n} ]
                    </span>
                  </div>

                  {/* Name + tagline */}
                  <h3 className="text-[1.5rem] font-bold leading-tight mb-1 text-white">
                    {s.name}
                  </h3>
                  <p
                    className="text-[0.9rem] mb-4"
                    style={{
                      fontFamily: "var(--font-serif), Georgia, serif",
                      fontStyle: "italic",
                      color: "rgba(255,255,255,0.72)",
                    }}
                  >
                    {s.tagline}
                  </p>

                  {/* Description */}
                  <p className="text-[0.88rem] text-white/80 leading-relaxed mb-5">
                    {s.desc}
                  </p>

                  {/* Features */}
                  <ul className="flex flex-col gap-2.5 mb-6 flex-1">
                    {s.features.map((f, fi) => (
                      <li key={fi} className="flex items-start gap-2.5 text-[0.85rem] text-white/90">
                        <Check className="h-3.5 w-3.5 mt-0.5 shrink-0" style={{ color: s.iconColor }} strokeWidth={3} />
                        <span>{f}</span>
                      </li>
                    ))}
                  </ul>

                  {/* Price block */}
                  <div
                    className="rounded-xl px-5 py-4 mb-5"
                    style={{
                      background: "rgba(0,0,0,0.28)",
                      border: "1px solid rgba(255,255,255,0.10)",
                    }}
                  >
                    <div
                      className="text-[2.25rem] font-black leading-none mb-1"
                      style={{
                        color: "#ffffff",
                        textShadow: `0 0 28px ${s.priceGlow}`,
                      }}
                    >
                      {s.price}
                    </div>
                    <div className="text-[0.72rem] uppercase tracking-[0.18em] font-semibold" style={{ color: s.labelColor }}>
                      {s.terms}
                    </div>
                  </div>

                  {/* CTA */}
                  <a
                    href={CALL_URL} target="_blank" rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 text-[0.875rem] font-bold mt-auto group"
                    style={{ color: s.ctaColor }}
                  >
                    {s.cta}
                  </a>
                </article>
              </Reveal>
            );
          })}
        </div>

        {/* ENGINE ROOM — combo wide card */}
        <Reveal delay={0.35}>
          <div className="relative mb-12">
            {/* Best value badge */}
            <div className="flex justify-center mb-0 relative z-10">
              <span
                className="inline-flex items-center gap-2 px-5 py-1.5 rounded-full text-[0.72rem] font-black uppercase tracking-[0.22em]"
                style={{
                  background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
                  color: "#ffffff",
                  boxShadow: "0 6px 24px rgba(251,70,4,0.55)",
                  transform: "translateY(50%)",
                }}
              >
                ✦ Miglior Valore ✦
              </span>
            </div>

            <article
              className="rounded-[22px] p-8 md:p-10"
              style={{
                backgroundImage: [
                  GRAIN("3"),
                  "radial-gradient(80% 60% at 5% 5%, rgba(255,255,255,0.30) 0%, transparent 50%)",
                  "radial-gradient(60% 50% at 95% 95%, rgba(251,70,4,0.18) 0%, transparent 50%)",
                  "linear-gradient(145deg, #1a1200 0%, #2e2000 22%, #463200 50%, #2e2000 75%, #111000 100%)",
                ].join(", "),
                backgroundSize: "200px 200px, 100% 100%, 100% 100%, 100% 100%",
                backgroundBlendMode: "screen, normal, normal, normal",
                border: "2px solid rgba(210,218,232,0.80)",
                boxShadow: [
                  "0 0 80px -20px rgba(251,70,4,0.40)",
                  "0 40px 80px -28px rgba(0,0,0,0.85)",
                  "0 2px 0 rgba(255,255,255,0.25) inset",
                ].join(", "),
                color: "#ffffff",
              }}
            >
              <div className="flex flex-col md:flex-row md:items-start gap-8">
                {/* Left: icon + info */}
                <div className="flex-shrink-0">
                  <div className="flex items-center gap-4 mb-4">
                    <span
                      className="grid place-items-center w-14 h-14 rounded-2xl"
                      style={{
                        background: "linear-gradient(135deg, rgba(251,70,4,0.45) 0%, rgba(180,40,0,0.65) 100%)",
                        border: "1px solid rgba(251,100,50,0.60)",
                        boxShadow: "0 8px 24px rgba(251,70,4,0.45), inset 0 1px 0 rgba(255,255,255,0.22)",
                      }}
                    >
                      <Layers className="h-6 w-6 text-orange-pure" />
                    </span>
                    <div>
                      <div
                        className="text-[0.62rem] uppercase tracking-[0.24em] font-black mb-0.5"
                        style={{ color: "rgba(251,150,80,0.90)" }}
                      >
                        [ INTEGRAZIONE TOTALE ]
                      </div>
                      <h3 className="text-[1.75rem] md:text-[2rem] font-black leading-tight text-white">
                        Engine Room
                      </h3>
                    </div>
                  </div>
                  <p className="text-[0.94rem] text-white/80 leading-relaxed max-w-sm">
                    Tutti e tre i motori centralizzati in un&apos;unica Dashboard premium. I lead caldi dell&apos;outreach,
                    i contenuti ottimizzati e la memoria del business lavorano in sinergia totale — ogni motore alimenta gli altri in tempo reale.
                  </p>
                </div>

                {/* Middle: features grid */}
                <div className="flex-1">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {engineRoomFeatures.map((f, i) => (
                      <div key={i} className="flex items-start gap-2.5 text-[0.88rem] text-white/90">
                        <Check className="h-4 w-4 mt-0.5 shrink-0 text-orange-pure" strokeWidth={3} />
                        <span>{f}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Right: price + CTA */}
                <div className="flex-shrink-0 flex flex-col items-start md:items-end gap-4">
                  <div className="text-right">
                    <div className="flex items-baseline gap-3 flex-wrap md:justify-end">
                      <span
                        className="text-[2.5rem] md:text-[3rem] font-black leading-none"
                        style={{
                          color: "#ffffff",
                          textShadow: "0 0 36px rgba(251,70,4,0.55)",
                        }}
                      >
                        €8.000
                      </span>
                      <span
                        className="text-[1.25rem] font-semibold line-through"
                        style={{ color: "rgba(255,255,255,0.35)", textDecorationColor: "rgba(255,255,255,0.25)" }}
                      >
                        €10.000
                      </span>
                    </div>
                    <div className="text-[0.72rem] uppercase tracking-[0.18em] font-bold mt-1" style={{ color: "#fb7040" }}>
                      Risparmio €2.000 · 50% acconto, 50% consegna
                    </div>
                  </div>
                  <a
                    href={CALL_URL} target="_blank" rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 text-[0.95rem] font-black uppercase tracking-[0.12em] text-white group"
                    style={{
                      background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
                      borderRadius: 12,
                      padding: "0.85rem 1.75rem",
                      boxShadow: "0 0 32px rgba(251,70,4,0.45), inset 0 1px 0 rgba(255,255,255,0.22)",
                      transition: "filter 0.25s, transform 0.25s",
                    }}
                  >
                    Sistema Completo
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                  </a>
                </div>
              </div>
            </article>
          </div>
        </Reveal>

        {/* ROI Calculator */}
        <Reveal delay={0.45}>
          <div
            className="card-dark p-8 text-left"
            style={{ borderColor: "rgba(34,197,94,0.20)", background: "rgba(34,197,94,0.04)" }}
          >
            <div className="flex items-start gap-6">
              <div
                className="w-12 h-12 rounded-full flex items-center justify-center shrink-0"
                style={{ background: "rgba(34,197,94,0.12)" }}
              >
                <TrendingUp className="h-6 w-6 text-green-500" />
              </div>
              <div className="w-full">
                <h3 className="text-xl font-bold text-white mb-3">La matematica</h3>

                {/* Confronto una-tantum vs ricorrente */}
                <div className="grid sm:grid-cols-2 gap-3 mb-4">
                  <div
                    className="rounded-xl px-5 py-4"
                    style={{ background: "rgba(0,0,0,0.28)", border: "1px solid rgba(255,255,255,0.10)" }}
                  >
                    <div className="text-[0.7rem] uppercase tracking-[0.18em] font-bold text-white/60 mb-1">
                      Outreach Factory · una tantum
                    </div>
                    <div className="text-[1.6rem] font-black text-white leading-none">€4.000</div>
                    <div className="text-[0.8rem] text-white/70 mt-1">Lo paghi una volta. Il codice resta tuo.</div>
                  </div>
                  <div
                    className="rounded-xl px-5 py-4"
                    style={{ background: "rgba(0,0,0,0.28)", border: "1px solid rgba(255,255,255,0.10)" }}
                  >
                    <div className="text-[0.7rem] uppercase tracking-[0.18em] font-bold text-white/60 mb-1">
                      SaaS di outreach · ricorrente
                    </div>
                    <div className="text-[1.6rem] font-black text-white leading-none">€200<span className="text-[0.9rem] font-bold text-white/60">/mese</span></div>
                    <div className="text-[0.8rem] text-white/70 mt-1">€2.400/anno. Per sempre. Non è mai tuo.</div>
                  </div>
                </div>

                {/* Payback */}
                <p className="text-white/82 leading-relaxed text-[15px]">
                  €4.000 una tantum vs €200/mese fanno{" "}
                  <strong className="text-silver-white font-bold">~20 mesi per pareggiare</strong>.
                  Ma dopo i 20 mesi il SaaS continui a pagarlo a vita — il tuo sistema no:{" "}
                  <strong className="text-white font-bold underline decoration-orange-pure decoration-2 underline-offset-4 text-silver-white">
                    gira a costo zero per sempre
                  </strong>
                  . E il codice resta tuo. Senza contare il tempo risparmiato: 300+ messaggi/giorno automatici vs 30 a mano.
                </p>
              </div>
            </div>
          </div>
        </Reveal>

        {/* Bottom CTA strip */}
        <Reveal delay={0.5}>
          <div className="mt-12 flex flex-col items-center gap-5 text-center">
            <CallCTA variant="dark" />
            <div className="flex items-center gap-6 text-xs uppercase tracking-widest text-white/75 font-bold">
              <span className="flex items-center gap-2">
                <Shield className="h-3.5 w-3.5 text-orange-pure" /> Garanzia 30 Giorni
              </span>
              <span>·</span>
              <span>Rateizzazione Disponibile</span>
              <span>·</span>
              <span>Zero Canoni Mensili</span>
            </div>
          </div>
        </Reveal>

      </div>
    </section>
  );
}
