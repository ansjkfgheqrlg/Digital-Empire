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
// Sezioni AGGIUNTE il 2026-09-12 (ordine di Max: solo aggiungere, mai modificare l'esistente)
import { Specchio } from "@/sezioni-aggiunte/specchio";
import { ProveVere } from "@/sezioni-aggiunte/prove-vere";
import { CosaOttieni } from "@/sezioni-aggiunte/cosa-ottieni";
// Sezioni AGGIUNTE il 2026-09-13 (Dossier 38 v2, Atto I): la firma (null senza ritratto) e il rail dei fatti
import { Firma } from "@/sezioni-aggiunte/firma";
import { RailFatti } from "@/sezioni-aggiunte/rail-fatti";
// Sezioni AGGIUNTE il 2026-09-13 pomeriggio (Dossier 38 v2 §F + §I, ordine di Max «tutte»): solo inserimenti
import { CompetitorVivo } from "@/sezioni-aggiunte/competitor-vivo";
import { PrimaDopo } from "@/sezioni-aggiunte/prima-dopo";
import { Scala } from "@/sezioni-aggiunte/scala";
import { Cartella } from "@/sezioni-aggiunte/cartella";
import { GuardaloGirare } from "@/sezioni-aggiunte/guardalo-girare";
import { DueTipi } from "@/sezioni-aggiunte/due-tipi";
import { RailSistemi } from "@/sezioni-aggiunte/rail-sistemi";
import { FasciaManifesto } from "@/sezioni-aggiunte/fascia-manifesto";
import { Stanza } from "@/sezioni-aggiunte/stanza";
import { DietroLeQuinte } from "@/sezioni-aggiunte/dietro-le-quinte";
import { Mappa } from "@/sezioni-aggiunte/mappa";
import { Tessera } from "@/sezioni-aggiunte/tessera";
import { QuantoCosta } from "@/sezioni-aggiunte/quanto-costa";
import { SeNonFunziona } from "@/sezioni-aggiunte/se-non-funziona";
import { FaqContratto } from "@/sezioni-aggiunte/faq-contratto";
import { CodaLegale } from "@/sezioni-aggiunte/coda-legale";
import { StickyCTA } from "@/components/sticky-cta";
import { Header } from "@/components/header";
import { Results } from "@/components/sections/results";

export default function Home() {
  return (
    <main className="relative">
      <Header />
      <StickyCTA href="#prenota" label="Prenota una Chiamata" />
      
      <Hero />
      <Firma />
      <RailFatti />
      <VSL />
      <ScienceStats />
      <Audience />
      <Problems />
      <Specchio />
      <Competitors />
      <CompetitorVivo />
      <ListenUp />
      <PrimaDopo />
      <div className="divider-silver-orange" aria-hidden="true" />
      <Hierarchy />
      <Pillars />
      <FlowFramework />
      <Scala />
      <div className="divider-silver-orange" aria-hidden="true" />
      <SystemsShowcase />
      <Cartella />
      <OutreachDeep />
      <OutreachInside />
      <GuardaloGirare />
      <ContentDeep />
      <ContentOutput />
      <DueTipi />
      <BrainDeep />
      <SecondBrainInside />
      <Results />
      <ProveVere />
      <RailSistemi />
      <NoFluff />
      <ToolStack />
      <div className="divider-silver-orange" aria-hidden="true" />
      <PowerDeck />
      <FasciaManifesto />
      <div className="divider-silver-orange" aria-hidden="true" />
      <WhoGuides />
      <Stanza />
      <BuilderNotTrainer />
      <DietroLeQuinte />
      <Mappa />
      <Bonuses />
      <PricingROI />
      <Tessera />
      <Clarity />
      <QuantoCosta />
      <MyPromise />
      <SeNonFunziona />
      <Objections />
      <FAQ />
      <FaqContratto />
      <div className="divider-silver-orange" aria-hidden="true" />
      <CosaOttieni />
      <FinalCTA />
      <FinalOffer />
      <AboutStory />

      <CodaLegale />
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
