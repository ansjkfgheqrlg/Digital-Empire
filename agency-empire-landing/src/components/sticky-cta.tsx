"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";

/** Barra fissa in basso: compare dopo il primo schermo, una sola CTA verso /prenota/. */
export function StickyCTA({ label = "Prenota la chiamata →" }: { label?: string }) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > window.innerHeight * 0.7);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div
          data-visibile={visible ? "1" : "0"}
          className="barra-fissa fixed bottom-0 inset-x-0 z-[200] bg-[#0a0a0a]/90 backdrop-blur-md"
          style={{ borderTop: "1px solid var(--sv-hair)", paddingBottom: "env(safe-area-inset-bottom, 0)" }}
        >
          <div className="sv-container py-2 sm:py-3 flex items-center justify-center gap-4">
            <span className="hidden sm:inline sv-small" style={{ color: "var(--sv-silver-dim)" }}>30 minuti · il sistema in live · niente slide</span>
            <Link href={prenotaDa("sticky")} data-cta className="sv-btn" style={{ padding: "11px 20px", fontSize: "var(--fs-small)" }}>
              <span className="sm:hidden">Prenota</span>
              <span className="hidden sm:inline">{label}</span>
            </Link>
          </div>
        </div>
  );
}
