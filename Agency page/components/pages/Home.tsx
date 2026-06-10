
import React from 'react';
import { Hero } from '../Hero';
import { FunnelComparison } from '../FunnelComparison';
import { Services } from '../Services';
import { HowWeWork } from '../HowWeWork';
import { WebDesignShowcase } from '../WebDesignShowcase';
import { Philosophy } from '../Philosophy';
import { ObjectionFlow } from '../ObjectionFlow';
import { CroFunnelSection } from '../CroFunnelSection';
import { Trust } from '../Trust';
import { Contact } from '../Contact';
import { Newsletter } from '../Newsletter';
import { ScientificProofs } from '../ScientificProofs';
import { LuxDividerGreen } from '../ui/LuxDividerGreen';
import { LuxDividerGreenBottom } from '../ui/LuxDividerGreenBottom';
import { LuxThickDivider } from '../ui/LuxThickDivider';

interface HomeProps {
  onOpenSecretDashboard: () => void;
}

export const Home: React.FC<HomeProps> = ({ onOpenSecretDashboard }) => {
  return (
    <div className="relative w-full bg-black">
      
      {/* GLOBAL HOME GRAIN OVERLAY - DEEP ATMOSPHERE (NO LIGHT SPOT) */}
      <div className="fixed inset-0 w-full h-full pointer-events-none z-0">
          
          {/* Layer 1: Base Nero Assoluto */}
          <div className="absolute inset-0 bg-[#000000]"></div>

          {/* Layer 2: Deep Void Purple Atmosphere (Darker & Diffused) */}
          <div 
            className="absolute inset-0 opacity-60"
            style={{
                background: 'radial-gradient(circle at 50% 50%, #1a0024 0%, #0a0012 40%, #000000 80%)'
            }}
          />

          {/* Layer 3: Heavy Film Grain (High Fidelity) */}
          <div 
            className="absolute inset-0 opacity-[0.45]" 
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%)',
                mixBlendMode: 'overlay' 
            }} 
          />
          
          {/* Layer 4: Digital Crisp Noise */}
          <div 
            className="absolute inset-0 opacity-[0.3] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '100px 100px', 
                filter: 'contrast(180%) brightness(40%)'
            }}
          />
      </div>

      <div className="relative z-10">
        <Hero onOpenSecretDashboard={onOpenSecretDashboard} />
        
        {/* Comparison Section (Old vs Chaos vs Solution) */}
        <FunnelComparison />

        {/* NARRATIVE FLOW: Hero -> Comparison -> CroFunnel (Merged Hope + CRO) -> HowWeWork -> Services */}
        <CroFunnelSection />
        
        <LuxThickDivider />
        
        <HowWeWork />
        
        <LuxThickDivider />

        <ScientificProofs />
        
        <LuxThickDivider />
        
        <Services />
        
        <WebDesignShowcase />
        
        {/* SEZIONE VISIONE */}
        <Philosophy />
        
        <ObjectionFlow />
        
        <LuxDividerGreen />
        
        <Trust />

        <LuxDividerGreenBottom />

        <Contact />
        <Newsletter />
      </div>
    </div>
  );
};
