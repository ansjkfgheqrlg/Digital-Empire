import { Navbar } from "@/components/navbar";
import { StickyCTA } from "@/components/sticky-cta";

import { Hero } from "@/sections-vivo/n01-hero";
import { Specchio } from "@/sections-vivo/n02-specchio";
import { Numeri } from "@/sections-vivo/n03-numeri";
import { Fabbriche } from "@/sections-vivo/n04-fabbriche";
import { Casi } from "@/sections-vivo/n05-casi";
import { Competitor } from "@/sections-vivo/n06-competitor";
import { Diagnosi } from "@/sections-vivo/n07-diagnosi";
import { AscoltaBene } from "@/sections-vivo/n08-ascolta-bene";
import { Formula } from "@/sections-vivo/n09-formula";
import { Processo } from "@/sections-vivo/n10-processo";
import { ChiSiamo } from "@/sections-vivo/n11-chi-siamo";
import { PerChi } from "@/sections-vivo/n12-per-chi";
import { Prove } from "@/sections-vivo/n13-prove";
import { Garanzia } from "@/sections-vivo/n14-garanzia";
import { Obiezioni } from "@/sections-vivo/n15-obiezioni";
import { CosaOttieni } from "@/sections-vivo/n16-cosa-ottieni";
import { Faq } from "@/sections-vivo/n17-faq";
import { Chiusura } from "@/sections-vivo/n18-chiusura";
import { Legale } from "@/sections-vivo/n19-legale";

/* Sito Agency Vivo — Dossier 37, Parte III: 19 sezioni cucite, nessun divider.
   L'ordine segue la temperatura: specchio e agitazione, poi prova, metodo, chi siamo, il sì.
   Le 10 CTA "a temperatura" stanno dentro N1, N4, N5, N7, N8, N10, N12, N14, N16, N18. */
export default function HomePage() {
  return (
    <>
      <Navbar />
      <main id="main" className="relative">
        <Hero />
        <Specchio />
        <Numeri />
        <Fabbriche />
        <Casi />
        <Competitor />
        <Diagnosi />
        <AscoltaBene />
        <Formula />
        <Processo />
        <ChiSiamo />
        <PerChi />
        <Prove />
        <Garanzia />
        <Obiezioni />
        <CosaOttieni />
        <Faq />
        <Chiusura />
      </main>
      <Legale />
      <StickyCTA />
    </>
  );
}
