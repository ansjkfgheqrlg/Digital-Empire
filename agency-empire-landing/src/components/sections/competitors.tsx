"use client";

import { Reveal } from "@/components/reveal";
import { TrendingDown, Swords, Flame, Clock } from "lucide-react";

const facts = [
  {
    icon: Swords,
    big: "Stessi colli di bottiglia",
    label: "La maggior parte dei competitor",
    desc: "Condivide i tuoi stessi limiti operativi. Il primo che li risolve con l'AI guadagna un vantaggio difficile da recuperare.",
  },
  {
    icon: Flame,
    big: "Adozione in crescita",
    label: "AI nel tuo settore",
    desc: "Sempre più aziende stanno integrando automazioni AI nei processi interni. Mentre tu leggi questa frase.",
  },
  {
    icon: TrendingDown,
    big: "Margine eroso",
    label: "Nel medio periodo",
    desc: "Chi non automatizza tende a erodere margine contro chi ha sistemi AI proprietari che lavorano h24. È una traiettoria, non un'opinione.",
  },
  {
    icon: Clock,
    big: "Adesso",
    label: "La finestra per posizionarti",
    desc: "Posizionarti PRIMA che il mercato saturi è un vantaggio. Dopo, entri come commodity. La finestra si sta chiudendo.",
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
            <p className="text-white/82 text-lg max-w-3xl mx-auto mt-8 leading-relaxed">
              Non esiste mercato senza concorrenza. Esistono solo competitor visibili e competitor nascosti. E oggi i competitor che contano{" "}
              <strong className="text-silver-orange">stanno installando sistemi AI proprietari</strong> mentre tu sei ancora a mandare DM a mano.
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
                    className="text-[22px] md:text-[26px] font-black leading-[1.1] mb-3 min-h-[58px] flex items-center justify-center"
                    style={{
                      background:
                        "linear-gradient(180deg, #ffffff 0%, #d9d6cf 45%, #fb4604 100%)",
                      WebkitBackgroundClip: "text",
                      WebkitTextFillColor: "transparent",
                      backgroundClip: "text",
                      letterSpacing: "-0.01em",
                    }}
                  >
                    {f.big}
                  </div>
                  <div className="text-[11px] uppercase tracking-[0.18em] font-black text-white/80 mb-3">
                    {f.label}
                  </div>
                  <p className="text-[13.5px] leading-relaxed text-white/88">{f.desc}</p>
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
              Gli basta avere un sistema AI che <span style={{ color: "#7a2a05" }} className="font-bold">lavora mentre lui dorme</span>.
            </p>
            <p className="relative mt-6 text-[12px] uppercase tracking-[0.28em] font-black text-ink/70">
              → E tu cosa stai facendo adesso?
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.4}>
          <p className="text-center text-white/82 text-[15px] max-w-2xl mx-auto mt-10 leading-relaxed">
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
