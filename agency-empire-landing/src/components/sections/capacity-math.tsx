"use client";

import { Reveal } from "@/components/reveal";
import { Divide } from "lucide-react";

/** S2 (formula per una parola inflazionata) fusa con A8 (cosa costa NON farlo):
 *  erano due sezioni di aritmetica sullo stesso tema — una sola, piu' forte.
 *  I numeri sono dichiarati come esempio, non come risultato di un cliente. */
const bars = [
  { label: "Oggi, a mano", value: 12, unit: "lead lavorati / giorno", tone: "grey" as const },
  { label: "Con il sistema", value: 60, unit: "lead lavorati / giorno", tone: "orange" as const },
];

export function CapacityMath() {
  const max = Math.max(...bars.map((b) => b.value));

  return (
    <section className="bg-ink-2 section section-border-t">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-12">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Divide className="h-3.5 w-3.5" /> Ed è calcolabile
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-white">&ldquo;Automatizzare&rdquo; non è una parola. </span>
              <span className="text-orange-pure italic font-medium">È una divisione.</span>
            </h2>
          </Reveal>
        </div>

        <Reveal delay={0.15}>
          <div
            className="rounded-xl px-6 py-8 md:px-10 md:py-10 text-center mb-10"
            style={{
              background: "rgba(249,249,249,0.035)",
              border: "1px solid rgba(249,249,249,0.10)",
            }}
          >
            <p
              className="text-[18px] md:text-[26px] font-bold text-silver-white leading-snug"
              style={{ fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace" }}
            >
              capacità <span className="text-orange-pure">=</span> lavoro utile{" "}
              <span className="text-orange-pure">/</span> ore-persona
            </p>
            <p className="text-white/60 text-[13px] mt-4 leading-relaxed max-w-xl mx-auto">
              Assumere alza il numeratore e il denominatore insieme. Un sistema alza solo il
              numeratore. È tutta qui la differenza, e si misura.
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.25}>
          <div className="flex flex-col gap-6 mb-10">
            {bars.map((b) => (
              <div key={b.label}>
                <div className="flex items-baseline justify-between mb-2">
                  <span className="text-[11px] uppercase tracking-[0.2em] font-black text-white/60">
                    {b.label}
                  </span>
                  <span
                    className="text-[13px] font-bold tabular-nums"
                    style={{
                      fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace",
                      color: b.tone === "orange" ? "#fb4604" : "rgba(249,249,249,0.6)",
                    }}
                  >
                    {b.value} {b.unit}
                  </span>
                </div>
                <div
                  className="h-9 rounded-full overflow-hidden"
                  style={{ background: "rgba(249,249,249,0.05)" }}
                >
                  <div
                    className="h-full rounded-full"
                    style={{
                      width: `${(b.value / max) * 100}%`,
                      background:
                        b.tone === "orange"
                          ? "linear-gradient(90deg, #fb4604 0%, #ff6a2e 100%)"
                          : "rgba(249,249,249,0.22)",
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </Reveal>

        <Reveal delay={0.35}>
          <div
            className="rounded-xl px-7 py-7"
            style={{
              background:
                "linear-gradient(160deg, rgba(251,70,4,0.10) 0%, rgba(251,70,4,0.02) 70%, transparent 100%)",
              border: "1px solid rgba(251,70,4,0.36)",
            }}
          >
            <p className="text-[11px] uppercase tracking-[0.2em] font-black text-orange-pure mb-3">
              Cosa costa non farlo
            </p>
            <p className="text-white/90 text-[15px] leading-relaxed">
              Le stesse ore, ogni mese, per sempre — e non lasciano niente dietro. Un canone almeno
              te lo ricordi quando arriva l&apos;estratto conto; le ore del tuo team non compaiono da
              nessuna parte, e sono la voce di costo più alta che hai.{" "}
              <span className="text-orange-pure font-semibold">
                Non decidere è già una decisione: è scegliere di pagarle un altro anno.
              </span>
            </p>
            <p className="text-white/30 text-[12px] leading-relaxed mt-5">
              I numeri delle barre sono un esempio con cifre tonde, non il risultato di un cliente.
              Nella call li rifacciamo con i tuoi.
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
