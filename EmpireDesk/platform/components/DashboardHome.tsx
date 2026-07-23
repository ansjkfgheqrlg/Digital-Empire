
import React from 'react';
import { Task, Lead, User, InfobusinessProduct } from '../types';
import { DollarSign, Users, Activity, Book, ShieldCheck, Database, Server, Briefcase } from 'lucide-react';
import { 
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer
} from 'recharts';

interface DashboardHomeProps {
  currentUser: User;
  tasks: Task[];
  leads: Lead[];
  products: InfobusinessProduct[];
}

export const DashboardHome: React.FC<DashboardHomeProps> = ({ currentUser, tasks, leads, products }) => {
  
  const totalRevenue = leads
    .filter(l => l.stage === 'CLOSED_WON')
    .reduce((acc, curr) => acc + curr.value, 0);
  
  const pendingTasks = tasks.filter(t => t.status !== 'DONE').length;
  const activeLeads = leads.filter(l => l.stage !== 'CLOSED_WON' && l.stage !== 'CLOSED_LOST').length;
  const totalSales = products.reduce((acc, curr) => acc + (curr.sales * curr.price), 0);

  const stats = [
    { label: 'Fatturato Agenzia', value: `€${totalRevenue.toLocaleString()}`, icon: DollarSign },
    { label: 'Lead Attivi', value: activeLeads.toString(), icon: Users },
    { label: 'Task da Fare', value: pendingTasks.toString(), icon: Activity },
    { label: 'Vendite Info', value: `€${totalSales.toLocaleString()}`, icon: Book },
  ];

  const chartData = [
    { name: 'SET 1', value: totalRevenue * 0.2 },
    { name: 'SET 2', value: totalRevenue * 0.4 },
    { name: 'SET 3', value: totalRevenue * 0.6 },
    { name: 'SET 4', value: totalRevenue },
  ];

  // --- TRUE PURE SILVER STYLE ---
  // Heavy Metal Gradient: White -> Light Gray -> Dark Gray -> Light Gray (Simulates reflection)
  // Beveled Borders: Light Top/Left, Dark Bottom/Right
  const pureSilverBlockClass = `
    bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8]
    border-t border-l border-white/90 border-b border-r border-slate-500/60
    rounded-2xl p-6 shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5),inset_0_1px_0_rgba(255,255,255,0.8)]
    relative overflow-hidden group hover:-translate-y-1 hover:shadow-[0_20px_35px_-8px_rgba(0,0,0,0.65),inset_0_1px_0_rgba(255,255,255,0.8)]
    transition-all duration-300
  `;
  
  // Text needs to be dark to contrast with silver
  const silverTextMain = "text-slate-900 drop-shadow-[0_1px_0_rgba(255,255,255,0.5)]"; 
  const silverTextSub = "text-slate-600 font-medium";
  const silverIconBg = "bg-gradient-to-br from-slate-200 to-slate-300 border border-white shadow-inner text-slate-800";

  return (
    <div className="space-y-8 animate-in fade-in slide-in-from-bottom-2 duration-500 pb-10">
      
      {/* Header - CHROME TEXT */}
      <div className="flex justify-between items-end border-b border-white/10 pb-6">
        <div>
           <h1 className="text-4xl font-black text-silver-gradient mb-2 tracking-tight">
             Panoramica Operativa
           </h1>
           <p className="text-platinum-400 text-sm font-medium">Bentornato, <span className="text-white font-bold">{currentUser.name}</span>. Ecco i dati in tempo reale.</p>
        </div>
        <div className="text-right">
            <p className="text-xs text-platinum-500 font-mono uppercase border border-white/10 px-3 py-1 rounded-sm bg-black/20">
              {new Date().toLocaleDateString('it-IT', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
            </p>
        </div>
      </div>

      {/* KPI Cards - PURE SILVER BLOCKS */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className={pureSilverBlockClass}>
                 {/* Brushed Metal Texture */}
                 <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
                 
                 {/* High Gloss Shine Top Right */}
                 <div className="absolute top-[-50%] right-[-50%] w-[200%] h-[200%] bg-gradient-to-b from-white/40 via-transparent to-transparent rotate-45 pointer-events-none"></div>
                 
                 <div className="flex justify-between items-start mb-4 relative z-10">
                    <span className={`text-[10px] font-bold uppercase tracking-widest ${silverTextSub}`}>{stat.label}</span>
                    <div className={`p-2 rounded-full ${silverIconBg} shadow-sm`}>
                        <Icon className="w-5 h-5" />
                    </div>
                 </div>
                 <div className={`text-3xl font-black tracking-tight mb-2 ${silverTextMain}`}>{stat.value}</div>
                 
                 <div className="w-full bg-slate-900/10 h-1.5 rounded-full overflow-hidden relative z-10 border-t border-black/5 border-b border-white/20">
                    <div className="bg-slate-800 h-full w-2/3 group-hover:w-full transition-all duration-1000 shadow-[0_0_5px_rgba(0,0,0,0.3)]"></div>
                 </div>
            </div>
          );
        })}
      </div>

      {/* Chart Section & System Health - PURE SILVER BLOCKS */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className={`lg:col-span-2 ${pureSilverBlockClass}`}>
               <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>

               <div className="flex justify-between items-center mb-6 relative z-10">
                  <h3 className={`text-xs font-bold uppercase tracking-widest ${silverTextMain}`}>Andamento Finanziario</h3>
               </div>
               
               <div className="h-[250px] w-full relative z-10">
                   <ResponsiveContainer width="100%" height="100%">
                     <AreaChart data={chartData}>
                       <defs>
                         <linearGradient id="colorValueDark" x1="0" y1="0" x2="0" y2="1">
                           <stop offset="5%" stopColor="#0F172A" stopOpacity={0.1}/>
                           <stop offset="95%" stopColor="#0F172A" stopOpacity={0}/>
                         </linearGradient>
                       </defs>
                       <CartesianGrid strokeDasharray="3 3" stroke="#94a3b8" vertical={false} opacity={0.5} />
                       <XAxis dataKey="name" stroke="#475569" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} axisLine={false} tickLine={false} dy={10} />
                       <YAxis stroke="#475569" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} tickFormatter={(val) => `€${val}`} axisLine={false} tickLine={false} dx={-10} />
                       <Tooltip 
                          contentStyle={{ backgroundColor: '#f8fafc', borderColor: '#cbd5e1', borderRadius: '4px', color: '#0f172a', fontWeight: 'bold', boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)' }}
                          itemStyle={{ color: '#0f172a' }}
                       />
                       <Area type="monotone" dataKey="value" stroke="#0F172A" strokeWidth={3} fillOpacity={1} fill="url(#colorValueDark)" />
                     </AreaChart>
                   </ResponsiveContainer>
               </div>
          </div>

          {/* System Status Widget - PURE SILVER BLOCK */}
          <div className={`${pureSilverBlockClass} flex flex-col`}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              
              <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                  <ShieldCheck className="w-4 h-4 text-slate-600"/> System Health
              </h3>
              <div className="space-y-4 flex-1 relative z-10">
                  <div className="flex items-center justify-between p-3 bg-white/50 rounded-xl border border-white/60 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:shadow-md hover:bg-white/60">
                      <div className="flex items-center gap-3">
                          <Database className="w-4 h-4 text-slate-700"/>
                          <span className={`text-xs font-bold ${silverTextMain}`}>Database Leads</span>
                      </div>
                      <span className="text-[10px] font-bold text-emerald-700 flex items-center gap-1"><span className="w-1.5 h-1.5 bg-emerald-600 rounded-full animate-pulse shadow-[0_0_5px_#059669]"></span> ONLINE</span>
                  </div>
                  <div className="flex items-center justify-between p-3 bg-white/50 rounded-xl border border-white/60 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:shadow-md hover:bg-white/60">
                      <div className="flex items-center gap-3">
                          <Server className="w-4 h-4 text-slate-700"/>
                          <span className={`text-xs font-bold ${silverTextMain}`}>API Gateway</span>
                      </div>
                      <span className="text-[10px] font-bold text-emerald-700 flex items-center gap-1"><span className="w-1.5 h-1.5 bg-emerald-600 rounded-full animate-pulse shadow-[0_0_5px_#059669]"></span> ONLINE</span>
                  </div>
                  <div className="flex items-center justify-between p-3 bg-white/50 rounded-xl border border-white/60 shadow-sm backdrop-blur-sm transition-all duration-300 hover:-translate-y-0.5 hover:shadow-md hover:bg-white/60">
                      <div className="flex items-center gap-3">
                          <Activity className="w-4 h-4 text-slate-700"/>
                          <span className={`text-xs font-bold ${silverTextMain}`}>Latency</span>
                      </div>
                      <span className={`text-[10px] font-mono font-bold ${silverTextSub}`}>24ms</span>
                  </div>
              </div>
              <div className="mt-4 pt-4 border-t border-slate-300 text-center relative z-10">
                  <p className="text-[9px] text-slate-500 font-bold uppercase tracking-widest">All systems operational</p>
              </div>
          </div>
      </div>

      {/* Workflow & Agency Products - NEW SECTION */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
          {/* Prodotti Agency */}
          <div className={`${pureSilverBlockClass} flex flex-col`}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              <h3 className={`text-[11px] font-extrabold uppercase tracking-widest mb-4 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                  <Briefcase className="w-4 h-4 text-slate-600"/> Prodotti Agency
              </h3>
              <div className="space-y-3 relative z-10 flex-1 overflow-auto max-h-48 scrollbar-hide">
                  {products.slice(0, 4).map(p => (
                      <div key={p.id} className="flex justify-between items-center p-3 bg-white/40 rounded-xl border border-white/60 shadow-sm backdrop-blur-sm hover:-translate-y-0.5 transition-transform">
                         <div className="flex flex-col">
                             <span className={`text-[11px] font-bold ${silverTextMain}`}>{p.title}</span>
                             <span className={`text-[9.5px] uppercase font-bold text-slate-600`}>€{p.price.toLocaleString()}</span>
                         </div>
                         <div className="bg-slate-800 text-white text-[9.5px] px-2 py-0.5 rounded-full font-bold tracking-wider">
                             {p.sales} VENDITE
                         </div>
                      </div>
                  ))}
                  {products.length === 0 && (
                      <div className="text-[10px] text-slate-500 font-bold uppercase tracking-widest text-center mt-6">
                          Nessun prodotto configurato
                      </div>
                  )}
              </div>
          </div>
          
          {/* Sviluppo & Workflow */}
          <div className={`${pureSilverBlockClass} flex flex-col`}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              <h3 className={`text-[11px] font-extrabold uppercase tracking-widest mb-4 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                  <Activity className="w-4 h-4 text-slate-600"/> Sviluppo & Workflow Status
              </h3>
              <div className="space-y-4 relative z-10 flex-1">
                  <div className="p-3.5 bg-gradient-to-r from-[#D6E6F2] to-[#94BBD9] rounded-xl border border-white/60 shadow-[0_4px_10px_rgba(93,138,168,0.2)]">
                      <div className="flex justify-between items-center mb-1.5">
                          <span className="text-[10px] font-bold text-slate-800 uppercase tracking-widest">Engine S7 - Memoria Ecosistemi</span>
                          <span className="text-[10px] font-bold text-slate-800">45%</span>
                      </div>
                      <div className="w-full bg-white/40 h-1.5 rounded-full overflow-hidden shadow-inner">
                          <div className="bg-slate-800 h-full w-[45%] shadow-[0_0_8px_rgba(0,0,0,0.5)]"></div>
                      </div>
                  </div>
                  <div className="p-3.5 bg-gradient-to-r from-[#fbcfe8] to-[#f472b6] rounded-xl border border-white/60 shadow-[0_4px_10px_rgba(244,114,182,0.2)]">
                      <div className="flex justify-between items-center mb-1.5">
                          <span className="text-[10px] font-bold text-slate-800 uppercase tracking-widest">PreventivoForge UI (Prof Autocad)</span>
                          <span className="text-[10px] font-bold text-slate-800">80%</span>
                      </div>
                      <div className="w-full bg-white/40 h-1.5 rounded-full overflow-hidden shadow-inner">
                          <div className="bg-slate-800 h-full w-[80%] shadow-[0_0_8px_rgba(0,0,0,0.5)]"></div>
                      </div>
                  </div>
                  <div className="p-3.5 bg-gradient-to-r from-[#e2e8f0] to-[#cbd5e1] rounded-xl border border-white/60 shadow-sm">
                      <div className="flex justify-between items-center mb-1.5">
                          <span className="text-[10px] font-bold text-slate-800 uppercase tracking-widest">Aureus OS App Refactoring</span>
                          <span className="text-[10px] font-bold text-slate-800">95%</span>
                      </div>
                      <div className="w-full bg-white/40 h-1.5 rounded-full overflow-hidden shadow-inner">
                          <div className="bg-emerald-600 h-full w-[95%] shadow-[0_0_8px_rgba(5,150,105,0.5)]"></div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    </div>
  );
};
