"use client";

import { Phone } from "lucide-react";
import { cn } from "@/lib/utils";

export const CALL_URL = "https://chiamata-formazione.netlify.app/";

export function CallCTA({
  variant = "dark",
  label = "Prenota una Chiamata Gratuita",
  sublabel = "30 min · Gratuita · Zero impegno",
  className,
}: {
  variant?: "dark" | "light";
  label?: string;
  sublabel?: string;
  className?: string;
}) {
  const base =
    "group inline-flex items-center gap-2.5 px-6 py-[14px] rounded-[12px] font-semibold text-[15px] transition-all duration-300";

  const styles =
    variant === "dark"
      ? "bg-white/5 text-white border border-white/20 hover:bg-white/10 hover:border-white/35 backdrop-blur-sm"
      : "bg-ink/5 text-ink border border-ink/25 hover:bg-ink/10 hover:border-ink/45";

  return (
    <a
      href={CALL_URL}
      target="_blank"
      rel="noopener noreferrer"
      className={cn(base, styles, className)}
    >
      <Phone className="h-4 w-4 opacity-80 group-hover:opacity-100" strokeWidth={2} />
      <span className="flex flex-col items-start leading-tight text-left">
        <span>{label}</span>
        <span className={cn("text-[10px] uppercase tracking-[0.18em] font-bold mt-0.5", variant === "dark" ? "text-white/70" : "text-ink/50")}>
          {sublabel}
        </span>
      </span>
    </a>
  );
}
