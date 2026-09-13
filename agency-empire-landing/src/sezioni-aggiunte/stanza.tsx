import { RITRATTI, type Immagine } from "@/lib/media";

/* AGGIUNTA A14 (Dossier 38 v2, Atto V) — «La stanza»: le tre persone vere, ognuna al proprio rapporto (§14).
   Inserita dopo <WhoGuides />. Superficie ink, h ≤ 640.
   I ritratti sono un gesto di Max (§H): finché sono tutti `null` la sezione rende `null` e il sito resta intero (ADR-028);
   se ne arriva anche uno solo, si mostra quello. Nomi e ruoli: dal brief F2, nessun altro dato. */
type Persona = { chiave: keyof typeof RITRATTI; nome: string; ruolo: string };
type PersonaConFoto = Persona & { img: NonNullable<Immagine> };
const PERSONE: Persona[] = [
  { chiave: "maxFirma", nome: "Maximilian", ruolo: "fondatore, sistemi" },
  { chiave: "gael", nome: "Gael", ruolo: "operazioni, outreach" },
  { chiave: "leonardo", nome: "Leonardo", ruolo: "contenuti, Second Brain" },
];

export function Stanza() {
  const presenti: PersonaConFoto[] = [];
  for (const p of PERSONE) {
    const img = RITRATTI[p.chiave];
    if (img) presenti.push({ ...p, img });
  }
  if (presenti.length === 0) return null;
  return (
    <div className="vivo">
      <section id="stanza" className="sv sv-ink sv-section stanza" aria-labelledby="stanza-h2">
        <div className="sv-container stz-grid">
          <div>
            <span className="sv-eyebrow">Chi c&apos;è dietro</span>
            <h2 id="stanza-h2" className="sv-h2 mt-3">
              Tre persone. <span className="sv-it">Nessun account manager in mezzo.</span>
            </h2>
          </div>
          <ul className="stz-figure list-none m-0 p-0">
            {presenti.map((p) => (
              <li key={p.chiave} className="stz-fig">
                <figure className="foto-intera" style={{ aspectRatio: `${p.img.width}/${p.img.height}` }}>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={p.img.src} width={p.img.width} height={p.img.height} alt={p.img.alt} loading="lazy" decoding="async" />
                </figure>
                <div className="stz-targa c-grana">
                  <b>{p.nome}</b>
                  <span className="sv-mono">{p.ruolo}</span>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}
