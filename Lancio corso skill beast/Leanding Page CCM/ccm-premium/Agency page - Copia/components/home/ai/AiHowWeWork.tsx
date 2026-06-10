import React from 'react';
import { motion } from 'framer-motion';
import { Search, BrainCircuit, Rocket, ArrowDown } from 'lucide-react';

const MotionDiv = motion.div as any;

const steps = [
    {
        id: "01",
        title: "ANALISI DEI PROCESSI",
        subtitle: "Process Mapping",
        description: "Mappiamo l'intera infrastruttura della tua azienda. Cerchiamo colli di bottiglia, task ripetitivi e sprechi di capitale umano che rallentano la crescita.",
        icon: Search,
        gradient: "bg-gradient-to-br from-[#FFFFFF] via-[#E2E8F0] to-[#94A3B8]",
        border: "border-[#94A3B8]",
        shadow: "shadow-[0_20px_40px_rgba(0,0,0,0.1)] hover:shadow-[0_30px_60px_rgba(0,0,0,0.2)]",
        iconColor: "text-slate-900",
        textColor: "text-slate-900"
    },
    {
        id: "02",
        title: "OPPORTUNITÀ AI",
        subtitle: "Intelligence Discovery",
        description: "Individuiamo le aree dove l'integrazione di Agenti AI può abbattere i costi operativi e moltiplicare l'output senza dover assumere nuovo personale.",
        icon: BrainCircuit,
        gradient: "bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B]",
        border: "border-[#64748B]",
        shadow: "shadow-[0_20px_40px_rgba(100,116,139,0.15)] hover:shadow-[0_30px_60px_rgba(100,116,139,0.25)]",
        iconColor: "text-slate-800",
        textColor: "text-slate-900"
    },
    {
        id: "03",
        title: "IMPLEMENTAZIONE CUSTOM",
        subtitle: "System Deployment",
        description: "Sviluppiamo e integriamo l'Agente AI su misura per la tua realtà. Un ecosistema autonomo che lavora 24/7, senza ferie e senza errori.",
        icon: Rocket,
        gradient: "bg-gradient-to-br from-[#FFFBEB] via-[#FCD34D] to-[#B45309]",
        border: "border-[#B45309]",
        shadow: "shadow-[0_20px_40px_rgba(180,83,9,0.2)] hover:shadow-[0_30px_60px_rgba(180,83,9,0.3)]",
        iconColor: "text-yellow-950",
        textColor: "text-yellow-950",
        isFinal: true
    }
];

export const AiHowWeWork: React.FC = () => {

    const darkMetalTitle = {
        backgroundImage: 'linear-gradient(180deg, #5B5B5B 0%, #333333 40%, #000000 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        filter: 'drop-shadow(0px 2px 0px rgba(255,255,255,0.5))',
    };

    return (
        <section id="process" className="py-32 relative overflow-hidden bg-[#DCD8CF]">

            {/* BACKGROUND */}
            <div className="absolute inset-0 w-full h-full z-0 pointer-events-none">
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

            <div className="container mx-auto px-4 relative z-20 max-w-5xl">

                {/* HEADER */}
                <div className="text-center mb-24">
                    <MotionDiv
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                    >
                        <div className="inline-block mb-6 px-4 py-1.5 rounded-full border border-slate-400/30 bg-white/20 backdrop-blur-md shadow-sm">
                            <span className="text-[10px] font-mono text-slate-600 uppercase tracking-[0.3em] font-bold">
                                Protocollo AI
                            </span>
                        </div>

                        <h2 className="font-serif text-5xl md:text-7xl font-black tracking-tight leading-none text-slate-900 mb-6 drop-shadow-sm lowercase">
                            <span style={darkMetalTitle as any}>architettura</span><br />
                            del nostro processo
                        </h2>

                        <p className="max-w-xl mx-auto text-slate-600 text-sm md:text-base font-medium leading-relaxed">
                            Non ci limitiamo a fornirti un software. Analizziamo, progettiamo e distribuiamo un sistema intelligente che si adatta alle tue regole di business.
                        </p>
                    </MotionDiv>
                </div>

                {/* BLOCKS */}
                <div className="relative flex flex-col items-center gap-8 md:gap-12">

                    <div className="absolute top-4 bottom-4 left-1/2 -translate-x-1/2 w-[1px] bg-gradient-to-b from-transparent via-slate-400 to-transparent z-0 hidden md:block opacity-40"></div>

                    {steps.map((step, index) => (
                        <div key={step.id} className="relative z-10 w-full group">
                            <MotionDiv
                                initial={{ opacity: 0, y: 40, scale: 0.95 }}
                                whileInView={{ opacity: 1, y: 0, scale: 1 }}
                                viewport={{ once: true, margin: "-50px" }}
                                transition={{ duration: 0.6, delay: index * 0.1 }}
                                className="flex flex-col md:flex-row items-center justify-center"
                            >
                                <div className={`
                      relative w-full md:w-[800px] p-8 md:p-10 rounded-2xl md:rounded-3xl
                      flex flex-col md:flex-row items-start md:items-center gap-6 md:gap-10
                      ${step.gradient} border ${step.border} ${step.shadow}
                      transform transition-transform duration-500 hover:scale-[1.02]
                   `}>
                                    <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20 opacity-80"></div>
                                    <div className="absolute inset-0 bg-gradient-to-br from-white/60 to-transparent opacity-40 pointer-events-none rounded-2xl md:rounded-3xl"></div>

                                    <div className="hidden md:block absolute right-6 top-2 text-[80px] font-black text-black/5 font-serif leading-none select-none pointer-events-none">
                                        {step.id}
                                    </div>

                                    <div className={`
                         flex-shrink-0 w-16 h-16 rounded-xl bg-white/80 backdrop-blur-md border border-white/60 shadow-inner
                         flex items-center justify-center ${step.iconColor}
                      `}>
                                        <step.icon size={32} strokeWidth={1.5} />
                                    </div>

                                    <div className="flex-grow relative z-10">
                                        <div className="flex items-center gap-3 mb-2">
                                            <span className={`text-[10px] font-mono uppercase tracking-[0.2em] font-bold opacity-60 ${step.textColor}`}>
                                                {step.subtitle}
                                            </span>
                                            <div className={`h-[1px] w-8 ${step.iconColor} opacity-20`}></div>
                                        </div>

                                        <h3 className={`text-2xl md:text-3xl font-serif font-black mb-3 leading-tight ${step.textColor}`}>
                                            {step.title}
                                        </h3>

                                        <p className={`text-sm md:text-base font-medium leading-relaxed opacity-80 max-w-xl ${step.textColor}`}>
                                            {step.description}
                                        </p>
                                    </div>

                                    <div className="md:hidden absolute top-6 right-6 font-mono font-black text-2xl opacity-10 text-black">
                                        {step.id}
                                    </div>
                                </div>
                            </MotionDiv>

                            {index !== steps.length - 1 && (
                                <div className="h-8 md:h-12 flex items-center justify-center relative z-0">
                                    <MotionDiv
                                        initial={{ height: 0 }}
                                        whileInView={{ height: "100%" }}
                                        className="w-[1px] bg-slate-400/50"
                                    />
                                    <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#DCD8CF] border border-slate-400/50 p-1.5 rounded-full shadow-sm">
                                        <ArrowDown size={14} className="text-slate-600" />
                                    </div>
                                </div>
                            )}
                        </div>
                    ))}
                </div>

            </div>
        </section>
    );
};
