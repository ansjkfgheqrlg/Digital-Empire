"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronDown } from "lucide-react";

type FAQ = {
  q: string;
  a: string;
};

export function FAQAccordion({ items }: { items: FAQ[] }) {
  const [openIdx, setOpenIdx] = useState<number | null>(0);

  return (
    <div className="flex flex-col">
      {items.map((it, i) => {
        const isOpen = openIdx === i;
        return (
          <div key={i} className="faq-item">
            <button
              type="button"
              className="faq-trigger"
              data-state={isOpen ? "open" : "closed"}
              aria-expanded={isOpen}
              onClick={() => setOpenIdx(isOpen ? null : i)}
            >
              <span>{it.q}</span>
              <ChevronDown
                className="faq-icon h-5 w-5 text-[#062155]"
                strokeWidth={2.2}
              />
            </button>
            <AnimatePresence initial={false}>
              {isOpen && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{
                    duration: 0.35,
                    ease: [0.22, 1, 0.36, 1],
                  }}
                  className="overflow-hidden"
                >
                  <div className="faq-content">{it.a}</div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}
