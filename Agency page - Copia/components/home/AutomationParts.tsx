
import React from 'react';
import { motion } from 'framer-motion';
import {
    Scan, FileWarning, ShieldAlert, Ban, AlertTriangle, Bot, Activity, Database, TrendingUp, Scale, CheckCircle2, Cpu, XCircle, Clock
} from 'lucide-react';

const MotionDiv = motion.div as any;

const platinumGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 50%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,0.1))'
};

const brightSilverGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 20%, #F1F5F9 50%, #CBD5E1 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.5))'
};

export const AutomationHeader = () => (
    <div className="flex flex-col items-center text-center mb-20 md:mb-32 relative">
        <MotionDiv
            initial={{ scale: 0.9, opacity: 0 }}
            whileInView={{ scale: 1, opacity: 1 }}
            viewport={{ once: true }}
            className="mb-8 inline-flex items-center gap-3 px-6 py-2 bg-[#0f2e4a]/30 border border-slate-400/30 backdrop-blur-md rounded-sm shadow-[0_0_20px_rgba(14,165,233,0.1)] relative z-20"
        >
            <Scan className="text-sky-300 animate-pulse" size={16} />
            <span className="font-mono text-[10px] font-black uppercase tracking-[0.3em] text-sky-100">
                Forensic System Analysis
            </span>
        </MotionDiv>

        <h2 className="font-serif text-4xl sm:text-5xl md:text-7xl lg:text-8xl text-white tracking-tighter leading-[0.9] mb-12 drop-shadow-[0_4px_10px_rgba(0,0,0,0.8)]">
            <span className="font-thin italic tracking-normal text-sky-200/60">il</span> <span style={platinumGradient as any} className="font-black">lavoro manuale</span> <br />
            <span className="font-thin italic tracking-normal text-sky-200/60">è un </span>
            <span style={brightSilverGradient as any} className="font-black drop-shadow-[0_0_35px_rgba(255,255,255,0.5)]">crimine.</span>
        </h2>

        <div className="w-full max-w-3xl mx-auto p-[1px] bg-gradient-to-r from-slate-600 via-sky-300 to-slate-700 rounded-lg shadow-[0_0_50px_rgba(14,165,233,0.1)]">
            <div className="bg-[#020617]/90 rounded-lg p-6 md:p-10 relative overflow-hidden backdrop-blur-sm">
                <div className="absolute top-0 right-0 p-3 opacity-10 pointer-events-none">
                    <FileWarning size={80} className="text-sky-400" />
                </div>
                <p className="text-lg md:text-2xl font-serif font-medium text-sky-100/90 mb-6 leading-relaxed relative z-10 italic">
                    "Ogni minuto che il tuo team passa a spostare dati invece di chiudere contratti è un furto diretto al tuo margine operativo netto."
                </p>
                <div className="flex items-center gap-3 relative z-10">
                    <div className="h-[2px] w-12 bg-sky-400"></div>
                    <p className="text-sky-300 font-mono text-[10px] uppercase tracking-widest font-black">
                        Rapporto Empire Systems
                    </p>
                </div>
            </div>
        </div>
    </div>
);

export const UserIcon = ({ size, className }: { size?: number, className?: string }) => (
    <svg
        xmlns="http://www.w3.org/2000/svg"
        width={size}
        height={size}
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={className}
    >
        <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
        <circle cx="12" cy="7" r="4" />
    </svg>
);
