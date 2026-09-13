import type { Immagine } from "@/lib/media";

/* AGGIUNTA A15 (Dossier 38 v2, Atto V) — «Dietro le quinte»: quattro foto di lavoro vere, a coppie, intere (§14).
   Inserita dopo <BuilderNotTrainer />. Superficie carta, h ≤ 600.
   Le foto sono un gesto di Max (§H): finché FOTO_LAVORO è `null` la sezione rende `null` (ADR-028).
   Quando arrivano, si mettono qui nell'ordine delle didascalie ({src,width,height,alt} in public/aura/); una voce `null` = quel posto salta. */
type QuattroFoto = readonly [Immagine, Immagine, Immagine, Immagine];
/** gesto di Max: quando le foto ci sono, questa funzione restituisce le quattro voci al posto di `null`. */
function fotoLavoro(): QuattroFoto | null {
  return null;
}

const DIDASCALIE = [
  "Max, la sera del primo go-live",
  "la chiamata delle 18 con il cliente",
  "Gael, il turno dei follow-up",
  "Leonardo, la riunione del lunedì",
] as const;

export function DietroLeQuinte() {
  const foto = fotoLavoro();
  if (!foto) return null;
  const scatti = DIDASCALIE.map((d, i) => ({ d, img: foto[i] })).filter(
    (s): s is { d: (typeof DIDASCALIE)[number]; img: NonNullable<Immagine> } => s.img !== null && s.img !== undefined,
  );
  if (scatti.length === 0) return null;
  const coppie: (typeof scatti)[] = [];
  for (let i = 0; i < scatti.length; i += 2) coppie.push(scatti.slice(i, i + 2));
  return (
    <div className="vivo">
      <section id="dietro-le-quinte" className="sv sv-carta sv-section dietro-le-quinte" aria-labelledby="dlq-h2">
        <div className="sv-container">
          <span className="sv-eyebrow">Dietro le quinte</span>
          <h2 id="dlq-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Il lavoro, <span className="sv-it">mentre succede.</span>
          </h2>
          <div className="dlq-coppie">
            {coppie.map((coppia, ci) => (
              <div key={ci} className="dlq-coppia">
                {coppia.map((s) => (
                  <figure key={s.d} className="foto-intera dlq-fig" style={{ aspectRatio: `${s.img.width}/${s.img.height}` }}>
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={s.img.src} width={s.img.width} height={s.img.height} alt={s.img.alt} loading="lazy" decoding="async" />
                    <figcaption>{s.d}</figcaption>
                  </figure>
                ))}
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
