/**
 * CONTATTI — la porta d'uscita del sito (Dossier 37 v2, C1.1).
 * Tutte le CTA vanno a PRENOTA (pagina nostra, brand agenzia) via <Link>; `?da=Nxx` dice da quale
 * sezione si arriva (analytics.tsx lo passa all'evento). Nessun dominio del corso, mai.
 */
export const PRENOTA = "/prenota/";
export const CALENDLY =
  "https://calendly.com/max-infoproducer/30min?hide_gdpr_banner=1&background_color=0a0a0a&text_color=f8f8f2&primary_color=fb4604";
/** email pubblica di contatto: gesto di Max (ADR-026). Vuota = le righe che la usano non si renderizzano. Mai inventarla. */
export const EMAIL = "";

/** href della CTA di una sezione: "/prenota/?da=N17" */
export function prenotaDa(sezione: string): string {
  return `${PRENOTA}?da=${sezione}`;
}
