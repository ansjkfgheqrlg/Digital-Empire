import { Hero } from "@/components/sections/hero";
import { ScienceStats } from "@/components/sections/science-stats";
import { Audience } from "@/components/sections/audience";
import { Problems } from "@/components/sections/problems";
import { Hierarchy } from "@/components/sections/hierarchy";
import { Roadmap } from "@/components/sections/roadmap";
import { PowerDeck } from "@/components/sections/power-deck";
import { FAQ } from "@/components/sections/faq";
import { FinalCTA } from "@/components/sections/final-cta";
import { StickyCTA } from "@/components/sticky-cta";

export default function Home() {
  return (
    <main className="relative">
      <StickyCTA href="#offer" label="Prendi il Posto" />
      
      <Hero />
      <ScienceStats />
      <Audience />
      <Problems />
      <Hierarchy />
      <Roadmap />
      <PowerDeck />
      <FAQ />
      <FinalCTA />

      {/* Footer Minimal Empire */}
      <footer className="bg-ink-2 py-12 border-t border-white/5">
        <div className="max-w-5xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="text-white/30 text-xs uppercase tracking-widest font-bold">
            Digital Empire &copy; 2026 · Claude Code Mastery
          </div>
          <div className="flex gap-8 text-white/20 text-xs uppercase tracking-widest font-medium">
            <a href="#" className="hover:text-orange transition-colors">Privacy</a>
            <a href="#" className="hover:text-orange transition-colors">Termini</a>
            <a href="#" className="hover:text-orange transition-colors">Contatti</a>
          </div>
        </div>
      </footer>
    </main>
  );
}
