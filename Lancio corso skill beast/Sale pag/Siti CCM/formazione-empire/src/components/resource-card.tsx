"use client";
import type { Resource } from "@/lib/data";

const typeIcons: Record<Resource["type"], string> = {
  pdf: "PDF",
  md: "MD",
  skill: "SKL",
  zip: "ZIP",
  link: "URL",
};

const typeColors: Record<Resource["type"], string> = {
  pdf: "#fb4604",
  md: "#ff6a2e",
  skill: "#ff8a4a",
  zip: "#8a8594",
  link: "#c9370a",
};

export default function ResourceCard({ resource, dark = false }: { resource: Resource; dark?: boolean }) {
  // "dark" prop ora attiva il look silver-light Empire (mantenuto il nome per compat)
  const bg = dark
    ? "linear-gradient(180deg, #ffffff 0%, #f4f1f7 50%, #e8e3ef 100%)"
    : "#ffffff";
  const border = "rgba(255,255,255,0.85)";
  const fg = "#1c1c1c";
  const fgDim = "rgba(28,28,28,0.6)";
  const hoverBg = dark
    ? "linear-gradient(180deg, #ffffff 0%, #ece6f2 50%, #ddd6e4 100%)"
    : "rgba(28,28,28,0.02)";
  const ringShadow = dark
    ? "0 12px 28px -16px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.9), 0 0 0 1px rgba(138,133,148,0.18)"
    : "none";

  return (
    <a
      href={resource.href}
      className="group flex items-center gap-4 p-4 rounded-xl transition-all relative overflow-hidden"
      style={{ background: bg, border: `1px solid ${border}`, boxShadow: ringShadow, color: fg }}
      onMouseEnter={(e) => { e.currentTarget.style.background = hoverBg; }}
      onMouseLeave={(e) => { e.currentTarget.style.background = bg; }}
    >
      {dark && (
        <span aria-hidden className="absolute inset-0 pointer-events-none rounded-xl" style={{
          backgroundImage:
            "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.4' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
          mixBlendMode: "multiply",
          opacity: 0.45,
        }} />
      )}
      <div
        className="relative flex-shrink-0 w-12 h-12 rounded-lg flex items-center justify-center text-xs font-bold"
        style={{
          background: `${typeColors[resource.type]}1f`,
          color: typeColors[resource.type],
          border: `1px solid ${typeColors[resource.type]}45`,
        }}
      >
        {typeIcons[resource.type]}
      </div>
      <div className="relative flex-1 min-w-0">
        <div className="text-sm font-semibold truncate" style={{ color: fg }}>{resource.title}</div>
        {resource.size && <div className="text-xs mt-0.5" style={{ color: fgDim }}>{resource.size}</div>}
      </div>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{ color: fgDim, transition: "transform 0.2s" }} className="relative group-hover:translate-x-1">
        <line x1="5" y1="12" x2="19" y2="12" />
        <polyline points="12 5 19 12 12 19" />
      </svg>
    </a>
  );
}
