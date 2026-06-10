"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { CourseCTA, COURSE_URL } from "@/components/course-cta";

const BOOKING_URL = "https://clinquant-pie-aab8d2.netlify.app/";

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
          <div className="max-w-4xl mx-auto px-5 py-3 flex justify-center items-center gap-3 flex-wrap">
            <a href={BOOKING_URL} className="btn-orange group">
              Prenota la Tua Call Gratis
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
            <a
              href={COURSE_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="group inline-flex items-center gap-2 px-5 py-[13px] rounded-[12px] font-semibold text-[14px] bg-white/5 text-white border border-white/20 hover:bg-white/10 hover:border-white/35 transition-all duration-300 whitespace-nowrap"
            >
              <span className="flex flex-col items-start leading-tight text-left">
                <span>Vai al corso completo</span>
                <span className="text-[9px] uppercase tracking-[0.18em] font-bold mt-0.5 text-white/45">System Architect · Accedi ora</span>
              </span>
              <ArrowRight className="h-4 w-4 opacity-60 group-hover:opacity-100 group-hover:translate-x-0.5 transition-transform" strokeWidth={2} />
            </a>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
