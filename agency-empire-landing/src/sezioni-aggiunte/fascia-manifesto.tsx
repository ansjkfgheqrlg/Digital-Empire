import { TEXTURE } from "@/lib/media";

/* AGGIUNTA D3 (ordine di Max, 13/09 — Dossier 38 v2 §I) — la fascia-manifesto: una sezione piccola, «quasi un elemento»,
   con la texture «grana di fuoco» come sfondo e una frase sola. Inserita dopo <PowerDeck />. h ≤ 320.
   Sfondo: TEXTURE.granaFuoco intera come <img> assoluto in `cover` — eccezione §14 dichiarata (è uno sfondo, non
   un'immagine di contenuto). Sopra: velo con vignetta scura ai bordi (radial + linear) per la leggibilità, grana locale
   sul velo e non sulla texture (D6). Nessuna CTA (§15); il cerchio-freccia «↓» è stato tolto il 13/09 sera (F3 blocco C, 39B r.31).
   Se la texture non c'è (null) la sezione rende null e il sito resta intero (ADR-028). CSS: aggiunte-a.css. */
export function FasciaManifesto() {
  const t = TEXTURE.granaFuoco;
  if (!t) return null;
  return (
    <div className="vivo">
      <section id="manifesto" className="sv sv-ink fascia-manifesto" aria-labelledby="manifesto-h2">
        <div className="fm-sfondo" aria-hidden="true">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={t.src} width={t.width} height={t.height} alt="" loading="lazy" decoding="async" />
          <div className="fm-velo" />
        </div>
        <div className="sv-container fm-corpo">
          <p className="sv-eyebrow">Una frase, e basta</p>
          <h2 id="manifesto-h2" className="sv-h2 fm-h2">
            I tool si pagano. <span className="sv-it">I sistemi si possiedono.</span>
          </h2>
        </div>
      </section>
    </div>
  );
}
