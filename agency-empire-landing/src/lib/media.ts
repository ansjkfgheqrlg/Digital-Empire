/**
 * MEDIA — i pezzi che accendono le sezioni aggiunte (Dossier 38 v2 §H/§I).
 * Ogni voce `null` = il posto rende `null` e il sito resta intero (ADR-028: niente blocca niente).
 * I file veri li mette Max in public/; qui si dichiara solo dove stanno.
 */
export const TEXTURE = {
  /** D1 — onde di linee puntinate arancioni (sfondo dell'hero). È L'IMMAGINE DI MAX (13/09 sera, incollata in chat,
   *  estratta dal transcript e salvata in public/texture/hero-onde-ORIGINALE.jpg, 899×1748). hero-onde.jpg/.webp (3840×2000) =
   *  la tessera INTERA a tutta altezza, MAI ingrandita (sul desktop 1x è rimpicciolita ≈0,57), ripetuta 4× in orizzontale
   *  (alternate specchiate) con giunti sfumati a nero — ordine di Max 13/09 sera: «doppioni fino a coprire, sfumatura scura sui tagli».
   *  Generatore: scripts/texture_hero_tile.py. Nessuna approssimazione. */
  heroOnde: { src: "/texture/hero-onde.jpg", webp: "/texture/hero-onde.webp", width: 3840, height: 2000 } as const,
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
