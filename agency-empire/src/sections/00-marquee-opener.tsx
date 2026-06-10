const TICKER_ITEMS = [
  "Digital Empire",
  "AI Workflow Agency",
  "Outreach Workflow",
  "Content Workflow",
  "Milano · Dubai",
  "Demo gratuita",
];

export function MarqueeOpener() {
  const repeated = Array.from({ length: 6 }).flatMap(() => TICKER_ITEMS);
  return (
    <div
      aria-hidden
      style={{
        marginTop: "68px",
        /* Barra metallica navy-crema */
        background: [
          /* Luce silver in cima */
          "linear-gradient(180deg, rgba(255,255,255,0.50) 0%, rgba(255,255,255,0.15) 18%, transparent 50%)",
          /* Gradiente metallico silver-orange orizzontale */
          "linear-gradient(90deg, #c8c4c0 0%, #ddd8d4 14%, #f0edec 28%, #ffffff 38%, rgba(251,70,4,0.90) 50%, #ffffff 62%, #f0edec 72%, #ddd8d4 86%, #c8c4c0 100%)",
        ].join(", "),
        boxShadow: [
          "inset 0 1.5px 0 rgba(255,255,255,0.88)",
          "inset 0 -2px 0 rgba(0,0,30,0.30)",
          "0 6px 24px -12px rgba(251,70,4,0.25)",
        ].join(", "),
      }}
      className="overflow-hidden py-[11px] relative"
    >
      <div className="marquee flex gap-10 whitespace-nowrap text-[0.72rem] uppercase tracking-[0.30em] font-bold text-[#1c1c1c]">
        {repeated.map((item, i) => (
          <span key={i} className="flex items-center gap-10 shrink-0">
            <span>{item}</span>
            <span style={{ color: "#fb4604", opacity: 0.8 }}>✦</span>
          </span>
        ))}
      </div>
    </div>
  );
}
