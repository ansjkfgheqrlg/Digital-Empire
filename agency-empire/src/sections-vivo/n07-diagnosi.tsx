"use client";

import { useState } from "react";

/* N7 — Diagnosi + micro-sondaggio (speedrun T7): due pulsanti fantasma, stesso ancoraggio.
   Il clic e' micro-commitment, non un bivio. Copy: COPY-V2 §N7. Pattern Fabbrica: micro-sondaggio. */
const SEGNALI = [
  ["Rimandi il follow-up.", "Il lead di martedì lo ricontatti venerdì, se te lo ricordi. Nelle nostre sequenze il 60% delle risposte arriva dal secondo o terzo messaggio: quello che non mandi."],
  ["Pubblichi quando riesci.", "Tre post una settimana, zero la successiva. L'algoritmo premia chi c'è ogni giorno, non chi c'è quando può."],
  ["Copi e incolli.", "Stesso messaggio a trenta persone diverse. Loro se ne accorgono: 3-7% di risposta è il prezzo del template."],
  ["Sai tutto tu.", "Clienti, prezzi, processi: nella tua testa, nelle chat, in cinque cartelle Drive. Il giorno che manchi tu, manca l'azienda."],
];

export function Diagnosi() {
  const [voto, setVoto] = useState<"si" | "no" | null>(null);
  const vota = (v: "si" | "no") => {
    setVoto(v);
    document.getElementById("ascolta-bene")?.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  };

  return (
    <section id="diagnosi" className="sv sv-carta" aria-labelledby="diagnosi-h2">
      <div className="container-default py-16 md:py-20">
        <p className="sv-eyebrow">Dimmi se ti ritrovi</p>
        <h2 id="diagnosi-h2" className="sv-h2 mt-3 max-w-[18ch]">
          I quattro segnali che la tua operatività{" "}
          <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>ti sta mangiando.</span>
        </h2>

        <ol className="mt-10 grid md:grid-cols-2 gap-x-10 gap-y-8 list-none p-0 m-0">
          {SEGNALI.map(([t, d], i) => (
            <li key={t} className="grid grid-cols-[44px_1fr] gap-4 items-start">
              <span
                className="grid place-items-center w-11 h-11 rounded-full sv-stat"
                style={{ background: "var(--sv-orange)", color: "#000", fontSize: 18 }}
                aria-hidden
              >
                {i + 1}
              </span>
              <div>
                <div className="sv-h3" style={{ color: "#1c1c1c" }}>{t}</div>
                <p className="sv-body sv-muted mt-1 max-w-[46ch]">{d}</p>
              </div>
            </li>
          ))}
        </ol>

        <div className="mt-12 flex flex-wrap items-center gap-4">
          <span className="sv-body" style={{ color: "#1c1c1c" }}>Leggi e poi vota: ti ritrovi o no? <span className="sv-muted">(4 segnali, ne basta 1.)</span></span>
          <button type="button" className="sv-btn-ghost" onClick={() => vota("si")} aria-pressed={voto === "si"} data-voto="si">
            Sì, mi ritrovo
          </button>
          <button type="button" className="sv-btn-ghost" onClick={() => vota("no")} aria-pressed={voto === "no"} data-voto="no">
            Non mi ritrovo
          </button>
        </div>
        <p className="sv-small mt-3" style={{ color: "#6f6a62" }}>
          (Se hai cliccato &quot;no&quot; e sei ancora qui: ascolta bene lo stesso.)
        </p>
      </div>
    </section>
  );
}
