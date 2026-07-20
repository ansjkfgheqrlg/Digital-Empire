
import React, { useState } from 'react';
import { User, Task, TaskStatus } from '../types';
import { MOCK_USERS } from '../constants';
import { Shield, Briefcase, Plus, Activity, Mail, Clock, Zap, CheckCircle2, ChevronRight, User as UserIcon } from 'lucide-react';
import { Button } from './ui/Button';

interface TeamManagementProps {
  currentUser: User;
  tasks: Task[];
}

export const TeamManagement: React.FC<TeamManagementProps> = ({ currentUser, tasks }) => {
  const [selectedUserId, setSelectedUserId] = useState<string | null>(null);
  const isAdmin = currentUser.role === 'ADMIN';
  const getInitials = (name: string) => name.substring(0, 2).toUpperCase();

  // 1. FILTER: Exclude Clients from Team View
  const teamMembers = MOCK_USERS.filter(u => u.role !== 'CLIENT');

  // Helper Metrics
  const getUserStats = (userId: string) => {
      const userTasks = tasks.filter(t => t.assignee === userId);
      const total = userTasks.length;
      const completed = userTasks.filter(t => t.status === TaskStatus.DONE).length;
      const active = userTasks.filter(t => t.status === TaskStatus.IN_PROGRESS).length;
      const completionRate = total > 0 ? Math.round((completed / total) * 100) : 0;
      
      // Calculate Workload Score (0-100) based on active tasks
      const workloadScore = Math.min(100, active * 15); 

      return { total, completed, active, completionRate, workloadScore, userTasks };
  };

  const selectedUser = selectedUserId ? teamMembers.find(u => u.id === selectedUserId) : null;
  const selectedStats = selectedUserId ? getUserStats(selectedUserId) : null;

  // --- METALLIC THEME SYSTEM ---
  const MetallicTexture = () => (
      <>
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] pointer-events-none mix-blend-overlay"></div>
        <div className="absolute top-0 right-0 w-40 h-40 bg-white opacity-[0.2] rounded-full blur-3xl -translate-y-10 translate-x-10 group-hover:opacity-[0.3] transition-opacity pointer-events-none"></div>
        <div className="absolute bottom-0 left-0 w-full h-1/3 bg-gradient-to-t from-black/5 to-transparent pointer-events-none"></div>
      </>
  );

  const getMemberTheme = (name: string) => {
      if (name.includes('Maximilian')) return 'GOLD';
      if (name.includes('Leonardo')) return 'PURPLE';
      if (name.includes('Gael')) return 'GREEN';
      if (name.includes('Neri')) return 'ORANGE';
      return 'SILVER';
  };

  const THEMES: Record<string, any> = {
      GOLD: {
          block: "bg-gradient-to-br from-[#FFFBEB] via-[#FCD34D] to-[#B45309] border-yellow-200/50",
          textMain: "text-[#451a03]", // Deep Bronze
          textSub: "text-[#78350f]",
          iconBg: "bg-[#78350f]/10 border border-[#78350f]/20 text-[#78350f]",
          badge: "bg-[#FEF3C7] text-[#92400e] border-[#FDE68A]",
          barColor: "bg-[#B45309]",
          button: "border border-[#78350f]/20 text-[#78350f] hover:bg-[#78350f] hover:text-white"
      },
      PURPLE: {
          block: "bg-gradient-to-br from-[#F3E8FF] via-[#D8B4FE] to-[#7E22CE] border-purple-200/50",
          textMain: "text-[#3B0764]", // Deep Indigo
          textSub: "text-[#581C87]",
          iconBg: "bg-[#581C87]/10 border border-[#581C87]/20 text-[#581C87]",
          badge: "bg-[#F3E8FF] text-[#6b21a8] border-[#E9D5FF]",
          barColor: "bg-[#7E22CE]",
          button: "border border-[#581C87]/20 text-[#581C87] hover:bg-[#581C87] hover:text-[#F3E8FF]"
      },
      GREEN: {
          block: "bg-gradient-to-br from-[#ECFDF5] via-[#6EE7B7] to-[#047857] border-emerald-200/50",
          textMain: "text-[#022c22]", // Deep Emerald
          textSub: "text-[#065f46]",
          iconBg: "bg-[#065f46]/10 border border-[#065f46]/20 text-[#065f46]",
          badge: "bg-[#D1FAE5] text-[#047857] border-[#A7F3D0]",
          barColor: "bg-[#047857]",
          button: "border border-[#065f46]/20 text-[#065f46] hover:bg-[#065f46] hover:text-[#ECFDF5]"
      },
      ORANGE: {
          block: "bg-gradient-to-br from-[#FFF7ED] via-[#FDBA74] to-[#C2410C] border-orange-200/50",
          textMain: "text-[#431407]", // Deep Rust
          textSub: "text-[#9a3412]",
          iconBg: "bg-[#9a3412]/10 border border-[#9a3412]/20 text-[#9a3412]",
          badge: "bg-[#FFEDD5] text-[#c2410c] border-[#FED7AA]",
          barColor: "bg-[#C2410C]",
          button: "border border-[#9a3412]/20 text-[#9a3412] hover:bg-[#9a3412] hover:text-[#FFF7ED]"
      },
      SILVER: {
          block: "bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B] border-white/50",
          textMain: "text-[#0f172a]",
          textSub: "text-[#334155]",
          iconBg: "bg-[#334155]/10 border border-[#334155]/20 text-[#334155]",
          badge: "bg-[#F1F5F9] text-[#475569] border-[#E2E8F0]",
          barColor: "bg-[#475569]",
          button: "border border-[#334155]/20 text-[#334155] hover:bg-[#334155] hover:text-white"
      }
  };

  // Get theme for the detailed view
  const activeThemeKey = selectedUser ? getMemberTheme(selectedUser.name) : 'SILVER';
  const activeTheme = THEMES[activeThemeKey];

  return (
    <div className="h-full flex flex-col animate-in fade-in duration-500">
      <div className="flex justify-between items-center border-b border-white/5 pb-6 shrink-0">
        <div>
            <h1 className="text-3xl font-bold text-silver-gradient mb-2 tracking-tight">Team Operations Center</h1>
            <p className="text-platinum-500 text-sm">Gestione organico, assegnazione incarichi e monitoraggio performance.</p>
        </div>
        {isAdmin && <Button icon={<Plus className="w-4 h-4" />}>Nuovo Agente</Button>}
      </div>

      <div className="flex flex-1 gap-8 mt-8 overflow-hidden min-h-0">
          
          {/* LEFT: Team List Grid */}
          <div className={`flex-1 overflow-y-auto custom-scrollbar pr-4 grid grid-cols-1 lg:grid-cols-2 gap-6 content-start pb-10 ${selectedUserId ? 'hidden xl:grid xl:w-1/2' : ''}`}>
            {teamMembers.map((user) => {
              const stats = getUserStats(user.id);
              const isSelected = selectedUserId === user.id;
              const themeKey = getMemberTheme(user.name);
              const theme = THEMES[themeKey];

              return (
                <div 
                    key={user.id} 
                    onClick={() => setSelectedUserId(user.id)}
                    className={`
                        ${theme.block} border-t border-l border-b border-r rounded-sm overflow-hidden relative group cursor-pointer transition-all duration-300 flex flex-col min-h-[260px] shadow-xl hover:-translate-y-1 hover:shadow-2xl
                        ${isSelected ? 'ring-2 ring-white/50 scale-[1.02]' : ''}
                    `}
                >
                    <MetallicTexture />
                    
                    <div className="p-6 flex flex-col flex-1 justify-between relative z-10">
                        
                        {/* Header Part */}
                        <div className="flex justify-between items-start mb-6">
                            <div className="flex items-center gap-4">
                                <div className={`w-14 h-14 rounded-sm flex items-center justify-center text-lg font-black shadow-inner ${theme.iconBg}`}>
                                    {getInitials(user.name)}
                                </div>
                                <div className="min-w-0">
                                    <h3 className={`text-xl font-black truncate leading-tight ${theme.textMain}`}>{user.name}</h3>
                                    <p className={`text-[10px] uppercase tracking-widest truncate max-w-[150px] font-bold ${theme.textSub}`}>{user.title}</p>
                                </div>
                            </div>
                            {user.role === 'ADMIN' && (
                                <span className={`px-2 py-1 text-[8px] font-bold uppercase tracking-wider flex items-center gap-1 rounded-sm border shadow-sm ${theme.badge}`}>
                                    <Shield className="w-3 h-3" /> Admin
                                </span>
                            )}
                        </div>

                        {/* Stats Part */}
                        <div className={`grid grid-cols-3 gap-4 py-5 border-t border-b border-black/5 mb-4 rounded-sm px-2 bg-white/20 shadow-sm`}>
                            <div className="text-center">
                                <p className={`text-[9px] uppercase tracking-wider mb-1 font-bold opacity-70 ${theme.textSub}`}>Tasks</p>
                                <p className={`text-2xl font-black leading-none ${theme.textMain}`}>{stats.total}</p>
                            </div>
                            <div className="text-center border-l border-black/5">
                                <p className={`text-[9px] uppercase tracking-wider mb-1 font-bold opacity-70 ${theme.textSub}`}>Rate</p>
                                <p className={`text-2xl font-black leading-none ${theme.textMain}`}>{stats.completionRate}%</p>
                            </div>
                            <div className="text-center border-l border-black/5">
                                <p className={`text-[9px] uppercase tracking-wider mb-1 font-bold opacity-70 ${theme.textSub}`}>Load</p>
                                <p className={`text-2xl font-black leading-none ${theme.textMain}`}>{stats.workloadScore}%</p>
                            </div>
                        </div>

                        {/* Tags Footer */}
                        <div className="flex flex-wrap gap-2 h-6 overflow-hidden">
                            {user.tags.slice(0,3).map((tag, i) => (
                                <span key={i} className={`px-2 py-0.5 rounded-sm text-[8px] font-bold border truncate max-w-[100px] shadow-sm bg-white/40 border-white/50 ${theme.textSub}`}>
                                    {tag}
                                </span>
                            ))}
                        </div>
                    </div>
                    
                    {/* Active State Indicator */}
                    {isSelected && (
                        <div className={`absolute right-4 top-1/2 -translate-y-1/2 animate-pulse pointer-events-none ${theme.textMain}`}>
                            <ChevronRight className="w-8 h-8" />
                        </div>
                    )}
                </div>
              );
            })}
          </div>

          {/* RIGHT: Detailed Dossier (Metallic Adaptive) */}
          {selectedUser && selectedStats && (
              <div className={`w-full xl:w-1/2 ${activeTheme.block} border-t border-l border-b border-r rounded-sm flex flex-col overflow-hidden animate-in slide-in-from-right-4 duration-300 shadow-2xl h-full`}>
                  <MetallicTexture />
                  
                  {/* Header Dossier */}
                  <div className="p-8 border-b border-black/10 bg-white/10 relative overflow-hidden shrink-0 z-10 backdrop-blur-sm">
                      <div className="flex justify-between items-start relative z-10">
                          <div>
                              <h2 className={`text-4xl font-black mb-1 ${activeTheme.textMain}`}>{selectedUser.name}</h2>
                              <div className={`flex items-center gap-2 text-sm font-bold uppercase tracking-wider ${activeTheme.textSub}`}>
                                  <Briefcase className="w-4 h-4"/> {selectedUser.title}
                              </div>
                          </div>
                          <div className="flex gap-2">
                              <button className={`px-4 py-2 rounded-sm text-[10px] font-bold uppercase tracking-widest shadow-sm bg-white/50 ${activeTheme.button}`}>
                                  Contatta
                              </button>
                              <button className={`px-4 py-2 rounded-sm text-[10px] font-bold uppercase tracking-widest shadow-lg text-white ${activeTheme.barColor}`}>
                                  Assegna Task
                              </button>
                          </div>
                      </div>

                      <div className="grid grid-cols-2 gap-4 mt-8">
                          <div className="bg-white/30 border border-white/40 p-4 rounded-sm shadow-sm">
                              <h4 className={`text-[10px] uppercase tracking-widest mb-2 flex items-center gap-2 font-bold ${activeTheme.textSub}`}><Zap className="w-3 h-3"/> Workload</h4>
                              <div className="w-full bg-black/10 rounded-full h-2 mb-2">
                                  <div 
                                    className={`h-2 rounded-full ${activeTheme.barColor}`} 
                                    style={{width: `${selectedStats.workloadScore}%`}}
                                  ></div>
                              </div>
                              <p className={`text-xs font-bold text-right ${activeTheme.textMain}`}>{selectedStats.active} task attivi</p>
                          </div>
                          <div className="bg-white/30 border border-white/40 p-4 rounded-sm shadow-sm">
                              <h4 className={`text-[10px] uppercase tracking-widest mb-2 flex items-center gap-2 font-bold ${activeTheme.textSub}`}><Activity className="w-3 h-3"/> Performance</h4>
                              <div className="flex items-end gap-2">
                                  <span className={`text-3xl font-black ${activeTheme.textMain}`}>{selectedStats.completionRate}%</span>
                                  <span className={`text-xs font-bold mb-1 opacity-70 ${activeTheme.textSub}`}>su {selectedStats.total} totali</span>
                              </div>
                          </div>
                      </div>
                  </div>

                  {/* Task List */}
                  <div className="flex-1 overflow-y-auto custom-scrollbar p-6 bg-white/5 relative z-10">
                      <h3 className={`text-xs font-black uppercase tracking-widest mb-6 border-b border-black/10 pb-2 ${activeTheme.textMain}`}>Missioni Assegnate</h3>
                      
                      {selectedStats.userTasks.length > 0 ? (
                          <div className="space-y-3">
                              {selectedStats.userTasks.map(task => (
                                  <div key={task.id} className="p-4 bg-white/40 border border-white/50 rounded-sm flex justify-between items-center group hover:bg-white/60 transition-colors shadow-sm">
                                      <div className="flex items-center gap-4">
                                          <div className={`w-3 h-3 rounded-sm border border-black/10 ${task.status === 'DONE' ? 'bg-green-500' : task.status === 'IN_PROGRESS' ? 'bg-blue-500' : 'bg-slate-400'}`}></div>
                                          <div>
                                              <h4 className={`text-sm font-bold ${task.status === 'DONE' ? 'line-through opacity-50' : ''} ${activeTheme.textMain}`}>{task.title}</h4>
                                              <p className={`text-[10px] font-mono flex items-center gap-1 font-bold opacity-70 ${activeTheme.textSub}`}><Clock className="w-3 h-3"/> Scadenza: {task.dueDate}</p>
                                          </div>
                                      </div>
                                      <span className={`text-[9px] font-bold px-2 py-1 rounded-sm border uppercase ${task.priority === 'HIGH' ? 'bg-red-100 text-red-700 border-red-200' : 'bg-white text-slate-600 border-slate-200'}`}>
                                          {task.priority}
                                      </span>
                                  </div>
                              ))}
                          </div>
                      ) : (
                          <div className="text-center py-12 border border-dashed border-black/10 rounded-sm">
                              <CheckCircle2 className={`w-12 h-12 mx-auto mb-4 opacity-50 ${activeTheme.textMain}`}/>
                              <p className={`text-xs font-bold ${activeTheme.textSub}`}>Nessuna task assegnata a questo agente.</p>
                          </div>
                      )}
                  </div>
              </div>
          )}
          
          {!selectedUser && (
              <div className="hidden xl:flex w-1/2 items-center justify-center bg-[#050505] border border-white/5 rounded-sm opacity-50">
                  <div className="text-center">
                      <div className="w-20 h-20 bg-white/5 rounded-full flex items-center justify-center mx-auto mb-6">
                          <UserIcon className="w-10 h-10 text-platinum-700" />
                      </div>
                      <p className="text-sm text-platinum-500 uppercase tracking-widest">Seleziona un membro del team<br/>per visualizzare il dossier operativo.</p>
                  </div>
              </div>
          )}
      </div>
    </div>
  );
};
