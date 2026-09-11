import { Aura } from "@/components/vivo/aura";

/* N15 — Le sei cose che stai pensando: obiezione in bocca al lettore (V7), «No.» secco e conto delegato (V4).
   Copy: COPY-V2 §N15. */
const OBIEZIONI: [string, string, string][] = [
  ["Quindi c'è un canone mensile.", "No.", "Il codice è tuo. Fai tu il conto: 12 × quello che paghi oggi al tool che non sa chi sei, per ogni anno che lo tieni."],
  ["Costa troppo per quello che fa.", "No.", "Un sistema da 5.000 € manda 300 messaggi al giorno per anni. Fai tu il conto: quante ore al mese passi a fare outreach a mano, per il tuo costo orario."],
  ["Ho già provato gli strumenti AI, non funzionano.", "Giusto.", "Gli strumenti da soli sono tab aperti. Quello che manca è la logica che li fa lavorare insieme, i trigger, la gestione degli errori. È quello che costruiamo. Lo strumento non è il sistema."],
  ["Poi dipendo da voi per sempre.", "No.", "Siamo l'agenzia progettata per essere licenziata: 90 giorni di supporto, poi cammini da solo. Se ci richiami è perché vuoi il secondo sistema, non perché il primo si è rotto."],
  ["Non vi conosco abbastanza per fidarmi.", "Giusto.", "Per questo la prima chiamata è il sistema in live, non una presentazione. Niente slide. Niente demo finta. Niente \"ti richiamiamo\". Trenta minuti, e decidi con quello che hai visto."],
  ["Mi mostrerete delle slide.", "No.", "Trenta minuti, il sistema in live, 0 slide. Vedi sopra."],
];

export function Obiezioni() {
  return (
    <section id="obiezioni" className="sv sv-ink" aria-labelledby="obiezioni-h2">
      <div className="container-default py-16 md:py-20">
        <h2 id="obiezioni-h2" className="sv-h2 max-w-[18ch]">
          Le sei cose che stai pensando. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>In ordine.</span>
        </h2>
        <div className="mt-10 grid md:grid-cols-[1fr_360px] gap-10 items-start">
          <dl className="m-0">
            {OBIEZIONI.map(([q, no, a]) => (
              <div key={q} className="sv-hair py-4">
                <dt className="sv-body font-bold text-white">
                  <span style={{ color: "var(--sv-silver-dim)" }}>«</span>{q}<span style={{ color: "var(--sv-silver-dim)" }}>»</span>
                </dt>
                <dd className="sv-body sv-muted mt-1.5 m-0 max-w-[62ch]">
                  <b style={{ color: "var(--sv-orange)", fontWeight: 900, marginRight: 6 }}>{no}</b>{a}
                </dd>
              </div>
            ))}
          </dl>
          <Aura
            file="n15-obiezioni.webp"
            alt="Uomo con occhiali da sole che saluta dal finestrino di un'auto"
            riga="Ci licenzi quando vuoi. Il codice resta tuo. Ciao."
            className="aspect-square rounded-[4px] md:sticky md:top-24"
          />
        </div>
      </div>
    </section>
  );
}
