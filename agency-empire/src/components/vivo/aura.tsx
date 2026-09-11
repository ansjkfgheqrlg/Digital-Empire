"use client";

import { useEffect, useRef, useState } from "react";
import { cn } from "@/lib/utils";

/**
 * <Aura/> — una foto del manifest (public/aura/manifest.json) con la sua riga bianca.
 *
 * Regola C2.2 (Dossier 37): gli still originali non stanno mai in public/. In sviluppo si servono
 * da cantiere/aura-preview/ tramite un server statico locale (NEXT_PUBLIC_AURA_BASE, es.
 * http://localhost:8787/); in produzione la base e' /aura/ e i file sono generati/team/screenshot.
 * Se il file manca, il componente mostra il segnaposto (silhouette + nome): mai un buco, mai uno
 * still al posto di una faccia del team.
 *
 * Legge di Max: la riga si legge SEMPRE — banda scura + ombra tripla (classe .riga in vivo.css).
 */
const BASE = process.env.NEXT_PUBLIC_AURA_BASE ?? "/aura/";

type AuraProps = {
  /** nome file nel manifest, es. "n1-hero.webp" */
  file: string;
  alt: string;
  riga?: string;
  /** posizione della riga: bassa (default) / media / sinistra-bassa */
  rigaPos?: "bassa" | "media" | "sinistra";
  /** trattamento CSS: B (default) / carta / acciaio / negativo / filigrana */
  tratt?: "b" | "carta" | "acciaio" | "negativo" | "filigrana";
  /** segnaposto se il file manca: { nome, ruolo } */
  segnaposto?: { nome: string; ruolo: string };
  className?: string;
  objectPosition?: string;
  priority?: boolean;
};

export function Aura({
  file, alt, riga, rigaPos = "bassa", tratt = "b", segnaposto, className, objectPosition, priority,
}: AuraProps) {
  const [manca, setManca] = useState(false);
  const ref = useRef<HTMLImageElement>(null);
  // il 404 di un file mancante puo' arrivare PRIMA dell'idratazione: onError non scatta, si controlla al mount
  useEffect(() => {
    const el = ref.current;
    if (el && el.complete && el.naturalWidth === 0) setManca(true);
  }, []);

  if (manca && segnaposto) {
    return (
      <figure className={cn("foto-segnaposto", className)} role="img" aria-label={alt}>
        <div>
          <b>{segnaposto.nome}</b>
          <span>{segnaposto.ruolo}</span>
        </div>
      </figure>
    );
  }

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
        ref={ref}
        src={`${BASE}${file}`}
        alt={alt}
        loading={priority ? "eager" : "lazy"}
        decoding="async"
        fetchPriority={priority ? "high" : "auto"}
        style={objectPosition ? { objectPosition } : undefined}
        onError={() => setManca(true)}
      />
      {riga && (
        <figcaption
          className={cn(
            "riga",
            rigaPos === "media" ? "riga--media" : "riga--bassa",
            rigaPos === "sinistra" && "riga--sinistra"
          )}
        >
          {riga}
        </figcaption>
      )}
    </figure>
  );
}
