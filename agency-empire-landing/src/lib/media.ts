/**
 * MEDIA — i pezzi che accendono le sezioni aggiunte (Dossier 38 v2 §H/§I).
 * Ogni voce `null` = il posto rende `null` e il sito resta intero (ADR-028: niente blocca niente).
 * I file veri li mette Max in public/; qui si dichiara solo dove stanno.
 */
export const TEXTURE = {
  /** D1 — onde di linee puntinate arancioni (sfondo dell'hero). ≥ 2880 px di larghezza. */
  heroOnde: { src: "/texture/hero-onde.jpg", width: 2880, height: 1620 } as const,
  /** D3 — grana arancione con strisce scure diagonali (fascia-manifesto). */
  granaFuoco: { src: "/texture/grana-fuoco.jpg", width: 2400, height: 1000 } as const,
} as const;

export type Immagine = { src: string; width: number; height: number; alt: string } | null;

/** A01 / A14 / A19 — ritratti veri: finché sono `null` le sezioni che li usano non si renderizzano. */
export const RITRATTI: Record<"maxFirma" | "maxGaranzia" | "gael" | "leonardo", Immagine> = {
  maxFirma: null,
  maxGaranzia: null,
  gael: null,
  leonardo: null,
};
