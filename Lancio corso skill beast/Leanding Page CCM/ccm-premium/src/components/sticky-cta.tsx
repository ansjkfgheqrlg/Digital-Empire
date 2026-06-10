"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight } from "lucide-react";

const BOOKING_URL = "https://clinquant-pie-aab8d2.netlify.app/";
const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";

export function StickyCTA() {
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
          <div className="max-w-4xl mx-auto px-5 py-3 flex justify-center gap-3 flex-wrap">
            <a href={BOOKING_URL} className="btn-orange group">
              Prenota la Tua Call Gratis
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
            <a
              href={COURSE_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/[0.04] px-6 py-3 text-sm font-semibold text-white/70 backdrop-blur-sm transition-all duration-200 hover:border-[#fb4604]/70 hover:text-[#fb4604] hover:bg-[#fb4604]/[0.06] group"
            >
              Diventa System Architect
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
