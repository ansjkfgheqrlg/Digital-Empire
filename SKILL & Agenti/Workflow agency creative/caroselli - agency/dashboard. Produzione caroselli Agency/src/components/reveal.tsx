"use client";

import { motion } from "framer-motion";
import { cn } from "@/lib/utils";

type Variant = "up" | "left" | "right" | "scale" | "fade";

const variants = {
  up:    { hidden: { opacity: 0, y: 32 },       visible: { opacity: 1, y: 0 } },
  left:  { hidden: { opacity: 0, x: -40 },      visible: { opacity: 1, x: 0 } },
  right: { hidden: { opacity: 0, x: 40 },       visible: { opacity: 1, x: 0 } },
  scale: { hidden: { opacity: 0, scale: 0.94 }, visible: { opacity: 1, scale: 1 } },
  fade:  { hidden: { opacity: 0 },              visible: { opacity: 1 } },
};

export function Reveal({
  children,
  variant = "up",
  delay = 0,
  className,
}: {
  children: React.ReactNode;
  variant?: Variant;
  delay?: number;
  className?: string;
}) {
  return (
    <motion.div
      className={cn(className)}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: "-10% 0px" }}
      variants={variants[variant]}
      transition={{ duration: 0.7, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </motion.div>
  );
}
