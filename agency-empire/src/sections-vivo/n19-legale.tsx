import { LEGAL } from "@/lib/legal";

/* N19 — Coda legale: disclaimer a 88ch (armageddon T6: "set wide enough to actually be read"),
   firma con i soli dati presenti in lib/legal.ts. Copy: COPY-V2 §N19. Pattern Fabbrica: coda-legale. */
export function Legale() {
  const firma = [
    LEGAL.ragioneSociale,
    LEGAL.partitaIva && `P.IVA ${LEGAL.partitaIva}`,
    LEGAL.indirizzo,
  ].filter(Boolean);

  return (
    <footer id="legale" className="sv sv-ink-piatto sv-hair" aria-label="Note legali e collegamenti">
      <div className="container-default py-10 md:py-12">
        <p className="sv-small sv-muted" style={{ maxWidth: "88ch", lineHeight: 1.75 }}>
          Nessuna promessa di fatturato. I numeri in questa pagina sono misurati sui sistemi nostri e dei clienti
          citati, con date; il risultato del tuo sistema dipende dalla tua offerta e dal tuo mercato, e lo scriviamo
          nel contratto prima di partire. L&apos;uso dei dati dei tuoi contatti resta responsabilità tua: il sistema fa
          quello che tu faresti a mano, più in fretta.
        </p>
        <div className="mt-6 pt-5 flex flex-wrap items-center justify-between gap-x-6 gap-y-3 sv-mono" style={{ borderTop: "1px solid var(--sv-hair)", color: "var(--sv-silver-dim)", textTransform: "none", letterSpacing: ".04em" }}>
          <span>{firma.join(" · ")}</span>
          <nav className="flex flex-wrap gap-x-5 gap-y-2" aria-label="Collegamenti">
            <a className="hover:text-white transition-colors" href={`mailto:${LEGAL.email}`}>{LEGAL.email}</a>
            <a className="hover:text-white transition-colors" href="https://www.instagram.com/crea.illtuo_impero" rel="noopener" target="_blank">Instagram</a>
            <a className="hover:text-white transition-colors" href="/prenota">Prenota</a>
            <a className="hover:text-white transition-colors" href={LEGAL.privacyUrl}>Privacy</a>
            <a className="hover:text-white transition-colors" href={LEGAL.cookieUrl}>Cookie</a>
          </nav>
        </div>
      </div>
    </footer>
  );
}
