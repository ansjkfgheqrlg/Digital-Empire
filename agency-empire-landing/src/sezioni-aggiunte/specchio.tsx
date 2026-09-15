import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";

/* SEZIONE AGGIUNTA 1 — Specchio: «Ti voglio bene, ma lo stai facendo a mano» + i quattro segnali + CTA.
   Inserita dopo <Problems />. Tutto dentro <div class="vivo">.
   D5 (ordine di Max, 13/09 — Dossier 38 v2 §I): colonna foto a sinistra del blocco alto (grid md:grid-cols-[auto_1fr] gap-10),
   immagine intera 1/1 (400×400, resa ≤ 368 px, §14: mai cover, mai grana sull'immagine), la riga SOPRA l'immagine in basso
   (corsivo serif 400/18 su banda scura), bordo 1 px + ombra bassa.
   F6 (ordine di Max 15/09, dossier 41 blocco E, legge del copy generico): riscritto senza «DM»/concessionario —
   esempi generici in serie, il principio dell'automazione, la chiamata gratuita, la chiusura. Copy in
   brief/COPY-F6-gamma.md §E1. CSS della colonna foto/chat: aggiunte-a.css (.sp-*, .foto-intera--riga, .dm — vivo.css). */
const SEGNALI: [string, string][] = [
  ["Rimandi la risposta.", "A chi ti ha scritto ieri, rispondi domani. Se te lo ricordi."],
  ["Rifai lo stesso conto.", "Ogni preventivo calcolato daccapo, ogni volta, a mano."],
  ["Copi e incolli.", "Lo stesso messaggio, la stessa mail, lo stesso report. Cambia solo il nome in cima."],
  ["Sai tutto tu.", "Clienti, prezzi, processi: nella tua testa e in cinque cartelle Drive. Il giorno che manchi tu, manca l'azienda."],
];

/* D5 — la foto dello specchio. Il file è 400×400: si rende a 368 (≤ nativa, §14). */
const FOTO_SPECCHIO = {
  src: "/aura/specchio.webp",
  width: 400,
  height: 400,
  alt: "Un uomo seduto, la mano sul viso, davanti al computer: la mattina di chi rifà tutto a mano.",
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
                <figcaption>
                  Ogni mattina. Le stesse cose, a mano. <b>Da anni.</b>
                </figcaption>
              </figure>
            </div>

            <div>
              <h2 id="specchio-h2" className="sv-h2 max-w-[14ch]">
                Ti voglio bene, ma <span className="sv-it" style={{ color: "var(--sv-orange)" }}>lo stai facendo a mano.</span>
              </h2>
              <p className="sv-lead sv-muted mt-4 max-w-[52ch]">
                Non è colpa tua: nessuno ti ha mai mostrato il sistema. Ti hanno mostrato un tool, un abbonamento, un corso. Questo è quello
                che arriva anche a te, ogni giorno:
              </p>
              <div className="dm mt-6 max-w-[460px]">
                <span className="sv-mono block mb-2">Nella posta, oggi:</span>
                <i>Ciao, mi rimandi il preventivo aggiornato? Mi serve entro stasera 🙏</i>
                <em>— Il quarto oggi. Aperto il foglio, ricopiato a mano. Di nuovo.</em>
              </div>
              <p className="sv-body sv-muted mt-6 max-w-[54ch]">
                Il preventivo ricopiato a mano. Lo stesso report ogni lunedì. I dati spostati a mano da un foglio all&apos;altro. La stessa
                mail scritta {FATTI.dmAMano} volte.
              </p>
              <p className="sv-body mt-4 max-w-[54ch]">
                Se lo fai ogni giorno, uguale, <b style={{ color: "var(--sv-ink-1)" }}>è una macchina che lo deve fare.</b>
              </p>
              <p className="sv-body sv-muted mt-4 max-w-[54ch]">
                Automatizzare lo fa anche <b style={{ color: "var(--sv-ink-1)" }}>meglio</b> — o <b style={{ color: "var(--sv-ink-1)" }}>più
                in grande</b>. Dipende dal processo.
              </p>
              <p className="sv-body sv-muted mt-4 max-w-[54ch]">
                Non tutto va automatizzato. Per questo la prima chiamata è gratuita: in <b style={{ color: "var(--sv-ink-1)" }}>{FATTI.minutiChiamata}
                {" "}minuti</b> guardiamo la tua situazione e ti diciamo se possiamo aiutarti davvero, su un problema concreto.
              </p>
              <p className="sv-body sv-muted mt-4 max-w-[54ch]">
                Oggi con l&apos;AI si automatizza tutto. La differenza è <b style={{ color: "var(--sv-ink-1)" }}>automatizzare le cose
                giuste, nel modo giusto</b>. Le aziende che l&apos;hanno capito scalano così.
              </p>
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
