import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";

/* Bottone delle SEZIONI AGGIUNTE (2026-09-12): va a /prenota/, pagina nostra col brand dell'agenzia.
   Componente nuovo: il call-cta.tsx esistente non si tocca (ordine di Max: solo aggiungere). */
export function BottonePrenota({
  da,
  label = "Prenota la chiamata →",
  sublabel,
  principale = false,
  className = "",
}: {
  da: string;
  label?: string;
  sublabel?: string;
  principale?: boolean;
  className?: string;
}) {
  return (
    <Link href={prenotaDa(da)} data-cta className={`sv-btn ${principale ? "sv-btn--bagliore" : ""} ${className}`}>
      <span>
        {label}
        {sublabel && <small>{sublabel}</small>}
      </span>
    </Link>
  );
}
