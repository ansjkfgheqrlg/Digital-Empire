"use client";
import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, Sparkles, Shield } from "lucide-react";
import { CountUp } from "../count-up";

export default function LandingHero() {
  return (
    <section className="bg-ink relative overflow-hidden pt-28 pb-20 md:pt-36 md:pb-28">
      {/* Base radial glow */}
      <div
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(120% 80% at 50% -10%, rgba(251,70,4,0.18) 0%, transparent 55%), radial-gradient(100% 60% at 80% 90%, rgba(255,138,74,0.10) 0%, transparent 55%)",
        }}
      />

      {/* Subtle grid overlay */}
      <div
        aria-hidden
        className="absolute inset-0 opacity-[0.06] pointer-events-none"
        style={{
          backgroundImage:
            "linear-gradient(rgba(251,70,4,0.4) 1px, transparent 1px), linear-gradient(90deg, rgba(251,70,4,0.4) 1px, transparent 1px)",
          backgroundSize: "64px 64px",
        }}
      />

      {/* Marquee border-b */}
      <div className="absolute top-0 inset-x-0 overflow-hidden border-b border-white/10 bg-black/40 backdrop-blur-sm z-20">
        <div className="marquee flex whitespace-nowrap py-2 text-[0.72rem] font-semibold tracking-widest uppercase text-white/60">
          {Array.from({ length: 12 }).flatMap((_, i) => [
            <span key={`a${i}`} className="px-6">Da AI User a System Architect</span>,
            <span key={`b${i}`} className="px-2 text-orange-pure">✦</span>,
            <span key={`c${i}`} className="px-6">Launch Mastery</span>,
            <span key={`d${i}`} className="px-2 text-orange-pure">✦</span>,
            <span key={`e${i}`} className="px-6">CRO Copy Mastery</span>,
            <span key={`f${i}`} className="px-2 text-orange-pure">✦</span>,
            <span key={`g${i}`} className="px-6">Digital Empire</span>,
            <span key={`h${i}`} className="px-2 text-orange-pure">✦</span>,
          ])}
        </div>
      </div>

      {/* Floating silver chips */}
      <div className="silver-chip float-a" style={{ top: "22%", left: "5%" }}>
        <span className="dot" />
        <span>Piattaforma <strong>Premium</strong></span>
      </div>
      <div className="silver-chip float-b" style={{ top: "18%", right: "6%" }}>
        <span className="dot" />
        <span><strong>9 Moduli</strong> · 32+ Lezioni</span>
      </div>
      <div className="silver-chip float-c" style={{ bottom: "24%", left: "7%" }}>
        <span className="dot" />
        <span>Accesso <strong>a vita</strong></span>
      </div>
      <div className="silver-chip float-d" style={{ bottom: "20%", right: "7%" }}>
        <span className="dot" />
        <span>Update <strong>inclusi</strong></span>
      </div>

      <div className="container-narrow relative z-10">
        {/* Eyebrow bubble */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
          className="flex justify-center mb-6"
        >
          <span className="bubble-orange">
            <Sparkles className="h-3.5 w-3.5" />
            La piattaforma ufficiale Digital Empire
          </span>
        </motion.div>

        {/* Pre-headline */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.05, ease: [0.22, 1, 0.36, 1] }}
          className="flex justify-center mb-7"
        >
          <span className="pre-headline">Formazione Empire presenta</span>
        </motion.div>

        {/* Headline */}
        <motion.h1
          initial={{ opacity: 0, y: 22 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.1, ease: [0.22, 1, 0.36, 1] }}
          className="text-center text-[clamp(2rem,4.8vw,3.75rem)] font-extrabold leading-[1.04] tracking-tight mb-7"
        >
          <span className="text-silver-white">La formazione per chi vuole </span>
          <span className="text-silver-orange">vincere davvero</span>
          <span className="text-silver-white"> nell&apos;era AI.</span>
        </motion.h1>

        {/* Subheadline */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.22, ease: [0.22, 1, 0.36, 1] }}
          className="max-w-3xl mx-auto mb-10 space-y-4"
          style={{ color: "rgba(249,249,249,0.78)" }}
        >
          <p className="text-base md:text-lg leading-[1.65] text-center">
            Niente corsi riciclati. Niente teoria <strong className="text-orange-pure">che invecchia in 3 mesi</strong>.
            Solo sistemi operativi costruiti da chi{" "}
            <span className="text-silver-orange font-semibold">vive il mercato ogni giorno</span>,
            testati sui clienti reali e rifiniti fino a produrre risultati misurabili.
          </p>
          <p className="text-base md:text-lg leading-[1.65] text-center">
            Ogni corso è un <span className="hl-block">sistema completo</span>:
            framework già pronti da applicare, video registrati in studio, descrizioni dense come veri articoli,
            risorse scaricabili per ogni lezione. <span className="text-silver-orange font-semibold">Nessuna scorciatoia.</span> Nessun filler.
            Solo quello che serve per eseguire.
          </p>
        </motion.div>

        {/* CTA row */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.38 }}
          className="flex flex-col sm:flex-row items-center justify-center gap-3 mb-4"
        >
          <Link href="#corsi" className="btn-orange btn-orange--lg group">
            Esplora i corsi
            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
          </Link>
          <Link href="/login" className="btn-ghost">
            Accedi alla piattaforma
          </Link>
        </motion.div>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.5 }}
          className="flex items-center justify-center gap-2 mb-14 text-xs"
          style={{ color: "rgba(249,249,249,0.5)" }}
        >
          <Shield className="h-3.5 w-3.5" />
          Nessuna carta al login · Rimborso entro 14 giorni
        </motion.div>

        {/* Stat row — silver cards */}
        <motion.div
          initial={{ opacity: 0, y: 14 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.55 }}
          className="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4 max-w-4xl mx-auto"
        >
          {[
            { value: 9, suffix: "", label: "Moduli CCM", sub: "Sistema completo" },
            { value: 32, suffix: "+", label: "Lezioni video", sub: "Studio production" },
            { value: 15, suffix: "+", label: "Skill riutilizzabili", sub: "Pronte da installare" },
            { value: null as number | null, label: "Accesso a vita", sub: "Update inclusi" },
          ].map((stat) => (
            <div key={stat.label} className="stat-card-silver">
              <div className="text-4xl md:text-5xl font-extrabold leading-none mb-2">
                <span
                  style={{
                    background: "linear-gradient(135deg, #3a3733 0%, #c9370a 50%, #fb4604 100%)",
                    WebkitBackgroundClip: "text",
                    backgroundClip: "text",
                    WebkitTextFillColor: "transparent",
                  }}
                >
                  {stat.value === null ? "∞" : <><CountUp to={stat.value} suffix={stat.suffix} /></>}
                </span>
              </div>
              <div className="text-[0.78rem] font-semibold uppercase tracking-widest" style={{ color: "#1c1c1c" }}>
                {stat.label}
              </div>
              <div className="text-[0.72rem] mt-1" style={{ color: "rgba(28,28,28,0.55)" }}>
                {stat.sub}
              </div>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
