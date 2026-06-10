import React from 'react';
import { motion } from 'framer-motion';
import { Workflow, BrainCircuit, Database, Layers, Infinity as InfinityIcon, ShieldCheck, Zap } from 'lucide-react';

const MotionDiv = motion.div as any;

export const AiEducation: React.FC = () => {
    return (
        <section className="relative py-32 bg-transparent overflow-hidden">
            <div className="container mx-auto px-4 relative z-10 flex flex-col items-center gap-16 md:gap-24">

                {/* --- ITEM 1: TRADITIONAL BUSINESS (GOLD/SILVER) --- */}
                <div className="flex flex-col items-center w-full max-w-lg">
                    <h3 className="text-2xl md:text-3xl font-serif text-white mb-8 lowercase tracking-wide text-center">
                        il lavoro <span className="font-bold text-[#94A3B8]">tradizionale...</span>
                    </h3>

                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="w-full h-[280px] relative drop-shadow-2xl mb-8"
                    >
                        {/* --- ANNOTATIONS (Desktop Only) --- */}
                        {/* Right Annotation */}
                        <div className="hidden lg:flex absolute right-[-280px] top-6 items-start gap-4 w-60">
                            <div className="w-3 h-3 rounded-full bg-[#94A3B8] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(148,163,184,0.5)]"></div>
                            <p className="text-sm text-gray-400 font-light leading-relaxed text-left">
                                <strong className="text-white font-medium">Il capitale umano</strong> viene sprecato in task meccanici ripetitivi invece che in strategia e pura creatività.
                            </p>
                        </div>

                        {/* Left Annotation 1 */}
                        <div className="hidden lg:flex absolute left-[-280px] top-6 items-start gap-4 w-60 flex-row-reverse text-right">
                            <div className="w-3 h-3 rounded-full bg-[#94A3B8] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(148,163,184,0.5)]"></div>
                            <p className="text-sm text-gray-400 font-light leading-relaxed">
                                <strong className="text-white font-medium">Il tempo</strong> è lineare: le persone hanno un limite fisico di ore. Per produrre il doppio, devi assumere il doppio.
                            </p>
                        </div>

                        {/* Graphic: Linear Box Process */}
                        <svg viewBox="0 0 400 300" className="w-full h-full overflow-visible">
                            <defs>
                                <linearGradient id="silverProcess" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" stopColor="#475569" />
                                    <stop offset="50%" stopColor="#94A3B8" />
                                    <stop offset="100%" stopColor="#CBD5E1" />
                                </linearGradient>
                            </defs>

                            <rect x="30" y="30" width="120" height="70" fill="url(#silverProcess)" rx="10" />
                            <text x="90" y="72" textAnchor="middle" fill="#0F172A" fontSize="16" fontWeight="bold">TASK 1</text>

                            <path d="M 160,65 H 205 M 197,57 L 205,65 L 197,73" stroke="#94A3B8" strokeWidth="4" fill="none" strokeLinecap="round" strokeLinejoin="round" />

                            <rect x="220" y="30" width="120" height="70" fill="url(#silverProcess)" rx="10" />
                            <text x="280" y="72" textAnchor="middle" fill="#0F172A" fontSize="16" fontWeight="bold">TASK 2</text>

                            <path d="M 280,110 V 145 M 272,137 L 280,145 L 288,137" stroke="#94A3B8" strokeWidth="4" fill="none" strokeLinecap="round" strokeLinejoin="round" />

                            <rect x="120" y="160" width="160" height="70" fill="url(#silverProcess)" rx="10" />
                            <text x="200" y="202" textAnchor="middle" fill="#0F172A" fontSize="16" fontWeight="bold">BOTTLENECK</text>
                        </svg>
                    </MotionDiv>
                </div>

                {/* --- ITEM 2: AI NETWORK (COMPLEX / SCALABLE) --- */}
                <div className="flex flex-col items-center w-full max-w-4xl">
                    <h3 className="text-xl md:text-2xl font-serif text-gray-400 mb-12 lowercase text-center">
                        ecco come <span className="text-white font-bold">funziona l'ai...</span>
                    </h3>

                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.95 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="w-full h-[300px] relative drop-shadow-2xl"
                    >
                        {/* Annotation */}
                        <div className="hidden lg:flex absolute right-[-240px] top-10 items-start gap-3 w-48">
                            <div className="w-2 h-2 rounded-full bg-[#FDE68A] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(253,230,138,0.5)]"></div>
                            <p className="text-xs text-gray-400 font-light leading-relaxed text-left">
                                <strong className="text-white font-medium">L'Agente AI</strong> lavora 24/7, parallelizza i processi, elabora centinaia di richieste in secondi e si auto-corregge. Costo infrastrutturale: quasi nullo.
                            </p>
                        </div>

                        <svg viewBox="0 0 800 400" className="w-full h-full overflow-visible">
                            <defs>
                                <radialGradient id="aiCoreGrad" cx="50%" cy="50%" r="50%">
                                    <stop offset="0%" stopColor="#FDE68A" />
                                    <stop offset="100%" stopColor="#D4AF37" />
                                </radialGradient>
                                <radialGradient id="dataNodeGrad" cx="50%" cy="50%" r="50%">
                                    <stop offset="0%" stopColor="#FFFFFF" />
                                    <stop offset="100%" stopColor="#94A3B8" />
                                </radialGradient>
                                <filter id="glowAi">
                                    <feGaussianBlur stdDeviation="6" result="coloredBlur" />
                                    <feMerge>
                                        <feMergeNode in="coloredBlur" />
                                        <feMergeNode in="SourceGraphic" />
                                    </feMerge>
                                </filter>
                            </defs>

                            {/* CONNECTIONS (FAST, PARALLEL) */}
                            <g stroke="#D4AF37" strokeWidth="2" opacity="0.6" filter="url(#glowAi)">
                                <line x1="400" y1="200" x2="200" y2="100" />
                                <line x1="400" y1="200" x2="600" y2="100" />
                                <line x1="400" y1="200" x2="200" y2="300" />
                                <line x1="400" y1="200" x2="600" y2="300" />
                                <line x1="400" y1="200" x2="400" y2="60" />
                                <line x1="400" y1="200" x2="400" y2="340" />
                            </g>

                            {/* NODES */}
                            {/* Peripheral Nodes (Data/Tasks) */}
                            <circle cx="200" cy="100" r="30" fill="url(#dataNodeGrad)" />
                            <circle cx="600" cy="100" r="30" fill="url(#dataNodeGrad)" />
                            <circle cx="200" cy="300" r="30" fill="url(#dataNodeGrad)" />
                            <circle cx="600" cy="300" r="30" fill="url(#dataNodeGrad)" />
                            <circle cx="400" cy="60" r="25" fill="url(#dataNodeGrad)" />
                            <circle cx="400" cy="340" r="25" fill="url(#dataNodeGrad)" />

                            <text x="200" y="105" textAnchor="middle" fill="#0F172A" fontSize="10" fontWeight="bold">EMAIL</text>
                            <text x="600" y="105" textAnchor="middle" fill="#0F172A" fontSize="10" fontWeight="bold">CRM</text>
                            <text x="200" y="305" textAnchor="middle" fill="#0F172A" fontSize="10" fontWeight="bold">SUPPORT</text>
                            <text x="600" y="305" textAnchor="middle" fill="#0F172A" fontSize="10" fontWeight="bold">REPORT</text>

                            {/* Center Core (AI Agent) */}
                            <circle cx="400" cy="200" r="60" fill="url(#aiCoreGrad)" filter="url(#glowAi)" />
                            <text x="400" y="195" textAnchor="middle" fill="#2A2312" fontSize="18" fontWeight="bold" fontFamily="monospace">AGENTE</text>
                            <text x="400" y="215" textAnchor="middle" fill="#2A2312" fontSize="18" fontWeight="bold" fontFamily="monospace">AI</text>

                            {/* Particles flowing to center */}
                            {[...Array(6)].map((_, i) => (
                                <motion.circle
                                    key={`p-${i}`}
                                    r="3"
                                    fill="#FFFFFF"
                                    initial={{ opacity: 0 }}
                                    animate={{
                                        opacity: [0, 1, 0],
                                        offsetDistance: ["0%", "100%"]
                                    }}
                                    transition={{
                                        duration: 1.5,
                                        repeat: Infinity,
                                        delay: i * 0.3,
                                    }}
                                    style={{
                                        offsetPath: `path('M ${i % 2 === 0 ? '200' : '600'},${i < 3 ? '100' : '300'} L 400,200')`
                                    }}
                                />
                            ))}
                        </svg>
                    </MotionDiv>
                </div>

                {/* --- ITEM 3: THE SOLUTION (GLOWING GOLD TEXT) --- */}
                <div className="flex flex-col items-center text-center mt-24 w-full">
                    <p className="text-xl md:text-2xl font-serif italic text-gray-500 mb-6 lowercase">
                        il risultato è l'unica cosa che conta:
                    </p>

                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.8 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="relative"
                    >
                        <div className="absolute inset-0 blur-[80px] bg-gold-500/5 rounded-full pointer-events-none"></div>

                        <h1 className="relative font-sans font-black text-5xl md:text-7xl lg:text-9xl tracking-tighter text-gray-200 drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] lowercase leading-none">
                            infrastruttura <br className="md:hidden" /> <span className="text-transparent bg-clip-text bg-gradient-to-b from-[#FAE8B6] via-[#D4AF37] to-[#855F23]">infinita.</span>
                        </h1>
                    </MotionDiv>

                    {/* --- STRATEGY CHECKLIST --- */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 30 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="mt-24 max-w-4xl mx-auto flex flex-col items-center gap-12"
                    >
                        <div className="flex flex-col items-start gap-6 pl-4 md:pl-0">
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Zero errori <span className="font-bold">umani</span></span>
                            </div>
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Scalabilità <span className="font-bold">istantanea</span></span>
                            </div>
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Margini di profitto <span className="font-bold">massimizzati</span></span>
                            </div>
                        </div>

                        <div className="text-center space-y-4 pt-4 px-4">
                            <p className="text-2xl md:text-3xl text-white font-light leading-relaxed mb-6 lowercase">
                                <span className="font-bold">chi non integra l'ai</span> <br />
                                è destinato a <span className="font-bold">scomparire</span> <br />
                                nei prossimi <span className="font-bold">3 anni...</span>
                            </p>
                        </div>
                    </MotionDiv>
                </div>

                {/* --- A DEEP DIVE INTO AI AGENTS --- */}
                <div className="w-full max-w-6xl mt-40 pt-32 relative z-20">
                    <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[80%] h-[1px] bg-gradient-to-r from-transparent via-slate-500/50 to-transparent"></div>

                    <div className="text-center mb-24">
                        <MotionDiv
                            initial={{ opacity: 0, y: 30 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 1 }}
                        >
                            <span className="inline-block px-4 py-2 border border-[#D4AF37]/30 rounded-full font-mono text-[10px] text-[#D4AF37] tracking-[0.3em] font-bold uppercase mb-8 shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                                Oltre la semplice automazione
                            </span>
                            <h2 className="text-5xl md:text-7xl font-serif text-white mb-8 tracking-tighter drop-shadow-2xl">
                                L'Anatomia di un <br className="md:hidden" />
                                <span className="font-bold" style={{
                                    backgroundImage: 'linear-gradient(90deg, #FFFFFF 0%, #D4AF37 50%, #FDE68A 100%)',
                                    WebkitBackgroundClip: 'text',
                                    color: 'transparent'
                                }}>Agente AI.</span>
                            </h2>
                            <p className="text-slate-400 font-light text-lg md:text-xl max-w-3xl mx-auto leading-relaxed">
                                Sgombriamo il campo dai malintesi: un <strong className="text-white font-medium">Agente AI</strong> non è un banale chatbot programmato per dire "ciao". È un'entità digitale complessa, dotata di capacità logiche, memoria persistente e accesso protetto agli strumenti operativi della tua azienda.
                            </p>
                        </MotionDiv>
                    </div>

                    {/* Educational Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-24 relative z-20">

                        {/* Box 1 - Silver + Blu */}
                        <MotionDiv
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: 0.1 }}
                            className="relative bg-gradient-to-br from-[#21314d] to-[#04070d] rounded-[24px] overflow-hidden border border-white/10 hover:border-slate-400/30 transition-all duration-700 group flex flex-col items-start h-full p-10 shadow-2xl"
                        >
                            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] mix-blend-overlay pointer-events-none"></div>
                            <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-duration-1000"></div>

                            <div className="flex items-center gap-5 relative z-10 mb-10">
                                <Workflow size={28} className="text-slate-400 group-hover:text-blue-400 transition-colors duration-500" strokeWidth={1} />
                                <div className="w-10 h-[1px] bg-slate-600/50"></div>
                                <BrainCircuit size={32} className="text-slate-300 group-hover:text-blue-300 transition-all duration-700" strokeWidth={1} />
                            </div>
                            
                            <div className="relative z-10 mt-auto">
                                <h3 className="text-2xl text-slate-100 font-serif font-light mb-4 tracking-wide group-hover:text-white transition-colors">
                                    Ragionamento Adattivo
                                </h3>
                                <p className="text-[15px] text-slate-400 font-light leading-relaxed">
                                    I software tradizionali <strong className="text-slate-200 font-normal">If/Then</strong> si bloccano al primo input imprevisto. Un Agente AI, invece, <strong className="text-blue-400 font-normal">comprende l'intento logico</strong>, analizza l'anomalia e trova autonomamente una strada alternativa.
                                </p>
                            </div>
                        </MotionDiv>

                        {/* Box 2 - Silver + Arancione (Bronzo Scuro) */}
                        <MotionDiv
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: 0.2 }}
                            className="relative bg-gradient-to-br from-[#3d271d] to-[#080403] rounded-[24px] overflow-hidden border border-white/10 hover:border-slate-400/30 transition-all duration-700 group flex flex-col items-start h-full p-10 shadow-2xl"
                        >
                            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] mix-blend-overlay pointer-events-none"></div>
                            <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-duration-1000"></div>

                            <div className="flex items-center gap-5 relative z-10 mb-10">
                                <Layers size={32} className="text-slate-300 group-hover:text-orange-400 transition-colors duration-500" strokeWidth={1} />
                            </div>
                            
                            <div className="relative z-10 mt-auto">
                                <h3 className="text-2xl text-slate-100 font-serif font-light mb-4 tracking-wide group-hover:text-white transition-colors">
                                    Memoria Aziendale
                                </h3>
                                <p className="text-[15px] text-slate-400 font-light leading-relaxed">
                                    L'Agente viene addestrato sui <strong className="text-slate-200 font-normal">tuoi specifici dataset</strong>: storici, CRM, procedure. Possiede la conoscenza millimetrica della tua azienda e aderisce a policy ferree.
                                </p>
                            </div>
                        </MotionDiv>

                        {/* Box 3 - Silver + Teal (Titanio Ossidato) */}
                        <MotionDiv
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: 0.3 }}
                            className="relative bg-gradient-to-br from-[#1d3331] to-[#030807] rounded-[24px] overflow-hidden border border-white/10 hover:border-slate-400/30 transition-all duration-700 group md:col-span-2 lg:col-span-1 flex flex-col items-start h-full p-10 shadow-2xl"
                        >
                            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] mix-blend-overlay pointer-events-none"></div>
                            <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-duration-1000"></div>

                            <div className="flex items-center gap-5 relative z-10 mb-10">
                                <InfinityIcon size={40} className="text-slate-300 group-hover:text-teal-400 transition-colors duration-500" strokeWidth={1} />
                            </div>
                            
                            <div className="relative z-10 mt-auto">
                                <h3 className="text-2xl text-slate-100 font-serif font-light mb-4 tracking-wide group-hover:text-white transition-colors">
                                    Scalabilità Asimmetrica
                                </h3>
                                <p className="text-[15px] text-slate-400 font-light leading-relaxed">
                                    Che l'azienda debba processare 10 pratiche o <strong className="text-slate-200 font-normal">10.000 richieste</strong>, l'Agente clona la propria capacità in tempo reale. Nessun server crash, nessun ritardo.
                                </p>
                            </div>
                        </MotionDiv>

                    </div>

                    {/* Bottom Summary - Shrinked and Minimal Lume */}
                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.98 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.8 }}
                        className="w-full max-w-4xl mx-auto relative rounded-3xl p-8 md:p-12 border border-white/10 overflow-hidden flex flex-col items-center justify-center text-center group"
                        style={{
                            background: 'linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)'
                        }}
                    >
                        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-5 mix-blend-overlay pointer-events-none"></div>

                        <div className="relative z-10 w-full flex flex-col items-center">
                            <h3 className="text-2xl md:text-3xl font-serif text-slate-900 mb-4 font-black leading-tight uppercase relative">
                                Implementare l'AI non significa "installare un software".
                            </h3>
                            <p className="text-slate-600 font-medium text-lg md:text-xl mb-8 max-w-2xl px-4">
                                Significa assumere il collaboratore più instancabile, rapido e preciso della storia, <span className="text-amber-700 font-black">per sempre.</span>
                            </p>

                            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 w-full text-left bg-slate-100 p-4 rounded-xl border border-slate-200 shadow-sm">
                                <div className="space-y-1 p-3 bg-white rounded-lg border border-slate-200 shadow-sm">
                                    <div className="text-2xl font-black text-slate-900">24/7</div>
                                    <div className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-widest">Disponibilità</div>
                                </div>
                                <div className="space-y-1 p-3 bg-white rounded-lg border border-slate-200 shadow-sm">
                                    <div className="text-2xl font-black text-slate-900">0.05s</div>
                                    <div className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-widest">Reazione</div>
                                </div>
                                <div className="space-y-1 p-3 bg-white rounded-lg border border-slate-200 shadow-sm">
                                    <div className="text-2xl font-black text-slate-900">100%</div>
                                    <div className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-widest">Precisione</div>
                                </div>
                                <div className="space-y-1 p-3 bg-slate-900 rounded-lg border border-slate-800 shadow-md">
                                    <div className="text-2xl font-black text-amber-500">∞</div>
                                    <div className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-widest">ROI Reale</div>
                                </div>
                            </div>
                        </div>
                    </MotionDiv>
                </div>

            </div>
        </section>
    );
};
