import { Aura } from "@/components/vivo/aura";

/* N2 — Specchio (tavola 3, speedrun T6): il lettore si riconosce prima di leggere una promessa.
   Copy: COPY-V2 §N2. Pattern Fabbrica: specchio. */
export function Specchio() {
  return (
    <section id="specchio" className="sv sv-carta" aria-labelledby="specchio-h2">
      <div className="container-default grid md:grid-cols-[300px_1fr] gap-10 md:gap-12 items-center py-16 md:py-20">
        <Aura
          file="n2-specchio.webp"
          alt="Uomo in giacca seduto con la mano sul viso"
          riga="Ogni mattina. Trenta DM. A mano. Da tre anni."
          tratt="carta"
          className="aspect-square rounded-[4px]"
        />
        <div>
          <h2 id="specchio-h2" className="sv-h2 max-w-[14ch]">
            Ti voglio bene, ma{" "}
            <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>
              lo stai facendo a mano.
            </span>
          </h2>
          <p className="sv-lead sv-muted mt-4 max-w-[52ch]">
            Non è colpa tua: nessuno ti ha mai mostrato il sistema. Ti hanno mostrato un tool, un
            abbonamento, un corso. Questo è quello che parte dal tuo telefono oggi:
          </p>
          <div className="dm mt-6 max-w-[460px]">
            <span className="sv-mono block mb-2" style={{ color: "#8a8478", letterSpacing: ".14em" }}>
              DM di oggi · concessionario, Veneto
            </span>
            <i>Ciao! Ho visto la tua concessionaria, complimenti 👏 Ti va se ti mando due info su come aumentare i contatti? 🚗</i>
            <em>— 30 volte al giorno, 2,5 ore, 3-7% di risposta. Perché sembra un template. Perché lo è.</em>
          </div>
        </div>
      </div>
    </section>
  );
}
