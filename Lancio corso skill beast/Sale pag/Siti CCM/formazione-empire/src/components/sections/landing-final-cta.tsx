"use client";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import Reveal from "../reveal";

export default function LandingFinalCta() {
  return (
    <section className="section section-border-t bg-ink-2 relative overflow-hidden">
      {/* Corner brackets */}
      <div className="corner-bracket corner-tl" />
      <div className="corner-bracket corner-tr" />
      <div className="corner-bracket corner-bl" />
      <div className="corner-bracket corner-br" />

      <div
        aria-hidden
        className="absolute inset-0 opacity-50 pointer-events-none"
        style={{
          backgroundImage:
            "radial-gradient(circle at 30% 20%, rgba(251,70,4,0.25) 0%, transparent 45%), radial-gradient(circle at 70% 80%, rgba(255,138,74,0.18) 0%, transparent 40%)",
        }}
      />
      <div className="container-narrow relative z-10 text-center">
        <Reveal>
          <span className="bubble-orange mb-6 inline-flex">Inizia oggi</span>
          <h2 className="text-3xl md:text-5xl lg:text-6xl font-extrabold tracking-tight leading-[1.05] mb-6">
            <span className="text-silver-white">Non aspettare il momento</span>
            <br />
            <span className="text-silver-orange">perfetto. Costruiscilo.</span>
          </h2>
          <p className="text-base md:text-lg max-w-2xl mx-auto leading-[1.65] mb-10" style={{ color: "rgba(249,249,249,0.72)" }}>
            Ogni giorno che passa senza questi sistemi è un giorno in cui{" "}
            <strong className="text-orange-pure">qualcun altro</strong> sta facendo i tuoi risultati al posto tuo.
            La curva dell&apos;AI non aspetta — <span className="text-silver-orange font-semibold">e nemmeno il mercato</span>.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
            <Link href="/signup" className="btn-orange btn-orange--lg group">
              Entra nella piattaforma
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </Link>
            <Link href="/login" className="btn-ghost">
              Ho già un account
            </Link>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
