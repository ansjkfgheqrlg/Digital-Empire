
import React from 'react';
import { motion } from 'framer-motion';

const MotionDiv = motion.div as any;
const MotionPath = motion.path as any;

export const SocialFunnelSection: React.FC = () => {
  
  // Marker Color Palette
  const MARKER_BLUE = "#3b82f6"; // Electric Blue Marker
  const MARKER_WHITE = "#e5e7eb"; // Chalk White
  const MARKER_GOLD = "#fbbf24"; // Gold Highlight

  return (
    <section className="py-24 md:py-32 relative overflow-hidden bg-[#0a0a0a] border-b border-white/5 min-h-[900px] flex items-center justify-center">
      
      {/* --- BACKGROUND: CLEAN DARK TEXTURE --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#0a0a0a]">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,#111_0%,#000_100%)]" />
          {/* Subtle noise for paper texture feel */}
          <div className="absolute inset-0 opacity-[0.15] bg-[url('https://grainy-gradients.vercel.app/noise.svg')] mix-blend-overlay"></div>
      </div>

      <div className="container mx-auto px-4 relative z-10 w-full max-w-7xl">
        
        {/* TITOLO SEZIONE: Professional & Simple - LOWERCASE */}
        <div className="text-center mb-24">
             <h2 className="text-4xl md:text-6xl font-serif text-white font-medium tracking-tight lowercase">
                ecosistema <span className="italic font-light text-gray-400">c.r.o.</span>
             </h2>
        </div>

        {/* --- MAPPA "PENNARELLO" (HAND DRAWN STYLE) --- */}
        <div className="relative w-full max-w-5xl mx-auto h-[600px] hidden lg:block">

            {/* SVG CANVAS FOR HAND-DRAWN LINES */}
            <svg className="absolute inset-0 w-full h-full pointer-events-none z-0 overflow-visible">
               <defs>
                 <filter id="markerRoughness">
                   <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" result="noise" />
                   <feDisplacementMap in="SourceGraphic" in2="noise" scale="2" />
                 </filter>
                 <marker id="arrowBlue" markerWidth="12" markerHeight="12" refX="10" refY="4" orient="auto">
                   <path d="M0,0 L12,4 L0,8" fill="none" stroke={MARKER_BLUE} strokeWidth="2" strokeLinecap="round" />
                 </marker>
                 <marker id="arrowGold" markerWidth="12" markerHeight="12" refX="10" refY="4" orient="auto">
                   <path d="M0,0 L12,4 L0,8" fill="none" stroke={MARKER_GOLD} strokeWidth="2" strokeLinecap="round" />
                 </marker>
               </defs>

               {/* 1. LEFT TO CENTER (Data -> CRO) */}
               <MotionPath
                  d="M 250,220 Q 350,220 420,220"
                  fill="none"
                  stroke={MARKER_WHITE}
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeDasharray="10 10"
                  markerEnd="url(#arrowBlue)"
                  initial={{ pathLength: 0, opacity: 0 }}
                  whileInView={{ pathLength: 1, opacity: 0.5 }}
                  transition={{ duration: 1.5, ease: "easeInOut" }}
               />

               {/* 2. CENTER TO RIGHT (CRO -> Funnel) */}
               <MotionPath
                  d="M 680,220 Q 750,220 820,220"
                  fill="none"
                  stroke={MARKER_WHITE}
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeDasharray="10 10"
                  markerEnd="url(#arrowBlue)"
                  initial={{ pathLength: 0, opacity: 0 }}
                  whileInView={{ pathLength: 1, opacity: 0.5 }}
                  transition={{ duration: 1.5, ease: "easeInOut", delay: 0.5 }}
               />

               {/* 3. FUNNEL CURVE DOWN (Funnel -> Profit) */}
               <MotionPath
                  d="M 900,320 C 900,450 700,500 550,520"
                  fill="none"
                  stroke={MARKER_BLUE}
                  strokeWidth="3"
                  strokeLinecap="round"
                  markerEnd="url(#arrowBlue)"
                  filter="url(#markerRoughness)"
                  initial={{ pathLength: 0, opacity: 0 }}
                  whileInView={{ pathLength: 1, opacity: 1 }}
                  transition={{ duration: 2, ease: "easeInOut", delay: 1 }}
               />
               
               {/* 4. UNDERLINE "GUADAGNO" */}
               <MotionPath
                  d="M 380,580 Q 500,590 620,575"
                  fill="none"
                  stroke={MARKER_GOLD}
                  strokeWidth="4"
                  strokeLinecap="round"
                  filter="url(#markerRoughness)"
                  initial={{ pathLength: 0, opacity: 0 }}
                  whileInView={{ pathLength: 1, opacity: 1 }}
                  transition={{ duration: 1, ease: "easeOut", delay: 2 }}
               />

            </svg>

            {/* --- ELEMENTS (MARKER TEXT) --- */}
            
            {/* 1. LEFT: DATI */}
            <div className="absolute top-[150px] left-[50px] w-[250px] text-center rotate-[-2deg]">
                <MotionDiv 
                  initial={{ opacity: 0, scale: 0.8 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.5 }}
                >
                    <p className="font-hand text-xl text-gray-400 mb-0 lowercase">analizzare i</p>
                    <h3 className="font-marker text-6xl text-blue-500 drop-shadow-[0_0_15px_rgba(59,130,246,0.4)] lowercase">
                        dati
                    </h3>
                    <div className="mt-4 font-hand text-lg text-gray-300 text-left leading-tight pl-4 border-l-2 border-gray-700 lowercase">
                        <p>• heatmaps</p>
                        <p>• user recordings</p>
                        <p>• drop-off points</p>
                    </div>
                </MotionDiv>
            </div>

            {/* 2. CENTER: C.R.O. */}
            <div className="absolute top-[120px] left-1/2 -translate-x-1/2 w-[300px] text-center z-10">
                <MotionDiv 
                   initial={{ opacity: 0, y: 20 }}
                   whileInView={{ opacity: 1, y: 0 }}
                   transition={{ duration: 0.5, delay: 0.3 }}
                   className="relative"
                >
                    {/* SVG Circle Draw around CRO */}
                    <svg className="absolute inset-0 w-full h-full -top-4 -left-4 w-[120%] h-[140%] pointer-events-none overflow-visible">
                       <MotionPath 
                          d="M 20,40 Q 150,-20 280,40 Q 300,100 150,140 Q 0,100 20,40"
                          fill="none"
                          stroke="white"
                          strokeWidth="2"
                          strokeOpacity="0.2"
                          strokeLinecap="round"
                          initial={{ pathLength: 0 }}
                          whileInView={{ pathLength: 1 }}
                          transition={{ duration: 2, delay: 0.5 }}
                       />
                    </svg>

                    <h3 className="font-marker text-8xl text-white tracking-widest drop-shadow-2xl lowercase">
                        c.r.o.
                    </h3>
                    <p className="font-hand text-xl text-blue-400 mt-2 lowercase">
                        conversion rate <span className="font-bold">optimization</span>
                    </p>
                    <p className="font-hand text-sm text-gray-500 mt-2 italic max-w-[200px] mx-auto lowercase">
                        "la <span className="font-bold">scienza</span> di vendere di <span className="font-bold">più</span> allo stesso traffico"
                    </p>
                </MotionDiv>
            </div>

            {/* 3. RIGHT: FUNNEL */}
            <div className="absolute top-[150px] right-[50px] w-[280px] text-center rotate-[2deg]">
                <MotionDiv 
                  initial={{ opacity: 0, scale: 0.8 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.5, delay: 0.6 }}
                >
                    <p className="font-hand text-xl text-gray-400 mb-0 lowercase">ottimizzare il</p>
                    <h3 className="font-marker text-6xl text-blue-500 drop-shadow-[0_0_15px_rgba(59,130,246,0.4)] lowercase">
                        funnel
                    </h3>
                    
                    {/* Handwritten List */}
                    <div className="mt-6 font-hand text-left space-y-2 bg-white/5 p-4 rounded-lg border border-white/5 rotate-[-1deg] lowercase">
                        <div className="flex justify-between items-center text-white text-lg">
                           <span>step 1: <span className="font-bold">ads</span></span>
                           <span className="text-green-400 font-bold">3.2%</span>
                        </div>
                        <div className="w-full h-[2px] bg-gray-700"></div>
                        <div className="flex justify-between items-center text-white text-lg">
                           <span>step 2: <span className="font-bold">page</span></span>
                           <span className="text-green-400 font-bold">12%</span>
                        </div>
                        <div className="w-full h-[2px] bg-gray-700"></div>
                        <div className="flex justify-between items-center text-white text-lg">
                           <span>step 3: <span className="font-bold">sale</span></span>
                           <span className="text-green-400 font-bold">8%</span>
                        </div>
                    </div>
                </MotionDiv>
            </div>

            {/* 4. BOTTOM: RESULT */}
            <div className="absolute top-[500px] left-1/2 -translate-x-1/2 w-[400px] text-center">
                <MotionDiv 
                   initial={{ opacity: 0, y: 20 }}
                   whileInView={{ opacity: 1, y: 0 }}
                   transition={{ duration: 0.5, delay: 1.5 }}
                >
                    <h3 className="font-marker text-5xl md:text-6xl text-white mb-2 lowercase">
                        guadagno <span className="text-gold-500">netto</span>
                    </h3>
                    <p className="font-hand text-lg text-gray-400 lowercase">
                        risultato <span className="font-bold">matematico</span> inevitabile
                    </p>
                </MotionDiv>
            </div>

        </div>

        {/* --- MOBILE STACKED VIEW --- */}
        <div className="lg:hidden flex flex-col items-center gap-12 lowercase">
            
            {/* Block 1 */}
            <div className="text-center">
               <p className="font-hand text-lg text-gray-400">1. analisi</p>
               <h3 className="font-marker text-5xl text-blue-500 mb-4">dati</h3>
               <div className="font-hand text-gray-400 text-sm">
                  heatmaps &bull; recordings &bull; metrics
               </div>
            </div>

            <div className="text-gray-600">↓</div>

            {/* Block 2 */}
            <div className="text-center relative p-8 border-2 border-dashed border-white/10 rounded-full">
               <h3 className="font-marker text-6xl text-white">c.r.o.</h3>
               <p className="font-hand text-blue-400">optimization core</p>
            </div>

            <div className="text-gray-600">↓</div>

            {/* Block 3 */}
            <div className="text-center w-full max-w-xs">
               <p className="font-hand text-lg text-gray-400">2. ottimizzazione</p>
               <h3 className="font-marker text-5xl text-blue-500 mb-4">funnel</h3>
               <div className="bg-white/5 p-4 rounded font-hand text-white text-left space-y-2">
                  <div className="flex justify-between"><span>ads</span> <span>3.2%</span></div>
                  <div className="flex justify-between"><span>page</span> <span>12%</span></div>
                  <div className="flex justify-between"><span>sale</span> <span>8%</span></div>
               </div>
            </div>

            <div className="text-blue-500 text-2xl">↓</div>

            {/* Block 4 */}
            <div className="text-center">
               <h3 className="font-marker text-4xl text-white">guadagno <span className="text-gold-500">netto</span></h3>
            </div>

        </div>

      </div>
    </section>
  );
};
