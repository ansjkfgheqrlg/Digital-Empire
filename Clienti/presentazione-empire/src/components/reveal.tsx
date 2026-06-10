"use client";

import { motion, useInView, Variants } from "framer-motion";
import { useRef } from "react";
import { cn } from "@/lib/utils";

type Variant = "up" | "left" | "right" | "scale" | "fade";

const variants: Record<Variant, Variants> = {
  up:    { hidden: { opacity: 0, y: 24 },       visible: { opacity: 1, y: 0 } },
  left:  { hidden: { opacity: 0, x: -32 },      visible: { opacity: 1, x: 0 } },
  right: { hidden: { opacity: 0, x: 32 },       visible: { opacity: 1, x: 0 } },
  scale: { hidden: { opacity: 0, scale: 0.95 }, visible: { opacity: 1, scale: 1 } },
  fade:  { hidden: { opacity: 0 },              visible: { opacity: 1 } },
};

export function Reveal({
  children,
  variant = "up",
  delay = 0,
  className,
  as: Tag = "div",
}: {
  children: React.ReactNode;
  variant?: Variant;
  delay?: number;
  className?: string;
  as?: keyof typeof motion;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true, amount: 0 });
  const Comp = motion[Tag] as typeof motion.div;

  return (
    <Comp
      ref={ref}
      className={cn(className)}
      initial="hidden"
      animate={inView ? "visible" : "hidden"}
      variants={variants[variant]}
      transition={{ duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </Comp>
  );
}
