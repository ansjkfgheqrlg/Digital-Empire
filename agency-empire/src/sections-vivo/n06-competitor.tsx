import { Aura } from "@/components/vivo/aura";

/* N6 — Fascia-lampo (speedrun T12: l'UNICO fondo pieno arancione della pagina, §12) + asse posizionale
   (speedrun T18: BROKIE→TU→COMPETITOR). Copy: COPY-V2 §N6. Pattern Fabbrica: fascia-lampo, asse-posizionale. */
export function Competitor() {
  return (
    <section id="competitor" aria-labelledby="competitor-h2">
      <div className="sv sv-fascia">
        <div className="container-default grid md:grid-cols-2 gap-8 items-center py-12 md:py-14 min-h-[300px]">
          <h2 id="competitor-h2" className="sv-h2" style={{ color: "#000", fontSize: "clamp(30px,3.8vw,50px)" }}>
            Hai <span style={{ color: "#fff" }}>competitor</span>
            <br />e non lo sai.
          </h2>
          <p className="sv-lead max-w-[44ch]" style={{ color: "#1a0a04", borderLeft: "2px solid #fff", paddingLeft: 16 }}>
            Lo vediamo ogni settimana nei saloni e negli studi che contattiamo: un competitor non è chi fa il tuo
            mestiere. È chi i tuoi clienti potrebbero scegliere al posto tuo — e oggi sta installando un sistema
            che risponde prima di te.
          </p>
        </div>
      </div>

      <div className="sv sv-ink">
        <div className="container-default grid md:grid-cols-[minmax(0,380px)_1fr] gap-10 items-center py-16 md:py-20">
          <Aura
            file="n6-fascia.webp"
            alt="Silhouette in controluce davanti a tre finestre, senza volto"
            riga="Non ha un nome. Ha un sistema. E ha i tuoi clienti."
            tratt="negativo"
            className="aspect-[4/5] max-h-[420px] rounded-[4px]"
          />
          <div>
            <p className="sv-eyebrow">Dove sei adesso</p>
            <h3 className="sv-h3 mt-3" style={{ fontSize: "clamp(22px,2.6vw,32px)" }}>
              Stessi limiti tuoi.
              <br />
              <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Il primo che li risolve non lo raggiungi più.</span>
            </h3>
            <div className="linea">
              <div>A mano</div>
              <div className="tu">Tu<small>sei qui</small></div>
              <div className="av">Automatizzato</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
