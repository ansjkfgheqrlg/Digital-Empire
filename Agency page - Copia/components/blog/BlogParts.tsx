
import React from 'react';
import { motion } from 'framer-motion';
import { Activity, Zap, Book, Target, Quote, Check } from 'lucide-react';

const silverGradientStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 60%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    textShadow: '0px 2px 4px rgba(0,0,0,0.3)'
};

const goldGradientStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFF7ED 0%, #FDE68A 30%, #D4AF37 70%, #B45309 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 0px rgba(0,0,0,0.5))'
};

export interface SilverBodyProps {
    children?: React.ReactNode;
    className?: string;
}

export const SilverBody: React.FC<SilverBodyProps> = ({ children, className = "" }) => (
    <div className={`font-sans font-light tracking-wide leading-relaxed text-lg md:text-xl lowercase ${className}`}>
        <span style={silverGradientStyle as any}>
            {children}
        </span>
    </div>
);

export const ChapterTitle = ({ children, number }: { children?: React.ReactNode, number: string }) => (
    <div className="mt-20 mb-10 border-t border-white/10 pt-10 relative z-10">
        <span className="font-mono text-xs uppercase tracking-[0.4em] block mb-3 lowercase" style={goldGradientStyle as any}>capitolo {number}</span>
        <h3 className="text-3xl md:text-5xl font-serif font-black tracking-tight leading-none lowercase">
            <span style={silverGradientStyle as any}>{children}</span>
        </h3>
    </div>
);

export const DataBlock = ({ label, value, delta, color = "gold" }: { label: string, value: string, delta: string, color?: "gold" | "red" | "blue" | "green" | "purple" }) => {
    const borderClasses = {
        gold: "border-gold-500/30 bg-gold-950/20",
        red: "border-red-500/30 bg-red-950/20",
        blue: "border-cyan-500/30 bg-cyan-950/20",
        green: "border-emerald-500/30 bg-emerald-950/20",
        purple: "border-purple-500/30 bg-purple-950/20"
    };

    return (
        <div className={`my-12 p-8 rounded-xl border ${borderClasses[color]} backdrop-blur-md relative overflow-hidden group z-10 shadow-xl`}>
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity text-white">
                <Activity size={64} />
            </div>
            <div className="text-xs font-mono uppercase tracking-widest text-slate-400 mb-3 lowercase">{label}</div>
            <div className="flex items-end gap-6">
                <div className="text-4xl md:text-6xl font-black lowercase" style={silverGradientStyle as any}>{value}</div>
                <div className={`text-lg font-bold flex items-center gap-1 mb-2 lowercase`} style={goldGradientStyle as any}>
                    <TrendingUp size={20} className="text-gold-500" /> {delta}
                </div>
            </div>
        </div>
    );
};

export const InsightBox = ({ title, children }: { title: string, children?: React.ReactNode }) => (
    <div className="my-12 p-8 md:p-10 border-l-2 border-gold-500 bg-black/40 backdrop-blur-md rounded-r-xl relative z-10 shadow-lg">
        <h4 className="flex items-center gap-3 font-mono text-sm uppercase tracking-[0.2em] font-bold mb-6 lowercase" style={goldGradientStyle as any}>
            <Zap size={16} className="text-gold-500" /> {title}
        </h4>
        <div className="font-serif text-xl italic leading-relaxed lowercase" style={silverGradientStyle as any}>
            {children}
        </div>
    </div>
);

export const StoryBox = ({ title, children }: { title: string, children?: React.ReactNode }) => (
    <div className="my-20 relative z-10">
        <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-slate-500 to-transparent opacity-30"></div>
        <div className="absolute bottom-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-slate-500 to-transparent opacity-30"></div>
        <div className="py-12 px-6 md:px-16 bg-[#080808]/60 backdrop-blur-md border-y border-white/5">
            <div className="flex items-center justify-center gap-4 mb-8 opacity-60">
                <Book size={20} className="text-slate-400" />
                <span className="text-xs font-mono uppercase tracking-[0.3em] text-slate-400 lowercase">storytelling archive</span>
            </div>
            <h4 className="text-3xl text-center font-serif mb-10 tracking-tight lowercase" style={silverGradientStyle as any}>{title}</h4>
            <div className="silver-prose italic lowercase">
                {children}
            </div>
        </div>
    </div>
);

export const StrategyCard = ({ title, steps }: { title: string, steps: string[] }) => (
    <div className="my-12 bg-black/40 backdrop-blur-md border border-slate-700/50 p-8 rounded-xl shadow-2xl relative z-10">
        <h4 className="flex items-center gap-3 text-xl font-bold mb-8 lowercase">
            <Target className="text-red-500" />
            <span style={silverGradientStyle as any}>{title}</span>
        </h4>
        <div className="space-y-6">
            {steps.map((step, i) => (
                <div key={i} className="flex gap-5">
                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-slate-900 border border-slate-600 flex items-center justify-center text-sm font-bold text-slate-300 shadow-inner">
                        {i + 1}
                    </div>
                    <p style={silverGradientStyle as any} className="text-lg lowercase">{step}</p>
                </div>
            ))}
        </div>
    </div>
);

export const EmpireQuote = ({ text, author }: { text: string, author?: string }) => (
    <div className="relative my-20 py-16 px-8 md:px-24 text-center bg-black/30 backdrop-blur-sm rounded-2xl border border-white/5 shadow-2xl z-10">
        <Quote className="absolute top-8 left-8 text-gold-500/20 w-16 h-16 transform -scale-x-100" />
        <h3 className="text-3xl md:text-5xl font-serif font-medium leading-tight mb-8 relative z-10 lowercase">
            <span style={silverGradientStyle as any}>"{text}"</span>
        </h3>
        {author && <div className="text-xs font-mono uppercase tracking-[0.4em] opacity-70 lowercase" style={goldGradientStyle as any}>— {author}</div>}
    </div>
);

export const ActionList = ({ items }: { items: string[] }) => (
    <div className="my-16 bg-[#030303]/60 backdrop-blur-md border border-gold-500/30 rounded-xl p-8 md:p-12 shadow-[0_0_60px_rgba(0,0,0,0.5)] relative z-10">
        <h4 className="font-serif text-2xl text-white mb-8 border-b border-white/5 pb-4 flex justify-between items-center lowercase">
            <span style={silverGradientStyle as any}>protocollo di implementazione</span>
            <span className="text-[10px] font-mono uppercase tracking-widest bg-gold-950/30 px-3 py-1 rounded text-gold-500 border border-gold-500/20 lowercase">actionable</span>
        </h4>
        <ul className="space-y-6">
            {items.map((item, i) => (
                <li key={i} className="flex items-start gap-4 group">
                    <div className="mt-1 w-6 h-6 rounded-full border border-gold-500 flex items-center justify-center group-hover:bg-gold-500 transition-colors flex-shrink-0 shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                        <Check size={12} className="text-gold-500 group-hover:text-black-900 transition-colors" />
                    </div>
                    <span className="text-lg leading-relaxed group-hover:translate-x-1 transition-transform duration-300 lowercase" style={silverGradientStyle as any}>{item}</span>
                </li>
            ))}
        </ul>
    </div>
);

export const MetallicFrame = ({ children, className = "", intensity = "silver" }: { children?: React.ReactNode, className?: string, intensity?: 'silver' | 'gold' | 'red' | 'blue' | 'purple' | 'emerald' }) => {
    const gradients = {
        silver: "from-slate-300 via-slate-500 to-slate-800",
        gold: "from-yellow-200 via-yellow-600 to-slate-800",
        red: "from-red-300 via-red-600 to-slate-900",
        blue: "from-cyan-300 via-cyan-600 to-slate-900",
        purple: "from-purple-300 via-purple-600 to-slate-900",
        emerald: "from-emerald-300 via-emerald-600 to-slate-900"
    };

    return (
        <div className={`relative p-[1px] rounded-sm group overflow-hidden ${className}`}>
            <div className={`absolute inset-0 bg-gradient-to-br ${gradients[intensity as keyof typeof gradients] || gradients.silver} opacity-100 z-0`}></div>
            <div className="relative z-10 bg-[#050505] h-full w-full rounded-sm overflow-hidden">
                <div className="absolute inset-0 opacity-20 pointer-events-none mix-blend-overlay bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-white/5 to-transparent pointer-events-none"></div>
                {children}
            </div>
        </div>
    );
};

const TrendingUp = ({ size, className }: { size?: number, className?: string }) => (
    <svg xmlns="http://www.w3.org/2000/svg" width={size || 24} height={size || 24} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline></svg>
);
