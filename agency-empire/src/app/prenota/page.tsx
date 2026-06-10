"use client";

import { useEffect, useState } from "react";
import { ArrowLeft, Phone, Shield, Clock, Star } from "lucide-react";

const CALENDLY_URL =
  "https://calendly.com/max-infoproducer/30min?hide_gdpr_banner=1&background_color=0a0a0a&text_color=f8f8f2&primary_color=edeebe";

export default function PrenotaPage() {
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://assets.calendly.com/assets/external/widget.js";
    script.async = true;
    script.onload = () => setLoaded(true);
    document.head.appendChild(script);
    return () => {
      if (document.head.contains(script)) document.head.removeChild(script);
    };
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0a] flex flex-col">
      {/* Ambient glows — z-index basso, NON fissi sui contenuti */}
      <div
        aria-hidden
        className="pointer-events-none fixed top-[10%] left-[15%] w-[600px] h-[400px]"
        style={{
          background: "radial-gradient(ellipse, rgba(6,33,85,0.30) 0%, transparent 70%)",
          zIndex: 1,
        }}
      />
      <div
        aria-hidden
        className="pointer-events-none fixed bottom-[5%] right-[10%] w-[400px] h-[400px]"
        style={{
          background: "radial-gradient(ellipse, rgba(58,107,192,0.18) 0%, transparent 70%)",
          zIndex: 1,
        }}
      />

      {/* NAV */}
      <nav className="relative flex items-center justify-between px-6 md:px-12 pt-6 pb-4" style={{ zIndex: 10 }}>
        <a
          href="/"
          className="flex items-center gap-2 text-sm group"
          style={{ color: "rgba(248,248,242,0.55)" }}
        >
          <ArrowLeft className="h-4 w-4 transition-transform group-hover:-translate-x-0.5" />
          <span className="group-hover:text-white transition-colors">Torna al sito</span>
        </a>

        <a href="/" aria-label="Digital Empire — Home" className="flex items-center gap-2.5">
          <span
            className="grid place-items-center rounded-lg w-9 h-9 font-display font-bold text-[0.95rem] tracking-[0.08em]"
            style={{
              color: "#edeebe",
              background: "linear-gradient(180deg, #1a4090 0%, #062155 100%)",
              boxShadow:
                "0 0 18px rgba(6,33,85,0.60), inset 0 1px 0 rgba(237,238,190,0.30), inset 0 -1px 0 rgba(0,0,20,0.35)",
            }}
          >
            DE
          </span>
          <div className="hidden sm:flex flex-col leading-none">
            <span
              className="font-display tracking-[0.18em] text-[0.78rem] font-bold"
              style={{ color: "#edeebe" }}
            >
              DIGITAL EMPIRE
            </span>
            <span
              className="text-[0.62rem] tracking-[0.20em] mt-0.5 uppercase"
              style={{ color: "rgba(237,238,190,0.40)" }}
            >
              Landing Page Studio
            </span>
          </div>
        </a>
      </nav>

      {/* MAIN */}
      <main
        className="relative flex-1 flex flex-col lg:flex-row gap-0 max-w-7xl mx-auto w-full px-4 md:px-8 pb-12 pt-4"
        style={{ zIndex: 5 }}
      >
        {/* LEFT — pitch */}
        <div className="lg:w-[380px] xl:w-[420px] shrink-0 flex flex-col justify-center py-8 lg:py-16 lg:pr-12">
          <div
            className="inline-flex items-center gap-2 rounded-full px-4 py-1.5 text-xs font-medium tracking-[0.12em] uppercase mb-8 self-start"
            style={{
              background: "linear-gradient(135deg, rgba(237,238,190,0.10) 0%, rgba(6,33,85,0.15) 100%)",
              border: "1px solid rgba(237,238,190,0.15)",
              color: "#edeebe",
            }}
          >
            <Phone className="h-3 w-3" />
            Strategy Call · 30 min · gratuita
          </div>

          <h1
            className="font-display font-bold leading-[1.1] mb-6"
            style={{ fontSize: "clamp(2rem, 4vw, 3rem)", color: "#f8f8f2" }}
          >
            Scegli il tuo{" "}
            <em
              className="font-accent not-italic"
              style={{
                fontStyle: "italic",
                background: "linear-gradient(135deg, #edeebe 0%, #3a6bc0 100%)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
              }}
            >
              momento.
            </em>
          </h1>

          <p className="text-base leading-relaxed mb-10" style={{ color: "rgba(248,248,242,0.55)" }}>
            30 minuti per capire dove il tuo funnel perde clienti e cosa fare
            concretamente per invertire la rotta. Nessuna vendita forzata.
          </p>

          <ul className="flex flex-col gap-4 mb-10">
            {[
              { icon: Clock, text: "30 minuti, solo business" },
              { icon: Star, text: "Audit CRO gratuito incluso" },
              { icon: Shield, text: "Nessun impegno, solo valore" },
            ].map(({ icon: Icon, text }) => (
              <li key={text} className="flex items-center gap-3">
                <span
                  className="grid place-items-center w-8 h-8 rounded-full shrink-0"
                  style={{
                    background: "linear-gradient(135deg, rgba(237,238,190,0.12) 0%, rgba(6,33,85,0.20) 100%)",
                    border: "1px solid rgba(237,238,190,0.18)",
                  }}
                >
                  <Icon className="h-3.5 w-3.5" style={{ color: "#edeebe" }} />
                </span>
                <span className="text-sm font-medium" style={{ color: "rgba(248,248,242,0.80)" }}>
                  {text}
                </span>
              </li>
            ))}
          </ul>

          <div
            className="rounded-2xl p-5"
            style={{
              background: "rgba(255,255,255,0.03)",
              border: "1px solid rgba(255,255,255,0.07)",
            }}
          >
            <div className="flex gap-0.5 mb-3">
              {[...Array(5)].map((_, i) => (
                <Star key={i} className="h-3.5 w-3.5" style={{ color: "#edeebe", fill: "#edeebe" }} />
              ))}
            </div>
            <p className="text-sm leading-relaxed italic mb-3" style={{ color: "rgba(248,248,242,0.60)" }}>
              &ldquo;In 30 minuti ho capito cosa non funzionava nella mia
              landing. Il team è stato preciso e senza perdere tempo.&rdquo;
            </p>
            <span className="text-xs font-medium tracking-wide" style={{ color: "rgba(237,238,190,0.45)" }}>
              — Cliente Digital Empire
            </span>
          </div>
        </div>

        {/* RIGHT — Calendly widget */}
        <div className="flex-1 flex flex-col">
          <div
            className="rounded-3xl relative"
            style={{
              background: "linear-gradient(180deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.02) 100%)",
              border: "1px solid rgba(255,255,255,0.09)",
              boxShadow: "0 40px 80px -32px rgba(0,0,0,0.65), inset 0 1px 0 rgba(255,255,255,0.05)",
            }}
          >
            {!loaded && (
              <div
                className="absolute inset-x-0 top-0 flex items-center justify-center"
                style={{ height: 900 }}
              >
                <div className="flex flex-col items-center gap-4" style={{ color: "rgba(248,248,242,0.35)" }}>
                  <div
                    className="w-8 h-8 rounded-full border-2 animate-spin"
                    style={{
                      borderColor: "rgba(237,238,190,0.25)",
                      borderTopColor: "rgba(237,238,190,0.70)",
                    }}
                  />
                  <span className="text-sm">Caricamento calendario…</span>
                </div>
              </div>
            )}
            <div
              className="calendly-inline-widget"
              data-url={CALENDLY_URL}
              style={{ width: "100%", height: 900, minWidth: 320 }}
            />
          </div>

          <p className="text-center text-xs mt-4" style={{ color: "rgba(248,248,242,0.25)" }}>
            Prenotazione sicura tramite Calendly · I tuoi dati restano riservati
          </p>
        </div>
      </main>
    </div>
  );
}
