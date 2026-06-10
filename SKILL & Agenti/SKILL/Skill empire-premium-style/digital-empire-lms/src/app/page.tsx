"use client";

import React from "react";
import Link from "next/link";
import { ArrowRight, Sparkles, ShieldCheck, Zap } from "lucide-react";
import { Reveal } from "@/components/common/reveal";

export default function Home() {
  return (
    <main className="min-h-screen bg-ink flex flex-col items-center justify-center p-6 text-center">
      <div className="max-w-3xl space-y-8">
        <Reveal>
          <div className="bubble-orange mb-4">
            <Sparkles className="h-4 w-4" /> Editorial Excellence
          </div>
        </Reveal>
        
        <Reveal delay={0.1}>
          <h1 className="text-[56px] md:text-[84px] font-black tracking-tighter leading-[0.95]">
            <span className="text-silver-white">Digital Empire</span>
            <br />
            <span className="text-silver-orange italic">Mastery.</span>
          </h1>
        </Reveal>

        <Reveal delay={0.2}>
          <p className="text-white/40 text-lg md:text-xl font-light leading-relaxed max-w-2xl mx-auto">
            L'architettura definitiva per costruire piattaforme AI premium. 
            Maestria tecnica, estetica editoriale e performance cinematografica.
          </p>
        </Reveal>

        <Reveal delay={0.3}>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-6 pt-8">
            <Link href="/course" className="btn-orange group py-4 px-10 text-lg">
              Entra nell'Empire <ArrowRight className="h-5 w-5 ml-2 transition-transform group-hover:translate-x-1" />
            </Link>
            <div className="flex items-center gap-2 text-white/30 text-xs font-bold uppercase tracking-widest">
              <ShieldCheck className="h-4 w-4" /> Student Access Only
            </div>
          </div>
        </Reveal>
      </div>

      {/* Decorative Floor */}
      <div className="fixed bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-orange/50 to-transparent opacity-20" />
    </main>
  );
}
