
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import { GoldButton } from './ui/GoldButton';

interface HeroProps {
  onOpenSecretDashboard?: () => void;
}

export const Hero: React.FC<HeroProps> = ({ onOpenSecretDashboard }) => {
  
  // 1. ULTRA-SHARP "WHITE GOLD & PLATINUM" (Line 1)
  const seamlessLuxuryGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 45%, #FDE68A 50%, #D4AF37 75%, #FFF7ED 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 4px 1px rgba(0,0,0,0.9)) drop-shadow(0px 0px 30px rgba(253, 230, 138, 0.15))',
  };

  // 2. REVERSE PLATINUM MIX (Line 2)
  const goldToSilverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FCD34D 0%, #FDE68A 30%, #F1F5F9 55%, #FFFFFF 85%, #E2E8F0 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 4px 1px rgba(0,0,0,0.9)) drop-shadow(0px 0px 30px rgba(253, 230, 138, 0.15))',
  };

  // 4. SIZE CLASSES
  const unifiedSizeClass = "text-[1.8rem] sm:text-[3rem] md:text-[4.2rem] lg:text-[5.2rem] xl:text-[6.2rem] leading-[1.1] tracking-tighter pb-2";

  return (
    // ADJUSTED HEIGHT: min-h-[150vh] instead of 220vh since modules are gone
    // REDUCED PADDING BOTTOM to 0 to seamlessly connect with next section
    <section id="hero" className="relative w-full min-h-[150vh] flex flex-col items-center pt-32 md:pt-48 pb-0 overflow-hidden">
      
      {/* --- THE INFINITY RING --- */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.8, x: "-50%", y: 0 }}
        animate={{ opacity: 1, scale: 1, x: "-50%", y: 0 }}
        transition={{ duration: 2, ease: "easeOut", delay: 0.2 }}
        className="absolute left-1/2 pointer-events-none z-10 top-[420px] md:top-[560px]" 
        style={{ width: '2200px', height: '2200px' }}
      >
          <svg className="w-full h-full overflow-visible" viewBox="0 0 100 100">
            <defs>
              <linearGradient id="phosphorGoldSilver" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="#896628" />
                <stop offset="20%" stopColor="#F9F1D0" /> 
                <stop offset="40%" stopColor="#FFFFFF" /> 
                <stop offset="60%" stopColor="#F9F1D0" />
                <stop offset="80%" stopColor="#D4AF37" />
                <stop offset="100%" stopColor="#896628" />
              </linearGradient>
              
              <filter id="intenseLuminosity" x="-100%" y="-100%" width="300%" height="300%">
                 <feGaussianBlur in="SourceGraphic" stdDeviation="0.4" result="blur1" />
                 <feGaussianBlur in="SourceGraphic" stdDeviation="1.0" result="blur2" />
                 <feMerge>
                    <feMergeNode in="blur2" />
                    <feMergeNode in="blur1" />
                    <feMergeNode in="SourceGraphic" />
                 </feMerge>
              </filter>
            </defs>
            <circle 
              cx="50" cy="50" r="49.5" 
              stroke="url(#phosphorGoldSilver)" 
              strokeWidth="0.25" 
              fill="none" 
              filter="url(#intenseLuminosity)"
              className="drop-shadow-[0_0_8px_rgba(255,255,255,0.8)] drop-shadow-[0_0_30px_rgba(253,224,71,0.4)]" 
              style={{ strokeLinecap: 'round', opacity: 1 }}
            />
          </svg>
      </motion.div>

      <div className="relative z-20 w-full px-2 text-center max-w-[100vw] mx-auto flex flex-col items-center">
        
        {/* 1. HEADLINE BLOCK */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1.2, ease: "circOut" }}
          className="relative z-20 w-full flex flex-col items-center select-none mb-4"
        >
            <div className="flex flex-row flex-wrap justify-center gap-x-2 md:gap-x-4 w-full items-baseline">
               <h1 style={seamlessLuxuryGradient as any} className={`${unifiedSizeClass} font-sans font-light mb-0 lowercase`}>digital empire:</h1>
               <span style={seamlessLuxuryGradient as any} className={`${unifiedSizeClass} font-sans font-black lowercase`}>ingegneria</span>
            </div>
            <div className="flex flex-row flex-wrap justify-center gap-x-2 md:gap-x-4 w-full items-baseline -mt-1 md:-mt-4">
               <span style={goldToSilverGradient as any} className={`${unifiedSizeClass} font-sans font-light lowercase`}>strategica</span>
               <span style={goldToSilverGradient as any} className={`${unifiedSizeClass} font-sans font-light lowercase`}>per la</span>
               <span style={goldToSilverGradient as any} className={`${unifiedSizeClass} font-sans font-black lowercase`}>tua scalata</span>
            </div>
        </motion.div>

        {/* 2. SUB-HEADLINE (RESTORED) */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.4 }}
          className="relative z-20 mt-8 mb-8 max-w-3xl text-center px-4"
        >
           <p className="text-gray-400 text-sm md:text-base font-light leading-relaxed tracking-wide lowercase">
              misuriamo dove perdi clienti. pratichiamo il c.r.o. (conversion rate optimization).
              <br className="hidden md:block" />
              <span className="text-white font-medium">analizziamo il tuo funnel</span> = miglioriamo il tasso di conversione di ogni step.
           </p>
           
           <div className="mt-6 inline-block bg-white/5 border border-white/10 px-6 py-2 rounded-full backdrop-blur-sm">
              <span className="text-[10px] md:text-xs text-gray-300 tracking-widest font-mono lowercase">
                 collaboriamo solo con chi possiamo <span className="text-white font-bold">veramente aiutare</span>.
              </span>
           </div>
        </motion.div>

        {/* 3. CTA BUTTON */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.6 }}
          className="relative z-20 mt-12 mb-12"
        >
          <GoldButton href="#contact" className="px-8 py-3 text-[10px] tracking-[0.2em] shadow-[0_0_30px_rgba(253,185,19,0.15)]">
             esegui protocollo crescita
             <ArrowRight size={14} />
          </GoldButton>
        </motion.div>

        {/* 4. PRECISION/RESULTS TEXT */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1.5, delay: 0.8 }}
          className="flex items-center gap-12 text-[10px] md:text-xs font-mono tracking-[0.3em] lowercase text-gray-500 relative z-20 mt-4"
        >
           <span className="hover:text-white transition-colors cursor-default font-black">precisione</span>
           <span className="text-[#D4C596] animate-pulse">•</span>
           <span className="hover:text-white transition-colors cursor-default font-light">risultati</span>
           <span className="text-[#D4C596] animate-pulse">•</span>
           <span className="hover:text-white transition-colors cursor-default font-bold">asset</span>
        </motion.div>

        {/* --- 5. NEW TEXT BLOCK (Refined Typography) --- */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 1.2, delay: 0.5 }}
          className="relative z-20 mt-32 max-w-4xl px-6 flex flex-col items-center text-center gap-6"
        >
             <h3 className="font-sans text-2xl md:text-4xl leading-tight md:leading-[1.3] font-light tracking-wide text-gray-400 lowercase">
                più <span className="text-white font-bold">resti</span> in questa pagina, <br className="hidden md:block" />
                più <span className="text-white font-bold">scorri</span> questa pagina, <br className="hidden md:block" />
                più <span className="text-transparent bg-clip-text bg-gradient-to-b from-white via-white to-gray-300 font-bold drop-shadow-lg">acquisisci formazione</span>.
             </h3>

             <div className="flex flex-col items-center gap-4 mt-2">
                 <span className="text-xl md:text-2xl font-serif text-white italic border-b border-white/20 pb-1">
                    continua a leggere.
                 </span>
                 
                 <p className="text-[10px] md:text-xs font-mono text-gold-500 uppercase tracking-[0.2em] font-bold opacity-80 mt-2">
                    (nel peggiore dei casi ne uscirai con del valore in più)
                 </p>
             </div>
        </motion.div>

        {/* --- 6. PROBLEM AWARENESS BLOCK --- */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 1.2, delay: 0.7 }}
          className="relative z-20 mt-32 mb-24 max-w-4xl px-6 w-full text-left mx-auto"
        >
             <h3 className="font-sans text-3xl md:text-5xl font-bold tracking-tighter text-white drop-shadow-2xl mb-10 leading-none md:whitespace-nowrap">
                Conosciamo già il tuo problema
             </h3>

             <div className="space-y-8 text-lg md:text-xl text-gray-300 font-light leading-relaxed">
                <div>
                   <p className="mb-4">Stai pagando traffico ads su <span className="text-white font-bold">Meta</span>, ma:</p>
                   <ul className="space-y-2 pl-6 border-l-2 border-gold-500/30 ml-2">
                      <li className="flex items-center gap-3">
                         <span className="w-1.5 h-1.5 bg-white rounded-full flex-shrink-0"></span>
                         le richieste non arrivano
                      </li>
                      <li className="flex items-center gap-3">
                         <span className="w-1.5 h-1.5 bg-white rounded-full flex-shrink-0"></span>
                         i form restano a metà
                      </li>
                      <li className="flex items-center gap-3">
                         <span className="w-1.5 h-1.5 bg-white rounded-full flex-shrink-0"></span>
                         i visitatori spariscono prima della CTA
                      </li>
                   </ul>
                </div>

                <p>
                   Non è il “servizio” il problema: è il <span className="text-white font-bold">percorso cliente (Funnel)</span> che perde conversioni nei punti caldi.
                </p>

                <p>
                   Ogni giorno di attesa è <span className="text-gold-500 font-bold">budget sprecato</span>.
                </p>
             </div>
        </motion.div>

        {/* --- 7. SOLUTION/FUNNEL EXPLANATION BLOCK (UPDATED: REMOVED TEXT) --- */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 1.2, delay: 0.2 }}
          className="relative z-20 mt-12 mb-20 w-full max-w-6xl px-6"
        >
             <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">
                
                {/* LEFT: TEXT EXPLANATION */}
                <div className="text-left space-y-8">
                    <div>
                        {/* 
                           REMOVED: "architettura della soluzione", "il tuo business", "necessita di un"
                           Kept: The main headline "funnel vincente" for context
                        */}
                        
                        <h3 className="font-sans text-white leading-[0.9] mb-8">
                           {/* FUNNEL: GOLD METAL GRADIENT */}
                           <span className="block text-6xl md:text-7xl lg:text-8xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-b from-[#FDE68A] via-[#D4AF37] to-[#B45309] lowercase drop-shadow-[0_0_30px_rgba(212,175,55,0.3)]">
                             funnel
                           </span>
                           
                           {/* VINCENTE: SOLID STRUCTURE */}
                           <span className="block text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter text-white lowercase drop-shadow-2xl">
                             vincente.
                           </span>
                        </h3>
                    </div>

                    <div className="text-lg text-gray-400 font-light leading-relaxed space-y-6 lowercase">
                        <p>
                           la parola "funnel" viene spesso abusata. ecco la definizione tecnica definitiva:
                        </p>
                        <p className="border-l-2 border-white/20 pl-6 italic text-gray-300">
                           "un funnel è un <strong className="text-white">setaccio digitale strutturato</strong>. è un percorso obbligato che filtra il traffico caotico (visitatori casuali) e lo raffina passo dopo passo, fino a isolare solo l'oro puro: i clienti paganti."
                        </p>
                    </div>

                    <div className="space-y-4 pt-4">
                        <div className="flex items-start gap-4">
                            <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-white/10 shrink-0 text-white font-serif font-bold">1</div>
                            <div>
                               <h4 className="text-white font-bold text-sm uppercase tracking-wide lowercase">attrarre (top of funnel)</h4>
                               <p className="text-sm text-gray-500 mt-1 lowercase">catturiamo l'attenzione nel mercato freddo con ads chirurgiche.</p>
                            </div>
                        </div>
                        <div className="flex items-start gap-4">
                            <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-white/10 shrink-0 text-white font-serif font-bold">2</div>
                            <div>
                               <h4 className="text-white font-bold text-sm uppercase tracking-wide lowercase">educare (middle of funnel)</h4>
                               <p className="text-sm text-gray-500 mt-1 lowercase">costruiamo fiducia automatica smontando le obiezioni.</p>
                            </div>
                        </div>
                        <div className="flex items-start gap-4">
                            <div className="w-8 h-8 rounded-full bg-gold-900/40 flex items-center justify-center border border-gold-500/50 shrink-0 text-gold-500 font-serif font-bold">3</div>
                            <div>
                               <h4 className="text-gold-500 font-bold text-sm uppercase tracking-wide lowercase">convertire (bottom of funnel)</h4>
                               <p className="text-sm text-gray-500 mt-1 lowercase">presentiamo l'offerta irresistibile al momento esatto.</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* RIGHT: VISUAL GRAPHIC (UPDATED: LOWERCASE) */}
                <div className="relative h-[500px] flex items-center justify-center">
                    {/* Background Glow */}
                    <div className="absolute inset-0 bg-gold-500/5 blur-[100px] rounded-full pointer-events-none"></div>

                    {/* THE FUNNEL SVG */}
                    <svg viewBox="0 0 400 500" className="w-full h-full drop-shadow-2xl overflow-visible">
                        <defs>
                           <linearGradient id="glassGradient" x1="0" y1="0" x2="1" y2="1">
                              <stop offset="0%" stopColor="rgba(255,255,255,0.1)" />
                              <stop offset="100%" stopColor="rgba(255,255,255,0.02)" />
                           </linearGradient>
                           <linearGradient id="goldLiquid" x1="0" y1="0" x2="0" y2="1">
                              <stop offset="0%" stopColor="#FDE68A" />
                              <stop offset="100%" stopColor="#B45309" />
                           </linearGradient>
                           <filter id="glow">
                              <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
                              <feMerge>
                                  <feMergeNode in="coloredBlur"/>
                                  <feMergeNode in="SourceGraphic"/>
                              </feMerge>
                           </filter>
                        </defs>

                        {/* STAGE 1: TRAFFIC (Top) */}
                        <motion.path 
                           d="M 20,20 L 380,20 L 320,150 L 80,150 Z" 
                           fill="url(#glassGradient)" 
                           stroke="rgba(255,255,255,0.2)" 
                           strokeWidth="1"
                           initial={{ opacity: 0, y: -20 }}
                           whileInView={{ opacity: 1, y: 0 }}
                           transition={{ duration: 1 }}
                        />
                        <text x="200" y="90" textAnchor="middle" fill="white" fontSize="12" fontFamily="monospace" letterSpacing="2" opacity="0.6" className="lowercase">traffico (ads)</text>

                        {/* STAGE 2: NURTURING (Middle) */}
                        <motion.path 
                           d="M 90,160 L 310,160 L 260,300 L 140,300 Z" 
                           fill="url(#glassGradient)" 
                           stroke="rgba(255,255,255,0.3)" 
                           strokeWidth="1"
                           initial={{ opacity: 0, scale: 0.9 }}
                           whileInView={{ opacity: 1, scale: 1 }}
                           transition={{ duration: 1, delay: 0.3 }}
                        />
                        <text x="200" y="240" textAnchor="middle" fill="white" fontSize="12" fontFamily="monospace" letterSpacing="2" opacity="0.8" className="lowercase">educazione</text>

                        {/* STAGE 3: CONVERSION (Bottom - Gold) */}
                        <motion.path 
                           d="M 150,310 L 250,310 L 250,450 L 150,450 Z" 
                           fill="url(#goldLiquid)" 
                           stroke="#FDE68A" 
                           strokeWidth="2"
                           filter="url(#glow)"
                           initial={{ opacity: 0, pathLength: 0 }}
                           whileInView={{ opacity: 1, pathLength: 1 }}
                           transition={{ duration: 1.5, delay: 0.6 }}
                        />
                         <text x="200" y="380" textAnchor="middle" fill="#2A2312" fontSize="14" fontFamily="serif" fontWeight="bold" letterSpacing="1" className="lowercase">vendita</text>

                        {/* PARTICLES FLOWING */}
                        {[...Array(5)].map((_, i) => (
                           <motion.circle 
                              key={i}
                              r="3"
                              fill="#FDE68A"
                              initial={{ x: 200, y: 20, opacity: 0 }}
                              animate={{ 
                                 y: [20, 400], 
                                 opacity: [0, 1, 0],
                                 x: [200 + (Math.random() * 200 - 100), 200] // Start wide, end narrow
                              }}
                              transition={{ 
                                 duration: 2 + Math.random(), 
                                 repeat: Infinity, 
                                 delay: Math.random() * 2,
                                 ease: "easeInOut"
                              }}
                           />
                        ))}
                    </svg>
                </div>

             </div>
        </motion.div>

      </div>
      
      {/* Secret Trigger Area */}
      <div onClick={onOpenSecretDashboard} className="absolute bottom-10 left-10 w-4 h-4 rounded-full cursor-default z-50 opacity-0 hover:opacity-100 transition-opacity" />
    </section>
  );
};
