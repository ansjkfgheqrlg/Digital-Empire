"use client";

import { Reveal } from "@/components/reveal";

const tools = [
  { name: "Claude AI", desc: "Il cervello del sistema. Qualifica lead in ingresso, genera copy APSOC personalizzato, risponde alla knowledge base in tempo reale." },
  { name: "Gmail API", desc: "Il motore dell'Outreach Factory: 300+ email personalizzate al giorno, warm-up graduale, zero spam, massima deliverability." },
  { name: "Playwright", desc: "Automazione browser per l'outreach Instagram: simula comportamento umano con timing randomizzato. Zero ban, zero rischio account." },
  { name: "Proxy Residenziali", desc: "IP dedicati per blindare ogni account Instagram. Ogni profilo ha il suo proxy residenziale. Il sistema è invisibile alle detection." },
  { name: "APSOC Framework", desc: "Il framework copy proprietario che l'AI usa per scrivere ogni messaggio, caption e script. Calibrato sul tuo ICP e brand voice." },
  { name: "n8n", desc: "Il tessuto connettivo. Orchestra ogni flusso automatico: dalla qualificazione lead alla notifica Slack, dall'upload Drive alla risposta CRM." },
  { name: "OpenAI API", desc: "Generazione contenuti ad alto volume per la Content Factory: caroselli, script Reels, caption. Costi API minimi a consumo." },
  { name: "Supabase", desc: "Database real-time per lead, status conversazioni e metriche. La dashboard web custom legge da qui in tempo reale." },
  { name: "Google Drive", desc: "Storage organizzato per la Content Factory. Ogni output — caroselli, script, grafiche — viene uploadato automaticamente per argomento e data." },
  { name: "Slack / CRM", desc: "Notifiche istantanee quando l'AI identifica un lead caldo. Il tuo team riceve il profilo qualificato direttamente dove lavora." },
  { name: "React / Next.js", desc: "Le dashboard web custom che ti diamo. Interfaccia per monitorare lead, configurare brief contenuti, scaricare output in 30 secondi." },
  { name: "Obsidian / Notion", desc: "Il layer di accesso al Second Brain. L'AI indicizza tutto e risponde a qualsiasi domanda sulla tua knowledge base aziendale." },
];

export function ToolStack() {
  return (
    <section className="bg-ink section section-border-t relative overflow-hidden">
      <div className="max-w-6xl mx-auto px-6 relative">
        <Reveal>
          <span className="bubble-orange mb-8">Lo stack tecnico del sistema</span>
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
            Niente black box. <br />
            Ogni tool{" "}
            <span
              className="text-orange-pure"
              style={{
                fontFamily: "var(--font-serif), Georgia, serif",
                fontStyle: "italic",
                fontWeight: 400,
                WebkitTextFillColor: "#fb4604",
              }}
            >
              spiegato e consegnato.
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="text-white/90 text-lg max-w-3xl leading-relaxed mb-14">
            Ti mostriamo lo stack esatto che gira dentro ogni sistema AI che installiamo. Nessun componente nascosto,
            nessun vendor lock-in. Hai il codice sorgente di tutto —{" "}
            <span className="text-silver-orange font-semibold">puoi vedere, modificare e gestire ogni pezzo.</span>
          </p>
        </Reveal>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-5">
          {tools.map((t, i) => (
            <Reveal key={i} delay={0.1 + (i % 6) * 0.06}>
              {/* B3 — erano 12 card a gradiente arancione con testo nero su sezione scura:
                  il contrasto peggiore della pagina e 12 rettangoli che gridano insieme.
                  Griglia sobria, nome in monospaziato (D4): l'etichetta tecnica dice
                  "qui si misura" senza doverlo scrivere. */}
              <div
                className="relative rounded-xl p-6 h-full transition-colors duration-300"
                style={{
                  background: "rgba(249,249,249,0.035)",
                  border: "1px solid rgba(249,249,249,0.10)",
                }}
              >
                <h3
                  className="relative text-[13px] font-bold text-orange-pure mb-3 uppercase tracking-[0.12em]"
                  style={{ fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace" }}
                >
                  {t.name}
                </h3>
                <p className="relative text-[14px] leading-relaxed text-white/60">
                  {t.desc}
                </p>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.5}>
          <p className="mt-14 text-center text-[12px] uppercase tracking-[0.22em] font-black text-white/75">
            <span className="text-orange-pure">→</span> Tutto lo stack è tuo · Codice sorgente consegnato a setup completato
          </p>
        </Reveal>
      </div>
    </section>
  );
}
