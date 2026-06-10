"use client";

import { Reveal } from "@/components/reveal";
import { ShieldCheck } from "lucide-react";

export function Garanzia() {
  return (
    <section
      className="bg-ink-2 section-airy relative overflow-hidden"
      aria-labelledby="garanzia-h2"
    >
      {/* Glow ambient */}
      <div
        className="glow-gold-amb"
        style={{
          width: 600,
          height: 360,
          left: "50%",
          top: "50%",
          transform: "translate(-50%, -50%)",
          opacity: 0.18,
        }}
        aria-hidden
      />

      <div className="container-tight text-center relative">
        <Reveal>
          <span className="bubble-silver">
            <ShieldCheck className="h-3.5 w-3.5" />
            Garanzia operativa
          </span>
        </Reveal>

        <Reveal delay={0.10}>
          <h2 id="garanzia-h2" className="mt-6">
            <span className="text-silver-white">Se non funziona,</span>{" "}
            <span className="text-silver-gold font-accent italic">
              lo sistemiamo gratis.
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.20}>
          <p className="mt-7 text-[1.10rem] leading-relaxed text-white/90 max-w-2xl mx-auto font-light">
            Se entro 30 giorni dal go-live il workflow non produce almeno 1
            risultato misurabile (lead generati, post pubblicati, email
            mandate automaticamente) rimettiamo mano gratuitamente finché
            non funziona. Non ci scappiamo. Non ti lasciamo con un sistema
            rotto.
          </p>
        </Reveal>

        <Reveal delay={0.30}>
          <p className="mt-6 text-[0.92rem] uppercase tracking-[0.20em] font-semibold text-gold-pure/85">
            Risultati misurabili · o rifacciamo gratis · senza discussioni
          </p>
        </Reveal>
      </div>
    </section>
  );
}
