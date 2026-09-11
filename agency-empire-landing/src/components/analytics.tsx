"use client";

import { useEffect } from "react";
import { Analytics } from "@vercel/analytics/next";
import { track } from "@vercel/analytics";

/**
 * Misura due cose sole (Dossier 37, F0 — C1.2): il clic su una CTA e la chiamata prenotata.
 * Nessun cookie, nessun banner (Vercel Web Analytics e' privacy-first: la lezione `dnt=1` di Armageddon).
 *
 * - `cta_click`     ogni <a> o <button> con `data-cta`, oppure che porta a /prenota o a Calendly.
 *                    `sezione` = id della <section> piu' vicina (o "fuori-sezione").
 * - `call_prenotata` il postMessage `calendly.event_scheduled` dell'embed su /prenota.
 */
export function EmpireAnalytics() {
  useEffect(() => {
    const onClick = (e: MouseEvent) => {
      const target = (e.target as HTMLElement | null)?.closest<HTMLElement>(
        "a, button"
      );
      if (!target) return;
      const href = (target as HTMLAnchorElement).getAttribute("href") ?? "";
      const isCta =
        target.hasAttribute("data-cta") ||
        href.includes("/prenota") ||
        href.includes("calendly.com");
      if (!isCta) return;
      const section = target.closest("section");
      track("cta_click", {
        sezione: section?.id || target.dataset.cta || "fuori-sezione",
        testo: (target.textContent ?? "").trim().slice(0, 60),
      });
    };

    const onMessage = (e: MessageEvent) => {
      if (
        typeof e.data === "object" &&
        e.data &&
        (e.data as { event?: string }).event === "calendly.event_scheduled"
      ) {
        // C3.2: `?da=Nxx` sull'URL di /prenota/ dice da quale sezione si e' arrivati alla prenotazione
        const da = new URLSearchParams(window.location.search).get("da") ?? "diretto";
        track("call_prenotata", { da });
      }
    };

    document.addEventListener("click", onClick, { capture: true });
    window.addEventListener("message", onMessage);
    return () => {
      document.removeEventListener("click", onClick, { capture: true });
      window.removeEventListener("message", onMessage);
    };
  }, []);

  return <Analytics />;
}
