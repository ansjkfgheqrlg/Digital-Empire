"use client";

import { Terminal } from "lucide-react";
import { LiveTerminal } from "@/components/live-terminal";

export default function LogsPage() {
  return (
    <div className="flex flex-col h-screen bg-ink">

      {/* Header */}
      <header className="h-14 border-b border-white/[0.08] flex items-center gap-3 px-8 bg-ink-2 sticky top-0 z-40 shrink-0">
        <Terminal className="w-4 h-4 text-[#fb4604]" />
        <span className="text-sm font-black text-white uppercase tracking-widest">Terminal Logs</span>
        <span className="text-[10px] text-white/50 font-bold">— output live da tutti i processi</span>
      </header>

      {/* Full-height terminal */}
      <div className="flex-1 overflow-hidden p-6">
        <div className="h-full rounded-[20px] overflow-hidden border border-white/[0.08]"
          style={{ boxShadow: "0 40px 80px -40px rgba(0,0,0,0.9)" }}>
          <LiveTerminal />
        </div>
      </div>
    </div>
  );
}
