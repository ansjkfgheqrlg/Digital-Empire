import Link from "next/link";
import { LEGAL_RIGHE } from "@/lib/legal";

/**
 * N20 — Coda legale (COPY.md §N20). Firma composta da LEGAL_RIGHE (campo vuoto = riga assente,
 * mai "[da inserire]"). Nessun anno di copyright: FATTI.annoNascita è la nascita dell'agenzia, non
 * l'anno del copyright, e stamparlo lì sarebbe un fatto sbagliato — meglio nessun anno.
 */
export function Legale() {
  return (
    <footer id="legale" className="sv sv-ink-piatto sv-section" aria-label="Note legali e collegamenti">
      <div className="sv-container">
        <p className="sv-small sv-muted max-w-[80ch]">
          Nessuna promessa di fatturato. I numeri in questa pagina sono contati sui sistemi nostri e dei clienti
          citati, con le date; il risultato del tuo sistema dipende dalla tua offerta e dal tuo mercato, e lo
          scriviamo nel contratto prima di partire. L&apos;uso dei dati dei tuoi contatti resta responsabilità tua:
          il sistema fa quello che tu faresti a mano, più in fretta.
        </p>

        <div className="mt-6 pt-5 flex flex-wrap items-center justify-between gap-x-6 gap-y-3 sv-hair">
          <span className="sv-mono">{LEGAL_RIGHE.join(" · ")}</span>
          <nav aria-label="Collegamenti" className="flex flex-wrap gap-x-5 gap-y-2 sv-small">
            <Link href="/privacy/">Privacy</Link> · <Link href="/cookie/">Cookie</Link> · <Link href="/prenota/">Prenota</Link>
          </nav>
        </div>
      </div>
    </footer>
  );
}
