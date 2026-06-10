
import React from 'react';
import { motion } from 'framer-motion';
import { MousePointer2, Zap, Smartphone, Search, ArrowRight, MousePointerClick, Eye, ShoppingBag, X, Check } from 'lucide-react';
import { GoldButton } from './ui/GoldButton';

const MotionDiv = motion.div as any;

export const WebDesignShowcase: React.FC = () => {
  
  const silverPureStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 25%, #CBD5E1 50%, #94A3B8 75%, #475569 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.2))',
  };

  const features = [
    {
      title: "Velocità Istantanea",
      desc: "Sotto i 0.2 secondi. Se il sito è lento, il cliente esce prima ancora di vedere il logo.",
      icon: Zap
    },
    {
      title: "Mobile First",
      desc: "Il 90% dei tuoi clienti compra dal telefono. Progettiamo per il pollice, non per il mouse.",
      icon: Smartphone
    },
    {
      title: "SEO Semantico",
      desc: "Codice pulito che Google ama. Non serve pagare ads se sei primo su Google gratis.",
      icon: Search
    },
    {
      title: "Design Persuasivo",
      desc: "Non facciamo arte. Usiamo layout psicologici che guidano l'occhio verso il bottone 'Acquista'.",
      icon: MousePointer2
    }
  ];

  return (
    <section className="py-24 md:py-32 relative overflow-hidden bg-[#000000]">
      
      {/* --- BACKGROUND: INTENSE FILM GRAIN (High Visibility) --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#000000]">
          
          {/* Layer 1: Sharp Static Noise (White Grain) - High Opacity */}
          <div 
            className="absolute inset-0 opacity-[0.35]"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(170%) brightness(150%) invert(100%)' 
            }} 
          />
          
          {/* Layer 2: Coarse Digital Grain - Mix Blend Screen for pop */}
          <div 
            className="absolute inset-0 opacity-[0.25] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '150px 150px',
                filter: 'contrast(150%)'
            }}
          />

          {/* Vignette to keep focus center, but lighter to show grain */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#000000_100%)] opacity-40" />
      </div>

      <div className="container mx-auto px-6 max-w-6xl relative z-10">
        
        {/* --- HEADER --- */}
        <div className="text-center mb-20 md:mb-28">
           <div className="inline-block px-3 py-1 mb-6 border border-white/10 rounded-full bg-white/5 backdrop-blur-md">
              <span className="text-[10px] font-mono uppercase tracking-[0.2em] text-gray-400">
                 Conversion Rate Optimization
              </span>
           </div>
           
           <h2 className="font-playfair text-5xl md:text-7xl lg:text-8xl text-white tracking-tight leading-[0.9] mb-8 drop-shadow-2xl">
             <span className="font-thin italic tracking-normal text-gray-400">non vendiamo</span> <span className="font-black text-white">siti web.</span><br/>
             <span className="font-thin italic tracking-normal text-gray-400">vendiamo</span> <span style={silverPureStyle as any} className="font-black">risultati.</span>
           </h2>
           
           <p className="max-w-2xl mx-auto text-gray-400 text-lg font-light leading-relaxed">
             La maggior parte delle agenzie ti consegna una "vetrina digitale" statica. <br/>
             Noi ti consegniamo un sistema attivo che trasforma i visitatori in clienti paganti.
           </p>
        </div>

        {/* --- CENTRAL SPLIT: CONCEPT & CTR --- */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center mb-32">
           
           {/* LEFT: THE INTERFACE CONCEPT (Minimal Wireframe) */}
           <MotionDiv 
             initial={{ opacity: 0, x: -30 }}
             whileInView={{ opacity: 1, x: 0 }}
             viewport={{ once: true }}
             className="relative"
           >
              <div className="relative aspect-[4/3] bg-[#050505] rounded-xl border border-white/10 shadow-[0_0_50px_rgba(0,0,0,0.8)] overflow-hidden group">
                 {/* Browser Header */}
                 <div className="h-10 border-b border-white/5 bg-[#0a0a0a] flex items-center px-4 gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-500/20"></div>
                    <div className="w-3 h-3 rounded-full bg-yellow-500/20"></div>
                    <div className="w-3 h-3 rounded-full bg-green-500/20"></div>
                    <div className="ml-4 flex-grow h-4 bg-white/5 rounded-full max-w-[200px]"></div>
                 </div>

                 {/* Website Content Preview */}
                 <div className="p-8 flex flex-col items-center justify-center h-full relative">
                    {/* Hero Text Skeleton */}
                    <div className="w-3/4 h-8 bg-white/10 rounded mb-4 animate-pulse"></div>
                    <div className="w-1/2 h-4 bg-white/5 rounded mb-8"></div>
                    
                    {/* THE BUTTON (The Focus) */}
                    <div className="relative group/btn cursor-pointer">
                       <div className="absolute inset-0 bg-gold-500 blur-lg opacity-20 group-hover/btn:opacity-40 transition-opacity"></div>
                       <div className="relative px-8 py-3 bg-gold-500 text-black font-bold uppercase tracking-widest text-xs rounded shadow-[0_0_20px_rgba(212,175,55,0.3)] transform group-hover/btn:scale-105 transition-transform flex items-center gap-2">
                          Clicca Qui per Acquistare <MousePointerClick size={14}/>
                       </div>
                       
                       {/* Cursor graphic */}
                       <MotionDiv 
                         className="absolute -bottom-8 -right-8 text-white drop-shadow-md"
                         animate={{ x: [10, 0, 10], y: [10, 0, 10] }}
                         transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                       >
                          <MousePointer2 size={24} fill="white" className="text-black" />
                       </MotionDiv>
                    </div>

                    {/* Minimal Metrics Overlay */}
                    <div className="absolute bottom-4 left-4 right-4 flex justify-between text-[9px] font-mono text-gray-600 uppercase tracking-widest">
                       <span>Load: 0.12s</span>
                       <span className="text-green-500">Sales: Active</span>
                    </div>
                 </div>
                 
                 {/* Scanline Effect */}
                 <div className="absolute inset-0 bg-gradient-to-b from-transparent via-white/5 to-transparent h-[10px] w-full pointer-events-none animate-[scan_4s_linear_infinite]"></div>
              </div>
              
              {/* Decorative behind elements */}
              <div className="absolute -top-4 -right-4 w-full h-full border border-dashed border-white/10 rounded-xl -z-10 opacity-30"></div>
           </MotionDiv>


           {/* RIGHT: THE CTR EXPLANATION (Simple & Direct) */}
           <MotionDiv 
             initial={{ opacity: 0, x: 30 }}
             whileInView={{ opacity: 1, x: 0 }}
             viewport={{ once: true }}
             className="flex flex-col justify-center"
           >
              <div className="mb-6 flex items-center gap-3">
                 <div className="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center border border-white/10">
                    <Eye className="text-gold-500" size={20} />
                 </div>
                 <h3 className="text-2xl font-serif text-white font-bold">Cos'è il CTR?</h3>
              </div>

              {/* MODIFIED: GLASS EFFECT (10% OPACITY + BLUR XL) */}
              <div className="p-6 bg-[#0a0a0a]/10 backdrop-blur-xl border border-white/10 rounded-xl mb-8 relative overflow-hidden">
                 <div className="absolute left-0 top-0 h-full w-1 bg-gold-500"></div>
                 <p className="text-lg text-gray-200 leading-relaxed font-light">
                    Il <strong>CTR (Click-Through Rate)</strong> è la "Legge della Vetrina".
                 </p>
                 <div className="mt-4 space-y-4 text-sm text-gray-400">
                    <p>
                       Immagina il tuo sito come un negozio in centro. <br/>
                       Passano <strong>100 persone</strong> davanti alla vetrina.
                    </p>
                    <ul className="space-y-3 pl-4 border-l border-white/10">
                       <li className="flex items-center gap-3">
                          <X size={14} className="text-red-500" />
                          <span>Se entrano in <strong>1</strong>, il tuo CTR è dell'1%. <span className="text-red-400 italic">(Stai fallendo)</span></span>
                       </li>
                       <li className="flex items-center gap-3">
                          <Check size={14} className="text-green-500" />
                          <span>Se entrano in <strong>15</strong>, il tuo CTR è del 15%. <span className="text-green-400 italic font-bold">(Stai facendo soldi)</span></span>
                       </li>
                    </ul>
                    <p className="pt-2 text-white font-medium">
                       Noi costruiamo vetrine irresistibili che costringono le persone a entrare. Semplice.
                    </p>
                 </div>
              </div>

              <GoldButton href="#contact" variant="silver">
                 Aumenta il Mio CTR Ora
              </GoldButton>
           </MotionDiv>

        </div>

        {/* --- BOTTOM: 4 PILLARS (Clean Grid) --- */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
           {features.map((feature, idx) => (
             <MotionDiv
               key={idx}
               initial={{ opacity: 0, y: 20 }}
               whileInView={{ opacity: 1, y: 0 }}
               viewport={{ once: true }}
               transition={{ delay: idx * 0.1 }}
               // MODIFICATO: GLASS EFFECT (10% OPACITY + BLUR XL)
               className="p-6 border border-white/10 bg-[#0a0a0a]/10 backdrop-blur-xl hover:bg-[#0a0a0a]/20 hover:border-white/20 transition-all duration-300 rounded-lg group shadow-lg"
             >
                <div className="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center mb-4 text-gray-400 group-hover:text-white group-hover:bg-white/10 transition-colors">
                   <feature.icon size={20} />
                </div>
                <h4 className="text-white font-serif text-lg font-bold mb-2 group-hover:text-gold-200 transition-colors">
                   {feature.title}
                </h4>
                <p className="text-xs text-gray-500 leading-relaxed font-mono">
                   {feature.desc}
                </p>
             </MotionDiv>
           ))}
        </div>

      </div>
    </section>
  );
};
