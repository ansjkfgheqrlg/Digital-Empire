# components

> Source: File system (`SKILL & Agenti\SKILL\Skill empire-premium-style\references\components.md`)
> Collected: 2026-05-06
> Published: Unknown

# Componenti base — codice integrale

Genera esattamente questi 5 file. Non modificare niente.

## `src/lib/utils.ts`

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

## `src/components/smooth-scroll-provider.tsx`

```tsx
"use client";

import { useEffect } from "react";
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
}

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const prefersReduced =
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) return;

    const lenis = new Lenis({ lerp: 0.1, smoothWheel: true, wheelMultiplier: 1 });

    lenis.on("scroll", ScrollTrigger.update);
    const tickerCb = (time: number) => lenis.raf(time * 1000);
    gsap.ticker.add(tickerCb);
    gsap.ticker.lagSmoothing(0);

    return () => {
      gsap.ticker.remove(tickerCb);
      lenis.destroy();
    };
  }, []);

  return <>{children}</>;
}
```

## `src/components/reveal.tsx`

```tsx
"use client";

import { motion, useInView, Variants } from "framer-motion";
import { useRef } from "react";
import { cn } from "@/lib/utils";

type Variant = "up" | "left" | "right" | "scale" | "fade";

const variants: Record<Variant, Variants> = {
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
  as: Tag = "div",
}: {
  children: React.ReactNode;
  variant?: Variant;
  delay?: number;
  className?: string;
  as?: keyof typeof motion;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true, margin: "0px 0px -10% 0px" });
  const Comp = motion[Tag] as typeof motion.div;

  return (
    <Comp
      ref={ref}
      className={cn(className)}
      initial="hidden"
      animate={inView ? "visible" : "hidden"}
      variants={variants[variant]}
      transition={{ duration: 0.7, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </Comp>
  );
}
```

## `src/components/count-up.tsx`

```tsx
"use client";

import { animate, useInView } from "framer-motion";
import { useEffect, useRef, useState } from "react";

export function CountUp({
  to, prefix = "", suffix = "", duration = 1.8,
}: { to: number; prefix?: string; suffix?: string; duration?: number }) {
  const ref = useRef<HTMLSpanElement>(null);
  const inView = useInView(ref, { once: true, amount: 0.5 });
  const [value, setValue] = useState(0);

  useEffect(() => {
    if (!inView) return;
    const controls = animate(0, to, {
      duration, ease: [0.22, 1, 0.36, 1],
      onUpdate(v) { setValue(Math.round(v)); },
    });
    return () => controls.stop();
  }, [inView, to, duration]);

  return <span ref={ref}>{prefix}{value}{suffix}</span>;
}
```

## `src/components/sticky-cta.tsx`

```tsx
"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight } from "lucide-react";

export function StickyCTA({ href, label = "Prenota Ora" }: { href: string; label?: string }) {
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
          <div className="max-w-4xl mx-auto px-5 py-3 flex justify-center">
            <a href={href} className="btn-orange group">
              {label}
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </a>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```
