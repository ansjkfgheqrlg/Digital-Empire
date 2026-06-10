"use client";

import { Navbar } from "@/components/Navbar";
import { ArrowRight, Sparkles, Zap, Shield } from "lucide-react";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <>
      <Navbar />

      {/* --- BACKGROUND LAYER --- */}
      <div className="fixed inset-0 bg-[#050505] -z-20" />
      


      <main className="flex flex-col items-center justify-center pt-48 px-4 sm:px-8 pb-32">
        


        {/* Headline */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: [0.16, 1, 0.3, 1], delay: 0.1 }}
          className="text-center max-w-5xl mx-auto mb-8 flex flex-col items-center"
        >
          <h1 className="text-6xl md:text-9xl font-black tracking-tighter text-silver-white leading-[0.8] pb-6 overflow-visible">
            LandingForge.
          </h1>
          <h1 className="text-6xl md:text-9xl font-serif italic text-neon-purple leading-[0.8] -mt-6 md:-mt-10 pb-4 overflow-visible">
            Conversione Pura.
          </h1>
        </motion.div>




        {/* Subheadline */}
        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
          className="text-lg md:text-xl text-zinc-500 max-w-3xl text-center mb-16 font-medium leading-relaxed"
        >
          LandingForge è l&apos;ecosistema definitivo che trasforma la complessità in <strong className="text-zinc-300">risultati concreti</strong>. Grazie all&apos;intelligenza artificiale, puoi generare e ottimizzare le tue pagine in <strong className="text-zinc-300">pochi secondi</strong>, eliminando ogni barriera tra il tuo prodotto e i tuoi <strong className="text-zinc-300">nuovi clienti</strong>.
        </motion.p>


        {/* --- HERO INTERACTIVE SECTION (THE CONNECTOR) --- */}
        <div className="relative w-full flex flex-col items-center" style={{ isolation: 'isolate' }}>

          {/* ── LIGHT ENGINE (sits at z=1, BELOW the button at z=2) ── */}
          <div
            className="absolute left-1/2 -translate-x-1/2 pointer-events-none"
            style={{
              top: '18px',       /* vertically centered on the button */
              width: '700px',
              height: '700px',
              zIndex: 1,
              background: [
                'radial-gradient(ellipse 30% 15% at 50% 10%, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%)',
                'radial-gradient(ellipse 60% 50% at 50% 15%, rgba(168,85,247,0.95) 0%, rgba(168,85,247,0) 100%)',
              ].join(', '),
            }}
          />

          {/* ── EMAIL FORM (z=2 so it covers the top half of the light) ── */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.5 }}
            className="relative w-full max-w-lg"
            style={{ zIndex: 2 }}
          >
            <div className="rounded-full p-2.5 flex items-center justify-between border border-white/15 bg-[#0d0d10] backdrop-blur-2xl">
              <input 
                type="email" 
                placeholder="Inserisci la tua Email" 
                className="bg-transparent border-none outline-none text-white px-6 w-full placeholder:text-zinc-600 font-medium"
              />
              <button className="bg-white text-black font-black uppercase tracking-tighter text-sm rounded-full py-4 px-8 flex items-center gap-2 hover:bg-zinc-200 transition-all active:scale-[0.98] group">
                Join Waitlist 
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </button>
            </div>
          </motion.div>

          {/* ── CHANNEL SPACER (light shines through, z=1) ── */}
          <div className="relative w-full" style={{ height: '160px', zIndex: 1, marginTop: '-4px' }}>
            {/* animated drip */}
            <motion.div
              animate={{ y: [0, 180], opacity: [0, 1, 0] }}
              transition={{ duration: 1.1, repeat: Infinity, ease: "easeIn", repeatDelay: 0.4 }}
              style={{
                position: 'absolute',
                top: 0,
                left: '50%',
                transform: 'translateX(-50%)',
                width: '6px',
                height: '80px',
                borderRadius: '999px',
                background: 'linear-gradient(to bottom, white, rgba(192,132,252,0))',
                filter: 'blur(4px)',
              }}
            />
          </div>

          {/* ── DASHBOARD MOCKUP (z=2) ── */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.99 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1.2, delay: 1 }}
            className="relative w-full max-w-6xl mx-auto"
            style={{
              aspectRatio: '16/9',
              zIndex: 2,
              marginTop: '-120px',
              borderRadius: '36px',
              /* Unified neon wrap: same purple as the light column above */
              boxShadow: [
                '0 0 0 2px rgba(255,255,255,0.8)',
                '0 0 0 6px rgba(168,85,247,1)',
                '0 0 30px 8px rgba(168,85,247,1)',
                '0 0 80px 25px rgba(168,85,247,0.6)',
                '0 0 160px 50px rgba(168,85,247,0.3)',
              ].join(', '),
            }}
          >
            {/* opaque dark base so content shows correctly */}
            <div className="absolute inset-0 rounded-[34px] bg-[#080809]" style={{ zIndex: 0 }} />






            <div className="relative w-full h-full glass-premium rounded-[32px] overflow-hidden bg-[#0a0a0a] border-white/10 p-1 flex flex-col">
              {/* Fake UI Browser Bar */}
              <div className="h-14 border-b border-white/5 flex items-center px-6 gap-6 bg-white/[0.02]">
                <div className="flex gap-2.5">
                  <div className="w-3.5 h-3.5 rounded-full bg-zinc-800 border border-white/5" />
                  <div className="w-3.5 h-3.5 rounded-full bg-zinc-800 border border-white/5" />
                  <div className="w-3.5 h-3.5 rounded-full bg-zinc-800 border border-white/5" />
                </div>
                <div className="flex-1 max-w-md">
                   <div className="bg-white/5 border border-white/5 px-4 py-1.5 rounded-lg text-[10px] font-bold tracking-widest text-zinc-500 uppercase flex items-center gap-2">
                     <Shield className="w-3 h-3" /> landingforge.io/dashboard/v2
                   </div>
                </div>
                <div className="flex items-center gap-4">
                   <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-primary to-secondary" />
                </div>
              </div>
              
              {/* Fake UI Content */}
              <div className="flex-1 p-10 grid grid-cols-12 gap-8 overflow-hidden">
                <div className="col-span-3 space-y-6">
                  <div className="h-4 w-24 bg-white/10 rounded-full" />
                  <div className="space-y-4">
                    {[1, 2, 3, 4, 5].map(i => (
                      <div key={i} className="h-12 w-full glass rounded-2xl border-white/5 flex items-center px-4 gap-3">
                         <div className="w-4 h-4 bg-white/5 rounded-md" />
                         <div className="h-2 w-full bg-white/5 rounded-full" />
                      </div>
                    ))}
                  </div>
                </div>
                <div className="col-span-9 space-y-8">
                   <div className="grid grid-cols-3 gap-6">
                      {[1, 2, 3].map(i => (
                        <div key={i} className="h-40 glass-premium rounded-[24px] border-white/10 p-6 flex flex-col justify-between">
                           <div className="flex justify-between items-start">
                             <div className="w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center">
                                <Zap className="w-5 h-5 text-primary" />
                             </div>
                             <div className="w-2 h-2 rounded-full bg-green-500" />
                           </div>
                           <div className="h-4 w-2/3 bg-white/10 rounded-full" />
                        </div>
                      ))}
                   </div>
                   <div className="h-full glass rounded-[32px] border-white/5 p-8 relative overflow-hidden">
                      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent" />
                      <div className="space-y-4 relative">
                         <div className="h-8 w-1/3 bg-white/10 rounded-xl" />
                         <div className="h-4 w-1/2 bg-white/5 rounded-full" />
                         <div className="h-48 w-full bg-white/[0.02] border border-white/5 rounded-[24px]" />
                      </div>
                   </div>
                </div>
              </div>
            </div>
          </motion.div>

        </div>

      </main>
    </>
  );
}
