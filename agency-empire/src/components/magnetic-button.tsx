"use client";

import { useRef } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";
import { cn } from "@/lib/utils";

type MagneticButtonProps = {
  children: React.ReactNode;
  href?: string;
  className?: string;
  onClick?: () => void;
  intensity?: number;
};

export function MagneticButton({
  children,
  href,
  className,
  onClick,
  intensity = 0.15,
}: MagneticButtonProps) {
  const ref = useRef<HTMLDivElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const sx = useSpring(x, { stiffness: 200, damping: 18, mass: 0.4 });
  const sy = useSpring(y, { stiffness: 200, damping: 18, mass: 0.4 });

  const onMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!ref.current) return;
    if (window.matchMedia("(hover: none)").matches) return;
    const rect = ref.current.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = e.clientX - cx;
    const dy = e.clientY - cy;
    const dist = Math.hypot(dx, dy);
    if (dist < 100) {
      x.set(dx * intensity);
      y.set(dy * intensity);
    }
  };

  const onLeave = () => {
    x.set(0);
    y.set(0);
  };

  const Comp = motion.div;
  const inner = (
    <Comp
      ref={ref}
      style={{ x: sx, y: sy, display: "inline-block" }}
      onMouseMove={onMove}
      onMouseLeave={onLeave}
    >
      {children}
    </Comp>
  );

  if (href) {
    return (
      <a href={href} onClick={onClick} className={cn("inline-block", className)}>
        {inner}
      </a>
    );
  }
  return (
    <button onClick={onClick} className={cn("inline-block bg-transparent border-0 p-0", className)}>
      {inner}
    </button>
  );
}
