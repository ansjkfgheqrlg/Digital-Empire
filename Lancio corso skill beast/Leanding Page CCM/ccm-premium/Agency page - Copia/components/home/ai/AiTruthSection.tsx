import React from 'react';
import { motion } from 'framer-motion';

export const GoldText = ({ children }: { children: React.ReactNode }) => (
    <span className="text-transparent bg-clip-text bg-gradient-to-b from-[#FDE68A] via-[#D4AF37] to-[#B45309] font-bold">
        {children}
    </span>
);

export const SilverText = ({ children }: { children: React.ReactNode }) => (
    <span className="text-transparent bg-clip-text bg-gradient-to-b from-[#FFFFFF] via-[#E2E8F0] to-[#94A3B8] font-bold">
        {children}
    </span>
);

export const AiTruthSection: React.FC = () => {
    return (
        <section className="relative py-32 md:py-48 overflow-hidden bg-black -mt-20 pt-20">
            {/* Background Decorativo - Minimal Dark */}
            <div className="absolute top-0 left-0 w-full h-full pointer-events-none z-0">
                <div className="absolute inset-0 bg-black opacity-100"></div>
                {/* Removed radial gradient for a cleaner look */}
            </div>

            <div className="container mx-auto px-6 relative z-10">
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1 }}
                    className="flex flex-col items-center text-center gap-24"
                >
                    {/* --- HEADLINE --- */}
                    <div className="mb-0">
                        <motion.h2
                            initial={{ y: 20, opacity: 0 }}
                            whileInView={{ y: 0, opacity: 1 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.8 }}
                            className="font-sans leading-[1.1] lowercase text-center"
                        >
                            <span className="block text-5xl md:text-7xl lg:text-8xl mb-6 text-transparent bg-clip-text bg-gradient-to-b from-[#FDE68A] via-[#D4AF37] to-[#B45309] font-black">
                                la verità scomoda
                            </span>
                            <span className="font-light text-white block text-3xl md:text-5xl lg:text-6xl tracking-tight">
                                sull'implementazione AI.
                            </span>
                        </motion.h2>
                    </div>

                    {/* --- NARRATIVE FLOW --- */}
                    <div className="max-w-4xl space-y-32">

                        {/* SECTION 1 */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            className="space-y-8"
                        >
                            <p className="text-2xl md:text-4xl text-gray-300 font-serif leading-relaxed">
                                L'intelligenza artificiale non è un semplice "strumento". <br className="hidden md:block" />
                                È un <SilverText>cambio di paradigma</SilverText> che sta riscrivendo le regole del gioco aziendale.
                            </p>
                            <p className="text-lg md:text-2xl text-gray-500 font-light">
                                Ignorarla è un <GoldText>suicidio strategico</GoldText>.
                            </p>
                        </motion.div>

                        {/* SECTION 2 */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                        >
                            <p className="text-2xl md:text-4xl text-gray-300 font-serif leading-relaxed">
                                Mentre tu continui a pagare stipendi per <SilverText>mansioni ripetitive</SilverText> e data entry...<br />
                                I tuoi concorrenti stanno automatizzando interi comparti aziendali a frazioni del costo.
                            </p>
                        </motion.div>

                        {/* SECTION 3: THE NVIDIA QUOTE - Pure Minimal */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.98 }}
                            whileInView={{ opacity: 1, scale: 1 }}
                            viewport={{ once: true }}
                            className="relative py-24 px-8 group"
                        >
                            <div className="relative z-10 flex flex-col items-center">
                                <h3 className="font-sans text-4xl md:text-6xl font-black lowercase leading-tight text-white mb-14 max-w-2xl">
                                    "l'ai non ruberà il tuo lavoro.
                                </h3>
                                <p className="font-serif text-2xl md:text-4xl text-[#D4AF37] italic leading-relaxed max-w-4xl mx-auto font-medium drop-shadow-2xl uppercase">
                                    Un professionista o un'azienda che usa l'AI lo farà."
                                </p>
                                <div className="mt-16 flex flex-col items-center gap-4">
                                    <div className="w-12 h-[1px] bg-white/10"></div>
                                    <p className="text-gray-500 font-mono text-xs uppercase tracking-[0.3em]">
                                        — Jensen Huang, CEO di NVIDIA
                                    </p>
                                </div>
                            </div>
                        </motion.div>

                        {/* FOOTER: LOGIC CORE */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            className="space-y-16"
                        >
                            <p className="text-2xl md:text-3xl text-gray-400 font-light leading-relaxed max-w-2xl mx-auto">
                                Chi non implementa l'intelligenza artificiale nei propri processi <GoldText>rimarrà indietro</GoldText> senza possibilità di recupero.
                            </p>

                            <div className="pt-8">
                                <h3 className="text-5xl md:text-8xl font-sans font-black text-white lowercase mb-6">
                                    la scelta?
                                </h3>
                                <p className="text-2xl md:text-4xl text-[#D4AF37] font-serif italic lowercase tracking-tighter">
                                    adattarsi ed evolvere <br className="hidden md:block" />
                                    oppure estinguersi.
                                </p>
                            </div>
                        </motion.div>

                    </div>
                </motion.div>
            </div>
        </section>
    );
};
