
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, TrendingUp, Check, ArrowRight, ChevronDown, Monitor, Zap, Database, FileText } from 'lucide-react';
import { GoldButton } from './ui/GoldButton';

// Dati aggiornati: UNICO SERVIZIO (CRO) diviso in 3 Step
const services = [
  {
    id: 0,
    title: "ottimizzazione funnel",
    description: "step 1: analizziamo e correggiamo.",
    icon: Search,
    details: {
      headline: "non devi rifare tutto. devi solo aggiustare ciò che è rotto.",
      emotionalCopy: "spesso hai già l'oro tra le mani, ma scivola via dai buchi del secchio. noi analizziamo il tuo funnel attuale, troviamo dove i clienti abbandonano e chiudiamo le falle. il risultato? più soldi senza spendere un euro in più in ads.",
      specs: [
        "audit ux/ui completo",
        "analisi drop-off points",
        "speed optimization",
        "friction removal"
      ]
    }
  },
  {
    id: 1,
    title: "creazione asset",
    description: "step 2: costruiamo ciò che manca.",
    icon: FileText,
    details: {
      headline: "i ponti mancanti verso la vendita.",
      emotionalCopy: "hai il traffico ma non converte? forse manca una sales page persuasiva. forse mancano le email di recupero carrello. forse manca una vsl. noi identifichiamo i pezzi mancanti del puzzle e li creiamo da zero con standard d'élite.",
      specs: [
        "sales page ad alta conversione",
        "email marketing sequences",
        "vsl scripting & production",
        "checkout optimization"
      ]
    }
  },
  {
    id: 2,
    title: "boost conversioni",
    description: "step 3: scaliamo il profitto.",
    icon: TrendingUp,
    details: {
      headline: "la matematica non è un'opinione.",
      emotionalCopy: "una volta che la macchina è oliata e completa, spingiamo sull'acceleratore. testiamo varianti diverse (a/b testing), affiniamo il copy e usiamo la psicologia comportamentale per trasformare una % sempre maggiore di visitatori in clienti.",
      specs: [
        "a/b testing continuo",
        "copywriting persuasivo",
        "pricing psychology",
        "aumento ltv (lifetime value)"
      ]
    }
  }
];

export const Services: React.FC = () => {
  const [selected, setSelected] = useState<number | null>(null);

  // GRADIENTE ARGENTO PURO (Per titoli e parola "SERVIZI")
  const pureSilverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 40%, #94A3B8 70%, #475569 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.3))',
  };

  // GRADIENTE "CHAMPAGNE" (Più uniforme, meno giallo saturo)
  const champagneGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 10%, #F8FAFC 30%, #F3E5AB 50%, #D4AF37 75%, #B48B3E 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 0px 20px rgba(227,200,120,0.15))',
  };

  return (
    <section id="services" className="py-32 relative border-t border-white/5 scroll-mt-20 bg-[#050505] overflow-hidden">
      
      {/* --- BACKGROUND: LIGHTER NOISE FOR VISIBILITY --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#050505]">
          
          {/* Layer 1: Texture (Reduced Opacity/Contrast for better text visibility) */}
          <div 
            className="absolute inset-0 opacity-[0.15]"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(120%) brightness(120%)' 
            }} 
          />
          
          {/* Vignette */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#000000_100%)] opacity-60" />
      </div>

      <div className="container mx-auto px-6 max-w-6xl relative z-10">
        
        {/* HEADER MODIFICATO: UNICO SERVIZIO CRO */}
        <div className="text-center mb-16 relative">
          <motion.h2 
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="font-serif text-4xl md:text-6xl lg:text-7xl font-light tracking-tight lowercase leading-[0.9]"
          >
            {/* Unificazione visiva */}
            <span style={pureSilverGradient as any}>l'unico servizio:</span>
            <br className="md:hidden" />
            <span className="mx-2 md:mx-4 text-white/10 font-thin hidden md:inline">|</span>
            <span style={champagneGradient as any} className="font-black">c.r.o.</span>
          </motion.h2>
          
          {/* Elemento di connessione visiva con le card */}
          <div className="flex items-center justify-center gap-4 mt-6 opacity-80">
             <div className="h-[1px] w-12 bg-gradient-to-r from-transparent to-white/30"></div>
             <p className="text-xs font-mono uppercase tracking-[0.2em] text-gray-300">
               conversion rate optimization protocol
             </p>
             <div className="h-[1px] w-12 bg-gradient-to-l from-transparent to-white/30"></div>
          </div>
        </div>

        {/* GRID CARD - BRIGHTER BORDERS FOR CONTRAST */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          {services.map((service, i) => {
            const isSelected = selected === i;
            return (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                onClick={() => setSelected(isSelected ? null : i)}
                // OUTER CONTAINER: Acts as the "Border"
                className={`
                  relative p-[1px] rounded-[32px] cursor-pointer group transition-all duration-500
                  ${isSelected 
                    ? 'scale-[1.02] z-20' 
                    : 'hover:scale-[1.01] z-10'
                  }
                `}
                style={{
                  // THE METAL GRADIENT BORDER: Silver -> Gold -> White -> Silver
                  background: isSelected
                    ? 'linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 20%, #F59E0B 50%, #D4AF37 80%, #FFFFFF 100%)'
                    : 'linear-gradient(135deg, #475569 0%, #94A3B8 50%, #E2E8F0 100%)' // Brighter default border for visibility
                }}
              >
                {/* INNER CONTAINER: Lighter Black Content Background */}
                <div className={`
                    h-full w-full bg-[#0a0a0a] rounded-[31px] p-8 md:p-12 relative overflow-hidden flex flex-col items-center md:items-start text-center md:text-left
                    border border-white/5
                    ${isSelected ? 'bg-[#0f0f0f]' : ''}
                `}>
                  
                  {/* Subtle Inner Glow/Noise */}
                  <div className="absolute inset-0 opacity-[0.05] bg-[url('https://grainy-gradients.vercel.app/noise.svg')] pointer-events-none"></div>
                  
                  {/* Top Shine inside the card */}
                  <div className={`absolute top-0 left-0 w-full h-[40%] bg-gradient-to-b from-white/10 to-transparent pointer-events-none transition-opacity duration-500 ${isSelected ? 'opacity-100' : 'opacity-50'}`}></div>

                  {/* CONTENT */}
                  <div className="relative z-10 w-full flex flex-col items-center md:items-start">
                      <div className={`
                        inline-flex items-center justify-center w-16 h-16 mb-8 transition-colors duration-500 rounded-2xl
                        ${isSelected 
                            ? 'text-gold-500 bg-[#402E11]/20 border border-gold-500/30' 
                            : 'text-gray-300 bg-white/10 border border-white/20 group-hover:text-gold-100 group-hover:border-gold-500/20'
                        }
                      `}>
                        <service.icon size={32} strokeWidth={1.5} />
                      </div>
                      
                      {/* TITOLO IN ARGENTO/ORO */}
                      <h3 
                        className={`font-serif text-2xl md:text-3xl font-black mb-5 tracking-tight lowercase leading-none ${isSelected ? 'text-transparent bg-clip-text bg-gradient-to-r from-white via-gold-200 to-gold-500' : 'text-white'}`}
                      >
                        {service.title}
                      </h3>
                      
                      <p className="text-gray-400 text-sm md:text-base leading-relaxed font-mono uppercase text-[10px] tracking-widest group-hover:text-gray-200 transition-colors">
                        {service.description}
                      </p>

                      <div className={`mt-8 w-full flex justify-center md:justify-start`}>
                         <div className={`flex items-center gap-2 text-[10px] font-mono lowercase tracking-widest transition-all duration-300 ${isSelected ? 'text-gold-500 opacity-100 translate-y-0' : 'text-gray-500 opacity-80 group-hover:opacity-100 group-hover:text-white'}`}>
                            <span>scopri <span className="font-bold">dettagli</span></span>
                            <ChevronDown size={12} className={`transition-transform duration-300 ${isSelected ? 'rotate-180' : ''}`} />
                         </div>
                      </div>
                  </div>

                </div>
              </motion.div>
            );
          })}
        </div>

        {/* EXPANDABLE DETAILS PANEL */}
        <AnimatePresence mode="wait">
          {selected !== null && (
            <motion.div
              key="details-panel"
              initial={{ opacity: 0, height: 0, y: -10 }}
              animate={{ opacity: 1, height: 'auto', y: 0 }}
              exit={{ opacity: 0, height: 0, y: -10 }}
              transition={{ duration: 0.5, ease: [0.32, 0.72, 0, 1] }}
              className="overflow-hidden"
            >
              <div 
                  className="relative p-[1px] rounded-[32px] mt-4"
                  style={{
                      background: 'linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 20%, #F59E0B 50%, #D4AF37 80%, #FFFFFF 100%)'
                  }}
              >
                <div className="rounded-[31px] p-10 md:p-16 relative overflow-hidden bg-[#080808]">
                    
                    {/* Decorative Elements */}
                    <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/10 to-transparent" />
                    <div className="absolute bottom-0 right-0 p-4 opacity-5 pointer-events-none">
                       <Monitor size={150} className="text-white" strokeWidth={0.5} />
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-16 relative z-10">
                      
                      {/* LEFT: Emotional Logic */}
                      <div>
                        <div className="inline-flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/10 rounded-full mb-8">
                           <div className="w-1.5 h-1.5 bg-white rounded-full animate-pulse shadow-[0_0_10px_white]" />
                           <span className="text-[9px] font-mono lowercase tracking-widest text-gray-300">approfondimento step {selected + 1}</span>
                        </div>

                        <h3 className="font-serif text-3xl md:text-5xl text-white leading-tight mb-8 font-medium lowercase">
                          {services[selected].details.headline}
                        </h3>
                        
                        <p className="text-gray-300 text-base md:text-lg leading-relaxed font-light border-l border-white/20 pl-8 lowercase">
                          {services[selected].details.emotionalCopy}
                        </p>

                        <div className="mt-10">
                           <a href="#contact" className="inline-flex items-center gap-2 text-white border-b border-white/30 pb-1 hover:border-white transition-all text-xs font-bold uppercase tracking-widest group lowercase">
                              attiva <span className="font-bold">protocollo cro</span> <ArrowRight size={12} className="group-hover:translate-x-1 transition-transform" />
                           </a>
                        </div>
                      </div>

                      {/* RIGHT: Technical Specs (Silver Style) */}
                      <div className="bg-[#121212] border border-white/10 p-8 rounded-2xl shadow-inner">
                         <h4 className="text-[10px] font-mono lowercase tracking-[0.3em] text-gray-400 mb-8 font-bold flex items-center gap-2">
                            <Database size={12} /> azioni pratiche
                         </h4>
                         
                         <div className="space-y-5">
                            {services[selected].details.specs.map((spec, idx) => (
                               <div key={idx} className="flex items-center gap-5 group/spec">
                                  <div className="w-8 h-8 rounded-full bg-black flex items-center justify-center border border-white/20 group-hover/spec:border-white/50 transition-colors shadow-lg">
                                     <Check size={14} className="text-gray-400 group-hover/spec:text-white transition-colors" />
                                  </div>
                                  <span style={pureSilverGradient as any} className="text-xl font-sans font-bold tracking-tight lowercase">
                                     {spec}
                                  </span>
                               </div>
                            ))}
                         </div>

                         <div className="mt-10 pt-8 border-t border-white/5 flex justify-between items-center opacity-50">
                            <span className="text-[9px] font-mono text-gray-500 uppercase">system: cro_v3</span>
                            <Zap size={12} className="text-white" />
                         </div>
                      </div>

                    </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

      </div>
    </section>
  );
};
