"use client";

import React, { useState } from "react";
import { Play, Pause, Volume2, Maximize, Settings, Sparkles } from "lucide-react";
import { cn } from "@/lib/utils";

export const VideoPlayer = ({ title }: { title?: string }) => {
  const [isPlaying, setIsPlaying] = useState(false);

  return (
    <div className="relative group rounded-[32px] overflow-hidden border border-white/10 bg-ink shadow-2xl">
      {/* Aspect Ratio Container */}
      <div className="aspect-video relative overflow-hidden bg-black">
        {/* Mock Poster / Overlay */}
        {!isPlaying && (
          <div className="absolute inset-0 flex items-center justify-center z-10">
            <div className="absolute inset-0 bg-ink/60 backdrop-blur-sm" />
            <button 
              onClick={() => setIsPlaying(true)}
              className="relative w-24 h-24 rounded-full bg-orange flex items-center justify-center shadow-[0_0_60px_rgba(251,70,4,0.4)] hover:scale-110 transition-transform duration-500 group/play"
            >
              <div className="absolute inset-0 rounded-full border border-white/30 animate-pulse" />
              <Play className="h-10 w-10 text-white fill-white ml-2 transition-transform group-hover/play:scale-110" />
            </button>
            <div className="absolute bottom-10 left-1/2 -translate-x-1/2 flex items-center gap-3">
              <span className="bubble-orange py-1.5 px-4 text-[10px] uppercase tracking-widest font-bold">
                <Sparkles className="h-3 w-3" /> Digital Empire Cinema
              </span>
            </div>
          </div>
        )}

        {/* Video Placeholder Content */}
        <div className="absolute inset-0 flex flex-col items-center justify-center p-12 text-center">
            <div className="text-white/20 font-bold text-4xl uppercase tracking-[0.2em] select-none">
              Empire Video Player
            </div>
            <div className="mt-4 text-white/10 text-xs font-mono select-none">
              // Premium Content Encrypted for {title || "Student"}
            </div>
        </div>

        {/* Custom Controls (Simplified Mock) */}
        <div className={cn(
          "absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black/90 to-transparent transition-opacity duration-300 z-20",
          !isPlaying ? "opacity-0" : "opacity-100 group-hover:opacity-100"
        )}>
          <div className="flex flex-col gap-6">
            {/* Progress Bar */}
            <div className="h-1.5 bg-white/10 rounded-full relative group/progress cursor-pointer overflow-hidden">
               <div className="absolute h-full bg-orange w-1/3 rounded-full" />
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center gap-6">
                <button onClick={() => setIsPlaying(!isPlaying)} className="hover:text-orange transition-colors">
                  {isPlaying ? <Pause className="h-5 w-5" /> : <Play className="h-5 w-5" />}
                </button>
                <div className="flex items-center gap-3">
                  <Volume2 className="h-5 w-5" />
                  <div className="w-20 h-1 bg-white/20 rounded-full">
                    <div className="w-2/3 h-full bg-white rounded-full" />
                  </div>
                </div>
                <span className="text-xs font-mono text-white/50">12:45 / 45:00</span>
              </div>
              
              <div className="flex items-center gap-6">
                <Settings className="h-5 w-5 hover:rotate-45 transition-transform" />
                <Maximize className="h-5 w-5 hover:scale-110 transition-transform" />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Empire Framing Details */}
      <div className="absolute top-6 left-6 pointer-events-none opacity-20">
        <div className="border-t border-l border-white/40 w-8 h-8 rounded-tl-lg" />
      </div>
      <div className="absolute top-6 right-6 pointer-events-none opacity-20">
        <div className="border-t border-r border-white/40 w-8 h-8 rounded-tr-lg" />
      </div>
    </div>
  );
};
