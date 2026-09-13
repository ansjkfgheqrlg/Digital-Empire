"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { PRENOTA } from "@/lib/contatti";
import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A03 (Dossier 38 v2) — la CTA fissa: pillola flottante «Prenota la chiamata · 30 min» → /prenota/.
   NON va in home per ora (Max decide): si esporta e basta. Non sostituisce la barra <StickyCTA> esistente
   (src/components/sticky-cta.tsx, z 200, che si tocca solo con un ordine): questa sta in basso a destra, z 190.
   Compare quando l'hero (`main > section:first-of-type`) esce dallo schermo; sparisce (`hidden` + `inert`) quando una
   CTA di pagina (`[data-cta]`) o il footer sono in vista, così non copre mai il bottone vero. */
export function CtaFissa() {
  const [oltreHero, setOltreHero] = useState(false);
  const [coperta, setCoperta] = useState(false);

  useEffect(() => {
    if (typeof IntersectionObserver === "undefined") {
      setOltreHero(true);
      return;
    }
    const hero = document.querySelector<HTMLElement>("main > section:first-of-type");
    let osHero: IntersectionObserver | null = null;
    if (hero) {
      osHero = new IntersectionObserver(([e]) => setOltreHero(!e.isIntersecting), { threshold: 0 });
      osHero.observe(hero);
    } else {
      setOltreHero(true);
    }

    const bersagli = [...Array.from(document.querySelectorAll<HTMLElement>("[data-cta]")), ...Array.from(document.querySelectorAll("footer"))];
    const inVista = new Set<Element>();
    const osCta = new IntersectionObserver(
      (voci) => {
        for (const v of voci) {
          if (v.isIntersecting) inVista.add(v.target);
          else inVista.delete(v.target);
        }
        setCoperta(inVista.size > 0);
      },
      { threshold: 0.05 },
    );
    bersagli.forEach((b) => osCta.observe(b));

    return () => {
      osHero?.disconnect();
      osCta.disconnect();
    };
  }, []);

  const nascosta = !oltreHero || coperta;
  return (
    <div className="vivo">
      <div className="ctaf" hidden={nascosta} inert={nascosta ? true : undefined}>
        <Link href={PRENOTA} className="sv-btn" aria-label={`Prenota la chiamata, ${FATTI.minutiChiamata} minuti`}>
          Prenota la chiamata
          <small>· {FATTI.minutiChiamata} min</small>
        </Link>
      </div>
    </div>
  );
}
