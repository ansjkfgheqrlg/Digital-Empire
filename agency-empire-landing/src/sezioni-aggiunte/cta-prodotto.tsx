import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";
import { LISTINO, eur, type Sistema } from "@/lib/listino";

/* AGGIUNTA F5 (ordine di Max 14/09 notte) — «CTA prodotto»: una pagina CTA intera per ogni sistema
   (Outreach Factory / Content Factory / Second Brain), sul modello di brief/F5-allegati/08.jpg
   (funneloperator.it): fondo ink + grana-fuoco a bassissima opacità, eyebrow, titolo enorme a due
   parole (seconda in arancio), tessera appesa (disegno riusato da A17, aggiunte-c.css), prezzo grande,
   niente countdown (nessuna scadenza vera: al suo posto lo slot su chiamata), due bottoni.
   Prezzi da LISTINO (eur + data-prezzo), giorni/numeri da FATTI: nessun numero scritto a mano.
   Ancore dei bottoni ghost: solo id ESISTENTI nel resto del sito (content → #content-output, già montato
   da ContentOutputV2); outreach e brain non hanno un id di dettaglio proprio → fallback #prezzi (ordine
   esplicito di Max). Montata 3 volte in page.tsx (non toccato da questo scagnozzo). */

type Prodotto = "outreach" | "content" | "brain";

type Config = {
  id: string;
  eyebrow: string;
  parola1: string;
  parola2: string;
  sistema: Sistema;
  tesseraNome: string;
  confrontoSaas: boolean;
  ghostHref: string;
  prenotaSezione: string;
  voci: string[];
};

const CONFIG: Record<Prodotto, Config> = {
  outreach: {
    id: "cta-outreach",
    eyebrow: "Installa il tuo",
    parola1: "OUTREACH",
    parola2: "FACTORY",
    sistema: "outreach",
    tesseraNome: "Outreach Factory",
    confrontoSaas: true,
    ghostHref: "#cartella",
    prenotaSezione: "cta-outreach",
    voci: [
      `Setup in ${FATTI.giorniSetup} giorni`,
      `${FATTI.messaggiGiorno} messaggi al giorno`,
      "Codice tuo, per sempre",
      `${FATTI.giorniSupporto} giorni di supporto`,
    ],
  },
  content: {
    id: "cta-content",
    eyebrow: "Accendi la tua",
    parola1: "CONTENT",
    parola2: "FACTORY",
    sistema: "content",
    tesseraNome: "Content Factory",
    confrontoSaas: false,
    ghostHref: "#content-output",
    prenotaSezione: "cta-content",
    voci: [
      `Setup in ${FATTI.giorniSetup} giorni`,
      "Caroselli, script e caption su Drive",
      "Codice tuo, per sempre",
      `${FATTI.giorniSupporto} giorni di supporto`,
    ],
  },
  brain: {
    id: "cta-brain",
    eyebrow: "Dai memoria alla tua",
    parola1: "SECOND",
    parola2: "BRAIN",
    sistema: "brain",
    tesseraNome: "Second Brain",
    confrontoSaas: false,
    ghostHref: "#tessera",
    prenotaSezione: "cta-brain",
    voci: [
      `Setup in ${FATTI.giorniSetup} giorni`,
      "Wiki indicizzata, query in secondi",
      "Codice tuo, per sempre",
      `${FATTI.giorniSupporto} giorni di supporto`,
    ],
  },
};

export function CtaProdotto({ prodotto }: { prodotto: Prodotto }) {
  const c = CONFIG[prodotto];
  const prezzo = eur(LISTINO[c.sistema]);

  return (
    <div className="vivo">
      <section
        id={c.id}
        className="sv sv-ink cp-sezione"
        aria-labelledby={`${c.id}-h2`}
      >
        <div className="cp-sfondo" aria-hidden="true" />
        <div className="cp-wrap">
          <span className="sv-eyebrow cp-eyebrow">{c.eyebrow}</span>

          <h2 id={`${c.id}-h2`} className="cp-titolo">
            {c.parola1} <span className="cp-accento">{c.parola2}</span>
          </h2>

          <div className="cp-scena" aria-label={`La tessera ${c.tesseraNome}`}>
            <span className="cp-laccio" aria-hidden="true" />
            <div className="cp-card c-grana">
              <div className="cp-card-testa sv-mono">
                <span>Digital Empire</span>
                <b>{c.tesseraNome}</b>
              </div>
              <ul className="cp-card-lista">
                {c.voci.map((v) => (
                  <li key={v}>{v}</li>
                ))}
              </ul>
              <div className="cp-card-piede sv-mono">Digital Empire</div>
            </div>
          </div>

          <p className="cp-prezzo-riga" data-prezzo={c.sistema}>
            {prezzo}
          </p>
          <p className="cp-prezzo-nota">
            Pagamento unico. Codice tuo, zero canoni. Metà alla firma, metà al go-live.
          </p>
          {c.confrontoSaas && (
            <p className="cp-prezzo-confronto">
              Un SaaS equivalente: <span data-prezzo="saasMese">{eur(LISTINO.saasMese)}</span> al mese, per sempre.
            </p>
          )}

          <p className="cp-slot sv-mono">Prossimo slot di installazione: su chiamata</p>

          <div className="cp-bottoni">
            <Link href={prenotaDa(c.prenotaSezione)} data-cta className="sv-btn">
              Prenota la chiamata di {FATTI.minutiChiamata} minuti →
            </Link>
            <Link href={c.ghostHref} className="sv-btn-ghost">
              Cosa contiene, nel dettaglio ↓
            </Link>
          </div>

          <p className="cp-garanzie sv-mono">
            Setup in {FATTI.giorniSetup} giorni · garanzia {FATTI.giorniGaranzia} giorni · {FATTI.giorniSupporto} giorni di supporto
          </p>
        </div>
      </section>
    </div>
  );
}
