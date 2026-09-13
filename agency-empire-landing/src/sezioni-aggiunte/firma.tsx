import { RITRATTI } from "@/lib/media";
import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A01 (Dossier 38 v2, Atto I) — «La firma»: il primo volto vero, subito sotto l'hero (§15: entro il 10%).
   Ritratto di Max intero, in colonna al suo pixel (§14), riga in prima persona, micro-CTA «↓».
   Finché RITRATTI.maxFirma è null la sezione rende null e il sito è intero (ADR-028). Il ritratto è un gesto di Max (§H). */
export function Firma() {
  const r = RITRATTI.maxFirma;
  if (!r) return null;
  return (
    <div className="vivo">
      <section id="firma" className="sv sv-ink sv-section firma" aria-labelledby="firma-h2">
        <div className="sv-container firma-grid">
          <figure className="firma-foto" style={{ aspectRatio: `${r.width}/${r.height}` }}>
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={r.src} width={r.width} height={r.height} alt={r.alt} loading="lazy" decoding="async" />
          </figure>
          <div>
            <span className="sv-eyebrow sv-mono">Fondatore</span>
            <h2 id="firma-h2" className="sv-h2 mt-3">
              Ho costruito il primo sistema per me. <span className="sv-it">Poi ho smesso di venderlo come «tool».</span>
            </h2>
            <p className="sv-lead sv-muted mt-4 max-w-[46ch]">
              Maximilian — {FATTI.sistemi} sistemi, {FATTI.persone} persone, nati a {FATTI.meseNascita} {FATTI.annoNascita}. Quello che vedi qui
              sotto gira per noi ogni giorno.
            </p>
            <a href="#specchio" className="sv-btn-ghost mt-6">↓ Guarda come funziona</a>
          </div>
        </div>
      </section>
    </div>
  );
}
