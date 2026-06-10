"use client";

import React, { useState } from "react";
import { useParams, useRouter } from "next/navigation";
import {
  Play,
  ChevronLeft,
  ChevronRight,
  FileText,
  Download,
  CheckCircle,
  MessageSquare,
  Video,
  ExternalLink,
  Sparkles,
} from "lucide-react";
import { courseData } from "@/lib/course-data";

export function LessonClient() {
  const params = useParams();
  const router = useRouter();
  const moduleId = params.moduleId as string;
  const lessonSlug = params.lessonSlug as string;

  const currentModule = courseData.find((m) => m.id === moduleId);
  const currentLessonIndex = currentModule?.lessons.findIndex((l) => l.slug === lessonSlug) ?? -1;
  const currentLesson = currentModule?.lessons[currentLessonIndex];

  const [activeTab, setActiveTab] = useState<"notes" | "resources" | "checklist">("notes");

  if (!currentModule || !currentLesson) {
    return (
      <div className="flex flex-col items-center justify-center h-[60vh] text-white/50">
        <p>Lezione non trovata.</p>
        <button onClick={() => router.push("/platform")} className="mt-4 text-orange-pure hover:underline">
          Torna alla dashboard
        </button>
      </div>
    );
  }

  const prevLesson = currentLessonIndex > 0 ? currentModule.lessons[currentLessonIndex - 1] : null;
  const nextLesson = currentLessonIndex < currentModule.lessons.length - 1 ? currentModule.lessons[currentLessonIndex + 1] : null;

  return (
    <div className="pb-20">
      <div className="flex items-center gap-4 mb-6 text-xs font-bold uppercase tracking-widest">
        <span className="text-white/30">{currentModule.title}</span>
        <ChevronRight className="h-3 w-3 text-white/10" />
        <span className="text-orange-pure">{currentLesson.title}</span>
      </div>

      <section className="space-y-6">
        <h1 className="text-2xl md:text-3xl font-bold">{currentLesson.title}</h1>

        <div className="aspect-video bg-ink rounded-3xl border border-white/10 overflow-hidden relative group shadow-2xl">
          <div className="absolute inset-0 flex items-center justify-center bg-black/40 group-hover:bg-black/20 transition-all cursor-pointer">
            <div className="w-20 h-20 rounded-full bg-orange-pure flex items-center justify-center shadow-2xl shadow-orange-pure/40 group-hover:scale-110 transition-transform">
              <Play className="h-8 w-8 text-white fill-white ml-1" />
            </div>
          </div>
          <div className="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/80 to-transparent">
            <div className="flex items-center gap-3 text-sm font-medium">
              <Video className="h-4 w-4 text-orange-pure" />
              <span>DURATA: {currentLesson.duration}</span>
            </div>
          </div>
        </div>

        <div className="flex justify-between items-center py-4 border-b border-white/10">
          <div>
            {prevLesson && (
              <button
                onClick={() => router.push(`/platform/course/${moduleId}/${prevLesson.slug}`)}
                className="flex items-center gap-2 text-white/50 hover:text-white transition-colors text-sm font-medium"
              >
                <ChevronLeft className="h-4 w-4" /> Precedente
              </button>
            )}
          </div>
          <div className="flex items-center gap-4">
            <button className="flex items-center gap-2 px-6 py-2 rounded-full bg-white/5 border border-white/10 hover:bg-white/10 transition-all text-sm font-bold">
              <CheckCircle className="h-4 w-4 text-green-500" /> Segna come completata
            </button>
            {nextLesson && (
              <button
                onClick={() => router.push(`/platform/course/${moduleId}/${nextLesson.slug}`)}
                className="flex items-center gap-2 bg-orange-pure px-6 py-2 rounded-full text-sm font-bold hover:bg-orange-pure/90 transition-all"
              >
                Prossima <ChevronRight className="h-4 w-4" />
              </button>
            )}
          </div>
        </div>
      </section>

      <section className="mt-12 grid lg:grid-cols-3 gap-10">
        <div className="lg:col-span-2 space-y-8">
          <div className="flex gap-8 border-b border-white/5">
            {[
              { id: "notes", label: "Contenuto", icon: FileText },
              { id: "resources", label: "Risorse & Template", icon: Download },
              { id: "checklist", label: "Checklist", icon: CheckCircle },
            ].map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as "notes" | "resources" | "checklist")}
                  className={`flex items-center gap-2 pb-4 text-sm font-bold tracking-tight transition-all relative ${
                    activeTab === tab.id ? "text-orange-pure" : "text-white/30 hover:text-white/60"
                  }`}
                >
                  <Icon className="h-4 w-4" />
                  {tab.label}
                  {activeTab === tab.id && (
                    <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-orange-pure shadow-[0_0_10px_rgba(251,70,4,0.5)]" />
                  )}
                </button>
              );
            })}
          </div>

          <div className="min-h-[300px] animate-in fade-in slide-in-from-bottom-2 duration-500">
            {activeTab === "notes" && (
              <div className="prose prose-invert max-w-none">
                <h3 className="text-xl font-bold mb-4">Cosa imparerai in questa lezione</h3>
                <p className="text-white/70 leading-relaxed mb-6">
                  {currentModule.description} In questa specifica sessione ci concentreremo su come massimizzare l'efficacia di Claude Code applicando i principi del framework proprietario Digital Empire.
                </p>
                <div className="bg-white/5 border-l-4 border-orange-pure p-6 rounded-r-2xl mb-8">
                  <h4 className="text-orange-pure font-bold mb-2 flex items-center gap-2">
                    <Sparkles className="h-4 w-4" /> Insight del Builder
                  </h4>
                  <p className="text-sm italic text-white/80">
                    "Il segreto non è scrivere più prompt, ma dare al modello una struttura identitaria forte. Claude Code non è un chatbot, è un'estensione della tua intelligenza operativa."
                  </p>
                </div>
                <ul className="space-y-4 text-white/70">
                  <li className="flex gap-3">
                    <div className="w-1.5 h-1.5 rounded-full bg-orange-pure mt-2 shrink-0" />
                    <span>Comprensione profonda dell'architettura sottostante.</span>
                  </li>
                  <li className="flex gap-3">
                    <div className="w-1.5 h-1.5 rounded-full bg-orange-pure mt-2 shrink-0" />
                    <span>Eliminazione degli errori comuni di configurazione.</span>
                  </li>
                  <li className="flex gap-3">
                    <div className="w-1.5 h-1.5 rounded-full bg-orange-pure mt-2 shrink-0" />
                    <span>Esercitazione guidata per produrre il tuo primo asset.</span>
                  </li>
                </ul>
              </div>
            )}

            {activeTab === "resources" && (
              <div className="space-y-4">
                <h3 className="text-xl font-bold mb-6">Documenti e Risorse Scaricabili</h3>
                {[
                  { name: "Framework I.C.R.O. - Template Master", format: "PDF", size: "2.4 MB" },
                  { name: "Esempio CLAUDE.md Real Case", format: "Markdown", size: "45 KB" },
                  { name: "Cheat Sheet Comandi Avanzati", format: "PNG", size: "1.2 MB" },
                ].map((res, i) => (
                  <div key={i} className="flex items-center justify-between p-4 bg-white/5 border border-white/10 rounded-2xl hover:border-orange-pure/50 transition-all group">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-xl bg-ink flex items-center justify-center text-white/40 group-hover:text-orange-pure transition-colors">
                        <FileText className="h-5 w-5" />
                      </div>
                      <div>
                        <div className="text-sm font-bold">{res.name}</div>
                        <div className="text-[10px] text-white/30 uppercase tracking-widest">{res.format} • {res.size}</div>
                      </div>
                    </div>
                    <button className="p-2 hover:bg-orange-pure rounded-lg transition-colors group/btn">
                      <Download className="h-4 w-4 text-white/40 group-hover/btn:text-white" />
                    </button>
                  </div>
                ))}
              </div>
            )}

            {activeTab === "checklist" && (
              <div className="space-y-6">
                <h3 className="text-xl font-bold mb-6">Checkpoint Operativi</h3>
                <div className="space-y-4">
                  {[
                    "Ho seguito la lezione integralmente",
                    "Ho scaricato e analizzato il template fornito",
                    "Ho eseguito il comando di test nel mio terminale",
                    "Ho prodotto l'output richiesto nell'esercizio",
                    "Ho verificato la coerenza dell'output con il framework",
                  ].map((check, i) => (
                    <label key={i} className="flex items-center gap-4 p-4 rounded-2xl border border-white/5 hover:bg-white/5 cursor-pointer transition-all group">
                      <input type="checkbox" className="w-5 h-5 rounded border-white/20 bg-transparent text-orange-pure focus:ring-orange-pure cursor-pointer" />
                      <span className="text-sm text-white/70 group-hover:text-white transition-colors">{check}</span>
                    </label>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="space-y-6">
          <div className="bg-[#111111] rounded-3xl p-6 border border-white/5">
            <h4 className="font-bold flex items-center gap-2 mb-4">
              <MessageSquare className="h-4 w-4 text-orange-pure" /> Supporto Studente
            </h4>
            <p className="text-xs text-white/50 leading-relaxed mb-6">
              Hai un dubbio tecnico o una domanda sul framework? Chiedi nella community o prenota una sessione rapida di AI-Pairing.
            </p>
            <div className="space-y-3">
              <button className="w-full py-3 rounded-xl bg-orange-pure/10 text-orange-pure text-[11px] font-bold uppercase tracking-widest hover:bg-orange-pure/20 transition-all flex items-center justify-center gap-2">
                Forum Studenti <ExternalLink className="h-3 w-3" />
              </button>
              <button className="w-full py-3 rounded-xl border border-white/10 text-white/60 text-[11px] font-bold uppercase tracking-widest hover:text-white hover:border-white/30 transition-all">
                Apri Ticket
              </button>
            </div>
          </div>

          <div className="bg-white/5 rounded-3xl p-6 border border-white/10">
            <div className="text-[10px] font-bold text-orange-pure/60 uppercase tracking-widest mb-1">PROSSIMA LEZIONE</div>
            {nextLesson ? (
              <>
                <div className="text-sm font-bold mb-3 truncate">{nextLesson.title}</div>
                <button
                  onClick={() => router.push(`/platform/course/${moduleId}/${nextLesson.slug}`)}
                  className="text-xs text-white/40 hover:text-white flex items-center gap-1 transition-colors"
                >
                  Salta ora <ChevronRight className="h-3 w-3" />
                </button>
              </>
            ) : (
              <div className="text-sm font-bold text-white/20 italic">Fine del Modulo</div>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}
