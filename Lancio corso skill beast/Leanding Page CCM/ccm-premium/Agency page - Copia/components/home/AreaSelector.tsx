import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, Cpu, ChevronDown } from 'lucide-react';

interface AreaSelectorProps {
    activeArea: 'CRO' | 'AI' | null;
    onSelectArea: (area: 'CRO' | 'AI') => void;
}

export const AreaSelector: React.FC<AreaSelectorProps> = ({ activeArea, onSelectArea }) => {

    const goldSilverGradient = {
        backgroundImage: 'linear-gradient(90deg, #B48529 0%, #D4AF37 25%, #F3F4F6 50%, #94A3B8 75%, #64748B 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
    };

    return (
        <section className="relative w-full py-32 flex flex-col items-center bg-black overflow-hidden border-t-0">

            {/* Background Glows */}
            <div className="absolute top-1/2 left-1/4 w-[500px] h-[500px] bg-white/5 blur-[150px] rounded-full pointer-events-none transform -translate-y-1/2"></div>
            <div className="absolute top-1/2 right-1/4 w-[500px] h-[500px] bg-slate-400/5 blur-[150px] rounded-full pointer-events-none transform -translate-y-1/2"></div>

            <div className="relative z-20 max-w-7xl px-4 w-full text-center mx-auto flex flex-col items-center">

                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1.2 }}
                    className="mb-14 relative w-full flex flex-col items-center justify-center overflow-visible px-2"
                >
                    <h2 className="text-[4.5vw] min-[500px]:text-4xl md:text-6xl lg:text-7xl font-sans tracking-tight lowercase whitespace-nowrap leading-none flex items-center justify-center gap-2 md:gap-3" style={goldSilverGradient as any}>
                        <span className="font-bold">digital empire</span>
                        <span className="font-light">è diviso in</span>
                        <span className="font-bold">due aree</span>
                    </h2>
                </motion.div>

                {/* Blocks Row */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-10 w-full max-w-6xl">

                    {/* LEFT: CRO BLOCK */}
                    <motion.div
                        initial={{ opacity: 0, x: -30 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.8, delay: 0.2 }}
                        className={`group relative p-12 rounded-[2rem] transition-all duration-700 shadow-2xl flex flex-col items-center text-center gap-8 cursor-pointer border-[3px] border-transparent
                     ${activeArea === 'CRO'
                                ? 'scale-[1.03] shadow-[0_0_60px_rgba(212,175,55,0.25)]'
                                : 'hover:scale-[1.01]'}`}
                        style={{
                            background: activeArea === 'CRO'
                                ? 'linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%) padding-box, linear-gradient(135deg, #D4AF37 0%, #FFFFFF 50%, #B45309 100%) border-box'
                                : 'linear-gradient(135deg, #0f172a 0%, #000000 100%) padding-box, linear-gradient(135deg, #D4AF37 0%, #FFFFFF 50%, #94A3B8 100%) border-box'
                        }}
                        onClick={() => onSelectArea('CRO')}
                    >
                        {/* Glassmorphism / Noise */}
                        <div className={`absolute inset-0 mix-blend-overlay pointer-events-none rounded-[2rem] bg-[url('https://grainy-gradients.vercel.app/noise.svg')] ${activeArea === 'CRO' ? 'opacity-50' : 'opacity-20'}`}></div>



                        <div className={`relative z-10 p-5 rounded-2xl mb-4 transition-all duration-500 transform group-hover:scale-110 ${activeArea === 'CRO' ? 'bg-slate-900 text-white shadow-2xl' : 'bg-white/5 text-white border border-white/10'}`}>
                            <TrendingUp size={40} strokeWidth={1.2} />
                        </div>

                        <div className="relative z-10 space-y-6">
                            <div>
                                <h3 className={`font-mono text-5xl font-black uppercase tracking-tighter ${activeArea === 'CRO' ? 'text-slate-900' : 'text-white'}`}>
                                    CRO
                                </h3>
                                <p className={`text-xs tracking-[0.3em] font-bold uppercase mt-3 ${activeArea === 'CRO' ? 'text-slate-500' : 'text-slate-400'}`}>
                                    conversion rate optimization
                                </p>
                            </div>

                            <p className={`text-base md:text-lg leading-relaxed max-w-sm mx-auto font-medium ${activeArea === 'CRO' ? 'text-slate-700' : 'text-gray-300'}`}>
                                Se stai cercando di vendere attraverso ads su Meta e non sta andando come speravi... <br />
                                <span className={`font-black uppercase block mt-4 text-xl tracking-tight ${activeArea === 'CRO' ? 'text-red-600' : 'text-red-500'}`}>
                                    IL TUO PROBLEMA è il funnel.
                                </span>
                            </p>
                        </div>

                        <div className="relative z-10 mt-auto pt-10 w-full">
                            <button className={`w-full py-5 px-8 rounded-xl font-mono text-[10px] uppercase tracking-[0.3em] font-black transition-all duration-500 flex items-center justify-center gap-4
                        ${activeArea === 'CRO'
                                    ? 'bg-slate-900 text-white shadow-[0_20px_40px_rgba(0,0,0,0.4)] hover:shadow-[0_25px_50px_rgba(0,0,0,0.5)]'
                                    : 'bg-white/5 text-white hover:bg-white/10 border border-white/10'}`}>
                                {activeArea === 'CRO' ? 'Area Selezionata' : 'Mostra Area'}
                                {activeArea === 'CRO' && <ChevronDown size={18} />}
                            </button>
                        </div>
                    </motion.div>

                    {/* RIGHT: AI BLOCK */}
                    <motion.div
                        initial={{ opacity: 0, x: 30 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.8, delay: 0.4 }}
                        className={`group relative p-12 rounded-[2rem] transition-all duration-700 shadow-2xl flex flex-col items-center text-center gap-8 cursor-pointer border-[3px] border-transparent
                     ${activeArea === 'AI'
                                ? 'scale-[1.03] shadow-[0_0_60px_rgba(212,175,55,0.25)]'
                                : 'hover:scale-[1.01]'}`}
                        style={{
                            background: activeArea === 'AI'
                                ? 'linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%) padding-box, linear-gradient(135deg, #D4AF37 0%, #FFFFFF 50%, #B45309 100%) border-box'
                                : 'linear-gradient(135deg, #0f172a 0%, #000000 100%) padding-box, linear-gradient(135deg, #D4AF37 0%, #FFFFFF 50%, #94A3B8 100%) border-box'
                        }}
                        onClick={() => onSelectArea('AI')}
                    >

                        {/* Glassmorphism / Noise */}
                        <div className={`absolute inset-0 mix-blend-overlay pointer-events-none rounded-[2rem] bg-[url('https://grainy-gradients.vercel.app/noise.svg')] ${activeArea === 'AI' ? 'opacity-50' : 'opacity-20'}`}></div>



                        <div className={`relative z-10 p-5 rounded-2xl mb-4 transition-all duration-500 transform group-hover:scale-110 ${activeArea === 'AI' ? 'bg-slate-900 text-white shadow-2xl' : 'bg-white/5 text-white border border-white/10'}`}>
                            <Cpu size={40} strokeWidth={1.2} />
                        </div>

                        <div className="relative z-10 space-y-6">
                            <div>
                                <h3 className={`font-mono text-5xl font-black uppercase tracking-tighter leading-[0.9] ${activeArea === 'AI' ? 'text-slate-900' : 'text-white'}`}>
                                    Impl. AI
                                </h3>
                                <p className={`text-xs tracking-[0.3em] font-bold uppercase mt-3 ${activeArea === 'AI' ? 'text-slate-500' : 'text-slate-400'}`}>
                                    Implementazione Ai
                                </p>
                            </div>

                            <div className={`text-base md:text-lg leading-relaxed max-w-sm mx-auto font-medium space-y-4 ${activeArea === 'AI' ? 'text-slate-700' : 'text-gray-300'}`}>
                                <p className={`font-black text-xl tracking-tight ${activeArea === 'AI' ? 'text-slate-900' : 'text-white'}`}>
                                    Creazione di agenti ai su misura.
                                    <br />Automatizza sistemi aziendali.
                                </p>
                                <p className="text-sm font-semibold opacity-80">
                                    Analizziamo i tuoi processi, troviamo delle opportunità Ai e andiamo ad implementare soluzioni custom.
                                </p>
                            </div>
                        </div>

                        <div className="relative z-10 mt-auto pt-10 w-full">
                            <button className={`w-full py-5 px-8 rounded-xl font-mono text-[10px] uppercase tracking-[0.3em] font-black transition-all duration-500 flex items-center justify-center gap-4
                        ${activeArea === 'AI'
                                    ? 'bg-slate-900 text-white shadow-[0_20px_40px_rgba(0,0,0,0.4)] hover:shadow-[0_25px_50px_rgba(0,0,0,0.5)]'
                                    : 'bg-white/5 text-white hover:bg-white/10 border border-white/10'}`}>
                                {activeArea === 'AI' ? 'Area Selezionata' : 'Mostra Area'}
                                {activeArea === 'AI' && <ChevronDown size={18} />}
                            </button>
                        </div>
                    </motion.div>

                </div>
            </div>
        </section>
    );
};
