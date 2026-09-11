"use client";

import { Reveal } from "@/components/reveal";

export function ListenUp() {
  return (
    <section className="bg-ink-2 section relative overflow-hidden">
      <div className="max-w-4xl mx-auto px-6 relative">
        <Reveal>
          <h2
            className="text-[52px] md:text-[88px] font-black leading-[0.95] tracking-tight mb-10"
            style={{
              background:
                "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #8a8378 100%)",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              backgroundClip: "text",
            }}
          >
            ASCOLTA BENE.
          </h2>
        </Reveal>

        <div className="space-y-6 text-white/75 text-lg md:text-xl leading-relaxed max-w-3xl">
          <Reveal delay={0.1}>
            <p>
              Che tu sia un coach, un social media manager, un imprenditore o una piccola agenzia —{" "}
              <strong className="text-silver-white">se sei qui è perché senti il peso dell&apos;operatività.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <p>
              E ogni volta che guardi un competitor crescere più veloce di te, sai già la risposta:
              <br />
              <span className="block mt-3 text-[22px] md:text-[28px] font-bold text-silver-white leading-snug">
                &ldquo;Loro hanno qualcosa che{" "}
                <span className="text-orange-pure italic font-normal" style={{ fontFamily: "var(--font-serif), Georgia, serif" }}>
                  lavora mentre dormono.
                </span>
                &rdquo;
              </span>
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <p className="text-[19px] md:text-[22px] leading-relaxed">
              Non è fortuna.{" "}
              <span className="hl-block">È un sistema. E noi lo costruiamo per te.</span>
            </p>
          </Reveal>

          <Reveal delay={0.6}>
            <p>
              Quello che ti serve non è un altro abbonamento da pagare. È un&apos;infrastruttura AI proprietaria — installata sui tuoi server, calibrata sul tuo brand e{" "}
              <strong className="text-silver-white">tua per sempre</strong>. Con zero canoni mensili dopo il setup.
            </p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
