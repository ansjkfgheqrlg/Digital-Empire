
import React from 'react';
import { motion } from 'framer-motion';
import { 
  XCircle,
  TrendingUp,
  ArrowDown,
  MousePointer2,
  AlertTriangle,
  Ban,
  Calculator,
  Users,
  ShoppingCart,
  FileText,
  CheckCircle2,
  BrainCircuit,
  Flame,
  AlertOctagon,
  Lightbulb,
  ShieldCheck,
  MousePointerClick,
  X,
  Check,
  Lock,
  ArrowRight,
  ChevronRight
} from 'lucide-react';
import { GoldButton } from './ui/GoldButton';
import { DustCanvas } from './ui/DustCanvas';

const MotionDiv = motion.div as any;

export const CroFunnelSection: React.FC = () => {
  
  // Gradienti Tipografici
  const goldGradient = {
    backgroundImage: 'linear-gradient(180deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(212,175,55,0.2))'
  };

  const silverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 60%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  };

  return (
    <section className="relative z-20 pb-32 overflow-hidden bg-black -mt-20 pt-20">
      
      {/* Background Decorativo che continua dalla hero */}
      <div className="absolute top-0 left-0 w-full h-full pointer-events-none z-0">
         <div className="absolute inset-0 bg-gradient-to-b from-black via-[#050505] to-black opacity-100"></div>
         <DustCanvas />
      </div>

      <div className="container mx-auto px-6 max-w-7xl relative z-10">
        
        {/* --- MOVED BLOCCO 3: EDUCAZIONE STRATEGICA (THE MISTAKE - RED/SILVER MIX) --- */}
        <div className="mb-40 pt-10">
            <div className="text-center mb-16">
                 <h2 className="font-serif text-3xl md:text-5xl text-white font-bold leading-tight lowercase mb-6">
                    l'errore che ti costa <br/>
                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-red-600">il 70% del budget</span>.
                 </h2>
                 <p className="text-gray-400 text-lg max-w-2xl mx-auto font-light leading-relaxed lowercase">
                    mandare traffico "freddo" (ads) direttamente a una pagina di acquisto (checkout) 
                    è un suicidio commerciale. il cliente non ti conosce. non si fida. non compra.
                 </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl mx-auto">
                
                {/* 1. WRONG WAY (SILVER mixed with RED) */}
                <div 
                    className="relative p-[1px] rounded-2xl group transition-all duration-500 shadow-[0_0_30px_rgba(220,38,38,0.05)] hover:shadow-[0_0_50px_rgba(220,38,38,0.2)]"
                    style={{
                        background: 'linear-gradient(135deg, #475569 0%, #cbd5e1 30%, #ef4444 50%, #7f1d1d 75%, #475569 100%)'
                    }}
                >
                    <div className="h-full bg-[#0a0a0a] rounded-[15px] p-8 relative overflow-hidden">
                        {/* Inner Red Glow */}
                        <div className="absolute top-0 right-0 w-[200px] h-[200px] bg-red-500/10 blur-[80px] pointer-events-none"></div>
                        
                        <div className="flex justify-between items-start mb-8">
                            <h3 className="text-red-400 font-serif text-2xl lowercase font-bold tracking-tight">approccio amatoriale</h3>
                            <AlertTriangle size={24} className="text-red-500 opacity-80"/>
                        </div>

                        {/* Visual Flow */}
                        <div className="flex items-center justify-between gap-4 mb-8 px-2 relative">
                             {/* Linea di base rossa sbiadita */}
                             <div className="absolute top-1/2 left-0 w-full h-[1px] bg-red-900/30 z-0"></div>

                             <div className="flex flex-col items-center gap-3 relative z-10">
                                 <div className="w-12 h-12 bg-[#120505] rounded-xl flex items-center justify-center border border-red-900/50 text-blue-400 shadow-lg">
                                    <MousePointer2 size={18}/>
                                 </div>
                                 <span className="text-[10px] font-mono text-gray-500">ads</span>
                             </div>

                             <div className="relative z-10 bg-[#0a0a0a] px-2">
                                 <XCircle size={20} className="text-red-500"/>
                             </div>

                             <div className="flex flex-col items-center gap-3 relative z-10 opacity-50">
                                 <div className="w-12 h-12 bg-[#120505] rounded-xl flex items-center justify-center border border-red-900/30 text-gray-500">
                                    <ShoppingCart size={18}/>
                                 </div>
                                 <span className="text-[10px] font-mono text-gray-600 line-through decoration-red-500">checkout</span>
                             </div>
                        </div>

                        <p className="text-sm text-gray-400 leading-relaxed border-t border-white/5 pt-6 lowercase font-light">
                            il cliente arriva, vede il prezzo, si spaventa e se ne va. hai pagato il click per niente.
                            <br/><span className="text-red-400 font-bold">tasso di conversione: &lt;0.5%.</span>
                        </p>
                    </div>
                </div>

                {/* 2. RIGHT WAY (SILVER mixed with GREEN) */}
                <div 
                    className="relative p-[1px] rounded-2xl group transition-all duration-500 shadow-[0_0_30px_rgba(16,185,129,0.1)] hover:shadow-[0_0_60px_rgba(16,185,129,0.2)]"
                    style={{
                        background: 'linear-gradient(135deg, #475569 0%, #cbd5e1 30%, #10b981 50%, #064e3b 75%, #475569 100%)'
                    }}
                >
                    <div className="h-full bg-[#0a0a0a] rounded-[15px] p-8 relative overflow-hidden">
                        {/* Inner Green Glow */}
                        <div className="absolute top-0 right-0 w-[200px] h-[200px] bg-emerald-500/10 blur-[80px] pointer-events-none"></div>

                        <div className="flex justify-between items-start mb-8">
                            <h3 className="text-emerald-400 font-serif text-2xl lowercase font-bold tracking-tight">approccio empire</h3>
                            <CheckCircle2 size={24} className="text-emerald-500 opacity-80"/>
                        </div>

                        {/* Visual Flow */}
                        <div className="flex items-center justify-between gap-2 mb-8 px-2 relative">
                             {/* Linea di base verde */}
                             <div className="absolute top-1/2 left-0 w-full h-[1px] bg-emerald-900/50 z-0"></div>

                             <div className="flex flex-col items-center gap-3 relative z-10">
                                 <div className="w-10 h-10 bg-[#021c10] rounded-xl flex items-center justify-center border border-emerald-900/50 text-blue-400">
                                    <MousePointer2 size={16}/>
                                 </div>
                                 <span className="text-[10px] font-mono text-gray-500">ads</span>
                             </div>

                             {/* THE BRIDGE */}
                             <div className="flex flex-col items-center gap-3 relative z-10 -mt-6">
                                 <div className="px-2 py-0.5 bg-emerald-950 border border-emerald-500/50 rounded text-[9px] text-emerald-400 uppercase tracking-widest font-bold mb-1 shadow-[0_0_10px_rgba(16,185,129,0.3)]">PONTE</div>
                                 <div className="w-14 h-14 bg-gradient-to-b from-[#022c22] to-[#064e3b] rounded-xl flex items-center justify-center border border-emerald-400 text-white shadow-[0_0_20px_rgba(16,185,129,0.2)]">
                                    <FileText size={24}/>
                                 </div>
                                 <span className="text-[10px] font-mono text-white font-bold">sales page</span>
                             </div>

                             <div className="flex flex-col items-center gap-3 relative z-10">
                                 <div className="w-10 h-10 bg-[#021c10] rounded-xl flex items-center justify-center border border-emerald-900/50 text-white">
                                    <ShoppingCart size={16}/>
                                 </div>
                                 <span className="text-[10px] font-mono text-gray-500">soldi</span>
                             </div>
                        </div>

                        <p className="text-sm text-gray-400 leading-relaxed border-t border-white/5 pt-6 lowercase font-light">
                            la landing page agisce da "venditore digitale". educa, riscalda, crea desiderio e SOLO ALLA FINE chiede i soldi.
                            <br/><span className="text-emerald-400 font-bold">tasso di conversione: 3% - 8%.</span>
                        </p>
                    </div>
                </div>
            </div>

            {/* NEW EXPLANATION BLOCK - ADDED HERE */}
            <div className="mt-16 text-center">
                <MotionDiv
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    className="max-w-4xl mx-auto px-6"
                >
                    {/* Visual connector */}
                    <div className="flex justify-center mb-8 opacity-30">
                        <div className="h-12 w-[1px] bg-gradient-to-b from-white to-transparent"></div>
                    </div>

                    <p className="font-serif text-2xl md:text-3xl text-gray-200 leading-relaxed lowercase">
                        il <span className="text-red-400 italic font-medium">dilettante</span> spera che il cliente capisca da solo.<br />
                        l'<span className="text-emerald-400 italic font-medium">esperto</span> lo prende per mano e lo accompagna alla cassa.
                    </p>
                    
                    <p className="mt-6 text-sm md:text-base text-gray-500 font-light max-w-2xl mx-auto font-mono lowercase tracking-wide">
                        eliminare le distrazioni aumenta il focus. aumentare il focus aumenta il fatturato. <br/>
                        è matematica, non magia.
                    </p>
                </MotionDiv>
            </div>
            
        </div>

        {/* --- BLOCCO 1: LA SPERANZA NON È UNA STRATEGIA (UPDATED: FONT-SANS & LOWERCASE) --- */}
        <div className="py-20 flex flex-col items-center text-center">
            
            <MotionDiv 
               initial={{ opacity: 0, scale: 0.9 }}
               whileInView={{ opacity: 1, scale: 1 }}
               viewport={{ once: true }}
               className="mb-10 relative group"
            >
               {/* Icona "Fingers Crossed" barrata */}
               <div className="relative w-32 h-32 flex items-center justify-center bg-white/[0.03] rounded-full border border-white/10 backdrop-blur-md shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                   {/* Dita Incrociate (Emoji Grayscale) */}
                   <span className="text-6xl grayscale opacity-60" style={{ filter: 'grayscale(100%) brightness(1.2)' }}>🤞</span>
                   
                   {/* Divieto Rosso */}
                   <div className="absolute inset-0 flex items-center justify-center opacity-80">
                      <Ban className="text-red-600 w-20 h-20 drop-shadow-[0_0_15px_rgba(220,38,38,0.5)]" strokeWidth={1.5} />
                   </div>
               </div>
            </MotionDiv>

            <MotionDiv
               initial={{ opacity: 0, y: 20 }}
               whileInView={{ opacity: 1, y: 0 }}
               viewport={{ once: true }}
               className="max-w-5xl"
            >
               <h2 className="font-sans text-4xl md:text-6xl lg:text-7xl font-light tracking-tighter leading-[1.0] mb-8 text-white lowercase">
                   <span className="font-bold">la speranza</span> <span className="text-gray-600 font-light">non è una</span> <br/>
                   <span style={goldGradient as any} className="font-black">strategia aziendale.</span>
               </h2>
               
               <p className="font-sans text-gray-400 text-lg md:text-xl font-light leading-relaxed max-w-2xl mx-auto lowercase">
                   incrociare le dita dopo aver lanciato il sito non porta fatturato. <br/>
                   il mercato non premia gli ottimisti. premia gli <span className="text-white font-bold border-b border-white/20 pb-0.5">ingegneri</span>.
               </p>
            </MotionDiv>
        </div>


        {/* --- BLOCCO 2: C.R.O. (Dispersivo vs Chirurgico) - OPEN AIR LAYOUT --- */}
        <div className="relative mb-32 pb-20">
            
            {/* Ambient Light for Open Layout */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-gold-500/5 blur-[120px] rounded-full pointer-events-none -z-10"></div>
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-white/5 blur-[120px] rounded-full pointer-events-none -z-10"></div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center relative z-10">
            
            {/* LEFT: TEXT EXPLANATION & CARDS */}
            <div>
                <h3 className="text-5xl md:text-7xl font-serif text-white mb-8 leading-[0.9] tracking-tighter">
                    <span style={goldGradient as any} className="font-black block mb-2">C.R.O.</span>
                    <span style={silverGradient as any} className="text-2xl md:text-4xl font-light block lowercase">conversion rate optimization</span>
                </h3>
                
                <p className="text-xl text-gray-400 font-light lowercase mb-8">
                    non serve più traffico. serve più efficienza.
                </p>

                <div className="space-y-8 text-lg text-gray-400 font-light lowercase leading-relaxed mb-10">
                    <p className="border-l-2 border-gold-500 pl-6 italic text-gray-300">
                        "se raddoppi il tasso di conversione del tuo funnel (dall'1% al 2%), hai letteralmente <strong>dimezzato il costo di acquisizione clienti</strong> senza spendere un centesimo in più in pubblicità."
                    </p>
                    <p>
                        il <span className="text-white font-bold">funnel ingegnerizzato</span> è l'applicazione pratica del cro. non è "arte". è un percorso a imbuto progettato per eliminare le distrazioni e forzare una decisione.
                    </p>
                </div>

                {/* COMPARISON CARDS */}
                <div className="grid grid-cols-2 gap-4">
                    {/* SITO TRADIZIONALE */}
                    <div className="p-6 bg-[#0a0a0a] border border-white/10 rounded-2xl backdrop-blur-sm group hover:border-red-500/30 transition-colors shadow-lg">
                        <div className="text-[10px] font-mono text-gray-500 uppercase tracking-widest mb-3 lowercase">sito tradizionale</div>
                        <div className="text-2xl font-serif text-red-400 mb-2 font-medium tracking-tight">DISPERSIVO</div>
                        <div className="text-xs text-gray-600 lowercase group-hover:text-gray-500 transition-colors">troppi link, zero focus.</div>
                    </div>
                    
                    {/* FUNNEL EMPIRE */}
                    <div className="p-6 bg-gold-950/20 border border-gold-500/30 rounded-2xl backdrop-blur-sm relative overflow-hidden shadow-[0_0_30px_rgba(212,175,55,0.05)]">
                        <div className="absolute inset-0 bg-gold-500/5 animate-pulse"></div>
                        <div className="relative z-10">
                            <div className="text-[10px] font-mono text-gold-500 uppercase tracking-widest mb-3 lowercase">funnel empire</div>
                            <div className="text-2xl font-serif text-white mb-2 font-medium tracking-tight">CHIRURGICO</div>
                            <div className="text-xs text-gray-400 lowercase">una sola via d'uscita: l'acquisto.</div>
                        </div>
                    </div>
                </div>
            </div>

            {/* RIGHT: THE CALCULATOR DASHBOARD (UPDATED WITH GOLD/SILVER BORDER) */}
            <div className="relative group">
                
                {/* 1. OUTER BORDER CONTAINER (Gradient) */}
                <div 
                    className="relative p-[2px] rounded-[32px] overflow-hidden shadow-[0_0_40px_rgba(212,175,55,0.15)]"
                    style={{
                        background: 'linear-gradient(135deg, #E2E8F0 0%, #94A3B8 20%, #FDE68A 45%, #D4AF37 55%, #B45309 70%, #E2E8F0 100%)',
                    }}
                >
                    {/* 2. INNER CONTAINER (Black Background) */}
                    <div className="bg-[#080808] p-8 md:p-12 rounded-[30px] relative backdrop-blur-xl h-full">
                        
                        <div className="space-y-2 font-mono text-sm relative z-10">
                            
                            {/* ROW 1: TRAFFIC */}
                            <div className="flex items-center justify-between p-5 bg-[#0f0f0f] rounded-xl border border-white/5 mb-4 shadow-inner">
                                <span className="text-gray-500 lowercase">traffico (visitatori)</span>
                                <span className="text-white font-bold tracking-widest text-lg">10.000</span>
                            </div>
                            
                            <div className="flex justify-center text-gray-700 py-2"><XCircle size={16} strokeWidth={1.5} /></div>
                            
                            {/* ROW 2: CONVERSION RATE (GOLD) */}
                            <div className="relative overflow-hidden group mb-4">
                                <div className="relative flex items-center justify-between p-5 bg-gold-900/10 rounded-xl border border-gold-500/40 shadow-[0_0_30px_rgba(212,175,55,0.05)]">
                                    <div className="flex items-center gap-3">
                                        <MousePointer2 size={18} className="text-gold-500" />
                                        <span className="text-gold-100 font-bold lowercase">tasso conversione (cro)</span>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span className="text-gray-600 line-through text-xs font-light">0.8%</span>
                                        <ArrowDown size={14} className="text-gold-500 -rotate-90"/>
                                        <span className="text-white font-black text-2xl">2.4%</span>
                                    </div>
                                </div>
                            </div>

                            <div className="flex justify-center text-gray-700 py-2">=</div>

                            {/* ROW 3: PROFIT (GREEN) */}
                            <div className="flex items-center justify-between p-6 bg-gradient-to-r from-[#051c14] to-[#022c22] rounded-2xl border border-emerald-500/30 shadow-[0_10px_40px_rgba(16,185,129,0.1)]">
                                <span className="text-emerald-400 font-bold text-xs font-mono lowercase tracking-widest">
                                    nuovi clienti
                                </span>
                                <div className="flex items-center gap-4">
                                    <TrendingUp size={24} className="text-emerald-500" />
                                    <span className="text-5xl text-white font-black tracking-tighter">240</span>
                                    <span className="text-[10px] text-emerald-400 bg-emerald-900/50 px-2 py-1 rounded border border-emerald-500/20 font-bold lowercase">
                                        (3x profitto)
                                    </span>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            </div>
        </div>

        {/* --- BLOCCO 4: IL PROTOCOLLO A.P.S.O.C. (OPEN LAYOUT REVISED - SILVER FILLED) --- */}
        <div className="relative mt-0 mb-20">
            
            {/* Header Area - Floating */}
            <div className="max-w-5xl mx-auto px-6 mb-16 text-center relative z-10">
                 <div className="inline-flex items-center gap-2 px-3 py-1 border border-gold-500/30 rounded-full bg-gold-950/10 mb-6 backdrop-blur-sm shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                     <BrainCircuit size={12} className="text-gold-500"/>
                     <span className="text-[10px] font-mono text-gold-500 uppercase tracking-[0.3em] font-black">
                         Psychology Engine
                     </span>
                 </div>
                 <h3 className="font-serif text-4xl md:text-6xl text-white lowercase leading-none">
                     protocollo <span className="text-transparent bg-clip-text bg-gradient-to-b from-gold-100 via-gold-400 to-gold-700 drop-shadow-sm">a.p.s.o.c.</span>
                 </h3>
                 <p className="text-gray-500 text-sm max-w-xl mx-auto font-light lowercase mt-4 leading-relaxed">
                     non scriviamo "testi carini". ingegnerizziamo le parole seguendo la sequenza esatta 
                     con cui il cervello umano prende decisioni d'acquisto.
                 </p>
            </div>

            {/* THE 5 STEPS - FILLED SILVER CARDS */}
            <div className="max-w-7xl mx-auto px-6 space-y-4 relative z-10">
                
                {[
                    {
                        letter: "A",
                        title: "Attenzione (the hook)",
                        desc: "ferma lo scroll. rompi il pattern. l'obiettivo della prima frase è solo far leggere la seconda. se non catturi l'attenzione in 0.3 secondi, hai perso.",
                        icon: Flame,
                        color: "text-red-600", // Darkened for silver bg
                        bullets: [
                            "stop scrolling",
                            "rottura del pattern",
                            "impatto visivo"
                        ]
                    },
                    {
                        letter: "P",
                        title: "Problema (the pain)",
                        desc: "agita il dolore. mostra al cliente che capisci il suo problema meglio di lui. crea empatia istantanea dimostrando che conosci le sue frustrazioni notturne.",
                        icon: AlertOctagon,
                        color: "text-orange-600", // Darkened for silver bg
                        bullets: [
                            "empatia profonda",
                            "agitazione dolore",
                            "validazione"
                        ]
                    },
                    {
                        letter: "S",
                        title: "Soluzione (the product)",
                        desc: "presenta il tuo prodotto non come un 'oggetto', ma come l'unica via d'uscita logica al dolore. non vendere caratteristiche, vendi la nuova identità del cliente.",
                        icon: Lightbulb,
                        color: "text-amber-600", // Darkened for silver bg
                        bullets: [
                            "nuovo veicolo",
                            "logica unica",
                            "beneficio primario"
                        ]
                    },
                    {
                        letter: "O",
                        title: "Obiezioni (the shield)",
                        desc: "'costa troppo?', 'funzionerà per me?'. anticipa ogni dubbio e distruggilo prima che nasca. usa garanzie, case study e logica inattaccabile per disarmare lo scetticismo.",
                        icon: ShieldCheck,
                        color: "text-blue-600", // Darkened for silver bg
                        bullets: [
                            "garanzia di ferro",
                            "riprova sociale",
                            "zero rischi"
                        ]
                    },
                    {
                        letter: "C",
                        title: "Call to Action (the command)",
                        desc: "dì loro esattamente cosa fare. non 'se vuoi, clicca qui'. usa imperativi: 'acquista ora', 'inizia la scalata'. la confusione uccide la conversione. sii chiaro.",
                        icon: MousePointerClick,
                        color: "text-yellow-700", // Darkened for silver bg
                        bullets: [
                            "comando diretto",
                            "urgenza motivata",
                            "chiarezza assoluta"
                        ]
                    }
                ].map((step, idx) => (
                    <div 
                        key={idx}
                        className={`group relative p-6 md:p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40
                            bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1]
                            hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)]
                        `}
                    >
                        {/* Metallic Noise Texture for "Extreme Quality" */}
                        <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                        
                        {/* Shine Effect */}
                        <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                        <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                        {/* GRID LAYOUT: Left (Content) - Right (Bullets) */}
                        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
                            
                            {/* COL 1: Main Content (Letters + Text) */}
                            <div className="lg:col-span-8 flex items-start gap-6 md:gap-10">
                                {/* Big Letter Watermark - Darker now */}
                                <div className="flex-shrink-0 w-16 md:w-20 text-center">
                                    <span className={`font-serif font-black text-6xl md:text-7xl leading-none transition-all duration-500 text-slate-900/10 group-hover:text-slate-900/20 group-hover:scale-110`}>
                                        {step.letter}
                                    </span>
                                </div>

                                <div className="flex-grow pt-2">
                                    <div className="flex items-center gap-3 mb-3">
                                        {/* Title - Dark */}
                                        <h4 className={`font-bold text-lg md:text-xl lowercase text-slate-900`}>
                                            {step.title}
                                        </h4>
                                        {/* Icon - Colored */}
                                        <step.icon size={16} className={`${step.color} opacity-100`}/>
                                    </div>
                                    {/* Description - Dark Gray */}
                                    <p className="text-sm md:text-base text-slate-700 font-medium lowercase leading-relaxed max-w-2xl">
                                        {step.desc}
                                    </p>
                                </div>
                            </div>

                            {/* COL 2: Bullet Points (Visible on Desktop) */}
                            <div className="hidden lg:flex lg:col-span-4 border-l border-slate-900/10 pl-8 flex-col justify-center h-full">
                                <h5 className="font-mono text-[10px] uppercase tracking-widest text-slate-500 mb-4 font-black">
                                    key tactics
                                </h5>
                                <ul className="space-y-3">
                                    {step.bullets.map((bullet, bIdx) => (
                                        <li key={bIdx} className="flex items-center gap-3 text-xs md:text-sm text-slate-800 font-mono lowercase font-bold">
                                            {/* Bullet dot */}
                                            <div className={`w-1.5 h-1.5 rounded-full bg-slate-900`}></div>
                                            {bullet}
                                        </li>
                                    ))}
                                </ul>
                            </div>

                        </div>
                    </div>
                ))}

            </div>
        </div>

      </div>
    </section>
  );
};
