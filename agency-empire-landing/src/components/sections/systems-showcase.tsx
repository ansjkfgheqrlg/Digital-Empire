"use client";

import { Reveal } from "@/components/reveal";
import { Check, Zap, FileText, Brain, ArrowRight } from "lucide-react";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.25' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.96 0 0 0 0 0.95 0 0 0 0 0.93 0 0 0 0.30 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const systems = [
  {
    id: "outreach",
    icon: Zap,
    label: "Outreach Factory",
    tagline: "Il tuo sales team che lavora 24/7",
    metric: "312",
    metricUnit: "msg / giorno",
    metricSub: "Gmail + Instagram DM in parallelo",
    uptime: "99.7%",
    uptimeLabel: "uptime",
    seed: "9",
    accent: "#ff6030",
    accentLight: "#ffaa88",
    border: "rgba(220,140,110,0.52)",
    glow: "rgba(150,35,0,0.38)",
    bgLayers: [
      "radial-gradient(72% 52% at 8% 6%, rgba(255,255,255,0.46) 0%, transparent 48%)",
      "radial-gradient(40% 30% at 90% 92%, rgba(200,110,70,0.15) 0%, transparent 38%)",
      "linear-gradient(148deg, #3a0c00 0%, #701e00 24%, #b03600 54%, #7c2000 77%, #200800 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(251,70,4,0.32) 0%, rgba(180,36,0,0.52) 100%)",
    badgeBorder: "rgba(251,80,4,0.48)",
    steps: [
      { t: "Scraping", d: "Profili target estratti con filtri AI sul tuo ICP ideale" },
      { t: "Personalization", d: "GPT-4o scrive ogni messaggio con variabili dinamiche e brand voice" },
      { t: "Send & Track", d: "Notifica lead caldi → Slack in tempo reale + follow-up 3× automatico" },
    ],
    features: [
      "Gmail automation: 300+ email personalizzate/giorno con APSOC",
      "Instagram DM safe: proxy residenziali dedicati, comportamento umano",
      "Qualificazione semantica AI: lead caldi isolati automaticamente",
      "Follow-up sequenziale fino a 3 touchpoint per ogni prospect",
      "Dashboard web live: monitoraggio lead, status, conversazioni",
    ],
    stack: ["Python", "Selenium", "GPT-4o", "Slack API", "Gmail API", "Proxy Resi."],
    timeline: "Go-live in 7 giorni",
    roi: "Da 0 a 300+ contatti / giorno",
  },
  {
    id: "content",
    icon: FileText,
    label: "Content Factory",
    tagline: "Pubblica ogni giorno senza toccare niente",
    metric: "24",
    metricUnit: "contenuti / giorno",
    metricSub: "caroselli · reels · caption + hashtag",
    uptime: "100%",
    uptimeLabel: "upload rate",
    seed: "13",
    accent: "#ffb040",
    accentLight: "#ffd090",
    border: "rgba(220,178,120,0.52)",
    glow: "rgba(120,72,0,0.38)",
    bgLayers: [
      "radial-gradient(72% 52% at 8% 6%, rgba(255,255,255,0.43) 0%, transparent 48%)",
      "radial-gradient(40% 30% at 90% 92%, rgba(200,155,70,0.14) 0%, transparent 38%)",
      "linear-gradient(148deg, #2c1400 0%, #563000 24%, #8e5800 54%, #623e00 77%, #1a0c00 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(200,130,0,0.32) 0%, rgba(140,78,0,0.52) 100%)",
    badgeBorder: "rgba(220,150,0,0.48)",
    steps: [
      { t: "Brief Input", d: "Un argomento o prompt → sistema si attiva in automatico" },
      { t: "Generazione AI", d: "Copy CRO + grafiche costruite via browser automation in parallelo" },
      { t: "Upload Drive", d: "File organizzati per categoria, data e formato — pronti all'uso" },
    ],
    features: [
      "Caroselli Instagram APSOC-optimized: copy CRO su ogni slide",
      "Script Reels: hook, corpo, CTA in formato 30-60 secondi",
      "Caption + hashtag strategici per massimizzare reach organico",
      "Costruzione automatica grafiche via browser automation",
      "Upload organizzato su Google Drive per argomento e data",
    ],
    stack: ["GPT-4o", "Browser Auto.", "Drive API", "Canva API", "FFmpeg"],
    timeline: "Go-live in 7 giorni",
    roi: "Settimane di contenuti in minuti",
  },
  {
    id: "brain",
    icon: Brain,
    label: "Second Brain",
    tagline: "La tua azienda sa tutto. Sempre.",
    metric: "1.4k",
    metricUnit: "query / giorno",
    metricSub: "risposta media in 0.3 secondi",
    uptime: "99.8%",
    uptimeLabel: "uptime",
    seed: "3",
    accent: "#70b8ff",
    accentLight: "#a8d4ff",
    border: "rgba(140,185,240,0.52)",
    glow: "rgba(0,44,150,0.38)",
    bgLayers: [
      "radial-gradient(72% 52% at 8% 6%, rgba(255,255,255,0.32) 0%, transparent 48%)",
      "radial-gradient(40% 30% at 90% 92%, rgba(90,150,240,0.14) 0%, transparent 38%)",
      "linear-gradient(148deg, #010b26 0%, #081c42 24%, #103c7c 54%, #082a5c 77%, #010810 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(50,120,255,0.30) 0%, rgba(8,54,180,0.52) 100%)",
    badgeBorder: "rgba(70,140,255,0.46)",
    steps: [
      { t: "Indicizzazione", d: "Notion, Drive, Obsidian vettorizzati in real-time nel knowledge graph" },
      { t: "Query AI", d: "Domanda in linguaggio naturale → risposta precisa con source citation" },
      { t: "Sync live", d: "Ogni documento nuovo aggiornato automaticamente nella base di conoscenza" },
    ],
    features: [
      "Wiki aziendale strutturata: prodotti, processi, clienti, decisioni",
      "AI risponde in tempo reale a qualsiasi domanda operativa",
      "Aggiornamento continuo: ogni info archiviata e resa ricercabile",
      "Connessione a Notion, Google Drive, Obsidian o sistema custom",
      "Accesso team: ogni membro trova ciò che cerca in secondi",
    ],
    stack: ["RAG Pipeline", "OpenAI Embed.", "Notion API", "Drive API", "Pinecone"],
    timeline: "Go-live in 10 giorni",
    roi: "Zero dispersione di conoscenza aziendale",
  },
];

const bottomStats = [
  { n: "312+", l: "messaggi / giorno per cliente" },
  { n: "7", l: "giorni al primo go-live" },
  { n: "0 €", l: "canoni mensili SaaS" },
  { n: "100%", l: "codice proprietario tuo" },
];

export function SystemsShowcase() {
  return (
    <section id="servizi" className="bg-ink section section-border-t relative overflow-hidden">
      <style>{`
        @keyframes ss-pulse {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.30; transform: scale(0.65); }
        }
        .ss-dot { animation: ss-pulse 2.2s ease-in-out infinite; }
        .ss-card {
          transition: transform 0.45s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease;
        }
        .ss-card:hover { transform: translateY(-9px) scale(1.012); }
        .ss-step-connector {
          background: linear-gradient(180deg, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.04) 100%);
        }
        .ss-stat-card {
          transition: transform 0.3s ease, background 0.3s ease;
        }
        .ss-stat-card:hover {
          transform: translateY(-3px);
          background: rgba(255,255,255,0.07) !important;
        }
      `}</style>

      {/* Ambient top glow */}
      <div aria-hidden="true" className="pointer-events-none absolute inset-0"
        style={{
          background: "radial-gradient(ellipse 90% 40% at 50% 0%, rgba(251,70,4,0.07) 0%, transparent 55%)",
        }} />

      <div className="max-w-6xl mx-auto px-6 relative z-10">

        {/* ── Section header ── */}
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">Tre sistemi. Zero compromessi.</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[28px] md:text-[48px] font-bold leading-[1.15] mt-6 text-white">
              Ogni sistema,{" "}
              <span
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  color: "#fb4604",
                }}
              >
                nel dettaglio.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.18}>
            <p className="text-white/80 mt-5 text-[1.05rem] md:text-[1.15rem] max-w-2xl mx-auto leading-relaxed font-medium">
              Implementazioni AI verticali — ognuna automatizza un&apos;area precisa del tuo business.
              Girano sui <strong className="text-white font-semibold">tuoi server</strong>, con il
              <strong className="text-white font-semibold"> codice sorgente incluso</strong>. Nessun canone, nessuna dipendenza.
            </p>
          </Reveal>
        </div>

        {/* ── 3 Cards ── */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5 items-start">
          {systems.map((s, si) => {
            const Icon = s.icon;
            return (
              <Reveal key={s.id} delay={0.15 + si * 0.11}>
                <article
                  className="ss-card rounded-2xl overflow-hidden flex flex-col"
                  style={{
                    backgroundImage: [GRAIN(s.seed), ...s.bgLayers].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal, normal",
                    border: `1.5px solid ${s.border}`,
                    boxShadow: [
                      `0 0 48px -14px ${s.glow}`,
                      "0 22px 56px -16px rgba(0,0,0,0.70)",
                      "0 2px 0 rgba(255,255,255,0.26) inset",
                      "0 -1px 0 rgba(0,0,0,0.28) inset",
                      "0 0 0 1px rgba(255,255,255,0.06) inset",
                    ].join(", "),
                  }}
                >
                  {/* ── HEADER ── */}
                  <div className="px-5 pt-5 pb-4"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div className="flex items-center justify-between mb-2.5">
                      <span
                        className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-[10.5px] font-black uppercase tracking-[0.16em]"
                        style={{
                          background: s.badgeBg,
                          border: `1px solid ${s.badgeBorder}`,
                          color: "#ffffff",
                        }}
                      >
                        <Icon className="h-3.5 w-3.5" style={{ color: s.accentLight }} />
                        {s.label}
                      </span>
                      <span className="flex items-center gap-1.5">
                        <span className="ss-dot w-2 h-2 rounded-full bg-green-400"
                          style={{ animationDelay: `${si * 0.65}s`, boxShadow: "0 0 8px rgba(74,222,128,0.9)" }} />
                        <span className="text-[10px] font-black uppercase tracking-[0.18em] text-green-300">live</span>
                      </span>
                    </div>
                    <p className="text-[14px] font-semibold text-white/85 italic leading-snug"
                      style={{ fontFamily: "var(--font-serif), Georgia, serif" }}>
                      {s.tagline}
                    </p>
                  </div>

                  {/* ── HERO METRIC ── */}
                  <div className="px-5 py-5 flex items-end justify-between"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div>
                      <div
                        className="font-black leading-none mb-1"
                        style={{
                          fontSize: "clamp(2.8rem, 4.5vw, 3.6rem)",
                          letterSpacing: "-0.05em",
                          color: "#ffffff",
                          textShadow: `0 0 55px ${s.glow}, 0 2px 8px rgba(0,0,0,0.55)`,
                        }}
                      >
                        {s.metric}
                      </div>
                      <div className="text-[11.5px] font-black uppercase tracking-[0.16em] mb-1"
                        style={{ color: s.accentLight }}>
                        {s.metricUnit}
                      </div>
                      <div className="text-[12px] text-white/70 font-medium">{s.metricSub}</div>
                      <div className="text-[10px] uppercase tracking-[0.14em] font-semibold text-white/50 mt-1.5">
                        Capacità del sistema · esempio di configurazione
                      </div>
                    </div>
                    <div className="text-right shrink-0">
                      <div className="text-[1.5rem] font-black text-white leading-none mb-1"
                        style={{ letterSpacing: "-0.03em" }}>
                        {s.uptime}
                      </div>
                      <div className="text-[10px] uppercase tracking-[0.18em] text-white/65 font-bold">
                        {s.uptimeLabel}
                      </div>
                    </div>
                  </div>

                  {/* ── HOW IT WORKS ── */}
                  <div className="px-5 py-4"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div className="text-[10.5px] uppercase tracking-[0.24em] font-black mb-3"
                      style={{ color: s.accentLight }}>
                      Come funziona
                    </div>
                    <div className="flex flex-col gap-0">
                      {s.steps.map((step, si2) => (
                        <div key={si2} className="flex gap-3">
                          <div className="shrink-0 flex flex-col items-center">
                            <span
                              className="w-6 h-6 rounded-full flex items-center justify-center text-[11px] font-black shrink-0"
                              style={{
                                background: s.badgeBg,
                                border: `1px solid ${s.badgeBorder}`,
                                color: "#ffffff",
                              }}
                            >
                              {si2 + 1}
                            </span>
                            {si2 < s.steps.length - 1 && (
                              <div className="w-px flex-1 my-0.5 ss-step-connector" style={{ minHeight: 16 }} />
                            )}
                          </div>
                          <div className={si2 < s.steps.length - 1 ? "pb-3.5" : ""}>
                            <div className="text-[13.5px] font-bold text-white leading-tight">{step.t}</div>
                            <div className="text-[12.5px] text-white/75 leading-snug mt-1">{step.d}</div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* ── FEATURES ── */}
                  <div className="px-5 py-4"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div className="text-[10.5px] uppercase tracking-[0.24em] font-black mb-3"
                      style={{ color: s.accentLight }}>
                      Cosa è incluso
                    </div>
                    <div className="flex flex-col gap-2.5">
                      {s.features.map((f, fi) => (
                        <div key={fi} className="flex items-start gap-2.5">
                          <Check className="h-4 w-4 mt-[1px] shrink-0" style={{ color: s.accentLight }} strokeWidth={3} />
                          <span className="text-[13px] text-white/90 leading-snug font-medium">{f}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* ── TECH STACK ── */}
                  <div className="px-5 py-3.5"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div className="text-[10.5px] uppercase tracking-[0.24em] font-black mb-2.5"
                      style={{ color: s.accentLight }}>
                      Stack tecnico
                    </div>
                    <div className="flex flex-wrap gap-1.5">
                      {s.stack.map(t => (
                        <span key={t}
                          className="text-[10px] font-bold uppercase tracking-[0.10em] px-2.5 py-1 rounded-md"
                          style={{
                            border: "1px solid rgba(255,255,255,0.28)",
                            color: "rgba(255,255,255,0.88)",
                            background: "rgba(255,255,255,0.10)",
                          }}>
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* ── ROI ROW ── */}
                  <div className="px-5 py-4"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                    <div className="text-[10.5px] uppercase tracking-[0.20em] font-black mb-1.5"
                      style={{ color: s.accentLight }}>
                      Il risultato per te
                    </div>
                    <div className="text-[15px] font-extrabold italic text-white leading-snug"
                      style={{ fontFamily: "var(--font-serif), Georgia, serif" }}>
                      {s.roi}
                    </div>
                  </div>

                  {/* ── FOOTER ── */}
                  <div className="px-5 py-4 flex items-center justify-between mt-auto">
                    <span
                      className="text-[11px] font-black uppercase tracking-[0.14em]"
                      style={{ color: s.accentLight }}
                    >
                      ⚡ {s.timeline}
                    </span>
                    <a
                      href="#prenota"
                      className="flex items-center gap-1.5 text-[11px] font-black uppercase tracking-[0.12em] text-white hover:text-white transition-colors duration-200 group"
                    >
                      Prenota ora
                      <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
                    </a>
                  </div>
                </article>
              </Reveal>
            );
          })}
        </div>

        {/* ── Bottom stats bar ── */}
        <Reveal delay={0.50}>
          <div className="mt-8 grid grid-cols-2 md:grid-cols-4 gap-3">
            {bottomStats.map((stat, i) => (
              <div
                key={i}
                className="ss-stat-card rounded-xl px-5 py-4 text-center"
                style={{
                  background: "rgba(255,255,255,0.04)",
                  border: "1px solid rgba(255,255,255,0.09)",
                }}
              >
                <div
                  className="font-black text-white leading-none mb-2"
                  style={{ fontSize: "clamp(1.6rem,2.6vw,2rem)", letterSpacing: "-0.04em" }}
                >
                  {stat.n}
                </div>
                <div className="text-[11px] uppercase tracking-[0.14em] text-white/75 font-bold leading-snug">
                  {stat.l}
                </div>
              </div>
            ))}
          </div>
        </Reveal>
      </div>
    </section>
  );
}
