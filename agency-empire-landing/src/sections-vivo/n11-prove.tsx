import { FATTI } from "@/lib/fatti";

/**
 * N11 — Prove, solo vere (COPY.md §N11). Le cifre Novacar vengono da FATTI.novacar.*, i 50 di
 * Preventa da FATTI.preventaWhatsappGiorno; il resto del testo resta quello del COPY, parola per
 * parola. Il caso-3 non porta data-fonte: come dice COPY.md, la fonte è la chiamata stessa.
 */
export function Prove() {
  return (
    <section id="prove" className="sv sv-carta sv-section" aria-labelledby="prove-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">Prove, non frasi</p>
        <h2 id="prove-h2" className="sv-h2 mt-3 max-w-[24ch]">
          Un caso coi numeri contati. <span className="sv-it" style={{ color: "var(--sv-orange)" }}>Le facce le stiamo raccogliendo.</span>
        </h2>

        <div className="mt-10 grid gap-6 md:grid-cols-3">
          <article
            className="sv-card"
            style={{ borderColor: "var(--sv-hair-light)" }}
            data-fonte="company/Memory/checkpoints/CP-20260723-003.md"
          >
            <p className="sv-body">
              <strong>Un concessionario, luglio 2026 — preventivi.</strong> {FATTI.novacar.preventivi} preventivi
              generati su annunci veri in dieci giorni (3-13 luglio), {FATTI.novacar.marche} marche, circa{" "}
              {FATTI.novacar.minutiPerPdf} minuti dal link al PDF, {FATTI.novacar.controlli} controlli automatici
              prima di ogni PDF. Lo diciamo intero: quei {FATTI.novacar.preventivi} includono i nostri collaudi, e
              non sostengono che il cliente venda di più. Cosa non è andato al primo giro: le foto tagliate
              nell&apos;impaginazione. Regola del cliente, ora è il controllo numero 4.
            </p>
          </article>

          <article
            className="sv-card"
            style={{ borderColor: "var(--sv-hair-light)" }}
            data-fonte=".claude/skills/avvia-outreach-preventa/SKILL.md"
          >
            <p className="sv-body">
              <strong>Concessionari — outreach su WhatsApp.</strong> Lo stesso motore di outreach, puntato sui
              saloni: scraping, qualifica, messaggi da un profilo vero, lead nel CRM. Fino a{" "}
              {FATTI.preventaWhatsappGiorno} contatti al giorno, zero fatti a mano.
            </p>
          </article>

          <article className="sv-card" style={{ borderColor: "var(--sv-hair-light)" }}>
            <p className="sv-body">
              <strong>Il nostro.</strong> L&apos;Outreach Factory con cui probabilmente ti abbiamo trovato gira per
              noi ogni giorno. In chiamata la vedi: invii di oggi, risposte in coda, lead entrati.
            </p>
          </article>
        </div>

        <p className="sv-small sv-muted mt-6 max-w-[70ch]">
          Testimonianze con nome e faccia: le metteremo qui solo con nome, foto e link. Finché non ci sono, ci sono i
          numeri sopra — e la dashboard in chiamata. Il nome del cliente lo scriviamo quando ce lo autorizza per
          iscritto.
        </p>
      </div>
    </section>
  );
}
