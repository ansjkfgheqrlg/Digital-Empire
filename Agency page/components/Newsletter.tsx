
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Loader2, Check } from 'lucide-react';

const MotionDiv = motion.div as any;

export const Newsletter: React.FC = () => {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success'>('idle');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    
    setStatus('loading');
    
    // Simulate API call
    setTimeout(() => {
      setStatus('success');
      setEmail('');
    }, 1500);
  };

  return (
    <section className="py-40 bg-transparent relative overflow-hidden flex flex-col items-center justify-center min-h-[70vh] border-t border-gray-900">
      
      {/* --- VORTEX GRID BACKGROUND --- */}
      <div className="absolute inset-0 pointer-events-none">
        <div 
            className="absolute inset-0 opacity-20"
            style={{
                backgroundImage: `
                    linear-gradient(to right, #333 1px, transparent 1px),
                    linear-gradient(to bottom, #333 1px, transparent 1px)
                `,
                backgroundSize: '50px 50px',
                transform: 'perspective(500px) rotateX(60deg) scale(2.5)',
                transformOrigin: 'top center',
                maskImage: 'radial-gradient(circle at 50% 50%, black 0%, transparent 80%)'
            }}
        />
        {/* RIMOSSO: Horizon Light (Luce accanto alla linea) */}
      </div>

      <div className="container mx-auto px-4 relative z-10 w-full max-w-lg flex flex-col items-center">
        
        {/* --- 3D ENVELOPE --- */}
        <MotionDiv 
          initial={{ y: 20, opacity: 0 }}
          whileInView={{ y: 0, opacity: 1 }}
          transition={{ duration: 1 }}
          className="relative mb-8 w-64 h-40 md:w-80 md:h-48 perspective-1000"
        >
            <MotionDiv
               animate={{ y: [-10, 10, -10], rotateX: [5, 0, 5] }}
               transition={{ duration: 6, ease: "easeInOut", repeat: Infinity }}
               className="w-full h-full relative preserve-3d"
            >
                <div className="absolute inset-0 bg-[#111]/90 backdrop-blur-sm border border-gray-800 rounded-sm shadow-2xl"></div>
                
                <div 
                    className="absolute top-0 left-0 w-full h-full z-20 origin-top"
                    style={{
                        clipPath: 'polygon(0 0, 100% 0, 50% 60%)',
                        background: 'linear-gradient(to bottom, #222, #0a0a0a)',
                        borderTop: '1px solid rgba(255,255,255,0.1)'
                    }}
                ></div>
                
                <div 
                    className="absolute inset-0 z-10"
                    style={{
                        background: 'linear-gradient(135deg, #050505 0%, #151515 100%)',
                        clipPath: 'polygon(0 0, 50% 50%, 100% 0, 100% 100%, 0 100%)',
                        border: '1px solid #333'
                    }}
                ></div>

                <div className="absolute top-[35%] right-[20%] z-30 w-12 h-12 md:w-16 md:h-16 bg-black-900 rounded-full border-2 border-gold-500 shadow-[0_0_20px_rgba(253,185,19,0.3)] flex items-center justify-center">
                    <div className="absolute inset-1 border border-dashed border-gold-500/50 rounded-full animate-spin-slow"></div>
                    <span className="font-serif font-black text-lg md:text-xl text-gold-500">234</span>
                </div>

                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-gold-500/5 blur-3xl -z-10"></div>
            </MotionDiv>
        </MotionDiv>

        {/* --- INPUT BAR --- */}
        <MotionDiv 
            initial={{ width: "80%", opacity: 0 }}
            whileInView={{ width: "100%", opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="w-full relative group"
        >
            <form onSubmit={handleSubmit} className="relative w-full h-14 bg-[#0a0a0a]/80 backdrop-blur-md border border-gray-800 rounded-md flex items-center shadow-[0_10px_30px_rgba(0,0,0,0.5)] overflow-hidden transition-colors hover:border-gray-700 focus-within:border-gold-500/50">
                <input 
                    type="email" 
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                    className="flex-grow bg-transparent text-gray-300 font-mono text-sm px-6 h-full focus:outline-none placeholder-gray-600"
                    disabled={status === 'loading' || status === 'success'}
                />
                <button 
                    type="submit"
                    disabled={status === 'loading' || status === 'success'}
                    className="px-6 h-full text-gray-400 font-mono text-sm hover:text-gold-500 transition-colors flex items-center gap-2 border-l border-gray-800 bg-black-900/80 hover:bg-white/5"
                >
                    {status === 'loading' ? (
                        <Loader2 className="animate-spin w-4 h-4" />
                    ) : status === 'success' ? (
                        <span className="text-green-500 flex items-center gap-2"><Check size={14}/> Joined</span>
                    ) : (
                        <span>Join waitlist</span>
                    )}
                </button>
                <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/10 to-transparent pointer-events-none"></div>
            </form>
            <div className="absolute -bottom-4 left-0 right-0 h-4 bg-gradient-to-b from-gold-500/5 to-transparent blur-md opacity-0 group-focus-within:opacity-100 transition-opacity duration-500"></div>
            <div className="mt-6 text-center">
                 <p className="text-[10px] text-gray-600 font-mono tracking-widest uppercase">
                    Accesso Limitato &bull; Digital Empire Inner Circle
                 </p>
            </div>
        </MotionDiv>
      </div>
    </section>
  );
};
