"use client";

import { ArrowRight, Shield } from "lucide-react";
import { Reveal } from "@/components/reveal";

const BOOKING_URL = "#prenota";

const nodes = [
  {
    id: "outreach",
    label: "Outreach Factory",
    metric: "312",
    metricSub: "msg / giorno",
    bar: 78,
    barLabel: "78% lead qualificati",
    color: "#ff7040",
    border: "rgba(255,100,40,0.65)",
    glow: "rgba(180,40,0,0.70)",
    bgImage: [
      "radial-gradient(80% 50% at 14% 6%, rgba(255,255,255,0.44) 0%, transparent 52%)",
      "linear-gradient(155deg, #5a1200 0%, #8c2800 28%, #c43800 62%, #6a1600 100%)",
    ].join(", "),
    inputs: ["Gmail", "Instagram DM"],
    outputs: ["Lead → Slack", "Follow-up ×3", "Dashboard live"],
  },
  {
    id: "content",
    label: "Content Factory",
    metric: "24",
    metricSub: "contenuti / giorno",
    bar: 91,
    barLabel: "Upload Drive: completato",
    color: "#ffd080",
    border: "rgba(255,200,80,0.60)",
    glow: "rgba(140,90,0,0.65)",
    bgImage: [
      "radial-gradient(80% 50% at 14% 6%, rgba(255,255,255,0.40) 0%, transparent 52%)",
      "linear-gradient(155deg, #3c2200 0%, #6a4000 28%, #9e6400 62%, #4e2e00 100%)",
    ].join(", "),
    inputs: ["Brief testuale"],
    outputs: ["Carosello Drive", "Script Reels", "Caption + tag"],
  },
  {
    id: "brain",
    label: "Second Brain",
    metric: "1.4k",
    metricSub: "query / giorno",
    bar: 98,
    barLabel: "Uptime 99.8%",
    color: "#a0d0ff",
    border: "rgba(100,180,255,0.62)",
    glow: "rgba(0,50,180,0.70)",
    bgImage: [
      "radial-gradient(80% 50% at 14% 6%, rgba(255,255,255,0.32) 0%, transparent 52%)",
      "linear-gradient(155deg, #001c44 0%, #003480 28%, #0054b4 62%, #002260 100%)",
    ].join(", "),
    inputs: ["Notion", "Google Drive"],
    outputs: ["Query → 0.3s", "Wiki indicizzata", "Sync live"],
  },
];

export function VSL() {
  return (
    <section
      className="section section-border-t relative overflow-hidden"
      style={{
        // WebP q82: 3,18 MB -> 388 KB. La grana rossa e' rumore ad alta frequenza:
        // se comparisse banding, rigenerare a q88.
        backgroundImage: "url('/vsl-bg.webp')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
      }}
    >
      {/* Velo scuro: alza il contrasto del testo sul fondo rosso granuloso. */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{ background: "rgba(20,10,6,0.34)" }}
      />
      <style>{`
        @keyframes pulse-dot {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.40; transform: scale(0.75); }
        }
        @keyframes flow-dash {
          0%   { stroke-dashoffset: 0; }
          100% { stroke-dashoffset: -20; }
        }
        .live-dot  { animation: pulse-dot 1.8s ease-in-out infinite; }
        .flow-line { animation: flow-dash 1.4s linear infinite; }
        .node-card {
          transition: transform 0.4s cubic-bezier(0.22,1,0.36,1),
                      box-shadow 0.4s ease;
        }
        .node-card:hover { transform: translateY(-7px) scale(1.012); }
      `}</style>

      <div aria-hidden="true" className="pointer-events-none absolute inset-0"
        style={{ background: "rgba(6,4,4,0.14)" }} />

      <div className="max-w-5xl mx-auto px-6 relative z-10">

        {/* ── Header ── */}
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">Sistema live · Tre implementazioni attive</span>
          </Reveal>
          <Reveal delay={0.12}>
            <p className="text-[11px] font-black uppercase tracking-[0.28em] text-white/60 mt-7 mb-4"
              style={{ textShadow: "0 1px 8px rgba(0,0,0,0.9)" }}>
              Digital Empire · Come funziona il sistema
            </p>
          </Reveal>
          <Reveal delay={0.18}>
            <h2 className="text-[20px] md:text-[38px] font-extrabold leading-[1.5] tracking-tight">
              <span style={{
                background: "linear-gradient(135deg, #fb4604 0%, #d93d00 50%, #ff6a2e 100%)",
                color: "#ffffff",
                padding: "0.12em 0.45em",
                boxDecorationBreak: "clone",
                WebkitBoxDecorationBreak: "clone",
                boxShadow: "0 0 60px rgba(251,70,4,0.55), 0 4px 24px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.22)",
                textShadow: "0 1px 3px rgba(0,0,0,0.5)",
                letterSpacing: "-0.02em",
              }}>
                Tre sistemi. Un&apos;unica operatività che gira da sola.
              </span>
            </h2>
          </Reveal>
        </div>

        {/* ── Desktop flow map ── */}
        <Reveal delay={0.24}>
          <div className="hidden md:flex items-stretch gap-0">
            {nodes.map((n, i) => (
              <div key={n.id} className="contents">

                {/* Node card */}
                <div
                  className="node-card flex-1 rounded-xl flex flex-col overflow-hidden"
                  style={{
                    backgroundImage: n.bgImage,
                    backgroundSize: "100% 100%, 100% 100%",
                    border: `1.5px solid ${n.border}`,
                    boxShadow: [
                      "0 2px 0 rgba(255,255,255,0.28) inset",
                      "0 -1px 0 rgba(0,0,0,0.25) inset",
                      "0 0 0 1px rgba(255,255,255,0.08) inset",
                      `0 0 70px -14px ${n.glow}`,
                      "0 32px 90px -24px rgba(0,0,0,0.88)",
                    ].join(", "),
                  }}
                >
                  {/* INPUT */}
                  <div className="px-5 pt-5 pb-4"
                    style={{ borderBottom: "1px solid rgba(255,255,255,0.10)" }}>
                    <div className="text-[10px] uppercase tracking-[0.24em] font-black text-white/60 mb-2">
                      Input
                    </div>
                    <div className="flex flex-wrap gap-1.5">
                      {n.inputs.map(inp => (
                        <span key={inp}
                          className="text-[11px] font-bold uppercase tracking-[0.10em] px-2.5 py-1 rounded-full"
                          style={{
                            border: "1px solid rgba(255,255,255,0.40)",
                            color: "#ffffff",
                            background: "rgba(255,255,255,0.16)",
                          }}>
                          {inp}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* METRIC */}
                  <div className="px-5 py-5 flex-1">
                    <div className="flex items-center justify-between mb-5">
                      <span className="text-[12px] font-black uppercase tracking-[0.18em] text-white">
                        {n.label}
                      </span>
                      <span className="flex items-center gap-1.5">
                        <span className="live-dot w-1.5 h-1.5 rounded-full bg-green-400"
                          style={{ animationDelay: `${i * 0.55}s` }} />
                        <span className="text-[10px] font-black uppercase tracking-[0.18em] text-green-300">live</span>
                      </span>
                    </div>

                    <div className="font-black leading-none mb-0.5 text-white"
                      style={{
                        fontSize: "clamp(3rem, 5vw, 4.25rem)",
                        letterSpacing: "-0.045em",
                        textShadow: `0 0 80px ${n.glow}, 0 2px 6px rgba(0,0,0,0.45)`,
                      }}>
                      {n.metric}
                    </div>
                    <div className="text-[11.5px] font-bold uppercase tracking-[0.18em] text-white/75 mb-2">
                      {n.metricSub}
                    </div>
                    <div className="text-[10px] uppercase tracking-[0.14em] font-semibold text-white/60 mb-6">
                      Capacità del sistema
                    </div>

                    {/* Progress */}
                    <div className="w-full h-1.5 rounded-full mb-1.5"
                      style={{ background: "rgba(255,255,255,0.14)" }}>
                      <div className="h-1.5 rounded-full"
                        style={{
                          width: `${n.bar}%`,
                          background: "linear-gradient(90deg, rgba(255,255,255,0.55), rgba(255,255,255,0.95))",
                          boxShadow: "0 0 14px rgba(255,255,255,0.55)",
                        }} />
                    </div>
                    <div className="text-[11.5px] font-semibold text-white/75">{n.barLabel}</div>
                  </div>

                  {/* OUTPUT */}
                  <div className="px-5 py-4"
                    style={{ borderTop: "1px solid rgba(255,255,255,0.10)" }}>
                    <div className="text-[10px] uppercase tracking-[0.24em] font-black text-white/60 mb-2.5">
                      Output
                    </div>
                    <div className="flex flex-col gap-2">
                      {n.outputs.map(out => (
                        <div key={out} className="flex items-center gap-2 text-[12.5px] font-medium text-white/90">
                          <span className="w-1.5 h-1.5 rounded-full shrink-0" style={{ background: n.color }} />
                          {out}
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Arrow between cards */}
                {i < 2 && (
                  <div className="shrink-0 self-center flex items-center justify-center" style={{ width: 44 }}>
                    <svg width="44" height="18" viewBox="0 0 44 18">
                      <line x1="0" y1="9" x2="33" y2="9"
                        stroke="rgba(255,255,255,0.38)"
                        strokeWidth="1.5"
                        strokeDasharray="3 2.5"
                        className="flow-line" />
                      <polygon points="44,9 32,4 32,14" fill="rgba(255,255,255,0.48)" />
                    </svg>
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Status row */}
          <div className="hidden md:flex items-center justify-between mt-5 px-1">
            <div className="flex items-center gap-2">
              <span className="live-dot w-1.5 h-1.5 rounded-full bg-green-400" />
              <span className="text-[11px] font-black uppercase tracking-[0.22em] text-white/75">
                All systems online
              </span>
            </div>
            <div className="flex items-center gap-5">
              {nodes.map(n => (
                <div key={n.id} className="flex items-center gap-1.5">
                  <span className="w-1.5 h-1.5 rounded-full" style={{ background: n.color, opacity: 0.85 }} />
                  <span className="text-[11px] font-mono font-semibold text-white/60">
                    <span style={{ color: n.color }}>{n.metric}</span>{" "}
                    {n.metricSub.split(" ")[0]}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </Reveal>

        {/* ── Mobile stack ── */}
        <Reveal delay={0.24}>
          <div className="flex flex-col gap-4 md:hidden">
            {nodes.map((n, i) => (
              <div key={n.id}>
                <div className="node-card rounded-xl overflow-hidden"
                  style={{
                    backgroundImage: n.bgImage,
                    backgroundSize: "100% 100%, 100% 100%",
                    border: `1.5px solid ${n.border}`,
                    boxShadow: `0 0 60px -16px ${n.glow}, 0 20px 60px -20px rgba(0,0,0,0.85)`,
                  }}>
                  <div className="p-5">
                    <div className="flex items-center justify-between mb-4">
                      <span className="text-[12px] font-black uppercase tracking-[0.18em] text-white">
                        {n.label}
                      </span>
                      <span className="flex items-center gap-1.5">
                        <span className="live-dot w-1.5 h-1.5 rounded-full bg-green-400" />
                        <span className="text-[10px] font-black uppercase tracking-[0.18em] text-green-300">live</span>
                      </span>
                    </div>

                    <div className="text-[3.75rem] font-black leading-none mb-0.5 text-white"
                      style={{ letterSpacing: "-0.045em" }}>
                      {n.metric}
                    </div>
                    <div className="text-[11.5px] font-bold uppercase tracking-[0.16em] text-white/75 mb-1.5">
                      {n.metricSub}
                    </div>
                    <div className="text-[10px] uppercase tracking-[0.14em] font-semibold text-white/60 mb-4">
                      Capacità del sistema
                    </div>

                    <div className="w-full h-1.5 rounded-full mb-1"
                      style={{ background: "rgba(255,255,255,0.14)" }}>
                      <div className="h-1.5 rounded-full"
                        style={{ width: `${n.bar}%`, background: "rgba(255,255,255,0.85)" }} />
                    </div>
                    <div className="text-[11.5px] font-semibold text-white/75 mb-4">{n.barLabel}</div>

                    <div className="flex flex-wrap gap-1.5">
                      {n.outputs.map(out => (
                        <span key={out}
                          className="text-[11px] font-semibold px-2.5 py-1 rounded-full text-white"
                          style={{ border: "1px solid rgba(255,255,255,0.32)", background: "rgba(255,255,255,0.14)" }}>
                          {out}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                {i < 2 && (
                  <div className="flex justify-center py-1.5">
                    <svg width="14" height="28" viewBox="0 0 14 28">
                      <line x1="7" y1="0" x2="7" y2="20"
                        stroke="rgba(255,255,255,0.35)" strokeWidth="1.5"
                        strokeDasharray="3 2" className="flow-line" />
                      <polygon points="7,28 2,18 12,18" fill="rgba(255,255,255,0.45)" />
                    </svg>
                  </div>
                )}
              </div>
            ))}
          </div>
        </Reveal>

        {/* ── CTAs ── */}
        <Reveal delay={0.36}>
          <div className="flex flex-col items-center gap-5 mt-14">
            {/* B6 — erano due CTA gemelle affiancate, stessa destinazione:
                nessuna gerarchia, quindi nessuna scelta. Ne resta una. */}
            <div className="flex items-center justify-center w-full sm:w-auto">
              <a href={BOOKING_URL} className="btn-orange group w-full sm:w-auto justify-center"
                style={{ padding: "1.1rem 2.5rem", fontSize: "1.05rem", fontWeight: 700 }}>
                Vediamo se ha senso lavorare insieme
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </a>
            </div>
            <div className="flex items-center gap-2 text-xs uppercase tracking-widest text-white/75"
              style={{ textShadow: "0 1px 6px rgba(0,0,0,0.9)" }}>
              <Shield className="h-3.5 w-3.5" /> Setup in 7 giorni · Zero canoni · Codice tuo per sempre
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
