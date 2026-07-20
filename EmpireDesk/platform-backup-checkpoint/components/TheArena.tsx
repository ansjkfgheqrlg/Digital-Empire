
import React from 'react';
import { User, Task, Lead, Badge, Quest } from '../types';
import { MOCK_BADGES, DAILY_QUESTS, MOCK_USERS } from '../constants';
import { 
  Trophy, Star, Award, Zap, Target, Shield, Crown, TrendingUp, 
  Flame, Lock, CheckCircle2, Hexagon
} from 'lucide-react';
import { AreaChart, Area, ResponsiveContainer, XAxis, Tooltip } from 'recharts';

interface TheArenaProps {
  currentUser: User;
  tasks: Task[];
  leads: Lead[];
}

export const TheArena: React.FC<TheArenaProps> = ({ currentUser, tasks, leads }) => {
  
  // Calculate dynamic XP based on activity (Mock logic)
  const completedTasks = tasks.filter(t => t.status === 'DONE' && t.assignee === currentUser.id).length;
  const closedDeals = leads.filter(l => l.stage === 'CLOSED_WON').length; // Assuming user participated
  
  const calculatedXP = (currentUser.xp || 0) + (completedTasks * 100) + (closedDeals * 1000);
  const currentLevel = Math.floor(Math.sqrt(calculatedXP / 100)); // Simple RPG formula
  const nextLevelXP = Math.pow(currentLevel + 1, 2) * 100;
  const currentLevelBaseXP = Math.pow(currentLevel, 2) * 100;
  const progressPercent = ((calculatedXP - currentLevelBaseXP) / (nextLevelXP - currentLevelBaseXP)) * 100;

  const getRankName = (level: number) => {
      if (level < 10) return { name: 'Bronze Agent', color: 'text-orange-400' };
      if (level < 20) return { name: 'Silver Executive', color: 'text-slate-300' };
      if (level < 30) return { name: 'Gold Partner', color: 'text-yellow-400' };
      if (level < 40) return { name: 'Platinum Leader', color: 'text-cyan-200' };
      if (level < 50) return { name: 'Diamond Elite', color: 'text-diamond-400' };
      return { name: 'Aureus Legend', color: 'text-amber-500' };
  };

  const rank = getRankName(currentLevel);

  // Mock Performance Data
  const performanceData = [
      { day: 'Lun', xp: 450 }, { day: 'Mar', xp: 800 }, { day: 'Mer', xp: 300 }, 
      { day: 'Gio', xp: 1200 }, { day: 'Ven', xp: 950 }, { day: 'Sab', xp: 200 }, { day: 'Dom', xp: 0 }
  ];

  const getIcon = (name: string) => {
      switch(name) {
          case 'Zap': return <Zap className="w-5 h-5"/>;
          case 'Layout': return <Hexagon className="w-5 h-5"/>;
          case 'Diamond': return <Crown className="w-5 h-5"/>;
          default: return <Award className="w-5 h-5"/>;
      }
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-500 pb-10">
        
        {/* Hero Section: The Player Card */}
        <div className="relative bg-[#0A0A0A] border border-white/10 rounded-sm p-8 overflow-hidden shadow-2xl">
            {/* Ambient Background */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-diamond-500/10 rounded-full blur-[120px] pointer-events-none"></div>
            <div className="absolute bottom-0 left-0 w-[300px] h-[300px] bg-purple-500/10 rounded-full blur-[100px] pointer-events-none"></div>

            <div className="relative z-10 flex justify-between items-center">
                <div className="flex items-center gap-8">
                    {/* Avatar / Level Hexagon */}
                    <div className="relative w-32 h-32 flex items-center justify-center">
                        <svg viewBox="0 0 100 100" className="absolute inset-0 w-full h-full text-white/10 drop-shadow-xl" fill="currentColor">
                            <polygon points="50 1 95 25 95 75 50 99 5 75 5 25" />
                        </svg>
                        <div className="absolute inset-2 bg-gradient-to-br from-[#1a1a1a] to-black clip-path-hexagon flex flex-col items-center justify-center">
                            <span className="text-4xl font-bold text-white">{currentLevel}</span>
                            <span className="text-[9px] uppercase tracking-widest text-platinum-500">Level</span>
                        </div>
                        {/* Progress Border (Simulated with distinct strokes/gradients in real app, here simple ring) */}
                        <div className="absolute inset-0 border-4 border-diamond-500/30 rounded-full scale-90 opacity-0"></div> 
                    </div>

                    <div>
                        <div className="flex items-center gap-3 mb-1">
                            <h1 className="text-4xl font-bold text-white tracking-tight">{currentUser.name}</h1>
                            <span className={`px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-bold uppercase tracking-widest ${rank.color}`}>
                                {rank.name}
                            </span>
                        </div>
                        <p className="text-platinum-400 text-sm mb-6 flex items-center gap-2">
                            <Shield className="w-4 h-4"/> {currentUser.title}
                        </p>
                        
                        {/* XP Bar */}
                        <div className="w-[400px]">
                            <div className="flex justify-between text-[10px] font-bold text-platinum-500 uppercase tracking-widest mb-2">
                                <span>{calculatedXP.toLocaleString()} XP</span>
                                <span>{nextLevelXP.toLocaleString()} XP</span>
                            </div>
                            <div className="h-3 w-full bg-white/10 rounded-full overflow-hidden relative">
                                <div className="absolute inset-0 bg-[linear-gradient(45deg,transparent_25%,rgba(255,255,255,0.1)_50%,transparent_75%)] bg-[length:20px_20px] animate-pulse"></div>
                                <div 
                                    className="h-full bg-gradient-to-r from-diamond-600 to-diamond-400 shadow-[0_0_15px_#22d3ee]" 
                                    style={{width: `${progressPercent}%`}}
                                ></div>
                            </div>
                            <p className="text-[10px] text-platinum-600 mt-2 text-right">
                                {Math.floor(nextLevelXP - calculatedXP)} XP al prossimo livello
                            </p>
                        </div>
                    </div>
                </div>

                {/* Quick Stats */}
                <div className="flex gap-6">
                    <div className="text-center p-4 bg-white/5 rounded-sm border border-white/5 min-w-[100px]">
                        <Trophy className="w-6 h-6 text-yellow-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">{MOCK_BADGES.filter(b => b.earnedDate).length}</div>
                        <div className="text-[9px] uppercase tracking-widest text-platinum-500">Badges</div>
                    </div>
                    <div className="text-center p-4 bg-white/5 rounded-sm border border-white/5 min-w-[100px]">
                        <Flame className="w-6 h-6 text-orange-500 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">12</div>
                        <div className="text-[9px] uppercase tracking-widest text-platinum-500">Day Streak</div>
                    </div>
                </div>
            </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            
            {/* Left Column: Quests & XP Trend */}
            <div className="lg:col-span-2 space-y-8">
                
                {/* Active Quests */}
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-6">
                    <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-6 flex items-center gap-2">
                        <Target className="w-4 h-4 text-red-400"/> Daily Quests
                    </h3>
                    <div className="grid grid-cols-1 gap-4">
                        {DAILY_QUESTS.map(quest => (
                            <div key={quest.id} className="relative overflow-hidden bg-[#0F0F0F] border border-white/5 p-4 rounded-sm flex items-center justify-between group hover:border-diamond-500/20 transition-all">
                                {quest.isCompleted && (
                                    <div className="absolute inset-0 bg-green-900/10 pointer-events-none"></div>
                                )}
                                <div className="relative z-10 flex-1">
                                    <div className="flex items-center gap-3 mb-1">
                                        <h4 className={`text-sm font-bold ${quest.isCompleted ? 'text-green-400' : 'text-white'}`}>{quest.title}</h4>
                                        {quest.isCompleted && <CheckCircle2 className="w-4 h-4 text-green-400" />}
                                    </div>
                                    <p className="text-xs text-platinum-500 mb-3">{quest.description}</p>
                                    
                                    <div className="w-full max-w-md h-1.5 bg-white/10 rounded-full overflow-hidden">
                                        <div 
                                            className={`h-full ${quest.isCompleted ? 'bg-green-500' : 'bg-diamond-500'}`} 
                                            style={{width: `${(quest.progress / quest.total) * 100}%`}}
                                        ></div>
                                    </div>
                                    <div className="text-[9px] text-platinum-600 mt-1 font-mono">
                                        {quest.progress} / {quest.total}
                                    </div>
                                </div>
                                <div className="text-right relative z-10">
                                    <div className="text-xs font-bold text-yellow-400 flex items-center justify-end gap-1">
                                        +{quest.rewardXp} XP
                                    </div>
                                    <div className="text-[9px] uppercase tracking-widest text-platinum-600">Reward</div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>

                {/* XP History Chart */}
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-6 h-64 flex flex-col">
                    <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-4 flex items-center gap-2">
                        <TrendingUp className="w-4 h-4 text-emerald-400"/> XP Performance (7 Giorni)
                    </h3>
                    <div className="flex-1 w-full min-h-0">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={performanceData}>
                                <defs>
                                    <linearGradient id="colorXp" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="day" stroke="#52606D" tick={{fill: '#9AA5B1', fontSize: 10}} axisLine={false} tickLine={false} />
                                <Tooltip 
                                    cursor={{stroke: 'rgba(255,255,255,0.1)'}} 
                                    contentStyle={{ backgroundColor: '#050505', borderColor: '#333', borderRadius: '2px', color: '#fff' }} 
                                />
                                <Area type="monotone" dataKey="xp" stroke="#8b5cf6" strokeWidth={2} fillOpacity={1} fill="url(#colorXp)" />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            </div>

            {/* Right Column: Badges & Leaderboard */}
            <div className="space-y-8">
                
                {/* Hall of Fame */}
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-6">
                    <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-6 flex items-center gap-2">
                        <Crown className="w-4 h-4 text-yellow-500"/> Hall of Fame
                    </h3>
                    <div className="space-y-4">
                        {MOCK_USERS.sort((a,b) => (b.xp || 0) - (a.xp || 0)).slice(0, 5).map((user, idx) => (
                            <div key={user.id} className="flex items-center gap-4 group">
                                <div className={`
                                    w-8 h-8 rounded-sm flex items-center justify-center font-bold text-black text-xs
                                    ${idx === 0 ? 'bg-yellow-400 shadow-[0_0_15px_rgba(250,204,21,0.4)]' : 
                                      idx === 1 ? 'bg-slate-300' : 
                                      idx === 2 ? 'bg-orange-700' : 'bg-[#111] text-white border border-white/10'}
                                `}>
                                    {idx + 1}
                                </div>
                                <div className="flex-1">
                                    <div className="flex justify-between items-center mb-1">
                                        <span className={`text-sm font-bold ${user.id === currentUser.id ? 'text-diamond-400' : 'text-platinum-200'}`}>{user.name}</span>
                                        <span className="text-xs font-mono text-platinum-500">{user.xp?.toLocaleString()} XP</span>
                                    </div>
                                    <div className="w-full bg-white/5 h-1 rounded-full overflow-hidden">
                                        <div className="bg-white/20 h-full" style={{width: `${Math.min(100, ((user.xp || 0) / 20000) * 100)}%`}}></div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Badge Collection */}
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-6">
                    <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-6 flex items-center gap-2">
                        <Award className="w-4 h-4 text-purple-400"/> Badge Collection
                    </h3>
                    <div className="grid grid-cols-4 gap-2">
                        {MOCK_BADGES.map(badge => (
                            <div key={badge.id} className="group relative">
                                <div className={`
                                    aspect-square rounded-sm border flex items-center justify-center transition-all duration-300
                                    ${badge.earnedDate 
                                        ? `bg-gradient-to-br ${badge.rarity === 'LEGENDARY' ? 'from-yellow-900/40 to-yellow-600/10 border-yellow-500/50 text-yellow-400' : 
                                           badge.rarity === 'EPIC' ? 'from-purple-900/40 to-purple-600/10 border-purple-500/50 text-purple-400' : 
                                           'from-white/10 to-white/5 border-white/20 text-white'}` 
                                        : 'bg-[#050505] border-white/5 text-platinum-800 opacity-50 grayscale'}
                                `}>
                                    {getIcon(badge.icon)}
                                </div>
                                
                                {/* Tooltip */}
                                <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-40 bg-black border border-white/20 p-2 rounded-sm text-center opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
                                    <div className={`text-[10px] font-bold uppercase mb-1 ${badge.earnedDate ? 'text-white' : 'text-platinum-600'}`}>{badge.title}</div>
                                    <div className="text-[9px] text-platinum-500 leading-tight">{badge.description}</div>
                                    {badge.earnedDate && <div className="text-[8px] text-emerald-500 mt-1">Ottenuto: {badge.earnedDate}</div>}
                                </div>
                            </div>
                        ))}
                        {/* Empty Slots Fillers */}
                        {Array.from({length: 4}).map((_, i) => (
                            <div key={`empty-${i}`} className="aspect-square rounded-sm border border-white/5 bg-[#050505] flex items-center justify-center">
                                <Lock className="w-4 h-4 text-platinum-800" />
                            </div>
                        ))}
                    </div>
                </div>

            </div>
        </div>
    </div>
  );
};
