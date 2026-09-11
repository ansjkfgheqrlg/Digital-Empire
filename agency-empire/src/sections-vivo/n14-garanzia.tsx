import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N14 — Garanzia: una frase, una condizione, zero asterischi (tavola 8). Copy: COPY-V2 §N14. */
export function Garanzia() {
  return (
    <section id="garanzia" className="sv sv-carta" aria-labelledby="garanzia-h2">
      <div className="container-default grid md:grid-cols-2 gap-10 items-center py-16 md:py-20">
        <Aura
          file="n14-garanzia.webp"
          alt="Elmo da cavaliere medievale, visiera abbassata, luce laterale"
          riga={'Se il sistema non gira come scritto, lo rifacciamo. Non "ti richiamiamo".'}
          tratt="acciaio"
          className="aspect-[4/5] max-h-[460px] rounded-[4px]"
          objectPosition="50% 30%"
        />
        <div>
          <p className="sv-eyebrow"><b>Garanzia</b> · una frase, una condizione</p>
          <h2 id="garanzia-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Funziona come scritto nel contratto,{" "}
            <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>o lo rifacciamo noi.</span>
          </h2>
          <p className="sv-body sv-muted mt-5 max-w-[48ch]">
            Trenta giorni di monitoraggio dopo il go-live, dashboard aperta, alert automatici. Se un risultato
            scritto nel contratto — messaggi mandati, contenuti pubblicati, lead nel CRM — non arriva, il lavoro
            per farlo arrivare è nostro e non costa niente. Nessun asterisco.
          </p>
          <p className="sv-small mt-4" style={{ color: "#6f6a62" }}>
            Ti garantiamo che funziona come scritto. Chi ti garantisce i clienti, diffidane.
          </p>
          <a href="/prenota" className="btn-gold mt-8" data-cta="garanzia">
            Va bene, vediamolo <ArrowRight className="h-4 w-4" />
          </a>
        </div>
      </div>
    </section>
  );
}
