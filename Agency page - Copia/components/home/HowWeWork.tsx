
import React from 'react';
import { motion } from 'framer-motion';
import { Search, AlertOctagon, Zap, BarChart3, CheckCircle2, ArrowDown } from 'lucide-react';

const MotionDiv = motion.div as any;

// --- CONFIGURAZIONE BLOCCHI METALLICI (Updated for Light Background) ---
const steps = [
  {
    id: "01",
    title: "ANALISI PROFONDA",
    subtitle: "Deep Scan Ecosystem",
    description: "Mappatura completa dell'ecosistema. Identifichiamo ogni singolo touchpoint tra brand e cliente per trovare le inefficienze.",
    icon: Search,
    // PLATINUM (Cool Silver) - Keeping light gradients but adding stronger shadows for light bg
    gradient: "bg-gradient-to-br from-[#FFFFFF] via-[#E2E8F0] to-[#94A3B8]",
    border: "border-[#94A3B8]",
    shadow: "shadow-[0_20px_40px_rgba(0,0,0,0.1)] hover:shadow-[0_30px_60px_rgba(0,0,0,0.2)]",
    iconColor: "text-slate-900",
    textColor: "text-slate-900"
  },
  {
    id: "02",
    title: "RILEVAMENTO PERDITE",
    subtitle: "Leakage Detection",
    description: "Procediamo solo se identifichiamo margini netti. Se il sistema è già performante, te lo comunichiamo con trasparenza assoluta.",
    icon: AlertOctagon,
    // BRONZE GOLD (Warm Metal)
    gradient: "bg-gradient-to-br from-[#FFF7ED] via-[#FDE68A] to-[#D4AF37]",
    border: "border-[#D4AF37]",
    shadow: "shadow-[0_20px_40px_rgba(212,175,55,0.15)] hover:shadow-[0_30px_60px_rgba(212,175,55,0.25)]",
    iconColor: "text-yellow-900",
    textColor: "text-slate-900"
  },
  {
    id: "03",
    title: "INSTALLAZIONE AI",
    subtitle: "System Deployment",
    description: "Rifacimento UX/UI e integrazione automazioni. Non è un restyling, è un trapianto di organi vitali per il tuo business.",
    icon: Zap,
    // PURE SILVER (High Tech)
    gradient: "bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B]",
    border: "border-[#64748B]",
    shadow: "shadow-[0_20px_40px_rgba(100,116,139,0.15)] hover:shadow-[0_30px_60px_rgba(100,116,139,0.25)]",
    iconColor: "text-slate-800",
    textColor: "text-slate-900"
  },
  {
    id: "04",
    title: "VALIDAZIONE DATI",
    subtitle: "Numeric Truth",
    description: "Monitoraggio in tempo reale del ROAS e del LTV. I dati non mentono: verifichiamo l'aumento effettivo del profitto netto.",
    icon: BarChart3,
    // CHAMPAGNE (Luxury)
    gradient: "bg-gradient-to-br from-[#FFFEF5] via-[#F1F5F9] to-[#DBCBA8]",
    border: "border-[#BCA876]",
    shadow: "shadow-[0_20px_40px_rgba(188,168,118,0.15)] hover:shadow-[0_30px_60px_rgba(188,168,118,0.25)]",
    iconColor: "text-slate-900",
    textColor: "text-slate-900"
  },
  {
    id: "05",
    title: "ASSET OWNERSHIP",
    subtitle: "Final Transfer",
    description: "Il sistema ora è un asset di tua proprietà che genera profitto autonomamente. Nessun canone eterno, solo risultati.",
    icon: CheckCircle2,
    // ROYAL GOLD (The Standard)
    gradient: "bg-gradient-to-br from-[#FFFBEB] via-[#FCD34D] to-[#B45309]",
    border: "border-[#B45309]",
    shadow: "shadow-[0_20px_40px_rgba(180,83,9,0.2)] hover:shadow-[0_30px_60px_rgba(180,83,9,0.3)]",
    iconColor: "text-yellow-950",
    textColor: "text-yellow-950",
    isFinal: true
  }
];

export const HowWeWork: React.FC = () => {
  
  // DARKER METAL TITLE for Light Background
  const darkMetalTitle = {
    backgroundImage: 'linear-gradient(180deg, #5B5B5B 0%, #333333 40%, #000000 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 0px rgba(255,255,255,0.5))',
  };

  return (
    <section id="process" className="py-32 relative overflow-hidden bg-[#DCD8CF]">
      
      {/* --- BACKGROUND: ARGENTO DORATO (SOLID / NORM) + HIGH QUALITY GRAIN --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none">
          
          {/* Layer 1: Sharp Static Noise (For Texture) */}
          <div 
            className="absolute inset-0 opacity-[0.6] mix-blend-overlay"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(150%) brightness(100%)' 
            }} 
          />
          
          {/* Layer 2: Coarse Digital Grain (For Depth - "Quality" Feel) */}
          <div 
            className="absolute inset-0 opacity-[0.4] mix-blend-soft-light"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '120px 120px',
                filter: 'contrast(120%)'
            }}
          />

          {/* Vignette */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.05)_100%)] opacity-100" />
      </div>

      <div className="container mx-auto px-4 relative z-20 max-w-5xl">
        
        {/* --- HEADER --- */}
        <div className="text-center mb-24">
             <MotionDiv
               initial={{ opacity: 0, y: 20 }}
               whileInView={{ opacity: 1, y: 0 }}
               viewport={{ once: true }}
             >
                <div className="inline-block mb-6 px-4 py-1.5 rounded-full border border-slate-400/30 bg-white/20 backdrop-blur-md shadow-sm">
                   <span className="text-[10px] font-mono text-slate-600 uppercase tracking-[0.3em] font-bold">
                      Protocollo Operativo v.5.0
                   </span>
                </div>
                
                <h2 className="font-serif text-5xl md:text-7xl font-black tracking-tight leading-none text-slate-900 mb-6 drop-shadow-sm">
                   <span style={darkMetalTitle as any}>ARCHITETTURA</span><br/>
                   DEL SUCCESSO
                </h2>
                
                <p className="max-w-xl mx-auto text-slate-600 text-sm md:text-base font-medium leading-relaxed">
                   Nessuna magia. Solo una sequenza ingegneristica di 5 step progettata per eliminare l'errore umano e forzare la crescita.
                </p>
             </MotionDiv>
        </div>

        {/* --- STACK DEI BLOCCHI (VERTICALE, CENTRATO, COORDINATO) --- */}
        <div className="relative flex flex-col items-center gap-8 md:gap-12">
           
           {/* Linea Connettiva Centrale (Background) - Darker for visibility on light bg */}
           <div className="absolute top-4 bottom-4 left-1/2 -translate-x-1/2 w-[1px] bg-gradient-to-b from-transparent via-slate-400 to-transparent z-0 hidden md:block opacity-40"></div>

           {steps.map((step, index) => (
             <div key={step.id} className="relative z-10 w-full group">
                
                <MotionDiv
                   initial={{ opacity: 0, y: 40, scale: 0.95 }}
                   whileInView={{ opacity: 1, y: 0, scale: 1 }}
                   viewport={{ once: true, margin: "-50px" }}
                   transition={{ duration: 0.6, delay: index * 0.1 }}
                   className="flex flex-col md:flex-row items-center justify-center"
                >
                   {/* 
                      IL BLOCCO METALLICO 
                      Solid gradients, borders, shadows.
                   */}
                   <div className={`
                      relative w-full md:w-[800px] p-8 md:p-10 rounded-2xl md:rounded-3xl
                      flex flex-col md:flex-row items-start md:items-center gap-6 md:gap-10
                      ${step.gradient} border ${step.border} ${step.shadow}
                      transform transition-transform duration-500 hover:scale-[1.02]
                   `}>
                      
                      {/* Shine Effect Overlay */}
                      <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20 opacity-80"></div>
                      <div className="absolute inset-0 bg-gradient-to-br from-white/60 to-transparent opacity-40 pointer-events-none rounded-2xl md:rounded-3xl"></div>

                      {/* 1. ID NUMBER (Huge & Watermarked) - Darker for light bg */}
                      <div className="hidden md:block absolute right-6 top-2 text-[80px] font-black text-black/5 font-serif leading-none select-none pointer-events-none">
                         {step.id}
                      </div>

                      {/* 2. ICON BLOCK (Glassmorphism inside Metal) */}
                      <div className={`
                         flex-shrink-0 w-16 h-16 rounded-xl bg-white/80 backdrop-blur-md border border-white/60 shadow-inner
                         flex items-center justify-center ${step.iconColor}
                      `}>
                         <step.icon size={32} strokeWidth={1.5} />
                      </div>

                      {/* 3. CONTENT (Dark Text on Light Metal) */}
                      <div className="flex-grow relative z-10">
                         <div className="flex items-center gap-3 mb-2">
                             <span className={`text-[10px] font-mono uppercase tracking-[0.2em] font-bold opacity-60 ${step.textColor}`}>
                                {step.subtitle}
                             </span>
                             <div className={`h-[1px] w-8 ${step.iconColor} opacity-20`}></div>
                         </div>
                         
                         <h3 className={`text-2xl md:text-3xl font-serif font-black mb-3 leading-tight ${step.textColor}`}>
                            {step.title}
                         </h3>
                         
                         <p className={`text-sm md:text-base font-medium leading-relaxed opacity-80 max-w-xl ${step.textColor}`}>
                            {step.description}
                         </p>
                      </div>

                      {/* 4. MOBILE ID */}
                      <div className="md:hidden absolute top-6 right-6 font-mono font-black text-2xl opacity-10 text-black">
                         {step.id}
                      </div>

                   </div>
                </MotionDiv>

                {/* CONNECTOR ARROW (Between Blocks) - Updated color */}
                {index !== steps.length - 1 && (
                   <div className="h-8 md:h-12 flex items-center justify-center relative z-0">
                      <MotionDiv 
                         initial={{ height: 0 }}
                         whileInView={{ height: "100%" }}
                         className="w-[1px] bg-slate-400/50"
                      />
                      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#DCD8CF] border border-slate-400/50 p-1.5 rounded-full shadow-sm">
                         <ArrowDown size={14} className="text-slate-600" />
                      </div>
                   </div>
                )}

             </div>
           ))}

        </div>
        
        {/* --- GUARANTEE BLOCK (New Copy) --- */}
        <MotionDiv 
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="mt-24 w-full bg-[#0a0a0a] rounded-[2rem] p-8 md:p-16 border border-slate-800 relative overflow-hidden shadow-2xl mx-auto"
        >
            {/* Texture */}
            <div className="absolute inset-0 opacity-30 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] mix-blend-overlay"></div>
            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/10"></div>
            
            <div className="relative z-10 flex flex-col gap-12">
                {/* Part 1 */}
                <div>
                    <h3 className="font-serif text-2xl md:text-3xl text-white mb-4 leading-snug">
                        In altre parole: con un investimento una tantum potrai <span className="border-b-2 border-red-500 pb-0.5 inline-block">incrementare le tue conversioni.</span>
                    </h3>
                    <p className="text-gray-400 text-lg md:text-xl font-light leading-relaxed">
                        Questo processo si chiama CRO e può portare un aumento del fatturato anche di 30% anche mantenendo la stessa spesa pubblicitaria.
                    </p>
                    <a href="https://www.boraso.com/blog/conversion-rate-optimization-cro-le-statistiche-2023-e-le-tendenze-del-settore/" target="_blank" rel="noopener noreferrer" className="inline-block mt-4 text-xs font-mono text-gray-500 underline hover:text-white transition-colors lowercase">- fonte</a>
                </div>

                {/* Part 2 */}
                <div>
                      <h3 className="font-serif text-2xl md:text-3xl text-white mb-4 leading-snug">
                        E se le tue conversioni non aumentano?
                    </h3>
                    <p className="text-gray-400 text-lg md:text-xl font-light leading-relaxed">
                        Se le conversioni non aumentano, continuiamo a lavorare per te <span className="text-white font-bold">a gratis</span> fino a quando le conversioni aumentano davvero.
                    </p>
                </div>
            </div>
        </MotionDiv>

        {/* FOOTER LABEL */}
        <div className="mt-20 text-center">
           <p className="text-slate-500 font-mono text-[10px] uppercase tracking-[0.3em] font-bold">
              Processo standardizzato ISO-Level per Digital Empire
           </p>
        </div>

      </div>
    </section>
  );
};
