"use client";

import { ArrowRight, Shield, Sparkles } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";
import { cn } from "@/lib/utils";

const BOOKING_URL = "https://buy.stripe.com/aFafZj9bU0J25sj9MDdby00";

function CTA({ 
  large = false, 
  label = "Inizia il Percorso per €397" 
}: { large?: boolean; label?: string }) {
  return (
    <a href={BOOKING_URL} className={cn("btn-orange group", large && "btn-orange--lg")}>
      {label}
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}

export function Hero() {
  return (
    <section className="bg-ink relative overflow-hidden section-border-t">
      {/* Marquee */}
      <div
        className="overflow-hidden py-3 relative"
        style={{
          background: "linear-gradient(90deg, #d9d4d0 0%, #f4f1ee 18%, #ffffff 35%, #ffd9c2 55%, #fb4604 75%, #f4f1ee 92%, #d9d4d0 100%)",
          borderTop: "1px solid rgba(255,255,255,0.7)",
          borderBottom: "1px solid rgba(251,70,4,0.35)",
          boxShadow: "inset 0 1px 0 rgba(255,255,255,0.9), 0 6px 24px -12px rgba(251,70,4,0.5)",
        }}
      >
        <div className="marquee flex gap-10 whitespace-nowrap text-[11px] uppercase tracking-[0.28em] font-extrabold text-[#0a0a0a]" style={{ width: "max-content", textShadow: "0 1px 0 rgba(255,255,255,0.6)" }}>
          {Array.from({ length: 8 }).map((_, i) => (
            <span key={i} className="flex items-center gap-10">
              <span>Claude Code Mastery</span>
              <span className="text-[#fb4604]">✦</span>
              <span>Tech-Lux Edition</span>
              <span className="text-[#fb4604]">✦</span>
              <span>Ecosistema Claude · Code · Projects · Cowork</span>
              <span className="text-[#fb4604]">✦</span>
              <span>by Digital Empire</span>
              <span className="text-[#fb4604]">✦</span>
            </span>
          ))}
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-6 py-24 md:py-32 text-center relative">
        {/* Silver Chips */}
        <span className="silver-chip float-a hidden md:inline-flex" style={{ top: "10%", left: "-2%" }}>
          <span className="dot" /> <strong>9 Moduli</strong> · 6 core + 3 avanzati
        </span>
        <span className="silver-chip float-b hidden md:inline-flex" style={{ top: "20%", right: "-4%" }}>
          <span className="dot" /> Zero <strong>righe di codice</strong>
        </span>
        <span className="silver-chip float-c hidden md:inline-flex" style={{ bottom: "15%", left: "-3%" }}>
          <span className="dot" /> <strong>30 giorni</strong> garanzia
        </span>
        <span className="silver-chip float-d hidden md:inline-flex" style={{ bottom: "10%", right: "-2%" }}>
          <span className="dot" /> <strong>Ricerca di mercato</strong> inclusa
        </span>

        <Reveal>
          <span className="bubble-orange mb-8">
            <Sparkles className="h-3.5 w-3.5" /> Il primo percorso italiano sull'ecosistema Claude
          </span>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="pre-headline mb-6">Digital Empire presenta · Mastery 2026</div>
        </Reveal>

        <Reveal delay={0.2}>
          <h1 className="text-[44px] md:text-[72px] font-extrabold leading-[1.05] tracking-tight mb-8">
            <span className="text-silver-white">Da AI User a</span>
            <br />
            <span className="text-silver-orange">System Architect.</span>
          </h1>
        </Reveal>

        <Reveal delay={0.3}>
          <p className="text-lg md:text-xl text-white/70 max-w-3xl mx-auto mb-10 leading-relaxed">
            Per chi è stanco di &quot;chattare&quot; con l&apos;AI sperando nel colpo di fortuna e vuole iniziare a <strong className="text-silver-orange font-semibold">orchestrare Agenti, Skill e System Prompt</strong> nell&apos;intero ecosistema Claude — Code, Projects, Cowork, Perplexity, Manus. In 6 settimane costruisci System AI deterministici, li vendi a €500–€2.000 a progetto e impari <strong className="text-silver-orange font-semibold">a leggere il mercato prima di costruire</strong>. Zero righe da scrivere: <span className="hl-block">l&apos;AI esegue, tu dirigi l&apos;impero</span>.
          </p>
        </Reveal>

        <Reveal delay={0.4}>
          <div className="flex flex-col gap-5 items-center">
            <div className="flex flex-col sm:flex-row gap-3 items-center justify-center">
              <CTA large />
              <CallCTA variant="dark" />
            </div>
            <div className="flex items-center gap-4 text-xs uppercase tracking-widest text-white/40">
              <span className="flex items-center gap-1.5"><Shield className="h-3.5 w-3.5" /> Garanzia &quot;Builder o Rimborsato&quot; · 30 giorni</span>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
