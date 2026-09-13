import type { ReactNode } from "react";
import { FATTI } from "@/lib/fatti";
import { LISTINO } from "@/lib/listino";

/* AGGIUNTA D2 (ordine di Max, 13/09) — rifatta il 13/09 sera (BRIEF F3, blocco C; 39B §5).
   Da «quattro scatole con frecce» a «una riga con quattro momenti»: un filetto hairline con 4 punti, sopra ogni punto la
   tappa in mono 11, sotto il titolo a 17 bold e UNA riga a 14. Niente card, niente sfondo, niente bordo. Solo l'ultima tappa
   porta l'accento (il punto e la cifra). Allineato a sinistra in una colonna ≤ 900. Altezza ≈ 170 px.
   Le frecce restano perché Max le vuole (lunghe, sottili, punta piccola, una che passa sotto) ma FERME (nessuna animazione)
   e più rade: collegano i 4 punti del filetto — la 1ª e la 3ª ad arco sopra, la 2ª passa sotto il filetto.
   Numeri da FATTI e LISTINO (§6/§8: nessun numero scritto a mano). Su mobile le tappe vanno in colonna con il filetto
   verticale e niente SVG. CSS: aggiunte-hero.css (.funnel-hero, .fh-*). */

const percentAcconto = Math.round(LISTINO.acconto * 100);
const ore = FATTI.orePerDm.toLocaleString("it-IT");

type Tappa = { k: string; tappa: string; titolo: string; riga: ReactNode; fine?: boolean };

const TAPPE: Tappa[] = [
  { k: "oggi", tappa: "Oggi", titolo: "Tutto a mano", riga: `${ore} ore tue al giorno` },
  { k: "chiamata", tappa: `Chiamata · ${FATTI.minutiChiamata}′`, titolo: "Vedi il sistema che gira", riga: "gratis, nessun impegno" },
  {
    k: "setup",
    tappa: `Setup · ${FATTI.giorniSetup} giorni`,
    titolo: "Sul tuo server",
    riga: `${percentAcconto} % alla firma, ${100 - percentAcconto} % al go-live`,
  },
  {
    k: "gira",
    tappa: "Da qui in poi",
    titolo: "Il tuo workflow gira",
    riga: (
      <>
        <b className="fh-cifra">{FATTI.messaggiGiorno}</b> messaggi al giorno, 0 ore tue
      </>
    ),
    fine: true,
  },
];

/* Le frecce vivono in un SVG steso sopra la riga delle tappe: viewBox 900×100 con preserveAspectRatio="none",
   alto esattamente 100 px → le y sono pixel veri (il filetto sta a y = 48, vedi --fh-linea nel CSS), le x sono
   quarti della colonna (passo 225). I punti stanno all'inizio di ogni colonna (centro a x = 4.5).
   Arco SOPRA: parte dal punto, sale al massimo di ~23 px sopra il filetto (resta sotto la tappa in mono) e atterra
   sul punto successivo. Arco SOTTO: scende di ~14 px sotto il filetto (resta sopra il titolo) e risale nel punto. */
const PASSO = 900 / 4;
const px = (i: number) => i * PASSO + 4.5;
const LINEA = 48;

function Arco({ i, sotto = false }: { i: number; sotto?: boolean }) {
  const x0 = px(i) + 8, x1 = px(i + 1) - 8;
  const d = sotto
    ? `M${x0},${LINEA + 4} C${x0 + 70},${LINEA + 23} ${x1 - 70},${LINEA + 23} ${x1},${LINEA + 4}`
    : `M${x0},${LINEA - 3} C${x0 + 70},${LINEA - 31} ${x1 - 70},${LINEA - 31} ${x1},${LINEA - 3}`;
  return (
    <>
      <path className="fh-fr-ghost" d={d} />
      <path className="fh-fr" d={d} />
    </>
  );
}

export function FunnelHero() {
  return (
    <div className="funnel-hero">
      <ol className="fh-tappe" role="list" aria-label="Da dove sei a dove arrivi, in quattro tappe">
        {TAPPE.map((t) => (
          <li key={t.k} className={`fh-tappa${t.fine ? " fh-tappa--fine" : ""}`}>
            <span className="fh-e">{t.tappa}</span>
            <span className="fh-punto" aria-hidden="true" />
            <b className="fh-t">{t.titolo}</b>
            <span className="fh-r">{t.riga}</span>
          </li>
        ))}
      </ol>
      <svg className="fh-frecce" viewBox="0 0 900 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <defs>
          <marker id="fh-punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
          </marker>
        </defs>
        <Arco i={0} />
        <Arco i={1} sotto />
        <Arco i={2} />
      </svg>
    </div>
  );
}
