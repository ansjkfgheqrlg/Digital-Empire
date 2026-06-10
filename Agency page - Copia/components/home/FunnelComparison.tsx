
import React from 'react';
import { motion } from 'framer-motion';

const MotionDiv = motion.div as any;

export const FunnelComparison: React.FC = () => {

    return (
        <section className="relative py-32 bg-transparent overflow-hidden">

            <div className="container mx-auto px-4 relative z-10 flex flex-col items-center gap-16 md:gap-24">

                {/* --- ITEM 1: SIMPLE FUNNEL (GOLD) --- */}
                <div className="flex flex-col items-center w-full max-w-lg">
                    <h3 className="text-2xl md:text-3xl font-serif text-white mb-8 lowercase tracking-wide text-center">
                        c'è chi fa <span className="font-bold text-[#FDE68A]">questo...</span>
                    </h3>

                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="w-full h-[220px] relative drop-shadow-2xl mb-8"
                    >
                        {/* --- ANNOTATIONS (Desktop Only) --- */}

                        {/* Right Annotation: Step Definition */}
                        <div className="hidden lg:flex absolute right-[-240px] top-4 items-start gap-3 w-48">
                            <div className="w-2 h-2 rounded-full bg-[#FDE68A] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(253,230,138,0.5)]"></div>
                            <p className="text-xs text-gray-400 font-light leading-relaxed text-left">
                                <strong className="text-white font-medium">Lo step</strong> è il punto in cui il tuo potenziale cliente si trova in quel preciso momento.
                            </p>
                        </div>

                        {/* Left Annotation 1: CRO context */}
                        <div className="hidden lg:flex absolute left-[-240px] top-4 items-start gap-3 w-48 flex-row-reverse text-right">
                            <div className="w-2 h-2 rounded-full bg-[#FDE68A] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(253,230,138,0.5)]"></div>
                            <p className="text-xs text-gray-400 font-light leading-relaxed">
                                Ogni step ha un <strong className="text-white font-medium">tasso di conversione</strong> che può essere migliorato drasticamente attraverso il CRO.
                            </p>
                        </div>

                        {/* Left Annotation 2: Conversion Rate Definition */}
                        <div className="hidden lg:flex absolute left-[-240px] top-28 items-start gap-3 w-48 flex-row-reverse text-right">
                            <div className="w-2 h-2 rounded-full bg-[#FDE68A] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(253,230,138,0.5)]"></div>
                            <p className="text-xs text-gray-400 font-light leading-relaxed">
                                <strong className="text-white font-medium">Tasso di conversione</strong> = persone che passano allo step successivo. Bisogna alzare questo numero.
                            </p>
                        </div>

                        <svg viewBox="0 0 400 300" className="w-full h-full overflow-visible">
                            <defs>
                                <linearGradient id="goldFunnelSimple" x1="0%" y1="0%" x2="0%" y2="100%">
                                    <stop offset="0%" stopColor="#FDE68A" />
                                    <stop offset="50%" stopColor="#D4AF37" />
                                    <stop offset="100%" stopColor="#92400E" />
                                </linearGradient>
                            </defs>

                            {/* FUNNEL TRAPEZOIDS (STEP 1, 2, 3) */}
                            {/* Step 1 */}
                            <path d="M 40,20 L 360,20 L 320,80 L 80,80 Z" fill="url(#goldFunnelSimple)" stroke="#FDE68A" strokeWidth="1" />
                            <text x="200" y="55" textAnchor="middle" fill="#2A2312" fontSize="18" fontWeight="bold" fontFamily="sans-serif">STEP 1</text>
                            <path d="M 200,85 L 190,95 L 210,95 Z" fill="#D4AF37" />

                            {/* Step 2 */}
                            <path d="M 80,100 L 320,100 L 280,160 L 120,160 Z" fill="url(#goldFunnelSimple)" stroke="#FDE68A" strokeWidth="1" />
                            <text x="200" y="135" textAnchor="middle" fill="#2A2312" fontSize="18" fontWeight="bold" fontFamily="sans-serif">STEP 2</text>
                            <path d="M 200,165 L 190,175 L 210,175 Z" fill="#D4AF37" />

                            {/* Step 3 */}
                            <path d="M 120,180 L 280,180 L 240,240 L 160,240 Z" fill="url(#goldFunnelSimple)" stroke="#FDE68A" strokeWidth="1" />
                            <text x="200" y="215" textAnchor="middle" fill="#2A2312" fontSize="18" fontWeight="bold" fontFamily="sans-serif">STEP 3</text>
                        </svg>
                    </MotionDiv>
                </div>

                {/* --- ITEM 2: COMPLEX NETWORK (WEB) --- */}
                <div className="flex flex-col items-center w-full max-w-4xl">
                    <h3 className="text-xl md:text-2xl font-serif text-gray-400 mb-12 lowercase text-center">
                        poi c'è chi fa <span className="text-white font-bold">questo...</span>
                    </h3>

                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.95 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="w-full h-[300px] relative drop-shadow-2xl"
                    >
                        {/* Annotation: Funnel Definition */}
                        <div className="hidden lg:flex absolute right-[-240px] top-10 items-start gap-3 w-48">
                            <div className="w-2 h-2 rounded-full bg-[#FDE68A] mt-1.5 flex-shrink-0 shadow-[0_0_10px_rgba(253,230,138,0.5)]"></div>
                            <p className="text-xs text-gray-400 font-light leading-relaxed text-left">
                                <strong className="text-white font-medium">Il funnel</strong> è il percorso che il tuo cliente compie dal momento in cui ti trova online (es. post, ad) fino all'acquisto.
                            </p>
                        </div>

                        <svg viewBox="0 0 800 400" className="w-full h-full overflow-visible">
                            <defs>
                                <radialGradient id="nodeGrad" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                                    <stop offset="0%" stopColor="#FFFFFF" />
                                    <stop offset="100%" stopColor="#94A3B8" />
                                </radialGradient>
                            </defs>

                            {/* CONNECTIONS (DASHED, CHAOTIC) */}
                            <g stroke="#475569" strokeWidth="1" strokeDasharray="5,5" opacity="0.5">
                                <line x1="120" y1="80" x2="350" y2="150" />
                                <line x1="120" y1="80" x2="250" y2="300" />
                                <line x1="680" y1="80" x2="450" y2="150" />
                                <line x1="680" y1="80" x2="550" y2="300" />
                                <line x1="350" y1="150" x2="450" y2="150" />
                                <line x1="350" y1="150" x2="400" y2="250" />
                                <line x1="450" y1="150" x2="400" y2="250" />
                                <line x1="250" y1="300" x2="400" y2="250" />
                                <line x1="550" y1="300" x2="400" y2="250" />
                                <line x1="400" y1="250" x2="400" y2="380" />
                            </g>

                            {/* NODES */}
                            <g>
                                <rect x="50" y="50" width="140" height="60" rx="10" fill="url(#nodeGrad)" stroke="#E2E8F0" />
                                <text x="120" y="85" textAnchor="middle" fill="#0F172A" fontSize="14" fontWeight="bold">ENTRATA 1</text>
                            </g>
                            <g>
                                <rect x="610" y="50" width="140" height="60" rx="10" fill="url(#nodeGrad)" stroke="#E2E8F0" />
                                <text x="680" y="85" textAnchor="middle" fill="#0F172A" fontSize="14" fontWeight="bold">ENTRATA 2</text>
                            </g>
                            <g>
                                <rect x="280" y="120" width="140" height="60" rx="6" fill="#F1F5F9" stroke="#94A3B8" />
                                <text x="350" y="155" textAnchor="middle" fill="#334155" fontSize="12" fontWeight="bold">STEP 1</text>
                            </g>
                            <g>
                                <rect x="330" y="220" width="140" height="60" rx="6" fill="#F1F5F9" stroke="#94A3B8" />
                                <text x="400" y="255" textAnchor="middle" fill="#334155" fontSize="12" fontWeight="bold">STEP 2</text>
                            </g>
                            <g>
                                <rect x="180" y="270" width="140" height="60" rx="6" fill="#F1F5F9" stroke="#94A3B8" />
                                <text x="250" y="305" textAnchor="middle" fill="#334155" fontSize="12" fontWeight="bold">STEP 4</text>
                            </g>
                            <g>
                                <rect x="480" y="270" width="140" height="60" rx="6" fill="#F1F5F9" stroke="#94A3B8" />
                                <text x="550" y="305" textAnchor="middle" fill="#334155" fontSize="12" fontWeight="bold">STEP A</text>
                            </g>
                            <g>
                                <rect x="330" y="350" width="140" height="50" rx="6" fill="#F1F5F9" stroke="#94A3B8" opacity="0.8" />
                                <text x="400" y="380" textAnchor="middle" fill="#334155" fontSize="12" fontWeight="bold">STEP 5</text>
                            </g>
                        </svg>
                    </MotionDiv>
                </div>

                {/* --- ITEM 3: THE SOLUTION (GLOWING GOLD TEXT) --- */}
                <div className="flex flex-col items-center text-center mt-24 w-full">
                    <p className="text-xl md:text-2xl font-serif italic text-gray-500 mb-6 lowercase">
                        e poi c'è chi fa questo:
                    </p>

                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.8 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="relative"
                    >
                        <div className="absolute inset-0 blur-[80px] bg-gold-500/5 rounded-full pointer-events-none"></div>

                        <h1 className="relative font-sans font-black text-5xl md:text-7xl lg:text-9xl tracking-tighter text-gray-200 drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] lowercase leading-none">
                            quello che <br className="md:hidden" /> <span className="text-transparent bg-clip-text bg-gradient-to-b from-[#FAE8B6] via-[#D4AF37] to-[#855F23]">funziona.</span>
                        </h1>
                    </MotionDiv>

                    {/* --- STRATEGY CHECKLIST (KEPT AS IS) --- */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 30 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="mt-24 max-w-4xl mx-auto flex flex-col items-center gap-12"
                    >
                        {/* ... (Existing checklist content) ... */}
                        <div className="flex flex-col items-start gap-6 pl-4 md:pl-0">
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Il funnel <span className="font-bold">giusto</span></span>
                            </div>
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Nel momento <span className="font-bold">giusto</span></span>
                            </div>
                            <div className="flex items-center gap-4">
                                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[#F1F5F9] via-[#D4AF37] to-[#996515] flex items-center justify-center shadow-[0_0_15px_rgba(212,175,55,0.4)] flex-shrink-0 border border-white/30">
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-[#2A2312]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={4}><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" /></svg>
                                </div>
                                <span className="text-xl md:text-2xl text-white font-light">Per le persone <span className="font-bold">giuste</span></span>
                            </div>
                        </div>

                        <div className="text-center space-y-4 pt-4 px-4">
                            <p className="text-2xl md:text-3xl text-white font-light leading-relaxed mb-6 lowercase">
                                <span className="font-bold">talmente tante aziende</span> <br />
                                devono <span className="font-bold">ancora capire</span> <br />
                                questo <span className="font-bold">concetto...</span>
                            </p>
                        </div>
                    </MotionDiv>
                </div>

            </div>
        </section>
    );
};
