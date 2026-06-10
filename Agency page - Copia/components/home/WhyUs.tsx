
import React from 'react';
import { motion } from 'framer-motion';
import { Target, TrendingUp, Users } from 'lucide-react';

const MotionDiv = motion.div as any;

export const WhyUs: React.FC = () => {
    const goldSilverGradient = {
        backgroundImage: 'linear-gradient(to right, #94A3B8 0%, #E2E8F0 25%, #E3C878 50%, #FFFFFF 60%, #E3C878 75%, #E2E8F0 90%, #94A3B8 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        filter: 'drop-shadow(0px 2px 10px rgba(227, 200, 120, 0.2))',
    };
    return (
        <section className="py-32 relative overflow-hidden bg-[#031c16]">
            {/* --- RICH GREEN GRAIN BACKGROUND (Matched with Trust/Divider) --- */}
            <div className="absolute inset-0 w-full h-full pointer-events-none z-0">
                <div className="absolute inset-0 bg-[#031c16]"></div>

                {/* Layer 1: Heavy Film Grain */}
                <div
                    className="absolute inset-0 opacity-[0.4]"
                    style={{
                        backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                        filter: 'contrast(350%) brightness(100%)',
                        mixBlendMode: 'overlay'
                    }}
                />

                {/* Layer 2: Digital Noise */}
                <div
                    className="absolute inset-0 opacity-[0.3] mix-blend-screen"
                    style={{
                        backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.7' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                        backgroundSize: '100px 100px',
                        filter: 'contrast(160%) brightness(50%)'
                    }}
                />

                {/* Subtle Grid for continuity */}
                <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:60px_60px] opacity-10" />
            </div>

            <div className="container mx-auto px-6 relative z-10 max-w-6xl">
                <MotionDiv
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    className="text-center mb-24"
                >
                    <span className="font-mono text-[10px] text-gray-500 uppercase tracking-[0.4em] font-bold block mb-4">
                        Differenziazione Radicale
                    </span>
                    <h2 className="font-serif text-4xl md:text-7xl text-white font-light tracking-tight leading-none uppercase">
                        perché <span className="font-black" style={goldSilverGradient}>digital empire?</span>
                    </h2>
                </MotionDiv>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-12 border-t border-white/10 pt-12">
                    {/* Pillar 1 */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.1 }}
                        className="group"
                    >
                        <div className="mb-6 opacity-50 group-hover:opacity-100 transition-opacity duration-500">
                            <Target size={32} strokeWidth={1} className="text-white" />
                        </div>
                        <h3 className="text-xl md:text-2xl font-serif text-white mb-4 uppercase tracking-tighter">
                            Siamo <span className="font-black underline decoration-white/10 underline-offset-8" style={goldSilverGradient}>Ingegneri</span>, <br /> non Artisti.
                        </h3>
                        <p className="text-gray-500 text-sm leading-relaxed font-light font-sans max-w-xs">
                            L'eccellenza non è un atto, ma un'abitudine organizzativa. Ogni nostro progetto segue un'architettura rigorosa e processi millimetrici che non lasciano nulla al caso.
                        </p>
                    </MotionDiv>

                    {/* Pillar 2 */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.2 }}
                        className="group"
                    >
                        <div className="mb-6 opacity-50 group-hover:opacity-100 transition-opacity duration-500">
                            <TrendingUp size={32} strokeWidth={1} className="text-white" />
                        </div>
                        <h3 className="text-xl md:text-2xl font-serif text-white mb-4 uppercase tracking-tighter">
                            Vendiamo <span className="font-black underline decoration-white/10 underline-offset-8" style={goldSilverGradient}>Profitto</span>, <br /> non Like.
                        </h3>
                        <p className="text-gray-500 text-sm leading-relaxed font-light font-sans max-w-xs">
                            Sfruttiamo l'intelligenza artificiale in modo estremamente architettato per massimizzare ogni singolo risultato. Non giochiamo con i prompt, costruiamo infrastrutture AI che dominano il mercato.
                        </p>
                    </MotionDiv>

                    {/* Pillar 3 */}
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.3 }}
                        className="group"
                    >
                        <div className="mb-6 opacity-50 group-hover:opacity-100 transition-opacity duration-500">
                            <Users size={32} strokeWidth={1} className="text-white" />
                        </div>
                        <h3 className="text-xl md:text-2xl font-serif text-white mb-4 uppercase tracking-tighter">
                            Creiamo <span className="font-black underline decoration-white/10 underline-offset-8" style={goldSilverGradient}>Imperi</span>, <br /> non Siti.
                        </h3>
                        <p className="text-gray-500 text-sm leading-relaxed font-light font-sans max-w-xs">
                            Un sito web è statico. Un impero digitale è dinamico, scalabile e domina il mercato. Non cerchiamo clienti a cui inviare fatture, ma partner con cui scalare vette.
                        </p>
                    </MotionDiv>
                </div>
            </div>
        </section>
    );
};
