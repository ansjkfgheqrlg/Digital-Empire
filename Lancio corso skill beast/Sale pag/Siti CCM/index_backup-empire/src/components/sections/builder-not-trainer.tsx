"use client";

import { Reveal } from "@/components/reveal";

const stats = [
  { n: "3+", l: "Anni full-AI" },
  { n: "50+", l: "Progetti spediti" },
  { n: "14", l: "System AI in produzione" },
  { n: "0", l: "Corsi rivenduti (finora)" },
];

export function BuilderNotTrainer() {
  return (
    <section className="bg-ink-2 section">
      <div className="max-w-6xl mx-auto px-6">
        <Reveal>
          <span className="bubble-orange mb-8">Chi ti forma</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2
            className="text-[40px] md:text-[64px] font-black leading-[1.02] tracking-tight mt-6 mb-16 max-w-4xl"
            style={{
              background:
                "linear-gradient(180deg, #ffffff 0%, #d9d6cf 40%, #fb4604 100%)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              backgroundClip: "text",
            }}
          >
            Max, founder di Digital Empire. Builder, non{" "}
            <span
              className="text-orange-pure"
              style={{
                fontFamily: "var(--font-serif), Georgia, serif",
                fontStyle: "italic",
                fontWeight: 400,
                WebkitTextFillColor: "#fb4604",
              }}
            >
              formatore.
            </span>
          </h2>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-10 md:gap-16 items-start">
          <div className="space-y-5 text-white/75 text-[16px] md:text-[17px] leading-relaxed">
            <Reveal delay={0.2}>
              <p>
                Ho passato gli ultimi 3 anni a costruire con l&apos;AI{" "}
                <strong className="text-silver-white">ogni singolo giorno</strong>: landing page, agenti, automazioni,
                skill custom, pipeline di ricerca, System AI interi. Oggi tutto questo vive sotto{" "}
                <strong>
                  Digital <span className="text-orange-pure">Empire</span>
                </strong>
                , la mia agenzia.
              </p>
            </Reveal>

            <Reveal delay={0.3}>
              <p>
                Dentro il corso c&apos;è <span className="text-orange-pure font-bold">solo me</span> — nessun sales,
                nessun junior, nessuno script registrato da uno che l&apos;AI l&apos;ha vista due volte. Ogni lezione
                nasce da un progetto reale che ho consegnato e che sto consegnando. Ogni framework l&apos;ho testato
                prima su clienti paganti, poi l&apos;ho messo nel corso.
              </p>
            </Reveal>

            <Reveal delay={0.4}>
              <p>
                Questo percorso esiste perché ogni settimana ci chiedono la stessa cosa:{" "}
                <em className="text-silver-white" style={{ fontFamily: "var(--font-serif), Georgia, serif" }}>
                  &ldquo;come fate a muovervi così veloce con l&apos;AI?&rdquo;
                </em>{" "}
                Ho deciso di smontare il metodo e metterlo a disposizione di chi vuole costruire davvero.
              </p>
            </Reveal>

            <Reveal delay={0.5}>
              <p className="text-silver-orange font-semibold">
                Non ti sto insegnando una teoria. Ti sto passando il manuale operativo che uso io, oggi, per pagare
                l&apos;affitto.
              </p>
            </Reveal>
          </div>

          <div className="grid grid-cols-2 gap-4 md:gap-5">
            {stats.map((s, i) => (
              <Reveal key={i} delay={0.25 + i * 0.08}>
                <div
                  className="relative rounded-2xl p-7 h-full overflow-hidden"
                  style={{
                    background:
                      "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                    border: "1px solid rgba(220,220,218,0.22)",
                    boxShadow:
                      "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                  }}
                >
                  <div
                    className="text-[44px] md:text-[54px] font-black leading-none mb-4"
                    style={{
                      background:
                        "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #fb4604 100%)",
                      WebkitBackgroundClip: "text",
                      WebkitTextFillColor: "transparent",
                      backgroundClip: "text",
                    }}
                  >
                    {s.n}
                  </div>
                  <div className="text-[11px] uppercase tracking-[0.22em] font-black text-white/55">
                    {s.l}
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
