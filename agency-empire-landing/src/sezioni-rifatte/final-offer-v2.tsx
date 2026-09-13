import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";

/* RIFATTA 47 — FinalOffer «AI Proprietaria» (BRIEF F3, blocco B; 39B §2 r.47 e §3.1 n.1).
   Sostituisce <FinalOffer /> in page.tsx (lo scambio lo fa Emperator). Il TESTO è copiato parola per parola
   da src/components/sections/final-offer.tsx, nello stesso ordine di lettura: eyebrow → lead → («Sistema Online»,
   «v1.0 · Digital Empire», «AI Proprietaria»: erano dentro il mock-schermo, qui restano come riga mono + titolo,
   senza schermo) → 5 voci → «Investimento» → prezzo → «Secondo il sistema scelto» → riga dei prezzi →
   «Pagamento unico · Zero canoni» → CTA (stesso testo del CallCTA di giugno: etichetta + sottoetichetta) →
   «Garanzia 30 giorni · Rateizzazione disponibile». Cambia solo la forma: ink piatto, colonna 1100, niente
   cornice a gradiente, niente mock-schermo, prezzo a 44 px, checklist bordata (39A E42), UNA CTA che va a
   /prenota/ (mai al dominio esterno del corso). I prezzi in giugno sono stringhe letterali (non da @/lib/constants
   né da @/lib/listino): restano letterali per non cambiare una virgola del testo. 0 KB di JS.
   Obiettivo ≤ 900 px. CSS: src/app/rifatte-b.css (.rb-fo*). */

const features = [
  "Sistema AI completo installato sui tuoi server",
  "Dashboard web custom per monitorare e configurare",
  "Codice sorgente in chiaro — asset tuo per sempre",
  "APSOC Framework calibrato sul tuo brand e ICP",
  "Garanzia 30 giorni · Rimborso se non funziona",
];

export function FinalOfferV2() {
  return (
    <div className="vivo">
      <section id="offerta" className="sv sv-ink-piatto sv-section rb-fo" aria-labelledby="offerta-h3">
        <div className="sv-container">
          <header className="rb-fo-testa">
            <span className="sv-eyebrow">Digital Empire · Implementazione AI</span>
            <p className="sv-lead rb-fo-lead">
              Installa il tuo <strong>sistema AI proprietario</strong> e fai girare l&apos;operatività
              da sola — zero canoni mensili, codice tuo per sempre.
            </p>
            <p className="sv-mono rb-fo-stato">
              <span><i aria-hidden="true" />Sistema Online</span>
              <span className="rb-accento">v1.0 · Digital Empire</span>
            </p>
            <h3 id="offerta-h3" className="sv-h2 rb-fo-titolo">AI Proprietaria</h3>
          </header>

          <div className="rb-fo-griglia">
            <ul className="rb-fo-lista rb-grana">
              {features.map((f) => (
                <li key={f}>{f}</li>
              ))}
            </ul>

            <div className="rb-fo-prezzo rb-grana">
              <span className="sv-mono">Investimento</span>
              <div className="rb-fo-cifra">da €2.500</div>
              <span className="sv-mono sv-muted">Secondo il sistema scelto</span>
              <p className="rb-fo-riga sv-muted">
                Second Brain €2.500 · Content Factory €3.500 · Outreach Factory €4.000 · tutti e 3 (Engine Room) €8.000
              </p>
              <span className="sv-mono rb-accento">Pagamento unico · Zero canoni</span>
              <Link href={prenotaDa("F47")} className="sv-btn rb-btn rb-fo-btn" data-cta>
                Prenota una Chiamata Gratuita
                <small>30 min · Gratuita · Zero impegno</small>
              </Link>
              <span className="sv-mono sv-muted">Garanzia 30 giorni · Rateizzazione disponibile</span>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
