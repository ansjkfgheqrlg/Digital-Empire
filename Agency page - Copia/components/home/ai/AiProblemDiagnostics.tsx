import React from 'react';
import { motion } from 'framer-motion';
import { Bot, LineChart, Clock, Database } from 'lucide-react';

export const AiProblemDiagnostics: React.FC = () => {
    return (
        <div className="relative w-full flex flex-col items-center overflow-hidden">
            <div className="relative z-20 w-full px-2 text-center max-w-[100vw] mx-auto flex flex-col items-center">

                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1.2, delay: 0.2 }}
                    className="relative z-20 mt-40 mb-32 max-w-7xl px-4 w-full text-center mx-auto flex flex-col items-center gap-16"
                >
                    {/* HEADLINE SECTION */}
                    <div className="flex flex-col items-center gap-4">
                        <p className="font-sans text-2xl md:text-3xl text-white font-light leading-relaxed lowercase max-w-5xl">
                            Se sei qui potrei già conoscere il tuo <span className="font-bold">problema</span>... <br />
                            La tua azienda cresce, ma <span className="font-bold">i processi si rompono</span> e il personale è sommerso da <span className="font-bold whitespace-nowrap">micro-task</span> <br />
                            Il tuo vero <span className="font-bold">problema</span> è l'assenza di <span className="font-bold text-transparent bg-clip-text bg-gradient-to-r from-slate-200 to-slate-400">automazione intelligente</span>.
                        </p>
                    </div>

                    {/* 4 DIAGNOSIS CARDS GRID - GLASSMORPHISM ARGENTO ROSSO */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full relative z-10">

                        {/* Card 1 */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/50 bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(203,213,225,0.4)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/90 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-10"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white shadow-[0_0_15px_rgba(15,23,42,0.5)]">
                                    <Clock size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black bg-white/50 px-2 py-1 rounded">Diagnosi #01</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-sans text-xl text-slate-900 mb-3 font-black tracking-tight uppercase">Collo di Bottiglia Operativo</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    Il tuo team passa l'80% del tempo su operazioni <span className="text-slate-900 font-black">ripetitive</span> (data entry, email, reportistica) incollato allo schermo.
                                </p>
                                <div className="w-full h-[1px] bg-slate-900/10 my-4"></div>
                                <p className="text-xs font-bold text-red-700 uppercase tracking-widest">
                                    Stai pagando per talenti, ma li usi come <span className="font-black text-slate-900">macchine</span>.
                                </p>
                            </div>
                        </div>

                        {/* Card 2 */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/50 bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(203,213,225,0.4)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/90 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-10"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white shadow-[0_0_15px_rgba(15,23,42,0.5)]">
                                    <Database size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black bg-white/50 px-2 py-1 rounded">Diagnosi #02</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-sans text-xl text-slate-900 mb-3 font-black tracking-tight uppercase">Caos Informativo</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    I dati aziendali sono sparsi tra CRM, fogli Excel e email. Nessuno ha una visione d'insieme aggiornata in <span className="text-slate-900 font-black">tempo reale</span>.
                                </p>
                                <div className="w-full h-[1px] bg-slate-900/10 my-4"></div>
                                <p className="text-xs font-bold text-red-700 uppercase tracking-widest">
                                    Le decisioni vengono prese a <span className="font-black text-slate-900">sensazione</span>, non sui dati.
                                </p>
                            </div>
                        </div>

                        {/* Card 3 */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/50 bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(203,213,225,0.4)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/90 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-10"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white shadow-[0_0_15px_rgba(15,23,42,0.5)]">
                                    <Bot size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black bg-white/50 px-2 py-1 rounded">Diagnosi #03</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-sans text-xl text-slate-900 mb-3 font-black tracking-tight uppercase">Servizio Clienti Lento</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    I clienti aspettano ore (o giorni) per risposte semplici. Nel frattempo i competitor <span className="text-slate-900 font-black">bruciano sul tempo</span> la tua assistenza.
                                </p>
                                <div className="w-full h-[1px] bg-slate-900/10 my-4"></div>
                                <p className="text-xs font-bold text-red-700 uppercase tracking-widest">
                                    Una cattiva assistenza uccide le <span className="font-black text-slate-900">vendite future</span>.
                                </p>
                            </div>
                        </div>

                        {/* Card 4 */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/50 bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(203,213,225,0.4)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/90 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-10"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white shadow-[0_0_15px_rgba(15,23,42,0.5)]">
                                    <LineChart size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black bg-white/50 px-2 py-1 rounded">Diagnosi #04</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-sans text-xl text-slate-900 mb-3 font-black tracking-tight uppercase">Scalabilità Bloccata</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    Ogni volta che l'azienda cresce del 10%, i costi operativi salgono del 20%. Non hai un sistema che slegli <span className="text-slate-900 font-black">costi dai ricavi</span>.
                                </p>
                                <div className="w-full h-[1px] bg-slate-900/10 my-4"></div>
                                <p className="text-xs font-bold text-red-700 uppercase tracking-widest">
                                    Più fatturi, meno <span className="font-black text-slate-900">margine netto</span> produci.
                                </p>
                            </div>
                        </div>

                    </div>

                    {/* WAVY SEPARATOR BOTTOM - GOLD/SILVER RIBBON (THICK & OPAQUE) */}
                    <div className="absolute bottom-[-160px] left-0 w-full overflow-visible z-10 pointer-events-none">
                        <div className="w-[100vw] relative left-1/2 -ml-[50vw]">
                            <svg viewBox="0 0 1440 60" className="w-full h-auto" preserveAspectRatio="none">
                                <defs>
                                    <linearGradient id="goldSilverRibbonThinAi" x1="0%" y1="0%" x2="100%" y2="0%">
                                        <stop offset="0%" style={{ stopColor: '#94A3B8', stopOpacity: 0.8 }} />
                                        <stop offset="20%" style={{ stopColor: '#FDE68A', stopOpacity: 1 }} />
                                        <stop offset="40%" style={{ stopColor: '#D4AF37', stopOpacity: 1 }} />
                                        <stop offset="60%" style={{ stopColor: '#FFFFFF', stopOpacity: 1 }} />
                                        <stop offset="80%" style={{ stopColor: '#D4AF37', stopOpacity: 1 }} />
                                        <stop offset="100%" style={{ stopColor: '#94A3B8', stopOpacity: 0.8 }} />
                                    </linearGradient>
                                </defs>
                                <path
                                    fill="none"
                                    stroke="url(#goldSilverRibbonThinAi)"
                                    strokeWidth="8"
                                    strokeLinecap="round"
                                    d="M-10,30 C150,20 300,40 450,30 C600,20 750,40 900,30 C1050,20 1200,40 1350,30 C1500,20 1650,40 1800,30"
                                    className="opacity-100"
                                />
                            </svg>
                        </div>
                    </div>

                </motion.div>
            </div>
        </div>
    );
};
