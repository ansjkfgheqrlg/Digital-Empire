"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Sparkles, Trophy, TrendingUp, TrendingDown, Minus, ArrowRight, Search } from "lucide-react";
import { Reveal } from "@/components/reveal";
import Link from "next/link";
import { initialArtists, type Artist } from "@/lib/artists";

export function RankingBoard() {
  const [artists, setArtists] = useState<Artist[]>(initialArtists);
  const [visibleCount, setVisibleCount] = useState(10);
  const [searchQuery, setSearchQuery] = useState("");

  const filteredArtists = artists.filter(artist => 
    artist.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    artist.alias.toLowerCase().includes(searchQuery.toLowerCase())
  );

  useEffect(() => {
    // ... useEffect content ...
    // Simulate real-time score updates every 3.5 seconds
    const interval = setInterval(() => {
      setArtists((currentArtists) => {
        // Calculate the second highest score to maintain MJ's lead
        const secondHighest = Math.max(...currentArtists.filter(a => a.id !== "mj").map(a => a.score));

        let updated = currentArtists.map((artist, index) => {
          // Logic:
          // 1. MJ has a "Master Momentum"
          // 2. Top 10 have "Stable Momentum"
          // 3. Artists 11-100 have "Market Momentum" (more volatile but based on a seed)
          
          let boost = 0;
          const isMJ = artist.id === "mj";
          const isTop10 = index < 10 && !isMJ;
          
          if (isMJ) {
            // MJ stays ahead by at least 15k points
            boost = Math.floor(Math.random() * 2000) + 500;
            const targetScore = Math.max(artist.score + boost, secondHighest + 15000);
            return { ...artist, score: targetScore };
          } else if (isTop10) {
            // Top 10 move slowly (prestige stability)
            boost = Math.floor(Math.random() * 1200) + 200;
          } else {
            // Others move based on their ID as a seed + time factor for "trends"
            const seed = artist.id.length + index;
            const trend = Math.sin((Date.now() / 20000) + seed) * 1500;
            boost = Math.floor(Math.random() * 2500) + 500 + trend;
          }

          return { ...artist, score: Math.max(0, Math.floor(artist.score + boost)) };
        });

        // Sort by score
        updated.sort((a, b) => b.score - a.score);

        return updated.map((artist, index) => ({
          ...artist,
          previousRank: currentArtists.findIndex((a) => a.id === artist.id) + 1,
        }));
      });
    }, 10000);

    return () => clearInterval(interval);
  }, []);


  return (
    <div className="max-w-4xl mx-auto w-full flex flex-col gap-4">
      <Reveal className="mb-6 flex flex-col items-center gap-6">
        <div className="bubble-purple shadow-2xl">
          <Sparkles className="w-4 h-4" />
          <span>Analisi Live: Classifica Superstar Globali</span>
        </div>

        {/* Mini Search Menu */}
        <div className="relative w-full max-w-md group">
          <div className="absolute inset-y-0 left-4 flex items-center pointer-events-none">
            <Search className="w-4 h-4 text-gray-400 group-focus-within:text-purple transition-colors" />
          </div>
          <input 
            type="text" 
            placeholder="Cerca la tua superstar..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-white/5 border border-white/10 rounded-full py-3 pl-12 pr-6 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-purple/30 focus:bg-white/10 transition-all placeholder:text-gray-500"
          />
        </div>
      </Reveal>

      <ul className="flex flex-col gap-4">
          {filteredArtists.slice(0, searchQuery ? 100 : visibleCount).map((artist, index) => {
            const currentRank = artists.findIndex(a => a.id === artist.id) + 1;
            const isPodium = currentRank <= 3;
            
            // Determine trend
            let TrendIcon = Minus;
            let trendColor = isPodium ? "text-white/70" : "text-gray-400";
            if (currentRank < artist.previousRank) {
              TrendIcon = TrendingUp;
              trendColor = isPodium ? "text-white" : "text-green-600";
            } else if (currentRank > artist.previousRank) {
              TrendIcon = TrendingDown;
              trendColor = isPodium ? "text-white/50" : "text-red-600";
            }

            return (
              <li
                key={artist.id}
              >
                <Link 
                  href={`/artists/${artist.id}`}
                  className={`group relative flex items-center justify-between p-5 md:p-6 rounded-2xl border transition-all duration-300 ${
                    currentRank === 1 ? "card-podium-1 z-20 scale-[1.03] shadow-2xl" :
                    currentRank === 2 ? "card-podium-2 z-10 scale-[1.01]" :
                    currentRank === 3 ? "card-podium-3 z-0" :
                    "card-paper z-0 hover:border-purple/30 hover:shadow-lg"
                  }`}
                >
                  <div className="flex items-center gap-5 md:gap-8 relative z-10">
                    {/* Rank Number */}
                    <div className={`w-12 h-12 flex items-center justify-center font-bold text-xl md:text-2xl rounded-full ${
                      isPodium ? "bg-white/20 text-white backdrop-blur-sm" : "bg-[#f4f4f4] text-[#1c1c1c]"
                    }`}>
                      #{currentRank}
                    </div>
                    
                    {/* Artist Info */}
                    <div className="flex flex-col">
                      <span className={`text-xs md:text-sm font-semibold tracking-wider uppercase mb-1 ${
                        isPodium ? "text-white/80" : "text-gray-500"
                      }`}>
                        {artist.alias}
                      </span>
                      <div className="flex items-center gap-3">
                        <h3 className={`text-xl md:text-4xl font-bold tracking-tight ${isPodium ? "text-white" : "text-ink"}`}>
                          {artist.name}
                        </h3>
                        <ArrowRight className={`w-5 h-5 transition-transform group-hover:translate-x-1 ${isPodium ? "text-white/60" : "text-purple/40"}`} />
                      </div>
                    </div>
                  </div>

                  {/* Score & Trend */}
                  <div className="flex flex-col items-end gap-2 relative z-10">
                    <div className={`flex items-center gap-2 font-mono text-xl md:text-3xl font-bold ${isPodium ? "text-white" : "text-ink"}`}>
                      {artist.score.toLocaleString()} 
                      <Trophy className={`w-5 h-5 ${isPodium ? "text-white" : "text-gray-400"}`} />
                    </div>
                    <div className={`flex items-center gap-1 text-sm font-semibold ${trendColor}`}>
                      <TrendIcon className="w-4 h-4" />
                      {currentRank < artist.previousRank ? "Salito" : currentRank > artist.previousRank ? "Sceso" : "Stabile"}
                    </div>
                  </div>
                  
                  {/* Visual indicator for #1 */}
                  {currentRank === 1 && (
                    <div className="absolute -top-3 -right-3 w-8 h-8 rounded-full bg-[#9D4EDD] shadow-[0_0_20px_rgba(157,78,221,0.8)] border-2 border-white flex items-center justify-center animate-pulse">
                      <Trophy className="w-4 h-4 text-white" />
                    </div>
                  )}
                </Link>
              </li>
            );
          })}
      </ul>

      {!searchQuery && visibleCount < artists.length && (
        <Reveal delay={0.2} className="mt-8 flex justify-center">
          <button 
            onClick={() => setVisibleCount(prev => Math.min(prev + 10, artists.length))}
            className="btn-purple px-10 py-4 text-lg font-bold group"
          >
            Espandi Classifica
            <TrendingUp className="w-5 h-5 transition-transform group-hover:translate-y-[-2px]" />
          </button>
        </Reveal>
      )}

      {searchQuery && filteredArtists.length === 0 && (
        <Reveal className="mt-12 text-center py-20 card-paper border-dashed">
          <p className="text-gray-500 font-medium">Nessun artista trovato per "{searchQuery}"</p>
        </Reveal>
      )}
    </div>


  );
}

