/* N13 — Prove, non frasi (C3.2: solo casi con nome; le testimonianze con faccia arrivano quando ci sono,
   con nome, foto e link — mai screenshot muti). Copy: COPY-V2 §N13. */
export function Prove() {
  return (
    <section id="prove" className="sv sv-ink-piatto sv-hair" aria-labelledby="prove-h2">
      <div className="container-default py-16 md:py-20">
        <p className="sv-eyebrow">Prove, non frasi</p>
        <h2 id="prove-h2" className="sv-h2 mt-3 max-w-[18ch]">
          Due casi con nome. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Le facce le stiamo raccogliendo.</span>
        </h2>

        <div className="mt-10 grid md:grid-cols-2 gap-px" style={{ background: "var(--sv-hair)" }}>
          <article className="p-6 md:p-7" style={{ background: "var(--sv-ink)" }} data-fonte="storico PreventivoForge Novacar, annunci reali 3-13 luglio 2026">
            <div className="sv-mono" style={{ color: "var(--sv-orange)" }}>Novacar — concessionario</div>
            <p className="sv-body sv-muted mt-3">
              65 preventivi in dieci giorni, 11 marche, due minuti l&apos;uno, sei controlli automatici prima di ogni PDF.
            </p>
            <p className="sv-body mt-3 text-white">
              Cosa non è andato al primo giro: le foto tagliate nell&apos;impaginazione. Regola del cliente, non nostra: ora è il controllo numero 4.
            </p>
          </article>
          <article className="p-6 md:p-7" style={{ background: "var(--sv-ink)" }} data-fonte="log invii Preventa Outreach Automation (Areus CRM), 2026">
            <div className="sv-mono" style={{ color: "var(--sv-orange)" }}>Preventa — concessionari, outreach</div>
            <p className="sv-body sv-muted mt-3">
              Lo stesso motore di outreach, puntato sui saloni: scraping, qualifica, messaggi WhatsApp da un profilo vero, lead in Areus.
            </p>
            <p className="sv-body mt-3 text-white">Cinquanta contatti al giorno, zero fatti a mano.</p>
          </article>
        </div>

        <p className="sv-small sv-muted mt-5 max-w-[70ch]">
          Testimonianze con nome e faccia: le stiamo raccogliendo, e le metteremo qui solo con nome, foto e link.
          Finché non ci sono, ci sono i numeri sopra — e la dashboard in chiamata.
        </p>
      </div>
    </section>
  );
}
