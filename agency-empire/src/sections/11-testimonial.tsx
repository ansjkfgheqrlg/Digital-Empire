"use client";

/*
Owner: 01-AGENCY
Controllore: A10-QA-Cliente
Origine: revisione onestà claim (Arena, 2026-07-27)
Governo: MANDATO Art.2 (prove non promesse) + ADR-008

═══════════════════════════════════════════════════════════════════════════
REGOLA DI QUESTA SEZIONE — leggere prima di modificare.

Qui vanno SOLO testimonianze REALI, di persone REALI, che hanno dato il
consenso a essere citate con nome e cognome.

Fino al 2026-07-27 questa sezione conteneva tre testimonianze firmate
"Marco Resta", "Sara Conti", "Luca Pellegrini" con claim precisi
("240 lead qualificati il primo mese", "ho triplicato i contatti").
Nessuno di quei nomi, e nessuno di quei numeri, ha un riscontro in nessun
file di questo repository. L'unico cliente documentato su disco è Novacar
(vedi 09b-prove-novacar.tsx), che è un cliente Preventa.

Sono state rimosse. Al loro posto c'è una dichiarazione onesta.

QUANDO ARRIVA UNA TESTIMONIANZA VERA:
1. serve il consenso scritto della persona (email o messaggio salvato)
2. nome e cognome veri, ruolo vero, azienda vera
3. ogni numero citato dev'essere verificabile su disco
4. si aggiunge a TESTIMONIANZE_REALI qui sotto e la sezione cambia
   automaticamente forma (mostra le card invece della dichiarazione)

Non reintrodurre testimonianze inventate. Se il sito ne aveva bisogno per
"riempire", il problema è la fretta di riempire, non la mancanza di testi.
═══════════════════════════════════════════════════════════════════════════
*/

import { Reveal } from "@/components/reveal";
import { Quote, Star, ShieldCheck, ArrowRight } from "lucide-react";

type Testimonianza = {
  quote: string;
  name: string;
  role: string;
  avatar: string;
};

/* Vuoto per scelta. Vedi il blocco di regole qui sopra. */
const TESTIMONIANZE_REALI: Testimonianza[] = [];

export function Testimonial() {
  const haTestimonianze = TESTIMONIANZE_REALI.length > 0;

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
              {haTestimonianze ? "Voci dei clienti" : "Carte scoperte"}
            </span>
            <h2 id="testi-h2" className="mt-6">
              {haTestimonianze ? (
                <>
                  <span className="text-silver-white">Quello che dicono</span>{" "}
                  <span className="text-silver-gold font-accent italic">
                    di noi.
                  </span>
                </>
              ) : (
                <>
                  <span className="text-silver-white">
                    Qui non c&apos;è ancora
                  </span>{" "}
                  <span className="text-silver-gold font-accent italic">
                    niente da leggere.
                  </span>
                </>
              )}
            </h2>
          </div>
        </Reveal>

        {haTestimonianze ? (
          <div className="grid md:grid-cols-3 gap-6">
            {TESTIMONIANZE_REALI.map((t, i) => (
              <Reveal key={i} delay={0.1 + i * 0.1}>
                <article className="card-dark relative h-full flex flex-col">
                  <Quote
                    className="h-6 w-6 text-gold-pure mb-4"
                    strokeWidth={2}
                  />
                  <p className="font-accent italic text-[1.0625rem] leading-relaxed text-white/85 mb-6 flex-1">
                    &ldquo;{t.quote}&rdquo;
                  </p>
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
                  <div
                    className="flex items-center gap-3 pt-4"
                    style={{ borderTop: "1px solid rgba(255,255,255,0.08)" }}
                  >
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
        ) : (
          /* ── Nessuna testimonianza: lo diciamo, invece di inventarla ── */
          <Reveal delay={0.12}>
            <div
              className="max-w-3xl mx-auto rounded-[22px] px-7 py-8 md:px-10 md:py-10"
              style={{
                border: "1px dashed rgba(255,255,255,0.22)",
                background: "rgba(255,255,255,0.03)",
              }}
            >
              <div className="flex items-start gap-3 mb-5">
                <ShieldCheck className="h-5 w-5 mt-0.5 shrink-0 text-gold-pure" />
                <p className="text-[1.05rem] md:text-[1.125rem] leading-[1.8] text-white/90 font-light">
                  <strong className="font-semibold text-white">
                    Non abbiamo ancora una testimonianza firmata da pubblicare.
                  </strong>{" "}
                  Potremmo scrivere tre virgolettati con nomi credibili e
                  cinque stelle, come fanno quasi tutti. Abbiamo preferito
                  lasciare lo spazio vuoto.
                </p>
              </div>

              <div className="space-y-4 text-[0.98rem] leading-[1.8] text-white/75 font-light">
                <p>
                  Quello che abbiamo è{" "}
                  <strong className="font-medium text-white/90">
                    un cliente reale con numeri contati
                  </strong>
                  : Novacar srl. La macchina che abbiamo costruito per loro ha
                  prodotto 65 preventivi su annunci veri tra il 3 e il 13 luglio
                  2026, su 11 marche diverse, in circa due minuti l&apos;uno.
                  Quei numeri li trovate qui sotto, e in demo ve li facciamo
                  vedere mentre girano.
                </p>
                <p>
                  Quando Novacar — o chi verrà dopo — ci darà una frase da
                  citare,{" "}
                  <strong className="font-medium text-white/90">
                    la pubblicheremo qui con nome, cognome e ruolo veri.
                  </strong>{" "}
                  Fino ad allora questo riquadro resta così.
                </p>
                <p className="text-white/60">
                  Se state valutando un fornitore, il consiglio vale anche
                  contro di noi: chiedete sempre di parlare con un cliente vero.
                  Una testimonianza che non si può verificare non vale la
                  riga su cui è scritta.
                </p>
              </div>

              <div className="mt-7 pt-6 border-t border-white/12 flex flex-col sm:flex-row sm:items-center gap-4 sm:justify-between">
                <p className="text-[0.92rem] text-white/75 font-light">
                  Preferite i numeri alle parole? Sono qui sotto.
                </p>
                <a href="#prove" className="btn-gold group shrink-0">
                  Vedi la prova reale
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </a>
              </div>
            </div>
          </Reveal>
        )}
      </div>
    </section>
  );
}
