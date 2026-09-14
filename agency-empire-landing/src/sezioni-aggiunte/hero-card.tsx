/* F4 BLOCCO A5 (dossier 40) — le 5 card fluttuanti dell'hero (3 sx, 2 dx). Riscritte da beta (F5, ordine
   di Max 14/09 notte): stile e struttura dell'allegato 02 — card scura stretta, illustrazione monocroma
   granulosa (stampa/risograph) nei 2/3 superiori che sfuma nel fondo, titolo bianco 600 + spunta in
   cerchio arancione, riga argento sotto. Le 5 illustrazioni sono PNG originali generate con Python/PIL
   (scripts/illustrazioni_card.py), non icone scaricate: terminale, calendario, lucchetto, server, busta.
   Le classi .f4-card / .f4-card--l1..l3 / .f4-card--r1..r2 restano INTATTE: la loro posizione, rotazione
   e visibilita' per breakpoint vivono in f4-hero.css (e vengono ristrette in f5-hero.css dallo scagnozzo
   alfa, nello stesso momento). Qui solo struttura interna + contenuto — l'aspetto vive in f5-card.css. */

import type { ReactNode } from "react";

type CardDef = {
  id: string;
  img: string;
  title: string;
  sub: string;
};

/* Spunta in cerchio arancione — accanto a ogni titolo, come nell'allegato 02 */
function CheckBadge() {
  return (
    <svg className="f5-card-check" viewBox="0 0 14 14" fill="none" aria-hidden="true">
      <circle cx="7" cy="7" r="6.3" stroke="#fb4604" strokeWidth="1.3" />
      <path d="M4.2 7.2l1.9 1.9 3.7-4.2" stroke="#fb4604" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

const CARDS: CardDef[] = [
  { id: "l1", img: "/card/c1.png", title: "300 messaggi al giorno", sub: "partono da soli, ogni mattina" },
  { id: "l2", img: "/card/c2.png", title: "Setup in 7 giorni", sub: "dal contratto al go-live" },
  { id: "l3", img: "/card/c3.png", title: "0 € di canone", sub: "il codice è tuo" },
  { id: "r1", img: "/card/c4.png", title: "Gira sui tuoi server", sub: "nessuna dipendenza da noi" },
  { id: "r2", img: "/card/c5.png", title: "Primo lead qualificato", sub: "entro la prima settimana" },
];

function Card({ c }: { c: CardDef }): ReactNode {
  return (
    <div className={`f4-card f4-card--${c.id}`}>
      <div className="f5-card-img">
        <img src={c.img} alt="" width={400} height={320} loading="lazy" decoding="async" />
      </div>
      <div className="f5-card-body">
        <div className="f5-card-title">
          <CheckBadge />
          <b>{c.title}</b>
        </div>
        <span className="f5-card-sub">{c.sub}</span>
      </div>
    </div>
  );
}

export function HeroCards() {
  return (
    <div className="f4-cards" aria-hidden="true">
      {CARDS.map((c) => (
        <Card key={c.id} c={c} />
      ))}
    </div>
  );
}
