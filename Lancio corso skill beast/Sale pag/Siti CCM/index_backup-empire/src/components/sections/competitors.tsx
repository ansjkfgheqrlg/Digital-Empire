"use client";

import { Reveal } from "@/components/reveal";
import { TrendingDown, Swords, Flame, Clock } from "lucide-react";

const facts = [
  {
    icon: Swords,
    big: "100%",
    label: "Dei tuoi competitor",
    desc: "Esistono. Sempre. In ogni nicchia. Non conosco un mercato senza concorrenza, e non esiste.",
  },
  {
    icon: Flame,
    big: "78%",
    label: "Già adotta AI",
    desc: "Delle aziende nel tuo settore sta integrando AI nei processi interni. Mentre tu leggi questa frase.",
  },
  {
    icon: TrendingDown,
    big: "-40%",
    label: "Margine a 18 mesi",
    desc: "Chi non orchestra AI proprietaria perderà margine e clienti contro chi lo fa. È matematica, non opinione.",
  },
  {
    icon: Clock,
    big: "6–12",
    label: "Mesi di vantaggio",
    desc: "La finestra per posizionarti PRIMA che il mercato saturi. Dopo, entri come commodity. Sei in ritardo.",
  },
];

export function Competitors() {
  return (
    <section className="bg-ink-2 section section-border-t relative overflow-hidden">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.14) 0%, transparent 55%)",
        }}
      />

      <div className="max-w-5xl mx-auto px-6 relative">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">La verità scomoda // Competitor</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[52px] font-bold leading-[1.05] mt-6">
              <span className="text-silver-white">Mentre leggi questa pagina, </span>
              <br className="hidden md:block" />
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                  letterSpacing: "-0.01em",
                }}
              >
                un tuo competitor sta automatizzando.
              </span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/65 text-lg max-w-3xl mx-auto mt-8 leading-relaxed">
              Ripetilo a voce alta: <strong className="text-silver-orange">tutti hanno competitor</strong>.
              Non esiste il mercato vergine, non esiste il &ldquo;nessuno fa quello che faccio io&rdquo;. Esistono solo
              competitor visibili e competitor nascosti. E oggi i competitor che contano stanno costruendo System AI
              mentre tu sei ancora a chattare con ChatGPT.
            </p>
          </Reveal>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5 mb-16">
          {facts.map((f, i) => {
            const Icon = f.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.08}>
                <div
                  className="relative rounded-2xl p-6 h-full text-center overflow-hidden"
                  style={{
                    background:
                      "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                    border: "1px solid rgba(220,220,218,0.22)",
                    boxShadow:
                      "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                  }}
                >
                  <div className="flex justify-center mb-4">
                    <Icon className="h-6 w-6 text-orange-pure" strokeWidth={1.7} />
                  </div>
                  <div
                    className="text-[38px] md:text-[44px] font-black leading-none mb-2"
                    style={{
                      background:
                        "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #fb4604 100%)",
                      WebkitBackgroundClip: "text",
                      WebkitTextFillColor: "transparent",
                      backgroundClip: "text",
                    }}
                  >
                    {f.big}
                  </div>
                  <div className="text-[10px] uppercase tracking-[0.22em] font-black text-white/55 mb-3">
                    {f.label}
                  </div>
                  <p className="text-[13px] leading-relaxed text-white/70">{f.desc}</p>
                </div>
              </Reveal>
            );
          })}
        </div>

        <Reveal delay={0.3}>
          <div
            className="relative max-w-3xl mx-auto rounded-2xl p-8 md:p-10 text-center overflow-hidden"
            style={{
              background:
                "linear-gradient(160deg, #d9d6cf 0%, #b8b4ac 45%, #7a7770 100%)",
              border: "1px solid rgba(255,255,255,0.35)",
              boxShadow:
                "inset 0 1px 0 rgba(255,255,255,0.55), inset 0 -1px 0 rgba(0,0,0,0.25), 0 20px 55px -15px rgba(0,0,0,0.55)",
            }}
          >
            <div
              aria-hidden="true"
              className="absolute -top-10 left-1/2 -translate-x-1/2 select-none pointer-events-none"
              style={{
                fontFamily: "var(--font-serif), Georgia, serif",
                fontStyle: "italic",
                fontSize: "160px",
                lineHeight: 1,
                color: "#1c1c1c",
                opacity: 0.18,
              }}
            >
              &ldquo;
            </div>
            <p
              className="relative text-[22px] md:text-[30px] leading-[1.4] text-ink"
              style={{
                fontFamily: "var(--font-serif), Georgia, serif",
                fontStyle: "italic",
                fontWeight: 500,
              }}
            >
              Il tuo competitor non ha bisogno di essere più bravo di te. <br />
              Gli basta avere un System AI che <span style={{ color: "#7a2a05" }} className="font-bold">lavora mentre lui dorme</span>.
            </p>
            <p className="relative mt-6 text-[12px] uppercase tracking-[0.28em] font-black text-ink/70">
              → E tu cosa stai facendo adesso?
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.4}>
          <p className="text-center text-white/55 text-sm max-w-2xl mx-auto mt-10 leading-relaxed">
            Puoi ignorarlo. Oppure puoi diventare tu quel competitor che gli altri rincorrono. <br />
            <span className="text-silver-orange font-semibold">
              La finestra è aperta per altri 12 mesi. Dopo è chiusa.
            </span>
          </p>
        </Reveal>
      </div>
    </section>
  );
}
