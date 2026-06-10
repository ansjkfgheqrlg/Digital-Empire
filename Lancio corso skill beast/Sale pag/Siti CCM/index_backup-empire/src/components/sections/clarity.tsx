"use client";

import { Reveal } from "@/components/reveal";
import { Mail, PlayCircle, Users, Calendar, LifeBuoy, CheckCircle2 } from "lucide-react";

const steps = [
  {
    icon: Mail,
    time: "T+0 minuti",
    title: "Email di conferma + accesso immediato",
    desc: "Ricevi subito le credenziali per l'area membri. Nessuna attesa, nessuna lista d'attesa: paghi e sei dentro.",
  },
  {
    icon: PlayCircle,
    time: "T+5 minuti",
    title: "Dentro la piattaforma",
    desc: "Trovi i 9 moduli già pronti, 30+ video-lezioni, 18 template scaricabili e l'ordine esatto in cui seguirli. Zero scelte da fare: parti dal Modulo 1.",
  },
  {
    icon: Users,
    time: "T+10 minuti",
    title: "Accesso alla community privata",
    desc: "Entri nel canale riservato Builder. Lì chiedi, condividi i tuoi System AI e ricevi feedback diretto dallo staff e dagli altri architetti.",
  },
  {
    icon: Calendar,
    time: "Ogni settimana",
    title: "Q&A live con lo staff",
    desc: "Una sessione settimanale in diretta. Porti i tuoi blocchi, li smontiamo insieme. Le registrazioni restano tue per sempre.",
  },
  {
    icon: LifeBuoy,
    time: "Sempre",
    title: "Supporto tecnico reale",
    desc: "Email, ticket, community. Risposta entro 24h lavorative. Non sei lasciato solo davanti a un player video.",
  },
  {
    icon: CheckCircle2,
    time: "Entro 30 giorni",
    title: "Garanzia \u201CBuilder o Rimborsato\u201D",
    desc: "Segui i primi 3 moduli, fai gli esercizi, non vedi progresso? Scrivi una mail, rimborso integrale. Il rischio è tutto mio.",
  },
];

export function Clarity() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Massima chiarezza // Zero zone grigie</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Cosa succede </span>
              <span className="text-orange-pure italic font-medium">esattamente</span>
              <span className="text-silver-black"> dopo l&apos;acquisto.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#2a2a2a]/75 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              Niente piccoli caratteri, niente upsell nascosti, niente &ldquo;ti arriverà una mail prima o poi&rdquo;.
              Ecco la sequenza precisa, minuto per minuto.
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          {steps.map((s, i) => {
            const Icon = s.icon;
            return (
              <Reveal key={i} delay={0.15 + i * 0.06}>
                <div className="card-paper rounded-2xl p-6 h-full flex gap-5 hover-lift">
                  <div
                    className="shrink-0 w-12 h-12 rounded-xl flex items-center justify-center"
                    style={{
                      background:
                        "radial-gradient(circle at 30% 30%, rgba(251,70,4,0.18), rgba(251,70,4,0.04) 65%, transparent 80%)",
                      border: "1px solid rgba(251,70,4,0.35)",
                    }}
                  >
                    <Icon className="h-5 w-5 text-orange-pure" strokeWidth={1.8} />
                  </div>
                  <div>
                    <div className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure mb-1">
                      {s.time}
                    </div>
                    <h3 className="text-lg font-black text-silver-black mb-2 leading-tight">
                      {s.title}
                    </h3>
                    <p className="text-[#2a2a2a]/78 text-sm leading-relaxed">{s.desc}</p>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>

        <Reveal delay={0.5}>
          <div className="mt-12 text-center">
            <p className="text-[13px] uppercase tracking-[0.2em] font-bold text-[#2a2a2a]/60">
              <span className="text-orange-pure">→</span> Accesso a vita · Aggiornamenti inclusi · Pagamento sicuro Stripe
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
