"use client";

import { Reveal } from "@/components/reveal";
import { motion, useInView } from "framer-motion";
import { useRef } from "react";
import { Inbox, Cpu, Zap } from "lucide-react";

const STAGES = [
  {
    icon: Inbox,
    label: "STEP 01 · INPUT",
    title: "Lead Source",
    body:
      "Il sistema identifica automaticamente i prospect dalla tua audience target: LinkedIn, database, social, liste. Nessuna ricerca manuale.",
  },
  {
    icon: Cpu,
    label: "STEP 02 · ELABORAZIONE AI",
    title: "AI Engine",
    body:
      "L'AI qualifica ogni lead, personalizza il messaggio, gestisce il timing dei follow-up e adatta il tono in base alle risposte ricevute.",
  },
  {
    icon: Zap,
    label: "STEP 03 · OUTPUT",
    title: "Tu ricevi solo i caldi",
    body:
      "Arrivano solo i lead che hanno risposto positivamente. Nessun lead freddo, nessun tempo perso. Tu fai solo le call che contano.",
  },
];

function WorkflowSvg() {
  const ref = useRef<SVGSVGElement>(null);
  const inView = useInView(ref, { once: true, amount: 0.4 });

  return (
    <svg
      ref={ref}
      viewBox="0 0 320 360"
      className="w-full max-w-[320px] mx-auto block"
      aria-hidden
    >
      <defs>
        <linearGradient id="flowGold" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="#fb4604" stopOpacity="0.35" />
          <stop offset="50%" stopColor="#ff6a2e" stopOpacity="0.50" />
          <stop offset="100%" stopColor="#c93a0a" stopOpacity="0.70" />
        </linearGradient>
        <linearGradient id="flowStroke" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stopColor="#fb4604" />
          <stop offset="100%" stopColor="#ff6a2e" />
        </linearGradient>
      </defs>

      {/* Vertical pipeline */}
      <motion.rect
        x="140"
        y="20"
        width="40"
        height="320"
        rx="20"
        fill="url(#flowGold)"
        stroke="url(#flowStroke)"
        strokeWidth="1.5"
        initial={{ scaleY: 0, opacity: 0 }}
        animate={inView ? { scaleY: 1, opacity: 1 } : {}}
        style={{ originY: "0%" }}
        transition={{ duration: 1.4, ease: [0.22, 1, 0.36, 1] }}
      />

      {/* Node dots */}
      {[60, 180, 300].map((cy, i) => (
        <motion.circle
          key={i}
          cx="160"
          cy={cy}
          r="10"
          fill="#fb4604"
          initial={{ scale: 0, opacity: 0 }}
          animate={inView ? { scale: 1, opacity: 1 } : {}}
          transition={{ duration: 0.4, delay: 0.8 + i * 0.3 }}
        />
      ))}

      {/* Flowing particles */}
      {[0, 1, 2, 3].map((i) => (
        <motion.circle
          key={i}
          cx={160}
          cy={20}
          r={3}
          fill="#fb4604"
          initial={{ cy: 20, opacity: 0 }}
          animate={
            inView
              ? {
                  cy: [20, 340],
                  opacity: [0, 0.9, 0],
                }
              : {}
          }
          transition={{
            duration: 2.2,
            delay: 1.2 + i * 0.5,
            repeat: Infinity,
            ease: "easeIn",
          }}
        />
      ))}

      <text x="160" y="14" textAnchor="middle" fill="#fb4604" opacity="0.5" fontSize="8" fontWeight="600" letterSpacing="2">
        INPUT
      </text>
      <text x="160" y="348" textAnchor="middle" fill="#fb4604" opacity="0.9" fontSize="10" fontWeight="700" letterSpacing="2">
        ★ LEAD CALDI
      </text>
    </svg>
  );
}

export function FunnelViz() {
  return (
    <section
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="funnel-h2"
    >
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-silver">
              <span
                className="w-1.5 h-1.5 rounded-full bg-gold-pure"
                style={{ boxShadow: "0 0 8px rgba(251,70,4,0.7)" }}
              />
              Come funziona
            </span>
            <h2 id="funnel-h2" className="mt-6">
              <span className="text-silver-white">Un workflow è una pipeline</span>{" "}
              <span className="text-silver-gold font-accent italic">
                intelligente.
              </span>
            </h2>
            <p className="mt-5 text-[1.05rem] text-white/90 leading-relaxed font-light">
              Dal lead grezzo al cliente pronto alla call: ogni step è
              automatico, personalizzato e tracciato. Tu intervieni solo
              dove conta davvero.
            </p>
          </div>
        </Reveal>

        <div className="grid lg:grid-cols-3 gap-8 lg:gap-10 items-center max-w-6xl mx-auto">
          {/* LEFT — stages 1+2 */}
          <div className="flex flex-col gap-5 order-2 lg:order-1">
            {STAGES.slice(0, 2).map((s, i) => {
              const Icon = s.icon;
              return (
                <Reveal key={i} delay={0.20 + i * 0.10}>
                  <div className="card-dark !p-6">
                    <div className="flex items-center gap-3 mb-3">
                      <span
                        className="grid place-items-center w-9 h-9 rounded-lg"
                        style={{
                          background: "rgba(251,70,4,0.08)",
                          border: "1px solid rgba(251,70,4,0.18)",
                        }}
                      >
                        <Icon className="h-4 w-4 text-gold-pure" />
                      </span>
                      <span className="text-[0.65rem] uppercase tracking-[0.20em] font-semibold text-white/40">
                        {s.label}
                      </span>
                    </div>
                    <h4 className="text-[1.125rem] font-bold text-white mb-2">
                      {s.title}
                    </h4>
                    <p className="text-[0.88rem] leading-relaxed text-white/85 font-light">
                      {s.body}
                    </p>
                  </div>
                </Reveal>
              );
            })}
          </div>

          {/* CENTER — workflow SVG */}
          <Reveal delay={0.30} className="order-1 lg:order-2">
            <div className="relative">
              <div
                className="glow-gold-amb"
                style={{
                  width: 320,
                  height: 320,
                  left: "50%",
                  top: "50%",
                  transform: "translate(-50%, -50%)",
                  opacity: 0.18,
                }}
                aria-hidden
              />
              <WorkflowSvg />
            </div>
          </Reveal>

          {/* RIGHT — stage 3 */}
          <div className="order-3">
            <Reveal delay={0.40}>
              <div className="card-gold !p-6">
                <div className="flex items-center gap-3 mb-3">
                  <span
                    className="grid place-items-center w-9 h-9 rounded-lg"
                    style={{
                      background:
                        "linear-gradient(135deg, #fb4604 0%, #c93a0a 100%)",
                    }}
                  >
                    <Zap className="h-4 w-4 text-gold-pure" />
                  </span>
                  <span className="text-[0.65rem] uppercase tracking-[0.20em] font-semibold text-[#0a0a0a]/65">
                    {STAGES[2].label}
                  </span>
                </div>
                <h4 className="text-[1.125rem] font-bold text-[#0a0a0a] mb-2">
                  {STAGES[2].title}
                </h4>
                <p className="text-[0.88rem] leading-relaxed text-[#0a0a0a]/75 font-light">
                  {STAGES[2].body}
                </p>
              </div>
            </Reveal>
          </div>
        </div>
      </div>
    </section>
  );
}
