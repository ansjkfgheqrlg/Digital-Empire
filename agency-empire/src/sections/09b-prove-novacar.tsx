"use client";

/*
Owner: 01-AGENCY
Controllore: A10-QA-Cliente
Origine: FORGE (Sessione Parallela)
Governo: MANDATO Art.8 + ADR-008
*/

import {
  ShieldCheck,
  FileCheck2,
  ArrowRight,
  ArrowDown,
  Eye,
} from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

/* ============================================================
   PROVE — sezione case study Novacar.
   REGOLA: qui dentro va SOLO ciò che è verificabile su disco.
   Fonte dei numeri: Clienti/Prof Autocad/preventivo-forge/
     · Memory/storico-preventivi/  → 65 record run (dealer novacar)
     · cartelle preventivi_<data>  → 52 PDF generati
     · CONSEGNA-NOVACAR.md §3      → tempo per preventivo ~1-2 min
     · Memory/decisioni/DEC-001    → template ricalcato sul modello cliente
   Nessun dato di vendita, nessuna testimonianza: non li abbiamo ancora.
   Se aggiungi una riga qui, deve avere una fonte su disco.
   ============================================================ */

type Numero = {
  value: number;
  prefix?: string;
  suffix: string;
  label: string;
  sub: string;
  numColor: string;
  numShadow: string;
};

const NUMERI: Numero[] = [
  {
    value: 65,
    suffix: "",
    label: "Preventivi generati",
    sub: "Annunci reali, dal 3 al 13 luglio 2026",
    numColor: "#fb4604",
    numShadow: "0 0 28px rgba(251,70,4,0.45)",
  },
  {
    value: 11,
    suffix: "",
    label: "Marche diverse",
    sub: "Mercedes, Audi, BMW, Tesla, Toyota, Renault…",
    numColor: "#7b4fb0",
    numShadow: "0 0 28px rgba(123,79,176,0.50)",
  },
  {
    value: 2,
    prefix: "~",
    suffix: " min",
    label: "Dal link al PDF finito",
    sub: "Tempo di lavoro della macchina, misurato",
    numColor: "#1c1c1c",
    numShadow: "none",
  },
  {
    value: 6,
    suffix: "",
    label: "Controlli prima di ogni PDF",
    sub: "Se uno fallisce, il preventivo non esce",
    numColor: "#fb4604",
    numShadow: "0 0 28px rgba(251,70,4,0.45)",
  },
];

const PRIMA = [
  "Annuncio in tedesco da tradurre a mano, voce per voce",
  "Prezzo finale ricalcolato ogni volta con la calcolatrice",
  "Foto salvate una a una, spesso tagliate nell'impaginazione",
  "PDF rimontato a mano su Word, diverso da venditore a venditore",
];

const DOPO = [
  "Si incolla il link dell'annuncio e si preme un tasto",
  "Le regole di prezzo del salone sono dentro la macchina",
  "Tutte le foto, complete, alla dimensione giusta",
  "Sempre lo stesso PDF, sul modello che Novacar già usava",
];

const CONTROLLI = [
  {
    k: "Dati",
    v: "L'annuncio è stato letto per intero: marca, modello, allestimento, scheda tecnica.",
  },
  {
    k: "Prezzo",
    v: "Il calcolo segue le regole del salone e il totale finisce anche nel titolo.",
  },
  {
    k: "Testo",
    v: "Scheda tecnica ed equipaggiamento sono in italiano, non in tedesco.",
  },
  {
    k: "Immagini",
    v: "Tutte le foto presenti, intere, mai tagliate: è una regola del cliente, non una preferenza nostra.",
  },
  {
    k: "Impaginazione",
    v: "Le quattordici regole del modello Novacar rispettate una per una.",
  },
  {
    k: "Consegna",
    v: "Il PDF si apre e viene archiviato nello storico del salone.",
  },
];

export function ProveNovacar() {
  return (
    <section
      id="prove"
      className="bg-ink-alt section relative overflow-hidden"
      aria-labelledby="prove-h2"
    >
      <div className="container-wide">
        {/* ── HEADER ── */}
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-gold">
              <ShieldCheck className="h-3.5 w-3.5" />
              La prova · numeri contati, non stimati
            </span>
            <h2 id="prove-h2" className="mt-6">
              <span className="text-silver-white">Una prova,</span>{" "}
              <span className="text-silver-gold font-accent italic">
                non una promessa.
              </span>
            </h2>
            <p className="mt-5 text-[1.0625rem] text-white/85 leading-relaxed font-light">
              Novacar srl, concessionaria multimarca, compra auto dai portali esteri e
              le rivende in Italia. Ogni auto richiedeva un preventivo tradotto,
              ricalcolato e reimpaginato a mano. Abbiamo costruito la macchina che lo fa
              al posto loro. Qui sotto ci sono i numeri di quella macchina.
            </p>
          </div>
        </Reveal>

        {/* ── NUMERI ── */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-6">
          {NUMERI.map((n, i) => (
            <Reveal key={n.label} delay={0.08 + i * 0.07}>
              <div className="stat-card-silver h-full">
                <div
                  className="font-display text-[2.5rem] md:text-[3rem] leading-none font-bold mb-3"
                  style={{ color: n.numColor, textShadow: n.numShadow }}
                >
                  <CountUp to={n.value} prefix={n.prefix ?? ""} suffix={n.suffix} />
                </div>
                <div className="text-[0.98rem] font-semibold mb-1.5 text-[#1c1c1c]">
                  {n.label}
                </div>
                <div className="text-[0.82rem] text-[#1c1c1c]/60">{n.sub}</div>
              </div>
            </Reveal>
          ))}
        </div>

        {/* ── PRIMA / DOPO ── */}
        <div className="grid md:grid-cols-2 gap-5 mb-6">
          <Reveal delay={0.10}>
            <article className="card-dark-red h-full flex flex-col">
              <span className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-white/60 mb-4 block">
                Prima — ogni singola auto
              </span>
              <h3 className="text-[1.3rem] font-bold text-white leading-snug mb-5">
                Mezz&apos;ora di lavoro d&apos;ufficio per un documento solo.
              </h3>
              <ul className="flex flex-col gap-3">
                {PRIMA.map((p) => (
                  <li
                    key={p}
                    className="flex items-start gap-3 text-[0.92rem] text-white/85 font-light"
                  >
                    <span
                      className="mt-2 w-1.5 h-1.5 rounded-full shrink-0"
                      style={{ background: "rgba(255,140,140,0.85)" }}
                    />
                    <span>{p}</span>
                  </li>
                ))}
              </ul>
            </article>
          </Reveal>

          <Reveal delay={0.16}>
            <article
              className="h-full flex flex-col rounded-[22px] p-8"
              style={{
                border: "1px solid rgba(251,70,4,0.35)",
                background:
                  "radial-gradient(120% 80% at 0% 0%, rgba(251,70,4,0.14) 0%, transparent 58%), linear-gradient(180deg, #1a1a1a 0%, #101010 100%)",
                boxShadow:
                  "0 40px 80px -40px rgba(0,0,0,0.9), 0 0 0 1px rgba(251,70,4,0.12)",
              }}
            >
              <span className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-gold-pure mb-4 block">
                Dopo — la macchina
              </span>
              <h3 className="text-[1.3rem] font-bold text-white leading-snug mb-5">
                Un link, un tasto, circa due minuti.
              </h3>
              <ul className="flex flex-col gap-3">
                {DOPO.map((d) => (
                  <li
                    key={d}
                    className="flex items-start gap-3 text-[0.92rem] text-white/90 font-light"
                  >
                    <FileCheck2 className="h-4 w-4 mt-0.5 shrink-0 text-gold-pure" />
                    <span>{d}</span>
                  </li>
                ))}
              </ul>
            </article>
          </Reveal>
        </div>

        {/* ── ESEMPIO REALE ── */}
        <Reveal delay={0.20}>
          <div className="card-paper mb-6">
            <div className="flex flex-col lg:flex-row lg:items-center gap-8">
              <div className="lg:flex-1">
                <span className="text-[0.7rem] uppercase tracking-[0.20em] font-semibold text-[#c93a0a] block mb-3">
                  Un preventivo vero, preso dallo storico
                </span>
                <h3 className="text-[1.4rem] font-bold text-[#1c1c1c] leading-snug mb-3">
                  Opel Insignia, 13 luglio 2026.
                </h3>
                <p className="text-[0.94rem] leading-relaxed text-[#1c1c1c]/75 font-light">
                  Annuncio estero letto dalla macchina, scheda tecnica riportata in
                  italiano, regole di prezzo del salone applicate. Il totale finisce anche
                  nel titolo del documento, come lo vuole Novacar:{" "}
                  <span className="font-semibold text-[#1c1c1c]">
                    «Opel Insignia Dynamic 19.428 €»
                  </span>
                  .
                </p>
              </div>

              <div className="flex items-center gap-5 lg:gap-7 shrink-0">
                <div className="text-center">
                  <div className="text-[0.7rem] uppercase tracking-[0.18em] text-[#1c1c1c]/50 mb-1">
                    Prezzo annuncio
                  </div>
                  <div className="font-display text-[1.65rem] font-bold text-[#1c1c1c]/45 line-through decoration-[#c93a0a]/40">
                    15.950 €
                  </div>
                </div>

                <ArrowRight className="hidden sm:block h-5 w-5 text-[#c93a0a]/60 shrink-0" />
                <ArrowDown className="sm:hidden h-5 w-5 text-[#c93a0a]/60 shrink-0" />

                <div className="text-center">
                  <div className="text-[0.7rem] uppercase tracking-[0.18em] text-[#c93a0a] mb-1">
                    Sul preventivo
                  </div>
                  <div
                    className="font-display text-[1.95rem] font-bold"
                    style={{ color: "#c93a0a" }}
                  >
                    19.428 €
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Reveal>

        {/* ── I SEI CONTROLLI ── */}
        <Reveal delay={0.24}>
          <div className="card-dark">
            <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-7">
              <div>
                <span className="bubble-gold !py-1 !px-3 !text-[0.7rem] uppercase tracking-[0.18em]">
                  Perché ci si può fidare del PDF
                </span>
                <h3 className="mt-4 text-[1.4rem] font-bold text-white leading-snug">
                  Sei controlli automatici, prima che il documento esista.
                </h3>
              </div>
              <p className="text-[0.85rem] text-white/60 font-light md:max-w-xs md:text-right">
                Se anche uno solo fallisce, la macchina si ferma e non consegna. Meglio
                nessun preventivo che un preventivo sbagliato al cliente.
              </p>
            </div>

            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-x-6 gap-y-5">
              {CONTROLLI.map((c, i) => (
                <div key={c.k} className="flex items-start gap-3">
                  <span
                    className="grid place-items-center w-7 h-7 rounded-lg shrink-0 font-display text-[0.75rem] font-bold"
                    style={{
                      background: "rgba(251,70,4,0.14)",
                      border: "1px solid rgba(251,70,4,0.32)",
                      color: "#ff8a4a",
                    }}
                  >
                    {i + 1}
                  </span>
                  <div>
                    <div className="text-[0.92rem] font-semibold text-white mb-0.5">
                      {c.k}
                    </div>
                    <p className="text-[0.85rem] leading-relaxed text-white/70 font-light">
                      {c.v}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </Reveal>

        {/* ── CARTE SCOPERTE: i limiti di questa prova ── */}
        <Reveal delay={0.28}>
          <div
            className="mt-6 rounded-2xl px-6 py-6 md:px-8"
            style={{
              border: "1px dashed rgba(255,255,255,0.22)",
              background: "rgba(255,255,255,0.03)",
            }}
          >
            <div className="flex items-start gap-3 mb-4">
              <Eye className="h-4 w-4 mt-1 shrink-0 text-white/60" />
              <h3 className="text-[1rem] font-semibold text-white">
                Cosa questa prova <span className="italic font-accent">non</span> dice
              </h3>
            </div>
            <ul className="flex flex-col gap-2.5 text-[0.9rem] leading-relaxed text-white/70 font-light">
              <li>
                <span className="text-white/90 font-medium">
                  Non diciamo che Novacar vende di più.
                </span>{" "}
                La macchina produce il documento, non chiude la trattativa. Chi vi promette
                un aumento di vendite da un software vi sta vendendo fumo.
              </li>
              <li>
                <span className="text-white/90 font-medium">
                  I 65 preventivi comprendono i nostri collaudi.
                </span>{" "}
                Sono annunci veri e PDF veri, generati mentre costruivamo e verificavamo la
                macchina: sono la prova che funziona, non il registro vendite del cliente.
              </li>
              <li>
                <span className="text-white/90 font-medium">
                  La testimonianza firmata non c&apos;è ancora.
                </span>{" "}
                Quando arriva la pubblichiamo qui, con nome e cognome. Fino ad allora
                restano i numeri, che potete verificare in demo.
              </li>
            </ul>

            <div className="mt-6 pt-5 border-t border-white/12 flex flex-col sm:flex-row sm:items-center gap-4 sm:justify-between">
              <p className="text-[0.9rem] text-white/75 font-light">
                Volete vedere la stessa macchina girare su un caso vostro?
              </p>
              <a href="/prenota" className="btn-gold group shrink-0">
                Prenota la demo
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </a>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
