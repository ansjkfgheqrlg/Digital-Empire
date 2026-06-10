"use client";

import { animate, useInView } from "framer-motion";
import { useEffect, useRef, useState } from "react";

export function CountUp({
  to,
  prefix = "",
  suffix = "",
  duration = 1.8,
  decimals = 0,
}: {
  to: number;
  prefix?: string;
  suffix?: string;
  duration?: number;
  decimals?: number;
}) {
  const ref = useRef<HTMLSpanElement>(null);
  const inView = useInView(ref, { once: true, amount: 0.5 });
  const [value, setValue] = useState(0);

  useEffect(() => {
    if (!inView) return;
    const controls = animate(0, to, {
      duration,
      ease: [0.34, 1.56, 0.64, 1],
      onUpdate(v) {
        if (decimals > 0) {
          setValue(Number(v.toFixed(decimals)));
        } else {
          setValue(Math.round(v));
        }
      },
    });
    return () => controls.stop();
  }, [inView, to, duration, decimals]);

  return (
    <span ref={ref}>
      {prefix}
      {decimals > 0 ? value.toFixed(decimals) : value}
      {suffix}
    </span>
  );
}
