"use client";

import { BookOpen, Zap, Shield, Users, Play, Terminal, CheckCircle2, ArrowRight } from "lucide-react";
import { Reveal } from "@/components/reveal";

const STEPS = [
  {
    num: "01", title: "Verifica Database",
    desc: "Prima di avviare, assicurati che 'lead-freschi.csv' sia aggiornato. Il sistema caricherà automaticamente i record e li qualificherà con NVIDIA Nemotron.",
    icon: Users, accent: "#a78bfa",
  },
  {
    num: "02", title: "Controlla SMTP",
    desc: "Vai in SMTP Accounts e verifica che almeno un account sia Active (non Throttled). Se un account è throttled, il sistema devia il traffico sugli altri.",
    icon: Shield, accent: "#60a5fa",
  },
  {
    num: "03", title: "Lancia dalla Dashboard",
    desc: "Nella Dashboard, seleziona il Target Email (quante email vuoi inviare) poi premi il bottone del canale desiderato: Email, Instagram, LinkedIn, o Full Stack.",
    icon: Play, accent: "#fb4604",
  },
  {
    num: "04", title: "Monitora il Terminal",
    desc: "Il terminal Live Console mostra l'output in tempo reale. Viola = Email, Arancione = Instagram, Azzurro = LinkedIn, Verde = successi, Rosso = errori.",
    icon: Terminal, accent: "#4ade80",
  },
];

const RULES = [
  "Non avviare due processi in parallelo manualmente — usa la modalità 'Full Stack' o 'Email + Instagram'",
  "Il limite Gmail è 500 email/giorno per account — non superarlo o rischi il ban",
  "Instagram: max 15 DM al giorno per non essere bannato",
  "Qualificatore AI: filtra automaticamente i lead non pertinenti — non disabilitarlo",
  "I follow-up Instagram vengono mandati 2-3 giorni dopo il primo DM",
];

export default function GuidePage() {
  return (
    <div className="flex flex-col min-h-screen bg-ink">

      {/* Header */}
      <header className="h-14 border-b border-white/[0.08] flex items-center gap-3 px-8 bg-ink-2 sticky top-0 z-40 shrink-0">
        <BookOpen className="w-4 h-4 text-[#fb4604]" />
        <span className="text-sm font-black text-white uppercase tracking-widest">Guida Operativa</span>
      </header>

      <div className="max-w-3xl mx-auto px-8 py-10 space-y-10 w-full">

        {/* Title */}
        <Reveal>
          <div className="bubble-orange text-xs mb-5">
            <BookOpen className="w-3 h-3" /> Come Usare la Piattaforma
          </div>
          <h1 className="text-5xl font-black tracking-[-0.03em] leading-tight mb-4">
            <span className="text-silver-white">Guida al</span>
            <br />
            <span className="text-silver-orange">Control Center.</span>
          </h1>
          <p className="text-white/70 text-base leading-relaxed max-w-xl">
            Segui questi 4 passi ogni volta che vuoi avviare una sessione di outreach.
            La piattaforma gestisce tutto il resto in autonomia.
          </p>
        </Reveal>

        {/* Steps */}
        <div className="space-y-3">
          {STEPS.map((step, i) => {
            const Icon = step.icon;
            return (
              <Reveal key={step.num} delay={i * 0.08}>
                <div className="card-dark flex gap-5 items-start" style={{ padding: "1.5rem" }}>
                  <div className="w-11 h-11 rounded-2xl flex items-center justify-center shrink-0"
                    style={{ background: `${step.accent}20`, border: `1px solid ${step.accent}40` }}>
                    <Icon className="w-5 h-5" style={{ color: step.accent }} />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-[10px] font-black text-white/55 uppercase tracking-widest">Step {step.num}</span>
                    </div>
                    <h3 className="text-base font-black text-white mb-1.5">{step.title}</h3>
                    <p className="text-sm text-white/65 leading-relaxed">{step.desc}</p>
                  </div>
                  <ArrowRight className="w-4 h-4 text-white/25 shrink-0 mt-1" />
                </div>
              </Reveal>
            );
          })}
        </div>

        {/* Golden rules */}
        <Reveal delay={0.35}>
          <div className="card-dark" style={{ padding: "1.75rem" }}>
            <div className="flex items-center gap-2 mb-5">
              <Zap className="w-4 h-4 text-[#fb4604]" />
              <h2 className="text-base font-black text-white">Regole d'Oro — non ignorare</h2>
            </div>
            <div className="space-y-3">
              {RULES.map((rule, i) => (
                <div key={i} className="flex items-start gap-3">
                  <CheckCircle2 className="w-4 h-4 text-[#fb4604] shrink-0 mt-0.5" />
                  <p className="text-sm text-white/70 leading-relaxed">{rule}</p>
                </div>
              ))}
            </div>
          </div>
        </Reveal>

        {/* Color legend */}
        <Reveal delay={0.45}>
          <div className="card-dark" style={{ padding: "1.75rem" }}>
            <h2 className="text-base font-black text-white mb-4">Legenda Colori Terminal</h2>
            <div className="grid grid-cols-2 gap-3">
              {[
                { color: "#a78bfa", label: "Email / Writer / Qualifier" },
                { color: "#fb923c", label: "Instagram / DM / Follow-up" },
                { color: "#60a5fa", label: "LinkedIn / Commenti" },
                { color: "#22d3ee", label: "Scraper / Maps / Extractor" },
                { color: "#4ade80", label: "Successo / Completato / OK" },
                { color: "#f87171", label: "Errore / Exit / Fallimento" },
              ].map((c) => (
                <div key={c.label} className="flex items-center gap-3">
                  <div className="w-3 h-3 rounded-full shrink-0" style={{ background: c.color }} />
                  <span className="text-sm font-medium" style={{ color: c.color }}>{c.label}</span>
                </div>
              ))}
            </div>
          </div>
        </Reveal>

        <div className="text-center py-4 border-t border-white/[0.07]">
          <p className="text-[10px] font-black text-white/50 uppercase tracking-[0.4em]">
            Digital Empire · Outreach Engine v3.0
          </p>
        </div>
      </div>
    </div>
  );
}
