import React from 'react';
import { motion } from 'framer-motion';
import { Target, Database, ShieldCheck, ArrowRight, Clock, PiggyBank, Briefcase, Users, HeartHandshake, Sparkles } from 'lucide-react';

const MotionDiv = motion.div as any;

export const AiObjections: React.FC = () => {
    return (
        <div className="bg-[#DCD8CF]">
            {/* --- OBJECTION 1: COST & TIME --- */}
            <section className="py-24 md:py-32 relative overflow-hidden">
                <div className="absolute inset-0 z-0 pointer-events-none">
                    <div
                        className="absolute inset-0 opacity-[0.6] mix-blend-overlay"
                        style={{
                            backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                            filter: 'contrast(150%) brightness(100%)'
                        }}
                    />
                    <div
                        className="absolute inset-0 opacity-[0.4] mix-blend-soft-light"
                        style={{
                            backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                            backgroundSize: '120px 120px',
                            filter: 'contrast(120%)'
                        }}
                    />
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.05)_100%)] opacity-100" />
                </div>

                <div className="container mx-auto px-6 max-w-6xl relative z-10">
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
                            "l'ai richiede <span className="italic text-slate-500">troppo tempo e denaro</span>..."
                        </h2>
                    </div>

                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        {/* CLAIM */}
                        <MotionDiv
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ delay: 0.1 }}
                            className="group relative p-8 rounded-3xl border-[3px] border-transparent shadow-xl overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 50%, #94A3B8 100%) padding-box, linear-gradient(135deg, #94A3B8 0%, #FFFFFF 50%, #64748B 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="relative z-10">
                                <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                    <Clock size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">01 // Claim</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    costruire costa meno di non averla.
                                </h3>
                                <p className="text-slate-700 text-sm leading-relaxed font-medium mt-10">
                                    Un dipendente costa stipendio, tasse, ferie e tempo perso in inefficienze. L'AI costa una frazione, richiede poche settimane di setup e lavora 24/7.
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
                            className="group relative p-8 rounded-3xl border-[3px] border-transparent shadow-xl overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #FFF7ED 0%, #FDE68A 50%, #D4AF37 100%) padding-box, linear-gradient(135deg, #D4AF37 0%, #FDE68A 50%, #B45309 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 bg-white/10 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="relative z-10">
                                <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                    <Database size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-yellow-900/60 uppercase tracking-widest font-bold mb-2 block">02 // Proof</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    ritorno d'investimento matematico.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Tracciamo esattamente le ore umane risparmiate dai nostri Agenti. In genere, il costo dell'implementazione viene recuperato entro 60 giorni netti.
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
                            className="group relative p-8 rounded-3xl border-[3px] border-transparent shadow-xl overflow-hidden"
                            style={{
                                background: 'linear-gradient(135deg, #F8FAFC 0%, #CBD5E1 50%, #64748B 100%) padding-box, linear-gradient(135deg, #64748B 0%, #CBD5E1 50%, #334155 100%) border-box'
                            }}
                        >
                            <div className="absolute inset-0 bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                            <div className="relative z-10">
                                <div className="w-12 h-12 rounded-xl bg-slate-900 flex items-center justify-center text-white mb-6 shadow-lg">
                                    <PiggyBank size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">03 // Benefit</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    drastico taglio dei costi di gestione.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Riduci il costo del lavoro amministrativo del 70% liberando budget vitale da investire in marketing o in profitto puro.
                                </p>
                            </div>
                            <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">B</div>
                        </MotionDiv>
                    </div>

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

            {/* --- OBJECTION 2: HUMAN JOB REPLACEMENT --- */}
            <section className="py-24 md:py-32 relative overflow-hidden">
                <div className="absolute inset-0 z-0 pointer-events-none">
                    <div
                        className="absolute inset-0 opacity-[0.6] mix-blend-overlay"
                        style={{
                            backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                            filter: 'contrast(150%) brightness(100%)'
                        }}
                    />
                    <div
                        className="absolute inset-0 opacity-[0.4] mix-blend-soft-light"
                        style={{
                            backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                            backgroundSize: '120px 120px',
                            filter: 'contrast(120%)'
                        }}
                    />
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.05)_100%)] opacity-100" />
                </div>

                <div className="container mx-auto px-6 max-w-6xl relative z-10">
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
                            "l'ai distrugge posti di lavoro e <span className="italic text-slate-500">ci rende disumani</span>..."
                        </h2>
                    </div>

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
                                    <Users size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">01 // Claim</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    l'ai ruba il lavoro robotico, non umano.
                                </h3>
                                <p className="text-slate-700 text-sm leading-relaxed font-medium mt-10">
                                    I tuoi dipendenti passano ore a fare copia-incolla, rispondere a mail identiche o sistemare fogli Excel. Questo è lavoro da robot. L'AI fa esattamente e solo questo.
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
                                    <HeartHandshake size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-yellow-900/60 uppercase tracking-widest font-bold mb-2 block">02 // Proof</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    i team aumentano la produttività, non si dimezzano.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Le aziende con cui collaboriamo riposizionano il personale su compiti ad alto valore: strategia, negoziazione, supporto emotivo ai clienti.
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
                                    <Sparkles size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">03 // Benefit</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    un'azienda radicalmente più umana.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Togliendo il lavoro meccanico, restituisci tempo ed energia al tuo team. Il risultato è un'assistenza migliore, dipendenti felici e un ecosistema aziendale sano.
                                </p>
                            </div>
                            <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">B</div>
                        </MotionDiv>
                    </div>

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

            {/* --- OBJECTION 3: TRADITIONAL BUSINESS --- */}
            <section className="py-24 md:py-32 relative overflow-hidden">
                <div className="absolute inset-0 z-0 pointer-events-none">
                    <div
                        className="absolute inset-0 opacity-[0.6] mix-blend-overlay"
                        style={{
                            backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                            filter: 'contrast(150%) brightness(100%)'
                        }}
                    />
                    <div
                        className="absolute inset-0 opacity-[0.4] mix-blend-soft-light"
                        style={{
                            backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                            backgroundSize: '120px 120px',
                            filter: 'contrast(120%)'
                        }}
                    />
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(0,0,0,0.05)_100%)] opacity-100" />
                </div>

                <div className="container mx-auto px-6 max-w-6xl relative z-10">
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
                            "il mio settore è <span className="italic text-slate-500">troppo tradizionale</span>..."
                        </h2>
                    </div>

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
                                    <Target size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">01 // Claim</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    i flussi di dati esistono ovunque.
                                </h3>
                                <p className="text-slate-700 text-sm leading-relaxed font-medium mt-10">
                                    Se emetti fatture, rispondi ai clienti o organizzi il lavoro, stai producendo dati. E dove ci sono dati testuali ripetitivi, l'AI eccelle.
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
                                    <Briefcase size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-yellow-900/60 uppercase tracking-widest font-bold mb-2 block">02 // Proof</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    risultati anche nell'industria pesante.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Abbiamo implementato chatbot di supporto B2B nell'edilizia e sistemi di gestione appuntamenti in studi notarili storici. Funziona ovunque.
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
                                    <ShieldCheck size={24} />
                                </div>
                                <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest font-bold mb-2 block">03 // Benefit</span>
                                <h3 className="text-2xl font-serif text-slate-900 font-bold mb-4 lowercase">
                                    diventerai l'eccezione locale.
                                </h3>
                                <p className="text-slate-800 text-sm leading-relaxed font-medium mt-10">
                                    Mentre i tuoi competitor storici restano analogici, diventi il player più veloce, reattivo e profittevole della tua categoria tradizionale.
                                </p>
                            </div>
                            <div className="absolute bottom-4 right-4 text-slate-900/5 font-black text-6xl font-serif">B</div>
                        </MotionDiv>
                    </div>

                </div>
            </section>
        </div>
    );
};
