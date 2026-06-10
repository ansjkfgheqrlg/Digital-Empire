"use client";

import { Reveal } from "@/components/reveal";
import { FileCode2, Library, Bot, Workflow, ClipboardCheck, Puzzle } from "lucide-react";

const assets = [
  {
    icon: FileCode2,
    tag: "Template Vault",
    t: "18 System Prompt pronti",
    d: "I System Prompt che uso io, oggi, sui progetti paganti. Copi, incolli, personalizzi 3 variabili. Parti già a 80% del lavoro.",
  },
  {
    icon: Library,
    tag: "Skill Library",
    t: "Libreria di Skill verticali",
    d: "30+ Skill custom divise per dominio (ricerca, scrittura, analisi, ops). Richiamabili on-demand dai tuoi Agenti.",
  },
  {
    icon: Bot,
    tag: "Agent Blueprints",
    t: "12 Agenti già orchestrati",
    d: "Blueprint completi di Agenti mono- e multi-step. Architettura, prompt, tool, handoff. Deploy in 15 minuti.",
  },
  {
    icon: Workflow,
    tag: "Workflow Pack",
    t: "Pipeline multi-step",
    d: "Flussi end-to-end per casi reali: lead research, content engine, client onboarding, reporting. Pronti da clonare.",
  },
  {
    icon: Puzzle,
    tag: "MCP Toolkit",
    t: "Setup MCP + Memory",
    d: "Configurazioni esatte per collegare Claude Code ai tuoi tool (GDrive, Notion, Gmail, DB). Niente tentativi, solo replica.",
  },
  {
    icon: ClipboardCheck,
    tag: "Operator Checklists",
    t: "Checklist operative",
    d: "Liste di controllo per ogni fase: dalla validazione M.A.P. alla consegna. Zero passaggi dimenticati, zero rework.",
  },
];

export function PowerDeck() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.10) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-6xl mx-auto px-6 relative">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Asset Vault // Tutto incluso</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6">
              <span className="text-silver-white">Non solo video. </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  letterSpacing: "-0.01em",
                }}
              >
                Un arsenale operativo.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/65 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Ogni modulo spedisce <strong className="text-silver-orange">asset reali</strong> che puoi clonare nel tuo
              business oggi stesso. Niente concetti teorici: file, prompt, blueprint, checklist.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5">
          {assets.map((a, i) => {
            const Icon = a.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.06} variant="scale">
                <div
                  className="relative rounded-2xl p-6 h-full overflow-hidden hover-lift"
                  style={{
                    background:
                      "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                    border: "1px solid rgba(220,220,218,0.22)",
                    boxShadow:
                      "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                  }}
                >
                  <div
                    aria-hidden="true"
                    className="pointer-events-none absolute inset-0 rounded-2xl"
                    style={{
                      background:
                        "linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 40%, transparent 70%, rgba(251,70,4,0.08) 100%)",
                    }}
                  />
                  <div className="relative">
                    <div className="flex items-center gap-3 mb-5">
                      <div
                        className="w-11 h-11 rounded-xl flex items-center justify-center shrink-0"
                        style={{
                          background:
                            "radial-gradient(circle at 30% 30%, rgba(251,70,4,0.5), rgba(251,70,4,0.15) 60%, rgba(255,240,225,0.08) 90%)",
                          border: "1px solid rgba(251,70,4,0.5)",
                          boxShadow: "0 0 20px -6px rgba(251,70,4,0.5), inset 0 1px 0 rgba(255,255,255,0.2)",
                        }}
                      >
                        <Icon className="h-5 w-5 text-white" strokeWidth={1.8} />
                      </div>
                      <span className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure">
                        {a.tag}
                      </span>
                    </div>
                    <h3 className="text-[18px] md:text-[20px] font-black text-silver-white mb-3 leading-tight">
                      {a.t}
                    </h3>
                    <p className="text-[13.5px] text-white/70 leading-relaxed">{a.d}</p>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>

        <Reveal delay={0.5}>
          <p className="text-center text-white/55 text-sm max-w-2xl mx-auto mt-12 leading-relaxed">
            <span className="text-orange-pure">→</span> Tutti gli asset si aggiornano quando aggiorno i miei.{" "}
            <span className="text-silver-orange font-semibold">Accesso a vita, incluso.</span>
          </p>
        </Reveal>
      </div>
    </section>
  );
}
