"use client";

import { Reveal } from "@/components/reveal";

const tools = [
  { name: "Claude Code", desc: "Il core. Dove costruisci e refactorizzi progetti reali ogni giorno. Senza scrivere codice: dirigi, l'AI esegue." },
  { name: "Claude Chat", desc: "Per pensare ad alta voce, brainstorming, prompt crafting prima di passare in produzione su Claude Code." },
  { name: "Claude Projects", desc: "Dove metti contesto, documenti e istruzioni persistenti. Il cervello lungo dell'AI che ricorda il tuo stile." },
  { name: "Claude Cowork", desc: "Il nuovo spazio operativo: automazioni, azioni sul web, workflow auto-esecutivi. Il braccio che lavora mentre dormi." },
  { name: "Claude Agent SDK", desc: "Subagenti, skill, hooks, MCP. Il layer che trasforma Claude in un team orchestrato, non in una chat singola." },
  { name: "Perplexity", desc: "Ricerca vera, con fonti. Dove vai quando devi capire qualcosa o validare una nicchia prima di costruirla." },
  { name: "Manus", desc: "Agente autonomo che esegue task complessi end-to-end mentre fai altro. Lo integri nei tuoi flussi ibridi." },
  { name: "Cursor + VS Code", desc: "Quando e perché li alterni a Claude Code. E quando NON servono proprio — spoiler: più spesso di quanto credi." },
  { name: "Playwright", desc: "Per automazioni browser che funzionano al primo colpo — generate dall'AI. Web scraping, testing, flussi UI." },
  { name: "Memory & MCP", desc: "Come fai ricordare al modello ciò che conta tra una sessione e l'altra. La memoria persistente è un superpotere." },
  { name: "ElevenLabs", desc: "Voice cloning e TTS professionale per dare voce ai tuoi agenti, podcast AI e contenuti auto-generati." },
  { name: "n8n · Make", desc: "Orchestrazione no-code per connettere i System AI ai tuoi tool: CRM, email, Notion, Airtable, Slack, Stripe." },
];

export function ToolStack() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <div className="max-w-6xl mx-auto px-6 relative">
        <Reveal>
          <span className="bubble-orange mb-8">Lo stack che vedrai dentro</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2
            className="text-[40px] md:text-[64px] font-black leading-[1.02] tracking-tight mt-6 mb-6 max-w-4xl"
            style={{
              background:
                "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #8a8378 100%)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              backgroundClip: "text",
            }}
          >
            Niente tool segreti. <br />
            Solo quelli{" "}
            <span
              className="text-orange-pure"
              style={{
                fontFamily: "var(--font-serif), Georgia, serif",
                fontStyle: "italic",
                fontWeight: 400,
                WebkitTextFillColor: "#fb4604",
              }}
            >
              che uso davvero.
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="text-white/65 text-lg max-w-3xl leading-relaxed mb-14">
            Ti mostro lo stack esatto che apro ogni mattina. Niente affiliate link, niente &ldquo;segreti&rdquo; a
            pagamento, niente tool esotici che non usi mai. Solo roba che funziona, usata nel mio flusso reale — e che
            ti farò vedere in azione, lezione dopo lezione.
          </p>
        </Reveal>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-5">
          {tools.map((t, i) => (
            <Reveal key={i} delay={0.1 + (i % 6) * 0.06}>
              <div
                className="relative rounded-2xl p-6 h-full overflow-hidden transition-transform duration-500 hover:-translate-y-1.5"
                style={{
                  background:
                    "linear-gradient(135deg, #e9e3da 0%, #d8cfc2 35%, #fb4604 100%)",
                  border: "1px solid rgba(251,70,4,0.35)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.55), 0 14px 40px -18px rgba(251,70,4,0.45), 0 0 0 1px rgba(255,255,255,0.2)",
                }}
              >
                <div
                  aria-hidden="true"
                  className="pointer-events-none absolute inset-0 rounded-2xl"
                  style={{
                    background:
                      "radial-gradient(circle at 85% 90%, rgba(251,70,4,0.6) 0%, transparent 55%)",
                    mixBlendMode: "soft-light",
                  }}
                />
                <h3 className="relative text-[18px] md:text-[20px] font-black text-[#1c1c1c] mb-3 tracking-tight">
                  {t.name}
                </h3>
                <p className="relative text-[13px] md:text-[14px] leading-relaxed text-[#2a2a2a]">
                  {t.desc}
                </p>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.5}>
          <p className="mt-14 text-center text-[12px] uppercase tracking-[0.25em] font-black text-white/50">
            <span className="text-orange-pure">→</span> Tutto lo stack coperto dentro i 9 moduli · Nessun tool venduto separatamente
          </p>
        </Reveal>
      </div>
    </section>
  );
}
