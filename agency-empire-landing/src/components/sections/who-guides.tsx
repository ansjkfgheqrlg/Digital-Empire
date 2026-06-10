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
          <span className="bubble-orange mb-8">Chi implementa il sistema</span>
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
            &ldquo;Ok ma chi siete?&rdquo;
          </h2>
        </Reveal>

        <div className="space-y-6 text-white/75 text-lg leading-relaxed max-w-3xl">
          <Reveal delay={0.2}>
            <p>
              Il sistema lo installa <span className="text-orange-pure font-bold">Maximilian (Max)</span> — founder di{" "}
              <strong className="text-silver-white">Digital Empire</strong>, agenzia che costruisce automazioni AI,
              landing page e System AI completi per clienti reali. Non un consulente. Un implementatore.
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <p>
              Negli ultimi anni nell&apos;ecosistema AI abbiamo costruito{" "}
              <span
                className="inline-block px-2 py-0.5 rounded font-black"
                style={{ background: "#fb4604", color: "#fff" }}
              >
                50+ sistemi
              </span>{" "}
              reali — outreach factory, content engine, knowledge base aziendali. Ogni sistema è in produzione,
              ogni cliente ha il codice sorgente in mano.
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <p>
              <strong className="text-silver-white">Digital Empire non è una software house.</strong> Non vendiamo
              abbonamenti, non facciamo onboarding infiniti, non ti teniamo in ostaggio con un SaaS. Installiamo,
              formiamo, consegniamo. Poi il sistema{" "}
              <span className="text-silver-orange font-semibold">gira da solo — e tu sei libero</span>.
            </p>
          </Reveal>

          <Reveal delay={0.5}>
            <p className="text-xl md:text-2xl font-bold text-silver-white leading-snug pt-4">
              Se vuoi capire quale sistema è giusto per te,{" "}
              <span className="text-orange-pure">prenota una chiamata strategica.</span>
            </p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
