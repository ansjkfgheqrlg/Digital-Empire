"use client";

import {
  ArrowRight,
  ArrowLeft,
  ArrowUpRight,
  Check,
  CheckCircle2,
  Lock,
  Mail,
  MailCheck,
  Sparkles,
  ShieldCheck,
  GraduationCap,
  Zap,
} from "lucide-react";
import { Reveal } from "@/components/reveal";
import { useEffect, useRef, useState } from "react";

const STRIPE_URL = "https://buy.stripe.com/4gM8wRfAi4Zi6wn6Ardby01";
const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";

const WINDOW_MS = 48 * 60 * 60 * 1000;
const KEY = "ccm_offer_start";

function useCountdown() {
  const [remaining, setRemaining] = useState<number | null>(null);

  useEffect(() => {
    let start = parseInt(localStorage.getItem(KEY) || "0", 10);
    if (!start || Number.isNaN(start)) {
      start = Date.now();
      try {
        localStorage.setItem(KEY, String(start));
      } catch {}
    }
    const end = start + WINDOW_MS;

    const tick = () => {
      const diff = end - Date.now();
      setRemaining(Math.max(0, diff));
    };

    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  if (remaining === null) {
    return { hours: "48", minutes: "00", seconds: "00", expired: false };
  }

  const expired = remaining <= 0;
  const hours = Math.floor(remaining / 3_600_000);
  const minutes = Math.floor((remaining % 3_600_000) / 60_000);
  const seconds = Math.floor((remaining % 60_000) / 1_000);

  const pad = (n: number) => String(n).padStart(2, "0");
  return { hours: pad(hours), minutes: pad(minutes), seconds: pad(seconds), expired };
}

export default function ThankYouPage() {
  const { hours, minutes, seconds, expired } = useCountdown();
  const skipRef = useRef<HTMLDivElement>(null);
  const [skipShown, setSkipShown] = useState(false);

  const onSkip = () => {
    setSkipShown(true);
    setTimeout(() => {
      skipRef.current?.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 100);
  };

  return (
    <main className="relative z-10 pb-24 bg-[#1c1c1c] min-h-screen">
      {/* CONFIRMATION HERO */}
      <section className="max-w-3xl mx-auto px-6 pt-16 md:pt-24 text-center">
        <Reveal>
          <span className="bubble-orange mb-6">
            <CheckCircle2 className="h-3.5 w-3.5" /> Richiesta Confermata
          </span>
        </Reveal>
        <Reveal delay={0.05}>
          <div className="pre-headline mt-4 mb-4">Ottimo lavoro</div>
        </Reveal>
        <Reveal delay={0.1}>
          <h1 className="text-4xl md:text-6xl font-bold leading-[1.05] mt-2 mb-6">
            <span className="text-silver-white">L&apos;ebook è in viaggio.</span>
            <br />
            <span className="text-silver-orange">Controlla la tua inbox.</span>
          </h1>
        </Reveal>
        <Reveal delay={0.15}>
          <div className="card-dark !p-6 md:!p-8 text-left mt-4 max-w-xl mx-auto">
            <div className="flex items-start gap-4">
              <div className="w-11 h-11 shrink-0 rounded-xl bg-[#fb4604]/15 border border-[#fb4604]/30 flex items-center justify-center">
                <MailCheck className="w-5 h-5 text-[#ff6a2e]" />
              </div>
              <div>
                <h2 className="text-lg md:text-xl font-bold text-white mb-2">
                  Claude Code Mastery in arrivo
                </h2>
                <p className="text-white/70 text-[15px] leading-relaxed font-light">
                  Entro i prossimi <strong className="text-white">5 minuti</strong>{" "}
                  riceverai un&apos;email con il link per scaricare l&apos;ebook. Se non
                  lo vedi, controlla <strong className="text-white">Spam</strong> o{" "}
                  <strong className="text-white">Promozioni</strong>.
                </p>
              </div>
            </div>
          </div>
        </Reveal>
      </section>

      {/* DIVIDER */}
      <div className="max-w-xs mx-auto my-16 flex items-center gap-4">
        <div className="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />
        <Sparkles className="w-4 h-4 text-[#ff6a2e]" />
        <div className="flex-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />
      </div>

      {/* MASTERCLASS OFFER */}
      <section className="max-w-4xl mx-auto px-6">
        <Reveal>
          <div className="text-center mb-8">
            <span className="bubble-silver mb-5 text-xs">
              <span className="w-2 h-2 rounded-full bg-[#fb4604] pulse-dot" />
              OFFERTA RISERVATA · DISPONIBILE SOLO ORA
            </span>
            <h2 className="text-[34px] md:text-[52px] font-bold leading-[1.08] mt-6 mb-4">
              <span className="text-silver-white">Prima di andare,</span>
              <br />
              <span className="text-silver-orange">hai 48 ore per questo.</span>
            </h2>
            <p className="text-white/65 max-w-2xl mx-auto text-lg font-light leading-relaxed">
              Abbiamo costruito una{" "}
              <strong className="text-silver-orange font-semibold">
                Masterclass live-replay di 3+ ore
              </strong>{" "}
              dedicata interamente a Claude Code.{" "}
              <span className="hl-block">
                Prendiamo ogni argomento dell&apos;ebook e lo mostriamo in pratica
              </span>
              , a schermo condiviso, pagina dopo pagina.
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.15}>
          <div className="card-offer">
            <div className="absolute top-[-40px] right-[-20px] text-[220px] leading-none font-black italic tracking-tighter opacity-[0.03] select-none pointer-events-none">
              CCM
            </div>

            <div className="relative z-10 grid md:grid-cols-[1.2fr_auto] gap-10 items-start">
              <div>
                <div className="flex items-center gap-3 mb-5">
                  <span className="bubble-orange text-[11px] py-1 px-3">
                    MASTERCLASS
                  </span>
                  <span className="text-[11px] font-bold uppercase tracking-[0.2em] text-white/50">
                    Solo 15 €
                  </span>
                </div>
                <h3 className="text-2xl md:text-4xl font-black leading-[1.1] mb-5 text-silver-white">
                  Claude Code Mastery ·{" "}
                  <span className="text-silver-orange">Masterclass Pratica</span>
                </h3>
                <p className="text-white/70 text-[15px] md:text-base leading-relaxed font-light mb-6">
                  <strong className="text-white">
                    3+ ore di formazione densa
                  </strong>
                  , interamente su Claude Code. Ogni concetto dell&apos;ebook viene{" "}
                  <strong className="text-white">mostrato a schermo</strong>,
                  applicato su progetti reali, commentato live. Zero teoria
                  astratta.
                </p>
                <ul className="space-y-3">
                  {[
                    "3+ ore di masterclass · ogni capitolo dell'ebook, applicato in pratica.",
                    "Schermo condiviso · comandi reali, hook, skill, agent che funzionano.",
                    "Accesso immediato appena completi il pagamento.",
                    "Valore estremo a un prezzo simbolico di 15 €.",
                  ].map((t, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-3 text-[15px] text-white/80"
                    >
                      <div className="w-5 h-5 rounded bg-[#fb4604]/15 border border-[#fb4604]/40 flex items-center justify-center shrink-0 mt-0.5">
                        <Check className="w-3 h-3 text-[#ff6a2e]" />
                      </div>
                      <span>{t}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Countdown + price */}
              <div className="md:border-l md:border-white/10 md:pl-10 w-full md:w-auto md:min-w-[260px]">
                <div className="text-center mb-6">
                  <div className="text-[11px] uppercase tracking-[0.22em] text-white/55 font-bold mb-4 flex items-center justify-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-[#fb4604] pulse-dot" />
                    Offerta scade in
                  </div>
                  <div
                    className={`flex items-center justify-center gap-2 ${
                      expired ? "opacity-50" : ""
                    }`}
                  >
                    <div className="cd-box">
                      <div className="cd-value">{hours}</div>
                      <div className="cd-label">ORE</div>
                    </div>
                    <div className="cd-box">
                      <div className="cd-value">{minutes}</div>
                      <div className="cd-label">MIN</div>
                    </div>
                    <div className="cd-box">
                      <div className="cd-value">{seconds}</div>
                      <div className="cd-label">SEC</div>
                    </div>
                  </div>
                  {expired && (
                    <p className="mt-4 text-[13px] text-white/60">
                      L&apos;offerta è terminata. Ci vediamo al corso.
                    </p>
                  )}
                </div>
                <div className="text-center">
                  <div className="text-[11px] uppercase tracking-[0.22em] text-white/45 font-bold mb-1">
                    Prezzo masterclass
                  </div>
                  <div className="flex items-end justify-center gap-2">
                    <span className="text-[64px] leading-none font-black text-silver-white">
                      15
                    </span>
                    <span className="text-2xl font-bold text-white/70 mb-2">
                      €
                    </span>
                  </div>
                  <div className="text-[12px] text-white/40 mt-1">
                    pagamento sicuro · Stripe
                  </div>
                </div>
              </div>
            </div>

            {/* CTAs */}
            <div className="relative z-10 mt-10 pt-8 border-t border-white/10 flex flex-col gap-4">
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                {expired ? (
                  <button
                    className="btn-orange flex-1 md:flex-none md:min-w-[320px] text-center opacity-55 cursor-not-allowed"
                    disabled
                  >
                    <Lock className="w-5 h-5" />
                    Offerta terminata
                  </button>
                ) : (
                  <a
                    href={STRIPE_URL}
                    className="btn-orange btn-orange--lg flex-1 md:flex-none md:min-w-[320px] justify-center"
                  >
                    <Zap className="w-5 h-5" />
                    OK, voglio la Masterclass
                  </a>
                )}
                <button
                  onClick={onSkip}
                  className="btn-ghost flex-1 md:flex-none md:min-w-[260px] justify-center"
                >
                  No, mi basta l&apos;ebook
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>

              <div className="flex justify-center pt-2">
                <a
                  href={COURSE_URL}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-ghost text-sm py-3 px-6"
                >
                  <GraduationCap className="w-4 h-4" />
                  Scopri il corso{" "}
                  <span className="hidden sm:inline">
                    Da AI User a System Architect
                  </span>
                  <ArrowUpRight className="w-3.5 h-3.5" />
                </a>
              </div>

              <p className="text-center text-[12px] text-white/40 mt-2 flex items-center justify-center gap-1.5">
                <ShieldCheck className="inline w-3.5 h-3.5" />
                Pagamento sicuro su Stripe · accesso immediato alla masterclass
              </p>
            </div>
          </div>
        </Reveal>
      </section>

      {/* SKIP CONFIRMATION */}
      {skipShown && (
        <section
          ref={skipRef}
          className="max-w-2xl mx-auto px-6 mt-20 text-center"
        >
          <Reveal>
            <div className="card-dark">
              <div className="w-12 h-12 mx-auto rounded-full bg-white/5 border border-white/15 flex items-center justify-center mb-5">
                <Mail className="w-5 h-5 text-white/70" />
              </div>
              <h3 className="text-2xl font-bold text-silver-white mb-3">
                Nessun problema.
              </h3>
              <p className="text-white/65 font-light leading-relaxed mb-6">
                Goditi l&apos;ebook{" "}
                <strong className="text-white">Claude Code Mastery</strong>. Se
                vorrai approfondire più in là, la masterclass e il corso{" "}
                <strong className="text-white">
                  Da AI User a System Architect
                </strong>{" "}
                saranno lì per te.
              </p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <a
                  href={COURSE_URL}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-ghost justify-center"
                >
                  Scopri il corso completo
                  <ArrowUpRight className="w-3.5 h-3.5" />
                </a>
                <a href="/" className="btn-ghost justify-center">
                  <ArrowLeft className="w-4 h-4" />
                  Torna alla home
                </a>
              </div>
            </div>
          </Reveal>
        </section>
      )}

      <footer className="py-10 mt-20 text-center text-white/30 text-xs tracking-widest uppercase font-medium border-t border-white/5">
        © 2026 Digital Empire Labs
      </footer>
    </main>
  );
}
