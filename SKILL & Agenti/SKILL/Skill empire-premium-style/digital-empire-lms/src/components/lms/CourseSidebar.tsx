"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  ChevronRight, 
  ChevronDown, 
  PlayCircle, 
  Sparkles, 
  CheckCircle2, 
  Lock, 
  Menu, 
  X,
  Layers,
  Zap,
  BookOpen
} from "lucide-react";
import { cn } from "@/lib/utils";
import { courseContent } from "@/lib/course-content";

export const CourseSidebar = () => {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(true);
  const [expandedChapters, setExpandedChapters] = useState<string[]>(["1"]);

  const toggleChapter = (id: string) => {
    setExpandedChapters(prev => 
      prev.includes(id) ? prev.filter(c => c !== id) : [...prev, id]
    );
  };

  return (
    <>
      {/* Mobile Toggle */}
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className="lg:hidden fixed bottom-6 right-6 z-50 w-14 h-14 bg-orange rounded-full flex items-center justify-center shadow-xl shadow-orange/30 text-white"
      >
        {isOpen ? <X /> : <Menu />}
      </button>

      {/* Sidebar */}
      <aside className={cn(
        "fixed inset-y-0 left-0 z-40 w-80 bg-ink border-r border-white/5 transition-transform duration-500 ease-out",
        !isOpen && "-translate-x-full lg:translate-x-0 lg:w-20"
      )}>
        <div className="flex flex-col h-full">
          {/* Header */}
          <div className="p-6 border-b border-white/5">
            <Link href="/course" className="flex items-center gap-3 group">
              <div className="w-8 h-8 rounded bg-orange flex items-center justify-center shrink-0">
                <Sparkles className="h-4 w-4 text-white" />
              </div>
              <div className={cn("transition-opacity duration-300", !isOpen && "lg:opacity-0")}>
                <h2 className="text-sm font-bold tracking-tight text-white leading-tight">Digital Empire</h2>
                <p className="text-[10px] uppercase tracking-widest text-white/40 font-bold">Mastery LMS</p>
              </div>
            </Link>
          </div>

          {/* Navigation */}
          <nav className="flex-1 overflow-y-auto p-4 custom-scrollbar space-y-2">
            {courseContent.map((chapter) => (
              <div key={chapter.id} className="space-y-1">
                <button
                  onClick={() => toggleChapter(chapter.id)}
                  className={cn(
                    "w-full flex items-center justify-between p-3 rounded-xl transition-all",
                    "hover:bg-white/5 group",
                    expandedChapters.includes(chapter.id) ? "text-white" : "text-white/50"
                  )}
                >
                  <div className="flex items-center gap-3">
                    <div className="w-6 h-6 rounded bg-white/5 flex items-center justify-center text-[10px] font-bold group-hover:text-orange transition-colors">
                      {chapter.id}
                    </div>
                    {isOpen && <span className="text-xs font-bold truncate max-w-[170px]">{chapter.title.split(":")[1].trim()}</span>}
                  </div>
                  {isOpen && (
                    expandedChapters.includes(chapter.id) ? <ChevronDown className="h-4 w-4 opacity-30" /> : <ChevronRight className="h-4 w-4 opacity-30" />
                  )}
                </button>

                {expandedChapters.includes(chapter.id) && isOpen && (
                  <div className="ml-6 space-y-1 border-l border-white/5">
                    {chapter.lessons.map((lesson) => {
                      const lessonPath = `/course/${chapter.slug}/${lesson.slug}`;
                      const isActive = pathname === lessonPath;

                      return (
                        <Link
                          key={lesson.id}
                          href={lessonPath}
                          className={cn(
                            "flex items-center gap-3 p-2.5 pl-5 rounded-r-xl text-[12px] transition-all border-l-2",
                            isActive 
                              ? "bg-white/5 text-orange border-orange font-semibold" 
                              : "text-white/30 border-transparent hover:text-white/60"
                          )}
                        >
                          <PlayCircle className={cn("h-3.5 w-3.5", isActive ? "text-orange" : "opacity-30")} />
                          {lesson.title}
                        </Link>
                      );
                    })}
                  </div>
                )}
              </div>
            ))}
          </nav>

          {/* Footer User Info */}
          <div className="p-6 border-t border-white/5 bg-ink-2">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center font-bold text-orange">
                ST
              </div>
              {isOpen && (
                <div className="flex flex-col">
                  <span className="text-xs font-bold text-white/90">Studente Pro</span>
                  <span className="text-[10px] text-white/30 font-bold uppercase tracking-widest">Digital Empire</span>
                </div>
              )}
            </div>
            
            {isOpen && (
              <div className="mt-6 flex flex-col gap-3">
                <div className="flex justify-between text-[10px] font-bold uppercase tracking-widest text-white/20">
                  <span>Progresso</span>
                  <span>15%</span>
                </div>
                <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                  <div className="h-full bg-orange w-[15%] rounded-full shadow-[0_0_10px_rgba(251,70,4,0.4)]" />
                </div>
              </div>
            )}
          </div>
        </div>
      </aside>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.05); border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(251,70,4,0.3); }
      `}</style>
    </>
  );
};
