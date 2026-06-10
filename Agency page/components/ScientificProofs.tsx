
import React from 'react';
import { motion } from 'framer-motion';
import { DustCanvas } from './ui/DustCanvas';

const MotionDiv = motion.div as any;

export const ScientificProofs: React.FC = () => {

  const rows = [
    {
      type: "donut",
      percent: 89,
      legend: ["Marketing personalizzato", "Marketing generico"],
      title: "89% dei leader in business crede nel marketing personalizzato",
      desc: "\"Marketing personalizzato\" è il contrario di \"marketing standard\". Capisci? Personalizzare, complottare, strategizzare correttamente è una cosa che i leader vogliono.\nMia opinione: spesso non lo fanno (anche se lo vogliono) perché non hanno tempo. Menomale che ci sei tu ad aiutarli (e farti pagare nel frattempo).",
      source: "#"
    },
    {
      type: "bar_comparison",
      val1: 20, // Small bar
      val2: 100, // Big bar
      highlightText: "+313%",
      legend: ["Marketers che non strategizzano", "Marketers strategici"],
      title: "313% in più di successo per aziende con marketing strategico.",
      desc: "Cioè, hai più di 3 volte le chance di vittoria rispetto a chi non usa una strategia. E non so te, ma girando su Facebook Ad Library a me non sembra che in Italia usino chissà che strategia (lol).",
      source: "#"
    },
    {
      type: "donut",
      percent: 68,
      legend: ["Aziende senza funnel efficace", "Aziende con funnel efficace"],
      title: "68% delle aziende non hanno identificato un funnel efficace",
      desc: "E nemmeno ci hanno provato. Significa che la maggior parte delle aziende sta andando... Un po' a casaccio 🤡. Secondo me non è che la fanno apposta. Dubito ci sia un CEO che dice \"regà oggi ci giochiamo 10k su FB Ads\". Semplicemente non sanno, non sanno di non sapere o non hanno tempo. Fatti pagare migliaia di euro per aiutarle ad aprire gli occhi.",
      source: "#"
    },
    {
      type: "bar_double",
      bars: [
          { val: 60, label: "+30%", sub: "Apertura delle email" },
          { val: 100, label: "+50%", sub: "Click sulle mail" }
      ],
      legend: ["Performance delle email segmentate", "rispetto a quelle non segmentate"],
      title: "30% più aperture e 50% più clic con email segmentate.",
      desc: "La maggior parte delle aziende ha un'unica mailing list a cui inviano di tutto. Sono recentemente stato pagato da un'azienda di Self Publishing per segmentare il pubblico proprio perché genera più vendite. Perché? Perché più segmenti le email, più diventano personalizzate.",
      source: "#"
    },
    {
      type: "donut",
      percent: 53.7,
      legend: ["Strategia > skill sottovalutata", "Strategia > skill qualsiasi"],
      title: "53.7% dei marketer pensano che la strategia sia una skill sottovalutata",
      desc: "Parola chiave: \"skill\". E' un'abilità, una cosa che puoi sviluppare. Perché \"strategia\" non è solo buzzword corporate che usano i power-user di LinkedIn. E' una reale skill che fa una reale differenza.",
      source: "#"
    }
  ];

  return (
    <section className="py-32 relative overflow-hidden border-t border-white/5 bg-black">
        
        {/* Background Atmosphere - Matched to CroFunnelSection */}
        <div className="absolute top-0 left-0 w-full h-full pointer-events-none z-0">
             <div className="absolute inset-0 bg-gradient-to-b from-black via-[#050505] to-black opacity-100"></div>
             <DustCanvas />
        </div>
        
        <div className="container mx-auto px-6 max-w-6xl relative z-10">
            {/* Header */}
            <div className="text-center mb-24">
                <h2 className="font-serif text-3xl md:text-5xl text-white font-medium leading-tight lowercase">
                    ...la scienza parla chiaro: <br />
                    funnel personalizzato = più <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#FDE68A] via-[#D4AF37] to-[#B45309] font-bold">profitto</span> <br />
                    (e quindi meno <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-500 to-red-800 font-bold">perdite</span>)
                </h2>
            </div>

            {/* Content Rows */}
            <div className="space-y-0">
                {rows.map((row, i) => (
                    <MotionDiv 
                        key={i}
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: i * 0.1 }}
                        className="flex flex-col md:flex-row items-center gap-12 md:gap-24 py-20 border-t border-white/5"
                    >
                        {/* LEFT: CHART VISUAL */}
                        <div className="w-full md:w-1/3 flex flex-col items-center justify-center">
                           <ChartVisual row={row} />
                           
                           {/* LEGEND */}
                           <div className="mt-8 flex flex-col gap-2 text-[10px] font-mono uppercase tracking-widest text-gray-500 w-full max-w-[200px]">
                                {row.type === 'bar_double' ? (
                                    <>
                                        <div className="text-white font-bold mb-1 lowercase">{row.legend[0]}</div>
                                        <div className="lowercase opacity-60">{row.legend[1]}</div>
                                    </>
                                ) : (
                                    <>
                                        <div className="flex items-center gap-3">
                                            <div className="w-3 h-3 bg-gradient-to-br from-[#FDE68A] to-[#B45309]"></div>
                                            <span className="text-gray-300 lowercase">{row.legend[0]}</span>
                                        </div>
                                        <div className="flex items-center gap-3">
                                            <div className="w-3 h-3 bg-gradient-to-br from-[#E2E8F0] to-[#475569]"></div>
                                            <span className="text-gray-600 lowercase">{row.legend[1]}</span>
                                        </div>
                                    </>
                                )}
                           </div>
                        </div>

                        {/* RIGHT: TEXT COPY */}
                        <div className="w-full md:w-2/3 text-left">
                            <h3 className="font-sans text-2xl md:text-3xl text-white font-bold mb-6 leading-tight lowercase tracking-tight">
                                {row.title}
                            </h3>
                            <p className="font-sans text-gray-400 text-base leading-relaxed mb-6 font-light whitespace-pre-line lowercase">
                                {row.desc}
                            </p>
                            <a href="#" className="text-xs font-mono text-gray-600 underline hover:text-white transition-colors uppercase tracking-widest lowercase">
                                fonte
                            </a>
                        </div>
                    </MotionDiv>
                ))}
            </div>
        </div>
    </section>
  );
};

const ChartVisual = ({ row }: { row: any }) => {
    // DONUT
    if (row.type === 'donut') {
        return (
            <div className="relative w-40 h-40">
                <svg viewBox="0 0 36 36" className="w-full h-full rotate-[-90deg]">
                    {/* Background Circle (Silver) */}
                    <path className="text-slate-800" 
                        d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none" stroke="currentColor" strokeWidth="6" 
                    />
                    {/* Foreground Circle (Gold) */}
                    <path 
                        d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                        fill="none" 
                        stroke="url(#goldGradientChart)" 
                        strokeWidth="6"
                        strokeDasharray={`${row.percent}, 100`}
                    />
                    <defs>
                        <linearGradient id="goldGradientChart" x1="0%" y1="0%" x2="100%" y2="100%">
                             <stop offset="0%" stopColor="#FDE68A" />
                             <stop offset="50%" stopColor="#D4AF37" />
                             <stop offset="100%" stopColor="#B45309" />
                        </linearGradient>
                    </defs>
                </svg>
                {/* Center Text */}
                <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-3xl font-black text-white tracking-tighter">{row.percent}%</span>
                </div>
            </div>
        )
    }

    // BAR COMPARISON
    if (row.type === 'bar_comparison') {
        return (
            <div className="h-40 w-full max-w-[200px] flex items-end justify-center gap-6 pb-2 border-b border-white/10 relative">
                 {/* Silver Bar */}
                 <div className="w-12 bg-gradient-to-t from-slate-800 to-slate-500 rounded-t-sm" style={{ height: `${row.val1}%` }}></div>
                 {/* Gold Bar */}
                 <div className="w-12 bg-gradient-to-t from-[#B45309] via-[#D4AF37] to-[#FDE68A] rounded-t-sm relative shadow-[0_0_20px_rgba(212,175,55,0.2)]" style={{ height: `${row.val2}%` }}>
                      <div className="absolute -top-8 left-1/2 -translate-x-1/2 text-gold-400 font-bold text-lg whitespace-nowrap">{row.highlightText}</div>
                 </div>
            </div>
        )
    }

    // BAR DOUBLE
    if (row.type === 'bar_double') {
        return (
            <div className="h-40 w-full max-w-[200px] flex items-end justify-center gap-4 pb-2 border-b border-white/10 relative">
                 {row.bars.map((bar: any, i: number) => (
                     <div key={i} className="w-12 bg-gradient-to-t from-[#B45309] via-[#D4AF37] to-[#FDE68A] rounded-t-sm relative shadow-[0_0_20px_rgba(212,175,55,0.2)] flex flex-col justify-end items-center pb-2 group" style={{ height: `${bar.val}%` }}>
                         <span className="text-white font-bold text-xs mb-1">{bar.label}</span>
                         <div className="absolute bottom-[-40px] text-[8px] text-gray-500 w-24 text-center leading-tight uppercase font-mono lowercase">{bar.sub}</div>
                     </div>
                 ))}
            </div>
        )
    }

    return null;
}
