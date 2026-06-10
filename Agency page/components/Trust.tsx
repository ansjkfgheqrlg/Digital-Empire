
import React from 'react';
import { motion } from 'framer-motion';
import { Phone, ShieldCheck, Clock, AlertCircle, Sparkles, TrendingUp, CheckCircle2 } from 'lucide-react';
import { GoldButton } from './ui/GoldButton';

const MotionDiv = motion.div as any;

export const Trust: React.FC = () => {
  return (
    <section id="trust" className="py-24 md:py-32 relative overflow-hidden">
      
      {/* --- HIGH FIDELITY GRAIN BACKGROUND --- */}
      <div className="absolute inset-0 w-full h-full pointer-events-none z-0">
          
          {/* Layer 1: Base Deep Green (Restored) */}
          <div className="absolute inset-0 bg-[#031c16]"></div>

          {/* Layer 2: Heavy Film Grain (Texture Principale) */}
          <div 
            className="absolute inset-0 opacity-[0.4]" 
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(350%) brightness(100%)',
                mixBlendMode: 'overlay' 
            }} 
          />
          
          {/* Layer 3: Digital High-Frequency Noise */}
          <div 
            className="absolute inset-0 opacity-[0.3] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.7' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '100px 100px', 
                filter: 'contrast(160%) brightness(50%)'
            }}
          />

          {/* Subtle Grid for Tech Feel */}
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:60px_60px] opacity-10" />
      </div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-16 lg:gap-24">
          
          {/* Left Column: The Provocation */}
          <div className="lg:w-1/2">
            <MotionDiv
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <div className="inline-flex items-center gap-2 px-4 py-1.5 border border-emerald-500/20 rounded-sm bg-[#021410]/60 mb-8 backdrop-blur-md shadow-lg">
                 <AlertCircle size={14} className="text-emerald-400 animate-pulse" />
                 <span className="text-emerald-400 text-[10px] font-mono font-black tracking-[0.3em] uppercase">Security Protocol: High Scrutiny</span>
              </div>
              
              <h2 className="font-serif text-4xl md:text-7xl text-white mb-8 leading-[0.9] font-black tracking-tighter drop-shadow-lg">
                IL TUO DUBBIO <br/>
                È IL NOSTRO <br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-200 via-emerald-400 to-white">MIGLIORE ALLEATO.</span>
              </h2>
              
              <div className="space-y-8 text-emerald-100/70 max-w-xl">
                <p className="text-lg leading-relaxed italic border-l-2 border-emerald-500/30 pl-6">
                  "Siamo d'accordo: là fuori è pieno di improvvisati che vendono fumo. <strong className="text-white">Il tuo scetticismo è segno di intelligenza.</strong> Noi non vogliamo convincerti a parole, vogliamo dimostrartelo con i fatti."
                </p>
                
                <div className="grid grid-cols-2 gap-6 pt-4">
                   <div className="p-4 border border-emerald-500/10 bg-emerald-950/20 backdrop-blur-sm rounded-lg hover:border-emerald-500/30 transition-colors">
                      <div className="text-emerald-400 font-black text-2xl mb-1">0%</div>
                      <div className="text-[10px] uppercase tracking-widest text-emerald-200/60">Rischio Finanziario</div>
                   </div>
                   <div className="p-4 border border-emerald-500/10 bg-emerald-950/20 backdrop-blur-sm rounded-lg hover:border-emerald-500/30 transition-colors">
                      <div className="text-emerald-400 font-black text-2xl mb-1">100%</div>
                      <div className="text-[10px] uppercase tracking-widest text-emerald-200/60">Trasparenza Dati</div>
                   </div>
                </div>
              </div>
            </MotionDiv>
          </div>

          {/* Right Column: THE EMERALD/SILVER VIP CARD */}
          <div className="lg:w-1/2 w-full perspective-2000">
            <MotionDiv 
              initial={{ opacity: 0, scale: 0.9, rotateY: 10 }}
              whileInView={{ opacity: 1, scale: 1, rotateY: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.8, type: "spring" }}
              className="relative overflow-hidden shadow-[0_50px_100px_rgba(0,0,0,0.8)] border border-emerald-500/20 group rounded-2xl"
              style={{
                // DARK EMERALD GRADIENT BACKGROUND - Adjusted to blend better with the section
                background: `linear-gradient(165deg, #022c22 0%, #031c16 100%)`,
              }}
            >
              {/* --- CARD LAYERS --- */}
              {/* Animated Sheen */}
              <MotionDiv 
                  animate={{ left: ['-100%', '200%'] }}
                  transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", repeatDelay: 2 }}
                  className="absolute inset-y-0 w-1/2 opacity-20 pointer-events-none z-10"
                  style={{
                    background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent)',
                    transform: 'skewX(-25deg)',
                  }}
              />
              {/* Noise Texture */}
              <div className="absolute inset-0 opacity-[0.15] pointer-events-none z-0 mix-blend-overlay" style={{ backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")' }} />
              
              {/* Top Highlight Border */}
              <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-emerald-400 to-transparent z-20 opacity-50" />

              <div className="relative z-20 p-8 md:p-12">
                <div className="flex flex-col items-center text-center mb-10">
                   {/* Badge */}
                   <div className="inline-block bg-gradient-to-r from-emerald-900 to-emerald-950 border border-emerald-500/30 text-emerald-400 font-black px-4 py-1.5 rounded-sm text-[10px] uppercase tracking-[0.4em] mb-6 shadow-xl">
                      Invito Esclusivo
                   </div>
                   
                   {/* Title */}
                   <h3 className="font-serif text-3xl md:text-5xl text-white font-black tracking-tighter leading-none mb-4 drop-shadow-md">
                      SESSIONE STRATEGICA <br/> GRATUITA
                   </h3>
                   
                   {/* Divider */}
                   <div className="w-24 h-[1px] bg-gradient-to-r from-transparent via-emerald-500/50 to-transparent mb-6"></div>
                   
                   {/* Price/Value */}
                   <p className="text-emerald-200/60 font-mono text-xs font-bold uppercase tracking-widest">
                      VALORE REALE: <span className="line-through decoration-red-500/50 decoration-2">€500</span> &bull; PER TE: <span className="text-white underline underline-offset-4 decoration-emerald-500">€0</span>
                   </p>
                </div>

                <div className="space-y-4 mb-10">
                  {/* Feature 1 */}
                  <div className="flex items-start gap-5 p-5 bg-black/20 border border-emerald-500/10 rounded-xl backdrop-blur-sm transition-all hover:bg-black/40 hover:border-emerald-500/30 group/item">
                    <div className="w-10 h-10 bg-emerald-950/50 rounded flex items-center justify-center flex-shrink-0 border border-emerald-500/20 group-hover/item:border-emerald-500/50 transition-colors">
                      <Clock className="text-emerald-400 w-5 h-5" />
                    </div>
                    <div>
                      <h4 className="text-white font-black text-sm uppercase tracking-wide mb-1">40 Minuti di Consulenza Pura</h4>
                      <p className="text-gray-400 text-xs leading-relaxed font-medium">Analizziamo il tuo ecosistema attuale e individuiamo i colli di bottiglia che ti impediscono di scalare.</p>
                    </div>
                  </div>

                  {/* Feature 2 */}
                  <div className="flex items-start gap-5 p-5 bg-black/20 border border-emerald-500/10 rounded-xl backdrop-blur-sm transition-all hover:bg-black/40 hover:border-emerald-500/30 group/item">
                    <div className="w-10 h-10 bg-emerald-950/50 rounded flex items-center justify-center flex-shrink-0 border border-emerald-500/20 group-hover/item:border-emerald-500/50 transition-colors">
                      <ShieldCheck className="text-emerald-400 w-5 h-5" />
                    </div>
                    <div>
                      <h4 className="text-white font-black text-sm uppercase tracking-wide mb-1">Garanzia "Zero Rischio"</h4>
                      <p className="text-gray-400 text-xs leading-relaxed font-medium">Se senti di aver perso tempo, ti inviamo comunque un piano d'azione personalizzato in PDF.</p>
                    </div>
                  </div>
                </div>

                {/* Status Bar */}
                <div className="bg-emerald-950/30 p-3 rounded-lg mb-8 border border-emerald-500/10 text-center relative overflow-hidden">
                  <div className="flex items-center justify-center gap-2">
                    <span className="relative flex h-2 w-2">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2 w-2 bg-red-500"></span>
                    </span>
                    <p className="text-emerald-100 text-[10px] font-black uppercase tracking-[0.2em]">
                      Solo 3 slot disponibili questa settimana
                    </p>
                  </div>
                </div>

                {/* CTA Button */}
                <GoldButton fullWidth href="#contact" variant="silverGreen" className="py-5 shadow-[0_0_30px_rgba(5,150,105,0.3)]">
                  <div className="flex items-center gap-3">
                    <Sparkles size={16} />
                    BLOCCA IL TUO SLOT ORA
                  </div>
                </GoldButton>

                {/* Footer Micro-copy */}
                <div className="mt-6 flex flex-col items-center gap-2 opacity-40 hover:opacity-100 transition-opacity">
                   <p className="text-center text-white text-[9px] font-bold uppercase tracking-[0.3em]">
                     Nessun obbligo d'acquisto &bull; Solo business
                   </p>
                </div>
              </div>
            </MotionDiv>
          </div>
        </div>
      </div>
    </section>
  );
};
