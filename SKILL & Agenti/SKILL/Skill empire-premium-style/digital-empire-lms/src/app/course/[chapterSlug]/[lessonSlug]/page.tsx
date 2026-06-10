"use client";

import React, { useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { 
  ChevronLeft, 
  ChevronRight, 
  FileText, 
  CheckCircle, 
  Download, 
  Sparkles,
  ArrowRight,
  BookOpen,
  Zap,
  ShieldCheck
} from "lucide-react";
import { Reveal } from "@/components/common/reveal";
import { VideoPlayer } from "@/components/lms/VideoPlayer";
import { ResourceCard } from "@/components/lms/ResourceCard";
import { courseContent } from "@/lib/course-content";
import { cn } from "@/lib/utils";

export default function LessonPage() {
  const params = useParams();
  const router = useRouter();
  const chapterSlug = params.chapterSlug as string;
  const lessonSlug = params.lessonSlug as string;

  const currentChapter = courseContent.find((c) => c.slug === chapterSlug);
  const currentLessonIndex = currentChapter?.lessons.findIndex((l) => l.slug === lessonSlug) ?? -1;
  const currentLesson = currentChapter?.lessons[currentLessonIndex];

  const [activeTab, setActiveTab] = useState<"content" | "resources" | "exercise">("content");

  if (!currentChapter || !currentLesson) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[50vh] text-center">
        <h2 className="text-xl font-bold text-white/50 mb-4">Lezione non trovata</h2>
        <button 
          onClick={() => router.push("/course")}
          className="text-orange font-bold uppercase tracking-widest text-xs hover:underline"
        >
          Torna alla Dashboard
        </button>
      </div>
    );
  }

  // Navigation logic
  const prevLesson = currentLessonIndex > 0 ? currentChapter.lessons[currentLessonIndex - 1] : null;
  const nextLesson = currentLessonIndex < currentChapter.lessons.length - 1 ? currentChapter.lessons[currentLessonIndex + 1] : null;

  return (
    <div className="space-y-12 pb-24">
      {/* Breadcrumb / Lesson Header */}
      <section className="space-y-6">
        <div className="flex items-center gap-4 text-[10px] font-bold uppercase tracking-[0.3em]">
          <span className="text-white/30">{currentChapter.title}</span>
          <ChevronRight className="h-3 w-3 text-white/10" />
          <span className="text-orange">{currentLesson.title}</span>
        </div>
        
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <Reveal>
            <h1 className="text-3xl md:text-4xl font-bold max-w-2xl">{currentLesson.title}</h1>
          </Reveal>
          <div className="flex items-center gap-4">
             <button className="flex items-center gap-2 px-6 py-2 rounded-full border border-green-500/20 bg-green-500/5 text-green-500 text-[10px] font-bold uppercase tracking-widest hover:bg-green-500/10 transition-all">
                <CheckCircle className="h-3.5 w-3.5" /> Completata
             </button>
          </div>
        </div>
      </section>

      {/* Video Player Section */}
      <section>
        <VideoPlayer title={currentLesson.title} />
      </section>

      {/* Content Area Split */}
      <section className="grid lg:grid-cols-3 gap-12 mt-12">
        <div className="lg:col-span-2 space-y-10">
          {/* Tabs */}
          <div className="flex gap-10 border-b border-white/5">
            {[
              { id: "content", label: "Note Lezione", icon: FileText },
              { id: "resources", label: "Risorse & Download", icon: Download },
              { id: "exercise", label: "Esercitazione Pratica", icon: Zap },
            ].map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as any)}
                  className={cn(
                    "flex items-center gap-2 pb-4 text-[11px] font-bold uppercase tracking-widest transition-all relative",
                    activeTab === tab.id ? "text-orange" : "text-white/30 hover:text-white/60"
                  )}
                >
                  <Icon className="h-3.5 w-3.5" />
                  {tab.label}
                  {activeTab === tab.id && (
                    <div className="absolute bottom-0 left-0 right-0 h-1 bg-orange shadow-[0_0_15px_rgba(251,70,4,0.6)]" />
                  )}
                </button>
              );
            })}
          </div>

          <div className="min-h-[300px] animate-in fade-in duration-500">
            {activeTab === "content" && (
              <div className="prose prose-invert max-w-none space-y-6">
                <p className="text-white/70 text-lg leading-relaxed">
                  In questa lezione focalizzeremo l'attenzione sui principi strutturali che rendono un'interfaccia non solo "bella", ma capace di trasmettere lusso e autorità istantanea.
                </p>
                <div className="bg-white/5 border-l-4 border-orange p-8 rounded-r-2xl space-y-4">
                  <h4 className="text-orange font-bold flex items-center gap-2 uppercase tracking-widest text-xs">
                    <Sparkles className="h-4 w-4" /> Empire Key Concept
                  </h4>
                  <p className="text-sm italic text-white/90">
                    "La percezione del Premium non deriva dall'abbondanza, ma dal controllo chirurgico di ogni singolo pixel. Il raggio degli angoli, la densità della grana, il ritardo di un millisecondo in un'animazione: qui si gioca la partita."
                  </p>
                </div>
                <div className="space-y-4 pt-4">
                   <h4 className="font-bold text-xl">Cosa abbiamo analizzato:</h4>
                   <ul className="space-y-4 text-white/50 text-[15px]">
                      <li className="flex gap-4 items-start">
                        <div className="w-1.5 h-1.5 rounded-full bg-orange mt-2 shrink-0" />
                        <span>Mappatura del DNA visivo del design system.</span>
                      </li>
                      <li className="flex gap-4 items-start">
                        <div className="w-1.5 h-1.5 rounded-full bg-orange mt-2 shrink-0" />
                        <span>Integrazione di Lenis per il controllo cinematico dello scrolling.</span>
                      </li>
                      <li className="flex gap-4 items-start">
                        <div className="w-1.5 h-1.5 rounded-full bg-orange mt-2 shrink-0" />
                        <span>Orchestrazione dei layer di Framer Motion per rivelazioni coerenti.</span>
                      </li>
                   </ul>
                </div>
              </div>
            )}

            {activeTab === "resources" && (
              <div className="grid sm:grid-cols-2 gap-4">
                <ResourceCard 
                  title="Empire Foundation Playbook" 
                  type="PDF Manual" 
                  size="12.4 MB" 
                  variant="silver"
                />
                <ResourceCard 
                  title="Next.js Luxury Scaffold" 
                  type="Github Repo" 
                  size="Access Private" 
                  variant="orange"
                />
                <ResourceCard 
                  title="Onest Variable Font Kit" 
                  type="Asset Pack" 
                  size="4.2 MB" 
                  variant="silver"
                />
              </div>
            )}

            {activeTab === "exercise" && (
              <div className="space-y-8">
                <div className="bg-ink-2 p-8 rounded-3xl border border-white/5">
                   <h3 className="text-xl font-bold mb-4">La Tua Sfida</h3>
                   <p className="text-white/60 mb-6">Implementa una sezione "Hero" utilizzando esclusivamente i token silver-orange definiti nel Chapter 1. Assicurati che ogni elemento rispetti la gerarchia visuale I.C.R.O.</p>
                   <div className="space-y-1">
                      {[
                        "Setup del repository con Tailwind v4",
                        "Integrazione del font Onest con feature settings ss01",
                        "Creazione del layer di Grana Fine (.grain-fine)",
                        "Implementazione del Reveal sull'headline",
                      ].map((step, i) => (
                        <div key={i} className="flex items-center gap-4 py-3 border-b border-white/5 last:border-0 group cursor-pointer">
                           <div className="w-5 h-5 rounded border border-white/10 flex items-center justify-center group-hover:border-orange transition-colors">
                             <div className="w-2 h-2 rounded-full bg-orange opacity-0 group-hover:opacity-100 transition-opacity" />
                           </div>
                           <span className="text-sm text-white/50 group-hover:text-white transition-colors">{step}</span>
                        </div>
                      ))}
                   </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Sidebar Mini-Nav / Support */}
        <div className="space-y-8">
          <div className="bg-[#111111] rounded-3xl p-8 border border-white/5 space-y-6">
            <h4 className="font-bold flex items-center gap-2 italic uppercase tracking-widest text-[11px]">
              <Zap className="h-4 w-4 text-orange" /> Next Protocol
            </h4>
            {nextLesson ? (
              <div className="space-y-4">
                <p className="text-xs text-white/40 leading-relaxed">Il prossimo step ci porterà a scoprire il controllo avanzato della tipografia variabile.</p>
                <button 
                  onClick={() => router.push(`/course/${chapterSlug}/${nextLesson.slug}`)}
                  className="w-full btn-orange justify-center text-xs py-4"
                >
                  Prossima Lezione <ChevronRight className="h-4 w-4" />
                </button>
              </div>
            ) : (
              <p className="text-xs text-white/20 italic">Fine del capitolo corrente.</p>
            )}
            
            <div className="pt-6 border-t border-white/5">
               <button className="flex items-center gap-2 text-[10px] font-bold text-white/30 uppercase tracking-[0.2em] hover:text-white transition-colors">
                  <BookOpen className="h-3.5 w-3.5" /> Torna all'indice
               </button>
            </div>
          </div>

          <div className="p-8 rounded-3xl border border-orange/20 bg-orange/5 space-y-4">
             <div className="flex items-center justify-between">
                <h4 className="font-bold text-xs uppercase tracking-widest text-orange">Certified Status</h4>
                <ShieldCheck className="h-5 w-5 text-orange" />
             </div>
             <p className="text-[11px] text-white/50 leading-relaxed">Questo capitolo sblocca il badge "Architect Foundational". Completa gli esercizi per validare la tua competenza.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
