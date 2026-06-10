
import React from 'react';
import { motion } from 'framer-motion';
import { Scale, Zap, Crown, Binary, ChevronRight } from 'lucide-react';

const MotionDiv = motion.div as any;
const MotionH2 = motion.h2 as any;

export const Philosophy: React.FC = () => {

   const pillars = [
      {
         icon: Binary,
         title: "ossessione numerica",
         desc: "Nel marketing, l'opinione è irrilevante. Contano solo i dati. Non 'pensiamo' che una campagna funzionerà. Lo sappiamo perché l'abbiamo testata matematicamente.",
         stat: "data-driven",
         color: "text-blue-400",
         border: "group-hover:border-blue-500/50"
      },
      {
         icon: Zap,
         title: "esecuzione militare",
         desc: "La strategia perfetta senza esecuzione vale zero. I nostri protocolli sono progettati per lanciare, testare e scalare alla velocità della luce, lasciando la concorrenza ferma a pianificare.",
         stat: "velocity",
         color: "text-gold-500",
         border: "group-hover:border-gold-500/50"
      },
      {
         icon: Crown,
         title: "sovranità digitale",
         desc: "Non affittiamo il tuo successo a piattaforme terze. Costruiamo asset proprietari (database, brand, infrastruttura) che nessuno può toglierti.",
         stat: "ownership",
         color: "text-emerald-400",
         border: "group-hover:border-emerald-500/50"
      }
   ];

   return (
      <section id="philosophy" className="relative pt-0 pb-24 md:pb-32 bg-[#020202]">

         {/* --- BACKGROUND TEXTURE CLEAN --- */}
         <div className="absolute inset-0 w-full h-full pointer-events-none z-0">
            <div className="absolute inset-0 bg-[#020202]"></div>
            {/* Grana fine e controllata - ULTRA QUALITY */}
            <div
               className="absolute inset-0 opacity-[0.45]"
               style={{
                  backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                  filter: 'contrast(150%) brightness(130%)',
                  mixBlendMode: 'overlay'
               }}
            />
            {/* Seconda layer di grana per profondità */}
            <div
               className="absolute inset-0 opacity-[0.2]"
               style={{
                  backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                  mixBlendMode: 'soft-light'
               }}
            />
            {/* Subtle Grid per dare struttura ingegneristica */}
            <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px] opacity-20" />
         </div>

         <div className="container mx-auto px-6 relative z-10 max-w-7xl">

            {/* --- HEADER MANIFESTO --- */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-end mb-20 gap-8 border-b border-white/10 pb-12">
               <div className="max-w-2xl">
                  <MotionDiv
                     initial={{ opacity: 0, x: -20 }}
                     whileInView={{ opacity: 1, x: 0 }}
                     viewport={{ once: true }}
                     className="flex items-center gap-3 mb-6"
                  >
                     <div className="w-2 h-2 bg-gold-500 rounded-full animate-pulse shadow-[0_0_10px_rgba(234,179,8,0.5)]"></div>
                     <span className="font-mono text-xs text-gold-500 uppercase tracking-[0.3em] font-bold lowercase">visione 2025</span>
                  </MotionDiv>

                  <MotionH2
                     initial={{ opacity: 0, y: 20 }}
                     whileInView={{ opacity: 1, y: 0 }}
                     viewport={{ once: true }}
                     className="font-serif text-4xl md:text-6xl text-white font-medium leading-[1.1] lowercase"
                  >
                     il <span className="font-bold">successo</span> non è <br />
                     una <span className="font-bold">lotteria</span>. <br />
                     <span className="text-gray-500 font-light">È ingegneria.</span>
                  </MotionH2>
               </div>

               <MotionDiv
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ delay: 0.2 }}
                  className="max-w-xs"
               >
                  <p className="text-gray-400 text-sm leading-relaxed font-mono border-l-2 border-white/10 pl-4">
                     <span className="block text-white/60 mb-1 text-[10px] uppercase">// status: classified</span>
                     Abbiamo eliminato la variabile "fortuna" dall'equazione.
                     Costruiamo sistemi <span className="text-white font-bold">deterministici</span> che producono risultati prevedibili.
                  </p>
               </MotionDiv>
            </div>

            {/* --- 3 PILLARS (CLEAN & PROFESSIONAL) --- */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
               {pillars.map((pillar, idx) => (
                  <MotionDiv
                     key={idx}
                     initial={{ opacity: 0, y: 30 }}
                     whileInView={{ opacity: 1, y: 0 }}
                     viewport={{ once: true }}
                     transition={{ delay: idx * 0.1 }}
                     className="group relative p-10 rounded-xl transition-all duration-500 overflow-hidden shadow-xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.02]"
                  >
                     <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                     <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                     <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                     <div className="flex justify-between items-start mb-8 relative z-10">
                        <div className="p-3 bg-slate-900 border border-slate-700 rounded-lg text-white">
                           <pillar.icon size={28} strokeWidth={1.5} />
                        </div>
                        <span className="font-mono text-[10px] uppercase tracking-widest font-black text-red-600 bg-red-50 px-2 py-1 rounded border border-red-100 lowercase">
                           {pillar.stat}
                        </span>
                     </div>

                     <h3 className="text-2xl text-slate-900 font-serif mb-4 lowercase font-bold relative z-10">
                        {pillar.title}
                     </h3>

                     <p className="text-slate-700 text-sm leading-relaxed font-medium lowercase relative z-10">
                        {pillar.desc}
                     </p>

                     <div className="mt-8 pt-6 border-t border-slate-900/10 flex items-center justify-between relative z-10">
                        <span className="text-[10px] text-slate-500 font-mono uppercase tracking-wider font-bold lowercase">protocollo <span className="text-red-700 font-black">attivo</span></span>
                        <ChevronRight size={14} className="text-red-600" />
                     </div>
                  </MotionDiv>
               ))}
            </div>

            {/* --- BOTTOM QUOTE (AUTHORITY) --- */}
            <div className="mt-20 text-center">
               <MotionDiv
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  className="inline-block relative p-10 md:p-14 border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] rounded-2xl shadow-2xl overflow-hidden"
               >
                  <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                  <Scale size={32} className="text-slate-900 mx-auto mb-8 relative z-10" strokeWidth={1.5} />
                  <p className="font-serif text-xl md:text-3xl text-slate-800 italic max-w-4xl mx-auto leading-relaxed relative z-10">
                     "Nel caos del mercato digitale, vince chi ha il sistema più <span className="font-bold not-italic text-slate-900">ordinato</span>.
                     Noi portiamo <span className="text-red-700 not-italic font-black border-b-2 border-red-200">ordine, logica e profitto</span> dove gli altri portano solo confusione."
                  </p>
                  <div className="mt-8 font-mono text-[10px] text-slate-500 tracking-[0.2em] font-bold lowercase relative z-10">
                     digital empire manifesto &bull; v.2025
                  </div>
               </MotionDiv>
            </div>

         </div>
      </section>
   );
};
