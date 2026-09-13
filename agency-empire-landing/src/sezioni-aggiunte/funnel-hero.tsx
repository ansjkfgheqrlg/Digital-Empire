import { FATTI } from "@/lib/fatti";
import { LISTINO } from "@/lib/listino";

/* AGGIUNTA D2 (ordine di Max, 13/09) — lo schema a blocchi dentro l'hero, sotto il sottotitolo e la CTA:
   dall'operatività a mano al workflow che gira. Quattro blocchi, tre frecce «a salto» in SVG: bezier,
   tratteggio a puntini che scorre verso la punta (ferme con prefers-reduced-motion), marker triangolare.
   Numeri da FATTI e LISTINO (§6/§8: nessun numero scritto a mano). Su mobile i blocchi vanno in colonna
   e le frecce diventano un tratteggio verticale in CSS. */

const percentAcconto = Math.round(LISTINO.acconto * 100);

const BLOCCHI: { k: string; occhiello: string; titolo: string; righe: string[]; piede: string; fine?: boolean }[] = [
  {
    k: "oggi",
    occhiello: "Oggi",
    titolo: "Tutto a mano",
    righe: [`${FATTI.dmAMano} DM al giorno, scritti da te`, "follow-up dimenticati", "contenuti «quando riesci»"],
    piede: `${FATTI.orePerDm.toLocaleString("it-IT")} ore tue al giorno`,
  },
  {
    k: "chiamata",
    occhiello: `Chiamata · ${FATTI.minutiChiamata}′`,
    titolo: "Vedi il sistema che gira",
    righe: ["invii di oggi, risposte in coda", "il tuo caso, i tuoi numeri", "nessuna slide"],
    piede: "gratis · nessun impegno",
  },
  {
    k: "setup",
    occhiello: `Setup · ${FATTI.giorniSetup} giorni`,
    titolo: "Sul tuo server",
    righe: ["coi tuoi account", "dashboard aperta dal primo giorno", "formazione al tuo team"],
    piede: `${percentAcconto} % alla firma · ${100 - percentAcconto} % al go-live`,
  },
  {
    k: "gira",
    occhiello: "Da qui in poi",
    titolo: "Il tuo workflow gira",
    righe: [`${FATTI.messaggiGiorno} messaggi al giorno`, `0 ore tue · ${FATTI.canoneMese} canoni`, "codice tuo, per sempre"],
    piede: "misurato, non promesso",
    fine: true,
  },
];

/* Le tre frecce: coordinate nel viewBox 1000×200 (preserveAspectRatio none). Ogni salto parte dal bordo alto del
   blocco i (x ≈ 0,196 + 0,26·i) e atterra sul bordo alto del blocco i+1. */
function Salto({ i }: { i: number }) {
  const x0 = 196 + i * 260;
  const d = `M${x0},-4 C${x0 + 30},-58 ${x0 + 66},-58 ${x0 + 88},-2`;
  return (
    <>
      <path className="fh-fr-ghost" d={d} />
      <path className="fh-fr" d={d} style={{ animationDelay: `${i * 0.8}s` }} />
    </>
  );
}

export function FunnelHero() {
  return (
    <div className="funnel-hero" role="list" aria-label="Da dove sei a dove arrivi, in quattro passi">
      {BLOCCHI.map((b) => (
        <div key={b.k} role="listitem" className={`fh-bl${b.fine ? " fh-bl-fine" : ""}`}>
          <span className="fh-e">{b.occhiello}</span>
          <b className="fh-t">{b.titolo}</b>
          <ul className="fh-ul">
            {b.righe.map((r) => (
              <li key={r}>{r}</li>
            ))}
          </ul>
          <span className="fh-f">{b.piede}</span>
        </div>
      ))}
      <svg className="fh-frecce" viewBox="0 0 1000 200" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <defs>
          <marker id="fh-punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="#fb4604" />
          </marker>
        </defs>
        <Salto i={0} />
        <Salto i={1} />
        <Salto i={2} />
      </svg>
    </div>
  );
}
