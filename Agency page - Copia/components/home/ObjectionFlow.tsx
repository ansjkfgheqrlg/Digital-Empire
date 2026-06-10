
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Plus, Minus, ArrowRight, ShieldCheck, BarChart3, Clock, Users, Globe, Lock } from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';

const MotionDiv = motion.div as any;

// Dati espansi e professionalizzati
const objections = [
    {
        id: "01",
        label: "Unicità del Settore",
        trigger: "Il mio business è troppo specifico...",
        truth: "PSICOLOGIA UNIVERSALE",
        icon: Globe,
        description: "È l'obiezione più comune e la più fallace. Non vendiamo prodotti, vendiamo stati emotivi. Le leve biologiche che spingono un essere umano ad acquistare (status, paura, avidità, affetto) sono identiche per chi vende macchinari industriali e per chi vende gioielli. La strategia si adatta, la biologia umana resta immutata.",
        stat: "ADATTABILITÀ: 100%"
    },
    {
        id: "02",
        label: "Asset Esistenti",
        trigger: "Ho già un sito web online...",
        truth: "OBSOLESCENZA FUNZIONALE",
        icon: Lock,
        description: "Avere un sito 'vetrina' nel mercato odierno equivale a non averlo. Noi non costruiamo siti, costruiamo ecosistemi di conversione. Se il tuo sito attuale non genera lead qualificati ogni giorno in automatico, è un costo, non un asset. È tempo di trasformarlo da biglietto da visita a macchina da vendita.",
        stat: "INCREMENTO LEADS: +400%"
    },
    {
        id: "03",
        label: "Fattore Umano",
        trigger: "L'AI renderà il brand freddo...",
        truth: "UMANITÀ POTENZIATA",
        icon: Users,
        description: "L'automazione non sostituisce l'umano, lo eleva. Eliminiamo il 90% del lavoro robotico (data entry, qualifiche base, FAQ) per permettere al tuo team di concentrarsi sull'unica cosa che conta: la relazione ad alto valore e la chiusura del contratto. Meno burocrazia, più empatia.",
        stat: "EFFICIENZA TEAM: MAX"
    },
    {
        id: "04",
        label: "Sostenibilità",
        trigger: "Il passaparola mi basta...",
        truth: "SCALABILITÀ IMPOSSIBILE",
        icon: BarChart3,
        description: "Il passaparola è fantastico, ma ha un difetto fatale: non è controllabile. Non puoi 'alzare il volume' del passaparola quando hai bisogno di più fatturato. I nostri sistemi sono rubinetti: vuoi più clienti? Apriamo il flusso. Vuoi stabilizzare? Lo regoliamo. Questo è il controllo.",
        stat: "PREDICIBILITÀ: ALTA"
    },
    {
        id: "05",
        label: "Investimento",
        trigger: "Costa troppo per noi...",
        truth: "IL COSTO DELL'INAZIONE",
        icon: ShieldCheck,
        description: "La domanda non è quanto costa farlo, ma quanto ti costa NON farlo. Ogni giorno senza un sistema di acquisizione automatizzato stai letteralmente regalando clienti ai tuoi concorrenti. Il nostro servizio non è una spesa, è un moltiplicatore di capitale con ROI misurabile.",
        stat: "ROI MEDIO: 5-10X"
    },
    {
        id: "06",
        label: "Risorse Tempo",
        trigger: "Non ho tempo da dedicare...",
        truth: "PROTOCOLLO 'DONE-FOR-YOU'",
        icon: Clock,
        description: "Non stiamo vendendo un corso dove tu devi lavorare. Stiamo vendendo un'infrastruttura chiavi in mano. Noi costruiamo, noi scriviamo, noi lanciamo. Il tuo unico compito è gestire l'aumento di fatturato e approvare la strategia. Al resto pensa Empire Systems.",
        stat: "IMPEGNO TUO: MINIMO"
    }
];

export const ObjectionFlow: React.FC = () => {
    const [activeId, setActiveId] = useState(objections[0].id);
    const activeData = objections.find(a => a.id === activeId) || objections[0];

    return (
        <section className="py-32 bg-[#020202] relative border-t border-white/5 overflow-hidden">

            {/* Minimal Background Grid */}
            <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:100px_100px] pointer-events-none" />

            <div className="container mx-auto px-4 md:px-8 relative z-10 max-w-7xl">

                {/* --- HEADER CLEAN --- */}
                <div className="flex flex-col md:flex-row justify-between items-end mb-20 gap-8 border-b border-white/10 pb-10">
                    <div>
                        <span className="font-mono text-[10px] uppercase tracking-[0.4em] text-gold-500 mb-4 block">
                            Analisi Strategica
                        </span>
                        <h2 className="text-4xl md:text-6xl font-serif text-white font-medium leading-none tracking-tight">
                            DECIFRAZIONE <br /> <span className="text-gray-600">OSTACOLI</span>
                        </h2>
                    </div>
                    <div className="max-w-md text-right md:text-left">
                        <p className="text-gray-400 text-sm leading-relaxed font-light">
                            I dubbi sono freni invisibili alla crescita. <br />
                            Abbiamo trasformato ogni tua incertezza in un protocollo di soluzione.
                        </p>
                    </div>
                </div>

                {/* --- INTERFACE: MINIMAL SPLIT --- */}
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-0 lg:gap-12 min-h-[600px]">

                    {/* LEFT: LIST (Minimal Rows) */}
                    <div className="lg:col-span-5 flex flex-col justify-center">
                        <div className="space-y-1">
                            {objections.map((item) => {
                                const isActive = activeId === item.id;
                                return (
                                    <button
                                        key={item.id}
                                        onClick={() => setActiveId(item.id)}
                                        className={`w-full group relative flex items-center justify-between p-6 transition-all duration-500 border-l-2 ${isActive
                                                ? 'border-gold-500 bg-white/[0.03]'
                                                : 'border-transparent hover:border-white/20 hover:bg-white/[0.01]'
                                            }`}
                                    >
                                        <div className="flex flex-col items-start text-left gap-1">
                                            <span className={`text-[10px] font-mono uppercase tracking-widest transition-colors ${isActive ? 'text-gold-500' : 'text-gray-600'}`}>
                                                {item.id} // {item.label}
                                            </span>
                                            <span className={`font-serif text-lg md:text-xl transition-colors ${isActive ? 'text-white' : 'text-gray-500 group-hover:text-gray-300'}`}>
                                                "{item.trigger}"
                                            </span>
                                        </div>

                                        <div className={`transition-all duration-500 ${isActive ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-4'}`}>
                                            <ArrowRight size={16} className="text-gold-500" />
                                        </div>
                                    </button>
                                );
                            })}
                        </div>
                    </div>

                    {/* RIGHT: CONTENT (Elegant Card) */}
                    <div className="lg:col-span-7 relative mt-10 lg:mt-0">
                        <AnimatePresence mode="wait">
                            <MotionDiv
                                key={activeId}
                                initial={{ opacity: 0, x: 20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -20 }}
                                transition={{ duration: 0.5, ease: [0.32, 0.72, 0, 1] }}
                                className="h-full flex flex-col justify-center bg-[#080808] border border-white/10 p-8 md:p-16 relative overflow-hidden"
                            >
                                {/* Background Number */}
                                <div className="absolute top-0 right-0 text-[15rem] font-serif font-black text-white/[0.02] leading-none -mt-10 -mr-10 select-none pointer-events-none">
                                    {activeData.id}
                                </div>

                                {/* Content */}
                                <div className="relative z-10">
                                    <div className="flex items-center gap-3 mb-8">
                                        <div className="p-3 bg-white/5 rounded-full border border-white/10">
                                            <activeData.icon size={20} className="text-gold-500" />
                                        </div>
                                        <div className="h-[1px] w-12 bg-gold-500/50"></div>
                                        <span className="text-[10px] font-mono text-gold-500 uppercase tracking-widest">
                                            Realtà Operativa
                                        </span>
                                    </div>

                                    <h3 className="text-3xl md:text-5xl font-serif text-white mb-8 leading-tight">
                                        {activeData.truth}
                                    </h3>

                                    <p className="text-gray-400 text-lg font-light leading-relaxed mb-12 border-l-2 border-white/10 pl-6">
                                        {activeData.description}
                                    </p>

                                    <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-8 pt-8 border-t border-white/5">
                                        <div>
                                            <span className="block text-[10px] text-gray-600 font-mono uppercase tracking-widest mb-1">
                                                Performance Metrica
                                            </span>
                                            <span className="text-xl text-white font-serif italic">
                                                {activeData.stat}
                                            </span>
                                        </div>

                                        <GoldButton href="#contact" variant="silver" className="!py-3 !px-6 !text-[10px]">
                                            Approfondisci Strategia
                                        </GoldButton>
                                    </div>
                                </div>
                            </MotionDiv>
                        </AnimatePresence>
                    </div>

                </div>
            </div>
        </section>
    );
};
