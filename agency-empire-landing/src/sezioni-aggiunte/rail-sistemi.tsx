/* AGGIUNTA A12 (Dossier 38 v2, Atto IV) — «Rail dei sistemi in produzione». Inserita dopo <ProveVere />.
   Ink. Nastro CSS lento (70 s, doppio elenco per il loop, fermo con prefers-reduced-motion e al passaggio del
   mouse) di CINQUE figure verticali INTERE (§14): due pagine vere di PDF PreventivoForge (intestazione del
   cliente ritagliata alla fonte, in public/aura/) e tre screenshot nostri del sito. Larghezza 190 px per i PDF;
   gli screenshot mobile hanno un tetto d'altezza (340 px) perché a 190 px di larghezza sarebbero alti fino
   a 931 px — mai tagliati, mai cover. Nessuna CTA. 0 KB di JS. CSS: src/app/aggiunte-b.css (.rs-*). */

type Figura = { src: string; width: number; height: number; alt: string; nome: string; ruolo: string };

const SISTEMI: Figura[] = [
  {
    src: "/aura/pf-scheda.webp",
    width: 1191,
    height: 1458,
    alt: "Pagina di un PDF vero di PreventivoForge: la scheda tecnica compilata dal sistema, intestazione del cliente ritagliata",
    nome: "PreventivoForge",
    ruolo: "PDF scheda",
  },
  {
    src: "/aura/pf-totale.webp",
    width: 1191,
    height: 1458,
    alt: "Pagina di un PDF vero di PreventivoForge: il riepilogo del totale, intestazione del cliente ritagliata",
    nome: "PreventivoForge",
    ruolo: "PDF totale",
  },
  {
    src: "/aura/shot-hero-mobile.webp",
    width: 390,
    height: 1911,
    alt: "Screenshot da telefono del sito dell'agenzia: la prima schermata, intera",
    nome: "Sito agency",
    ruolo: "hero",
  },
  {
    src: "/aura/shot-specchio-mobile.webp",
    width: 390,
    height: 1103,
    alt: "Screenshot da telefono del sito dell'agenzia: la sezione Specchio, intera",
    nome: "Sito agency",
    ruolo: "specchio",
  },
  {
    src: "/aura/shot-prenota-mobile.webp",
    width: 390,
    height: 1362,
    alt: "Screenshot da telefono della pagina /prenota/ dell'agenzia, intera",
    nome: "/prenota/",
    ruolo: "porta",
  },
];

export function RailSistemi() {
  const lista = [...SISTEMI, ...SISTEMI];
  return (
    <div className="vivo">
      <section id="rail-sistemi" className="sv sv-ink sv-section rs" aria-labelledby="rail-sistemi-h3">
        <div className="sv-container">
          <p className="sv-eyebrow">In produzione</p>
          <h3 id="rail-sistemi-h3" className="sv-h3 mt-3 max-w-[30ch]">
            Cinque cose che girano davvero. <span className="sv-it" style={{ color: "var(--sv-orange)" }}>Oscurate dove serve.</span>
          </h3>
        </div>
        <div className="rs-track">
          <ul className="rs-rail">
            {lista.map((f, i) => (
              <li key={`${f.src}-${i}`} className="rs-item" aria-hidden={i >= SISTEMI.length ? true : undefined}>
                <figure className="rs-fig">
                  <div className="foto-intera" style={{ aspectRatio: `${f.width}/${f.height}` }}>
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={f.src} width={f.width} height={f.height} alt={f.alt} loading="lazy" decoding="async" />
                  </div>
                  <figcaption>
                    <b>{f.nome}</b>
                    <span>{f.ruolo}</span>
                  </figcaption>
                </figure>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}
