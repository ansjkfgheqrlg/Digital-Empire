"use client";

import React from "react";
import { CourseSidebar } from "@/components/lms/CourseSidebar";

export default function CourseLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen bg-ink">
      <CourseSidebar />
      
      <main className="flex-1 lg:ml-80 transition-all duration-500">
        {/* Top bar subtle */}
        <header className="h-20 flex items-center justify-between px-8 border-b border-white/5 bg-ink/50 backdrop-blur-md sticky top-0 z-30">
          <div className="text-[10px] uppercase tracking-[0.3em] font-bold text-white/20">
            System: <span className="text-orange">Operational</span>
          </div>
          <div className="flex items-center gap-6">
            <div className="text-right hidden md:block">
              <p className="text-[10px] font-bold text-white/50 leading-none">Supporto Premium</p>
              <p className="text-[9px] uppercase tracking-widest text-orange mt-1">Connesso</p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center font-bold text-orange">
              ST
            </div>
          </div>
        </header>

        <div className="p-8 md:p-12 lg:p-16 max-w-7xl mx-auto">
          {children}
        </div>
      </main>
    </div>
  );
}
