"use client";

import { Reveal } from "@/components/reveal";

/* ─────────────────────────────────────────────────────────
   Stack — Strumenti che usiamo ogni giorno
   Adattato dal pattern CCM tool-stack con colori brand navy/cream
   Gradient card: silver/bianco → electric blue (al posto di silver → orange)
   ───────────────────────────────────────────────────────── */

const TOOLS = [
  {
    name: "Make (Integromat)",
    desc: "Il centro di orchestrazione. Connette tutti i tool e scatena i workflow automaticamente. Zero codice, massima potenza.",
  },
  {
    name: "n8n",
    desc: "Per workflow complessi con logica avanzata. Eseguito su server dedicato, flessibilità totale su ogni automazione.",
  },
  {
    name: "Clay",
    desc: "Enrichment dei lead su ogni livello — email, LinkedIn, dati aziendali, intent signals. Il CRM intelligente.",
  },
  {
    name: "Apollo.io",
    desc: "Database di 275M+ contatti business. Trova il tuo ICP in secondi, esporta e lancia in automatico.",
  },
  {
    name: "Claude AI",
    desc: "Il cervello del sistema. Personalizzazione email, generazione contenuti, analisi, copy — tutto orchestrato in modo deterministico.",
  },
  {
    name: "Instantly",
    desc: "Outreach email ad alto volume con deliverability premium. Warmup automatico, sending intelligente, report in tempo reale.",
  },
  {
    name: "HeyReach",
    desc: "Automazione LinkedIn multi-account. Connessioni, messaggi, follow-up — tutto mentre lavori ad altro.",
  },
  {
    name: "Airtable",
    desc: "Il database operativo. Ogni lead, ogni task, ogni contenuto gestito in tempo reale e sincronizzato con tutti i flussi.",
  },
  {
    name: "Notion",
    desc: "Gestione processi, SOP, documentazione. Il manuale operativo del workflow AI sempre aggiornato e consultabile.",
  },
  {
    name: "PhantomBuster",
    desc: "Automazioni web e scraping avanzato. Estrae dati da LinkedIn, siti web — pronto per Clay e il CRM.",
  },
  {
    name: "Buffer / Later",
    desc: "Scheduling e pubblicazione social multi-canale. Il Content Workflow pubblica H24 senza alcun intervento manuale.",
  },
  {
    name: "ElevenLabs",
    desc: "Voice cloning e TTS professionale per contenuti audio-video automatizzati e personalizzati su scala.",
  },
];

export function Stack() {
  return (
    <section
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="stack-h2"
    >
      {/* Ambient glow */}
      <div
        aria-hidden
        className="pointer-events-none absolute z-0"
        style={{
          width: 700,
          height: 500,
          right: "5%",
          top: "20%",
          background:
            "radial-gradient(ellipse, rgba(251,70,4,0.08) 0%, transparent 70%)",
          filter: "blur(80px)",
        }}
      />

      <div className="container-wide relative z-[1]">
        <Reveal>
          <span className="bubble-gold">
            <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
            Il nostro stack · Nessun segreto
          </span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2 id="stack-h2" className="mt-6 max-w-4xl">
            <span className="text-silver-white">Nessun tool segreto.</span>{" "}
            <span className="text-silver-gold font-accent italic">
              Solo quelli che usiamo ogni giorno.
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="mt-5 text-white/65 text-[1.05rem] max-w-3xl leading-relaxed mb-14 font-light">
            Ti mostriamo lo stack esatto che apriamo ogni mattina. Niente tool di moda pagati a
            commissione, niente soluzioni esotiche inutili. Solo quello che funziona, testato su
            decine di workflow reali.
          </p>
        </Reveal>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {TOOLS.map((t, i) => (
            <Reveal key={i} delay={0.08 + (i % 6) * 0.05}>
              <div
                className="relative rounded-2xl p-6 h-full overflow-hidden"
                style={{
                  /* Gradiente silver/cream → orange: ricetta CCM esatta */
                  background:
                    "linear-gradient(135deg, #fff0e8 0%, #f5d5c0 28%, #e8a070 58%, #fb4604 82%, #c93a0a 100%)",
                  border: "1px solid rgba(251,70,4,0.30)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.55), 0 14px 40px -18px rgba(201,55,10,0.35), 0 0 0 1px rgba(255,255,255,0.12)",
                  transition: "transform 0.45s cubic-bezier(0.22,1,0.36,1), box-shadow 0.45s",
                }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLElement).style.transform = "translateY(-4px)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLElement).style.transform = "translateY(0)";
                }}
              >
                {/* Radial glow navy in basso a destra (come CCM ma navy) */}
                <div
                  aria-hidden
                  className="pointer-events-none absolute inset-0 rounded-2xl"
                  style={{
                    background:
                      "radial-gradient(circle at 85% 88%, rgba(201,55,10,0.35) 0%, transparent 55%)",
                    mixBlendMode: "soft-light",
                  }}
                />
                <h3
                  className="relative font-black mb-2 tracking-tight"
                  style={{
                    fontSize: "clamp(0.88rem, 1.5vw, 0.98rem)",
                    color: "#1c1c1c",
                  }}
                >
                  {t.name}
                </h3>
                <p
                  className="relative leading-relaxed"
                  style={{
                    fontSize: "clamp(0.75rem, 1.2vw, 0.82rem)",
                    color: "rgba(10,10,10,0.82)",
                  }}
                >
                  {t.desc}
                </p>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.5}>
          <p
            className="mt-14 text-center uppercase font-black text-white/40"
            style={{ fontSize: "11px", letterSpacing: "0.25em" }}
          >
            <span className="text-gold-pure">→</span> Stack completamente gestito da noi{" "}
            <span className="text-white/25">·</span> Zero setup tecnico per il cliente
          </p>
        </Reveal>
      </div>
    </section>
  );
}
