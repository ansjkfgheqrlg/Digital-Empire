
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, TrendingDown, ShoppingCart, BarChart2, AlertTriangle } from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';

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

         {/* --- THE INFINITY RING REMOVED --- */}

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

            {/* 2. SUB-HEADLINE (UPDATED LAYOUT) */}
            <motion.div
               initial={{ opacity: 0, y: 20 }}
               animate={{ opacity: 1, y: 0 }}
               transition={{ duration: 1, delay: 0.4 }}
               className="relative z-20 mt-4 mb-8 max-w-5xl px-4"
            >
               {/* Sub-headline text and button container */}
               <div className="flex flex-col md:flex-row items-center justify-center gap-6 mb-6">
                  <p className="text-gray-400 text-base md:text-lg font-light leading-relaxed tracking-wide lowercase text-center md:text-left">
                     Misuriamo dove perdi clienti. Pratichiamo il c.r.o. (conversion rate optimization).
                     <br className="hidden md:block" />
                     <span className="text-white font-medium">Analizziamo il tuo funnel</span> = Miglioriamo il tasso di conversione di ogni step.
                  </p>

                  {/* CTA BUTTON (moved here) */}
                  <div className="shrink-0">
                     <GoldButton href="#contact" className="px-8 py-3 text-[10px] tracking-[0.2em] shadow-[0_0_30px_rgba(253,185,19,0.15)]">
                        esegui protocollo crescita
                        <ArrowRight size={14} />
                     </GoldButton>
                  </div>
               </div>

               {/* Collaboration message below */}
               <div className="inline-block bg-white/5 border border-white/10 px-6 py-2 rounded-full backdrop-blur-sm">
                  <span className="text-[10px] md:text-xs text-gray-300 tracking-widest font-mono lowercase">
                     collaboriamo solo con chi possiamo <span className="text-white font-bold">veramente aiutare</span>.
                  </span>
               </div>
            </motion.div>

            {/* 4. PRECISION/RESULTS TEXT */}


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

               <div className="flex flex-col items-center gap-2 mt-2">
                  <span className="text-3xl md:text-5xl lg:text-6xl font-sans font-light text-gray-400 lowercase">
                     Continua a leggere.
                  </span>

                  <p className="text-sm md:text-base font-sans font-light text-gray-400 lowercase">
                     (nel peggiore dei casi ne uscirai con del valore in più)
                  </p>
               </div>
            </motion.div>

         </div>

         {/* Secret Trigger Area */}
         <div onClick={onOpenSecretDashboard} className="absolute bottom-10 left-10 w-4 h-4 rounded-full cursor-default z-50 opacity-0 hover:opacity-100 transition-opacity" />
      </section>
   );
};
