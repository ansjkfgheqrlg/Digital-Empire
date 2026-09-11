"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Menu, X, ArrowRight } from "lucide-react";

const NAV_ITEMS = [
  { href: "#servizi", label: "Servizi" },
  { href: "#preventa", label: "Preventa" },
  { href: "#metodo", label: "Metodo" },
  { href: "#processo", label: "Processo" },
  { href: "#lavori", label: "Lavori" },
  { href: "#prove", label: "Prove" },
  { href: "#faq", label: "FAQ" },
];

export function Navbar() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  return (
    <>
      {/* ── FIXED TOP BAR ── */}
      <header className="fixed top-0 inset-x-0 z-[150] pointer-events-none">
        <nav
          aria-label="Principale"
          className="container-wide flex items-center justify-between gap-4 pt-5 pb-3 pointer-events-none"
        >
          {/* LOGO */}
          <a
            href="#"
            className="glass-block flex items-center gap-2.5 group pointer-events-auto"
            aria-label="Digital Empire — Home"
          >
            <span
              className="grid place-items-center rounded-lg w-9 h-9 font-display font-bold text-[0.95rem] tracking-[0.08em]"
              style={{
                color: "#edeebe",
                background: "linear-gradient(180deg, #1a4090 0%, #062155 100%)",
                boxShadow:
                  "0 0 18px rgba(6,33,85,0.40), inset 0 1px 0 rgba(237,238,190,0.30), inset 0 -1px 0 rgba(0,0,20,0.35)",
              }}
            >
              DE
            </span>
            <span className="hidden sm:block font-display tracking-[0.18em] text-[0.78rem] font-bold text-[#062155] pr-1">
              DIGITAL EMPIRE
            </span>
          </a>

          {/* DESKTOP NAV — hidden below lg (1024px) */}
          <ul className="hidden lg:flex items-center gap-1 glass-block px-2 pointer-events-auto">
            {NAV_ITEMS.map((it) => (
              <li key={it.href}>
                <a
                  href={it.href}
                  className="px-2.5 xl:px-3.5 py-2 text-[0.875rem] font-medium rounded-lg text-[#062155]/75 hover:text-[#062155] hover:bg-[#062155]/8 transition-colors"
                >
                  {it.label}
                </a>
              </li>
            ))}
          </ul>

          {/* RIGHT CLUSTER */}
          <div className="flex items-center gap-2 pointer-events-auto">
            {/* CTA desktop */}
            <a
              href="/prenota"
              className="hidden lg:inline-flex btn-gold !py-2 !px-4 !text-[0.875rem] group"
            >
              Demo gratuita
              <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" />
            </a>

            {/* Hamburger — visible below lg */}
            <button
              type="button"
              aria-label={open ? "Chiudi menu" : "Apri menu"}
              aria-expanded={open}
              onClick={() => setOpen((v) => !v)}
              className="lg:hidden glass-block !p-0 grid place-items-center w-10 h-10 text-[#062155]/80 hover:text-[#062155]"
            >
              <AnimatePresence mode="wait" initial={false}>
                <motion.span
                  key={open ? "x" : "menu"}
                  initial={{ opacity: 0, rotate: open ? -90 : 90, scale: 0.8 }}
                  animate={{ opacity: 1, rotate: 0, scale: 1 }}
                  exit={{ opacity: 0, rotate: open ? 90 : -90, scale: 0.8 }}
                  transition={{ duration: 0.18 }}
                  className="grid place-items-center"
                >
                  {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
                </motion.span>
              </AnimatePresence>
            </button>
          </div>
        </nav>
      </header>

      {/* ── MOBILE FULL-SCREEN OVERLAY ── z-140 (below header z-150) */}
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.22 }}
            className="fixed inset-0 z-[140] lg:hidden flex flex-col"
            style={{
              background: "linear-gradient(180deg, #ffffff 0%, #f5f0e8 100%)",
            }}
          >
            {/* spacer that clears the fixed top bar */}
            <div className="h-[72px] shrink-0" />

            {/* scrollable content */}
            <div className="flex-1 overflow-y-auto px-6 pt-2 pb-10">
              <nav aria-label="Menu mobile">
                <ul>
                  {NAV_ITEMS.map((it, i) => (
                    <motion.li
                      key={it.href}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{
                        delay: 0.06 + i * 0.055,
                        duration: 0.32,
                        ease: [0.22, 1, 0.36, 1],
                      }}
                    >
                      <a
                        href={it.href}
                        onClick={() => setOpen(false)}
                        className="flex items-center justify-between py-4 text-[1.4rem] font-semibold tracking-[-0.01em] text-[#062155] border-b border-[#062155]/8 group"
                      >
                        <span>{it.label}</span>
                        <ArrowRight className="h-4 w-4 text-[#062155]/25 transition-transform group-hover:translate-x-0.5 group-hover:text-[#062155]/55" />
                      </a>
                    </motion.li>
                  ))}
                </ul>
              </nav>

              <motion.div
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.38, duration: 0.36, ease: [0.22, 1, 0.36, 1] }}
                className="mt-8 flex flex-col gap-3"
              >
                <a
                  href="/prenota"
                  onClick={() => setOpen(false)}
                  className="btn-gold btn-gold--lg w-full justify-center group"
                >
                  Prenota Demo Gratuita
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </a>
                <p className="text-center text-[0.8rem] text-[#062155]/40">
                  Gratuita · 30 min · Risposta entro 24h
                </p>
              </motion.div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
