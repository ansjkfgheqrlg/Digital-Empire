import React from 'react';
import { motion } from 'framer-motion';
import { TrendingDown, ShoppingCart, BarChart2, AlertTriangle } from 'lucide-react';

export const CroHeroBottom: React.FC = () => {
    return (
        <div className="relative w-full flex flex-col items-center overflow-hidden">
            <div className="relative z-20 w-full px-2 text-center max-w-[100vw] mx-auto flex flex-col items-center">
                {/* --- 6. SYMPTOM DIAGNOSTICS BLOCK (REDESIGN) --- */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1.2, delay: 0.7 }}
                    className="relative z-20 mt-40 mb-48 max-w-7xl px-4 w-full text-center mx-auto flex flex-col items-center gap-16"
                >
                    {/* HEADLINE SECTION */}
                    <div className="flex flex-col items-center gap-4">
                        <p className="font-sans text-2xl md:text-3xl text-white font-light leading-relaxed lowercase max-w-5xl">
                            Se sei qui potrei già conoscere il tuo <span className="font-bold">problema</span>... <br />
                            Hai il tuo <span className="font-bold">prodotto/servizio</span> e cerchi di venderlo pagando <span className="font-bold whitespace-nowrap">ads su Meta</span> <br />
                            Ma non sta andando come speravi... Il tuo <span className="font-bold">problema</span> è il <span className="font-bold">funnel</span>.
                        </p>
                    </div>

                    {/* 4 DIAGNOSIS CARDS GRID - GLASSMORPHISM ARGENTO ROSSO */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full relative z-10">

                        {/* Card 1: Emorragia Pubblicitaria */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white">
                                    <TrendingDown size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black">Diagnosi #01</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-mono text-lg text-slate-900 mb-3 font-bold tracking-tight">L'Emorragia Pubblicitaria</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    Le tue Ads su <span className="text-slate-900 font-black">Meta</span> portano click, ma il telefono non squilla. Stai pagando per la curiosità, non per i clienti.
                                </p>
                                <p className="text-xs font-bold text-red-700/80 pt-4 border-t border-slate-900/10 w-full mt-4">
                                    Stai bruciando budget in <span className="font-black text-slate-900">clic</span> che non portano vendite.
                                </p>
                            </div>
                        </div>

                        {/* Card 2: Carrello Abbandonato */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white">
                                    <ShoppingCart size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black">Diagnosi #02</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-mono text-lg text-slate-900 mb-3 font-bold tracking-tight">Sindrome Carrello Vuoto</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    I clienti iniziano a compilare il form e poi svaniscono nel nulla. Li perdi proprio <span className="text-slate-900 font-black">sul più bello</span>.
                                </p>
                                <p className="text-xs font-bold text-red-700/80 pt-4 border-t border-slate-900/10 w-full mt-4">
                                    Il cliente non si fida abbastanza per <span className="font-black text-slate-900">pagare</span>.
                                </p>
                            </div>
                        </div>

                        {/* Card 3: Vanity Metrics */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white">
                                    <BarChart2 size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black">Diagnosi #03</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-mono text-lg text-slate-900 mb-3 font-bold tracking-tight">Vanity Metrics</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    Hai migliaia di visite e like, ma il <span className="text-slate-900 font-black">tasso di conversione</span> è imbarazzante (&lt;1%). I like non pagano le bollette.
                                </p>
                                <p className="text-xs font-bold text-red-700/80 pt-4 border-t border-slate-900/10 w-full mt-4">
                                    Ottimi numeri social, pessimo <span className="font-black text-slate-900">fatturato</span>.
                                </p>
                            </div>
                        </div>

                        {/* Card 4: Collo di Bottiglia */}
                        <div className="group relative p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex flex-col items-start text-left gap-6">
                            <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                            <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                            <div className="relative z-10 flex justify-between w-full items-start">
                                <div className="p-3 bg-slate-900 rounded-lg text-white">
                                    <AlertTriangle size={24} strokeWidth={1.5} />
                                </div>
                                <span className="font-mono text-xs text-red-600 uppercase tracking-widest font-black">Diagnosi #04</span>
                            </div>
                            <div className="relative z-10">
                                <h4 className="font-mono text-lg text-slate-900 mb-3 font-bold tracking-tight">Il Collo di Bottiglia</h4>
                                <p className="text-slate-700 font-medium leading-relaxed text-sm md:text-base">
                                    Il tuo servizio è eccellente, ma il tuo <span className="text-slate-900 font-black">sito</span> non riesce a spiegarlo. Il problema non è cosa vendi, ma COME lo vendi.
                                </p>
                                <p className="text-xs font-bold text-red-700/80 pt-4 border-t border-slate-900/10 w-full mt-4">
                                    Il sito non comunica il tuo <span className="font-black text-slate-900">valore</span> reale.
                                </p>
                            </div>
                        </div>

                    </div>

                    {/* WAVY SEPARATOR BOTTOM - GOLD/SILVER RIBBON (THICK & OPAQUE) */}
                    <div className="absolute bottom-[-160px] left-0 w-full overflow-visible z-10 pointer-events-none">
                        <div className="w-[100vw] relative left-1/2 -ml-[50vw]">
                            <svg viewBox="0 0 1440 60" className="w-full h-auto" preserveAspectRatio="none">
                                <defs>
                                    <linearGradient id="goldSilverRibbonThin" x1="0%" y1="0%" x2="100%" y2="0%">
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
                                    stroke="url(#goldSilverRibbonThin)"
                                    strokeWidth="8"
                                    strokeLinecap="round"
                                    d="M-10,30 C150,20 300,40 450,30 C600,20 750,40 900,30 C1050,20 1200,40 1350,30 C1500,20 1650,40 1800,30"
                                    className="opacity-100"
                                />
                            </svg>
                        </div>
                    </div>

                </motion.div>

                {/* --- 7. SOLUTION/FUNNEL EXPLANATION BLOCK (UPDATED: REMOVED TEXT) --- */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1.2, delay: 0.2 }}
                    className="relative z-20 mt-32 mb-20 w-full max-w-6xl px-6"
                >
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">

                        {/* LEFT: TEXT EXPLANATION */}
                        <div className="text-left space-y-8">
                            <div>
                                <h3 className="font-sans text-white leading-[0.9] mb-8">
                                    {/* FUNNEL: GOLD METAL GRADIENT */}
                                    <span className="block text-6xl md:text-7xl lg:text-8xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-b from-[#FDE68A] via-[#D4AF37] to-[#B45309] lowercase drop-shadow-[0_0_30px_rgba(212,175,55,0.3)]">
                                        funnel.
                                    </span>
                                </h3>
                            </div>

                            <div className="text-lg text-gray-400 font-light leading-relaxed space-y-6 lowercase">
                                <p>
                                    La parola "funnel" viene spesso abusata. Ecco la definizione tecnica definitiva:
                                </p>
                                <p className="border-l-2 border-white/20 pl-6 italic text-gray-300">
                                    Un funnel è un <strong className="text-white">setaccio digitale strutturato</strong>. È un percorso obbligato che filtra il traffico caotico (visitatori casuali) e lo raffina passo dopo passo, fino a isolare solo l'oro puro: i clienti paganti.
                                </p>
                            </div>

                            <div className="space-y-4 pt-4">
                                <div className="flex items-start gap-4">
                                    <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-white/10 shrink-0 text-white font-serif font-bold">1</div>
                                    <div>
                                        <h4 className="text-white font-bold text-sm uppercase tracking-wide lowercase">Attrarre (top of funnel)</h4>
                                        <p className="text-sm text-gray-500 mt-1 lowercase">catturiamo l'attenzione nel mercato freddo con ads chirurgiche.</p>
                                    </div>
                                </div>
                                <div className="flex items-start gap-4">
                                    <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-white/10 shrink-0 text-white font-serif font-bold">2</div>
                                    <div>
                                        <h4 className="text-white font-bold text-sm uppercase tracking-wide lowercase">Educare (middle of funnel)</h4>
                                        <p className="text-sm text-gray-500 mt-1 lowercase">costruiamo fiducia automatica smontando le obiezioni.</p>
                                    </div>
                                </div>
                                <div className="flex items-start gap-4">
                                    <div className="w-8 h-8 rounded-full bg-gold-900/40 flex items-center justify-center border border-gold-500/50 shrink-0 text-gold-500 font-serif font-bold">3</div>
                                    <div>
                                        <h4 className="text-gold-500 font-bold text-sm uppercase tracking-wide lowercase">Convertire (bottom of funnel)</h4>
                                        <p className="text-sm text-gray-500 mt-1 lowercase">presentiamo l'offerta irresistibile al momento esatto.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* RIGHT: VISUAL GRAPHIC (UPDATED: LOWERCASE) */}
                        <div className="relative h-[500px] flex items-center justify-center">
                            {/* Background Glow */}
                            <div className="absolute inset-0 bg-gold-500/5 blur-[100px] rounded-full pointer-events-none"></div>

                            {/* THE FUNNEL SVG */}
                            <svg viewBox="0 0 400 500" className="w-full h-full drop-shadow-2xl overflow-visible">
                                <defs>
                                    <linearGradient id="glassGradient" x1="0" y1="0" x2="1" y2="1">
                                        <stop offset="0%" stopColor="rgba(255,255,255,0.1)" />
                                        <stop offset="100%" stopColor="rgba(255,255,255,0.02)" />
                                    </linearGradient>
                                    <linearGradient id="goldLiquid" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="0%" stopColor="#FDE68A" />
                                        <stop offset="100%" stopColor="#B45309" />
                                    </linearGradient>
                                    <filter id="glow">
                                        <feGaussianBlur stdDeviation="4" result="coloredBlur" />
                                        <feMerge>
                                            <feMergeNode in="coloredBlur" />
                                            <feMergeNode in="SourceGraphic" />
                                        </feMerge>
                                    </filter>
                                </defs>

                                {/* STAGE 1: TRAFFIC (Top) */}
                                <motion.path
                                    d="M 20,20 L 380,20 L 320,150 L 80,150 Z"
                                    fill="url(#glassGradient)"
                                    stroke="rgba(255,255,255,0.2)"
                                    strokeWidth="1"
                                    initial={{ opacity: 0, y: -20 }}
                                    whileInView={{ opacity: 1, y: 0 }}
                                    transition={{ duration: 1 }}
                                />
                                <text x="200" y="90" textAnchor="middle" fill="white" fontSize="12" fontFamily="monospace" letterSpacing="2" opacity="0.6" className="lowercase">traffico (ads)</text>

                                {/* STAGE 2: NURTURING (Middle) */}
                                <motion.path
                                    d="M 90,160 L 310,160 L 260,300 L 140,300 Z"
                                    fill="url(#glassGradient)"
                                    stroke="rgba(255,255,255,0.3)"
                                    strokeWidth="1"
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    whileInView={{ opacity: 1, scale: 1 }}
                                    transition={{ duration: 1, delay: 0.3 }}
                                />
                                <text x="200" y="240" textAnchor="middle" fill="white" fontSize="12" fontFamily="monospace" letterSpacing="2" opacity="0.8" className="lowercase">educazione</text>

                                {/* STAGE 3: CONVERSION (Bottom - Gold) */}
                                <motion.path
                                    d="M 150,310 L 250,310 L 250,450 L 150,450 Z"
                                    fill="url(#goldLiquid)"
                                    stroke="#FDE68A"
                                    strokeWidth="2"
                                    filter="url(#glow)"
                                    initial={{ opacity: 0, pathLength: 0 }}
                                    whileInView={{ opacity: 1, pathLength: 1 }}
                                    transition={{ duration: 1.5, delay: 0.6 }}
                                />
                                <text x="200" y="380" textAnchor="middle" fill="#2A2312" fontSize="14" fontFamily="serif" fontWeight="bold" letterSpacing="1" className="lowercase">vendita</text>

                                {/* PARTICLES FLOWING */}
                                {[...Array(5)].map((_, i) => (
                                    <motion.circle
                                        key={i}
                                        r="3"
                                        fill="#FDE68A"
                                        initial={{ x: 200, y: 20, opacity: 0 }}
                                        animate={{
                                            y: [20, 400],
                                            opacity: [0, 1, 0],
                                            x: [200 + (Math.random() * 200 - 100), 200]
                                        }}
                                        transition={{
                                            duration: 2 + Math.random(),
                                            repeat: Infinity,
                                            delay: Math.random() * 2,
                                            ease: "easeInOut"
                                        }}
                                    />
                                ))}
                            </svg>
                        </div>

                    </div>
                </motion.div>
            </div>
        </div>
    );
};
