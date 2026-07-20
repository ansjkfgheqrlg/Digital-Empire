
import React from 'react';
import { AreaChart, Area, ResponsiveContainer } from 'recharts';
import { 
  ArrowRight, Activity, Globe, Shield, Search, LayoutGrid, Bell, HelpCircle, TrendingUp, Users 
} from 'lucide-react';

interface BrandLandingProps {
  onNavigate: (path: string) => void;
}

export const BrandLanding: React.FC<BrandLandingProps> = ({ onNavigate }) => {
  
  // Dati del grafico per matchare visivamente la curva dell'immagine
  const chartData = [
    { name: '1', val: 10 }, { name: '2', val: 25 }, { name: '3', val: 15 }, 
    { name: '4', val: 35 }, { name: '5', val: 30 }, { name: '6', val: 50 },
    { name: '7', val: 45 }, { name: '8', val: 65 }, { name: '9', val: 55 },
    { name: '10', val: 80 }, { name: '11', val: 70 }, { name: '12', val: 95 }
  ];

  return (
    <div className="min-h-screen bg-[#020202] text-white font-sans relative overflow-hidden flex flex-col selection:bg-white selection:text-black">
        
        {/* --- CINEMATIC BACKGROUND SYSTEM --- */}
        <div className="absolute inset-0 pointer-events-none select-none">
            
            {/* 1. Volumetric Top Spotlight (Studio Light Effect) */}
            <div className="absolute top-[-20%] left-1/2 -translate-x-1/2 w-[120%] h-[800px] bg-[radial-gradient(circle,rgba(255,255,255,0.06)_0%,transparent_60%)] blur-[100px]"></div>
            
            {/* 2. Bottom Glow (Lifts the dashboard) */}
            <div className="absolute bottom-[-20%] left-1/2 -translate-x-1/2 w-[100%] h-[600px] bg-[radial-gradient(circle,rgba(255,255,255,0.03)_0%,transparent_70%)] blur-[120px]"></div>

            {/* 3. Film Grain Overlay */}
            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.04] mix-blend-overlay"></div>
            
            {/* 4. High Fidelity Wings (SVG) */}
            <svg className="absolute inset-0 w-full h-full opacity-80" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">
                <defs>
                    <linearGradient id="wingGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stopColor="white" stopOpacity="0" />
                        <stop offset="40%" stopColor="white" stopOpacity="0.6" />
                        <stop offset="60%" stopColor="white" stopOpacity="0.6" />
                        <stop offset="100%" stopColor="white" stopOpacity="0" />
                    </linearGradient>
                    <filter id="glow">
                        <feGaussianBlur stdDeviation="12" result="coloredBlur" />
                        <feMerge>
                            <feMergeNode in="coloredBlur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                </defs>
                
                {/* Left Wing Group */}
                <g transform="translate(-150, 0)">
                    <path d="M 0 -100 Q 500 450 0 1200" stroke="url(#wingGradient)" strokeWidth="3" fill="none" filter="url(#glow)" opacity="0.5" />
                    <path d="M 40 -100 Q 540 450 40 1200" stroke="url(#wingGradient)" strokeWidth="1" fill="none" opacity="0.3" />
                </g>

                {/* Right Wing Group */}
                <g transform="translate(150, 0)">
                    <path d="M 1440 -100 Q 940 450 1440 1200" stroke="url(#wingGradient)" strokeWidth="3" fill="none" filter="url(#glow)" opacity="0.5" />
                    <path d="M 1400 -100 Q 900 450 1400 1200" stroke="url(#wingGradient)" strokeWidth="1" fill="none" opacity="0.3" />
                </g>
            </svg>

            {/* 5. Particle Starfield */}
            <div className="absolute inset-0">
                {[...Array(25)].map((_, i) => (
                    <div 
                        key={i}
                        className="absolute bg-white rounded-full animate-pulse"
                        style={{
                            top: `${Math.random() * 100}%`,
                            left: `${Math.random() * 100}%`,
                            width: Math.random() > 0.7 ? '2px' : '1px',
                            height: Math.random() > 0.7 ? '2px' : '1px',
                            opacity: Math.random() * 0.4 + 0.1,
                            animationDuration: `${Math.random() * 3 + 2}s`,
                            animationDelay: `${Math.random() * 5}s`
                        }}
                    ></div>
                ))}
            </div>
        </div>

        {/* --- HEADER --- */}
        <nav className="flex justify-between items-center px-8 md:px-12 py-8 relative z-50 max-w-[1400px] mx-auto w-full">
            <div className="flex items-center gap-3 cursor-pointer group" onClick={() => onNavigate('/')}>
                <div className="w-8 h-8 bg-white rounded-full flex items-center justify-center transition-transform group-hover:scale-110 shadow-[0_0_15px_rgba(255,255,255,0.5)]">
                    <div className="w-3 h-3 bg-black rounded-full"></div>
                </div>
                <span className="text-lg font-bold tracking-wide text-white">AUREUS</span>
            </div>
            
            <div className="hidden md:flex items-center gap-10 text-sm font-medium text-[#9CA3AF]">
                <button className="hover:text-white transition-colors hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">Services</button>
                <button className="hover:text-white transition-colors hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">Why Us</button>
                <button className="hover:text-white transition-colors hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">Solution</button>
                <button className="hover:text-white transition-colors hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">Pricing</button>
                <button className="hover:text-white transition-colors hover:drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]">FAQ</button>
            </div>

            <button 
                onClick={() => onNavigate('/')}
                className="hidden md:block px-6 py-2.5 rounded-full border border-white/20 text-white text-xs font-medium hover:bg-white hover:text-black transition-all hover:shadow-[0_0_20px_rgba(255,255,255,0.3)]"
            >
                Contact Us
            </button>
        </nav>

        {/* --- MAIN CONTENT --- */}
        <div className="flex-1 flex flex-col items-center pt-16 md:pt-24 relative z-10 w-full px-4 text-center">
            
            {/* AI Badge */}
            <div className="mb-10 animate-in fade-in slide-in-from-bottom-4 duration-700">
                <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#111] border border-white/10 shadow-[0_0_30px_rgba(255,255,255,0.1)] backdrop-blur-sm group hover:border-white/30 transition-all">
                    <span className="text-amber-400 text-xs shadow-amber-400/50 drop-shadow-sm">✨</span>
                    <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-400 group-hover:text-white transition-colors">Enterprise Operating System</span>
                </div>
            </div>

            {/* Silver Headline */}
            <div className="max-w-5xl mx-auto space-y-6 mb-12 animate-in fade-in slide-in-from-bottom-6 duration-700 delay-100 relative z-20">
                <h1 className="text-5xl md:text-[84px] leading-[1.05] font-bold tracking-tight">
                    <span className="text-transparent bg-clip-text bg-gradient-to-b from-white via-[#E2E8F0] to-[#64748B] drop-shadow-[0_0_30px_rgba(255,255,255,0.2)]">
                        Areus: Piattaforma Gestionale
                    </span>
                    <br/>
                    <span className="text-transparent bg-clip-text bg-gradient-to-b from-white via-[#E2E8F0] to-[#64748B] drop-shadow-[0_0_30px_rgba(255,255,255,0.2)]">
                        Team - Digital Empire
                    </span>
                </h1>
                
                <p className="text-[#9CA3AF] text-lg max-w-3xl mx-auto leading-relaxed font-normal pt-2">
                    Il sistema operativo definitivo per centralizzare processi, automazioni e performance. Organizza il tuo impero digitale con precisione ed efficienza assoluta.
                </p>
                
                <div className="pt-8">
                    <button 
                        onClick={() => onNavigate('/')}
                        className="bg-gradient-to-b from-[#FFFFFF] via-[#E2E8F0] to-[#94A3B8] text-black px-10 py-4 rounded-lg text-sm font-bold tracking-wide hover:scale-105 transition-transform shadow-[0_0_40px_rgba(255,255,255,0.3)] border border-white/50"
                    >
                        Accedi alla Dashboard
                    </button>
                </div>
            </div>

            {/* --- 3D DASHBOARD MOCKUP --- */}
            <div className="relative w-full max-w-[1000px] mx-auto mt-12 perspective-[2000px] pb-20">
                
                {/* Glow behind mockup - Enhanced */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[110%] h-[400px] bg-white opacity-[0.05] blur-[150px] rounded-full pointer-events-none"></div>

                <div className="relative bg-[#0E0E0E]/80 backdrop-blur-2xl border border-white/10 rounded-xl overflow-hidden shadow-2xl animate-in fade-in slide-in-from-bottom-10 duration-1000 delay-200 transform rotate-x-6 origin-center hover:rotate-x-0 transition-transform duration-700 ease-out ring-1 ring-white/10 group">
                    
                    <div className="flex h-[550px]">
                        {/* Sidebar */}
                        <div className="w-16 bg-[#080808]/90 border-r border-white/5 flex flex-col items-center py-8 gap-8">
                            <div className="p-2.5 bg-white/10 rounded-lg text-white shadow-[0_0_15px_rgba(255,255,255,0.1)]"><LayoutGrid className="w-5 h-5"/></div>
                            <div className="p-2.5 text-gray-600 hover:text-white transition-colors cursor-pointer"><Users className="w-5 h-5"/></div>
                            <div className="p-2.5 text-gray-600 hover:text-white transition-colors cursor-pointer"><Activity className="w-5 h-5"/></div>
                            <div className="p-2.5 text-gray-600 hover:text-white transition-colors cursor-pointer"><Globe className="w-5 h-5"/></div>
                            <div className="mt-auto p-2.5 text-gray-600 hover:text-white transition-colors cursor-pointer"><Shield className="w-5 h-5"/></div>
                        </div>

                        {/* Main Dash Area */}
                        <div className="flex-1 p-8 bg-gradient-to-b from-[#0E0E0E]/90 to-[#050505]/95">
                            
                            {/* Header Row */}
                            <div className="flex justify-between items-center mb-10">
                                <h3 className="text-2xl font-semibold text-white tracking-tight">Results</h3>
                                
                                <div className="flex items-center gap-4">
                                    <div className="hidden md:flex bg-[#121212] border border-white/5 rounded-lg p-1">
                                        <button className="px-3 py-1.5 text-[10px] font-medium text-white bg-[#222] rounded shadow-sm border border-white/5">Sort by</button>
                                        <button className="px-3 py-1.5 text-[10px] font-medium text-gray-500 hover:text-white transition-colors">Last 12 months</button>
                                        <button className="px-3 py-1.5 text-[10px] font-medium text-gray-500 hover:text-white transition-colors">List view</button>
                                    </div>
                                    
                                    <div className="relative group/search">
                                        <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 group-hover/search:text-gray-300 transition-colors"/>
                                        <input type="text" placeholder="Search contacts" className="bg-[#121212] border border-white/5 rounded-full py-2 pl-9 pr-4 text-xs text-white w-40 focus:w-48 focus:outline-none focus:border-white/20 transition-all"/>
                                    </div>
                                    
                                    <button className="flex items-center gap-2 px-3 py-1.5 rounded-full border border-white/10 text-[10px] text-gray-400 hover:text-white hover:bg-white/5 transition-all">
                                        <HelpCircle className="w-3.5 h-3.5" /> Need help
                                    </button>
                                    
                                    <div className="relative cursor-pointer w-8 h-8 rounded-full border border-white/5 flex items-center justify-center bg-[#121212] hover:bg-[#1a1a1a]">
                                        <Bell className="w-4 h-4 text-gray-400" />
                                        <span className="absolute top-1.5 right-2 w-1.5 h-1.5 bg-red-500 rounded-full border border-[#121212] animate-pulse"></span>
                                    </div>
                                </div>
                            </div>

                            {/* Metrics Grid */}
                            <div className="grid grid-cols-4 gap-5 mb-8">
                                {/* Card 1 */}
                                <div className="p-5 bg-[#121212] rounded-xl border border-white/5 hover:border-white/20 transition-all group/card shadow-lg hover:shadow-2xl hover:shadow-white/5">
                                    <div className="flex justify-between items-start mb-3">
                                        <p className="text-[11px] text-gray-500 font-medium">Total visits</p>
                                        <div className="w-6 h-6 rounded-full bg-white/5 flex items-center justify-center text-gray-400 group-hover/card:text-white transition-colors">
                                            <Activity className="w-3 h-3"/>
                                        </div>
                                    </div>
                                    <div className="flex items-end justify-between">
                                        <p className="text-3xl font-semibold text-white">2.1M</p>
                                        <div className="flex -space-x-2">
                                            <div className="w-6 h-6 rounded-full bg-gray-700 border-2 border-[#121212]"></div>
                                            <div className="w-6 h-6 rounded-full bg-gray-500 border-2 border-[#121212]"></div>
                                            <div className="w-6 h-6 rounded-full bg-gray-300 border-2 border-[#121212] flex items-center justify-center text-[8px] text-black font-bold">8</div>
                                        </div>
                                    </div>
                                </div>

                                {/* Card 2 */}
                                <div className="p-5 bg-[#121212] rounded-xl border border-white/5 hover:border-white/20 transition-all group/card shadow-lg hover:shadow-2xl hover:shadow-white/5">
                                    <div className="flex justify-between items-start mb-3">
                                        <p className="text-[11px] text-gray-500 font-medium">Total pageviews</p>
                                        <div className="w-6 h-6 rounded-full bg-white/5 flex items-center justify-center text-gray-400 group-hover/card:text-white transition-colors">
                                            <Globe className="w-3 h-3"/>
                                        </div>
                                    </div>
                                    <div className="flex flex-col gap-2">
                                        <p className="text-3xl font-semibold text-white">5.2M</p>
                                        <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                                            <div className="h-full w-[75%] bg-gradient-to-r from-gray-500 to-white"></div>
                                        </div>
                                    </div>
                                </div>

                                {/* Card 3 */}
                                <div className="p-5 bg-[#121212] rounded-xl border border-white/5 hover:border-white/20 transition-all group/card shadow-lg hover:shadow-2xl hover:shadow-white/5">
                                    <div className="flex justify-between items-start mb-3">
                                        <p className="text-[11px] text-gray-500 font-medium">Bounce rate</p>
                                        <div className="w-6 h-6 rounded-full bg-white/5 flex items-center justify-center text-gray-400 group-hover/card:text-white transition-colors">
                                            <TrendingUp className="w-3 h-3"/>
                                        </div>
                                    </div>
                                    <div className="flex flex-col gap-2">
                                        <p className="text-3xl font-semibold text-white">60%</p>
                                        <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                                            <div className="h-full w-[60%] bg-gradient-to-r from-gray-500 to-white"></div>
                                        </div>
                                    </div>
                                </div>

                                {/* Card 4 - Action */}
                                <div className="p-5 bg-[#121212] rounded-xl border border-white/5 flex flex-col items-center justify-center text-center hover:bg-white/5 transition-all cursor-pointer border-dashed border-white/10 hover:border-white/20 group/action">
                                    <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center mb-2 group-hover/action:scale-110 transition-transform group-hover/action:bg-white/10">
                                        <ArrowRight className="w-4 h-4 text-white"/>
                                    </div>
                                    <span className="text-[10px] text-gray-400 font-medium group-hover/action:text-white">View all reports</span>
                                </div>
                            </div>

                            {/* Chart Area */}
                            <div className="w-full h-60 relative rounded-lg overflow-hidden border border-white/5 bg-[#121212]/50">
                                {/* Fade overlay at bottom */}
                                <div className="absolute inset-0 bg-gradient-to-t from-[#0E0E0E] via-transparent to-transparent z-10 pointer-events-none"></div>
                                
                                <ResponsiveContainer width="100%" height="100%">
                                    <AreaChart data={chartData}>
                                        <defs>
                                            <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
                                                <stop offset="5%" stopColor="#fff" stopOpacity={0.2}/>
                                                <stop offset="95%" stopColor="#fff" stopOpacity={0}/>
                                            </linearGradient>
                                        </defs>
                                        <Area 
                                            type="monotone" 
                                            dataKey="val" 
                                            stroke="#fff" 
                                            strokeWidth={2} 
                                            fill="url(#chartGradient)" 
                                            animationDuration={1500}
                                        />
                                    </AreaChart>
                                </ResponsiveContainer>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  );
};
