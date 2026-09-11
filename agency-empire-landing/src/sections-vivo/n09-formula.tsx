import { Aura } from "@/components/vivo/aura";
import { FATTI } from "@/lib/fatti";
import { LISTINO, SAAS_ANNO, MESI_PAREGGIO, eur } from "@/lib/listino";

/* N9 — La formula (pattern formula + ora-con) + il conto del canone. Copy: COPY.md §N9. */
export function Formula() {
  const ore = FATTI.orePerDm.toLocaleString("it-IT");
  const lOra = Math.round(FATTI.dmAMano / FATTI.orePerDm);
  return (
    <section id="formula" className="sv sv-carta sv-section" aria-labelledby="formula-h2">
      <div className="sv-container">
        <div className="due-col">
          <div>
            <p className="sv-eyebrow">La produttività non è alzarsi alle 5</p>
            <h2 id="formula-h2" className="sv-h2 mt-3 max-w-[16ch]">
              Produttività = <span className="sv-it" style={{ color: "var(--sv-orange)" }}>cose utili fatte / ore tue.</span>
            </h2>

            <div className="mt-8 grid sm:grid-cols-2 gap-4">
              <div className="sv-card" style={{ borderColor: "var(--sv-hair-light)" }}>
                <p className="sv-mono">Ora</p>
                <ul className="mt-3 sv-body sv-muted space-y-2">
                  <li>{FATTI.dmAMano} messaggi in {ore} ore = {lOra} l&apos;ora</li>
                  <li>un carosello: un pomeriggio</li>
                  <li>follow-up: quelli che ti ricordi</li>
                </ul>
              </div>
              <div className="sv-card" style={{ borderColor: "var(--sv-orange)" }}>
                <p className="sv-mono" style={{ color: "var(--sv-orange)" }}>Con il sistema</p>
                <ul className="mt-3 sv-body space-y-2">
                  <li>{FATTI.messaggiGiorno} messaggi in 0 ore tue</li>
                  <li>un carosello, un reel e una caption al giorno in 0 ore tue</li>
                  <li>follow-up: tutti</li>
                </ul>
              </div>
            </div>
            <p className="sv-lead mt-6 max-w-[52ch]">
              {FATTI.messaggiGiorno} / 0 non si può dividere. È il punto: le ore tue non sono più al denominatore.
            </p>

            <h3 className="sv-h3 mt-10">Il conto del canone</h3>
            <p className="sv-body sv-muted mt-3 max-w-[56ch]">
              Outreach Factory: <span data-prezzo="outreach">{eur(LISTINO.outreach)}</span> una volta. Un SaaS di outreach:{" "}
              {eur(LISTINO.saasMese)} al mese, {eur(SAAS_ANNO)} l&apos;anno, per sempre. In {MESI_PAREGGIO} mesi hai pareggiato — e dal
              ventunesimo il tuo gira a costo zero. Fai tu il conto sugli anni.
            </p>
            <p className="sv-small sv-muted mt-6 max-w-[56ch]">
              E il metodo con cui scrive — APSOC: Attenzione, Problema, Promessa, Social proof, Obiezioni, CTA — è lo stesso che usiamo
              per le nostre pagine. Questa compresa.
            </p>
          </div>
          <Aura
            file="n9-formula.webp"
            alt="Uomo con occhiali che conta banconote dentro un'asciugatrice"
            riga="Dodici canoni all'anno per un tool che non sa chi sei."
            tratt="carta"
          />
        </div>
      </div>
    </section>
  );
}
