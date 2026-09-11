"use client";

import { Reveal } from "@/components/reveal";
import { X, Check, FastForward } from "lucide-react";

const out = [
  "SaaS a canone mensile che smette di funzionare se smetti di pagare",
  "Tool generici addestrati su milioni di aziende — non sulla tua",
  "Mesi di consulenza prima di vedere un risultato",
  "Abbonamenti multipli per fare quello che un sistema solo può fare",
  "Dipendenza da terze parti per dati, lead e contenuti",
];

const inList = [
  "Codice sorgente in chiaro — asset aziendale tuo per sempre",
  "Sistema calibrato sul tuo brand, ICP e framework copy APSOC",
  "Setup completo in 7 giorni. Poi il sistema gira da solo",
  "Zero canoni mensili dopo il setup (solo costi API minimi a consumo)",
  "90 giorni di supporto tecnico dedicato inclusi nel pacchetto",
];

export function NoFluff() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">
              <FastForward className="h-3.5 w-3.5" /> Zero SaaS // Proprietà totale
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Non vendiamo abbonamenti. </span>
              <span className="text-orange-pure italic font-medium" style={{ whiteSpace: "nowrap" }}>Vendiamo asset.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#1c1c1c]/72 text-lg max-w-3xl mx-auto mt-6 leading-relaxed">
              Un SaaS ti chiede €200 al mese per sempre. Noi installiamo una volta,{" "}
              <strong className="text-silver-black">poi il sistema è tuo</strong>. Nessun canone ricorrente dopo il setup.
              Solo costi API minimi a consumo (pochi centesimi per operazione).{" "}
              <span className="text-orange-pure font-semibold">È matematica, non marketing.</span>
            </p>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          <Reveal delay={0.2}>
            <div
              className="rounded-xl p-7 h-full"
              style={{
                background: "linear-gradient(160deg, #ffffff 0%, #f1ede6 100%)",
                border: "1px solid rgba(28,28,28,0.12)",
                boxShadow: "0 10px 30px -15px rgba(0,0,0,0.15)",
              }}
            >
              <div className="flex items-center gap-2 mb-5">
                <span className="inline-block w-6 h-[2px] bg-[#1c1c1c]/50" />
                <span className="text-[11px] uppercase tracking-[0.18em] font-black text-[#1c1c1c]/72">
                  Quello che NON trovi qui
                </span>
              </div>
              <ul className="space-y-3">
                {out.map((o, i) => (
                  <li key={i} className="flex items-start gap-3 text-[#1c1c1c]/85 text-[14px] leading-relaxed">
                    <X className="h-4 w-4 text-[#1c1c1c]/40 shrink-0 mt-[3px]" />
                    <span className="line-through decoration-[#1c1c1c]/25">{o}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div
              className="rounded-xl p-7 h-full"
              style={{
                background:
                  "linear-gradient(160deg, rgba(251,70,4,0.08) 0%, rgba(251,70,4,0.02) 60%, transparent 100%)",
                border: "1px solid rgba(251,70,4,0.4)",
                boxShadow: "0 10px 30px -12px rgba(251,70,4,0.25)",
              }}
            >
              <div className="flex items-center gap-2 mb-5">
                <span className="inline-block w-6 h-[2px] bg-orange-pure" />
                <span className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure">
                  Quello che trovi invece
                </span>
              </div>
              <ul className="space-y-3">
                {inList.map((o, i) => (
                  <li key={i} className="flex items-start gap-3 text-[#1c1c1c] text-[14px] leading-relaxed font-medium">
                    <Check className="h-4 w-4 text-orange-pure shrink-0 mt-[3px]" />
                    <span>{o}</span>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>

        <Reveal delay={0.45}>
          <p className="text-center mt-12 text-[13px] uppercase tracking-[0.22em] font-black text-[#1c1c1c]/60">
            <span className="text-orange-pure">→</span> Implementazione reale. Asset permanente. Nessun abbonamento nascosto.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
