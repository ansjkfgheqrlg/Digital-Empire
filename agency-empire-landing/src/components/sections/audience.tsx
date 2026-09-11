"use client";

import { Reveal } from "@/components/reveal";

const audience_yes = [
  "Promuovi prodotti digitali, servizi o consulenza high ticket e vuoi più conversazioni qualificate ogni settimana.",
  "Hai già un prodotto sul mercato e vuoi scalare il volume di contatti senza assumere un team sales.",
  "L'outreach ti prosciuga ore ogni mattina, oppure non lo fai affatto perché è insostenibile a mano.",
  "Vuoi possedere i tuoi strumenti — non affittarli da un SaaS che può alzare i prezzi o sparire.",
  "Ogni lancio ti costa 2-3 settimane solo per produrre il copy. Sai che così non può continuare.",
];

const audience_no = [
  "Non hai ancora un prodotto valido sul mercato — l'automazione amplifica solo ciò che già funziona.",
  "Cerchi un'estensione Chrome da €10 al mese da installare e dimenticare nel browser.",
  "Vuoi delegare interamente il marketing senza comprendere o supervisionare i tuoi flussi.",
];

export function Audience() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">Per chi è questo sistema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[1.9rem] md:text-[3rem] font-bold leading-tight mt-5">
              <span className="text-silver-white">Ideato su misura per </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                }}
              >
                Creator, Coach <span style={{ whiteSpace: "nowrap" }}>&amp; Business Owner.</span>
              </span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          {/* YES card */}
          <Reveal delay={0.18}>
            <div
              className="rounded-2xl p-7 h-full"
              style={{
                background: "linear-gradient(145deg, #1f0800 0%, #3d0f00 25%, #621a00 52%, #3d0f00 76%, #1a0500 100%)",
                border: "2px solid rgba(210,218,232,0.68)",
                boxShadow: [
                  "0 0 60px -20px rgba(251,70,4,0.50)",
                  "0 20px 50px -20px rgba(0,0,0,0.70)",
                  "0 2px 0 rgba(255,255,255,0.12) inset",
                ].join(", "),
              }}
            >
              <div className="flex items-center gap-2.5 mb-6">
                <span
                  className="text-[11px] font-black uppercase tracking-[0.22em] px-3 py-1.5 rounded-full"
                  style={{
                    background: "linear-gradient(135deg, rgba(251,70,4,0.55) 0%, rgba(180,40,0,0.70) 100%)",
                    border: "1px solid rgba(251,100,50,0.65)",
                    color: "#ffffff",
                    boxShadow: "0 2px 12px rgba(251,70,4,0.35)",
                  }}
                >
                  ✓ È per te se:
                </span>
              </div>
              <ul className="space-y-4">
                {audience_yes.map((s, i) => (
                  <li
                    key={i}
                    className="flex gap-3 text-[0.92rem] leading-relaxed"
                    style={{ color: "rgba(255,255,255,0.92)" }}
                  >
                    <span className="shrink-0 font-black text-[1rem] mt-[-1px]" style={{ color: "#fb7040" }}>›</span>
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>

          {/* NO card */}
          <Reveal delay={0.28}>
            <div
              className="rounded-2xl p-7 h-full"
              style={{
                background: "linear-gradient(145deg, #060a14 0%, #0c1426 30%, #161e3a 58%, #0c1428 80%, #060810 100%)",
                border: "2px solid rgba(210,218,232,0.68)",
                boxShadow: [
                  "0 0 50px -20px rgba(60,90,180,0.35)",
                  "0 20px 50px -20px rgba(0,0,0,0.75)",
                  "0 2px 0 rgba(255,255,255,0.08) inset",
                ].join(", "),
              }}
            >
              <div className="flex items-center gap-2.5 mb-6">
                <span
                  className="text-[11px] font-black uppercase tracking-[0.22em] px-3 py-1.5 rounded-full"
                  style={{
                    background: "linear-gradient(135deg, rgba(80,100,160,0.55) 0%, rgba(30,45,100,0.70) 100%)",
                    border: "1px solid rgba(120,148,210,0.50)",
                    color: "rgba(220,228,250,0.98)",
                    boxShadow: "0 2px 12px rgba(40,60,140,0.30)",
                  }}
                >
                  ✕ Non è per te se:
                </span>
              </div>
              <ul className="space-y-4">
                {audience_no.map((s, i) => (
                  <li
                    key={i}
                    className="flex gap-3 text-[0.92rem] leading-relaxed"
                    style={{ color: "rgba(214,222,248,0.94)" }}
                  >
                    <span className="shrink-0 font-black text-[1rem] mt-[-1px]" style={{ color: "rgba(160,175,220,0.75)" }}>›</span>
                    <span>{s}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
