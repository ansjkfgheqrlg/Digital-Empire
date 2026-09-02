"use client";

import { Reveal } from "@/components/reveal";

const levels = [
  {
    lv: 1,
    t: "Operatività Manuale",
    d: "Tutto a mano. Outreach, contenuti, follow-up. La knowledge è nella tua testa. Sei il collo di bottiglia — e lo sai.",
    status: "La trappola",
  },
  {
    lv: 2,
    t: "SaaS di Terze Parti",
    d: "Paghi canoni mensili per tool generici che non conoscono il tuo brand. Se smetti di pagare, perdi tutto. Dipendenza totale.",
    status: "Il vicolo cieco",
  },
  {
    lv: 3,
    t: "Sistema AI Proprietario",
    d: "Il sistema AI gira sui tuoi server, conosce il tuo ICP, lavora h24. Zero canoni. Il codice è tuo per sempre.",
    status: "Target Empire",
    premium: true,
  },
];

export function Hierarchy() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">La scala dell&apos;operatività</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              In quale livello sei oggi?<br />
              <span className="text-orange-pure italic font-medium">E dove vuoi essere domani?</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {levels.map((l, i) => (
            <Reveal key={i} delay={0.2 + i * 0.1}>
              <div className="card-glass h-full flex flex-col">
                {/* Status label — top of card */}
                <div
                  className="inline-flex items-center gap-2 mb-5 self-start"
                  style={{
                    background: l.premium
                      ? "linear-gradient(135deg, rgba(251,70,4,0.22) 0%, rgba(251,70,4,0.10) 100%)"
                      : "linear-gradient(135deg, rgba(19,19,19,0.12) 0%, rgba(19,19,19,0.06) 100%)",
                    border: l.premium
                      ? "1px solid rgba(251,70,4,0.45)"
                      : "1px solid rgba(19,19,19,0.18)",
                    borderRadius: 9999,
                    padding: "0.3rem 0.85rem",
                  }}
                >
                  <span
                    style={{
                      width: 6,
                      height: 6,
                      borderRadius: "50%",
                      background: l.premium ? "#fb4604" : "rgba(19,19,19,0.45)",
                      display: "inline-block",
                      flexShrink: 0,
                    }}
                  />
                  <span
                    style={{
                      fontSize: "0.68rem",
                      fontWeight: 800,
                      letterSpacing: "0.22em",
                      textTransform: "uppercase",
                      color: l.premium ? "#fb4604" : "rgba(19,19,19,0.55)",
                    }}
                  >
                    {l.status}
                  </span>
                </div>

                {/* Step number */}
                <div
                  className="mb-5 inline-flex items-center justify-center rounded-xl font-black"
                  style={{
                    width: "2.75rem",
                    height: "2.75rem",
                    fontSize: "1.1rem",
                    background: l.premium
                      ? "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)"
                      : "linear-gradient(135deg, #1c1c1c 0%, #0a0a0a 100%)",
                    color: "#ffffff",
                    boxShadow: l.premium
                      ? "0 6px 20px rgba(251,70,4,0.45)"
                      : "0 6px 18px rgba(0,0,0,0.40)",
                  }}
                >
                  {l.lv}
                </div>

                <h3 className="text-2xl font-bold mb-3" style={{ color: "#0a0a0a" }}>{l.t}</h3>
                <p className="leading-relaxed text-[0.94rem]" style={{ color: "rgba(19,19,19,0.75)" }}>{l.d}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
