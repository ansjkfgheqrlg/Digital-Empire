import { FATTI } from "@/lib/fatti";
import { LISTINO } from "@/lib/listino";

/* AGGIUNTA A21 (Dossier 38 v2, Atto VI) — «FAQ del contratto»: due gruppi di <details>, la prima aperta.
   Inserita dopo <FAQ />. Superficie carta, h ≤ 700. 0 KB di JS (details/summary nativi).
   Lo stesso array FAQ_CONTRATTO genera anche il JSON-LD FAQPage dentro la sezione: una fonte, due usi.
   Numeri da FATTI (§6/§8): VPS 5-20 €/mese, setup 7 giorni. Il 50/50 è la regola d'acconto del listino (LISTINO.acconto = 0.5). */
const ACCONTO = `${Math.round(LISTINO.acconto * 100)}%`;
const SALDO = `${Math.round((1 - LISTINO.acconto) * 100)}%`;

export type VoceFaq = { q: string; a: string };
export type GruppoFaq = { titolo: string; voci: VoceFaq[] };

export const FAQ_CONTRATTO: GruppoFaq[] = [
  {
    titolo: "Sistema",
    voci: [
      { q: "Chi possiede il codice?", a: "Tu, dal primo giorno: repository a tuo nome." },
      {
        q: "Su quale server gira?",
        a: `Sul tuo (VPS ${FATTI.vpsMeseMin}-${FATTI.vpsMeseMax} €/mese) o su uno che apriamo a tuo nome.`,
      },
      { q: "Cosa succede se lo spegnete?", a: "Non possiamo: non abbiamo accessi che tu non ci dia." },
      { q: "Quanto dura il setup?", a: `${FATTI.giorniSetup} giorni lavorativi dal contratto.` },
    ],
  },
  {
    titolo: "Contratto e pagamento",
    voci: [
      { q: "Come si paga?", a: `${ACCONTO} alla firma, ${SALDO} al go-live, con fattura.` },
      { q: "Ci sono canoni?", a: "No. Paghi il tuo VPS e le API a consumo." },
      { q: "Se cambiamo idea a metà?", a: "Tieni il lavoro fatto fino a lì, pagato quello." },
      { q: "Rate?", a: "Sì, su richiesta, in contratto." },
    ],
  },
];

function jsonLdFaq(gruppi: GruppoFaq[]) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: gruppi.flatMap((g) =>
      g.voci.map((v) => ({
        "@type": "Question",
        name: v.q,
        acceptedAnswer: { "@type": "Answer", text: v.a },
      })),
    ),
  };
}

export function FaqContratto() {
  return (
    <div className="vivo">
      <section id="faq-contratto" className="sv sv-carta sv-section faq-contratto" aria-labelledby="faq-contratto-h2">
        <div className="sv-container">
          <span className="sv-eyebrow">Le domande del contratto</span>
          <h2 id="faq-contratto-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Prima di firmare, <span className="sv-it">le risposte scritte.</span>
          </h2>
          <div className="fqc-gruppi">
            {FAQ_CONTRATTO.map((g, gi) => (
              <div key={g.titolo} className="fqc-gruppo">
                <h3 className="sv-h3">{g.titolo}</h3>
                {g.voci.map((v, vi) => (
                  <details key={v.q} className="fqc-voce" open={gi === 0 && vi === 0 ? true : undefined}>
                    <summary>{v.q}</summary>
                    <p className="sv-body">{v.a}</p>
                  </details>
                ))}
              </div>
            ))}
          </div>
        </div>
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLdFaq(FAQ_CONTRATTO)) }} />
      </section>
    </div>
  );
}
