"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { CALL_URL } from "@/components/call-cta";

const NAV_LINKS = [
  { label: "Servizi", href: "#servizi" },
  { label: "Risultati", href: "#risultati" },
  { label: "Prezzi", href: "#prenota" },
];

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
          className="fixed top-0 inset-x-0 z-[190] border-b border-white/10 bg-[#131313]/90 backdrop-blur-md"
        >
          <div className="max-w-6xl mx-auto px-6 h-[60px] flex items-center justify-between gap-6">
            {/* Wordmark */}
            <a
              href="#"
              className="flex items-center gap-1.5 font-bold text-[16px] text-white whitespace-nowrap"
            >
              <span>Digital Empire</span>
              <span className="text-orange-pure" aria-hidden="true">
                ✦
              </span>
            </a>

            {/* Desktop nav links */}
            <nav className="hidden md:flex items-center gap-8">
              {NAV_LINKS.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="text-[12.5px] font-semibold uppercase tracking-[0.14em] text-white/90 transition-colors duration-200 hover:text-white"
                >
                  {link.label}
                </a>
              ))}
            </nav>

            {/* Prenota button */}
            <a
              href={CALL_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-orange shrink-0"
              style={{ padding: "0.55rem 1.1rem", fontSize: "14px" }}
            >
              Prenota
            </a>
          </div>
        </motion.header>
      )}
    </AnimatePresence>
  );
}
