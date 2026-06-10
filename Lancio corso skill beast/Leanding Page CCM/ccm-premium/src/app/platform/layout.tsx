"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  ChevronRight, 
  ChevronDown, 
  PlayCircle, 
  CheckCircle2, 
  LayoutDashboard, 
  BookOpen, 
  Trophy, 
  Menu, 
  X,
  Sparkles
} from "lucide-react";
import { courseData } from "@/lib/course-data";

export default function PlatformLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const [isSidebarOpen, setSidebarOpen] = useState(true);
  const [expandedModules, setExpandedModules] = useState<string[]>(["0", "1"]);

  const toggleModule = (id: string) => {
    setExpandedModules((prev) =>
      prev.includes(id) ? prev.filter((m) => m !== id) : [...prev, id]
    );
  };

  return (
    <div className="flex h-screen bg-[#0a0a0a] text-white overflow-hidden font-onest">
      {/* Mobile Menu Overlay */}
      {!isSidebarOpen && (
        <button 
          onClick={() => setSidebarOpen(true)}
          className="lg:hidden fixed bottom-6 right-6 z-50 w-14 h-14 bg-orange-pure rounded-full flex items-center justify-center shadow-xl shadow-orange-pure/20"
        >
          <Menu className="h-6 w-6 text-white" />
        </button>
      )}

      {/* Sidebar */}
      <aside 
        className={`${
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        } lg:translate-x-0 fixed lg:relative z-40 w-80 h-full bg-[#111111] border-r border-white/10 transition-transform duration-300 flex flex-col`}
      >
        <div className="p-6 border-b border-white/10 flex items-center justify-between">
          <Link href="/platform" className="flex items-center gap-2 group">
            <div className="w-8 h-8 rounded bg-orange-pure flex items-center justify-center group-hover:scale-110 transition-transform">
              <Sparkles className="h-4 w-4 text-white" />
            </div>
            <span className="font-bold tracking-tight text-white/90">Claude Code Mastery</span>
          </Link>
          <button onClick={() => setSidebarOpen(false)} className="lg:hidden text-white/50 hover:text-white">
            <X className="h-5 w-5" />
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto p-4 custom-scrollbar">
          <div className="space-y-4">
            <Link 
              href="/platform"
              className={`flex items-center gap-3 p-3 rounded-lg text-sm transition-all ${
                pathname === "/platform" 
                  ? "bg-white/5 text-orange-pure font-semibold" 
                  : "text-white/60 hover:text-white hover:bg-white/5"
              }`}
            >
              <LayoutDashboard className="h-4 w-4" />
              Dashboard
            </Link>

            <div className="pt-4 pb-2 text-[11px] uppercase tracking-[0.2em] font-bold text-white/30 px-3">
              Programma Corso
            </div>

            {courseData.map((module) => (
              <div key={module.id} className="space-y-1">
                <button
                  onClick={() => toggleModule(module.id)}
                  className="w-full flex items-center justify-between p-3 rounded-lg text-sm transition-all text-white/80 hover:bg-white/5"
                >
                  <div className="flex items-center gap-3">
                    <span className="text-[10px] font-bold text-orange-pure/50 w-4">{module.id}</span>
                    <span className="font-medium truncate max-w-[180px]">{module.title.split("—")[0]}</span>
                  </div>
                  {expandedModules.includes(module.id) ? (
                    <ChevronDown className="h-4 w-4 text-white/30" />
                  ) : (
                    <ChevronRight className="h-4 w-4 text-white/30" />
                  )}
                </button>

                {expandedModules.includes(module.id) && (
                  <div className="ml-7 space-y-1 border-l border-white/5">
                    {module.lessons.map((lesson) => {
                      const lessonPath = `/platform/course/${module.id}/${lesson.slug}`;
                      const isActive = pathname === lessonPath;
                      
                      return (
                        <Link
                          key={lesson.id}
                          href={lessonPath}
                          className={`block p-2 pl-4 rounded-r-lg text-[13px] transition-all border-l-2 ${
                            isActive 
                              ? "bg-orange-pure/10 text-orange-pure border-orange-pure font-medium" 
                              : "text-white/40 hover:text-white/80 border-transparent"
                          }`}
                        >
                          <div className="flex items-center gap-2">
                            {isActive ? (
                              <PlayCircle className="h-3.5 w-3.5" />
                            ) : (
                              <div className="w-1 h-1 rounded-full bg-current" />
                            )}
                            {lesson.title}
                          </div>
                        </Link>
                      );
                    })}
                  </div>
                )}
              </div>
            ))}
          </div>
        </nav>

        <div className="p-4 border-t border-white/10 bg-[#0d0d0d]">
          <div className="bg-white/5 rounded-xl p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-[10px] uppercase tracking-widest font-bold text-white/40">Tuo Progresso</span>
              <span className="text-[10px] font-bold text-orange-pure">12%</span>
            </div>
            <div className="h-1 bg-white/10 rounded-full overflow-hidden">
              <div className="h-full bg-orange-pure w-[12%] rounded-full shadow-[0_0_8px_rgba(251,70,4,0.4)]" />
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden relative">
        {/* Top Header */}
        <header className="h-20 border-b border-white/10 flex items-center justify-between px-8 bg-[#0a0a0a]/80 backdrop-blur-md sticky top-0 z-30">
          <div className="flex items-center gap-4">
            <h2 className="text-sm md:text-base font-semibold text-white/90">
              {pathname === "/platform" ? "Bentornato, Student" : "Lezione in corso"}
            </h2>
          </div>
          <div className="flex items-center gap-5">
            <div className="hidden md:flex flex-col items-end">
              <span className="text-xs font-bold text-white/80">Supporto Studenti</span>
              <span className="text-[10px] text-orange-pure/70 uppercase tracking-widest">Digital Empire</span>
            </div>
            <div className="w-10 h-10 rounded-full bg-white/10 border border-white/20 flex items-center justify-center font-bold text-orange-pure">
              S
            </div>
          </div>
        </header>

        {/* Scrollable Viewport */}
        <div className="flex-1 overflow-y-auto custom-scrollbar p-6 md:p-10">
          <div className="max-w-6xl mx-auto">
            {children}
          </div>
        </div>
      </main>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.1);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(251, 70, 4, 0.4);
        }
      `}</style>
    </div>
  );
}
