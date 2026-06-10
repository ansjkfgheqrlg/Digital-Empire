"use client";

import { ArrowRight } from "lucide-react";

export const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";

export function CourseCTA({ variant = "light" }: { variant?: "light" | "dark" }) {
  const base =
    "group inline-flex items-center gap-2.5 px-6 py-[13px] rounded-[12px] font-semibold text-[15px] transition-all duration-300 w-full justify-center";

  const styles =
    variant === "light"
      ? "bg-[#1c1c1c]/5 text-[#1c1c1c] border border-[#1c1c1c]/20 hover:bg-[#1c1c1c]/10 hover:border-[#1c1c1c]/35"
      : "bg-white/5 text-white border border-white/20 hover:bg-white/10 hover:border-white/35";

  const sub =
    variant === "light" ? "text-[#1c1c1c]/45" : "text-white/45";

  return (
    <a
      href={COURSE_URL}
      target="_blank"
      rel="noopener noreferrer"
      className={`${base} ${styles}`}
    >
      <span className="flex flex-col items-start leading-tight text-left">
        <span>Vai al corso completo</span>
        <span className={`text-[10px] uppercase tracking-[0.18em] font-bold mt-0.5 ${sub}`}>
          System Architect · Accedi ora
        </span>
      </span>
      <ArrowRight className="h-4 w-4 ml-auto opacity-60 group-hover:opacity-100 group-hover:translate-x-0.5 transition-transform shrink-0" strokeWidth={2} />
    </a>
  );
}
