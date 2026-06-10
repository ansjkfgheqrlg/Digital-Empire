"use client";

import { Reveal } from "@/components/reveal";

export function MyPromise() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 20%, rgba(251,70,4,0.1) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-5xl mx-auto px-6 relative text-center">
        <Reveal>
          <span className="bubble-orange mb-10">La mia promessa</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2
            className="text-[34px] md:text-[58px] font-black leading-[1.1] tracking-tight mt-8 mb-10"
            style={{ letterSpacing: "-0.02em" }}
          >
            <span className="flex flex-wrap justify-center gap-x-[0.28em] gap-y-1">
              {[
                { w: "Se", o: false },
                { w: "nei", o: false },
                { w: "primi", o: false },
                { w: "3", o: false },
                { w: "moduli", o: false },
                { w: "non", o: false },
                { w: "ti", o: false },
                { w: "sto", o: false },
                { w: "dando", o: false },
                { w: "valore,", o: true },
                { w: "ti", o: true },
                { w: "rimborso.", o: true, serif: true },
              ].map(({ w, o, serif }, i) => (
                <span
                  key={i}
                  style={{
                    background: o
                      ? "linear-gradient(180deg, #ffd7b8 0%, #fb4604 55%, #8f2a02 100%)"
                      : "linear-gradient(180deg, #ffffff 0%, #e4dfd6 45%, #8a8378 100%)",
                    WebkitBackgroundClip: "text",
                    WebkitTextFillColor: "transparent",
                    backgroundClip: "text",
                    fontStyle: serif ? "italic" : "normal",
                    fontFamily: serif ? "var(--font-serif), Georgia, serif" : undefined,
                    fontWeight: serif ? 500 : 900,
                  }}
                >
                  {w}
                </span>
              ))}
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.2}>
          <div className="space-y-4 text-white/75 text-lg leading-relaxed max-w-2xl mx-auto">
            <p>
              Senza giustificazioni. Senza <em>&ldquo;dammi altri 5 giorni&rdquo;</em>.<br />
              Senza questionari da 20 domande per &ldquo;capire perché&rdquo;.
            </p>
            <p>
              Apri i primi 3 moduli, fai gli esercizi, metti le mani in pasta. Se non senti che stai diventando un
              System Architect, scrivi una mail.{" "}
              <strong className="text-silver-white">Rimborso integrale entro 48 ore.</strong>
            </p>
            <p className="text-[#ffb488]/80 text-[15px]">
              Finora, su tutti i Builder che hanno iniziato, zero hanno chiesto indietro i soldi. Ma il diritto di
              farlo ce l&apos;hai, sempre.
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.35}>
          <p
            className="mt-12 text-2xl md:text-3xl font-black text-silver-white"
            style={{ letterSpacing: "-0.01em" }}
          >
            Il rischio è <span className="text-orange-pure">tutto mio.</span>
          </p>
        </Reveal>

        <Reveal delay={0.45}>
          <p className="mt-4 text-[12px] uppercase tracking-[0.28em] font-black text-white/45">
            → 30 giorni · Builder o Rimborsato · Nessuna domanda
          </p>
        </Reveal>
      </div>
    </section>
  );
}
