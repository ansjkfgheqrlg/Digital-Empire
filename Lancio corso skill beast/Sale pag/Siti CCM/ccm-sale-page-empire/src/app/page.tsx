import { Hero } from "@/components/sections/hero";
import { ScienceStats } from "@/components/sections/science-stats";
import { Audience } from "@/components/sections/audience";
import { Problems } from "@/components/sections/problems";
import { Hierarchy } from "@/components/sections/hierarchy";
import { Pillars } from "@/components/sections/pillars";
import { Roadmap } from "@/components/sections/roadmap";
import { MasteryMap } from "@/components/sections/mastery-map";
import { PowerDeck } from "@/components/sections/power-deck";
import { Bonuses } from "@/components/sections/bonuses";
import { PricingROI } from "@/components/sections/pricing-roi";
import { Objections } from "@/components/sections/objections";
import { FAQ } from "@/components/sections/faq";
import { FinalCTA } from "@/components/sections/final-cta";
import { StickyCTA } from "@/components/sticky-cta";

export default function Home() {
  return (
    <main className="relative">
      <StickyCTA href="#pricing" label="Prendi il Posto" />
      
      <Hero />
      <ScienceStats />
      <Audience />
      <Problems />
      <Hierarchy />
      <Pillars />
      <Roadmap />
      <MasteryMap />
      <PowerDeck />
      <Bonuses />
      <PricingROI />
      <Objections />
      <FAQ />
      <FinalCTA />

      {/* Footer Minimal Empire */}
      <footer className="bg-ink-2 py-20 border-t border-white/5 text-center">
        <div className="max-w-5xl mx-auto px-6 flex flex-col items-center gap-8">
          <div className="text-white/30 text-xs uppercase tracking-[0.3em] font-bold">
            Digital Empire &copy; 2026 · Claude Code Mastery
          </div>
          <div className="flex gap-10 text-white/20 text-[10px] uppercase tracking-widest font-bold">
            <a href="#" className="hover:text-orange transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-orange transition-colors">Termini e Condizioni</a>
          </div>
          <div className="text-white/10 text-[9px] uppercase tracking-widest leading-relaxed max-w-md">
            I risultati promessi dipendono dall'impegno individuale. Questo sito non fa parte di Facebook o Facebook Inc. Inoltre, questo sito NON è approvato da Facebook in alcun modo.
          </div>
        </div>
      </footer>
    </main>
  );
}
