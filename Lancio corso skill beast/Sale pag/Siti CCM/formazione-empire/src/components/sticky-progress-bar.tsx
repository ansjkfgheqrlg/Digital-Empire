"use client";
import { useEffect, useState } from "react";

export default function StickyProgressBar({
  pct,
  completed,
  total,
  courseTitle,
}: {
  pct: number;
  completed: number;
  total: number;
  courseTitle: string;
}) {
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 360);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div
      className="sticky z-40 transition-all"
      style={{
        top: 64,
        opacity: visible ? 1 : 0,
        transform: visible ? "translateY(0)" : "translateY(-12px)",
        pointerEvents: visible ? "auto" : "none",
      }}
      aria-hidden={!visible}
    >
      <div
        className="container-wide"
      >
        <div
          className="flex items-center gap-4 px-5 py-3 rounded-full"
          style={{
            background: "rgba(20,20,20,0.92)",
            backdropFilter: "saturate(140%) blur(14px)",
            border: "1px solid rgba(251,70,4,0.22)",
            boxShadow: "0 20px 50px -14px rgba(0,0,0,0.7)",
          }}
        >
          <div className="hidden sm:flex flex-col min-w-0 flex-shrink-0 max-w-[40%]">
            <span className="text-[10px] font-semibold uppercase tracking-widest" style={{ color: "rgba(251,70,4,0.85)" }}>In corso</span>
            <span className="text-sm font-bold truncate" style={{ color: "#fafaf6" }}>{courseTitle}</span>
          </div>
          <div className="flex-1 progress-track" style={{ background: "rgba(249,249,249,0.08)", height: 8 }}>
            <div className="progress-fill-orange" style={{ width: `${pct}%`, height: 8, boxShadow: "0 0 14px rgba(251,70,4,0.5)" }} />
          </div>
          <div className="flex items-baseline gap-2 flex-shrink-0">
            <span className="text-lg font-extrabold text-orange-pure">{pct}%</span>
            <span className="hidden md:inline text-xs" style={{ color: "rgba(250,250,246,0.55)" }}>
              {completed}/{total}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
