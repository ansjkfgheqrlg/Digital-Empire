"use client";
import { useEffect } from "react";

/* STICKY GUARD (BRIEF-F3 BLOCCO D · dossier 39B, nota trasversale sulla StickyCTA).
   Non rende nulla: mette due classi su <body>, lette da src/app/ritocchi.css.
   - `dopo-hero`    : scrollY > innerHeight * 3 (listener scroll passivo, letto in un solo rAF per frame).
   - `cta-in-vista` : almeno un bersaglio è nel viewport (IntersectionObserver). Bersagli: ogni `[data-cta]`,
                      `#prenota`, ogni `.btn-orange` di pagina che NON sta dentro un elemento `.fixed`
                      (la sticky stessa e l'header restano fuori) e ogni `footer`.
   Effetto in CSS: la barra fissa di giugno (`.fixed.bottom-0.z-[200]`) è nascosta finché il body non ha
   `.dopo-hero` e sparisce quando ha `.cta-in-vista` → un solo bottone arancione per schermata.
   Zero dipendenze. Emperator la monta in page.tsx (`<StickyGuard />`, una volta, dove vuole dentro <main>). */
export function StickyGuard() {
  useEffect(() => {
    const body = document.body;
    const CLASSE_HERO = "dopo-hero";
    const CLASSE_CTA = "cta-in-vista";

    /* --- 1. dopo-hero: scroll passivo + rAF --- */
    let ticket: number | null = null;
    const misura = () => {
      ticket = null;
      const oltre = window.scrollY > window.innerHeight * 3;
      if (body.classList.contains(CLASSE_HERO) !== oltre) body.classList.toggle(CLASSE_HERO, oltre);
    };
    const onScroll = () => {
      if (ticket === null) ticket = window.requestAnimationFrame(misura);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    misura();

    /* --- 2. cta-in-vista: IntersectionObserver sui bersagli --- */
    let osservatore: IntersectionObserver | null = null;
    if (typeof IntersectionObserver !== "undefined") {
      const bersagli = new Set<Element>();
      document.querySelectorAll("[data-cta], #prenota, footer").forEach((el) => bersagli.add(el));
      document.querySelectorAll(".btn-orange").forEach((el) => {
        if (!el.closest(".fixed")) bersagli.add(el);
      });
      if (bersagli.size > 0) {
        const inVista = new Set<Element>();
        osservatore = new IntersectionObserver(
          (voci) => {
            for (const v of voci) {
              if (v.isIntersecting) inVista.add(v.target);
              else inVista.delete(v.target);
            }
            body.classList.toggle(CLASSE_CTA, inVista.size > 0);
          },
          { threshold: 0.05 },
        );
        bersagli.forEach((b) => osservatore!.observe(b));
      }
    }

    /* --- 3. pulizia --- */
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      if (ticket !== null) window.cancelAnimationFrame(ticket);
      osservatore?.disconnect();
      body.classList.remove(CLASSE_HERO, CLASSE_CTA);
    };
  }, []);

  return null;
}
