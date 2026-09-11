import Link from "next/link";
import { cn } from "@/lib/utils";
import { PRENOTA, prenotaDa } from "@/lib/contatti";

/**
 * CTA di sezione (Dossier 37 v2, C1.1): SEMPRE verso /prenota/ (pagina nostra) via <Link>,
 * con `?da=<sezione>` per sapere da dove si prenota. Mai un dominio esterno, mai un'ancora al listino.
 */
/** @deprecated solo per le sezioni v1 in attesa di rimozione (F7): oggi è la pagina nostra, non il dominio del corso */
export const CALL_URL = PRENOTA;

export function CallCTA({
  da = "v1",
  label = "Prenota la chiamata →",
  sublabel,
  principale = false,
  className,
}: {
  da?: string;
  label?: string;
  sublabel?: string;
  principale?: boolean;
  className?: string;
  /** ignorato: compatibilità con le sezioni v1 */
  variant?: "dark" | "light";
}) {
  return (
    <Link
      href={prenotaDa(da)}
      data-cta
      className={cn("sv-btn", principale && "sv-btn--bagliore", className)}
    >
      <span>
        {label}
        {sublabel && <small>{sublabel}</small>}
      </span>
    </Link>
  );
}
