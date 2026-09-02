"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { CALL_URL } from "@/components/call-cta";

/** Barra fissa in basso. B8: su mobile occupava troppa altezza e copriva il contenuto —
 *  padding e testo ridotti sotto sm, label piena solo da sm in su.
 *  File riformattato senza cambi di logica (era su riga singola). */
export function StickyCTA({
  href,
  label = "Prenota una Chiamata",
}: {
  href: string;
  label?: string;
}) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > window.innerHeight * 0.7);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ y: 80, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 80, opacity: 0 }}
          transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
          className="fixed bottom-0 inset-x-0 z-[200] border-t border-white/10 bg-[#131313]/90 backdrop-blur-md"
          style={{ paddingBottom: "env(safe-area-inset-bottom, 0)" }}
        >
          <div className="max-w-4xl mx-auto px-4 py-2 sm:px-5 sm:py-3 flex items-center justify-center gap-4">
            <a
              href={href}
              className="hidden sm:inline-flex text-sm font-medium text-white/60 hover:text-white transition-colors"
            >
              Prezzi
            </a>
            <a
              href={CALL_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-orange group !px-5 !py-3 !text-[13px] sm:!px-7 sm:!py-4 sm:!text-[15px]"
            >
              <span className="sm:hidden">Prenota</span>
              <span className="hidden sm:inline">{label}</span>
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
