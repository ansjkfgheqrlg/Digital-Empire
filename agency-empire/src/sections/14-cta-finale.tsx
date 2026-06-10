"use client";

import { useState } from "react";
import { Reveal } from "@/components/reveal";
import {
  Send,
  Check,
  ArrowRight,
  Mail,
  Sparkles,
  ShieldCheck,
} from "lucide-react";
import { MagneticButton } from "@/components/magnetic-button";

const BENEFITS = [
  "Demo live del workflow (non slides. Il sistema vero)",
  "Piano di automazione personalizzato sul tuo business",
  "Risposta entro 24h dal team Digital Empire",
];

export function CTAFinale() {
  const [submitted, setSubmitted] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [obiettivo, setObiettivo] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);

    if (obiettivo === "strategy-call") {
      window.location.href = "/prenota";
      return;
    }

    setSubmitting(true);
    const form = e.currentTarget;
    const data = new FormData(form);
    const nome = data.get("nome") as string;
    const email = data.get("email") as string;
    const det = data.get("dettagli") as string;

    const subject = encodeURIComponent(`Demo richiesta: ${obiettivo} - ${nome}`);
    const body = encodeURIComponent(
      `Nome / Azienda: ${nome}\nEmail: ${email}\nInteresse: ${obiettivo}\n\nDettagli:\n${det}`
    );
    window.location.href = `mailto:hq@digitalempire.team?subject=${subject}&body=${body}`;
    setSubmitting(false);
    setSubmitted(true);
  }

  return (
    <section
      id="cta-finale"
      className="bg-ink section-airy relative overflow-hidden"
      aria-labelledby="cta-h2"
    >
      {/* Glow ambient duo */}
      <div
        className="glow-gold-amb"
        style={{
          width: 700,
          height: 460,
          left: "20%",
          top: "30%",
          opacity: 0.22,
        }}
        aria-hidden
      />
      <div
        className="glow-purple-amb"
        style={{
          width: 360,
          height: 360,
          right: "10%",
          bottom: "10%",
          opacity: 0.12,
        }}
        aria-hidden
      />

      <div className="container-wide relative">
        <div className="grid lg:grid-cols-2 gap-8 lg:gap-16 items-start py-6 md:py-12">
          {/* LEFT — pitch */}
          <div>
            <Reveal>
              <span className="bubble-gold">
                <Sparkles className="h-3.5 w-3.5" />
                Ultima fermata
              </span>
            </Reveal>
            <Reveal delay={0.10} className="mt-5 mb-5">
              <div className="pre-headline">
                Demo gratuita · 30 minuti · nessun impegno
              </div>
            </Reveal>
            <Reveal delay={0.20}>
              <h2 id="cta-h2" className="mb-6">
                <span className="text-silver-white">Automatizza ciò che ti blocca.</span>{" "}
                <span className="text-silver-gold font-accent italic">
                  Adesso.
                </span>
              </h2>
            </Reveal>
            <Reveal delay={0.30}>
              <p className="text-[1.05rem] leading-relaxed text-white/90 max-w-lg mb-8 font-light">
                Parliamo 30 minuti. Ti mostro in live un workflow attivo. Niente
                slides, niente pitch. Solo il sistema reale che cambia la tua
                operatività. Se non ti convince, non si fa niente.
              </p>
            </Reveal>

            <Reveal delay={0.40}>
              <ul className="flex flex-col gap-3 mb-10">
                {BENEFITS.map((b, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-3 text-[0.96rem] text-white/85"
                  >
                    <span
                      className="grid place-items-center w-6 h-6 rounded-full mt-0.5 shrink-0"
                      style={{
                        background:
                          "linear-gradient(135deg, #fb4604 0%, #c93a0a 100%)",
                        boxShadow: "0 0 12px rgba(201,55,10,0.35)",
                      }}
                    >
                      <Check
                        className="h-3.5 w-3.5 text-white"
                        strokeWidth={3}
                      />
                    </span>
                    <span>{b}</span>
                  </li>
                ))}
              </ul>
            </Reveal>

            <Reveal delay={0.50}>
              <div className="flex items-center gap-2 text-[0.85rem] text-white/50">
                <ShieldCheck className="h-4 w-4 text-gold-pure" />
                <span>hq@digitalempire.team</span>
              </div>
            </Reveal>
          </div>

          {/* RIGHT — form */}
          <Reveal delay={0.20}>
            <div
              className="relative rounded-2xl p-5 md:p-10"
              style={{
                background:
                  "linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%)",
                border: "1px solid rgba(255,255,255,0.10)",
                boxShadow:
                  "0 40px 80px -32px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.08)",
                backdropFilter: "blur(8px)",
              }}
            >
              {!submitted ? (
                <form
                  onSubmit={handleSubmit}
                  className="flex flex-col gap-5"
                  data-lenis-prevent
                >
                  <div className="grid sm:grid-cols-2 gap-4">
                    <div className="form-field">
                      <label htmlFor="nome">Nome / Azienda</label>
                      <input
                        type="text"
                        id="nome"
                        name="nome"
                        required
                        placeholder="Mario Rossi · Acme S.r.l."
                        className="form-input"
                      />
                    </div>
                    <div className="form-field">
                      <label htmlFor="email">Email</label>
                      <input
                        type="email"
                        id="email"
                        name="email"
                        required
                        placeholder="mario@acme.com"
                        className="form-input"
                      />
                    </div>
                  </div>

                  <div className="form-field">
                    <label htmlFor="obiettivo">Cosa ti interessa vedere?</label>
                    <select
                      id="obiettivo"
                      name="obiettivo"
                      required
                      className="form-input form-select"
                      value={obiettivo}
                      onChange={(e) => setObiettivo(e.target.value)}
                    >
                      <option value="" disabled>
                        Seleziona...
                      </option>
                      <option value="strategy-call">Demo Outreach Workflow</option>
                      <option value="content-workflow">Demo Content Workflow</option>
                      <option value="entrambi">Entrambi i workflow</option>
                      <option value="landing-nuova">Landing Page Premium</option>
                      <option value="strategy">Consulenza strategica</option>
                    </select>
                  </div>

                  <div className="form-field">
                    <label htmlFor="dettagli">Il tuo business in 2 righe</label>
                    <textarea
                      id="dettagli"
                      name="dettagli"
                      rows={4}
                      placeholder="Cosa vendi, a chi, e qual è il task che ti toglie più tempo ogni giorno..."
                      className="form-input form-textarea"
                    />
                  </div>

                  {error && (
                    <p className="text-[0.88rem] text-[#DC2F37]">{error}</p>
                  )}

                  <MagneticButton intensity={0.10}>
                    <button
                      type="submit"
                      disabled={submitting}
                      className="btn-gold btn-gold--lg w-full justify-center group disabled:opacity-60 disabled:cursor-not-allowed"
                    >
                      {submitting ? (
                        "Invio in corso..."
                      ) : (
                        <>
                          Prenota la demo gratuita
                          <Send className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                        </>
                      )}
                    </button>
                  </MagneticButton>

                  <p className="text-[0.78rem] text-white/40 text-center">
                    Demo gratuita · Nessun impegno · Risposta entro 24h
                  </p>
                </form>
              ) : (
                <div className="text-center py-10">
                  <span
                    className="grid place-items-center w-16 h-16 rounded-full mx-auto mb-6"
                    style={{
                      background:
                        "linear-gradient(135deg, #fb4604 0%, #c93a0a 100%)",
                      boxShadow:
                        "0 0 40px rgba(201,55,10,0.40), inset 0 1px 0 rgba(255,255,255,0.30)",
                    }}
                  >
                    <Check className="h-8 w-8 text-white" strokeWidth={3} />
                  </span>
                  <h3 className="text-[1.50rem] font-bold text-white mb-3">
                    Richiesta ricevuta
                  </h3>
                  <p className="text-[0.96rem] text-white/65 leading-relaxed max-w-sm mx-auto">
                    Ti contattiamo entro 24 ore per fissare la demo live.
                    Controlla anche lo spam.
                  </p>
                  <a
                    href="mailto:hq@digitalempire.team"
                    className="inline-flex items-center gap-2 mt-6 text-[0.92rem] text-gold-pure hover:text-gold-bright transition-colors group"
                  >
                    <Mail className="h-4 w-4" />
                    hq@digitalempire.team
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </a>
                </div>
              )}
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
