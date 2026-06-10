"use client";

import { Reveal } from "@/components/reveal";

const GRAIN = (seed: string) =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.15' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.94 0 0 0 0 0.92 0 0 0 0 0.90 0 0 0 0.26 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

const deliverables = [
  {
    n: "01",
    title: "Caroselli Instagram",
    description:
      "L'AI genera il copy CRO per ogni slide, poi il motore di automazione costruisce le grafiche visive complete. Pronto da pubblicare.",
    seed: "5",
    bg: "linear-gradient(148deg, #d89080 0%, #c87870 40%, #b86858 70%, #985040 100%)",
    border: "rgba(220,140,120,0.45)",
    labelColor: "#b04030",
  },
  {
    n: "02",
    title: "Script Video AI",
    description:
      "Script parola per parola per Reels, TikTok e YouTube: hook di 3 secondi, corpo strutturato e CTA che genera engagement.",
    seed: "8",
    bg: "linear-gradient(148deg, #9098c8 0%, #8088b8 40%, #7078a8 70%, #505880 100%)",
    border: "rgba(150,160,220,0.42)",
    labelColor: "#4858a0",
  },
  {
    n: "03",
    title: "Caption + Hashtag",
    description:
      "Descrizione del post ottimizzata con emoji, CTA DM e set di hashtag calibrati tra volume alto e nicchia per massimizzare il reach.",
    seed: "2",
    bg: "linear-gradient(148deg, #88c090 0%, #78b080 40%, #68a070 70%, #508060 100%)",
    border: "rgba(130,200,140,0.42)",
    labelColor: "#2a7040",
  },
  {
    n: "04",
    title: "Upload Google Drive",
    description:
      "I contenuti finiti vengono caricati automaticamente su Google Drive, organizzati per argomento e pronti da scaricare o condividere.",
    seed: "14",
    bg: "linear-gradient(148deg, #d8a0b0 0%, #c890a0 40%, #b87888 70%, #906070 100%)",
    border: "rgba(220,160,180,0.42)",
    labelColor: "#904060",
  },
  {
    n: "05",
    title: "Pubblicazione Programmata",
    description:
      "Puoi collegare il workflow a strumenti di scheduling per pubblicare automaticamente sui tuoi canali social senza toccare nulla.",
    seed: "9",
    bg: "linear-gradient(148deg, #d8c880 0%, #c8b868 40%, #b8a050 70%, #987830 100%)",
    border: "rgba(220,200,120,0.42)",
    labelColor: "#806020",
  },
  {
    n: "06",
    title: "Batch Produzione Multipla",
    description:
      "Il sistema può girare in batch e generare 5, 10 o 20 caroselli in una sola sessione. Settimane di contenuti in pochi minuti.",
    seed: "6",
    bg: "linear-gradient(148deg, #b898c8 0%, #a888b8 40%, #9878a8 70%, #785888 100%)",
    border: "rgba(190,150,210,0.42)",
    labelColor: "#704888",
  },
];

export function ContentOutput() {
  return (
    <section className="bg-grey section section-border-t">
      <style>{`
        .co-card {
          transition: transform 0.42s cubic-bezier(0.22,1,0.36,1), box-shadow 0.38s ease;
        }
        .co-card:hover { transform: translateY(-6px) scale(1.007); }
      `}</style>

      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">Output del Sistema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[1.9rem] md:text-[2.9rem] font-bold leading-tight mt-6 text-silver-black">
              Cosa produce la tua{" "}
              <span style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400 }}>
                fabbrica di contenuti.
              </span>
            </h2>
          </Reveal>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {deliverables.map((d, i) => (
            <Reveal key={i} delay={0.12 + i * 0.07}>
              <div
                className="co-card rounded-2xl p-6 h-full flex flex-col"
                style={{
                  backgroundImage: [GRAIN(d.seed), d.bg].join(", "),
                  backgroundSize: "200px 200px, 100% 100%",
                  backgroundBlendMode: "screen, normal",
                  border: `1px solid ${d.border}`,
                  boxShadow: [
                    "0 16px 40px -14px rgba(0,0,0,0.20)",
                    "0 2px 0 rgba(255,255,255,0.45) inset",
                    "0 -1px 0 rgba(0,0,0,0.08) inset",
                  ].join(", "),
                }}
              >
                <div
                  className="text-[11px] font-black uppercase tracking-[0.22em] mb-4"
                  style={{ color: d.labelColor }}
                >
                  [ DELIVERABLE {d.n} ]
                </div>
                <h3 className="text-[1.05rem] font-bold text-ink leading-tight mb-3">
                  {d.title}
                </h3>
                <p className="text-ink/65 text-[0.88rem] leading-relaxed flex-1">
                  {d.description}
                </p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
