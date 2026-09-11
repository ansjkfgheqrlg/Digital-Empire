import { Aura } from "@/components/vivo/aura";

/* N5 — Fascia-lampo + asse posizionale. Copy: COPY.md §N5.
   Un solo <section>: il primo blocco è l'unico fondo pieno arancione della pagina (§12 vivo.css),
   il secondo torna a ink con l'asse A MANO — TU (sei qui) — CON UN SISTEMA e la foto Aura. */
export function Competitor() {
  return (
    <section id="competitor" aria-labelledby="competitor-h2">
      <div className="sv sv-fascia sv-section">
        <div className="sv-container">
          <h2 id="competitor-h2" className="sv-h2">
            Hai <span className="sv-it" style={{ color: "var(--sv-silver)" }}>competitor</span> e non lo sai.
          </h2>
          <p className="sv-lead mt-4 max-w-[62ch]">
            Lo vediamo ogni settimana nei saloni e negli studi che contattiamo: un competitor non è chi fa il tuo
            mestiere. È chi i tuoi clienti potrebbero scegliere al posto tuo — e oggi sta installando un sistema che
            risponde prima di te.
          </p>
        </div>
      </div>

      <div className="sv sv-ink sv-section">
        <div className="sv-container due-col">
          <div>
            <p className="sv-eyebrow">Dove sei adesso</p>
            <div className="linea">
              <div>A MANO</div>
              <div className="tu">
                TU<small>sei qui</small>
              </div>
              <div className="av">CON UN SISTEMA</div>
            </div>
            <p className="sv-body sv-muted mt-6">Stessi limiti tuoi. Il primo che li risolve non lo raggiungi più.</p>
          </div>
          <Aura
            file="n5-fascia.webp"
            alt="silhouette in controluce davanti a tre finestre bianche"
            riga="«Non ha un nome. Ha un sistema. E ha i tuoi clienti.»"
          />
        </div>
      </div>
    </section>
  );
}
