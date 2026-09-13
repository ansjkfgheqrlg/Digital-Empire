import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";
import { LISTINO, eur } from "@/lib/listino";

/* AGGIUNTA A17 (Dossier 38 v2, Atto VI) — «La tessera»: cosa c'è scritto sulla tua, in due colonne.
   Inserita dopo <PricingROI />. Superficie carta, h ≤ 600. CTA di vendita ammessa (Atto VI, §15).
   Prezzi da LISTINO, giorni da FATTI (§6/§8): nessun numero scritto a mano. Il QR finto in CSS è vietato; l'indirizzo in mono
   che stava al suo posto andava a capo dentro la tessera ed è stato tolto il 13/09 sera (F3 blocco C, 39B r.37). */

export function Tessera() {
  const voci = [
    "Codice consegnato, tuo",
    `${FATTI.giorniSupporto} giorni di supporto`,
    `Garanzia ${FATTI.giorniGaranzia} giorni`,
    "Zero canoni, mai",
  ];
  return (
    <div className="vivo">
      <section id="tessera" className="sv sv-carta sv-section tessera" aria-labelledby="tessera-h2">
        <div className="sv-container tess-grid">
          <div>
            <span className="sv-eyebrow">Cosa c&apos;è scritto sulla tua tessera</span>
            <h2 id="tessera-h2" className="sv-h2 mt-3 max-w-[14ch]">
              Un sistema, <span className="sv-it" style={{ color: "var(--sv-orange)" }}>una volta.</span>
            </h2>
            <p className="sv-lead sv-muted mt-5 max-w-[52ch]">
              Outreach Factory <b data-prezzo="outreach">{eur(LISTINO.outreach)}</b> · Content Factory{" "}
              <b data-prezzo="content">{eur(LISTINO.content)}</b> · Second Brain <b data-prezzo="brain">{eur(LISTINO.brain)}</b>. Metà alla
              firma, metà al go-live.
            </p>
            <Link href={prenotaDa("A17")} data-cta className="sv-btn mt-8">
              Prenota la chiamata →
            </Link>
          </div>

          <div className="tess-scena" aria-label="La tessera del sistema">
            <span className="tess-laccio" aria-hidden="true" />
            <div className="tess-card c-grana">
              <div className="tess-testa sv-mono">
                <span>
                  Digital Empire · <b>Sistema</b>
                </span>
                <span>№ 0001</span>
              </div>
              <p className="tess-nome">Sistema Empire</p>
              <ul className="tess-lista">
                {voci.map((v) => (
                  <li key={v} className="sv-check">
                    {v}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
