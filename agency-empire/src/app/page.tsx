import { Navbar } from "@/components/navbar";
import { Footer } from "@/components/footer";
import { StickyCTA } from "@/components/sticky-cta";

import { Hero } from "@/sections/01-hero";
import { Stats } from "@/sections/02-stats";
import { Servizi } from "@/sections/03-servizi";
import { Preventa } from "@/sections/03b-preventa";
import { Problema } from "@/sections/04-problema";
import { DiagnosiCRO } from "@/sections/05-diagnosi-cro";
import { AscoltaBene } from "@/sections/05b-ascolta-bene";
import { MetodoAPSOC } from "@/sections/06-metodo-apsoc";
import { FunnelViz } from "@/sections/07-funnel-viz";
import { Processo } from "@/sections/08-processo";
import { Stack } from "@/sections/17-stack";
import { Portfolio } from "@/sections/09-portfolio";
import { ProveNovacar } from "@/sections/09b-prove-novacar";
import { ChiSiamo } from "@/sections/16-chi-siamo";
import { PerChi } from "@/sections/10-per-chi";
import { Testimonial } from "@/sections/11-testimonial";
import { CarteScoperte } from "@/sections/11b-carte-scoperte";
import { Garanzia } from "@/sections/12-garanzia";
import { FAQSection } from "@/sections/13-faq";
import { CTAFinale } from "@/sections/14-cta-finale";
import { Objections } from "@/sections/15-objections";

function Divider() {
  return <div className="divider-silver-navy" aria-hidden="true" />;
}

export default function HomePage() {
  return (
    <>
      <Navbar />
      <main id="main" className="relative">
        {/* Sezioni 1-3 fluide, stesso sfondo bianco, nessun divider */}
        <Hero />
        <Stats />
        <Divider />
        <Servizi />

        <Preventa />
        <Divider />

        <Problema />
        <Divider />

        <DiagnosiCRO />
        <Divider />

        <AscoltaBene />
        <Divider />

        <MetodoAPSOC />
        <Divider />

        <FunnelViz />
        <Divider />

        <Processo />
        <Divider />

        <Stack />
        <Divider />

        <Portfolio />
        <Divider />

        <ProveNovacar />
        <Divider />

        <ChiSiamo />
        <Divider />

        <PerChi />
        <Divider />

        <Testimonial />
        <CarteScoperte />
        <Divider />

        <Garanzia />
        <Divider />

        <Objections />
        <Divider />

        <FAQSection />
        <Divider />

        <CTAFinale />
      </main>

      <Footer />

      <StickyCTA />
    </>
  );
}
