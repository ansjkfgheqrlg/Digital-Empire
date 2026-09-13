import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";

/* SEZIONE AGGIUNTA 1 — Specchio: «Ti voglio bene, ma lo stai facendo a mano» + il DM vero + i quattro segnali + voto.
   Inserita dopo <Problems />. Copy: cantieri/agency-empire-landing-vivo/COPY.md §N2. Tutto dentro <div class="vivo">.
   D5 (ordine di Max, 13/09 — Dossier 38 v2 §I): colonna foto a sinistra del blocco alto (grid md:grid-cols-[auto_1fr] gap-10),
   immagine intera 1/1 (400×400, resa ≤ 368 px, §14: mai cover, mai grana sull'immagine), la riga SOPRA l'immagine in basso
   (corsivo serif 400/18 su banda scura), bordo 1 px + ombra bassa. Il testo esistente non è cambiato di una parola.
   CSS della colonna foto: aggiunte-a.css (.sp-*, .foto-intera--riga). */
const SEGNALI: [string, string][] = [
  ["Rimandi il follow-up.", "Il lead di martedì lo ricontatti venerdì, se te lo ricordi."],
  ["Pubblichi quando riesci.", "Tre post una settimana, zero la successiva."],
  ["Copi e incolli.", "Lo stesso messaggio a trenta persone diverse. Loro se ne accorgono."],
  ["Sai tutto tu.", "Clienti, prezzi, processi: nella tua testa e in cinque cartelle Drive. Il giorno che manchi tu, manca l'azienda."],
];

/* D5 — la foto dello specchio. Il file è 400×400: si rende a 368 (≤ nativa, §14). */
const FOTO_SPECCHIO = {
  src: "/aura/specchio.webp",
  width: 400,
  height: 400,
  alt: "Un uomo seduto, la mano sul viso, davanti al telefono: la mattina dei trenta DM scritti a mano.",
} as const;

export function Specchio() {
  return (
    <div className="vivo">
      <section id="specchio" className="sv sv-carta sv-section" aria-labelledby="specchio-h2">
        <div className="sv-container">
          <div className="grid md:grid-cols-[auto_1fr] gap-10 items-start">
            <div className="sp-foto-col">
              <figure
                className="foto-intera foto-intera--riga sp-foto"
                style={{ aspectRatio: `${FOTO_SPECCHIO.width}/${FOTO_SPECCHIO.height}` }}
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={FOTO_SPECCHIO.src}
                  width={FOTO_SPECCHIO.width}
                  height={FOTO_SPECCHIO.height}
                  alt={FOTO_SPECCHIO.alt}
                  loading="lazy"
                  decoding="async"
                />
                {/* «Da tre anni» del brief non sta in FATTI.md: il numero non si scrive (regola 4). Segnalato nel rapporto. */}
                <figcaption>
                  Ogni mattina. {FATTI.dmAMano} DM. A mano. <b>Da anni.</b>
                </figcaption>
              </figure>
            </div>

            <div>
              <h2 id="specchio-h2" className="sv-h2 max-w-[14ch]">
                Ti voglio bene, ma <span className="sv-it" style={{ color: "var(--sv-orange)" }}>lo stai facendo a mano.</span>
              </h2>
              <p className="sv-lead sv-muted mt-4 max-w-[52ch]">
                Non è colpa tua: nessuno ti ha mai mostrato il sistema. Ti hanno mostrato un tool, un abbonamento, un corso. Questo è quello
                che parte dal tuo telefono oggi:
              </p>
              <div className="dm mt-6 max-w-[460px]">
                <span className="sv-mono block mb-2">DM di oggi · concessionario, Veneto</span>
                <i>Ciao! Ho visto la tua concessionaria, complimenti 👏 Ti va se ti mando due info su come aumentare i contatti? 🚗</i>
                <em>
                  — {FATTI.dmAMano} volte al giorno, {FATTI.minutiPerDm} minuti l&apos;uno: {FATTI.orePerDm.toLocaleString("it-IT")} ore. Sembra
                  un template perché lo è.
                </em>
              </div>
            </div>
          </div>

          <div className="mt-14">
            <h3 className="sv-h3">I quattro segnali. Ne basta uno.</h3>
            <ol className="mt-6 grid md:grid-cols-2 gap-x-10 gap-y-5 max-w-[900px]">
              {SEGNALI.map(([t, d], i) => (
                <li key={t} className="grid grid-cols-[28px_1fr] gap-3 items-start">
                  <span className="sv-mono" style={{ color: "var(--sv-orange)" }}>{i + 1}</span>
                  <p className="sv-body sv-muted">
                    <b style={{ color: "var(--sv-ink-1)" }}>{t}</b> {d}
                  </p>
                </li>
              ))}
            </ol>
            <div className="mt-8 flex flex-wrap items-center gap-4">
              <span className="sv-body">
                <b>Ti ritrovi?</b> Quattro segnali: ne basta 1.
              </span>
              <Link href={prenotaDa("specchio")} data-cta className="sv-btn">Sì, mi ritrovo →</Link>
              <a href="#prove-vere" className="sp-link">Non mi ritrovo</a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
