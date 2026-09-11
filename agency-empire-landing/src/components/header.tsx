"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { prenotaDa } from "@/lib/contatti";

const NAV_LINKS = [
  { label: "Sistemi", href: "#sistemi" },
  { label: "Prove", href: "#prove" },
  { label: "Prezzi", href: "#prezzi" },
];

/** Header: compare dopo 600px, canone v3 (ink, hairline, una CTA arancione verso /prenota/). */
export function Header() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 600);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <AnimatePresence>
      {visible && (
        <motion.header
          initial={{ y: -72, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -72, opacity: 0 }}
          transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
          className="fixed top-0 inset-x-0 z-[190] sv-hair bg-[#0a0a0a]/90 backdrop-blur-md"
          style={{ borderTop: "none", borderBottom: "1px solid var(--sv-hair)" }}
        >
          <div className="sv-container h-[60px] flex items-center justify-between gap-6">
            <Link href="/" className="flex items-center gap-1.5 font-bold text-white whitespace-nowrap sv-body">
              <span>Digital Empire</span>
              <span style={{ color: "var(--sv-orange)" }} aria-hidden="true">✦</span>
            </Link>
            <nav className="hidden md:flex items-center gap-8">
              {NAV_LINKS.map((link) => (
                <a key={link.href} href={link.href} className="sv-mono text-white/90 hover:text-white transition-colors">
                  {link.label}
                </a>
              ))}
            </nav>
            <Link href={prenotaDa("header")} data-cta className="sv-btn shrink-0" style={{ padding: "9px 16px", fontSize: "var(--fs-small)" }}>
              Prenota
            </Link>
          </div>
        </motion.header>
      )}
    </AnimatePresence>
  );
}
