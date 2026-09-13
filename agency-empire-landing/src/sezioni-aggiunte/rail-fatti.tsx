import { FATTI } from "@/lib/fatti";
import { eur } from "@/lib/listino";

/* AGGIUNTA A02 (Dossier 38 v2, Atto I) — il rail dei quattro fatti, subito sotto l'hero (dopo la Firma quando c'è).
   Superficie carta; nastro CSS lento, doppio elenco per il loop, fermo con prefers-reduced-motion e al passaggio del mouse.
   Ogni numero viene da FATTI/LISTINO (§6/§8) — cambiare un fatto = cambiarlo in un posto. FO-E01. */
const FATTI_RAIL: [string, string][] = [
  [`${FATTI.giorniSetup} giorni`, "dal contratto al go-live"],
  [`${FATTI.messaggiGiorno}`, "messaggi al giorno, zero a mano"],
  [eur(FATTI.canoneMese), "di canone, per sempre"],
  [`${FATTI.giorniSupporto} giorni`, "di supporto inclusi"],
];

export function RailFatti() {
  const lista = [...FATTI_RAIL, ...FATTI_RAIL];
  return (
    <div className="vivo">
      <section className="sv sv-carta rail-fatti" aria-label="Quattro fatti, con fonte">
        <div className="rf-track">
          <ul className="rf-rail" aria-hidden="false">
            {lista.map(([n, d], i) => (
              <li key={`${n}-${i}`} className="rf-fatto" aria-hidden={i >= FATTI_RAIL.length ? true : undefined}>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" aria-hidden="true">
                  <circle cx="12" cy="12" r="9" />
                </svg>
                <b>{n}</b>
                <span>{d}</span>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}
