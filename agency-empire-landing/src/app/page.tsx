import { Header } from "@/components/header";
import { StickyCTA } from "@/components/sticky-cta";
import { Hero } from "@/sections-vivo/n01-hero";
import { Specchio } from "@/sections-vivo/n02-specchio";
import { Numeri } from "@/sections-vivo/n03-numeri";
import { Competitor } from "@/sections-vivo/n05-competitor";
import { AscoltaBene } from "@/sections-vivo/n06-ascolta-bene";
import { Scala } from "@/sections-vivo/n07-scala";
import { Sistemi } from "@/sections-vivo/n08-sistemi";
import { Formula } from "@/sections-vivo/n09-formula";
import { Processo } from "@/sections-vivo/n10-processo";
import { Prove } from "@/sections-vivo/n11-prove";
import { PerChi } from "@/sections-vivo/n12-per-chi";
import { ChiSiamo } from "@/sections-vivo/n13-chi-siamo";
import { Prezzi } from "@/sections-vivo/n14-prezzi";
import { Garanzia } from "@/sections-vivo/n15-garanzia";
import { Obiezioni } from "@/sections-vivo/n16-obiezioni";
import { CosaOttieni } from "@/sections-vivo/n17-cosa-ottieni";
import { Faq } from "@/sections-vivo/n18-faq";
import { Chiusura } from "@/sections-vivo/n19-chiusura";
import { Legale } from "@/sections-vivo/n20-legale";

/* Sito Agency Vivo v2 (Dossier 37 v2, Parte III): 20 sezioni + coda, 0 divider.
   N4 (VSL) non esiste finché non esiste il `src` del video: mai un segnaposto video. */
export default function Home() {
  return (
    <main id="main" className="relative">
      <Header />
      <StickyCTA />
      <Hero />
      <Specchio />
      <Numeri />
      <Competitor />
      <AscoltaBene />
      <Scala />
      <Sistemi />
      <Formula />
      <Processo />
      <Prove />
      <PerChi />
      <ChiSiamo />
      <Prezzi />
      <Garanzia />
      <Obiezioni />
      <CosaOttieni />
      <Faq />
      <Chiusura />
      <Legale />
    </main>
  );
}
