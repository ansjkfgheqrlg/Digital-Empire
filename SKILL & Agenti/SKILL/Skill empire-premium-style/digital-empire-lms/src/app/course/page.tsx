"use client";

import React from "react";
import Link from "next/link";
import { 
  ArrowRight, 
  Play, 
  Sparkles, 
  Zap, 
  Target, 
  Layers, 
  Trophy,
  Rocket
} from "lucide-react";
import { Reveal } from "@/components/common/reveal";
import { courseContent } from "@/lib/course-content";
import { cn } from "@/lib/utils";

export default function CourseDashboard() {
  const lastLesson = {
    chapterSlug: "foundations",
    lessonSlug: "aesthetic-dna",
    title: "Decoding the Empire DNA"
  };

  return (
    <div className="space-y-16 pb-20">
      {/* Hero Dashboard */}
      <section className="relative overflow-hidden group">
        <div className="absolute top-0 right-0 p-12 opacity-5 pointer-events-none group-hover:scale-110 transition-transform duration-1000">
          <Rocket className="w-80 h-80 text-orange" />
        </div>
        
        <div className="relative z-10">
          <Reveal>
            <div className="bubble-orange mb-6">
              <Sparkles className="h-4 w-4" /> Welcome, Architect
            </div>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-[44px] md:text-[64px] font-bold tracking-tight mb-8">
              <span className="text-silver-white">Bentornato in</span>
              <br />
              <span className="text-silver-orange italic">Digital Empire Mastery.</span>
            </h1>
          </Reveal>
          
          <div className="flex flex-col md:flex-row gap-6 mt-12">
            {/* Quick Resume */}
            <Reveal delay={0.2}>
              <Link 
                href={`/course/${lastLesson.chapterSlug}/${lastLesson.lessonSlug}`}
                className="btn-orange group py-4 px-8"
              >
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                    <Play className="h-5 w-5 fill-white" />
                  </div>
                  <div className="text-left">
                    <p className="text-[10px] uppercase font-bold text-white/70 leading-none mb-1">Riprendi da</p>
                    <p className="text-sm font-bold text-white">{lastLesson.title}</p>
                  </div>
                </div>
              </Link>
            </Reveal>

            {/* Stats */}
            <Reveal delay={0.3}>
              <div className="flex items-center gap-6 px-8 py-3 rounded-2xl bg-white/5 border border-white/20">
                <div className="flex items-center gap-2">
                  <Zap className="h-5 w-5 text-orange" />
                  <div>
                    <p className="text-[10px] uppercase font-bold text-white/50">Progresso</p>
                    <p className="text-lg font-bold text-white">15%</p>
                  </div>
                </div>
                <div className="w-px h-8 bg-white/20" />
                <div className="flex items-center gap-2">
                  <Trophy className="h-5 w-5 text-orange" />
                  <div>
                    <p className="text-[10px] uppercase font-bold text-white/50">Chapter</p>
                    <p className="text-lg font-bold text-white">1 / 5</p>
                  </div>
                </div>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Chapter Grid */}
      <section className="space-y-10">
        <div className="flex items-center justify-between border-b border-white/5 pb-4">
          <h2 className="text-2xl font-bold flex items-center gap-3 italic">
            <Layers className="h-6 w-6 text-orange" /> Learning Architecture
          </h2>
          <span className="text-[10px] uppercase tracking-widest font-bold text-white/20">Unlocked Access</span>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          {courseContent.map((chapter, i) => {
            const isFirstChapter = i === 0;
            return (
              <Reveal key={chapter.id} delay={i * 0.08}>
                <div className={cn(
                  "card-silver-orange group relative overflow-hidden h-full flex flex-col",
                  i % 2 !== 0 && "variant-orange"
                )}>
                  {/* Visual Background Decoration */}
                  <div className="absolute top-0 right-0 p-8 opacity-0 group-hover:opacity-10 transition-opacity">
                    <h3 className="text-6xl font-black text-black">{chapter.id}</h3>
                  </div>

                  <div className="relative z-10 flex flex-col h-full">
                    <div className="flex items-center justify-between mb-6">
                       <span className="text-[10px] font-bold text-orange-deep uppercase tracking-[0.2em] eyebrow">Chapter 0{chapter.id}</span>
                       <div className="flex items-center gap-1.5 px-3 py-1 rounded-full bg-black/5 text-[10px] font-bold text-black/60 shadow-inner">
                         {chapter.lessons.length} Lezioni
                       </div>
                    </div>
                    
                    <h3 className="text-3xl font-black mb-4 text-black group-hover:text-orange transition-colors">{chapter.title.split(":")[1].trim()}</h3>
                    <p className="text-black/70 text-[15px] font-medium leading-relaxed mb-8 flex-1">{chapter.description}</p>
                    
                    <div className="pt-6 border-t border-black/10 mt-auto flex items-center justify-between">
                      <Link 
                        href={`/course/${chapter.slug}/${chapter.lessons[0].slug}`}
                        className="flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-black hover:text-orange transition-colors"
                      >
                        Inizia Capitolo <ArrowRight className="h-4 w-4" />
                      </Link>
                      
                      {isFirstChapter ? (
                        <div className="flex items-center gap-2">
                           <div className="w-2 h-2 rounded-full bg-orange animate-pulse" />
                           <span className="text-[10px] font-bold text-black/50 italic">Active</span>
                        </div>
                      ) : (
                        <Target className="h-4 w-4 text-black/20" />
                      )}
                    </div>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>
      </section>

      {/* Marquee Footer for Dashboard */}
      <footer className="pt-20">
        <div className="border-y border-white/5 py-10 overflow-hidden bg-ink-2/50">
          <div className="marquee flex gap-16 whitespace-nowrap text-[32px] md:text-[56px] font-black uppercase tracking-tighter text-white/5 opacity-50 italic">
            {Array.from({ length: 12 }).map((_, i) => (
              <span key={i}>Digital Empire Mastery ✦ The Architecture of Premium AI Platforms ✦ </span>
            ))}
          </div>
        </div>
      </footer>
    </div>
  );
}
