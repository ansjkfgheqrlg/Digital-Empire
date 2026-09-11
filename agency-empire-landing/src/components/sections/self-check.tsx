"use client";

import { useState } from "react";
import { Reveal } from "@/components/reveal";
import { ClipboardCheck } from "lucide-react";

/** Micro-sondaggio di auto-diagnosi.
 *  Chi clicca "mi ritrovo" si e' appena dichiarato il problema da solo:
 *  da li' in poi la pagina non deve piu' convincerlo che il problema esiste.
 *  L'evento viene inoltrato a GA4 se presente (F1-E3), altrimenti e' inerte. */
const steps = [
  "Un lead arriva dal sito o dai social",
  "Qualcuno del team lo cerca a mano, uno per uno",
  "Scrive il messaggio, lo personalizza, lo invia",
  "Il giorno dopo ricomincia da capo",
];

type Answer = "si" | "no" | null;

export function SelfCheck() {
  const [answer, setAnswer] = useState<Answer>(null);

  function choose(value: Exclude<Answer, null>) {
    setAnswer(value);
    if (typeof window !== "undefined") {
      const w = window as unknown as { gtag?: (...a: unknown[]) => void };
      w.gtag?.("event", "self_check", { risposta: value });
    }
  }

  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-3xl mx-auto px-6">
        <div className="text-center mb-10">
          <Reveal>
            <span className="bubble-orange mb-6">
              <ClipboardCheck className="h-3.5 w-3.5" /> Dimmi se ti ritrovi
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[30px] md:text-[42px] font-bold leading-tight mt-6">
              <span className="text-silver-white">La tua giornata assomiglia </span>
              <span className="text-orange-pure italic font-medium">a questa?</span>
            </h2>
          </Reveal>
        </div>

        <Reveal delay={0.2}>
          <ol className="flex flex-col gap-3 mb-10">
            {steps.map((s, i) => (
              <li
                key={i}
                className="flex items-start gap-4 rounded-xl px-5 py-4"
                style={{
                  background: "rgba(249,249,249,0.035)",
                  border: "1px solid rgba(249,249,249,0.09)",
                }}
              >
                <span
                  className="shrink-0 text-[11px] font-black tabular-nums mt-[3px] text-orange-pure"
                  style={{ fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace" }}
                >
                  0{i + 1}
                </span>
                <span className="text-white/75 text-[15px] leading-relaxed">{s}</span>
              </li>
            ))}
          </ol>
        </Reveal>

        <Reveal delay={0.3}>
          {answer === null ? (
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <button
                type="button"
                onClick={() => choose("si")}
                className="btn-orange"
              >
                Sì, mi ritrovo
              </button>
              <button
                type="button"
                onClick={() => choose("no")}
                className="rounded-xl px-7 py-4 text-[14px] font-bold uppercase tracking-[0.14em] text-white/60 transition-colors hover:text-white"
                style={{ border: "1px solid rgba(249,249,249,0.22)" }}
              >
                No, non mi ritrovo
              </button>
            </div>
          ) : (
            <div
              className="rounded-xl px-7 py-7 text-center"
              style={{
                background:
                  "linear-gradient(160deg, rgba(251,70,4,0.10) 0%, rgba(251,70,4,0.02) 70%, transparent 100%)",
                border: "1px solid rgba(251,70,4,0.38)",
              }}
              role="status"
            >
              {answer === "si" ? (
                <p className="text-white/90 text-[16px] leading-relaxed">
                  Allora il problema non è la tua bravura: è che{" "}
                  <span className="text-orange-pure font-semibold">
                    quelle quattro righe sono un lavoro che una macchina fa meglio di una persona
                  </span>
                  , tutti i giorni, senza stancarsi. Il resto di questa pagina è come lo togliamo dal
                  tuo calendario.
                </p>
              ) : (
                <p className="text-white/90 text-[16px] leading-relaxed">
                  Buon segno — vuol dire che qualcosa di strutturato ce l&apos;hai già. La domanda
                  utile allora è un&apos;altra:{" "}
                  <span className="text-orange-pure font-semibold">
                    quel processo gira anche quando tu non ci sei?
                  </span>
                </p>
              )}
            </div>
          )}
        </Reveal>
      </div>
    </section>
  );
}
