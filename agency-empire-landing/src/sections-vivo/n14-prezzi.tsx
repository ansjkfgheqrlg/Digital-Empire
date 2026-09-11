import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";
import { LISTINO, eur } from "@/lib/listino";

/* N14 — I tre sistemi e il prezzo (4 sezioni v1 → 1). Tre card ink con etichetta mono + numero romano,
   Engine Room evidenziata da un bordo arancione, non da un colore diverso. Ogni prezzo da listino.ts con data-prezzo.
   Copy: COPY.md §N14. */
const CARD = [
  { n: "I", nome: "Outreach Factory", chiave: "outreach" as const, claim: "Il tuo sales team che non dorme mai.", testo: `${FATTI.messaggiGiorno} messaggi al giorno, qualificazione AI, follow-up, dashboard, lead nel CRM.` },
  { n: "II", nome: "Content Factory", chiave: "content" as const, claim: "Pubblica ogni giorno senza toccare niente.", testo: "Caroselli APSOC, script reel, caption e hashtag, su Drive." },
  { n: "III", nome: "Second Brain", chiave: "brain" as const, claim: "La tua azienda sa tutto, sempre.", testo: "Documenti, processi, clienti, decisioni: indicizzati, con risposta." },
];

const INCLUSO = [
  "Codice sorgente sul tuo server",
  "dashboard web",
  "proxy residenziali configurati",
  "copy engine APSOC calibrato sul tuo brand",
  "lead su Slack o nel tuo CRM",
  "manuale tecnico",
  `${FATTI.giorniSupporto} giorni di supporto`,
  "1 sessione di formazione al team",
];

export function Prezzi() {
  return (
    <section id="prezzi" className="sv sv-ink sv-section" aria-labelledby="prezzi-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">Prezzi · nessuna sorpresa</p>
        <h2 id="prezzi-h2" className="sv-h2 mt-3 max-w-[14ch]">
          Un sistema. Un prezzo. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Una volta.</span>
        </h2>

        <ul className="mt-10 grid md:grid-cols-3 gap-4">
          {CARD.map((c) => (
            <li key={c.n} className="sv-card flex flex-col gap-3">
              <p className="sv-etichetta"><b>{c.n}</b> · {c.nome}</p>
              <p className="sv-stat" data-prezzo={c.chiave}>{eur(LISTINO[c.chiave])}</p>
              <p className="sv-body text-white">{c.claim}</p>
              <p className="sv-small sv-muted">{c.testo}</p>
            </li>
          ))}
        </ul>

        <div className="sv-card sv-card--engine mt-4 md:flex md:items-center md:justify-between md:gap-10">
          <div>
            <p className="sv-etichetta"><b>Engine Room</b> · tutti e tre</p>
            <p className="sv-body sv-muted mt-2 max-w-[60ch]">
              I lead dell&apos;outreach, i contenuti e la memoria dell&apos;azienda lavorano insieme, in una dashboard sola.
            </p>
          </div>
          <p className="mt-4 md:mt-0 whitespace-nowrap">
            <span className="sv-stat" data-prezzo="engine">{eur(LISTINO.engine)}</span>{" "}
            <span className="sv-small sv-muted">invece di <s data-prezzo="engineListino">{eur(LISTINO.engineListino)}</s></span>
          </p>
        </div>

        <div className="mt-12 grid md:grid-cols-[1fr_1fr] gap-10">
          <div>
            <h3 className="sv-h3">In ogni sistema, sempre</h3>
            <ul className="mt-4 grid sm:grid-cols-2 gap-x-6 gap-y-2">
              {INCLUSO.map((v) => (
                <li key={v} className="sv-check sv-body sv-muted">{v}</li>
              ))}
            </ul>
          </div>
          <div>
            <p className="sv-body sv-muted">
              {Math.round(LISTINO.acconto * 100)}% all&apos;ordine, {Math.round((1 - LISTINO.acconto) * 100)}% alla consegna. Rateizzazione
              disponibile. <b className="text-white">Canone mensile? No.</b> Non ne abbiamo mai messo uno. Fai tu il conto: 12 × quello
              che paghi oggi al tool che non sa chi sei.
            </p>
            <div className="mt-6">
              <CallCTA da="N14" />
            </div>
            <p className="sv-small sv-muted mt-3">Il prezzo esatto per il tuo caso lo diciamo in chiamata, non «a partire da».</p>
          </div>
        </div>
      </div>
    </section>
  );
}
