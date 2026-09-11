import { cn } from "@/lib/utils";
import presenti from "@/lib/aura-presenti.json";

/**
 * <Aura/> — una foto del manifest (public/aura/manifest.json) con la sua riga bianca.
 *
 * Composizione B (Dossier 37 v2, C3.1): il componente NON controlla il 404 a runtime. Legge
 * `src/lib/aura-presenti.json`, scritto da `scripts/aura_prep.py` a build time: se il file non è
 * fra i presenti il componente rende `null`, e il contenitore `.due-col` chiude la colonna
 * (`:has(> .foto)`). Niente cornice vuota, niente segnaposto, niente salto al mount, già nell'HTML statico.
 *
 * Regola C2.2 (v1): gli still originali non stanno mai in public/. In locale, per la misura "manifest
 * pieno", si servono da cantiere/aura-preview/ tramite NEXT_PUBLIC_AURA_BASE (es. http://localhost:8787/).
 *
 * Legge di Max: la riga si legge SEMPRE — banda scura + ombra tripla (classe .riga in vivo.css).
 */
const BASE = process.env.NEXT_PUBLIC_AURA_BASE ?? "/aura/";
const PRESENTI = new Set<string>(presenti.file);

export function auraPresente(file: string): boolean {
  return PRESENTI.has(file);
}

type AuraProps = {
  /** nome file nel manifest, es. "n1-hero.webp" */
  file: string;
  alt: string;
  riga?: string;
  rigaPos?: "bassa" | "media" | "sinistra";
  tratt?: "b" | "carta" | "acciaio" | "negativo" | "filigrana";
  className?: string;
  objectPosition?: string;
  priority?: boolean;
};

export function Aura({ file, alt, riga, rigaPos = "bassa", tratt = "b", className, objectPosition, priority }: AuraProps) {
  if (!auraPresente(file)) return null;

  return (
    <figure
      className={cn(
        "foto",
        tratt === "carta" && "foto--carta",
        tratt === "acciaio" && "foto--acciaio",
        tratt === "negativo" && "foto--negativo",
        tratt === "filigrana" && "foto--filigrana",
        className
      )}
    >
      {/* eslint-disable-next-line @next/next/no-img-element -- output: export, niente loader */}
      <img
        src={`${BASE}${file}`}
        alt={alt}
        loading={priority ? "eager" : "lazy"}
        decoding="async"
        fetchPriority={priority ? "high" : "auto"}
        style={objectPosition ? { objectPosition } : undefined}
      />
      {riga && (
        <figcaption
          className={cn("riga", rigaPos === "media" ? "riga--media" : "riga--bassa", rigaPos === "sinistra" && "riga--sinistra")}
        >
          {riga}
        </figcaption>
      )}
    </figure>
  );
}
