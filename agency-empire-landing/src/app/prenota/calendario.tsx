"use client";

import { useEffect, useState } from "react";
import { CALENDLY } from "@/lib/contatti";

/* Calendly inline, caricato ON DEMAND (C2.1): al primo gesto del visitatore (scroll, tocco, mouse, tasto)
   oppure dopo 2,5 s — così il primo render è nostro e il widget non pesa sull'LCP.
   L'evento `calendly.event_scheduled` lo legge analytics.tsx (call_prenotata, con `?da=`). */
export function Calendario() {
  const [attivo, setAttivo] = useState(false);
  const [pronto, setPronto] = useState(false);

  useEffect(() => {
    const accendi = () => setAttivo(true);
    const eventi = ["pointermove", "scroll", "touchstart", "keydown"] as const;
    eventi.forEach((e) => window.addEventListener(e, accendi, { once: true, passive: true }));
    const t = window.setTimeout(accendi, 2500);
    return () => {
      eventi.forEach((e) => window.removeEventListener(e, accendi));
      window.clearTimeout(t);
    };
  }, []);

  useEffect(() => {
    if (!attivo) return;
    const script = document.createElement("script");
    script.src = "https://assets.calendly.com/assets/external/widget.js";
    script.async = true;
    script.onload = () => setPronto(true);
    document.head.appendChild(script);
    return () => {
      if (document.head.contains(script)) document.head.removeChild(script);
    };
  }, [attivo]);

  return (
    <div className="sv-card relative" style={{ padding: 0, minHeight: 720 }} aria-live="polite">
      {!pronto && (
        <div className="absolute inset-0 grid place-items-center">
          <p className="sv-small sv-muted">Caricamento del calendario…</p>
        </div>
      )}
      {attivo && <div className="calendly-inline-widget" data-url={CALENDLY} style={{ width: "100%", height: 720, minWidth: 320 }} />}
    </div>
  );
}
