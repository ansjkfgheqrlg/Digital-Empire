/* N17 — FAQ native <details> (armageddon T5: si aprono con JavaScript spento, allineate a sinistra
   "perché si leggono"). Copy: COPY-V2 §N17. Pattern Fabbrica: faq-native. */
const FAQ: [string, string][] = [
  ["Devo saperne di tecnica per usarlo?", "No. Ti consegniamo il sistema funzionante, collegato ai tuoi strumenti, e ti formiamo in 60 minuti: come leggere la dashboard, cosa fare se un alert si accende. Il resto gira da solo."],
  ["Quanto tempo ci vuole?", "Sette giorni per Outreach Factory e Content Factory standard. Tre-quattro settimane se il sistema è su misura (multi-canale, CRM particolari, integrazioni tue). Te lo diciamo prima di firmare, non dopo."],
  ["Quanto costa?", "Da 5.000 € a sistema, una tantum. I più complessi arrivano a 15.000 €. Il prezzo esatto per il tuo caso lo diciamo in chiamata, dopo aver visto come lavori. Zero canoni mensili."],
  ["Funziona davvero senza che io tocchi niente?", "Per i compiti che scriviamo insieme nel briefing, sì. Tu decidi cosa automatizzare, noi lo costruiamo. Quello che sta fuori dal perimetro resta tuo — e te lo diciamo prima."],
  ["E se smette di funzionare?", "Trenta giorni di monitoraggio con alert dopo il go-live: se qualcosa si ferma lo vediamo noi prima di te. Poi 90 giorni di supporto. Dopo, se vuoi, manutenzione mensile — ma è una scelta, non una condizione."],
  ["È mio il codice?", "Sì. Gira sui tuoi server, con i tuoi account. Se domani ci licenzi, resta lì e continua a girare."],
  ["Fate ancora landing page?", "Sì, come servizio a parte. Ma se il problema è l'operatività, una landing non lo risolve: lo sposta."],
  ["Su quali piattaforme funziona l'outreach?", "Email, DM Instagram e WhatsApp, da sessioni browser reali con proxy residenziali e digitazione a velocità umana. Non usiamo API che ti fanno bannare l'account."],
];

export function Faq() {
  return (
    <section id="faq" className="sv sv-carta" aria-labelledby="faq-h2">
      <div className="container-default py-16 md:py-20">
        <h2 id="faq-h2" className="sv-h2 max-w-[16ch]">
          Domande <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>che ci fanno davvero.</span>
        </h2>
        <div className="mt-8 max-w-[760px]">
          {FAQ.map(([q, a]) => (
            <details key={q} className="sv-faq">
              <summary style={{ color: "#1c1c1c" }}>{q}</summary>
              <p>{a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
