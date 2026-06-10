type Props = {
  variant?: "dark" | "light";
  items?: string[];
};

const DEFAULT_ITEMS = [
  "Ingegneria strategica",
  "Landing Page Studio",
  "CRO Engineering",
  "Conversion Engineered",
  "Audit gratuito",
  "Risposta in 24h",
];

export function MarqueeMini({ variant = "dark", items = DEFAULT_ITEMS }: Props) {
  const isDark = variant === "dark";
  const list = [...items, ...items, ...items, ...items];

  return (
    <div
      className={`border-y overflow-hidden py-2.5 ${
        isDark
          ? "border-white/10 bg-[#0a0a0a]/50"
          : "border-black/8 bg-[#faf6ee]/50"
      }`}
      aria-hidden
    >
      <div
        className={`marquee-fast flex gap-8 whitespace-nowrap text-[0.7rem] uppercase tracking-[0.3em] font-medium ${
          isDark ? "text-white/40" : "text-black/40"
        }`}
      >
        {list.map((item, i) => (
          <span key={i} className="flex items-center gap-8 shrink-0">
            <span>{item}</span>
            <span className="text-gold-pure">✦</span>
          </span>
        ))}
      </div>
    </div>
  );
}
