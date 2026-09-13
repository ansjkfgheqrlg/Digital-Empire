import { TEXTURE } from "@/lib/media";

/* AGGIUNTA D1 (ordine di Max, 13/09) — la texture «onde puntinate» come sfondo dell'hero.
   Layer assoluto inserito come PRIMO figlio della <section> dell'hero: sta sotto tutto il resto (marquee, chip,
   titolo), che non viene toccato. Eccezione §14 dichiarata: è uno sfondo, quindi `object-fit: cover`.
   Sopra la texture c'è un velo scuro calibrato al contrasto (misurato con lo screenshot in F1, non a occhio):
   più denso dove passano le scritte, più leggero ai bordi dove si vede l'onda. La grana fissa del sito
   (.grain-fine, z 100/101) resta sopra a tutto: la texture NON la copre. */
export function HeroTexture() {
  const t = TEXTURE.heroOnde;
  if (!t) return null;
  return (
    <div className="hero-tex" aria-hidden="true">
      <picture>
        <source type="image/webp" srcSet={t.webp} />
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={t.src} width={t.width} height={t.height} alt="" fetchPriority="high" decoding="async" />
      </picture>
      <div className="hero-tex-velo" />
    </div>
  );
}
