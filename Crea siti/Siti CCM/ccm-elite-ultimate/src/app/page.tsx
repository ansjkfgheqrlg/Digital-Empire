import { Hero } from "@/components/sections/hero";
import { ScienceStats } from "@/components/sections/science-stats";
import { Overview } from "@/components/sections/overview";
import { Hierarchy } from "@/components/sections/hierarchy";
import { PowerDeck } from "@/components/sections/power-deck";
import { Method } from "@/components/sections/method";
import { MasteryMap } from "@/components/sections/mastery-map";
import { ObjectionsGrid } from "@/components/sections/objections-grid";
import { Ecosystem } from "@/components/sections/ecosystem";
import { FinalCTA } from "@/components/sections/final-cta";
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";
import { StickyCTA } from "@/components/sticky-cta";

export default function Home() {
  return (
    <SmoothScrollProvider>
      <main className="relative grain-fine">
        <StickyCTA href="#offer" label="Prendi il Posto" />
        
        <Hero />
        <ScienceStats />
        <Overview />
        <Hierarchy />
        <PowerDeck />
        <Method />
        <MasteryMap />
        <ObjectionsGrid />
        <Ecosystem />
        <FinalCTA />

        {/* Footer Minimal Elite */}
        <footer className="bg-ink-2 py-16 border-t border-white/5 relative z-10">
          <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-10">
            <div className="text-white/20 text-[10px] uppercase tracking-[0.4em] font-black italic">
              Digital Empire &copy; 2026 · Claude Code Mastery · Elite Architecture
            </div>
            <div className="flex gap-10 text-white/10 text-[10px] uppercase tracking-[0.2em] font-bold">
              <a href="#" className="hover:text-orange transition-colors">Privacy Policy</a>
              <a href="#" className="hover:text-orange transition-colors">Termini di Servizio</a>
              <a href="#" className="hover:text-orange transition-colors">Lavora con noi</a>
            </div>
          </div>
        </footer>
      </main>
    </SmoothScrollProvider>
  );
}
