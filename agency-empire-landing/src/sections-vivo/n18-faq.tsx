import { LISTINO, eur } from "@/lib/listino";
import { FATTI } from "@/lib/fatti";

/**
 * N18 — FAQ (COPY.md §N18), 9 domande in <details> nativi. Decisione: "50% all'ordine e 50% alla
 * consegna" resta testo piatto — è la condizione di pagamento (listino.ts porta LISTINO.acconto
 * come frazione 0.5 per i calcoli, non un valore da stampare come percentuale in questa frase).
 */
const FAQ: [string, string][] = [
  [
    "Devo saperne di tecnica per usarlo?",
    "No. Ti consegniamo il sistema funzionante, collegato ai tuoi strumenti, e facciamo 1 sessione di formazione al tuo team: come leggere la dashboard, cosa fare se un alert si accende. Il resto gira da solo.",
  ],
  [
    "Quanto tempo ci vuole?",
    `${FATTI.giorniSetup} giorni lavorativi dal contratto firmato. Se il tuo caso è su misura te lo diciamo prima di firmare, non dopo.`,
  ],
  [
    "Quanto costa?",
    `Outreach Factory ${eur(LISTINO.outreach)}, Content Factory ${eur(LISTINO.content)}, Second Brain ${eur(LISTINO.brain)}, tutti e tre ${eur(LISTINO.engine)}. Una tantum, 50% all'ordine e 50% alla consegna. Zero canoni mensili.`,
  ],
  [
    "Ho bisogno di un server dedicato?",
    `No. Un VPS cloud (DigitalOcean, Hetzner, AWS) da ${FATTI.vpsMeseMin}-${FATTI.vpsMeseMax} € al mese. L'importante è che sia tuo: nessun lock-in sulla nostra infrastruttura.`,
  ],
  [
    "Posso comprare un solo sistema?",
    "Sì. Ognuno dei tre si compra da solo. Molti partono da uno e aggiungono gli altri dopo aver visto i risultati.",
  ],
  [
    "E se smette di funzionare?",
    `${FATTI.giorniMonitoraggio} giorni di monitoraggio con alert dopo il go-live: se qualcosa si ferma lo vediamo noi prima di te. Poi ${FATTI.giorniSupporto} giorni di supporto, e per quei ${FATTI.giorniSupporto} giorni ogni cambiamento di piattaforma lo gestiamo noi. Dopo, se vuoi, manutenzione — ma è una scelta, non una condizione.`,
  ],
  [
    "È mio il codice?",
    "Sì. Gira sul tuo server, con i tuoi account. Se domani ci licenzi, resta lì e continua a girare.",
  ],
  [
    "Su quali piattaforme funziona l'outreach?",
    "Email e DM Instagram, da sessioni browser reali con proxy residenziali e digitazione a velocità umana; WhatsApp per i concessionari. Non usiamo API che ti fanno bannare l'account.",
  ],
  [
    "C'è una garanzia?",
    `Sì, ${FATTI.giorniGaranzia} giorni: se il sistema non funziona come scritto lo sistemiamo noi senza costi. Se non è risolvibile, rimborso integrale.`,
  ],
];

export function Faq() {
  return (
    <section id="faq" className="sv sv-carta sv-section" aria-labelledby="faq-h2">
      <div className="sv-container">
        <h2 id="faq-h2" className="sv-h2 max-w-[16ch]">
          Domande <span className="sv-it" style={{ color: "var(--sv-orange)" }}>che ci fanno davvero.</span>
        </h2>
        <div className="mt-8 max-w-[72ch]">
          {FAQ.map(([q, a]) => (
            <details key={q} className="sv-faq">
              <summary>{q}</summary>
              <p>{a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
