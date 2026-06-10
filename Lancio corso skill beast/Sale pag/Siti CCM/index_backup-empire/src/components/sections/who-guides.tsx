"use client";

import { Reveal } from "@/components/reveal";

export function WhoGuides() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 20% 30%, rgba(251,70,4,0.08) 0%, transparent 50%)",
        }}
      />
      <div className="max-w-4xl mx-auto px-6 relative">
        <Reveal>
          <span className="bubble-orange mb-8">Chi ti guida</span>
        </Reveal>

        <Reveal delay={0.1}>
          <h2
            className="text-[44px] md:text-[72px] font-black leading-[1] tracking-tight mt-6 mb-12"
            style={{
              background:
                "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #8a8378 100%)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              backgroundClip: "text",
            }}
          >
            &ldquo;Ok ma tu chi sei?&rdquo;
          </h2>
        </Reveal>

        <div className="space-y-6 text-white/75 text-lg leading-relaxed max-w-3xl">
          <Reveal delay={0.2}>
            <p>
              Dentro il corso ci vediamo io, <span className="text-orange-pure font-bold">Max</span> — founder di{" "}
              <strong className="text-silver-white">Digital Empire</strong>, agenzia che costruisce prodotti, landing
              page, automazioni e System AI completi per clienti reali.
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <p>
              Da marzo 2025 ho buttato tutti gli altri tool e lavoro solo nell&apos;ecosistema Claude. Abbiamo spedito{" "}
              <span
                className="inline-block px-2 py-0.5 rounded font-black"
                style={{ background: "#fb4604", color: "#fff" }}
              >
                50+ progetti
              </span>{" "}
              reali in questi mesi usando Claude Code come unica IDE, Claude Projects come cervello lungo, Cowork e
              Perplexity come bracci operativi.
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <p>
              <strong className="text-silver-white">Digital Empire non è un guru-brand.</strong> Non c&apos;è un corso
              da $999 venduto a ripetizione, non c&apos;è una pipeline di upsell infiniti, non ci sono webinar &ldquo;gratis&rdquo;
              che ti vendono l&apos;evento da €2.000. Solo un team che costruisce, un laptop, un abbonamento Claude Max
              e <span className="text-silver-orange font-semibold">un metodo che funziona</span>.
            </p>
          </Reveal>

          <Reveal delay={0.5}>
            <p className="text-xl md:text-2xl font-bold text-silver-white leading-snug pt-4">
              Se vuoi vederlo dall&apos;interno,{" "}
              <span className="text-orange-pure">te lo mostro io, dal Modulo 1.</span>
            </p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
