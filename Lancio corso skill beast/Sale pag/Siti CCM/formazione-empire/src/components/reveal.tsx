"use client";
import { motion, useReducedMotion } from "framer-motion";
import type { ReactNode } from "react";

type Variant = "up" | "left" | "right" | "scale" | "fade";

type Props = {
  children: ReactNode;
  delay?: number;
  y?: number;
  className?: string;
  variant?: Variant;
};

export default function Reveal({ children, delay = 0, y = 28, className, variant = "up" }: Props) {
  const reduce = useReducedMotion();

  const initial =
    variant === "up"    ? { opacity: 0, y } :
    variant === "left"  ? { opacity: 0, x: -40 } :
    variant === "right" ? { opacity: 0, x: 40 } :
    variant === "scale" ? { opacity: 0, scale: 0.94 } :
                          { opacity: 0 };
  const animate =
    variant === "up"    ? { opacity: 1, y: 0 } :
    variant === "left" || variant === "right" ? { opacity: 1, x: 0 } :
    variant === "scale" ? { opacity: 1, scale: 1 } :
                          { opacity: 1 };

  return (
    <motion.div
      initial={reduce ? undefined : initial}
      whileInView={reduce ? undefined : animate}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1], delay }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
