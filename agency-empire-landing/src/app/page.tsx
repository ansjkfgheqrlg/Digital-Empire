import { Hero } from "@/components/sections/hero";
import { VSL } from "@/components/sections/vsl";
import { ScienceStats } from "@/components/sections/science-stats";
import { Audience } from "@/components/sections/audience";
import { Problems } from "@/components/sections/problems";
import { Hierarchy } from "@/components/sections/hierarchy";
import { Pillars } from "@/components/sections/pillars";
import { FlowFramework } from "@/components/sections/flow-framework";
import { PowerDeck } from "@/components/sections/power-deck";
import { Bonuses } from "@/components/sections/bonuses";
import { PricingROI } from "@/components/sections/pricing-roi";
import { Competitors } from "@/components/sections/competitors";
import { SystemsShowcase } from "@/components/sections/systems-showcase";
import { OutreachDeep, ContentDeep, BrainDeep } from "@/components/sections/service-deep";
import { OutreachInside } from "@/components/sections/outreach-inside";
import { ContentOutput } from "@/components/sections/content-output";
import { SecondBrainInside } from "@/components/sections/second-brain-inside";
import { NoFluff } from "@/components/sections/no-fluff";
import { Clarity } from "@/components/sections/clarity";
import { ListenUp } from "@/components/sections/listen-up";
import { WhoGuides } from "@/components/sections/who-guides";
import { BuilderNotTrainer } from "@/components/sections/builder-not-trainer";
import { MyPromise } from "@/components/sections/my-promise";
import { ToolStack } from "@/components/sections/tool-stack";
import { Objections } from "@/components/sections/objections";
import { FAQ } from "@/components/sections/faq";
import { FinalCTA } from "@/components/sections/final-cta";
import { FinalOffer } from "@/components/sections/final-offer";
import { AboutStory } from "@/components/sections/about-story";
import { StickyCTA } from "@/components/sticky-cta";
import { Header } from "@/components/header";
import { Results } from "@/components/sections/results";

export default function Home() {
  return (
    <main className="relative">
      <Header />
      <StickyCTA href="#prenota" label="Prenota una Chiamata" />
      
      <Hero />
      <VSL />
      <ScienceStats />
      <Audience />
      <Problems />
      <Competitors />
      <ListenUp />
      <div className="divider-silver-orange" aria-hidden="true" />
      <Hierarchy />
      <Pillars />
      <FlowFramework />
      <div className="divider-silver-orange" aria-hidden="true" />
      <SystemsShowcase />
      <OutreachDeep />
      <OutreachInside />
      <ContentDeep />
      <ContentOutput />
      <BrainDeep />
      <SecondBrainInside />
      <Results />
      <NoFluff />
      <ToolStack />
      <div className="divider-silver-orange" aria-hidden="true" />
      <PowerDeck />
      <div className="divider-silver-orange" aria-hidden="true" />
      <WhoGuides />
      <BuilderNotTrainer />
      <Bonuses />
      <PricingROI />
      <Clarity />
      <MyPromise />
      <Objections />
      <FAQ />
      <div className="divider-silver-orange" aria-hidden="true" />
      <FinalCTA />
      <FinalOffer />
      <AboutStory />

      {/* Footer Minimal Empire */}
      <footer className="bg-ink-2 py-20 border-t border-white/5 text-center">
        <div className="max-w-5xl mx-auto px-6 flex flex-col items-center gap-8">
          <div className="text-white/30 text-xs uppercase tracking-[0.3em] font-bold">
            Digital Empire &copy; 2026 · Implementazioni AI Proprietarie
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
