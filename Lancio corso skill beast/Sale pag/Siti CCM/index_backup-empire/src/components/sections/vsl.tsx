"use client";

import { ArrowRight, Play, Shield } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";

const BOOKING_URL = "https://buy.stripe.com/aFafZj9bU0J25sj9MDdby00";
const VIDEO_ID = "Bl0p1at3ff4";

export function VSL() {
  return (
    <section
      className="section section-border-t relative overflow-hidden"
      style={{
        backgroundImage: "url('/vsl-bg.png')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
      }}
    >
      {/* Dark overlay per leggibilità */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{ background: "rgba(8,6,6,0.18)" }}
      />
      {/* Glow arancione centrale */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0"
        style={{
          background:
            "radial-gradient(ellipse 70% 50% at 50% 55%, rgba(251,70,4,0.07) 0%, transparent 70%)",
        }}
      />

      <div className="max-w-4xl mx-auto px-6 relative z-10">
        {/* Header */}
        <div className="text-center mb-10">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Play className="h-3.5 w-3.5 fill-white" /> Guarda prima di decidere
            </span>
          </Reveal>

          <Reveal delay={0.12}>
            <p
              className="text-[11px] font-black uppercase tracking-[0.28em] text-white/70 mt-7 mb-4"
              style={{ textShadow: "0 1px 8px rgba(0,0,0,0.9)" }}
            >
              Digital Empire · VSL
            </p>
          </Reveal>

          <Reveal delay={0.18}>
            <h2 className="text-[20px] md:text-[38px] font-extrabold leading-[1.5] tracking-tight">
              <span
                style={{
                  background: "linear-gradient(135deg, #fb4604 0%, #d93d00 50%, #ff6a2e 100%)",
                  color: "#ffffff",
                  padding: "0.12em 0.45em",
                  boxDecorationBreak: "clone",
                  WebkitBoxDecorationBreak: "clone",
                  boxShadow:
                    "0 0 60px rgba(251,70,4,0.55), 0 4px 24px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.22), inset 0 -1px 0 rgba(0,0,0,0.2)",
                  textShadow: "0 1px 3px rgba(0,0,0,0.5)",
                  letterSpacing: "-0.02em",
                }}
              >
                Tutto quello che devi sapere prima di entrare.
              </span>
            </h2>
          </Reveal>
        </div>

        {/* Video frame */}
        <Reveal delay={0.25}>
          <div
            className="relative rounded-2xl overflow-hidden"
            style={{
              border: "1px solid rgba(251,70,4,0.28)",
              boxShadow:
                "0 0 0 1px rgba(255,255,255,0.04) inset, 0 40px 100px -40px rgba(0,0,0,0.95), 0 0 70px -15px rgba(251,70,4,0.18)",
            }}
          >
            {/* Top bar decorativo stile player */}
            <div
              className="flex items-center gap-2 px-4 py-2.5"
              style={{
                background:
                  "linear-gradient(90deg, #111111 0%, #1a1a1a 100%)",
                borderBottom: "1px solid rgba(251,70,4,0.2)",
              }}
            >
              <span className="h-2.5 w-2.5 rounded-full bg-orange-500 opacity-80" />
              <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
              <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
              <span className="ml-auto text-[10px] font-bold uppercase tracking-[0.22em] text-white/25 hidden sm:block">
                Claude Code Mastery · VSL
              </span>
            </div>

            {/* 16:9 YouTube embed */}
            <div className="aspect-video w-full bg-black">
              <iframe
                src={`https://www.youtube-nocookie.com/embed/${VIDEO_ID}?rel=0&modestbranding=1&color=white`}
                title="Claude Code Mastery — Video di Presentazione"
                className="w-full h-full"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowFullScreen
                referrerPolicy="strict-origin-when-cross-origin"
              />
            </div>
          </div>
        </Reveal>

        {/* CTA sotto il video */}
        <Reveal delay={0.35}>
          <div className="flex flex-col items-center gap-5 mt-12">
            <div className="flex flex-col sm:flex-row gap-3 items-center justify-center w-full sm:w-auto">
              <a
                href={BOOKING_URL}
                className="btn-orange group w-full sm:w-auto justify-center"
                style={{ padding: "1.1rem 2.5rem", fontSize: "1.05rem", fontWeight: 700 }}
              >
                Inizia il Percorso per €397
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
              </a>
              <CallCTA variant="dark" className="!bg-black/60 !border-white/40 backdrop-blur-md w-full sm:w-auto justify-center" />
            </div>
            <div
              className="flex items-center gap-2 text-xs uppercase tracking-widest text-white/80"
              style={{ textShadow: "0 1px 6px rgba(0,0,0,0.9)" }}
            >
              <Shield className="h-3.5 w-3.5" /> Garanzia &ldquo;Builder o Rimborsato&rdquo; · 30 giorni
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
