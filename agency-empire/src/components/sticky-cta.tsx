"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight, Phone } from "lucide-react";

export function StickyCTA() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onScroll = () => {
      setVisible(window.scrollY > window.innerHeight * 0.7);
    };
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
          transition={{
            duration: 0.35,
            ease: [0.22, 1, 0.36, 1],
          }}
          className="fixed bottom-0 inset-x-0 z-[200] border-t border-white/10 bg-[#0a0a0a]/95 backdrop-blur-md"
          style={{ paddingBottom: "env(safe-area-inset-bottom, 0)" }}
        >
          <div className="container-default py-3 flex items-center justify-between gap-3 flex-wrap">
            <div className="hidden md:flex items-center gap-3 min-w-0">
              <span className="bubble-gold !py-1 !px-2.5 !text-xs">
                <Phone className="h-3 w-3" /> Strategy Call gratuita
              </span>
              <span className="text-sm text-white/60 truncate">
                Vediamo insieme dove perdi clienti.
              </span>
            </div>
            <a
              href="/prenota"
              className="btn-gold !py-2.5 !px-5 !text-sm group ml-auto"
            >
              Prenota Ora
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
