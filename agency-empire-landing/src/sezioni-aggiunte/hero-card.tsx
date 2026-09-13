/* F4 BLOCCO A5 (dossier 40) — le 5 card fluttuanti dell'hero (3 sx, 2 dx). Riempito dallo scagnozzo alfa.
   Stile ispirato all'allegato 02 (card scura arrotondata, illustrazione monocroma in alto, titolo bianco + riga argento)
   ma contenuto e illustrazioni completamente nostri: 5 SVG inline monocromi argento/ink con grana e un tocco
   d'arancio ciascuno. Assolute dentro <section>, pointer-events:none, z-index sotto il testo ma sopra la texture
   (l'ordine nel DOM di hero.tsx — subito dopo <HeroTexture /> — basta: vedi f4-hero.css per la nota di stacking).
   TUTTA la geometria (posizione, rotazione, breakpoint 1920/1440/1280) vive in f4-hero.css: qui solo struttura + contenuto. */

import type { ReactNode } from "react";

type CardDef = {
  id: string;
  icon: ReactNode;
  title: string;
  sub: string;
};

/* Terminale con cursore — "300 messaggi al giorno" */
function IconTerminale() {
  return (
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <rect x="4" y="8" width="40" height="30" rx="3" stroke="#c9c4d1" strokeWidth="1.6" />
      <path d="M10 18l6 5-6 5" stroke="#c9c4d1" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
      <path d="M22 28h10" stroke="#c9c4d1" strokeWidth="1.6" strokeLinecap="round" />
      <rect x="34" y="26.4" width="3.2" height="4" fill="#fb4604" />
      <path d="M4 13h40" stroke="#c9c4d1" strokeWidth="1.2" opacity=".5" />
    </svg>
  );
}

/* Calendario con "7" — "Setup in 7 giorni" */
function IconCalendario() {
  return (
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <rect x="6" y="9" width="36" height="32" rx="3" stroke="#c9c4d1" strokeWidth="1.6" />
      <path d="M6 18h36" stroke="#c9c4d1" strokeWidth="1.6" />
      <path d="M14 5v8M34 5v8" stroke="#c9c4d1" strokeWidth="1.6" strokeLinecap="round" />
      <text x="24" y="33" textAnchor="middle" fontSize="15" fontWeight="800" fill="#fb4604" fontFamily="inherit">7</text>
    </svg>
  );
}

/* Lucchetto aperto — "0 € di canone" */
function IconLucchetto() {
  return (
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <rect x="11" y="21" width="26" height="19" rx="3" stroke="#c9c4d1" strokeWidth="1.6" />
      <path d="M16 21v-5a8 8 0 0 1 14.5-4.6" stroke="#c9c4d1" strokeWidth="1.6" strokeLinecap="round" />
      <circle cx="24" cy="29" r="2.6" fill="#fb4604" />
      <path d="M24 31.6v4" stroke="#fb4604" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
  );
}

/* Server rack — "Gira sui tuoi server" */
function IconServer() {
  return (
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <rect x="8" y="7" width="32" height="11" rx="2" stroke="#c9c4d1" strokeWidth="1.6" />
      <rect x="8" y="20.5" width="32" height="11" rx="2" stroke="#c9c4d1" strokeWidth="1.6" />
      <rect x="8" y="34" width="32" height="7" rx="2" stroke="#c9c4d1" strokeWidth="1.6" />
      <circle cx="14" cy="12.5" r="1.6" fill="#fb4604" />
      <circle cx="14" cy="26" r="1.6" fill="#6f6a7a" />
      <path d="M20 12.5h14M20 26h14" stroke="#6f6a7a" strokeWidth="1.2" />
    </svg>
  );
}

/* Busta con lampeggio — "Primo lead qualificato" */
function IconBusta() {
  return (
    <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
      <rect x="6" y="12" width="36" height="25" rx="3" stroke="#c9c4d1" strokeWidth="1.6" />
      <path d="M7 14l17 13 17-13" stroke="#c9c4d1" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
      <circle cx="37" cy="12" r="5" fill="#0a0a0a" stroke="#fb4604" strokeWidth="1.6" />
      <circle cx="37" cy="12" r="1.6" fill="#fb4604" />
    </svg>
  );
}

const CARDS: CardDef[] = [
  { id: "l1", icon: <IconTerminale />, title: "300 messaggi al giorno", sub: "partono da soli, ogni mattina" },
  { id: "l2", icon: <IconCalendario />, title: "Setup in 7 giorni", sub: "dal contratto al go-live" },
  { id: "l3", icon: <IconLucchetto />, title: "0 € di canone", sub: "il codice è tuo" },
  { id: "r1", icon: <IconServer />, title: "Gira sui tuoi server", sub: "nessuna dipendenza da noi" },
  { id: "r2", icon: <IconBusta />, title: "Primo lead qualificato", sub: "entro la prima settimana" },
];

export function HeroCards() {
  return (
    <div className="f4-cards" aria-hidden="true">
      {CARDS.map((c) => (
        <div key={c.id} className={`f4-card f4-card--${c.id}`}>
          <span className="f4-card-ico">{c.icon}</span>
          <b className="f4-card-t">{c.title}</b>
          <span className="f4-card-s">{c.sub}</span>
        </div>
      ))}
    </div>
  );
}
