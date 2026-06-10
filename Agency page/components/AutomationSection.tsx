
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Bot, 
  Zap, 
  Activity, 
  ShieldAlert, 
  Cpu, 
  Clock, 
  ArrowRight,
  Database,
  XCircle,
  CheckCircle2,
  TrendingUp,
  FileWarning,
  Scale,
  Ban,
  Scan,
  AlertTriangle
} from 'lucide-react';
import { GoldButton } from './ui/GoldButton';

const MotionDiv = motion.div as any;

export const AutomationSection: React.FC = () => {
  const [activeCrime, setActiveCrime] = useState<number>(0);

  const crimes = [
    {
      id: "C-01",
      title: "Lentezza Operativa",
      desc: "Un umano impiega in media 25 minuti per rispondere a un lead. In quel tempo, il cliente ha già comprato dal concorrente.",
      penalty: "Perdita del 60% delle conversioni.",
      icon: Clock
    },
    {
      id: "C-02",
      title: "Errore di Trascrizione",
      desc: "Copiare dati da Excel al CRM porta a un tasso di errore del 18%. Numeri sbagliati, email perse, fatture errate.",
      penalty: "Danno d'immagine e contabile.",
      icon: FileWarning
    },
    {
      id: "C-03",
      title: "Burnout del Personale",
      desc: "Costringere talenti creativi a fare data-entry ripetitivo uccide la produttività e aumenta il turnover.",
      penalty: "Costi di riassunzione elevati.",
      icon: UserIcon // Helper comp defined below or just map directly
    }
  ];

  // STILI TIPOGRAFICI LUSSO DARK
  const platinumGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 50%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,0.1))'
  };

  const brightSilverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 20%, #F1F5F9 50%, #CBD5E1 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.5))'
  };

  return (
    <section id="automation" className="py-20 md:py-32 relative overflow-hidden bg-[#020617]">
      
      {/* --- BACKGROUND: DEEP CELESTIAL BLUE + INTENSE GRAIN --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#020617]">
          
          {/* Base: Deep Azure/Celestial Gradient (Dark Abyss) */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_30%,#0f2e4a_0%,#020617_70%)] opacity-100" />
          
          {/* Layer 1: Sharp Static Noise (White Grain) - High Visibility on Blue */}
          <div 
            className="absolute inset-0 opacity-[0.35]"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(170%) brightness(150%) invert(100%)' 
            }} 
          />
          
          {/* Layer 2: Coarse Digital Grain - Mix Blend Screen for Texture Pop */}
          <div 
            className="absolute inset-0 opacity-[0.3] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '150px 150px',
                filter: 'contrast(150%)'
            }}
          />

          {/* Vignette to focus center */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#020617_100%)] opacity-50" />
      </div>


      <div className="container mx-auto px-6 md:px-12 relative z-10 max-w-7xl">

        {/* --- 1. HEADER: THE ACCUSATION --- */}
        <div className="flex flex-col items-center text-center mb-20 md:mb-32 relative">
            
            {/* TAG */}
            <MotionDiv 
              initial={{ scale: 0.9, opacity: 0 }}
              whileInView={{ scale: 1, opacity: 1 }}
              viewport={{ once: true }}
              className="mb-8 inline-flex items-center gap-3 px-6 py-2 bg-[#0f2e4a]/30 border border-slate-400/30 backdrop-blur-md rounded-sm shadow-[0_0_20px_rgba(14,165,233,0.1)] relative z-20"
            >
               <Scan className="text-sky-300 animate-pulse" size={16} />
               <span className="font-mono text-[10px] font-black uppercase tracking-[0.3em] text-sky-100">
                  Forensic System Analysis
               </span>
            </MotionDiv>

            <h2 className="font-serif text-4xl sm:text-5xl md:text-7xl lg:text-8xl text-white tracking-tighter leading-[0.9] mb-12 drop-shadow-[0_4px_10px_rgba(0,0,0,0.8)]">
               <span className="font-thin italic tracking-normal text-sky-200/60">il</span> <span style={platinumGradient as any} className="font-black">lavoro manuale</span> <br/>
               <span className="font-thin italic tracking-normal text-sky-200/60">è un </span> 
               <span style={brightSilverGradient as any} className="font-black drop-shadow-[0_0_35px_rgba(255,255,255,0.5)]">crimine.</span>
            </h2>

            {/* QUOTE BOX */}
            <div className="w-full max-w-3xl mx-auto p-[1px] bg-gradient-to-r from-slate-600 via-sky-300 to-slate-700 rounded-lg shadow-[0_0_50px_rgba(14,165,233,0.1)]">
               <div className="bg-[#020617]/90 rounded-lg p-6 md:p-10 relative overflow-hidden backdrop-blur-sm">
                   <div className="absolute top-0 right-0 p-3 opacity-10 pointer-events-none">
                      <FileWarning size={80} className="text-sky-400" />
                   </div>
                   <p className="text-lg md:text-2xl font-serif font-medium text-sky-100/90 mb-6 leading-relaxed relative z-10 italic">
                      "Ogni minuto che il tuo team passa a spostare dati invece di chiudere contratti è un furto diretto al tuo margine operativo netto."
                   </p>
                   <div className="flex items-center gap-3 relative z-10">
                      <div className="h-[2px] w-12 bg-sky-400"></div>
                      <p className="text-sky-300 font-mono text-[10px] uppercase tracking-widest font-black">
                         Rapporto Empire Systems
                      </p>
                   </div>
               </div>
            </div>
        </div>

        {/* --- 2. THE EVIDENCE (Grid Layout Fixed) --- */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-24 mb-32 items-start relative">
           
           {/* Left: CAPI D'ACCUSA (List) */}
           <div className="lg:col-span-7 flex flex-col gap-6 relative z-10">
              <div className="flex items-center gap-4 mb-4 border-b border-white/10 pb-4">
                 <ShieldAlert size={20} className="text-sky-300" />
                 <h3 className="font-mono text-xs font-bold uppercase tracking-[0.3em] text-sky-200/60">
                    Registro Inefficienze
                 </h3>
              </div>

              {crimes.map((crime, idx) => {
                 const isActive = activeCrime === idx;
                 
                 return (
                   <div 
                      key={idx}
                      onClick={() => setActiveCrime(idx)}
                      className={`
                         relative p-[1px] group cursor-pointer transition-all duration-500 rounded-xl
                         ${isActive ? 'scale-[1.02] z-20 shadow-[0_10px_40px_rgba(255,255,255,0.1)]' : 'hover:opacity-80 z-10'}
                      `}
                      style={{
                        background: isActive 
                            ? 'linear-gradient(135deg, #FFFFFF 0%, #94A3B8 50%, #475569 100%)' // Pure Silver Gradient
                            : 'linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%)'
                      }}
                   >
                      {/* INNER CONTENT */}
                      <div className={`
                          relative h-full p-6 md:p-8 bg-[#020617]/90 backdrop-blur-md rounded-xl transition-colors duration-300 overflow-hidden
                          ${isActive ? 'bg-[#0f172a]/95' : ''}
                      `}>
                          <div className="flex flex-col md:flex-row items-start gap-6 relative z-10">
                             {/* Icon Box */}
                             <div className={`
                                p-3 rounded-lg border flex-shrink-0 transition-colors duration-300
                                ${isActive 
                                   ? 'border-slate-300 text-white bg-slate-700/50 shadow-[0_0_20px_rgba(255,255,255,0.2)]' 
                                   : 'border-white/10 text-gray-500 bg-white/5'
                                }
                             `}>
                                <crime.icon size={28} strokeWidth={1.5} />
                             </div>

                             {/* Text Content */}
                             <div className="flex-grow">
                                <div className="flex flex-wrap justify-between items-center mb-3 gap-2">
                                   <h4 className={`text-xl font-serif font-bold ${isActive ? 'text-white' : 'text-gray-400'}`}>
                                      {crime.title}
                                   </h4>
                                   <span className={`font-mono text-[10px] font-bold tracking-widest py-1 px-2 border rounded ${isActive ? 'text-white border-white' : 'text-gray-600 border-white/5'}`}>
                                      {crime.id}
                                   </span>
                                </div>
                                
                                <p className="text-sm text-gray-400 leading-relaxed mb-5 font-light">
                                   {crime.desc}
                                </p>
                                
                                <div className={`
                                   inline-flex items-center gap-2 text-[10px] font-mono uppercase tracking-widest font-bold border-l-2 pl-3
                                   ${isActive ? 'text-slate-300 border-slate-300' : 'text-gray-600 border-gray-700'}
                                `}>
                                   <Ban size={12} />
                                   PENALITÀ: <span className="text-white">{crime.penalty}</span>
                                </div>
                             </div>
                          </div>
                      </div>
                   </div>
                 );
              })}
           </div>

           {/* Right: THE VERDICT (Monitor Style) */}
           <div className="lg:col-span-5 relative h-full min-h-[500px]">
              <div className="sticky top-32 w-full">
                 {/* MONITOR FRAME: Silver Gradient */}
                 <div className="p-[2px] bg-gradient-to-b from-white via-slate-400 to-slate-800 shadow-[0_0_60px_rgba(255,255,255,0.1)] rounded-2xl">
                     <div className="bg-[#020617]/95 backdrop-blur-xl p-8 md:p-10 relative overflow-hidden rounded-2xl">
                        
                        {/* Scanlines Background - Enhanced for VHS feel */}
                        <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,255,255,0.03),rgba(255,255,255,0.01))] z-0 bg-[length:100%_2px,3px_100%] pointer-events-none opacity-50"></div>
                        
                        <div className="relative z-10">
                            {/* Header Alert: Silver */}
                            <div className="flex items-center gap-3 mb-8 text-slate-200 border-b border-white/10 pb-4">
                               <AlertTriangle size={20} className="text-white animate-pulse" />
                               <span className="font-mono text-[10px] font-black uppercase tracking-[0.3em]">Allerta Critica</span>
                            </div>

                            <h3 className="font-serif text-2xl md:text-3xl text-white mb-2 leading-tight">
                               STAI BRUCIANDO
                            </h3>
                            {/* NUMBER: ICE SILVER */}
                            <div className="text-5xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white via-slate-200 to-slate-500 tracking-tighter mb-4 filter drop-shadow-[0_0_15px_rgba(255,255,255,0.4)]">
                               €4.500
                            </div>
                            <p className="text-[10px] font-mono text-gray-500 uppercase tracking-[0.2em] mb-10">
                               Al Mese in Inefficienza Operativa
                            </p>

                            {/* Data Table */}
                            <div className="space-y-4 font-mono text-xs mb-10">
                               <div className="flex justify-between items-center py-2 border-b border-dashed border-gray-800">
                                  <span className="text-gray-500">COSTO STAFF MANUALE</span>
                                  <span className="text-white font-bold">€3.200</span>
                               </div>
                               <div className="flex justify-between items-center py-2 border-b border-dashed border-gray-800">
                                  <span className="text-gray-500">LEAD PERSI (STIMATI)</span>
                                  <span className="text-white font-bold">€1.300</span>
                               </div>
                               <div className="flex justify-between items-center py-4 border-t border-white/20 mt-4 bg-white/5 px-4 -mx-4 rounded">
                                  <span className="text-slate-300 font-bold uppercase">Totale Spreco Annuo</span>
                                  <span className="text-white font-black text-sm">€54.000</span>
                               </div>
                            </div>

                            {/* Solution Link */}
                            <div className="text-center pt-4">
                                <div className="flex justify-center">
                                   <div className="p-3 border border-white/30 rounded-full animate-bounce text-white bg-white/10 hover:bg-white/20 transition-colors cursor-pointer shadow-[0_0_15px_rgba(255,255,255,0.2)]">
                                      <ArrowRight size={20} className="rotate-90" />
                                   </div>
                                </div>
                            </div>
                        </div>
                     </div>
                 </div>
              </div>
           </div>
        </div>

        {/* --- 3. THE SOLUTION: EMPIRE PROTOCOL --- */}
        <div className="relative mt-20 border-t border-white/5 pt-24">
           {/* Section Title */}
           <div className="text-center mb-20 relative z-10">
               <span className="px-4 py-2 border border-slate-500/30 bg-[#0f2e4a]/60 backdrop-blur-md text-sky-200 font-mono text-[10px] font-black uppercase tracking-[0.2em] mb-8 inline-block rounded-full shadow-[0_0_15px_rgba(14,165,233,0.1)]">
                  Protocollo Correttivo Attivato
               </span>
               <h2 className="text-4xl md:text-6xl lg:text-7xl font-serif font-black text-white mb-8 tracking-tight drop-shadow-xl">
                  L'ERA DELL' <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-200 to-white decoration-white/30 underline-offset-8 decoration-2 drop-shadow-lg">AUTOMAZIONE</span>
               </h2>
               <p className="max-w-2xl mx-auto text-lg text-gray-300 font-light leading-relaxed">
                  Sostituiamo processi umani fallibili con infrastrutture digitali perfette.
                  <br/>Più veloce. Più economico. Senza errori.
               </p>
           </div>

           {/* The Machinery (Cards) */}
           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              
              {/* Card 1: 24/7 Agent */}
              <div className="bg-[#020617]/80 backdrop-blur-md border border-white/10 p-10 hover:border-slate-400/50 transition-all duration-500 group relative overflow-hidden rounded-xl shadow-2xl">
                 <div className="absolute top-0 right-0 p-4 opacity-5 group-hover:opacity-10 transition-opacity">
                    <Bot size={100} className="text-white" />
                 </div>
                 <div className="w-16 h-16 bg-white/5 rounded-xl flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 group-hover:text-white transition-colors">
                    <Bot size={32} />
                 </div>
                 <h3 className="text-2xl font-bold font-serif text-white mb-4">Agente Neurale H24</h3>
                 <p className="text-gray-400 text-sm leading-relaxed mb-8 font-light">
                    Mentre tu dormi, il nostro sistema qualifica i lead, risponde alle domande e fissa appuntamenti sul tuo calendario.
                 </p>
                 <div className="flex items-center gap-2 text-[10px] font-mono uppercase font-bold text-gray-600 group-hover:text-white transition-colors">
                    <CheckCircle2 size={12} />
                    Zero Tempi Morti
                 </div>
              </div>

              {/* Card 2: CRM Sync (Highlighted) - Silver Edition */}
              <div className="bg-gradient-to-b from-[#1e293b]/90 to-[#020617]/90 backdrop-blur-md border border-slate-400/30 p-10 relative z-10 shadow-[0_0_40px_rgba(255,255,255,0.05)] group rounded-xl transform md:-translate-y-4">
                 <div className="absolute top-0 left-0 w-full h-[1px] bg-white/50"></div>
                 <div className="absolute top-4 right-4 text-white animate-pulse">
                    <Activity size={18} />
                 </div>
                 <div className="w-16 h-16 bg-slate-900/50 rounded-xl flex items-center justify-center mb-8 border border-slate-400/30 text-white shadow-[0_0_20px_rgba(255,255,255,0.1)]">
                    <Database size={32} />
                 </div>
                 <h3 className="text-2xl font-bold font-serif text-white mb-4">Sync Istantaneo</h3>
                 <p className="text-gray-300 text-sm leading-relaxed mb-8 font-medium">
                    Colleghiamo Ads, Sito e CRM. I dati scorrono fluidi come acqua. Nessun copia-incolla. Nessun dato perso.
                 </p>
                 <div className="flex items-center gap-2 text-[10px] font-mono uppercase font-bold text-white">
                    <Zap size={12} />
                    Real-Time Processing
                 </div>
              </div>

              {/* Card 3: Profit Scale */}
              <div className="bg-[#020617]/80 backdrop-blur-md border border-white/10 p-10 hover:border-slate-400/50 transition-all duration-500 group relative overflow-hidden rounded-xl shadow-2xl">
                 <div className="absolute top-0 right-0 p-4 opacity-5 group-hover:opacity-10 transition-opacity">
                    <TrendingUp size={100} className="text-white" />
                 </div>
                 <div className="w-16 h-16 bg-white/5 rounded-xl flex items-center justify-center mb-8 border border-white/10 group-hover:bg-white/10 group-hover:text-white transition-colors">
                    <TrendingUp size={32} />
                 </div>
                 <h3 className="text-2xl font-bold font-serif text-white mb-4">Margine Puro</h3>
                 <p className="text-gray-400 text-sm leading-relaxed mb-8 font-light">
                    Riducendo i costi operativi del 70% e aumentando la conversione dei lead, il tuo margine netto esplode.
                 </p>
                 <div className="flex items-center gap-2 text-[10px] font-mono uppercase font-bold text-gray-600 group-hover:text-white transition-colors">
                    <Scale size={12} />
                    ROI Massimizzato
                 </div>
              </div>

           </div>
        </div>

        {/* --- 4. VISUAL COMPARISON (Mugshot Style - Dark Mode) --- */}
        <div className="mt-32 md:mt-40 border border-white/10 bg-[#020617]/80 backdrop-blur-md relative rounded-2xl overflow-hidden shadow-2xl">
            
            {/* Center VS Badge */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 bg-black rounded-full flex items-center justify-center border border-white/20 shadow-xl z-20 font-black text-white italic text-lg">
               VS
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-0 divide-y md:divide-y-0 md:divide-x divide-white/10">
               
               {/* OLD WAY */}
               <div className="p-12 md:p-16 text-center opacity-50 hover:opacity-100 transition-opacity duration-500 bg-[#0a0a0a]">
                  <div className="inline-block p-5 border border-dashed border-gray-700 rounded-full mb-8">
                     <UserIcon size={40} className="text-gray-500" />
                  </div>
                  <h4 className="text-xl font-bold uppercase tracking-widest text-gray-500 mb-8">Il Vecchio Metodo</h4>
                  <ul className="space-y-4 text-xs font-mono text-gray-500 text-left mx-auto max-w-xs">
                     <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700"/> Costi Fissi Alti</li>
                     <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700"/> Lento (9-18h)</li>
                     <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700"/> Emotivo/Stanco</li>
                  </ul>
               </div>

               {/* NEW WAY - Silver/White Glow */}
               <div className="p-12 md:p-16 text-center relative overflow-hidden bg-slate-900/20">
                  <div className="absolute inset-0 bg-white/5 z-0 animate-pulse"></div>
                  <div className="relative z-10">
                    <div className="inline-block p-5 border border-white/50 rounded-full mb-8 bg-white/10 shadow-[0_0_30px_rgba(255,255,255,0.2)]">
                        <Cpu size={40} className="text-white" />
                    </div>
                    <h4 className="text-xl font-black uppercase tracking-widest text-white mb-8">Empire System</h4>
                    <ul className="space-y-4 text-xs font-mono text-gray-300 font-bold text-left mx-auto max-w-xs">
                        <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white"/> Costo Marginale Zero</li>
                        <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white"/> Istantaneo (0.2s)</li>
                        <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white"/> Perfezione Logica</li>
                    </ul>
                  </div>
               </div>

            </div>
        </div>

        {/* CTA */}
        <div className="mt-32 text-center pb-20 relative z-10">
           <h3 className="font-serif text-3xl md:text-4xl font-bold text-white mb-10">
              Smetti di pagare per l'inefficienza.
           </h3>
           <GoldButton href="#contact" variant="silver" className="shadow-[0_0_50px_rgba(255,255,255,0.15)] border-white/30 px-10 py-5 text-sm">
              INSTALLA AUTOMAZIONE ORA
           </GoldButton>
           <p className="mt-8 text-[10px] text-gray-600 font-mono uppercase tracking-widest">
              Configurazione in 7 giorni lavorativi.
           </p>
        </div>

      </div>
    </section>
  );
};

// Helper component for user icon to avoid name conflict if necessary, 
// though we can just import User as UserIcon
const UserIcon = ({ size, className }: { size?: number, className?: string }) => {
  // We use the imported User icon but rename it in the import or usage context if needed.
  // Since we imported { User, ... } above, let's just use it.
  // But wait, in the array `crimes` we used `UserIcon` but it wasn't defined.
  // Let's fix the imports.
  return (
      <svg 
        xmlns="http://www.w3.org/2000/svg" 
        width={size} 
        height={size} 
        viewBox="0 0 24 24" 
        fill="none" 
        stroke="currentColor" 
        strokeWidth="2" 
        strokeLinecap="round" 
        strokeLinejoin="round" 
        className={className}
      >
        <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
        <circle cx="12" cy="7" r="4"/>
      </svg>
  )
};
