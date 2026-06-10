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
              Che tu sia uno che sta imparando adesso, un freelancer che vuole scalare, un consulente stanco di vendere
              ore, o uno che lavora in azienda e vede il mercato cambiare sotto i piedi —{" "}
              <strong className="text-silver-white">se sei qui è perché l&apos;AI ti ha già preso.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.2}>
            <p>
              Stai già usando Claude. ChatGPT. Forse Perplexity, forse Gemini. E ti piacciono pure. Ci passi ore ogni
              settimana.
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <p>
              Ma ogni volta che apri una chat nuova hai sempre la stessa sensazione:
              <br />
              <span className="block mt-3 text-[22px] md:text-[28px] font-bold text-silver-white leading-snug">
                &ldquo;Questo coso è potente&hellip;{" "}
                <span className="text-orange-pure italic font-normal" style={{ fontFamily: "var(--font-serif), Georgia, serif" }}>
                  ma sto grattando la superficie.
                </span>
                &rdquo;
              </span>
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <p className="text-[19px] md:text-[22px] leading-relaxed">
              Non è un tuo limite.{" "}
              <span className="hl-block">È che nessuno te l&apos;ha mai spiegato come va spiegato.</span>
            </p>
          </Reveal>

          <Reveal delay={0.5}>
            <p>
              Online trovi 10.000 video su &ldquo;come scrivere il prompt perfetto&rdquo;, influencer che ti vendono il
              plugin della settimana, corsi che parlano di AI senza averne mai messo uno in produzione.{" "}
              <strong className="text-silver-orange">Rumore. Tutto rumore.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.6}>
            <p>
              Quello che ti serve non è un altro trucco da prompt. È un metodo. Una bussola. Un modo di pensare l&apos;AI
              come <strong className="text-silver-white">sistema</strong>, non come chat. E te lo serve qualcuno che i
              System AI li costruisce davvero, ogni giorno, per sé e per i clienti.
            </p>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
