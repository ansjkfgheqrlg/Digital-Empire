import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Hero } from '../home/Hero';
import { AreaSelector } from '../home/AreaSelector';
import { AiProblemDiagnostics } from '../home/ai/AiProblemDiagnostics';
import { AiEducation } from '../home/ai/AiEducation';
import { AiTruthSection } from '../home/ai/AiTruthSection';
import { AiHowWeWork } from '../home/ai/AiHowWeWork';
import { AiServices } from '../home/ai/AiServices';
import { AiObjections } from '../home/ai/AiObjections';
import { CroHeroBottom } from '../home/CroHeroBottom';
import { FunnelComparison } from '../home/FunnelComparison';
import { Services } from '../home/Services';
import { HowWeWork } from '../home/HowWeWork';
import { WebDesignShowcase } from '../home/WebDesignShowcase';

import { CroFunnelSection } from '../home/CroFunnelSection';
import { Trust } from '../home/Trust';
import { WhyUs } from '../home/WhyUs';
import { Contact } from '../home/Contact';
import { Newsletter } from '../home/Newsletter';
import { ScientificProofs } from '../home/ScientificProofs';
import { LuxDividerGreen } from '../ui/LuxDividerGreen';
import { LuxDividerGreenBottom } from '../ui/LuxDividerGreenBottom';
import { LuxThickDivider } from '../ui/LuxThickDivider';
import { CosmicBackground } from '../ui/CosmicBackground';

import { ObjectionCPB } from '../home/ObjectionCPB';
import { ObjectionCPB_Checkout } from '../home/ObjectionCPB_Checkout';
import { ObjectionCPB_Website } from '../home/ObjectionCPB_Website';
import { ObjectionCPB_WordOfMouth } from '../home/ObjectionCPB_WordOfMouth';
import { ObjectionCPB_Time } from '../home/ObjectionCPB_Time';

interface HomeProps {
  onOpenSecretDashboard: () => void;
}

export const Home: React.FC<HomeProps> = ({ onOpenSecretDashboard }) => {
  const [activeArea, setActiveArea] = useState<'CRO' | 'AI' | null>(null);

  return (
    <div className="relative w-full bg-black">
      <CosmicBackground />

      <div className="relative z-10">
        <Hero onOpenSecretDashboard={onOpenSecretDashboard} />
        <AreaSelector activeArea={activeArea} onSelectArea={setActiveArea} />

        {activeArea === 'CRO' && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <CroHeroBottom />
            <FunnelComparison />
            <CroFunnelSection />
            <LuxThickDivider />
            <HowWeWork />
            <LuxThickDivider />
            <ScientificProofs />
            <LuxThickDivider />
            <Services />
            <LuxThickDivider />

            {/* Objection CPB Sections */}
            <ObjectionCPB />
            <ObjectionCPB_Checkout />
            <ObjectionCPB_Website />
            <ObjectionCPB_WordOfMouth />
            <ObjectionCPB_Time />

            <LuxDividerGreen />
            <WhyUs />
            <Trust />
            <LuxDividerGreenBottom />
            <Contact />
            <Newsletter />
          </motion.div>
        )}

        {activeArea === 'AI' && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <AiProblemDiagnostics />
            <AiEducation />
            <AiTruthSection />
            <LuxThickDivider />
            <AiHowWeWork />
            <LuxThickDivider />
            <AiServices />
            <LuxThickDivider />
            <AiObjections />

            <LuxDividerGreen />
            <WhyUs />
            <Trust />
            <LuxDividerGreenBottom />
            <Contact />
            <Newsletter />
          </motion.div>
        )}
      </div>
    </div>
  );
};
