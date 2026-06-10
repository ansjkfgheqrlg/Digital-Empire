
import React from 'react';
import { motion } from 'framer-motion';

const MotionDiv = motion.div as any;

export const FunnelComparison: React.FC = () => {
  
  return (
    <section className="relative py-32 bg-transparent overflow-hidden">
      
      {/* 
          REMOVED LOCAL BACKGROUND TO ENSURE CONTINUITY 
          The section now relies on the fixed global background defined in Home.tsx
      */}

      <div className="container mx-auto px-4 relative z-10 flex flex-col items-center gap-24">

        {/* --- PART 1: THE OLD FUNNEL (CLEAN SMOOTH GOLD) --- */}
        <div className="flex flex-col items-center w-full max-w-lg">
            <h3 className="text-2xl md:text-3xl font-sans font-light text-white mb-8 lowercase tracking-wide">
               alcuni fanno questo <span className="font-bold text-[#FDE68A]">funnel...</span>
            </h3>
            
            <MotionDiv 
               initial={{ opacity: 0, y: 20 }}
               whileInView={{ opacity: 1, y: 0 }}
               viewport={{ once: true }}
               className="w-full h-[300px] relative drop-shadow-2xl"
            >
                <svg viewBox="0 0 400 300" className="w-full h-full overflow-visible">
                    <defs>
                        {/* CLEAN SMOOTH GOLD GRADIENT - NO HARD LINES */}
                        <linearGradient id="cleanGold" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stopColor="#FFFBEB" />   {/* Very Light Gold/White */}
                            <stop offset="30%" stopColor="#FDE68A" />  {/* Bright Gold */}
                            <stop offset="100%" stopColor="#D97706" /> {/* Deep Gold/Orange */}
                        </linearGradient>
                        <filter id="goldGlow" x="-50%" y="-50%" width="200%" height="200%">
                            <feDropShadow dx="0" dy="4" stdDeviation="6" floodColor="rgba(212,175,55,0.4)" />
                        </filter>
                    </defs>

                    {/* Step 1: Wide Trapezoid */}
                    <path d="M 20,0 L 380,0 L 320,80 L 80,80 Z" fill="url(#cleanGold)" filter="url(#goldGlow)" stroke="rgba(255,255,255,0.4)" strokeWidth="1" />
                    <text x="200" y="50" textAnchor="middle" fill="#2A1805" fontSize="22" fontWeight="900" fontFamily="sans-serif" letterSpacing="1" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.3)'}}>STEP 1</text>
                    
                    {/* Arrow Down */}
                    <path d="M 185,85 L 215,85 L 200,105 Z" fill="#FDE68A" filter="drop-shadow(0 0 5px rgba(253, 230, 138, 0.5))" />

                    {/* Step 2: Medium Trapezoid */}
                    <path d="M 80,110 L 320,110 L 280,190 L 120,190 Z" fill="url(#cleanGold)" filter="url(#goldGlow)" stroke="rgba(255,255,255,0.4)" strokeWidth="1" />
                    <text x="200" y="160" textAnchor="middle" fill="#2A1805" fontSize="22" fontWeight="900" fontFamily="sans-serif" letterSpacing="1" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.3)'}}>STEP 2</text>

                    {/* Arrow Down */}
                    <path d="M 185,195 L 215,195 L 200,215 Z" fill="#FDE68A" filter="drop-shadow(0 0 5px rgba(253, 230, 138, 0.5))" />

                    {/* Step 3: Narrow Trapezoid */}
                    <path d="M 120,220 L 280,220 L 240,300 L 160,300 Z" fill="url(#cleanGold)" filter="url(#goldGlow)" stroke="rgba(255,255,255,0.4)" strokeWidth="1" />
                    <text x="200" y="270" textAnchor="middle" fill="#2A1805" fontSize="22" fontWeight="900" fontFamily="sans-serif" letterSpacing="1" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.3)'}}>STEP 3</text>
                </svg>
            </MotionDiv>
        </div>

        {/* --- PART 2: THE CHAOS (CLEAN SMOOTH SILVER) --- */}
        <div className="flex flex-col items-center w-full max-w-3xl">
            <h3 className="text-2xl md:text-3xl font-sans font-light text-gray-400 mb-8 lowercase tracking-wide">
               ...e altri fanno <span className="font-bold text-white">questo...</span>
            </h3>

            <MotionDiv 
               initial={{ opacity: 0, scale: 0.95 }}
               whileInView={{ opacity: 1, scale: 1 }}
               viewport={{ once: true }}
               className="w-full h-[400px] relative"
            >
                <svg viewBox="0 0 600 400" className="w-full h-full overflow-visible">
                    <defs>
                        {/* CLEAN SMOOTH SILVER GRADIENT - NO HARD LINES */}
                        <linearGradient id="cleanSilver" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stopColor="#FFFFFF" />    {/* Pure White Top */}
                            <stop offset="40%" stopColor="#E2E8F0" />  {/* Light Grey Middle */}
                            <stop offset="100%" stopColor="#94A3B8" /> {/* Cool Grey Bottom */}
                        </linearGradient>
                        
                        <filter id="crispShadow" x="-50%" y="-50%" width="200%" height="200%">
                            <feDropShadow dx="0" dy="4" stdDeviation="4" floodColor="rgba(0,0,0,0.5)" />
                        </filter>
                    </defs>

                    {/* CONNECTIONS (Brighter Dashed Lines) */}
                    <g stroke="#94A3B8" strokeWidth="1.5" strokeDasharray="5 5" fill="none" opacity="0.6">
                        <path d="M 100,50 L 300,100" />
                        <path d="M 300,100 L 500,50" />
                        <path d="M 300,100 L 300,200" />
                        <path d="M 300,200 L 150,250" />
                        <path d="M 300,200 L 450,250" />
                        <path d="M 150,250 L 300,350" />
                        <path d="M 450,250 L 300,350" />
                        <path d="M 500,50 L 450,250" />
                        <path d="M 100,50 L 150,250" />
                    </g>

                    {/* NODES (Rectangles with Clean Gradient) */}
                    {/* Top Row */}
                    <g filter="url(#crispShadow)">
                        <rect x="50" y="30" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="100" y="55" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>ENTRATA 1</text>

                        <rect x="250" y="80" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="300" y="105" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>STEP 1</text>

                        <rect x="450" y="30" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="500" y="55" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>ENTRATA 2</text>
                    </g>

                    {/* Middle Row */}
                    <g filter="url(#crispShadow)">
                        <rect x="250" y="180" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="300" y="205" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>STEP 2</text>
                    </g>

                    {/* Complex Side Steps */}
                    <g filter="url(#crispShadow)">
                        <rect x="100" y="230" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="150" y="255" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>STEP 4</text>

                        <rect x="400" y="230" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="450" y="255" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>STEP A</text>
                    </g>

                    {/* Bottom */}
                    <g filter="url(#crispShadow)">
                        <rect x="250" y="330" width="100" height="40" rx="6" fill="url(#cleanSilver)" stroke="#FFFFFF" strokeWidth="1" />
                        <text x="300" y="355" textAnchor="middle" fill="#000000" fontSize="11" fontWeight="900" fontFamily="sans-serif" style={{textShadow: '0px 1px 0px rgba(255,255,255,0.5)'}}>STEP 5</text>
                    </g>

                </svg>
            </MotionDiv>
        </div>

        {/* --- PART 3: THE SOLUTION (GLOWING GOLD TEXT) --- */}
        <div className="flex flex-col items-center text-center mt-12 w-full">
            <p className="text-xl md:text-2xl font-serif italic text-gray-500 mb-6 lowercase">
                e poi c'è chi fa questo:
            </p>
            
            <MotionDiv
                initial={{ opacity: 0, scale: 0.8 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                className="relative"
            >
                {/* 
                    UPDATED: Reduced glow intensity for a more professional look.
                    Was blur-[60px] bg-gold-500/30 -> blur-[80px] bg-gold-500/5 
                */}
                <div className="absolute inset-0 blur-[80px] bg-gold-500/5 rounded-full pointer-events-none"></div>
                
                {/* 
                    UPDATED: Toned down brightness.
                    - text-white -> text-gray-200 (softer white)
                    - drop-shadow reduced radius and intensity (no neon bloom)
                    - gold gradient darkened slightly at top and bottom for richer metal look
                */}
                <h1 className="relative font-sans font-black text-5xl md:text-7xl lg:text-9xl tracking-tighter text-gray-200 drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] lowercase leading-none">
                    quello che <br className="md:hidden" /> <span className="text-transparent bg-clip-text bg-gradient-to-b from-[#FAE8B6] via-[#D4AF37] to-[#855F23]">funziona.</span>
                </h1>
            </MotionDiv>

            {/* --- NEW COPY BLOCK (STRATEGY CHECKLIST) --- */}
            <MotionDiv
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                className="mt-24 max-w-4xl mx-auto flex flex-col items-center gap-12"
            >
                <h4 className="text-xl md:text-3xl text-gray-200 font-light leading-relaxed">
                    Perché non venderai solo perché il funnel è lungo... O corto. <br className="hidden md:block"/>
                    Venderai <span className="font-bold text-white">solo</span> se strategizzi:
                </h4>

                <div className="flex flex-col items-start gap-6 pl-4 md:pl-0">
                    <div className="flex items-center gap-4">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                             <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                        </div>
                        <span className="text-xl md:text-2xl text-white font-light">Il funnel <span className="font-bold">giusto</span></span>
                    </div>
                    <div className="flex items-center gap-4">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                             <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                        </div>
                        <span className="text-xl md:text-2xl text-white font-light">Nel momento <span className="font-bold">giusto</span></span>
                    </div>
                    <div className="flex items-center gap-4">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                             <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                        </div>
                        <span className="text-xl md:text-2xl text-white font-light">Per le persone <span className="font-bold">giuste</span></span>
                    </div>
                </div>

                <div className="text-center space-y-4 pt-4 px-4">
                    <p className="text-xl md:text-3xl text-white font-medium leading-snug">
                        Talmente tante aziende devono ancora capire questo concetto...
                    </p>
                    <p className="text-lg md:text-xl text-gray-400 font-light leading-relaxed">
                        Che ho creato questa pagina per <span className="font-bold text-white border-b border-white/30 pb-0.5">avvisarti</span>, prima che sia troppo tardi.
                    </p>
                </div>
            </MotionDiv>
        </div>

      </div>
    </section>
  );
};
