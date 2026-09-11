// Compatibilità con le sezioni v1 (in sections/_v1 fino alla rimozione dopo F7).
// Le fonti vere sono listino.ts / contatti.ts / fatti.ts (Dossier 37 v2).
import { LISTINO, eur } from "./listino";
export { PRENOTA as BOOKING_URL } from "./contatti";
export const PRICE = eur(LISTINO.brain);
export const DISCOUNTED_PRICE = eur(LISTINO.engine);
export const SITE_TITLE = "Digital Empire | Sistemi AI installati sui tuoi server";
export const SITE_DESCRIPTION =
  "Outreach Factory, Content Factory e Second Brain: tre sistemi AI installati sul tuo server in 7 giorni. Zero canoni, codice tuo. Prenota 30 minuti: il sistema in live, niente slide.";
