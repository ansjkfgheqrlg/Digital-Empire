/**
 * LISTINO — l'unico posto del sito in cui vive un prezzo (Dossier 37 v2, C1.4).
 * Fonte: cantieri/agency-empire-landing-vivo/FATTI.md. Ogni prezzo in pagina è `eur(LISTINO.x)`
 * con `data-prezzo="x"`; il gate `grep -rnE "€ ?[0-9]{1,2}\.[0-9]{3}" src/components src/app` deve dare 0.
 */
export const LISTINO = {
  outreach: 4000,
  content: 3500,
  brain: 2500,
  engine: 8000,
  engineListino: 10000,
  acconto: 0.5,
  /** SaaS di outreach a confronto (pricing-roi del sito v1): 200 €/mese */
  saasMese: 200,
} as const;

export type Sistema = "outreach" | "content" | "brain" | "engine";

/** "4.000 €" — formato italiano, senza decimali */
export function eur(n: number): string {
  return `${n.toLocaleString("it-IT", { maximumFractionDigits: 0 })} €`;
}

export const RISPARMIO_ENGINE = LISTINO.engineListino - LISTINO.engine;
export const SAAS_ANNO = LISTINO.saasMese * 12;
export const MESI_PAREGGIO = Math.round(LISTINO.outreach / LISTINO.saasMese);
