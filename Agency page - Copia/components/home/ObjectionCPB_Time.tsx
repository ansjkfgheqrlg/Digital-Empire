
import React from 'react';
import { motion } from 'framer-motion';
import { Clock, Zap, CheckCircle2, ArrowRight } from 'lucide-react';

const MotionDiv = motion.div as any;

export const ObjectionCPB_Time: React.FC = () => {
    return (
        <section id="objection-time" className="py-32 relative overflow-hidden bg-[#DCD8CF]">

            {/* --- BACKGROUND: ARGENTO DORATO (MATCHING HOWWEWORK) --- */}
            <div className="absolute inset-0 w-full h-full z-0 pointer-events-none">
                {/* Layer 1: Sharp Static Noise */}
                <div
                    className="absolute inset-0 opacity-[0.6] mix-blend-overlay"
                    style={{
                        backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                        filter: 'contrast(150%) brightness(100%)'
                    }}
                />
                {/* Layer 2: Coarse Digital Grain */}
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

            <div className="container mx-auto px-6 max-w-6xl relative z-10">

                {/* --- HEADER --- */}
                <div className="mb-20">
                    <MotionDiv
                        initial={{ opacity: 0, x: -20 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                        className="flex items-center gap-4 mb-6"
                    >
                        <div className="h-[1px] w-12 bg-slate-900/20"></div>
                        <span className="text-[10px] font-mono text-slate-500 uppercase tracking-[0.3em] font-bold">
                            Gestione Obiezioni // Protocollo CPB
                        </span>
                    </MotionDiv>

                    <h2 className="font-serif text-4xl md:text-6xl text-slate-900 font-black leading-tight lowercase">
                        "non ho <span className="italic text-slate-500">tempo</span> da dedicare..."
                    </h2>
                </div>

                {/* --- CPB GRID --- */}
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

                    {/* CLAIM */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.1 }}
                        className="group relative p-8 rounded-3xl bg-gradient-to-br from-[#FFFFFF] via-[#E2E8F0] to-[#94A3B8] border border-slate-300 shadow-xl overflow-hidden"
                    >
                        <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                        <div className="relative z-10">
                            <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                <Clock size={24} />
                            </div>
                            <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">01 // Claim</span>
                            <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                liberiamo il tuo tempo, non lo consumiamo.
                            </h3>
                            <p className="text-slate-700 text-sm leading-relaxed font-medium mt-10">
                                Il nostro protocollo è progettato per eliminare il lavoro operativo dalle tue spalle. Non siamo un corso da seguire, siamo un'infrastruttura che lavora per te.
                            </p>
                        </div>
                        <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">C</div>
                    </MotionDiv>

                    {/* PROOF */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.2 }}
                        className="group relative p-8 rounded-3xl bg-gradient-to-br from-[#FFF7ED] via-[#FDE68A] to-[#D4AF37] border border-yellow-600/30 shadow-xl overflow-hidden"
                    >
                        <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                        <div className="relative z-10">
                            <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                <Zap size={24} />
                            </div>
                            <span className="text-[10px] font-mono text-yellow-900/60 uppercase tracking-widest font-bold mb-2 block">02 // Proof</span>
                            <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                protocollo 100% "done-for-you".
                            </h3>
                            <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                Gestiamo noi ogni fase: dall'analisi dati al copywriting persuasivo, fino all'ingegneria tecnica. Il tuo impegno è ridotto esclusivamente al feedback strategico.
                            </p>
                        </div>
                        <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">P</div>
                    </MotionDiv>

                    {/* BENEFIT */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.3 }}
                        className="group relative p-8 rounded-3xl bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B] border border-slate-400 shadow-xl overflow-hidden"
                    >
                        <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                        <div className="relative z-10">
                            <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                <CheckCircle2 size={24} />
                            </div>
                            <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">03 // Benefit</span>
                            <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                focalizzati sulla visione, non sul bottone.
                            </h3>
                            <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                Smetti di essere il collo di bottiglia del tuo business. Otterrai un asset automatico che fattura 24/7 mentre tu ti riprendi il controllo della tua vita.
                            </p>
                        </div>
                        <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">B</div>
                    </MotionDiv>

                </div>

                {/* --- CONNECTIVE ARROW --- */}
                <div className="mt-20 flex justify-center">
                    <MotionDiv
                        initial={{ opacity: 0, scale: 0.8 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="p-4 rounded-full border border-slate-400/30 bg-white/20 backdrop-blur-md shadow-sm"
                    >
                        <ArrowRight size={24} className="text-slate-600 rotate-90" />
                    </MotionDiv>
                </div>

            </div>
        </section>
    );
};
