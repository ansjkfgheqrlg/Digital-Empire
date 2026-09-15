"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
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
   esplicito di Max). Montata 3 volte in page.tsx (non toccato da questo scagnozzo).

   F6 H2/L1 (dossier 41, ordini di Max 15/09, scagnozzo δ) — via il vecchio laccio/moschettone: la
   tessera ora pende da due catenelle d'argento agganciate all'ultima lettera tonda della seconda parola
   del titolo (FACTORY → «O», BRAIN → «A»). "use client" perché il punto di aggancio si misura a runtime
   con getBoundingClientRect (il titolo è responsive/clamp: niente offset fissi). Colori in f6-colori.css. */

type Prodotto = "outreach" | "content" | "brain";

/** L'ultima lettera "tonda" della seconda parola del titolo, dove si aggancia la catena. */
function trovaAggancio(parola: string): { pre: string; lettera: string; post: string } {
  const target = parola === "BRAIN" ? "A" : "O";
  const idx = parola.lastIndexOf(target);
  if (idx === -1) return { pre: parola, lettera: "", post: "" };
  return { pre: parola.slice(0, idx), lettera: parola[idx], post: parola.slice(idx + 1) };
}

type Anello = { cx: number; cy: number; rx: number; ry: number; angle: number };

/** Genera gli anelli di una catenella lungo il segmento (x1,y1)-(x2,y2): ovali 8x5 alternati
    orizzontale/verticale, leggero wobble per sembrare vera (non un tubo dritto). */
function generaAnelli(x1: number, y1: number, x2: number, y2: number): Anello[] {
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy) || 1;
  const passo = 9; // px per anello, circa
  const n = Math.max(14, Math.min(18, Math.round(len / passo)));
  const angleBase = (Math.atan2(dy, dx) * 180) / Math.PI;
  const px = -dy / len;
  const py = dx / len;
  const anelli: Anello[] = [];
  for (let i = 0; i < n; i++) {
    const t = (i + 0.5) / n;
    const verticale = i % 2 === 0;
    const wob = Math.sin(i * 1.3) * 1.2;
    anelli.push({
      cx: x1 + dx * t + px * wob,
      cy: y1 + dy * t + py * wob,
      rx: verticale ? 5 : 8,
      ry: verticale ? 8 : 5,
      angle: angleBase + (verticale ? 90 : 0),
    });
  }
  return anelli;
}

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

type Catena = { id: string; anelli: Anello[] };

export function CtaProdotto({ prodotto }: { prodotto: Prodotto }) {
  const c = CONFIG[prodotto];
  const prezzo = eur(LISTINO[c.sistema]);
  const agg = trovaAggancio(c.parola2);

  const wrapRef = useRef<HTMLDivElement>(null);
  const hookRef = useRef<HTMLSpanElement>(null);
  const cardRef = useRef<HTMLDivElement>(null);
  const foroSxRef = useRef<HTMLSpanElement>(null);
  const foroDxRef = useRef<HTMLSpanElement>(null);
  const foroMidRef = useRef<HTMLSpanElement>(null);
  const [catene, setCatene] = useState<Catena[]>([]);

  useEffect(() => {
    function misura() {
      const wrap = wrapRef.current;
      const hook = hookRef.current;
      const card = cardRef.current;
      if (!wrap || !hook || !card) return;
      const wrapRect = wrap.getBoundingClientRect();
      const hookRect = hook.getBoundingClientRect();
      const hookX = hookRect.left + hookRect.width / 2 - wrapRect.left;
      const hookY = hookRect.bottom - wrapRect.top; // punto basso del glifo (Range.getBoundingClientRect)

      const mobile = window.matchMedia("(max-width: 640px)").matches;
      if (mobile) {
        const mid = foroMidRef.current;
        if (!mid) return;
        const midRect = mid.getBoundingClientRect();
        const foroX = midRect.left + midRect.width / 2 - wrapRect.left;
        const foroY = midRect.top + midRect.height / 2 - wrapRect.top;
        setCatene([{ id: "mid", anelli: generaAnelli(hookX, hookY, foroX, foroY) }]);
      } else {
        const sx = foroSxRef.current;
        const dx = foroDxRef.current;
        if (!sx || !dx) return;
        const sxRect = sx.getBoundingClientRect();
        const dxRect = dx.getBoundingClientRect();
        const sxX = sxRect.left + sxRect.width / 2 - wrapRect.left;
        const sxY = sxRect.top + sxRect.height / 2 - wrapRect.top;
        const dxX = dxRect.left + dxRect.width / 2 - wrapRect.left;
        const dxY = dxRect.top + dxRect.height / 2 - wrapRect.top;
        setCatene([
          { id: "sx", anelli: generaAnelli(hookX - 3, hookY, sxX, sxY) },
          { id: "dx", anelli: generaAnelli(hookX + 3, hookY, dxX, dxY) },
        ]);
      }
    }
    misura();
    document.fonts?.ready?.then(misura).catch(() => {});
    window.addEventListener("resize", misura);
    return () => window.removeEventListener("resize", misura);
  }, [prodotto]);

  return (
    <div className="vivo">
      <section
        id={c.id}
        className="sv sv-ink cp-sezione"
        aria-labelledby={`${c.id}-h2`}
      >
        <div className="cp-sfondo" aria-hidden="true" />
        <div className="cp-wrap" ref={wrapRef}>
          <span className="sv-eyebrow cp-eyebrow">{c.eyebrow}</span>

          <h2 id={`${c.id}-h2`} className="cp-titolo">
            {c.parola1}{" "}
            <span className="cp-accento">
              {agg.pre}
              <span className="cp-aggancio" ref={hookRef}>{agg.lettera}</span>
              {agg.post}
            </span>
          </h2>

          {catene.length > 0 && (
            <svg className="cp-catene" aria-hidden="true">
              <defs>
                <linearGradient id={`cp-argento-${c.id}`} x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stopColor="#f4f4f6" />
                  <stop offset="35%" stopColor="#cfcfd6" />
                  <stop offset="65%" stopColor="#8a8a92" />
                  <stop offset="100%" stopColor="#4a4a50" />
                </linearGradient>
              </defs>
              {catene.map((cat) => (
                <g key={cat.id} style={{ filter: "drop-shadow(0 1px 1px rgba(0,0,0,.8))" }}>
                  {cat.anelli.map((a, i) => (
                    <ellipse
                      key={i}
                      cx={a.cx}
                      cy={a.cy}
                      rx={a.rx}
                      ry={a.ry}
                      transform={`rotate(${a.angle} ${a.cx} ${a.cy})`}
                      fill="none"
                      stroke={`url(#cp-argento-${c.id})`}
                      strokeWidth={1.4}
                    />
                  ))}
                  {cat.anelli.map((a, i) => (
                    <ellipse
                      key={`hl-${i}`}
                      cx={a.cx - a.rx * 0.15}
                      cy={a.cy - a.ry * 0.15}
                      rx={a.rx * 0.55}
                      ry={a.ry * 0.55}
                      transform={`rotate(${a.angle} ${a.cx} ${a.cy})`}
                      fill="none"
                      stroke="rgba(255,255,255,.55)"
                      strokeWidth={0.6}
                    />
                  ))}
                </g>
              ))}
            </svg>
          )}

          <div className="cp-scena" aria-label={`La tessera ${c.tesseraNome}`}>
            <div className="cp-card c-grana" ref={cardRef}>
              <span className="cp-fondo" aria-hidden="true" />
              <span className="cp-foro cp-foro-sx" ref={foroSxRef} aria-hidden="true" />
              <span className="cp-foro cp-foro-dx" ref={foroDxRef} aria-hidden="true" />
              <span className="cp-foro cp-foro-mid" ref={foroMidRef} aria-hidden="true" />
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
