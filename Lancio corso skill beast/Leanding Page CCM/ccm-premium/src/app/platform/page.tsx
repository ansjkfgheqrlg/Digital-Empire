"use client";

import React from "react";
import Link from "next/link";
import { 
  Play, 
  BookOpen, 
  ArrowRight, 
  Clock, 
  Trophy, 
  Sparkles,
  Zap,
  Target,
  Rocket
} from "lucide-react";
import { courseData } from "@/lib/course-data";
import { Reveal } from "@/components/reveal";

export default function PlatformDashboard() {
  const lastLesson = {
    moduleId: "0",
    moduleTitle: "SETUP — SISTEMA OPERATIVO AI",
    lessonTitle: "Installazione Guidata Step-by-Step",
    lessonSlug: "installazione-guidata"
  };

  return (
    <div className="space-y-12 pb-20">
      {/* Welcome Hero */}
      <section className="relative rounded-3xl overflow-hidden bg-ink p-8 md:p-12 border border-white/10 shadow-2xl">
        <div className="absolute top-0 right-0 p-8 opacity-10 pointer-events-none">
          <Rocket className="w-64 h-64 text-orange-pure" />
        </div>
        
        <div className="relative z-10 max-w-2xl">
          <Reveal>
            <span className="bubble-orange mb-4">
              <Sparkles className="h-3.5 w-3.5" /> Studente Pro
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-3xl md:text-4xl font-bold mb-4">
              Bentornato in <span className="text-orange-pure">Claude Code Mastery.</span>
            </h1>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/60 text-lg mb-8 leading-relaxed">
              Hai completato il <strong className="text-white">12%</strong> del percorso. 
              Ricorda: la maestria si ottiene costruendo, non solo guardando. 
              Qual è il prossimo sistema che lancerai?
            </p>
          </Reveal>
          
          <Reveal delay={0.3}>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link 
                href={`/platform/course/${lastLesson.moduleId}/${lastLesson.lessonSlug}`}
                className="btn-orange group bg-[#fb4604] hover:bg-[#fb4604]/90"
              >
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center">
                    <Play className="h-4 w-4 fill-white" />
                  </div>
                  <div className="text-left">
                    <div className="text-[10px] uppercase font-bold text-white/60 leading-none mb-1">Riprendi da</div>
                    <div className="text-sm font-bold truncate max-w-[150px]">{lastLesson.lessonTitle}</div>
                  </div>
                </div>
              </Link>
              
              <div className="flex items-center gap-4 px-6 py-3 rounded-xl bg-white/5 border border-white/10">
                <Trophy className="h-5 w-5 text-orange-pure" />
                <div>
                  <div className="text-[10px] uppercase font-bold text-white/40">Prossimo Obiettivo</div>
                  <div className="text-sm font-bold">Modulo 0 Completato</div>
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* Stats Grid */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {[
          { icon: Clock, label: "Tempo speso", val: "4h 20m" },
          { icon: BookOpen, label: "Lezioni viste", val: "3 / 21" },
          { icon: Zap, label: "Skill buildate", val: "2" },
          { icon: Target, label: "Moduli finiti", val: "0" },
        ].map((s, i) => {
          const Icon = s.icon;
          return (
            <Reveal key={i} delay={i * 0.05}>
              <div className="bg-[#111111] border border-white/5 p-5 rounded-2xl">
                <Icon className="h-5 w-5 text-orange-pure mb-3" />
                <div className="text-[10px] uppercase tracking-widest text-white/30 font-bold">{s.label}</div>
                <div className="text-xl font-bold mt-1">{s.val}</div>
              </div>
            </Reveal>
          );
        })}
      </section>

      {/* Modules Roadmap */}
      <section className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-2xl font-bold">La Tua Roadmap</h2>
          <span className="text-xs text-white/40">Tutti i moduli sbloccati</span>
        </div>
        
        <div className="space-y-4">
          {courseData.map((module, i) => (
            <Reveal key={module.id} delay={i * 0.08}>
              <div className="group relative overflow-hidden bg-[#111111] hover:bg-[#161616] border border-white/5 hover:border-orange-pure/30 transition-all rounded-2xl p-6">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
                  <div className="flex items-start gap-6">
                    <div className="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center font-bold text-lg text-white/20 group-hover:text-orange-pure transition-colors">
                      {module.id}
                    </div>
                    <div>
                      <h3 className="text-lg font-bold mb-1 group-hover:text-white transition-colors">{module.title}</h3>
                      <p className="text-white/40 text-sm max-w-xl line-clamp-1">{module.description}</p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-6">
                    <div className="text-right hidden sm:block">
                      <div className="text-[10px] uppercase tracking-widest font-bold text-white/30">{module.lessons.length} Lezioni</div>
                      <div className="text-xs font-medium text-white/60">~ {module.id === "0" ? "40 min" : "60 min"} totali</div>
                    </div>
                    <Link 
                      href={`/platform/course/${module.id}/${module.lessons[0].slug}`}
                      className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center hover:bg-orange-pure hover:border-orange-pure transition-all group/btn"
                    >
                      <ArrowRight className="h-4 w-4 text-white group-hover/btn:translate-x-0.5 transition-transform" />
                    </Link>
                  </div>
                </div>
                
                {/* Progress bar subtle */}
                <div className="absolute bottom-0 left-0 h-[2px] bg-white/5 w-full">
                  <div className="h-full bg-orange-pure/50" style={{ width: i === 0 ? "35%" : "0%" }} />
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
