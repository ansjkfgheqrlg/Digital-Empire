
import React from 'react';
import { motion } from 'framer-motion';
import {
    XCircle, TrendingUp, ArrowDown, MousePointer2, AlertTriangle, Ban, Calculator, Users, ShoppingCart, FileText, CheckCircle2, BrainCircuit, Flame, AlertOctagon, Lightbulb, ShieldCheck, MousePointerClick, X, Check, Lock, ArrowRight, ChevronRight
} from 'lucide-react';

const MotionDiv = motion.div as any;

export const EducationalBridge = () => (
    <div className="relative py-40 mb-20 w-full overflow-hidden">

        {/* LIGHT BEAMS BACKGROUND */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full max-w-7xl pointer-events-none">
            <div className="absolute top-0 left-1/4 w-[1px] h-full bg-gradient-to-b from-transparent via-white/8 to-transparent"></div>
            <div className="absolute top-0 right-1/4 w-[1px] h-full bg-gradient-to-b from-transparent via-white/8 to-transparent"></div>
        </div>

        <div className="container mx-auto px-6 relative z-10">

            {/* HEADLINE SECTION */}
            <div className="text-center mb-32">
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8 }}
                >
                    <span className="font-mono text-[10px] text-gray-600 uppercase tracking-[0.4em] font-bold block mb-10">
                        Il Diagnostico
                    </span>
                    <h2 className="font-playfair text-5xl md:text-7xl lg:text-8xl text-white/90 leading-[1.05] tracking-tighter lowercase mb-8">
                        l'errore che <span className="font-bold">ti costa</span>
                        <br />
                        <span
                            className="font-black"
                            style={{
                                backgroundImage: 'linear-gradient(135deg, #fca5a5 0%, #ef4444 20%, #ffffff 52%, #ef4444 78%, #7f1d1d 100%)',
                                WebkitBackgroundClip: 'text',
                                backgroundClip: 'text',
                                WebkitTextFillColor: 'transparent',
                                filter: 'drop-shadow(0px 0px 40px rgba(220,38,38,0.25))'
                            }}
                        >il 70% del budget</span>.
                    </h2>
                </motion.div>

                <motion.p
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ delay: 0.3, duration: 1 }}
                    className="text-gray-400 font-light text-lg md:text-xl max-w-2xl mx-auto leading-relaxed"
                >
                    Mandare traffico freddo alla cassa è <span className="text-white border-b border-white/20 pb-0.5">matematicamente sbagliato</span>.
                    <br />
                    Ecco perché i numeri non tornano.
                </motion.p>
            </div>

            {/* COMPARISON GRID — DARK PREMIUM */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 relative">

                {/* LEFT: AMATEUR — Dark, red-tinted */}
                <MotionDiv
                    initial={{ opacity: 0, x: -24 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.7 }}
                    className="relative p-10 md:p-14 rounded-3xl overflow-hidden border border-red-900/20 bg-gradient-to-br from-[#130000] via-[#0d0000] to-[#0a0a0a] mb-6 lg:mb-0"
                >
                    {/* Top accent line */}
                    <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-red-800/50 to-transparent" />
                    {/* Ambient glow */}
                    <div className="absolute top-0 left-1/2 -translate-x-1/2 w-56 h-28 bg-red-900/10 blur-[50px] rounded-full pointer-events-none" />

                    <div className="flex flex-col items-center text-center gap-8 relative z-10">

                        <span className="font-mono text-[10px] tracking-[0.35em] text-red-500/70 uppercase font-black border border-red-900/35 px-4 py-1.5 rounded-full bg-red-950/15">
                            Modello Obsoleto
                        </span>

                        <h3 className="text-3xl font-playfair text-white/55 font-light">Approccio Amatoriale</h3>

                        {/* VISUALIZATION: BROKEN FLOW */}
                        <div className="w-full max-w-sm flex items-center justify-between relative py-10">
                            <div className="flex flex-col items-center gap-3">
                                <div className="w-11 h-11 rounded-xl bg-white/[0.04] border border-white/10 flex items-center justify-center">
                                    <MousePointer2 size={15} className="text-white/30" />
                                </div>
                                <span className="text-[10px] font-mono uppercase text-gray-600 font-bold">Ads</span>
                            </div>

                            <div className="flex-grow flex items-center mx-4">
                                <div className="h-[1px] flex-1 bg-gradient-to-r from-white/8 to-transparent" />
                                <div className="mx-2 w-7 h-7 rounded-full bg-red-950/50 border border-red-800/40 flex items-center justify-center flex-shrink-0">
                                    <X size={11} className="text-red-500" />
                                </div>
                                <div className="h-[1px] flex-1 bg-gradient-to-l from-white/8 to-transparent" />
                            </div>

                            <div className="flex flex-col items-center gap-3">
                                <div className="w-11 h-11 rounded-xl bg-red-950/20 border border-red-900/30 flex items-center justify-center">
                                    <ShoppingCart size={15} className="text-red-700/50" />
                                </div>
                                <span className="text-[10px] font-mono uppercase text-red-700/65 font-black">Bounce</span>
                            </div>
                        </div>

                        <p className="text-gray-500 font-light leading-relaxed text-sm max-w-sm">
                            Il visitatore atterra su una pagina priva di contesto emotivo. Non percependo il valore reale, il suo sguardo cade immediatamente sul prezzo.
                            <span className="text-red-400/75 font-medium mt-2 block">
                                Senza guida strategica, l'unica decisione logica è abbandonare la pagina per sempre.
                            </span>
                        </p>

                        <div className="px-6 py-2.5 border border-red-900/45 rounded-full text-red-500/65 font-mono text-sm font-bold bg-red-950/10 tracking-widest">
                            CR: &lt;0.5%
                        </div>

                    </div>
                </MotionDiv>

                {/* RIGHT: EMPIRE — Dark, gold-tinted */}
                <MotionDiv
                    initial={{ opacity: 0, x: 24 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.7, delay: 0.12 }}
                    className="relative p-10 md:p-14 rounded-3xl overflow-hidden border border-gold-500/18 bg-gradient-to-br from-[#0e0900] via-[#090800] to-[#0a0a0a]"
                    style={{ boxShadow: '0 0 80px rgba(212,175,55,0.06), inset 0 0 0 0.5px rgba(212,175,55,0.06)' }}
                >
                    {/* Top accent line */}
                    <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-gold-500/55 to-transparent" />
                    {/* Ambient glow */}
                    <div className="absolute top-0 left-1/2 -translate-x-1/2 w-72 h-36 bg-gold-500/5 blur-[70px] rounded-full pointer-events-none" />

                    <div className="flex flex-col items-center text-center gap-8 relative z-10">

                        <span
                            className="font-mono text-[10px] tracking-[0.35em] uppercase font-black border border-gold-500/20 px-4 py-1.5 rounded-full bg-gold-950/10"
                            style={{
                                backgroundImage: 'linear-gradient(135deg, #FDE68A, #D4AF37)',
                                WebkitBackgroundClip: 'text',
                                backgroundClip: 'text',
                                WebkitTextFillColor: 'transparent',
                            }}
                        >
                            Protocollo Empire
                        </span>

                        <h3 className="text-4xl font-playfair text-white font-light italic">Protocollo Ponte</h3>

                        {/* VISUALIZATION: THE BRIDGE */}
                        <div className="w-full max-w-md flex items-center justify-between relative py-10">
                            <div className="absolute top-1/2 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-gold-500/18 to-transparent" />

                            <div className="flex flex-col items-center gap-3 relative z-10">
                                <div className="w-11 h-11 rounded-xl bg-white/[0.04] border border-white/10 flex items-center justify-center">
                                    <MousePointer2 size={15} className="text-white/30" />
                                </div>
                                <span className="text-[10px] font-mono text-gray-600 uppercase font-bold">Ads</span>
                            </div>

                            <div className="flex flex-col items-center gap-3 relative z-10">
                                <div
                                    className="w-14 h-14 rounded-2xl border border-gold-500/30 flex items-center justify-center"
                                    style={{
                                        background: 'linear-gradient(135deg, #1c1300, #0e0900)',
                                        boxShadow: '0 0 35px rgba(212,175,55,0.18), inset 0 1px 0 rgba(253,230,138,0.08)'
                                    }}
                                >
                                    <FileText size={20} className="text-gold-500" />
                                </div>
                                <span
                                    className="text-[10px] font-mono uppercase font-black tracking-widest px-2 py-1 rounded border border-gold-500/20 bg-gold-950/10"
                                    style={{
                                        backgroundImage: 'linear-gradient(135deg, #FDE68A, #D4AF37)',
                                        WebkitBackgroundClip: 'text',
                                        backgroundClip: 'text',
                                        WebkitTextFillColor: 'transparent',
                                    }}
                                >Sales Page</span>
                            </div>

                            <div className="flex flex-col items-center gap-3 relative z-10">
                                <div className="w-11 h-11 rounded-xl bg-gold-950/15 border border-gold-500/20 flex items-center justify-center">
                                    <ShoppingCart size={15} className="text-gold-500/60" />
                                </div>
                                <span className="text-[10px] font-mono text-gold-600/55 uppercase font-bold">$$$</span>
                            </div>
                        </div>

                        <p className="text-gray-400 font-light leading-relaxed text-sm max-w-sm">
                            Il tuo 'Venditore Digitale' trasforma il traffico freddo in una relazione di fiducia. Attraverso il Protocollo Ponte, ogni dubbio viene anticipato ed educato.
                            <span
                                className="font-medium mt-2 block"
                                style={{
                                    backgroundImage: 'linear-gradient(135deg, #FDE68A, #D4AF37)',
                                    WebkitBackgroundClip: 'text',
                                    backgroundClip: 'text',
                                    WebkitTextFillColor: 'transparent',
                                }}
                            >
                                Non vendiamo merce. Ingegnerizziamo decisioni d'acquisto.
                            </span>
                        </p>

                        <div
                            className="px-8 py-3 rounded-full font-mono text-sm font-bold border border-gold-500/20 tracking-widest text-white"
                            style={{
                                background: 'linear-gradient(135deg, rgba(212,175,55,0.08), rgba(212,175,55,0.04))',
                                boxShadow: '0 0 25px rgba(212,175,55,0.08)'
                            }}
                        >
                            CR: 3% — 8%
                        </div>

                    </div>
                </MotionDiv>

            </div>

            <div className="mt-24 text-center">
                <p className="font-serif italic text-2xl text-white/25">
                    "Il business è un gioco di <span className="text-white not-italic font-sans font-bold uppercase tracking-widest text-sm align-middle px-2">scelte</span>, non di fortuna."
                </p>
            </div>
        </div>
    </div>
);

export const HopeIsNoStrategy = () => {
    const goldGradient = {
        backgroundImage: 'linear-gradient(135deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
    };

    const stats = [
        { value: '97%', label: 'dei siti web non converte', sub: 'fonte: HubSpot' },
        { value: '0.5s', label: 'per giudicare un sito', sub: 'fonte: Google UX Research' },
        { value: '3x', label: 'più conversioni con CRO', sub: 'fonte: Unbounce' },
    ];

    return (
        <div className="py-24 flex flex-col items-center text-center">
            <MotionDiv
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.7 }}
                className="max-w-5xl w-full"
            >
                {/* Eyebrow */}
                <span className="font-mono text-[10px] text-gray-500 uppercase tracking-[0.4em] font-bold block mb-8">
                    Il problema reale
                </span>

                {/* Main Headline */}
                <h2 className="font-sans text-5xl md:text-7xl lg:text-8xl tracking-tighter leading-[0.95] mb-10 lowercase">
                    <span className="text-white font-light">la speranza</span>{' '}
                    <span className="text-gray-600 font-light italic">non è una</span>
                    <br />
                    <span style={goldGradient as any} className="font-black">strategia aziendale.</span>
                </h2>

                {/* Sub-copy */}
                <p className="font-sans text-gray-400 text-xl md:text-2xl font-light leading-relaxed max-w-3xl mx-auto mb-20">
                    Incrociare le dita dopo aver lanciato il sito non porta fatturato.{' '}
                    <br className="hidden md:block" />
                    Il mercato non premia gli ottimisti.{' '}
                    <span style={{ background: 'rgba(212,175,55,0.18)', borderRadius: '3px', padding: '0 5px', WebkitTextFillColor: 'inherit', color: 'inherit' } as any}>
                        Premia gli ingegneri.
                    </span>
                </p>

                {/* Stats Row */}
                <MotionDiv
                    initial={{ opacity: 0, y: 16 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.2 }}
                    className="grid grid-cols-1 md:grid-cols-3 gap-0 border-t border-b border-white/8 divide-y md:divide-y-0 md:divide-x divide-white/8 w-full max-w-4xl mx-auto"
                >
                    {stats.map((stat, i) => (
                        <div key={i} className="py-10 px-8 text-center">
                            <div
                                className="text-5xl md:text-6xl font-black font-sans tracking-tighter mb-3"
                                style={goldGradient as any}
                            >
                                {stat.value}
                            </div>
                            <div className="text-sm text-gray-300 font-light lowercase leading-snug mb-2">
                                {stat.label}
                            </div>
                            <div className="text-[10px] font-mono uppercase tracking-widest text-gray-600">
                                {stat.sub}
                            </div>
                        </div>
                    ))}
                </MotionDiv>
            </MotionDiv>
        </div>
    );
};

export const CroCalculator = ({ goldGradient, silverGradient }: { goldGradient: any, silverGradient: any }) => (
    <div className="relative mb-32 pb-20">
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-gold-500/5 blur-[120px] rounded-full pointer-events-none -z-10"></div>
        <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-white/5 blur-[120px] rounded-full pointer-events-none -z-10"></div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center relative z-10">
            <div>
                <h3 className="text-white mb-12 leading-[0.8] tracking-tighter text-center lg:text-left">
                    <span style={goldGradient as any} className="font-black block mb-4 text-[80px] md:text-[120px] lg:text-[160px]">C.R.O.</span>
                    <span className="font-sans text-3xl md:text-5xl font-black block uppercase tracking-[0.2em] text-transparent bg-clip-text bg-gradient-to-r from-[#94A3B8] via-[#FDE68A] to-[#D4AF37]">
                        conversion rate optimization
                    </span>
                </h3>
                <p className="text-2xl md:text-3xl text-gray-400 font-sans font-light mb-12">non serve più traffico. <span className="text-white font-bold tracking-tight">Serve più efficienza.</span></p>
                <div className="space-y-12 text-xl md:text-2xl text-gray-400 font-sans font-light leading-relaxed mb-16">
                    <p className="border-l border-white/10 pl-8 italic text-gray-300 leading-relaxed py-2">
                        "se <GoldText>raddoppi</GoldText> il tasso di conversione (dall'1% al 2%), hai <GoldText>letteralmente dimezzato</GoldText> il costo di acquisizione <SilverText>senza spendere</SilverText> un centesimo in più in advertising."
                    </p>
                    <p>il <SilverText>funnel ingegnerizzato</SilverText> è l'unica applicazione pratica del <SilverText>cro</SilverText>. Non è "arte". È un <SilverText>sistema a imbuto</SilverText> progettato per <GoldText>eliminare ogni distrazione</GoldText> e forzare una <GoldText>decisione d'acquisto</GoldText> immediata.</p>
                </div>

                {/* Minimal Comparison Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-xl">
                    <div className="p-8 rounded-2xl bg-[#0a0a0a] border border-white/5 shadow-2xl relative group overflow-hidden">
                        <div className="absolute inset-0 bg-gradient-to-br from-red-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <div className="relative z-10 flex flex-col gap-4">
                            <span className="text-[10px] font-mono text-gray-600 uppercase tracking-[0.3em] font-bold">Modello Standard</span>
                            <div className="text-2xl font-serif text-gray-400 group-hover:text-red-500/80 transition-colors duration-500 tracking-wider">Dispersivo</div>
                            <p className="text-xs text-gray-600 lowercase font-medium">Troppi link, zero focus aziendale.</p>
                        </div>
                    </div>

                    <div className="p-8 rounded-2xl bg-[#0a0a0a] border border-gold-500/20 shadow-2xl relative group overflow-hidden">
                        <div className="absolute inset-0 bg-gradient-to-br from-gold-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <div className="absolute top-0 right-0 p-3 opacity-20"><BrainCircuit size={14} className="text-gold-500" /></div>
                        <div className="relative z-10 flex flex-col gap-4">
                            <span className="text-[10px] font-mono text-gold-600/60 uppercase tracking-[0.3em] font-bold">Protocollo Empire</span>
                            <div className="text-2xl font-serif text-white group-hover:text-gold-400 transition-colors duration-500 tracking-wider italic">Chirurgico</div>
                            <p className="text-xs text-gray-500 lowercase font-medium">un'unica via d'uscita: <span className="text-gold-500/80 italic">l'acquisto</span>.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="relative group">
                <div className="relative p-[2px] rounded-[32px] overflow-hidden shadow-[0_0_40px_rgba(212,175,55,0.15)]" style={{ background: 'linear-gradient(135deg, #E2E8F0 0%, #94A3B8 20%, #FDE68A 45%, #D4AF37 55%, #B45309 70%, #E2E8F0 100%)' }}>
                    <div className="bg-[#080808] p-8 md:p-12 rounded-[30px] relative backdrop-blur-xl h-full">
                        <div className="space-y-2 font-mono text-sm relative z-10">
                            <div className="flex items-center justify-between p-5 bg-[#0f0f0f] rounded-xl border border-white/5 mb-4 shadow-inner">
                                <span className="text-gray-500 lowercase">traffico (visitatori)</span>
                                <span className="text-white font-bold tracking-widest text-lg">10.000</span>
                            </div>
                            <div className="flex justify-center text-gray-700 py-2"><XCircle size={16} strokeWidth={1.5} /></div>
                            <div className="relative overflow-hidden group mb-4">
                                <div className="relative flex items-center justify-between p-5 bg-gold-900/10 rounded-xl border border-gold-500/40 shadow-[0_0_30px_rgba(212,175,55,0.05)]">
                                    <div className="flex items-center gap-3">
                                        <MousePointer2 size={18} className="text-gold-500" />
                                        <span className="text-gold-100 font-bold lowercase">tasso conversione (cro)</span>
                                    </div>
                                    <div className="flex items-center gap-3">
                                        <span className="text-gray-600 line-through text-xs font-light">0.8%</span>
                                        <ArrowDown size={14} className="text-gold-500 -rotate-90" />
                                        <span className="text-white font-black text-2xl">2.4%</span>
                                    </div>
                                </div>
                            </div>
                            <div className="flex justify-center text-gray-700 py-2">=</div>
                            <div className="flex items-center justify-between p-6 bg-gradient-to-r from-[#051c14] to-[#022c22] rounded-2xl border border-emerald-500/30 shadow-[0_10px_40px_rgba(16,185,129,0.1)]">
                                <span className="text-emerald-400 font-bold text-xs font-mono lowercase tracking-widest">nuovi clienti</span>
                                <div className="flex items-center gap-4">
                                    <TrendingUp size={24} className="text-emerald-500" />
                                    <span className="text-5xl text-white font-black tracking-tighter">240</span>
                                    <span className="text-[10px] text-emerald-400 bg-emerald-900/50 px-2 py-1 rounded border border-emerald-500/20 font-bold lowercase">(3x profitto)</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
);

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

const GoldSilverText = ({ children, className = "" }: { children: React.ReactNode, className?: string }) => (
    <span className={`text-transparent bg-clip-text bg-gradient-to-r from-[#94A3B8] via-[#FDE68A] to-[#D4AF37] ${className}`}>
        {children}
    </span>
);

export const CroEditorialSection = () => {
    return (
        <section className="relative py-32 md:py-48 overflow-hidden">
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
                                sul traffico a pagamento.
                            </span>
                        </motion.h2>
                    </div>

                    {/* --- NARRATIVE FLOW --- */}
                    <div className="max-w-4xl space-y-32">

                        {/* SECTION 1: THE OBSESSION */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            className="space-y-8"
                        >
                            <p className="text-2xl md:text-4xl text-gray-300 font-serif leading-relaxed">
                                La maggior parte degli imprenditori è ossessionata dal portare più persone sul sito. <br className="hidden md:block" />
                                Pensano che il volume <SilverText>sia la soluzione</SilverText>.
                            </p>
                            <p className="text-lg md:text-2xl text-gray-500 font-light">
                                Comprano traffico come se fosse <GoldText>benzina</GoldText>.
                            </p>
                        </motion.div>

                        {/* SECTION 2: THE PROBLEM (NO PROFIT) */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                        >
                            <p className="text-2xl md:text-4xl text-gray-300 font-serif leading-relaxed">
                                Ma il traffico, da solo, non genera <span className="font-bold text-white italic">profitto</span>. <br />
                                Genera solo <SilverText>rumore</SilverText> e costi che si accumulano ogni giorno.
                            </p>
                        </motion.div>

                        {/* SECTION 3: THE LEAKY BUCKET (ULTRA FOCUS) */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            className="space-y-12"
                        >
                            <p
                                className="text-4xl md:text-6xl lg:text-7xl font-serif lowercase leading-[1.15] tracking-tighter text-gray-300"
                                style={{
                                    textShadow: '0 0 15px rgba(255,255,255,0.05)',
                                    filter: 'drop-shadow(0 0 1px rgba(255,255,255,0.1))'
                                }}
                            >
                                mandare mille persone <br />
                                su un sito{' '}
                                <span style={{
                                    background: 'rgba(59, 44, 11, 0.85)',
                                    borderRadius: '6px',
                                    padding: '0 10px',
                                    fontWeight: 700,
                                    color: '#FDE68A',
                                    boxShadow: '0 0 25px rgba(253, 230, 138, 0.1)',
                                    display: 'inline-block',
                                    marginTop: '-4px',
                                    marginBottom: '-4px'
                                }}>non ottimizzato</span> <br />
                                è come versare acqua <br />
                                in un{' '}
                                <span style={{
                                    background: 'rgba(59, 44, 11, 0.85)',
                                    borderRadius: '6px',
                                    padding: '0 10px',
                                    fontWeight: 700,
                                    color: '#FDE68A',
                                    boxShadow: '0 0 25px rgba(253, 230, 138, 0.1)',
                                    display: 'inline-block',
                                    marginTop: '-4px',
                                    marginBottom: '-4px'
                                }}>secchio bucato.</span>
                            </p>
                            <p className="text-lg md:text-xl text-gray-500 font-light">
                                È un'azione costosa. Ed è tecnicamente stupida.
                            </p>
                            <div className="max-w-2xl mx-auto">
                                <p className="text-xl md:text-2xl text-gray-400 font-light font-sans">
                                    Mentre cerchi di riempire il secchio, il tuo <GoldText>margine</GoldText> scappa dai fori che non hai mai chiuso.
                                </p>
                            </div>
                        </motion.div>

                        {/* SECTION 4: THE CRO TRUTH (INTEGRATED) */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.98 }}
                            whileInView={{ opacity: 1, scale: 1 }}
                            viewport={{ once: true }}
                            className="py-16"
                        >
                            <h3 className="font-sans text-4xl md:text-7xl font-bold lowercase leading-tight text-white mb-8">
                                "il c.r.o. non è un costo.
                            </h3>
                            <p className="font-serif text-xl md:text-3xl text-[#D4AF37] italic leading-relaxed max-w-3xl mx-auto font-medium">
                                È l'unica attività di marketing che ti ripaga retroattivamente per ogni euro che hai già speso."
                            </p>
                        </motion.div>

                        {/* FOOTER: LOGIC CORE */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            className="space-y-16"
                        >
                            <p className="text-2xl md:text-3xl text-gray-400 font-light leading-relaxed max-w-2xl mx-auto">
                                Applichiamo psicologia comportamentale e <GoldText>matematica</GoldText> per forzare una decisione logica.
                            </p>

                            <div className="pt-8">
                                <h3 className="text-5xl md:text-8xl font-sans font-black text-white lowercase mb-6">
                                    il risultato?
                                </h3>
                                <p className="text-2xl md:text-4xl text-[#D4AF37] font-serif italic lowercase tracking-tighter">
                                    un sistema deterministico <br className="hidden md:block" />
                                    progettato per il fatturato.
                                </p>
                            </div>
                        </motion.div>
                    </div>
                </motion.div>
            </div>
        </section>
    );
};

export const ApsocProtocol = () => (
    <div className="relative mt-0 mb-20">
        <div className="max-w-5xl mx-auto px-6 mb-16 text-center relative z-10">
            <div className="inline-flex items-center gap-2 px-3 py-1 border border-gold-500/30 rounded-full bg-gold-950/10 mb-6 backdrop-blur-sm shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                <BrainCircuit size={12} className="text-gold-500" />
                <span className="text-[10px] font-mono text-gold-500 uppercase tracking-[0.3em] font-black">Psychology Engine</span>
            </div>
            <h3 className="font-serif text-4xl md:text-6xl text-white lowercase leading-none">protocollo <span className="text-transparent bg-clip-text bg-gradient-to-b from-gold-100 via-gold-400 to-gold-700 drop-shadow-sm">a.p.s.o.c.</span></h3>
            <p className="text-gray-500 text-sm max-w-xl mx-auto font-light mt-4 leading-relaxed">Non scriviamo "testi carini". Ingegnerizziamo le parole seguendo la sequenza esatta con cui il cervello umano prende decisioni d'acquisto.</p>
        </div>
        <div className="max-w-7xl mx-auto px-6 space-y-4 relative z-10">
            {[
                { letter: "A", title: "Attenzione (the hook)", desc: "Ferma lo scroll. Rompi il pattern. L'obiettivo della prima frase è solo far leggere la seconda. Se non catturi l'attenzione in 0.3 secondi, hai perso.", icon: Flame, color: "text-red-600", bullets: ["stop scrolling", "rottura del pattern", "impatto visivo"] },
                { letter: "P", title: "Problema (the pain)", desc: "Agita il dolore. Mostra al cliente che capisci il suo problema meglio di lui. Crea empatia istantanea dimostrando che conosci le sue frustrazioni notturne.", icon: AlertOctagon, color: "text-orange-600", bullets: ["empatia profonda", "agitazione dolore", "validazione"] },
                { letter: "S", title: "Soluzione (the product)", desc: "Presenta il tuo prodotto non come un 'oggetto', ma come l'unica via d'uscita logica al dolore. Non vendere caratteristiche, vendi la nuova identità del cliente.", icon: Lightbulb, color: "text-amber-600", bullets: ["nuovo veicolo", "logica unica", "beneficio primario"] },
                { letter: "O", title: "Obiezioni (the shield)", desc: "'Costa troppo?', 'funzionerà per me?'. Anticipa ogni dubbio e distruggilo prima che nasca. Usa garanzie, case study e logica inattaccabile per disarmare lo scetticismo.", icon: ShieldCheck, color: "text-blue-600", bullets: ["garanzia di ferro", "riprova sociale", "zero rischi"] },
                { letter: "C", title: "Call to Action (the command)", desc: "Dì loro esattamente cosa fare. Non 'se vuoi, clicca qui'. Usa imperativi: 'Acquista ora', 'Inizia la scalata'. La confusione uccide la conversione. Sii chiaro.", icon: MousePointerClick, color: "text-yellow-700", bullets: ["comando diretto", "urgenza motivata", "chiarezza assoluta"] }
            ].map((step, idx) => (
                <div key={idx} className="group relative p-6 md:p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#f1f5f9] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)]">
                    <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                    <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                    <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
                        <div className="lg:col-span-8 flex items-start gap-6 md:gap-10">
                            <div className="flex-shrink-0 w-16 md:w-20 text-center"><span className="font-serif font-black text-6xl md:text-7xl leading-none transition-all duration-500 text-slate-900/10 group-hover:text-slate-900/20 group-hover:scale-110">{step.letter}</span></div>
                            <div className="flex-grow pt-2">
                                <div className="flex items-center gap-3 mb-3"><h4 className="font-bold text-lg md:text-xl lowercase text-slate-900">{step.title}</h4><step.icon size={16} className={`${step.color} opacity-100`} /></div>
                                <p className="text-sm md:text-base text-slate-700 font-medium lowercase leading-relaxed max-w-2xl">{step.desc}</p>
                            </div>
                        </div>
                        <div className="hidden lg:flex lg:col-span-4 border-l border-slate-900/10 pl-8 flex-col justify-center h-full">
                            <h5 className="font-mono text-[10px] uppercase tracking-widest text-slate-500 mb-4 font-black">key tactics</h5>
                            <ul className="space-y-3">
                                {step.bullets.map((bullet, bIdx) => (
                                    <li key={bIdx} className="flex items-center gap-3 text-xs md:text-sm text-slate-800 font-mono lowercase font-bold"><div className="w-1.5 h-1.5 rounded-full bg-slate-900"></div>{bullet}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    </div>
);
