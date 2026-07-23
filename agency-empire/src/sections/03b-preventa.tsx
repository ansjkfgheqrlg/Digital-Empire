"use client";

/*
Owner: 01-AGENCY
Controllore: A10-QA-Cliente
Origine: FORGE (Gael)
Governo: MANDATO Art.8 + ADR-008
*/

import {
  Car,
  Timer,
  Lock,
  Unplug,
  Check,
  ArrowRight,
  FileDown,
} from "lucide-react";
import { Reveal } from "@/components/reveal";

/* ============================================================
   PREZZO — DEC-EST-005 (attivazione €490 + canone €149/mese).
   Il veto M-EST-4 di Max è ancora aperto: se il prezzo cambia,
   si tocca SOLO questo blocco. Con MOSTRA_PREZZO = false la
   cifra sparisce dalla pagina e si rimanda alla demo.
   ============================================================ */
const MOSTRA_PREZZO = true;
const PREZZO_ATTIVAZIONE = "490";
const PREZZO_CANONE = "149";

const BENEFICI = [
  {
    icon: Timer,
    tag: "Velocità",
    h: "Il preventivo parte mentre il cliente è ancora caldo.",
    body:
      "Il venditore incolla il link dell'annuncio e preme Genera. In circa due minuti esce un PDF impaginato con la grafica della concessionaria, pronto da mandare su WhatsApp.",
    foot: "Link → PDF brandizzato, senza passare da Excel",
  },
  {
    icon: Lock,
    tag: "Controllo",
    h: "Il titolare fissa le regole di prezzo. Il venditore non le tocca.",
    body:
      "Ricarico, costi di messa su strada e margine sono impostati una volta nella configurazione del salone e applicati a ogni preventivo. Il venditore vede il prezzo finale, non lo modifica.",
    foot: "Stesse regole su ogni PDF, nessun conto a mano",
  },
  {
    icon: Unplug,
    tag: "Autonomia",
    h: "Non un'altra agenzia. Uno strumento vostro.",
    body:
      "Non pagate a preventivo e non aspettate un grafico. È un software che gira sul PC del salone, a canone fisso, che disdite quando volete.",
    foot: "Licenza a canone con kill-switch remoto, zero vincoli lunghi",
  },
];

const STEP = [
  {
    n: "01",
    t: "Incollate il link dell'annuncio",
    d: "Anche da portali in tedesco: scheda tecnica, equipaggiamento e foto vengono lette e riportate in italiano.",
  },
  {
    n: "02",
    t: "Il prezzo si calcola da solo",
    d: "Le regole del salone — ricarico, messa su strada, margine — sono già dentro. Il prezzo finale finisce anche nel titolo del preventivo.",
  },
  {
    n: "03",
    t: "Esce il PDF pronto da inviare",
    d: "Impaginato con logo e colori del salone, foto complete mai tagliate, equipaggiamento, garanzia e totale in strada IVA inclusa.",
  },
];

const INCLUSO = [
  "App desktop brandizzata con logo e colori della concessionaria",
  "Traduzione in italiano di scheda tecnica ed equipaggiamento",
  "Regole di prezzo del salone applicate a ogni preventivo",
  "Sei controlli automatici prima che il PDF venga emesso",
  "Storico dei preventivi generati, salvato sul PC del salone",
  "Aggiornamenti del motore inclusi nel canone",
];

const GRAIN = (seed: string, freq = "1.35") =>
  `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='${freq}' numOctaves='3' stitchTiles='stitch' seed='${seed}'/><feColorMatrix values='0 0 0 0 0.90 0 0 0 0 0.88 0 0 0 0 0.86 0 0 0 0.28 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")`;

export function Preventa() {
  return (
    <section
      id="preventa"
      className="bg-ink-2 section relative overflow-hidden"
      aria-labelledby="preventa-h2"
    >
      <div className="container-wide">
        {/* ── HEADER ── */}
        <Reveal>
          <div className="text-center mb-12 max-w-3xl mx-auto">
            <span className="bubble-silver">
              <Car className="h-3.5 w-3.5" />
              Settore verticale — Concessionari auto
            </span>
            <h2 id="preventa-h2" className="mt-6">
              <span className="text-silver-white">Preventa:</span>{" "}
              <span className="text-silver-gold font-accent italic">
                il preventivo che chiude.
              </span>{" "}
              <span className="text-silver-white">
                In due minuti, non in trenta.
              </span>
            </h2>
            <p className="mt-5 text-[1.0625rem] text-white/85 leading-relaxed font-light">
              Il venditore perde mezz&apos;ora tra gestionale, Excel e copia-incolla.
              Il cliente, intanto, ha già scritto ad altri tre saloni su WhatsApp.
              Preventa toglie di mezzo quella mezz&apos;ora.
            </p>
          </div>
        </Reveal>

        {/* ── NOTA DI POSIZIONAMENTO — separa il tier dai workflow su misura ── */}
        <Reveal delay={0.08}>
          <div
            className="max-w-3xl mx-auto mb-14 rounded-2xl px-6 py-5 text-center"
            style={{
              border: "1px dashed rgba(255,255,255,0.20)",
              background: "rgba(255,255,255,0.03)",
            }}
          >
            <p className="text-[0.94rem] leading-relaxed text-white/70 font-light">
              <span className="font-semibold text-white/90">
                Non è uno dei workflow su misura qui sopra.
              </span>{" "}
              Quelli si progettano sul processo di un&apos;azienda specifica. Preventa è
              l&apos;opposto: un software già fatto, per un mestiere solo, a canone fisso.
              Sta in questa pagina perché nasce dallo stesso motore, non perché sia lo
              stesso servizio.
            </p>
          </div>
        </Reveal>

        {/* ── 3 BENEFICI ── */}
        <div className="grid md:grid-cols-3 gap-5 mb-5">
          {BENEFICI.map((b, i) => {
            const Icon = b.icon;
            return (
              <Reveal key={b.tag} delay={0.10 + i * 0.08}>
                <article className="card-dark h-full flex flex-col">
                  <div className="flex items-center gap-3 mb-5">
                    <span
                      className="grid place-items-center w-11 h-11 rounded-xl shrink-0"
                      style={{
                        background:
                          "linear-gradient(135deg, rgba(251,70,4,0.28) 0%, rgba(201,55,10,0.42) 100%)",
                        border: "1px solid rgba(251,70,4,0.40)",
                        boxShadow:
                          "0 6px 18px rgba(100,20,0,0.38), inset 0 1px 0 rgba(255,255,255,0.18)",
                      }}
                    >
                      <Icon className="h-5 w-5 text-gold-pure" />
                    </span>
                    <span className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-white/50">
                      {b.tag}
                    </span>
                  </div>

                  <h3 className="text-[1.15rem] font-bold text-white leading-snug mb-3">
                    {b.h}
                  </h3>
                  <p className="text-[0.92rem] leading-relaxed text-white/80 font-light mb-5 flex-1">
                    {b.body}
                  </p>

                  <p className="text-[0.8rem] text-white/55 pt-4 border-t border-white/10">
                    {b.foot}
                  </p>
                </article>
              </Reveal>
            );
          })}
        </div>

        {/* ── COME FUNZIONA + PREZZO ── */}
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-5 items-stretch">
          {/* COME FUNZIONA */}
          <Reveal delay={0.14} className="lg:col-span-3">
            <div
              className="h-full rounded-[22px] p-7 md:p-9"
              style={{
                position: "relative",
                isolation: "isolate",
                border: "1px solid rgba(251,70,4,0.32)",
                color: "#ffffff",
                background: [
                  GRAIN("21"),
                  "radial-gradient(75% 55% at 5% 8%, rgba(255,255,255,0.28) 0%, transparent 48%)",
                  "linear-gradient(145deg, #1a0800 0%, #2d1200 20%, #6a2200 46%, #a83400 70%, #050505 100%)",
                ].join(", "),
                backgroundSize: "200px 200px, 100% 100%, 100% 100%",
                backgroundBlendMode: "screen, normal, normal",
                boxShadow: [
                  "0 60px 110px -28px rgba(0,0,30,0.88)",
                  "0 2px 0 rgba(255,255,255,0.30) inset",
                  "0 -2px 0 rgba(0,0,20,0.60) inset",
                ].join(", "),
              }}
            >
              <span className="bubble-gold !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                Come funziona
              </span>

              <h3 className="mt-5 mb-7 text-[1.5rem] md:text-[1.75rem] font-bold leading-tight text-white">
                Da annuncio a preventivo inviabile, in tre mosse.
              </h3>

              <ol className="flex flex-col gap-6">
                {STEP.map((s) => (
                  <li key={s.n} className="flex items-start gap-4">
                    <span
                      className="grid place-items-center w-10 h-10 rounded-xl shrink-0 font-display font-bold text-[0.9rem]"
                      style={{
                        background: "rgba(0,0,0,0.30)",
                        border: "1px solid rgba(255,255,255,0.22)",
                        color: "#ffb284",
                      }}
                    >
                      {s.n}
                    </span>
                    <div>
                      <h4 className="text-[1.02rem] font-semibold text-white mb-1">
                        {s.t}
                      </h4>
                      <p className="text-[0.9rem] leading-relaxed text-white/80 font-light">
                        {s.d}
                      </p>
                    </div>
                  </li>
                ))}
              </ol>

              <p className="mt-8 pt-5 border-t border-white/20 text-[0.85rem] text-white/70 font-light">
                Nasce per venditori, non per informatici. Gira sul PC del salone e non
                sostituisce il gestionale: gli si affianca. Nessun server da gestire,
                nessuna migrazione di dati.
              </p>
            </div>
          </Reveal>

          {/* PREZZO */}
          <Reveal delay={0.20} className="lg:col-span-2">
            <div className="card-silver-gold h-full flex flex-col">
              <span className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-[#c93a0a] block mb-4">
                Licenza a canone
              </span>

              {MOSTRA_PREZZO ? (
                <>
                  <div className="flex items-baseline gap-2">
                    <span className="font-display text-[3rem] leading-none font-bold text-[#1c1c1c]">
                      €{PREZZO_CANONE}
                    </span>
                    <span className="text-[0.95rem] font-medium text-[#1c1c1c]/60">
                      / mese
                    </span>
                  </div>
                  <p className="mt-2 text-[0.9rem] text-[#1c1c1c]/70">
                    più €{PREZZO_ATTIVAZIONE} una tantum di attivazione: configurazione
                    della concessionaria, logo, regole di prezzo e consegna dell&apos;app.
                  </p>
                </>
              ) : (
                <>
                  <div className="font-display text-[2rem] leading-tight font-bold text-[#1c1c1c]">
                    Canone fisso mensile
                  </div>
                  <p className="mt-2 text-[0.9rem] text-[#1c1c1c]/70">
                    Più una quota di attivazione una tantum. Cifra esatta in demo, sulla
                    dimensione del vostro salone.
                  </p>
                </>
              )}

              <ul className="flex flex-col gap-2.5 my-7">
                {INCLUSO.map((v) => (
                  <li
                    key={v}
                    className="flex items-start gap-2.5 text-[0.875rem] text-[#1c1c1c]/85"
                  >
                    <Check
                      className="h-4 w-4 mt-0.5 shrink-0 text-[#c93a0a]"
                      strokeWidth={2.5}
                    />
                    <span>{v}</span>
                  </li>
                ))}
              </ul>

              <div className="mt-auto">
                <a href="/prenota" className="btn-gold w-full justify-center group">
                  Demo su una vostra auto — 15 min
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </a>
                <p className="mt-3 text-center text-[0.8rem] text-[#1c1c1c]/55">
                  Schermo condiviso, un&apos;auto che avete davvero in salone. Nessuna slide.
                </p>
              </div>
            </div>
          </Reveal>
        </div>

        {/* ── PONTE ALLA SEZIONE PROVE ── */}
        <Reveal delay={0.26}>
          <div className="mt-10 text-center">
            <a
              href="#prove"
              className="inline-flex items-center gap-2 text-[0.95rem] font-semibold text-gold-pure group hover:gap-3 transition-all"
            >
              <FileDown className="h-4 w-4" />
              Guardate cosa produce davvero: 65 preventivi reali
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </a>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
