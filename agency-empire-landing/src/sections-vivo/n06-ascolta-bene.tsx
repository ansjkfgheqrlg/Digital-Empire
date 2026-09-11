import { Aura } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";

/* N6 — ASCOLTA BENE. (speedrun T8, tipografia-manifesto). Senza Barnum, con tre prove. Copy: COPY.md §N6. */
export function AscoltaBene() {
  return (
    <section id="ascolta-bene" className="sv sv-ink sv-section" aria-labelledby="ascolta-bene-h2">
      <div className="sv-container">
        <div className="due-col">
          <div>
            <h2 id="ascolta-bene-h2">
              <span className="manifesto">ASCOLTA BENE.</span>
            </h2>
            <p className="sv-lead sv-muted mt-7 max-w-[54ch]">
              Te lo diciamo come lo diremmo a noi stessi tre anni fa: chi ti sta passando davanti{" "}
              <b className="text-white">non è più bravo di te</b>. Non ha più budget. Non ha più clienti. Ha un sistema che manda{" "}
              {FATTI.messaggiGiorno} messaggi mentre tu ne scrivi {FATTI.dmAMano}, e pubblica ogni giorno mentre tu pubblichi quando
              riesci.
            </p>
            <div className="grid grid-cols-3 gap-3 mt-8 max-w-[560px]">
              <div className="prova" data-fonte="Outreach Factory di Digital Empire, dashboard mostrata in chiamata (FATTI.md)">
                <b>{FATTI.messaggiGiorno}</b>
                <span>messaggi al giorno, il sistema</span>
              </div>
              <div className="prova" data-fonte="aritmetica dichiarata: 30 DM × 5 minuti = 2,5 ore (FATTI.md)">
                <b>{FATTI.dmAMano}</b>
                <span>a mano, {FATTI.orePerDm.toLocaleString("it-IT")} ore tue</span>
              </div>
              <div className="prova" data-fonte="aritmetica dichiarata: 300 / 30 (FATTI.md)">
                <b>10×</b>
                <span>fai tu la divisione</span>
              </div>
            </div>
            <div className="mt-8">
              <CallCTA da="N6" label="Fammi vedere il sistema →" />
            </div>
          </div>
          <Aura
            file="n6-ascolta-bene.webp"
            alt="Silhouette controluce sulla soglia di una porta"
            riga="Non è più forte. È arrivato prima."
            tratt="negativo"
          />
        </div>
      </div>
    </section>
  );
}
