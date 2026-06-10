
import React from 'react';
import { motion } from 'framer-motion';

const MotionDiv = motion.div as any;

export const HopeSection: React.FC = () => {
  
  // GRADIENTI BRAND
  const silverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 50%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.3))'
  };

  const goldGradient = {
    backgroundImage: 'linear-gradient(180deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(212,175,55,0.3))'
  };

  return (
    <section className="py-24 relative overflow-hidden bg-[#0a0a0a] border-y border-white/5">
      
      {/* Background Texture Sottile */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none opacity-20" />
      
      <div className="container mx-auto px-6 relative z-10">
        <div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center justify-center gap-12 md:gap-16">
           
           {/* --- ICONA VISUALE (Fingers Crossed + X) --- */}
           <MotionDiv 
             initial={{ opacity: 0, scale: 0.8, rotate: -10 }}
             whileInView={{ opacity: 1, scale: 1, rotate: 0 }}
             viewport={{ once: true }}
             className="relative flex-shrink-0"
           >
              {/* Contenitore Vetro */}
              <div className="w-40 h-40 bg-white/[0.03] backdrop-blur-xl border border-white/10 rounded-3xl flex items-center justify-center shadow-[0_0_50px_rgba(0,0,0,0.5)] relative overflow-hidden group">
                  
                  {/* Glow interno */}
                  <div className="absolute inset-0 bg-gradient-to-tr from-gold-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

                  {/* Emoji fingers crossed (Resa metallica/Grayscale via CSS) */}
                  <span className="text-7xl grayscale brightness-150 contrast-125 opacity-80" style={{ filter: 'grayscale(100%) drop-shadow(0 0 10px rgba(255,255,255,0.2))' }}>
                    🤞
                  </span>

                  {/* La X Barrata (Brand Gold) */}
                  <div className="absolute inset-0 flex items-center justify-center">
                      <svg viewBox="0 0 100 100" className="w-full h-full p-6 drop-shadow-[0_0_15px_rgba(0,0,0,0.8)]">
                         <line x1="20" y1="20" x2="80" y2="80" stroke="url(#goldX)" strokeWidth="8" strokeLinecap="round" />
                         <line x1="80" y1="20" x2="20" y2="80" stroke="url(#goldX)" strokeWidth="8" strokeLinecap="round" />
                         <defs>
                            <linearGradient id="goldX" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stopColor="#FDE68A" />
                                <stop offset="50%" stopColor="#D4AF37" />
                                <stop offset="100%" stopColor="#B45309" />
                            </linearGradient>
                         </defs>
                      </svg>
                  </div>
              </div>
           </MotionDiv>

           {/* --- TESTO (Minuscolo e stilizzato) --- */}
           <div className="text-center md:text-left">
              <MotionDiv
                initial={{ opacity: 0, x: 20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
              >
                  <h2 className="font-serif text-3xl md:text-5xl lg:text-6xl font-black tracking-tight leading-[1.1] mb-6 lowercase">
                      <span style={silverGradient as any}>la speranza non è una </span>
                      <span style={goldGradient as any} className="underline decoration-gold-500/30 underline-offset-8">strategia</span>.
                  </h2>
                  
                  <p className="font-sans text-gray-400 text-lg md:text-xl font-light leading-relaxed max-w-2xl lowercase">
                      incrociare le dita e sperare che il cliente acquisti non ti porterà da <span className="text-white font-bold border-b border-white/20 pb-0.5">nessuna parte</span>.
                  </p>
              </MotionDiv>
           </div>

        </div>
      </div>
    </section>
  );
};
