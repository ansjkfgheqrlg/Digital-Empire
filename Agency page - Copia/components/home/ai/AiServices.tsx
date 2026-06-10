import React from 'react';
import { motion } from 'framer-motion';

const MotionDiv = motion.div as any;

export const AiServices: React.FC = () => {

    const pureSilverGradient = {
        background: 'linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 100%)',
        WebkitBackgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        textShadow: '0 0 30px rgba(255,255,255,0.1)'
    };

    const champagneGradient = {
        background: 'linear-gradient(135deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
        WebkitBackgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
    };

    return (
        <section id="services" className="py-32 pb-24 relative border-t border-white/5 scroll-mt-20 bg-[#000000] overflow-hidden">

            {/* --- UNIFIED GRAINY BACKGROUND --- */}
            <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#000000]">
                <div
                    className="absolute inset-0 opacity-[0.35]"
                    style={{
                        backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                        filter: 'contrast(170%) brightness(150%) invert(100%)'
                    }}
                />
                <div
                    className="absolute inset-0 opacity-[0.25] mix-blend-screen"
                    style={{
                        backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                        backgroundSize: '150px 150px',
                        filter: 'contrast(150%)'
                    }}
                />
                <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#000000_100%)] opacity-40" />
            </div>

            <div className="container mx-auto px-6 max-w-6xl relative z-10">

                {/* --- HEADER --- */}
                <div className="text-center mb-24 relative">
                    <motion.h2 className="font-serif text-4xl md:text-6xl lg:text-7xl font-light tracking-tight lowercase leading-[0.9]">
                        <span style={pureSilverGradient as any}>creazione</span>
                        <span className="mx-2 md:mx-4 text-white/10 font-thin">|</span>
                        <span style={champagneGradient as any} className="font-black">agenti ai.</span>
                    </motion.h2>
                    <p className="max-w-2xl mx-auto text-gray-400 text-lg font-light leading-relaxed mt-8">
                        Non vendiamo un "chatbot". Sviluppiamo un impiegato digitale perfetto, addestrato sui dati della tua azienda, che non dorme e non commette errori.
                    </p>
                </div>

                {/* --- HOW IT WORKS (THE ONBOARDING PHASES) --- */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    className="mt-10 mb-40 max-w-5xl mx-auto text-center"
                >
                    <h3 className="font-serif text-3xl md:text-5xl text-white mb-20 lowercase">Come <span className="italic text-[#D4AF37]">iniziamo?</span></h3>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative px-4">
                        {/* Connecting Line */}
                        <div className="hidden md:block absolute top-[2.5rem] left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/20 to-transparent z-0"></div>

                        {/* STEP 1 */}
                        <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl border-[3px] border-transparent shadow-xl transition-all duration-500 hover:scale-[1.02] overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #ffffff 0%, #fef2f2 50%, #cbd5e1 100%) padding-box, linear-gradient(135deg, #94A3B8 0%, #FFFFFF 50%, #475569 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                                <span className="font-serif text-2xl text-white">01</span>
                            </div>
                            <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Briefing Call <span className="text-red-600 text-xs ml-1">(Gratis)</span></h4>
                            <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                                Andiamo a trovare e isolare il sistema aziendale esatto che possiamo automatizzare. Misuriamo quanto tempo e denaro stai sprecando ora.
                            </p>
                        </div>

                        {/* STEP 2 */}
                        <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl border-[3px] border-transparent shadow-xl transition-all duration-500 hover:scale-[1.02] overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #ffffff 0%, #fef2f2 50%, #cbd5e1 100%) padding-box, linear-gradient(135deg, #94A3B8 0%, #FFFFFF 50%, #475569 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                                <span className="font-serif text-2xl text-white">02</span>
                            </div>
                            <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Progetto & Preventivo</h4>
                            <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                                Se il ROI matematico ha senso, ti presentiamo l'architettura esatta dell'Agente AI, i tempi di sviluppo e l'investimento necessario.
                            </p>
                        </div>

                        {/* STEP 3 */}
                        <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl border-[3px] border-transparent shadow-xl transition-all duration-500 hover:scale-[1.02] overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #ffffff 0%, #fef2f2 50%, #cbd5e1 100%) padding-box, linear-gradient(135deg, #94A3B8 0%, #FFFFFF 50%, #475569 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                                <span className="font-serif text-2xl text-white">03</span>
                            </div>
                            <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Strategy Call</h4>
                            <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                                Kickoff ufficiale. Diamo il via all'addestramento dell'Agente e all'integrazione con i tuoi software esistenti (WhatsApp, CRM, Email, ecc).
                            </p>
                        </div>
                    </div>
                </motion.div>

                {/* --- CLASSIFIED CITATION --- */}
                <div className="max-w-3xl mx-auto mt-12 px-6">
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="relative p-[1px] rounded-xl overflow-hidden bg-gradient-to-r from-gray-400 via-[#D4AF37] to-gray-400 shadow-[0_0_20px_rgba(212,175,55,0.15)]"
                    >
                        <div className="bg-[#0a0a0a] rounded-xl p-8 md:p-10 relative overflow-hidden flex flex-col items-center text-center">

                            {/* Background Noise for texture consistency */}
                            <div
                                className="absolute inset-0 opacity-[0.3]"
                                style={{
                                    backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                                    filter: 'contrast(150%) brightness(130%)'
                                }}
                            />

                            <div className="relative z-10">
                                <p className="font-mono text-xs text-gold-500 mb-4 tracking-[0.2em] uppercase font-bold">
                      // status: classified
                                </p>
                                <p className="text-gray-300 text-lg md:text-xl font-light leading-relaxed lowercase font-serif italic">
                                    "l'integrazione di un sistema intelligente <br className="hidden md:block" />
                                    rende la tua azienda <span className="text-white font-bold not-italic">agile</span>, <span className="text-white font-bold not-italic">scalabile</span> e spietatamente superiore."
                                </p>
                            </div>
                        </div>
                    </MotionDiv>
                </div>

            </div>
        </section>
    );
};
