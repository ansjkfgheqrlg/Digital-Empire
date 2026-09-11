import { Aura } from "@/components/vivo/aura";

/* N11 — Chi siamo: la stanza a parte (#202021, speedrun T16, usato una volta sola).
   Qui NIENTE still: facce vere. Finché i ritratti mancano, <Aura/> mostra la silhouette col nome
   (manifest: team-max, team-gael — dipende da Max, non blocca). Copy: COPY-V2 §N11. */
export function ChiSiamo() {
  return (
    <section id="chi-siamo" className="sv sv-stanza" aria-labelledby="chi-h2">
      <div className="container-default grid md:grid-cols-2 gap-10 items-center py-16 md:py-20">
        <div className="grid grid-cols-2 gap-3">
          <Aura
            file="n11-max.webp"
            alt="Max, ritratto in luce di taglio"
            className="aspect-[4/5] rounded-[4px]"
            segnaposto={{ nome: "Max", ruolo: "ritratto vero · luce AURA" }}
          />
          <Aura
            file="n11-gael.webp"
            alt="Gael, ritratto in luce di taglio"
            className="aspect-[4/5] rounded-[4px]"
            segnaposto={{ nome: "Gael", ruolo: "ritratto vero · luce AURA" }}
          />
        </div>
        <div>
          <p className="sv-eyebrow">Chi c&apos;è dietro</p>
          <h2 id="chi-h2" className="sv-h2 mt-3 max-w-[18ch]">
            Parli con chi ha le mani sui workflow.{" "}
            <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Per scelta, non per limite.</span>
          </h2>
          <p className="sv-body sv-muted mt-5 max-w-[50ch]">
            Siamo due. Max ha costruito il primo Outreach Factory per sé, perché mandava trenta DM a mano ogni
            mattina e non ne poteva più. Gael costruisce e tiene in piedi i sistemi dei clienti. Nessun account
            manager in mezzo: chi ti risponde è chi ha scritto il codice.
          </p>
          <p className="sv-body sv-muted mt-4 max-w-[50ch]">
            Sì: alla fine di questa pagina ti proponiamo di lavorare insieme. Ci guadagniamo tutti e due, o non lo
            faremmo. Prima però ti mostriamo il sistema che gira — il nostro, quello con cui probabilmente ti abbiamo trovato.
          </p>
          <p className="sv-mono mt-6" style={{ color: "var(--sv-orange)" }}>
            L&apos;agenzia progettata per essere licenziata
          </p>
          <p className="sv-small sv-muted mt-1 max-w-[50ch]">
            Ti consegniamo un sistema che cammina da solo, non una dipendenza.
          </p>
        </div>
      </div>
    </section>
  );
}
