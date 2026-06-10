import React from 'react';
import { motion } from 'framer-motion';
import { Cpu, Terminal, Sparkles } from 'lucide-react';

export const AiImplementationBase: React.FC = () => {
    return (
        <section className="relative w-full min-h-[50vh] flex flex-col items-center justify-center bg-black overflow-hidden">

            {/* Grid Background */}
            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 mix-blend-overlay pointer-events-none"></div>
            <div className="absolute inset-0" style={{
                backgroundImage: `linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px)`,
                backgroundSize: '40px 40px',
                backgroundPosition: 'center center'
            }}></div>

            <div className="relative z-20 max-w-4xl px-4 w-full text-center mx-auto flex flex-col items-center gap-8 py-20 pb-40">

                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    whileInView={{ opacity: 1, scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8 }}
                    className="p-4 bg-slate-900 shadow-[0_0_40px_rgba(255,255,255,0.1)] rounded-2xl border border-white/20 mb-4"
                >
                    <Cpu size={40} className="text-white" strokeWidth={1.5} />
                </motion.div>

                <motion.h2
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="text-4xl md:text-6xl font-sans font-light text-white tracking-widest lowercase"
                >
                    Area <span className="font-bold text-transparent bg-clip-text bg-gradient-to-r from-slate-200 via-white to-slate-400">In Costruzione</span>
                </motion.h2>

                <motion.p
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.4 }}
                    className="text-lg md:text-xl text-gray-400 font-medium max-w-2xl lowercase leading-relaxed"
                >
                    I nostri ingegneri stanno strutturando l'area dedicata all'implementazione di infrastrutture Ai. Qui presenteremo casi studio e agenti custom per l'automazione aziendale.
                </motion.p>

                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.6 }}
                    className="flex flex-col md:flex-row gap-6 mt-8 w-full max-w-lg"
                >
                    <div className="flex-1 bg-white/5 border border-white/10 rounded-xl p-6 flex flex-col items-center gap-3 backdrop-blur-sm">
                        <Terminal className="text-gray-400" size={24} />
                        <span className="font-mono text-xs text-white uppercase tracking-widest">Sviluppo Modelli</span>
                    </div>
                    <div className="flex-1 bg-white/5 border border-white/10 rounded-xl p-6 flex flex-col items-center gap-3 backdrop-blur-sm">
                        <Sparkles className="text-gray-400" size={24} />
                        <span className="font-mono text-xs text-white uppercase tracking-widest">Agenti Custom</span>
                    </div>
                </motion.div>

            </div>

        </section>
    );
};
