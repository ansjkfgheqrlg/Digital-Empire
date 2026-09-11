"use client";

import { Reveal } from "@/components/reveal";
import { Hourglass } from "lucide-react";

/** A9 — "quanto tempo devo dedicarci io?" e' l'obiezione silenziosa numero uno
 *  di chi e' gia' oberato, ed e' la domanda che chiude i clienti B2B.
 *  Rispondiamo con i momenti reali, non con un numero di ore inventato. */
const moments = [
  {
    tag: "Giorno 0",
    title: "Una call di apertura",
    body: "Ci racconti il processo che vuoi togliere dal tuo calendario. Portiamo noi le domande.",
  },
  {
    tag: "Giorno 1",
    title: "Gli accessi e i materiali",
    body: "Ci passi account, brand voice e quello che hai già scritto. Se non esiste, lo ricostruiamo noi.",
  },
  {
    tag: "Giorno 5",
    title: "Una revisione, asincrona",
    body: "Ti mandiamo il sistema che gira sui tuoi dati. Guardi e segni cosa cambiare, quando ti torna comodo.",
  },
  {
    tag: "Giorno 7",
    title: "La consegna",
    body: "Sistema installato, codice tuo, documentazione scritta perché la usi tu, non perché ci richiami.",
  },
];

export function YourTime() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-14">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Hourglass className="h-3.5 w-3.5" /> Il tuo tempo
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Ti serviamo in tre momenti. </span>
              <span className="text-orange-pure italic font-medium">Negli altri, no.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#1c1c1c]/72 text-lg max-w-2xl mx-auto mt-6 leading-relaxed">
              La domanda vera non è quanto costa: è quanto ti costa in{" "}
              <strong className="text-silver-black">attenzione</strong>. Un fornitore che ha bisogno
              di te ogni giorno è un secondo lavoro, non un servizio.
            </p>
          </Reveal>
        </div>

        <div className="flex flex-col gap-3">
          {moments.map((m, i) => (
            <Reveal key={m.tag} delay={0.2 + i * 0.07}>
              <div
                className="rounded-xl px-6 py-6 flex flex-col sm:flex-row sm:gap-8"
                style={{
                  background: "linear-gradient(160deg, #ffffff 0%, #f4f1ea 100%)",
                  border: "1px solid rgba(28,28,28,0.12)",
                }}
              >
                <span
                  className="text-[11px] uppercase tracking-[0.2em] font-black text-orange-pure shrink-0 sm:w-[96px] mb-2 sm:mb-0 sm:pt-1"
                  style={{ fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace" }}
                >
                  {m.tag}
                </span>
                <div>
                  <p className="text-[#1c1c1c] text-[17px] font-bold mb-1.5">{m.title}</p>
                  <p className="text-[#1c1c1c]/72 text-[14px] leading-relaxed">{m.body}</p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={0.5}>
          <p className="text-center mt-12 text-[13px] uppercase tracking-[0.2em] font-black text-[#1c1c1c]/60">
            <span className="text-orange-pure">→</span> Tra un momento e l&apos;altro, il lavoro è nostro
          </p>
        </Reveal>
      </div>
    </section>
  );
}
