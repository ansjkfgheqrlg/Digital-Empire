import { FATTI } from "@/lib/fatti";
import { LISTINO, eur, MESI_PAREGGIO, SAAS_ANNO } from "@/lib/listino";

/* AGGIUNTA A18 (Dossier 38 v2, Atto VI) — «Quanto costa»: la formula, oggi contro il sistema.
   Inserita dopo <Clarity />. Superficie ink, h ≤ 500. 0 KB di JS.
   Ogni numero da FATTI/LISTINO (§6/§8): 30 DM × 5 min = 2,5 ore è l'aritmetica dichiarata in FATTI.md (V9);
   il pareggio è MESI_PAREGGIO = outreach / saasMese. Niente «55 ore al mese»: non è in FATTI.md, quindi la frase non lo dice. */
export function QuantoCosta() {
  const ore = FATTI.orePerDm.toLocaleString("it-IT");
  return (
    <div className="vivo">
      <section id="quanto-costa" className="sv sv-ink sv-section quanto-costa" aria-labelledby="quanto-costa-h2">
        <div className="sv-container">
          <span className="sv-eyebrow">Quanto costa, davvero</span>
          <h2 id="quanto-costa-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Il conto lo fai <span className="sv-it">in una riga.</span>
          </h2>

          <div className="qc-formula" role="group" aria-label="Oggi contro il sistema">
            <div className="qc-col c-grana">
              <span className="sv-eyebrow">Oggi</span>
              <span className="qc-riga qc-riga--muta">
                {FATTI.dmAMano} DM × {FATTI.minutiPerDm} min
              </span>
              <span className="qc-riga qc-riga--tot">= {ore} ore al giorno</span>
            </div>
            <span className="qc-vs" aria-hidden="true">
              vs
            </span>
            <div className="qc-col qc-col--sistema c-grana">
              <span className="sv-eyebrow">
                <b>Con il sistema</b>
              </span>
              <span className="qc-riga" data-prezzo="outreach">
                {eur(LISTINO.outreach)} una volta
              </span>
              <span className="qc-riga qc-riga--muta">{FATTI.messaggiGiorno} messaggi al giorno</span>
              <span className="qc-riga qc-riga--tot">
                0 ore tue · {eur(FATTI.canoneMese)} al mese
              </span>
            </div>
          </div>

          <p className="sv-lead sv-muted qc-chiusa">
            Un SaaS da <span data-prezzo="saasMese">{eur(LISTINO.saasMese)}</span>/mese costa {eur(SAAS_ANNO)} l&apos;anno, per sempre. Il
            sistema <b>pareggia al {MESI_PAREGGIO}º mese</b> — e da lì gira a costo zero.
          </p>
        </div>
      </section>
    </div>
  );
}
