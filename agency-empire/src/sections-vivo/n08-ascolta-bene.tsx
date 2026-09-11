import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N8 — ASCOLTA BENE. (speedrun T8, tavola 6). La casella arancione e' tipografia-manifesto FUORI gerarchia
   (aria-hidden), il vero h2 e' visivamente nascosto: un solo H1 in pagina, i titoli restano puliti.
   Copy: COPY-V2 §N8. Pattern Fabbrica: tipografia-manifesto. */
export function AscoltaBene() {
  return (
    <section id="ascolta-bene" className="sv sv-ink" aria-labelledby="ascolta-h2">
      <div className="container-default grid md:grid-cols-[1fr_340px] gap-10 md:gap-12 items-center py-16 md:py-20">
        <div>
          <h2 id="ascolta-h2" className="sr-only">Ascolta bene: chi ti passa davanti ha un sistema, non più talento</h2>
          <p className="manifesto" aria-hidden>ASCOLTA BENE.</p>
          <p className="sv-lead sv-muted mt-6 max-w-[52ch]">
            Te lo diciamo come lo diremmo a noi stessi tre anni fa: chi ti sta passando davanti{" "}
            <b className="text-white">non è più bravo di te</b>. Non ha più budget. Non ha più clienti. Ha un sistema
            che manda 300 messaggi mentre tu ne scrivi 30, e pubblica ogni giorno mentre tu pubblichi quando riesci.
          </p>
          <div className="mt-6 grid grid-cols-3 gap-2 max-w-[520px]" data-fonte="Outreach Factory: capacita' misurata sulla dashboard (mostrata in chiamata); 30 DM a mano = 2,5 h misurate sul flusso manuale di Max, 2025-2026">
            <div className="prova" data-fonte="dashboard Outreach Factory, mostrata in chiamata"><b>300</b><span>messaggi/giorno, il sistema</span></div>
            <div className="prova" data-fonte="flusso manuale di Max, 2025-2026: 30 DM in 2,5 ore"><b>30</b><span>a mano, 2,5 ore tue</span></div>
            <div className="prova" data-fonte="300 / 30, aritmetica"><b>10×</b><span>fai tu la divisione</span></div>
          </div>
          <a href="/prenota" className="btn-gold mt-8" data-cta="ascolta-bene">
            Fammi vedere il sistema <ArrowRight className="h-4 w-4" />
          </a>
        </div>
        <Aura
          file="n8-ascolta-bene.webp"
          alt="Pugile in piedi sopra l'avversario a terra, sul ring"
          riga="Non è più forte. È arrivato prima."
          className="aspect-[3/4] rounded-[4px]"
          objectPosition="50% 15%"
        />
      </div>
    </section>
  );
}
