
import React, { useState, useEffect } from 'react';
import { Lead, Task } from '../types';
import { MOCK_USERS } from '../constants';
import { ArrowLeft, TrendingUp, Users, Activity, Globe, DollarSign, Target, Zap } from 'lucide-react';
import { AreaChart, Area, ResponsiveContainer, XAxis } from 'recharts';

interface WarRoomProps {
  leads: Lead[];
  tasks: Task[];
  onNavigate: (path: string) => void;
}

export const WarRoom: React.FC<WarRoomProps> = ({ leads, tasks, onNavigate }) => {
  const [currentTime, setCurrentTime] = useState(new Date());
  
  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const activeLeads = leads.filter(l => l.stage !== 'CLOSED_WON' && l.stage !== 'CLOSED_LOST');
  const totalRevenue = leads.filter(l => l.stage === 'CLOSED_WON').reduce((acc, l) => acc + l.value, 0);
  const urgentTasks = tasks.filter(t => t.priority === 'HIGH' && t.status !== 'DONE').length;

  const topClosers = MOCK_USERS.map(u => ({
      name: u.name,
      value: Math.floor(Math.random() * 50000) + 10000, // Mock for visual
      deals: Math.floor(Math.random() * 10) + 1
  })).sort((a,b) => b.value - a.value);

  return (
    <div className="fixed inset-0 bg-[#020202] z-[9999] overflow-hidden text-white font-mono flex flex-col">
       
       {/* Background Grid & Effects */}
       <div className="absolute inset-0 bg-[linear-gradient(rgba(0,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(0,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>
       <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-[#020202]/90 pointer-events-none"></div>

       {/* Top Bar */}
       <div className="flex justify-between items-center p-8 border-b border-diamond-500/20 bg-[#050505]/80 backdrop-blur relative z-10">
           <div className="flex items-center gap-6">
               <button onClick={() => onNavigate('/')} className="p-2 border border-white/10 rounded hover:bg-white/10 text-platinum-500 hover:text-white transition-colors">
                   <ArrowLeft className="w-5 h-5"/>
               </button>
               <div>
                   <h1 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-white to-platinum-400 tracking-[0.2em] uppercase">War Room</h1>
                   <div className="flex items-center gap-2 text-xs text-diamond-400 animate-pulse">
                       <div className="w-2 h-2 bg-diamond-500 rounded-full"></div>
                       LIVE OPERATIONS • AUREUS SYSTEM
                   </div>
               </div>
           </div>
           <div className="text-right">
               <div className="text-4xl font-bold text-white tracking-widest">{currentTime.toLocaleTimeString([], {hour12: false})}</div>
               <div className="text-sm text-platinum-500 uppercase tracking-[0.3em]">{currentTime.toLocaleDateString()}</div>
           </div>
       </div>

       {/* Main Grid */}
       <div className="flex-1 p-8 grid grid-cols-4 gap-8 relative z-10">
           
           {/* Column 1: Live Stats */}
           <div className="col-span-1 space-y-6">
               <div className="bg-[#08090A] border border-diamond-500/30 p-6 rounded-sm shadow-[0_0_30px_rgba(34,211,238,0.1)] relative overflow-hidden">
                   <div className="absolute top-0 right-0 p-4 opacity-20"><DollarSign className="w-16 h-16 text-diamond-400"/></div>
                   <h3 className="text-diamond-500 text-xs uppercase tracking-[0.3em] mb-2">Total Revenue</h3>
                   <div className="text-5xl font-bold text-white tracking-tighter mb-4">€{totalRevenue.toLocaleString()}</div>
                   <div className="h-1 w-full bg-diamond-950 rounded-full overflow-hidden">
                       <div className="h-full bg-diamond-400 w-[75%] animate-pulse"></div>
                   </div>
               </div>

               <div className="bg-[#08090A] border border-white/10 p-6 rounded-sm flex items-center justify-between">
                   <div>
                       <h3 className="text-platinum-500 text-xs uppercase tracking-[0.3em] mb-1">Active Leads</h3>
                       <div className="text-3xl font-bold text-white">{activeLeads.length}</div>
                   </div>
                   <Activity className="w-8 h-8 text-yellow-400 animate-pulse"/>
               </div>

               <div className="bg-[#08090A] border border-white/10 p-6 rounded-sm flex items-center justify-between">
                   <div>
                       <h3 className="text-platinum-500 text-xs uppercase tracking-[0.3em] mb-1">Urgent Tasks</h3>
                       <div className="text-3xl font-bold text-red-400">{urgentTasks}</div>
                   </div>
                   <Zap className="w-8 h-8 text-red-500"/>
               </div>
           </div>

           {/* Column 2 & 3: Map & Activity Feed */}
           <div className="col-span-2 flex flex-col gap-6">
                <div className="flex-1 bg-[#08090A] border border-white/10 rounded-sm relative overflow-hidden flex flex-col items-center justify-center">
                    {/* Fake Map Visualization */}
                    <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_center,#22D3EE_0%,transparent_60%)]"></div>
                    <Globe className="w-64 h-64 text-platinum-800 animate-pulse" strokeWidth={0.5} />
                    <div className="absolute top-1/2 left-1/2 w-2 h-2 bg-diamond-400 rounded-full shadow-[0_0_20px_#22D3EE] animate-ping"></div>
                    <div className="absolute top-1/3 left-1/3 w-2 h-2 bg-purple-400 rounded-full shadow-[0_0_20px_#A855F7] animate-ping [animation-delay:0.5s]"></div>
                    <div className="absolute bottom-1/3 right-1/4 w-2 h-2 bg-green-400 rounded-full shadow-[0_0_20px_#4ade80] animate-ping [animation-delay:1s]"></div>
                    
                    <div className="absolute bottom-6 left-6 text-xs text-diamond-400 font-mono bg-black/50 px-2 py-1 border border-diamond-500/30">
                        Signal Detected: Milano, IT
                    </div>
                </div>

                <div className="h-48 bg-[#08090A] border border-white/10 rounded-sm p-4 overflow-hidden relative">
                    <h3 className="text-[10px] text-platinum-500 uppercase tracking-widest mb-4 border-b border-white/5 pb-2">Live Activity Feed</h3>
                    <div className="space-y-3 font-mono text-xs">
                        <div className="flex justify-between text-green-400">
                            <span>[SYSTEM] New Lead Acquired: TechSolutions SRL</span>
                            <span>10:42:05</span>
                        </div>
                        <div className="flex justify-between text-platinum-400">
                            <span>[USER] Maximilian updated task "Q3 Strategy"</span>
                            <span>10:40:12</span>
                        </div>
                        <div className="flex justify-between text-blue-400">
                            <span>[AUTO] Email Sequence "Welcome" triggered</span>
                            <span>10:38:55</span>
                        </div>
                        <div className="flex justify-between text-platinum-400">
                            <span>[USER] Gael uploaded "Contract_v2.pdf"</span>
                            <span>10:35:20</span>
                        </div>
                    </div>
                </div>
           </div>

           {/* Column 4: Leaderboard */}
           <div className="col-span-1 bg-[#08090A] border border-white/10 rounded-sm p-6 flex flex-col">
               <h3 className="text-xs text-platinum-300 uppercase tracking-[0.3em] mb-6 flex items-center gap-2">
                   <Target className="w-4 h-4 text-yellow-400"/> Top Closers
               </h3>
               
               <div className="space-y-6">
                   {topClosers.map((user, idx) => (
                       <div key={idx} className="flex items-center gap-4">
                           <div className={`w-8 h-8 flex items-center justify-center font-bold text-black rounded-sm ${idx === 0 ? 'bg-yellow-400' : idx === 1 ? 'bg-platinum-300' : 'bg-orange-700'}`}>
                               {idx + 1}
                           </div>
                           <div className="flex-1">
                               <div className="flex justify-between mb-1">
                                   <span className="text-sm font-bold text-white">{user.name}</span>
                                   <span className="text-xs text-diamond-400">€{user.value.toLocaleString()}</span>
                               </div>
                               <div className="w-full bg-white/10 h-1 rounded-full">
                                   <div className="h-full bg-white" style={{width: `${(user.value / 60000) * 100}%`}}></div>
                               </div>
                           </div>
                       </div>
                   ))}
               </div>

               <div className="mt-auto pt-6 border-t border-white/5">
                   <div className="h-32 w-full">
                       <ResponsiveContainer width="100%" height="100%">
                           <AreaChart data={[{v:10}, {v:30}, {v:20}, {v:50}, {v:40}, {v:70}, {v:60}]}>
                               <defs>
                                   <linearGradient id="colorChart" x1="0" y1="0" x2="0" y2="1">
                                       <stop offset="5%" stopColor="#22D3EE" stopOpacity={0.3}/>
                                       <stop offset="95%" stopColor="#22D3EE" stopOpacity={0}/>
                                   </linearGradient>
                               </defs>
                               <Area type="monotone" dataKey="v" stroke="#22D3EE" strokeWidth={2} fill="url(#colorChart)" />
                           </AreaChart>
                       </ResponsiveContainer>
                   </div>
               </div>
           </div>
       </div>
    </div>
  );
};
