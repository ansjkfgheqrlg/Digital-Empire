"use client";

import { Reveal } from "@/components/reveal";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.96 0 0 0 0 0.95 0 0 0 0 0.94 0 0 0 0.28 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const steps = [
  {
    t: "Chiamata Strategica",
    d: "Analizziamo dove perdi più tempo e quale sistema risolve il tuo collo di bottiglia principale.",
    note: "30 minuti. Nessun impegno.",
    side: "right",
    seed: "7",
    accent: "#c41818",
    border: "rgba(220, 180, 180, 0.58)",
    glow: "rgba(160, 20, 20, 0.30)",
    bgLayers: [
      "radial-gradient(75% 55% at 6% 8%, rgba(255,255,255,0.42) 0%, transparent 50%)",
      "radial-gradient(50% 40% at 92% 88%, rgba(200,160,160,0.20) 0%, transparent 45%)",
      "linear-gradient(145deg, #2a0606 0%, #520e0e 22%, #881a1a 48%, #6a1010 72%, #1e0404 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(255,60,60,0.38) 0%, rgba(180,20,20,0.55) 100%)",
    badgeBorder: "rgba(255,80,80,0.52)",
    numColor: "#ff8888",
  },
  {
    t: "Proposta Tecnica",
    d: "Entro 24 ore ricevi una proposta personalizzata con lo stack esatto, i tempi e l'investimento.",
    note: "Massima trasparenza. Zero sorprese.",
    side: "left",
    seed: "11",
    accent: "#b84400",
    border: "rgba(220, 195, 170, 0.58)",
    glow: "rgba(160, 70, 0, 0.30)",
    bgLayers: [
      "radial-gradient(75% 55% at 6% 8%, rgba(255,255,255,0.44) 0%, transparent 50%)",
      "radial-gradient(50% 40% at 92% 88%, rgba(200,170,130,0.20) 0%, transparent 45%)",
      "linear-gradient(145deg, #2a1000 0%, #561e00 22%, #904000 48%, #6e2c00 72%, #200e00 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(251,100,4,0.38) 0%, rgba(180,60,0,0.55) 100%)",
    badgeBorder: "rgba(251,100,4,0.52)",
    numColor: "#ffaa70",
  },
  {
    t: "Setup & Installazione",
    d: "Installiamo il sistema sui tuoi server, configuriamo proxy, account e dashboard. Tutto testato.",
    note: "7 giorni. Poi è in produzione.",
    side: "right",
    seed: "4",
    accent: "#1a7a38",
    border: "rgba(170, 210, 180, 0.58)",
    glow: "rgba(10, 100, 40, 0.30)",
    bgLayers: [
      "radial-gradient(75% 55% at 6% 8%, rgba(255,255,255,0.38) 0%, transparent 50%)",
      "radial-gradient(50% 40% at 92% 88%, rgba(140,200,160,0.18) 0%, transparent 45%)",
      "linear-gradient(145deg, #031408 0%, #0a2e12 22%, #145a24 48%, #0e3e18 72%, #020e06 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(40,180,80,0.35) 0%, rgba(10,100,40,0.55) 100%)",
    badgeBorder: "rgba(50,200,90,0.50)",
    numColor: "#80ee99",
  },
  {
    t: "Calibrazione & Go-Live",
    d: "Addestriamo il sistema sul tuo brand e ICP. Formazione sulla dashboard inclusa — poi è tuo e gira da solo.",
    note: "Formazione inclusa. Sistema tuo.",
    side: "left",
    seed: "2",
    accent: "#1a44b0",
    border: "rgba(170, 190, 230, 0.58)",
    glow: "rgba(10, 40, 160, 0.30)",
    bgLayers: [
      "radial-gradient(75% 55% at 6% 8%, rgba(255,255,255,0.36) 0%, transparent 50%)",
      "radial-gradient(50% 40% at 92% 88%, rgba(130,160,220,0.18) 0%, transparent 45%)",
      "linear-gradient(145deg, #030818 0%, #0a1640 22%, #163080 48%, #0e2260 72%, #020610 100%)",
    ],
    badgeBg: "linear-gradient(135deg, rgba(60,120,255,0.35) 0%, rgba(10,50,180,0.55) 100%)",
    badgeBorder: "rgba(80,140,255,0.50)",
    numColor: "#90bbff",
  },
];

export function Roadmap() {
  return (
    <section className="bg-paper section section-border-t">
      <style>{`
        .rm-card {
          transition: transform 0.4s cubic-bezier(0.22,1,0.36,1), box-shadow 0.4s ease;
        }
        .rm-card:hover {
          transform: translateY(-4px) scale(1.006);
        }
      `}</style>

      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Come funziona</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              Dal primo contatto<br />
              <span className="text-orange-pure italic font-medium">al sistema in produzione.</span>
            </h2>
          </Reveal>
        </div>

        <div className="space-y-4">
          {steps.map((w, i) => (
            <Reveal key={i} delay={0.15 + i * 0.07}>
              <div className="relative">
                <div
                  className="rm-card flex gap-5 items-center rounded-2xl px-6 py-5"
                  style={{
                    backgroundImage: [GRAIN(w.seed), ...w.bgLayers].join(", "),
                    backgroundSize: "200px 200px, 100% 100%, 100% 100%, 100% 100%",
                    backgroundBlendMode: "screen, normal, normal, normal",
                    border: `1.5px solid ${w.border}`,
                    boxShadow: [
                      `0 0 40px -16px ${w.glow}`,
                      "0 12px 32px -12px rgba(0,0,0,0.40)",
                      "0 2px 0 rgba(255,255,255,0.30) inset",
                      "0 -1px 0 rgba(0,0,0,0.35) inset",
                      "0 0 0 1px rgba(255,255,255,0.08) inset",
                    ].join(", "),
                  }}
                >
                  {/* Step number badge */}
                  <span
                    className="shrink-0 grid place-items-center w-11 h-11 rounded-xl text-lg font-black"
                    style={{
                      background: w.badgeBg,
                      border: `1px solid ${w.badgeBorder}`,
                      boxShadow: `0 4px 16px ${w.glow}, inset 0 1px 0 rgba(255,255,255,0.22)`,
                      color: w.numColor,
                      letterSpacing: "-0.02em",
                      minWidth: 44,
                    }}
                  >
                    {i + 1}
                  </span>

                  <div>
                    <h3 className="text-[1.15rem] md:text-[1.35rem] font-bold leading-tight mb-1"
                      style={{ color: "#ffffff", textShadow: "0 1px 8px rgba(0,0,0,0.60)" }}>
                      Step {i + 1}: {w.t}
                    </h3>
                    <p className="text-[0.93rem] leading-relaxed"
                      style={{ color: "rgba(255,255,255,0.80)" }}>
                      {w.d}
                    </p>
                  </div>
                </div>

                {/* Side annotation */}
                <div
                  aria-hidden="true"
                  className="hidden xl:flex pointer-events-none items-center gap-2"
                  style={{
                    position: "absolute",
                    top: "50%",
                    transform: "translateY(-50%)",
                    [w.side === "right" ? "left" : "right"]: "calc(100% + 28px)",
                    width: "220px",
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 700,
                    fontSize: "16px",
                    lineHeight: 1.35,
                    color: w.accent,
                    letterSpacing: "-0.005em",
                    justifyContent: w.side === "right" ? "flex-start" : "flex-end",
                    textAlign: w.side === "right" ? "left" : "right",
                    opacity: 1,
                  } as React.CSSProperties}
                >
                  {w.side === "right" && <span style={{ color: w.accent, marginRight: 6, opacity: 0.9 }}>→</span>}
                  <span>{w.note}</span>
                  {w.side === "left" && <span style={{ color: w.accent, marginLeft: 6, opacity: 0.9 }}>←</span>}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
