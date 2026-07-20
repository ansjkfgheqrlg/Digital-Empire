
import React, { useState } from 'react';
import { Lead, Task, InfobusinessProduct, LeadStage, TaskStatus } from '../types';
import { 
  BarChart3, TrendingUp, Users, DollarSign, Activity, Calendar, Download, 
  PieChart as PieIcon, ArrowUpRight, ArrowDownRight, Target, Layers
} from 'lucide-react';
import { 
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, 
  BarChart, Bar, Cell, PieChart, Pie, Legend
} from 'recharts';
import { Button } from './ui/Button';

interface AnalyticsProps {
  leads: Lead[];
  tasks: Task[];
  products: InfobusinessProduct[];
}

const generateRevenueData = () => [
  { name: 'Gen', services: 4000, info: 2400 },
  { name: 'Feb', services: 3000, info: 1398 },
  { name: 'Mar', services: 2000, info: 9800 },
  { name: 'Apr', services: 2780, info: 3908 },
  { name: 'Mag', services: 1890, info: 4800 },
  { name: 'Giu', services: 2390, info: 3800 },
  { name: 'Lug', services: 3490, info: 4300 },
];

const generateLeadSourceData = () => [
  { name: 'Instagram', value: 45, color: '#be185d' }, // Pink
  { name: 'YouTube', value: 30, color: '#dc2626' },   // Red
  { name: 'Ads', value: 15, color: '#1d4ed8' },       // Blue
  { name: 'Referral', value: 10, color: '#047857' },  // Green
];

export const Analytics: React.FC<AnalyticsProps> = ({ leads, tasks, products }) => {
  const [timeRange, setTimeRange] = useState<'30D' | '90D' | 'YTD'>('30D');

  const totalRevenue = leads
    .filter(l => l.stage === LeadStage.CLOSED_WON)
    .reduce((acc, l) => acc + l.value, 0) 
    + products.reduce((acc, p) => acc + (p.sales * p.price), 0);

  const totalLeads = leads.length;
  const conversionRate = totalLeads > 0 
    ? (leads.filter(l => l.stage === LeadStage.CLOSED_WON).length / totalLeads) * 100 
    : 0;
  
  const completedTasks = tasks.filter(t => t.status === TaskStatus.DONE).length;
  const taskCompletionRate = tasks.length > 0 
    ? (completedTasks / tasks.length) * 100 
    : 0;

  const topProducts = [...products].sort((a, b) => (b.sales * b.price) - (a.sales * a.price)).slice(0, 5);

  // --- TRUE PURE SILVER STYLE ---
  const pureSilverBlockClass = `
    bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8] 
    border-t border-l border-white/90 border-b border-r border-slate-500/60
    rounded-sm p-6 shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5),inset_0_1px_0_rgba(255,255,255,0.8)]
    relative overflow-hidden flex flex-col group
  `;
  const silverTextMain = "text-slate-900 drop-shadow-[0_1px_0_rgba(255,255,255,0.5)]";
  const silverTextSub = "text-slate-600 font-medium";

  return (
    <div className="space-y-8 animate-in fade-in duration-500 pb-10">
      
      {/* Header */}
      <div className="flex flex-col md:flex-row justify-between items-end border-b border-white/10 pb-6 gap-4">
          <div>
              <h1 className="text-4xl font-black text-silver-gradient mb-2 tracking-tight">Business Intelligence</h1>
              <p className="text-platinum-500 text-sm">Analisi performance e metriche operative.</p>
          </div>
          <div className="flex gap-3">
              <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-1 flex shadow-inner">
                  {(['30D', '90D', 'YTD'] as const).map(range => (
                      <button 
                        key={range}
                        onClick={() => setTimeRange(range)}
                        className={`px-4 py-1.5 text-[10px] font-bold uppercase tracking-widest rounded-sm transition-all ${timeRange === range ? 'bg-white text-black shadow-lg' : 'text-platinum-500 hover:text-white'}`}
                      >
                          {range}
                      </button>
                  ))}
              </div>
              <Button variant="diamond" icon={<Download className="w-4 h-4"/>}>Export Report</Button>
          </div>
      </div>

      {/* KPI Cards - SILVER */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <KPICard title="Fatturato Totale" value={`€${totalRevenue.toLocaleString()}`} change="+12.5%" trend="UP" icon={DollarSign} />
          <KPICard title="Tasso Conversione" value={`${conversionRate.toFixed(1)}%`} change="+2.1%" trend="UP" icon={Target} />
          <KPICard title="Lead Acquisiti" value={totalLeads.toString()} change="-5%" trend="DOWN" icon={Users} />
          <KPICard title="Produttività Team" value={`${taskCompletionRate.toFixed(0)}%`} change="+8.4%" trend="UP" icon={Activity} />
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 h-[450px]">
          
          <div className={`lg:col-span-2 ${pureSilverBlockClass}`}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              
              <div className="flex justify-between items-center mb-6 relative z-10">
                  <h3 className={`text-xs font-bold uppercase tracking-widest flex items-center gap-2 ${silverTextMain}`}>
                      <TrendingUp className="w-4 h-4 text-slate-600"/> Revenue Trend
                  </h3>
                  <div className="flex gap-4 text-[10px] font-bold uppercase">
                      <span className="flex items-center gap-1 text-slate-700"><span className="w-2 h-2 rounded-full bg-slate-800"></span> Servizi</span>
                      <span className="flex items-center gap-1 text-slate-600"><span className="w-2 h-2 rounded-full bg-slate-400"></span> Infobusiness</span>
                  </div>
              </div>
              <div className="flex-1 w-full min-h-0 relative z-10">
                  <ResponsiveContainer width="100%" height="100%">
                      <AreaChart data={generateRevenueData()}>
                          <CartesianGrid strokeDasharray="3 3" stroke="#94a3b8" vertical={false} opacity={0.5} />
                          <XAxis dataKey="name" stroke="#64748B" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} axisLine={false} tickLine={false} dy={10} />
                          <YAxis stroke="#64748B" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} tickFormatter={(val) => `€${val/1000}k`} axisLine={false} tickLine={false} dx={-10} />
                          <Tooltip contentStyle={{ backgroundColor: '#fff', borderColor: '#e2e8f0', borderRadius: '4px', color: '#0f172a', fontWeight: 'bold' }} />
                          <Area type="monotone" dataKey="services" stroke="#1e293b" strokeWidth={2} fillOpacity={0.1} fill="#1e293b" />
                          <Area type="monotone" dataKey="info" stroke="#94a3b8" strokeWidth={2} fillOpacity={0.1} fill="#94a3b8" />
                      </AreaChart>
                  </ResponsiveContainer>
              </div>
          </div>

          <div className={pureSilverBlockClass}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              
              <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                  <PieIcon className="w-4 h-4 text-slate-600"/> Lead Source
              </h3>
              <div className="flex-1 relative z-10">
                  <ResponsiveContainer width="100%" height="100%">
                      <PieChart>
                          <Pie
                              data={generateLeadSourceData()}
                              cx="50%"
                              cy="50%"
                              innerRadius={60}
                              outerRadius={80}
                              paddingAngle={5}
                              dataKey="value"
                              stroke="none"
                          >
                              {generateLeadSourceData().map((entry, index) => (
                                  <Cell key={`cell-${index}`} fill={entry.color} />
                              ))}
                          </Pie>
                          <Tooltip contentStyle={{ backgroundColor: '#fff', borderColor: '#e2e8f0', borderRadius: '4px', color: '#0f172a', fontWeight: 'bold' }} />
                          <Legend verticalAlign="bottom" height={36} iconSize={8} iconType="circle" wrapperStyle={{fontSize: '9px', fontWeight: '700', color: '#475569'}} />
                      </PieChart>
                  </ResponsiveContainer>
                  <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-[60%] text-center pointer-events-none">
                      <div className={`text-3xl font-black ${silverTextMain}`}>{totalLeads}</div>
                      <div className={`text-[9px] ${silverTextSub} uppercase tracking-widest font-bold`}>Leads</div>
                  </div>
              </div>
          </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className={pureSilverBlockClass}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                   <Target className="w-4 h-4 text-slate-600"/> Top Performers (Infobusiness)
              </h3>
              <div className="space-y-4 relative z-10">
                  {topProducts.length > 0 ? topProducts.map((prod, idx) => (
                      <div key={prod.id} className="flex items-center justify-between group p-3 bg-white/40 border border-white/50 rounded-sm hover:bg-white/60 transition-colors shadow-sm">
                          <div className="flex items-center gap-4">
                              <div className="w-8 h-8 rounded-full bg-[#0F172A] text-white flex items-center justify-center text-[10px] font-bold shadow-md">
                                  #{idx + 1}
                              </div>
                              <div>
                                  <div className={`text-xs font-bold ${silverTextMain}`}>{prod.title}</div>
                                  <div className={`text-[9px] font-bold ${silverTextSub}`}>{prod.sales} Vendite</div>
                              </div>
                          </div>
                          <div className="text-right">
                              <div className={`text-xs font-bold ${silverTextMain}`}>€{(prod.sales * prod.price).toLocaleString()}</div>
                              <div className="w-24 h-1.5 bg-slate-200 rounded-full mt-1 overflow-hidden">
                                  <div className="h-full bg-[#0F172A]" style={{width: `${Math.min(100, (prod.sales * 10))}%`}}></div>
                              </div>
                          </div>
                      </div>
                  )) : (
                      <p className={`text-xs ${silverTextSub} italic text-center py-8 font-bold`}>Nessun dato di vendita.</p>
                  )}
              </div>
          </div>

          <div className={pureSilverBlockClass}>
              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
              <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 flex items-center gap-2 relative z-10 ${silverTextMain}`}>
                   <Activity className="w-4 h-4 text-slate-600"/> Efficienza Operativa
              </h3>
              <div className="h-64 relative z-10">
                   <ResponsiveContainer width="100%" height="100%">
                       <BarChart data={[
                           { name: 'Lun', tasks: 12 }, { name: 'Mar', tasks: 19 }, { name: 'Mer', tasks: 15 },
                           { name: 'Gio', tasks: 22 }, { name: 'Ven', tasks: 18 }, { name: 'Sab', tasks: 8 }, { name: 'Dom', tasks: 4 },
                       ]}>
                           <CartesianGrid strokeDasharray="3 3" stroke="#94a3b8" vertical={false} opacity={0.5} />
                           <XAxis dataKey="name" stroke="#64748B" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} axisLine={false} tickLine={false} />
                           <Tooltip cursor={{fill: 'rgba(0,0,0,0.05)'}} contentStyle={{ backgroundColor: '#fff', borderColor: '#e2e8f0', borderRadius: '4px', color: '#0f172a', fontWeight: 'bold' }} />
                           <Bar dataKey="tasks" fill="#475569" radius={[2, 2, 0, 0]} barSize={30} />
                       </BarChart>
                   </ResponsiveContainer>
              </div>
          </div>
      </div>
    </div>
  );
};

// Subcomponent for KPI Cards - SILVER
const KPICard = ({ title, value, change, trend, icon: Icon }: { title: string, value: string, change: string, trend: 'UP' | 'DOWN', icon: any }) => (
    <div className="bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8] border-t border-l border-white/90 border-b border-r border-slate-500/60 rounded-sm p-6 shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5),inset_0_1px_0_rgba(255,255,255,0.8)] relative overflow-hidden group hover:-translate-y-1 transition-transform duration-300">
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
        <div className="absolute top-[-50%] right-[-50%] w-[200%] h-[200%] bg-gradient-to-b from-white/40 via-transparent to-transparent rotate-45 pointer-events-none"></div>

        <div className="flex justify-between items-start mb-4 relative z-10">
            <span className="text-[10px] font-bold text-slate-600 uppercase tracking-widest">{title}</span>
            <div className="p-2 bg-gradient-to-br from-slate-200 to-slate-300 border border-white shadow-inner text-slate-800 rounded-full">
                <Icon className="w-4 h-4"/>
            </div>
        </div>
        <div className="flex items-end gap-3 mb-2 relative z-10">
            <span className="text-3xl font-black text-slate-900 tracking-tight drop-shadow-[0_1px_0_rgba(255,255,255,0.5)]">{value}</span>
        </div>
        <div className="relative z-10">
            <span className={`inline-flex items-center gap-1 text-[9px] font-bold uppercase tracking-wider px-2 py-1 rounded-sm border shadow-sm ${trend === 'UP' ? 'bg-emerald-100 text-emerald-800 border-emerald-200' : 'bg-rose-100 text-rose-800 border-rose-200'}`}>
                {trend === 'UP' ? <ArrowUpRight className="w-3 h-3" /> : <ArrowDownRight className="w-3 h-3" />}
                {change} vs mese scorso
            </span>
        </div>
    </div>
);
