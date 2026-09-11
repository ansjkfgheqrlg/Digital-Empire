import { Aura, auraPresente } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";

/**
 * N19 — Chiusura (COPY.md §N19). Se n8-dashboard.webp è nel manifest torna in filigrana come
 * sfondo assoluto sotto il testo (sv-container relative + Aura absolute inset-0 prima del blocco
 * testo, cosi' lo strato positivo successivo lo copre); altrimenti resta il fondo sv-chiusura
 * pieno, come previsto da COPY.md. "Trenta minuti" viene da FATTI.minutiChiamata.
 */
export function Chiusura() {
  return (
    <section id="chiusura" className="sv sv-chiusura sv-section" aria-labelledby="chiusura-h2">
      <div className="sv-container relative">
        {auraPresente("n8-dashboard.webp") && (
          <Aura
            file="n8-dashboard.webp"
            tratt="filigrana"
            className="absolute inset-0"
            alt="dashboard dell'Outreach Factory: invii di oggi, risposte in coda, lead in CRM"
          />
        )}

        <div className="relative">
          <p className="sv-eyebrow">{FATTI.minutiChiamata} minuti · niente slide</p>
          <h2 id="chiusura-h2" className="sv-h2 mt-3 max-w-[16ch]">
            In chiamata{" "}
            <span className="sv-it" style={{ color: "var(--sv-silver)" }}>
              la vedi girare.
            </span>
          </h2>
          <p className="sv-lead sv-muted mt-5 max-w-[48ch]">
            Lead veri che entrano, contenuti che si generano, la dashboard aperta. Poi decidi tu. Se non fa per te,
            ti abbiamo fatto perdere {FATTI.minutiChiamata} minuti e un caffè.
          </p>
          <CallCTA da="N19" label="Prenota la chiamata →" principale className="mt-8" />
          <p className="sv-small sv-muted mt-4">Calendly · {FATTI.minutiChiamata} minuti · zero canoni, mai</p>
        </div>
      </div>
    </section>
  );
}
