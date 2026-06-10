"use client";

import { Reveal } from "@/components/reveal";
import { Quote, Star } from "lucide-react";

const TESTIMONIALS = [
  {
    quote:
      "Ho triplicato i contatti mensili senza toccare niente io. Il workflow gira da solo. Prospect, email, follow-up. Io mi occupo solo delle call con i lead caldi che arrivano.",
    name: "Marco Resta",
    role: "Coach · Skill Beast",
    avatar: "MR",
  },
  {
    quote:
      "Prima ci mettevo 3 ore al giorno per i post. Ora 20 minuti di review settimanale. Il sistema genera, schedula, pubblica. Io non tocco niente e la mia presence è triplicata.",
    name: "Sara Conti",
    role: "Social Media Manager · Freelance",
    avatar: "SC",
  },
  {
    quote:
      "Primo mese: 240 lead qualificati arrivati in automatico. Non ci credevo finché non ho visto il dashboard in live. Nessun altro strumento mi aveva dato qualcosa di simile.",
    name: "Luca Pellegrini",
    role: "Founder · Agenzia Digitale",
    avatar: "LP",
  },
];

export function Testimonial() {
  return (
    <section
      className="bg-ink section relative overflow-hidden"
      aria-labelledby="testi-h2"
    >
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <span className="w-1.5 h-1.5 rounded-full bg-gold-pure" />
              Voci dei clienti
            </span>
            <h2 id="testi-h2" className="mt-6">
              <span className="text-silver-white">Quello che dicono</span>{" "}
              <span className="text-silver-gold font-accent italic">
                di noi.
              </span>
            </h2>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-3 gap-6">
          {TESTIMONIALS.map((t, i) => (
            <Reveal key={i} delay={0.10 + i * 0.10}>
              <article className="card-dark relative h-full flex flex-col">
                <Quote className="h-6 w-6 text-gold-pure mb-4" strokeWidth={2} />
                <p className="font-accent italic text-[1.0625rem] leading-relaxed text-white/85 mb-6 flex-1">
                  &ldquo;{t.quote}&rdquo;
                </p>
                {/* Stars */}
                <div className="flex gap-0.5 mb-4">
                  {Array.from({ length: 5 }).map((_, k) => (
                    <Star
                      key={k}
                      className="h-3.5 w-3.5 text-gold-pure"
                      fill="#fb4604"
                      strokeWidth={1}
                    />
                  ))}
                </div>
                <div className="flex items-center gap-3 pt-4" style={{ borderTop: "1px solid rgba(255,255,255,0.08)" }}>
                  <span
                    className="grid place-items-center w-10 h-10 rounded-full text-[0.85rem] font-bold text-[#0a0a0a] shrink-0"
                    style={{
                      background:
                        "linear-gradient(135deg, #fb4604 0%, #ff6a2e 50%, #c93a0a 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.50), 0 4px 8px rgba(0,0,0,0.25)",
                    }}
                  >
                    {t.avatar}
                  </span>
                  <div className="flex flex-col leading-tight">
                    <span className="text-[0.92rem] font-semibold text-white">
                      {t.name}
                    </span>
                    <span className="text-[0.78rem] text-white/50">
                      {t.role}
                    </span>
                  </div>
                </div>
              </article>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
