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

/* Le tre frecce, nel viewBox 1000×200 (preserveAspectRatio none; larghezza dei blocchi ≈ 205, gap ≈ 60).
   Sono lunghe: partono dal centro-alto di un blocco e atterrano sul centro-alto del successivo, arco alto e morbido.
   La 1ª e la 3ª passano SOPRA (svg davanti ai blocchi); la 2ª passa SOTTO: il suo tracciato scende dietro il blocco
   «Chiamata» e riemerge nel varco — si vede solo dove non c'è il blocco, come un filo che passa sotto. */
const BLOCCO_W = (1000 - 3 * 60) / 4; // ≈ 205
const cx = (i: number) => i * (BLOCCO_W + 60) + BLOCCO_W / 2;

function Sopra({ i, delay }: { i: number; delay: number }) {
  const x0 = cx(i) + 40, x1 = cx(i + 1) - 40;
  const d = `M${x0},-6 C${x0 + 60},-92 ${x1 - 60},-92 ${x1},-4`;
  return (
    <>
      <path className="fh-fr-ghost" d={d} />
      <path className="fh-fr" d={d} style={{ animationDelay: `${delay}s` }} />
    </>
  );
}
function Sotto({ i, delay }: { i: number; delay: number }) {
  const x0 = cx(i) + 30, x1 = cx(i + 1) - BLOCCO_W / 2 + 8;
  // scende dietro il blocco i, attraversa il varco a mezza altezza, risale lungo il fianco del blocco i+1 e atterra sul suo spigolo alto
  const d = `M${x0},40 C${x0 + 40},130 ${x1 - 70},170 ${x1 - 26},110 S${x1 - 4},20 ${x1},-4`;
  return (
    <>
      <path className="fh-fr-ghost" d={d} />
      <path className="fh-fr" d={d} style={{ animationDelay: `${delay}s` }} />
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
      <svg className="fh-frecce fh-frecce--sotto" viewBox="0 0 1000 200" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <defs>
          <marker id="fh-punta-sotto" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="#fb4604" />
          </marker>
        </defs>
        <Sotto i={1} delay={1.1} />
      </svg>
      <svg className="fh-frecce" viewBox="0 0 1000 200" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <defs>
          <marker id="fh-punta" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="#fb4604" />
          </marker>
        </defs>
        <Sopra i={0} delay={0} />
        <Sopra i={2} delay={2.2} />
      </svg>
    </div>
  );
}
