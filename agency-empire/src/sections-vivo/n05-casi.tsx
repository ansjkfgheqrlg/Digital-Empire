"use client";

import { useState } from "react";
import { ArrowRight, ChevronLeft, ChevronRight } from "lucide-react";

/* N5 — Vetrina cliente (speedrun T24: il sito del cliente dentro il nostro). Copy: COPY-V2 §N5.
   Numeri Novacar misurati: 65 preventivi, 11 marche, ~2 min, 6 controlli — annunci reali 3-13 luglio 2026
   (src/sections/09b-prove-novacar.tsx del sito v1). Pattern Fabbrica: vetrina-cliente. */
const NUMERI = [
  { n: "65", t: "preventivi generati" },
  { n: "11", t: "marche diverse" },
  { n: "~2 min", t: "dal link al PDF" },
  { n: "6", t: "controlli prima di ogni PDF" },
];

const SCHERMATE = [
  {
    titolo: "1 · Il venditore incolla il link",
    corpo: "Annuncio da un portale tedesco. Un campo, un tasto: Genera.",
    ui: ["mobile.de/…/audi-a4-avant-2021", "▶ GENERA PREVENTIVO"],
  },
  {
    titolo: "2 · Le regole del salone sono dentro",
    corpo: "Ricarico, messa su strada, margine: impostati una volta dal titolare. Il venditore vede il prezzo, non lo tocca.",
    ui: ["ricarico 12% · messa su strada 350 € · margine min 900 €", "totale in strada, IVA inclusa: nel titolo"],
  },
  {
    titolo: "3 · Sei controlli, poi il PDF",
    corpo: "Scheda tecnica in italiano, foto intere e mai tagliate, equipaggiamento completo, totale ricalcolato. Se uno fallisce, il preventivo non esce.",
    ui: ["✓ lingua ✓ foto 14/14 ✓ scheda ✓ prezzo ✓ modello ✓ archivio", "PDF pronto per WhatsApp"],
  },
  {
    titolo: "4 · Lo storico resta sul PC del salone",
    corpo: "Ogni preventivo archiviato con data, venditore e annuncio. Aggiornamenti del motore inclusi, nessun canone.",
    ui: ["2026-07-13 · 65 preventivi · 11 marche", "€ 2.000 una tantum"],
  },
];

export function Casi() {
  const [i, setI] = useState(0);
  const prev = () => setI((x) => (x - 1 + SCHERMATE.length) % SCHERMATE.length);
  const next = () => setI((x) => (x + 1) % SCHERMATE.length);
  const s = SCHERMATE[i];

  return (
    <section id="casi" className="sv sv-carta" aria-labelledby="casi-h2">
      <div className="container-default py-16 md:py-20">
        <p className="sv-eyebrow">Un cliente vero, con i numeri veri</p>
        <h2 id="casi-h2" className="sv-h2 mt-3 max-w-[16ch]">
          Novacar: 65 preventivi <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>in dieci giorni.</span>
        </h2>

        <div className="grid md:grid-cols-2 gap-8 mt-8">
          <p className="sv-body sv-muted">
            Un concessionario che abbiamo seguito noi, dall&apos;annuncio al PDF. <b style={{ color: "#1c1c1c" }}>Prima:</b> annuncio in
            tedesco da tradurre a mano, prezzo ricalcolato con la calcolatrice, foto salvate una a una, PDF rimontato
            su Word — diverso da venditore a venditore. Mezz&apos;ora a preventivo, se andava bene.
          </p>
          <p className="sv-body sv-muted">
            <b style={{ color: "#1c1c1c" }}>Dopo:</b> il venditore incolla il link dell&apos;annuncio e preme un tasto. Le regole di prezzo del
            salone sono dentro la macchina. Tutte le foto, intere. Sempre lo stesso PDF, sul modello che Novacar già usava.
          </p>
        </div>

        <div className="mt-10 grid grid-cols-2 md:grid-cols-4 gap-px" style={{ background: "var(--sv-hair-light)" }}>
          {NUMERI.map((x) => (
            <div key={x.t} className="p-5" style={{ background: "var(--sv-carta)" }}>
              <div className="sv-stat" style={{ color: "#1c1c1c" }}>{x.n}</div>
              <div className="sv-mono mt-2" style={{ color: "#6f6a62" }}>{x.t}</div>
            </div>
          ))}
        </div>
        <p className="sv-small mt-3" style={{ color: "#6f6a62" }}>Annunci reali, 3-13 luglio 2026.</p>

        {/* la vetrina: il prodotto del cliente, navigabile */}
        <div
          className="mt-10 rounded-[6px] overflow-hidden"
          style={{ border: "1px solid var(--sv-hair-light)", boxShadow: "0 30px 60px -30px rgba(0,0,0,.35)", background: "#131313", color: "#fff" }}
          aria-roledescription="carosello"
          aria-label="Preventa, il prodotto di Novacar"
        >
          <div className="flex items-center gap-2 px-3 h-7" style={{ background: "#161616", borderBottom: "1px solid var(--sv-hair)" }}>
            <i className="w-2 h-2 rounded-full" style={{ background: "#3a3a3a" }} />
            <i className="w-2 h-2 rounded-full" style={{ background: "#3a3a3a" }} />
            <i className="w-2 h-2 rounded-full" style={{ background: "#3a3a3a" }} />
            <span className="ml-auto sv-mono" style={{ color: "var(--sv-silver-dim)", letterSpacing: ".1em" }}>Preventa · app desktop del salone</span>
          </div>
          <div className="grid md:grid-cols-[1fr_auto] gap-6 p-6 md:p-8 min-h-[220px] items-center" aria-live="polite">
            <div>
              <div className="sv-h3">{s.titolo}</div>
              <p className="sv-body sv-muted mt-2 max-w-[56ch]">{s.corpo}</p>
              <div className="mt-4 grid gap-2">
                {s.ui.map((u) => (
                  <div key={u} className="sv-mono px-3 py-2 rounded-[4px]" style={{ background: "rgba(255,255,255,.05)", border: "1px solid var(--sv-hair)", color: "#fff", letterSpacing: ".04em", textTransform: "none" }}>{u}</div>
                ))}
              </div>
            </div>
            <div className="flex md:flex-col items-center gap-3">
              <button type="button" onClick={prev} className="sv-btn-ghost !p-0 min-w-11 min-h-11 justify-center" aria-label="Schermata precedente"><ChevronLeft className="h-4 w-4" /></button>
              <div className="flex md:flex-col gap-2" aria-hidden>
                {SCHERMATE.map((_, k) => (
                  <i key={k} className="block w-2 h-2 rounded-full" style={{ background: k === i ? "var(--sv-orange)" : "rgba(255,255,255,.25)" }} />
                ))}
              </div>
              <button type="button" onClick={next} className="sv-btn-ghost !p-0 min-w-11 min-h-11 justify-center" aria-label="Schermata successiva"><ChevronRight className="h-4 w-4" /></button>
            </div>
          </div>
        </div>

        <p className="sv-small mt-4" style={{ color: "#6f6a62" }}>
          Preventa è lo stesso motore venduto ai concessionari a 2.000 € una tantum, zero canone. Non un&apos;altra agenzia: uno strumento loro.
        </p>
        <a href="/prenota" className="btn-gold mt-8" data-cta="casi">
          Voglio un sistema così <ArrowRight className="h-4 w-4" />
        </a>
      </div>
    </section>
  );
}
