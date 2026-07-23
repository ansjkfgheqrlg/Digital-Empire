
import React, { useState } from 'react';
import { Task, TaskStatus, Department, Subtask } from '../types';
import { MOCK_USERS } from '../constants';
import { 
  Plus, Clock, X, MoreVertical, GripVertical, CheckSquare, MessageSquare, 
  Paperclip, Send, User, Search, Filter, List, Kanban as KanbanIcon, 
  Calendar as CalendarIcon, ChevronLeft, ChevronRight, AlertCircle, Layers,
  LayoutGrid, ArrowUpRight, Zap, Flag, Activity
} from 'lucide-react';
import { Button } from './ui/Button';

interface KanbanBoardProps {
  tasks: Task[];
  onAddTask: (task: Task) => void;
  onUpdateTask: (task: Task) => void;
}

// --- NEW DEFINITIONS FOR TACTICAL BOARD ---

const COLUMNS = [
  { 
    id: TaskStatus.TODO, 
    title: 'Da Assegnare', 
    accent: 'border-l-4 border-slate-500',
    indicator: 'bg-slate-500'
  },
  { 
    id: TaskStatus.IN_PROGRESS, 
    title: 'Operativi', 
    accent: 'border-l-4 border-blue-500',
    indicator: 'bg-blue-500 shadow-[0_0_10px_#3b82f6]'
  },
  { 
    id: TaskStatus.REVIEW, 
    title: 'Controllo Qualità', 
    accent: 'border-l-4 border-purple-500',
    indicator: 'bg-purple-500 shadow-[0_0_10px_#a855f7]'
  },
  { 
    id: TaskStatus.DONE, 
    title: 'Completati', 
    accent: 'border-l-4 border-emerald-500',
    indicator: 'bg-emerald-500 shadow-[0_0_10px_#10b981]'
  },
];

type ViewMode = 'BOARD' | 'LIST' | 'CALENDAR';

export const KanbanBoard: React.FC<KanbanBoardProps> = ({ tasks, onAddTask, onUpdateTask }) => {
  // UI State
  const [viewMode, setViewMode] = useState<ViewMode>('BOARD');
  const [searchQuery, setSearchQuery] = useState('');
  const [filterPriority, setFilterPriority] = useState<string>('ALL');
  const [filterDept, setFilterDept] = useState<string>('ALL');
  
  // Drag & Drop
  const [draggedTaskId, setDraggedTaskId] = useState<string | null>(null);
  
  // Modals
  const [isNewTaskModalOpen, setIsNewTaskModalOpen] = useState(false);
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);
  
  // Calendar State
  const [currentDate, setCurrentDate] = useState(new Date());

  // Form & Detail State
  const [newTask, setNewTask] = useState<Partial<Task>>({
    title: '', department: 'GENERAL', priority: 'MEDIUM', dueDate: '', assignee: ''
  });
  const [commentInput, setCommentInput] = useState('');
  const [subtaskInput, setSubtaskInput] = useState('');

  // --- METRICS ---
  const totalTasks = tasks.length;
  const completedTasks = tasks.filter(t => t.status === 'DONE').length;
  const urgentTasks = tasks.filter(t => t.priority === 'HIGH' && t.status !== 'DONE').length;
  const progressRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

  // --- FILTERS LOGIC ---
  const filteredTasks = tasks.filter(t => {
      const matchSearch = t.title.toLowerCase().includes(searchQuery.toLowerCase());
      const matchPriority = filterPriority === 'ALL' || t.priority === filterPriority;
      const matchDept = filterDept === 'ALL' || t.department === filterDept;
      return matchSearch && matchPriority && matchDept;
  });

  // --- DRAG & DROP ---
  const handleDragStart = (e: React.DragEvent, taskId: string) => {
    setDraggedTaskId(taskId);
    e.dataTransfer.effectAllowed = 'move';
    const el = e.target as HTMLElement;
    setTimeout(() => { el.style.opacity = '0.5'; }, 0);
  };

  const handleDragEnd = (e: React.DragEvent) => {
    const el = e.target as HTMLElement;
    el.style.opacity = '1';
    setDraggedTaskId(null);
  };

  const handleDrop = (e: React.DragEvent, status: TaskStatus) => {
    e.preventDefault();
    if (draggedTaskId) {
      const task = tasks.find(t => t.id === draggedTaskId);
      if (task && task.status !== status) onUpdateTask({ ...task, status });
      setDraggedTaskId(null);
    }
  };

  // --- CRUD ACTIONS ---
  const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      if (!newTask.title) return;
      onAddTask({
          id: `t${Date.now()}`,
          title: newTask.title,
          status: TaskStatus.TODO,
          department: newTask.department as Department,
          priority: newTask.priority as any,
          dueDate: newTask.dueDate || new Date().toISOString().split('T')[0],
          assignee: newTask.assignee,
          subtasks: [],
          comments: []
      });
      setIsNewTaskModalOpen(false);
      setNewTask({ title: '', department: 'GENERAL', priority: 'MEDIUM', dueDate: '', assignee: '' });
  };

  const handleQuickAdd = (status: TaskStatus) => {
      onAddTask({
          id: `t${Date.now()}`,
          title: 'Nuova Attività Rapida',
          status: status,
          department: 'GENERAL',
          priority: 'MEDIUM',
          dueDate: new Date().toISOString().split('T')[0],
          subtasks: [],
          comments: []
      });
  };

  // --- SUBTASKS & COMMENTS ---
  const handleAddSubtask = () => {
      if (!selectedTask || !subtaskInput.trim()) return;
      const newSubtask: Subtask = { id: `sub-${Date.now()}`, title: subtaskInput, isCompleted: false };
      const updated = { ...selectedTask, subtasks: [...(selectedTask.subtasks || []), newSubtask] };
      onUpdateTask(updated);
      setSelectedTask(updated);
      setSubtaskInput('');
  };

  const toggleSubtask = (subId: string) => {
      if (!selectedTask) return;
      const updated = {
          ...selectedTask,
          subtasks: selectedTask.subtasks?.map(s => s.id === subId ? {...s, isCompleted: !s.isCompleted} : s)
      };
      onUpdateTask(updated);
      setSelectedTask(updated);
  };

  const handleAddComment = () => {
      if (!selectedTask || !commentInput.trim()) return;
      const newComment = {
          id: `com-${Date.now()}`,
          authorId: 'u1',
          content: commentInput,
          date: new Date().toISOString()
      };
      const updated = { ...selectedTask, comments: [...(selectedTask.comments || []), newComment] };
      onUpdateTask(updated);
      setSelectedTask(updated);
      setCommentInput('');
  };

  // --- STYLING HELPERS ---
  const getPriorityStyle = (p: string) => {
      switch(p) {
          case 'HIGH': return { label: 'High Priority', bg: 'bg-rose-100', text: 'text-rose-800', border: 'border-rose-200' };
          case 'MEDIUM': return { label: 'Normal', bg: 'bg-amber-100', text: 'text-amber-800', border: 'border-amber-200' };
          default: return { label: 'Low', bg: 'bg-slate-100', text: 'text-slate-600', border: 'border-slate-200' };
      }
  };

  const getCalendarDays = () => {
      const year = currentDate.getFullYear();
      const month = currentDate.getMonth();
      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      const days = [];
      const startDay = firstDay.getDay() || 7; 
      for(let i=1; i<startDay; i++) days.push(null);
      for(let i=1; i<=lastDay.getDate(); i++) days.push(new Date(year, month, i));
      return days;
  };

  // --- ULTRA QUALITY DYNAMIC METALLIC THEME ---
  const getTaskTheme = (status: TaskStatus) => {
      const baseLayout = "rounded-sm relative overflow-hidden group/card cursor-grab active:cursor-grabbing transition-all duration-300 hover:-translate-y-1 border-t border-l border-b border-r";
      
      // Clean shadow only, NO colored glow behind
      const cleanShadow = "shadow-[0_4px_6px_-1px_rgba(0,0,0,0.3)] hover:shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5)]";

      switch (status) {
          case TaskStatus.IN_PROGRESS: // OPERATIVI (Azure Silver)
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#E0F2FE] via-[#BAE6FD] to-[#38BDF8] border-white/60 border-b-[#0284C7]/30 ${cleanShadow}`,
                  textPrimary: "text-[#0C4A6E]", 
                  textSecondary: "text-[#0284C7]",
                  badge: "bg-[#F0F9FF] text-[#0369A1] border-[#BAE6FD]",
                  iconColor: "text-[#0369A1]",
                  barBg: "bg-[#0284C7]"
              };
          case TaskStatus.REVIEW: // CONTROLLO QUALITÀ (Purple Silver)
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#F3E8FF] via-[#D8B4FE] to-[#9333EA] border-white/60 border-b-[#7E22CE]/30 ${cleanShadow}`,
                  textPrimary: "text-[#3B0764]",
                  textSecondary: "text-[#6B21A8]",
                  badge: "bg-[#FAF5FF] text-[#7E22CE] border-[#E9D5FF]",
                  iconColor: "text-[#6B21A8]",
                  barBg: "bg-[#7E22CE]"
              };
          case TaskStatus.DONE: // COMPLETATI (Emerald Silver)
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#ECFDF5] via-[#6EE7B7] to-[#059669] border-white/60 border-b-[#047857]/30 ${cleanShadow}`,
                  textPrimary: "text-[#022c22]",
                  textSecondary: "text-[#047857]",
                  badge: "bg-[#F0FDF4] text-[#15803d] border-[#BBF7D0]",
                  iconColor: "text-[#047857]",
                  barBg: "bg-[#065f46]"
              };
          default: // DA ASSEGNARE (Pure Silver)
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B] border-white/60 border-b-[#475569]/30 ${cleanShadow}`,
                  textPrimary: "text-[#0f172a]",
                  textSecondary: "text-[#334155]",
                  badge: "bg-[#F1F5F9] text-[#475569] border-[#E2E8F0]",
                  iconColor: "text-[#334155]",
                  barBg: "bg-[#334155]"
              };
      }
  };

  const metallicModalClass = "bg-gradient-to-br from-[#cbd5e1] via-[#94a3b8] to-[#64748b] border-t border-l border-white/40 border-b border-r border-black/40 rounded-sm shadow-2xl relative overflow-hidden";
  const metallicInputClass = "bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner";
  const metallicLabelClass = "text-slate-800 font-bold uppercase tracking-widest text-[10px]";

  return (
    <div className="flex flex-col animate-in fade-in duration-300 pb-20">
      
      {/* 1. HUD HEADER - STATS & ACTIONS */}
      <div className="flex flex-col gap-6 mb-8 shrink-0">
          <div className="flex justify-between items-end border-b border-white/5 pb-6">
            <div>
              <h1 className="text-3xl font-bold text-silver-gradient mb-2 tracking-tight flex items-center gap-3">
                  <LayoutGrid className="w-6 h-6 text-platinum-400" />
                  Tactical Operations Board
              </h1>
              <p className="text-platinum-500 text-sm">Centro di comando per la gestione dei flussi operativi.</p>
            </div>
            
            <div className="flex gap-3">
                {/* Stats Capsules */}
                <div className="hidden lg:flex gap-3 mr-6">
                    <div className="flex items-center gap-3 bg-[#0A0A0A] border border-white/10 px-4 py-2 rounded-sm shadow-inner">
                        <div className="p-1.5 bg-green-500/20 rounded-full border border-green-500/30 text-green-400"><CheckSquare className="w-3 h-3"/></div>
                        <div>
                            <p className="text-[9px] text-platinum-500 uppercase font-bold tracking-widest">Completed</p>
                            <p className="text-white font-mono font-bold leading-none">{completedTasks}/{totalTasks}</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3 bg-[#0A0A0A] border border-white/10 px-4 py-2 rounded-sm shadow-inner">
                        <div className="p-1.5 bg-red-500/20 rounded-full border border-red-500/30 text-red-400"><AlertCircle className="w-3 h-3"/></div>
                        <div>
                            <p className="text-[9px] text-platinum-500 uppercase font-bold tracking-widest">Urgent</p>
                            <p className="text-white font-mono font-bold leading-none">{urgentTasks} Active</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3 bg-[#0A0A0A] border border-white/10 px-4 py-2 rounded-sm shadow-inner">
                        <div className="p-1.5 bg-blue-500/20 rounded-full border border-blue-500/30 text-blue-400"><Zap className="w-3 h-3"/></div>
                        <div>
                            <p className="text-[9px] text-platinum-500 uppercase font-bold tracking-widest">Velocity</p>
                            <p className="text-white font-mono font-bold leading-none">{progressRate}%</p>
                        </div>
                    </div>
                </div>

                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-1 flex shadow-lg">
                    <button onClick={() => setViewMode('BOARD')} className={`p-2 rounded-sm transition-all duration-300 ${viewMode === 'BOARD' ? 'bg-gradient-to-b from-white to-platinum-300 text-black shadow-sm' : 'text-platinum-600 hover:text-white'}`} title="Board"><KanbanIcon className="w-4 h-4"/></button>
                    <button onClick={() => setViewMode('LIST')} className={`p-2 rounded-sm transition-all duration-300 ${viewMode === 'LIST' ? 'bg-gradient-to-b from-white to-platinum-300 text-black shadow-sm' : 'text-platinum-600 hover:text-white'}`} title="Elenco"><List className="w-4 h-4"/></button>
                    <button onClick={() => setViewMode('CALENDAR')} className={`p-2 rounded-sm transition-all duration-300 ${viewMode === 'CALENDAR' ? 'bg-gradient-to-b from-white to-platinum-300 text-black shadow-sm' : 'text-platinum-600 hover:text-white'}`} title="Calendario"><CalendarIcon className="w-4 h-4"/></button>
                </div>
                <Button variant="diamond" onClick={() => setIsNewTaskModalOpen(true)} icon={<Plus className="w-4 h-4" />}>NUOVA TASK</Button>
            </div>
          </div>

          {/* 2. TOOLBAR FILTERS */}
          <div className="flex justify-between items-center bg-[#08090A] border border-white/5 p-3 rounded-sm shadow-2xl relative overflow-hidden">
              {/* Metallic sheen on toolbar */}
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent pointer-events-none"></div>

              <div className="flex items-center gap-6 flex-1 relative z-10">
                  <div className="relative group">
                      <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-platinum-600 group-hover:text-white transition-colors" />
                      <input 
                          value={searchQuery}
                          onChange={(e) => setSearchQuery(e.target.value)}
                          placeholder="FILTRA MISSIONI..."
                          className="bg-[#111] border border-white/10 rounded-sm pl-10 pr-4 py-2 text-[10px] uppercase font-bold tracking-wider text-white focus:border-white/40 outline-none w-64 transition-all"
                      />
                  </div>
                  
                  <div className="h-6 w-[1px] bg-white/10"></div>

                  <div className="flex items-center gap-3">
                      <span className="text-[10px] font-bold text-platinum-600 uppercase tracking-widest"><Filter className="w-3 h-3 inline mr-1"/> Priority:</span>
                      <div className="flex gap-1">
                          {['ALL', 'HIGH', 'MEDIUM', 'LOW'].map(p => (
                              <button 
                                key={p} 
                                onClick={() => setFilterPriority(p)}
                                className={`text-[9px] font-bold uppercase px-2 py-1 rounded-sm border transition-all ${filterPriority === p ? 'bg-white text-black border-white' : 'bg-transparent text-platinum-500 border-white/10 hover:border-white/30'}`}
                              >
                                  {p}
                              </button>
                          ))}
                      </div>
                  </div>

                  <div className="flex items-center gap-3">
                      <span className="text-[10px] font-bold text-platinum-600 uppercase tracking-widest"><Layers className="w-3 h-3 inline mr-1"/> Dept:</span>
                      <select 
                          className="bg-[#111] border border-white/10 text-[9px] font-bold uppercase tracking-wider text-platinum-300 cursor-pointer hover:text-white outline-none py-1 px-2 rounded-sm"
                          value={filterDept}
                          onChange={(e) => setFilterDept(e.target.value)}
                      >
                          <option value="ALL">All Departments</option>
                          <option value="SOCIAL">Social Media</option>
                          <option value="EDITORIAL">Editoriale</option>
                          <option value="SALES">Vendite</option>
                          <option value="INFOBUSINESS">Infobusiness</option>
                      </select>
                  </div>
              </div>
              <div className="text-[9px] text-platinum-600 font-mono uppercase tracking-widest relative z-10 flex items-center gap-2">
                  <div className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse shadow-[0_0_5px_#22c55e]"></div>
                  Live Sync Active
              </div>
          </div>
      </div>

      {/* 3. MAIN BOARD VIEW - REINVENTED - FULL HEIGHT */}
      {viewMode === 'BOARD' && (
          <div className="flex overflow-x-auto pb-6 gap-6 items-start custom-scrollbar">
            {COLUMNS.map((col) => {
              const columnTasks = filteredTasks.filter(t => t.status === col.id);
              
              return (
                  <div 
                  key={col.id}
                  className="flex-shrink-0 w-[300px] flex flex-col rounded-sm group/col transition-all duration-300 relative"
                  onDragOver={(e) => e.preventDefault()}
                  onDrop={(e) => handleDrop(e, col.id)}
                >
                  {/* Column Header - Tech Style */}
                  <div className="mb-4 flex flex-col gap-1 px-1">
                      <div className="flex justify-between items-center">
                          <div className="flex items-center gap-3">
                              <div className={`w-2 h-2 rounded-full ${col.indicator}`}></div>
                              <h3 className="font-black text-sm uppercase tracking-[0.2em] text-white drop-shadow-md">
                                  {col.title}
                              </h3>
                          </div>
                          <span className="text-[10px] font-mono font-bold text-platinum-500 bg-white/5 px-2 py-0.5 rounded border border-white/5">
                              {columnTasks.length}
                          </span>
                      </div>
                      <div className={`h-[2px] w-full bg-gradient-to-r from-transparent via-white/20 to-transparent opacity-50`}></div>
                  </div>

                  <div className="p-1 space-y-4 relative z-10 pb-4">
                    {columnTasks.map(task => {
                      const completedSubtasks = task.subtasks?.filter(s => s.isCompleted).length || 0;
                      const totalSubtasks = task.subtasks?.length || 0;
                      const progress = totalSubtasks > 0 ? (completedSubtasks / totalSubtasks) * 100 : 0;
                      
                      const theme = getTaskTheme(task.status);

                      return (
                        <div
                          key={task.id}
                          draggable
                          onDragStart={(e) => handleDragStart(e, task.id)}
                          onDragEnd={handleDragEnd}
                          onClick={() => setSelectedTask(task)}
                          className={theme.card}
                        >
                          {/* Realistic Noise Texture */}
                          <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>
                          
                          {/* Metallic Sheen Overlay */}
                          <div className="absolute inset-0 bg-gradient-to-br from-white/30 via-transparent to-black/5 pointer-events-none z-0"></div>
                          
                          {/* Top Bar Accent - Colored by Priority */}
                          <div className={`absolute top-0 left-0 w-1 h-full z-20 ${task.priority === 'HIGH' ? 'bg-rose-600' : theme.barBg}`}></div>

                          <div className="relative z-10 pl-2 p-5">
                              {/* Meta Header */}
                              <div className="flex justify-between items-start mb-3">
                                 <span className={`text-[8px] font-bold px-2 py-0.5 rounded-sm uppercase tracking-wide shadow-sm border ${theme.badge}`}>
                                    {task.department}
                                 </span>
                                 {task.priority === 'HIGH' && (
                                     <Flag className="w-3 h-3 text-rose-700 fill-rose-600 animate-pulse drop-shadow-sm" />
                                 )}
                              </div>
                              
                              {/* Title */}
                              <h4 className={`text-xs font-black mb-2.5 leading-snug drop-shadow-sm tracking-tight ${theme.textPrimary}`}>
                                {task.title}
                              </h4>

                              {/* Progress Laser Line */}
                              {totalSubtasks > 0 && (
                                  <div className="mb-4 group-hover/card:opacity-100 transition-opacity">
                                      <div className={`flex justify-between text-[8px] mb-1 font-mono font-bold uppercase ${theme.textSecondary}`}>
                                          <span>Progress</span>
                                          <span>{Math.round(progress)}%</span>
                                      </div>
                                      <div className="h-[2px] w-full bg-black/10 rounded-full overflow-hidden border border-white/20">
                                          <div className={`h-full ${theme.barBg} shadow-[0_0_5px_rgba(0,0,0,0.2)]`} style={{width: `${progress}%`}}></div>
                                      </div>
                                  </div>
                              )}
                              
                              {/* Footer Info */}
                              <div className="flex items-center justify-between pt-3 border-t border-black/5">
                                <div className="flex items-center gap-3">
                                   {task.assignee ? (
                                       <div className="flex items-center gap-2" title={MOCK_USERS.find(u => u.id === task.assignee)?.name}>
                                           <div className={`w-5 h-5 rounded-sm flex items-center justify-center text-[8px] font-bold shadow-sm bg-black/80 text-white border border-white/20`}>
                                               {MOCK_USERS.find(u => u.id === task.assignee)?.name.substring(0,1)}
                                           </div>
                                       </div>
                                   ) : (
                                       <div className={`w-5 h-5 rounded-sm border border-dashed flex items-center justify-center ${theme.iconColor} border-current opacity-60`}>
                                           <User className="w-3 h-3" />
                                       </div>
                                   )}
                                   
                                   <div className={`flex items-center gap-1 text-[9px] font-bold font-mono ${theme.textSecondary}`}>
                                       <Clock className="w-3 h-3" /> 
                                       <span className={new Date(task.dueDate) < new Date() && task.status !== 'DONE' ? 'text-rose-700 font-black' : ''}>
                                          {new Date(task.dueDate).toLocaleDateString(undefined, {day:'2-digit', month:'2-digit'})}
                                       </span>
                                   </div>
                                </div>
                                
                                <div className={`flex gap-2 ${theme.textSecondary}`}>
                                    {task.comments && task.comments.length > 0 && (
                                        <div className="flex items-center gap-0.5 text-[9px] font-bold">
                                            <MessageSquare className="w-3 h-3" /> {task.comments.length}
                                        </div>
                                    )}
                                </div>
                              </div>
                          </div>
                        </div>
                      );
                    })}
                    
                    <button 
                        onClick={() => handleQuickAdd(col.id)}
                        className="w-full py-3 border-2 border-dashed border-white/20 rounded-sm text-[10px] text-platinum-500 font-bold uppercase tracking-widest hover:bg-white/5 hover:text-white hover:border-white/40 transition-all flex items-center justify-center gap-2 group shadow-[inset_0_0_20px_rgba(0,0,0,0.2)]"
                    >
                        <Plus className="w-3 h-3 group-hover:scale-110 transition-transform" /> Quick Add
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
      )}

      {/* STATS AND GRAPHS SECTION (Livello 1) */}
      {viewMode === 'BOARD' && (
          <div className="mt-8 grid grid-cols-1 lg:grid-cols-2 gap-6 pb-10 px-1 border-t border-white/5 pt-8">
              <div className="bg-gradient-to-br from-[#111315] to-[#08090A] border border-white/10 rounded-sm p-5 relative overflow-hidden shadow-2xl">
                  <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>
                  <h3 className="text-[10px] font-bold uppercase tracking-widest text-platinum-400 mb-4 flex items-center gap-2 relative z-10"><Activity className="w-3.5 h-3.5"/> Task Velocity / Trend Settimanale</h3>
                  <div className="h-28 flex items-end gap-3 mt-4 relative z-10 border-b border-white/10 pb-1">
                      <div className="flex-1 bg-white/5 rounded-t-sm hover:bg-white/10 transition-colors relative group h-[40%]">
                          <div className="absolute bottom-full mb-1 left-1/2 -translate-x-1/2 text-[9px] font-bold opacity-0 group-hover:opacity-100 transition-opacity text-platinum-300">12</div>
                          <div className="h-full bg-gradient-to-t from-blue-900 to-blue-500/80 rounded-t-sm w-full border-t border-blue-400/50"></div>
                      </div>
                      <div className="flex-1 bg-white/5 rounded-t-sm hover:bg-white/10 transition-colors relative group h-[60%]">
                          <div className="absolute bottom-full mb-1 left-1/2 -translate-x-1/2 text-[9px] font-bold opacity-0 group-hover:opacity-100 transition-opacity text-platinum-300">25</div>
                          <div className="h-full bg-gradient-to-t from-blue-900 to-blue-500/80 rounded-t-sm w-full border-t border-blue-400/50"></div>
                      </div>
                      <div className="flex-1 bg-white/5 rounded-t-sm hover:bg-white/10 transition-colors relative group h-[80%]">
                          <div className="absolute bottom-full mb-1 left-1/2 -translate-x-1/2 text-[9px] font-bold opacity-0 group-hover:opacity-100 transition-opacity text-platinum-300">34</div>
                          <div className="h-full bg-gradient-to-t from-blue-900 to-blue-500/80 rounded-t-sm w-full border-t border-blue-400/50"></div>
                      </div>
                      <div className="flex-1 bg-white/5 rounded-t-sm hover:bg-white/10 transition-colors relative group h-[100%]">
                          <div className="absolute bottom-full mb-1 left-1/2 -translate-x-1/2 text-[9px] font-bold opacity-0 group-hover:opacity-100 transition-opacity text-platinum-300">45</div>
                          <div className="h-full bg-gradient-to-t from-emerald-900 to-emerald-500/80 rounded-t-sm w-full border-t border-emerald-400/50"></div>
                      </div>
                  </div>
                  <div className="flex justify-between mt-2 text-[9px] font-mono text-platinum-600 uppercase tracking-widest relative z-10 px-2"><span>W1</span><span>W2</span><span>W3</span><span>W4</span></div>
              </div>

              <div className="bg-gradient-to-br from-[#111315] to-[#08090A] border border-white/10 rounded-sm p-5 relative overflow-hidden shadow-2xl flex flex-col justify-between">
                  <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>
                  <h3 className="text-[10px] font-bold uppercase tracking-widest text-platinum-400 mb-6 flex items-center gap-2 relative z-10"><Layers className="w-3.5 h-3.5"/> Compiti per Reparto Operativo</h3>
                  <div className="space-y-4 relative z-10 flex-1">
                      <div>
                          <div className="flex justify-between text-[9px] font-bold uppercase tracking-widest text-platinum-300 mb-1.5"><span>Marketing & Funnel</span><span className="text-rose-400">45%</span></div>
                          <div className="w-full bg-black/40 h-1.5 rounded-full overflow-hidden border border-white/5"><div className="bg-rose-500 h-full w-[45%] shadow-[0_0_8px_rgba(244,63,94,0.6)]"></div></div>
                      </div>
                      <div>
                          <div className="flex justify-between text-[9px] font-bold uppercase tracking-widest text-platinum-300 mb-1.5"><span>Dev & Automation</span><span className="text-blue-400">30%</span></div>
                          <div className="w-full bg-black/40 h-1.5 rounded-full overflow-hidden border border-white/5"><div className="bg-blue-500 h-full w-[30%] shadow-[0_0_8px_rgba(59,130,246,0.6)]"></div></div>
                      </div>
                      <div>
                          <div className="flex justify-between text-[9px] font-bold uppercase tracking-widest text-platinum-300 mb-1.5"><span>Admin & Finance</span><span className="text-emerald-400">25%</span></div>
                          <div className="w-full bg-black/40 h-1.5 rounded-full overflow-hidden border border-white/5"><div className="bg-emerald-500 h-full w-[25%] shadow-[0_0_8px_rgba(16,185,129,0.6)]"></div></div>
                      </div>
                  </div>
              </div>
          </div>
      )}

      {/* --- LIST VIEW - DATA TABLE STYLE --- */}
      {viewMode === 'LIST' && (
          <div className="bg-[#0A0A0A] border border-white/10 rounded-sm overflow-hidden flex flex-col shadow-2xl relative min-h-[500px]">
              <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>
              
              <div className="grid grid-cols-12 gap-4 p-4 bg-[#0F0F0F] border-b border-white/10 text-[9px] font-bold text-platinum-500 uppercase tracking-widest sticky top-0 z-10">
                  <div className="col-span-4 pl-4">Operation Name</div>
                  <div className="col-span-2">Department</div>
                  <div className="col-span-2">Status</div>
                  <div className="col-span-2">Assignee</div>
                  <div className="col-span-1">Priority</div>
                  <div className="col-span-1 text-right pr-4">Deadline</div>
              </div>
              <div className="overflow-visible relative z-10">
                  {filteredTasks.map((task, idx) => (
                      <div 
                        key={task.id} 
                        onClick={() => setSelectedTask(task)}
                        className={`grid grid-cols-12 gap-4 p-4 items-center cursor-pointer text-sm group border-b border-white/5 hover:bg-white/5 transition-colors ${idx % 2 === 0 ? 'bg-[#0A0A0A]' : 'bg-[#0C0C0C]'}`}
                      >
                          <div className="col-span-4 font-bold text-white flex items-center gap-4 pl-4">
                              <div className={`w-2 h-2 rounded-full ${task.status === 'DONE' ? 'bg-emerald-500' : 'bg-platinum-600'}`}></div>
                              <span className={task.status === 'DONE' ? 'line-through text-platinum-600' : ''}>{task.title}</span>
                          </div>
                          <div className="col-span-2 text-xs text-platinum-400 font-mono uppercase tracking-tight">{task.department}</div>
                          <div className="col-span-2">
                              <span className={`text-[9px] font-bold px-2 py-1 rounded-sm border uppercase tracking-wider bg-black/40 border-white/10 text-platinum-300`}>
                                  {COLUMNS.find(c => c.id === task.status)?.title}
                              </span>
                          </div>
                          <div className="col-span-2 flex items-center gap-2">
                              {task.assignee ? (
                                  <>
                                    <div className="w-5 h-5 rounded-sm bg-[#222] flex items-center justify-center text-[9px] text-white font-bold border border-white/10">
                                        {MOCK_USERS.find(u => u.id === task.assignee)?.name.substring(0,1)}
                                    </div>
                                    <span className="text-xs text-platinum-400">{MOCK_USERS.find(u => u.id === task.assignee)?.name}</span>
                                  </>
                              ) : <span className="text-platinum-700 text-xs">-</span>}
                          </div>
                          <div className="col-span-1">
                              {task.priority === 'HIGH' ? (
                                  <span className="flex items-center gap-1 text-[9px] font-bold text-rose-400 bg-rose-900/10 px-2 py-1 rounded border border-rose-900/30 uppercase"><Flag className="w-3 h-3"/> High</span>
                              ) : (
                                  <span className="text-[9px] font-bold text-platinum-500 uppercase">{task.priority}</span>
                              )}
                          </div>
                          <div className="col-span-1 text-right text-xs font-mono text-platinum-500 pr-4">
                              {new Date(task.dueDate).toLocaleDateString(undefined, {month:'numeric', day:'numeric'})}
                          </div>
                      </div>
                  ))}
              </div>
          </div>
      )}

      {/* --- CALENDAR VIEW --- */}
      {viewMode === 'CALENDAR' && (
          <div className="bg-[#0A0A0A] border border-white/10 rounded-sm flex flex-col min-h-[800px] overflow-hidden shadow-2xl relative">
               <div className="p-4 flex justify-between items-center border-b border-white/10 bg-[#0F0F0F] shrink-0 relative z-10">
                    <div className="flex items-center gap-4">
                        <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1))} className="hover:text-white text-platinum-500"><ChevronLeft className="w-5 h-5"/></button>
                        <span className="text-lg font-bold text-white uppercase tracking-widest min-w-[200px] text-center">
                            {currentDate.toLocaleDateString('it-IT', { month: 'long', year: 'numeric' })}
                        </span>
                        <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1))} className="hover:text-white text-platinum-500"><ChevronRight className="w-5 h-5"/></button>
                    </div>
               </div>
               <div className="flex-1 grid grid-cols-7 grid-rows-5 gap-[1px] bg-white/5 relative z-10">
                   {getCalendarDays().map((date, i) => {
                       if (!date) return <div key={i} className="bg-[#0A0A0A]"></div>;
                       const dayTasks = filteredTasks.filter(t => t.dueDate === date.toISOString().split('T')[0] && t.status !== 'DONE');
                       const isToday = new Date().toDateString() === date.toDateString();

                       return (
                           <div key={i} className={`bg-[#0A0A0A] p-2 hover:bg-[#0F0F0F] transition-colors relative group overflow-hidden flex flex-col ${isToday ? 'bg-white/5' : ''}`}>
                               <div className={`text-right text-xs font-mono mb-2 ${isToday ? 'text-white font-bold' : 'text-platinum-600'}`}>{date.getDate()}</div>
                               <div className="flex-1 space-y-1 overflow-y-auto custom-scrollbar">
                                   {dayTasks.map(t => (
                                       <div 
                                          key={t.id} 
                                          onClick={() => setSelectedTask(t)}
                                          className={`text-[8px] px-2 py-1.5 rounded-sm border-l-2 truncate cursor-pointer bg-[#151515] text-platinum-300 hover:text-white hover:bg-[#222] transition-colors ${t.priority === 'HIGH' ? 'border-rose-500' : 'border-platinum-500'}`}
                                       >
                                           {t.title}
                                       </div>
                                   ))}
                               </div>
                           </div>
                       );
                   })}
               </div>
          </div>
      )}

      {/* --- MODALS --- */}
      
      {/* NEW TASK MODAL */}
      {isNewTaskModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-md animate-in fade-in duration-200">
              <div className={`${metallicModalClass} w-full max-w-lg p-10`}>
                  {/* Texture */}
                  <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>
                  
                  <button onClick={() => setIsNewTaskModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20">
                    <X className="w-6 h-6" />
                  </button>
                  
                  <h3 className="text-2xl font-black text-slate-900 mb-8 uppercase tracking-widest flex items-center gap-3 relative z-10">
                      <Plus className="w-6 h-6 text-slate-800" /> Nuova Missione
                  </h3>
                  
                  <form onSubmit={handleSubmit} className="space-y-6 relative z-10">
                      <div className="space-y-2">
                        <label className={metallicLabelClass}>Titolo Task</label>
                        <input className={`${metallicInputClass} w-full p-4`} 
                            placeholder="Descrivi l'attività..." value={newTask.title} onChange={e => setNewTask({...newTask, title: e.target.value})} required />
                      </div>
                      <div className="grid grid-cols-2 gap-6">
                          <div className="space-y-2">
                            <label className={metallicLabelClass}>Dipartimento</label>
                            <select className={`${metallicInputClass} w-full p-4`} 
                                value={newTask.department} onChange={e => setNewTask({...newTask, department: e.target.value as any})}>
                               <option value="GENERAL">Generale</option>
                               <option value="SOCIAL">Social Media</option>
                               <option value="EDITORIAL">Editoriale</option>
                               <option value="INFOBUSINESS">Infobusiness</option>
                               <option value="SALES">Vendite</option>
                            </select>
                          </div>
                          <div className="space-y-2">
                            <label className={metallicLabelClass}>Priorità</label>
                            <select className={`${metallicInputClass} w-full p-4`} 
                                value={newTask.priority} onChange={e => setNewTask({...newTask, priority: e.target.value as any})}>
                               <option value="LOW">Bassa</option>
                               <option value="MEDIUM">Media</option>
                               <option value="HIGH">Alta</option>
                            </select>
                          </div>
                      </div>
                      <div className="grid grid-cols-2 gap-6">
                        <div className="space-y-2">
                          <label className={metallicLabelClass}>Assegnatario</label>
                          <select className={`${metallicInputClass} w-full p-4`} 
                              value={newTask.assignee} onChange={e => setNewTask({...newTask, assignee: e.target.value})}>
                              <option value="">-- Seleziona --</option>
                              {MOCK_USERS.map(u => <option key={u.id} value={u.id}>{u.name}</option>)}
                          </select>
                        </div>
                        <div className="space-y-2">
                          <label className={metallicLabelClass}>Scadenza</label>
                          <input type="date" className={`${metallicInputClass} w-full p-4`} 
                              value={newTask.dueDate} onChange={e => setNewTask({...newTask, dueDate: e.target.value})} required />
                        </div>
                      </div>
                      <Button type="submit" className="w-full py-4 mt-6 font-bold tracking-[0.2em] uppercase shadow-xl bg-slate-900 text-white hover:bg-slate-800 border-none">Conferma Creazione</Button>
                  </form>
              </div>
          </div>
      )}

      {/* TASK DETAIL MODAL (THE DOSSIER) */}
      {selectedTask && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-md animate-in fade-in duration-200">
               <div className={`${metallicModalClass} w-full max-w-5xl h-[85vh] flex flex-col`}>
                    {/* Texture */}
                    <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>

                    {/* Header */}
                    <div className="h-24 bg-slate-900/10 border-b border-slate-900/10 px-10 flex items-center justify-between shrink-0 relative z-10 backdrop-blur-sm">
                         <div className="flex items-center gap-6">
                             <div className={`text-[10px] font-bold px-3 py-1.5 rounded-sm border uppercase tracking-wider ${getPriorityStyle(selectedTask.priority).bg} ${getPriorityStyle(selectedTask.priority).text} ${getPriorityStyle(selectedTask.priority).border}`}>
                                 {selectedTask.priority} Priority
                             </div>
                             <div className="h-6 w-[1px] bg-slate-900/20"></div>
                             <div className="text-xs text-slate-800 font-mono uppercase flex items-center gap-2 font-bold">
                                <Layers className="w-4 h-4"/> {selectedTask.department}
                             </div>
                         </div>
                         <div className="flex items-center gap-6">
                             {selectedTask.assignee && (
                                 <div className="flex items-center gap-3 bg-slate-900/10 px-4 py-2 rounded-full border border-slate-900/10">
                                     <div className="w-6 h-6 rounded-full bg-slate-800 flex items-center justify-center text-[10px] text-white font-bold border border-slate-700 shadow-md">
                                        {MOCK_USERS.find(u => u.id === selectedTask.assignee)?.name.substring(0,1)}
                                     </div>
                                     <span className="text-xs text-slate-900 font-bold">{MOCK_USERS.find(u => u.id === selectedTask.assignee)?.name}</span>
                                 </div>
                             )}
                             <button onClick={() => setSelectedTask(null)} className="text-slate-700 hover:text-red-600 p-2 rounded-full transition-colors"><X className="w-6 h-6"/></button>
                         </div>
                    </div>

                    <div className="flex-1 flex overflow-hidden relative z-10">
                        {/* Main Content */}
                        <div className="flex-1 p-10 overflow-y-auto custom-scrollbar">
                             <h2 className="text-4xl font-black text-slate-900 mb-8 leading-tight tracking-tight drop-shadow-sm">{selectedTask.title}</h2>
                             
                             <div className="grid grid-cols-3 gap-10">
                                 {/* Column Left: Details & Checklists */}
                                 <div className="col-span-2 space-y-10">
                                     <div>
                                         <h4 className={`${metallicLabelClass} mb-4 flex items-center gap-2`}><GripVertical className="w-4 h-4"/> Descrizione</h4>
                                         <textarea 
                                            className={`${metallicInputClass} w-full h-48 p-6 text-sm resize-none leading-relaxed shadow-lg`}
                                            placeholder="Aggiungi dettagli operativi, link o note..."
                                            defaultValue={selectedTask.description}
                                            onBlur={(e) => onUpdateTask({...selectedTask, description: e.target.value})}
                                         />
                                     </div>

                                     <div>
                                         <div className="flex justify-between items-end mb-4">
                                             <h4 className={`${metallicLabelClass} flex items-center gap-2`}><CheckSquare className="w-4 h-4"/> Checklist Operativa</h4>
                                             <span className="text-[10px] text-slate-700 font-mono font-bold bg-white/40 px-2 py-1 rounded">
                                                 {selectedTask.subtasks?.filter(s => s.isCompleted).length || 0}/{selectedTask.subtasks?.length || 0}
                                             </span>
                                         </div>
                                         
                                         <div className="bg-slate-900/50 border border-slate-700 rounded-sm overflow-hidden backdrop-blur-sm shadow-lg">
                                             {selectedTask.subtasks?.map(sub => (
                                                 <div key={sub.id} className="flex items-center gap-4 p-4 border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors group">
                                                     <button 
                                                        onClick={() => toggleSubtask(sub.id)}
                                                        className={`w-5 h-5 rounded-sm border flex items-center justify-center transition-all ${sub.isCompleted ? 'bg-green-500 border-green-500' : 'border-slate-500 hover:border-white'}`}
                                                     >
                                                         {sub.isCompleted && <CheckSquare className="w-3 h-3 text-black" />}
                                                     </button>
                                                     <span className={`text-sm flex-1 font-medium ${sub.isCompleted ? 'text-slate-500 line-through' : 'text-white'}`}>{sub.title}</span>
                                                 </div>
                                             ))}
                                             <div className="flex bg-slate-900 border-t border-slate-700">
                                                 <input 
                                                    className="flex-1 bg-transparent border-none px-6 py-4 text-sm text-white focus:ring-0 outline-none placeholder:text-slate-500"
                                                    placeholder="Aggiungi step..."
                                                    value={subtaskInput}
                                                    onChange={(e) => setSubtaskInput(e.target.value)}
                                                    onKeyDown={(e) => e.key === 'Enter' && handleAddSubtask()}
                                                 />
                                                 <button onClick={handleAddSubtask} className="px-6 text-slate-400 hover:text-white"><Plus className="w-5 h-5"/></button>
                                             </div>
                                         </div>
                                     </div>
                                 </div>

                                 {/* Column Right: Meta & Activity */}
                                 <div className="col-span-1 border-l border-slate-900/10 pl-10 flex flex-col h-full">
                                     <div className="space-y-8 mb-10">
                                         <div>
                                             <label className={`${metallicLabelClass} mb-2 block`}>Stato Attuale</label>
                                             <select 
                                                className={`${metallicInputClass} w-full p-3 text-xs font-bold uppercase tracking-wider`}
                                                value={selectedTask.status}
                                                onChange={(e) => {
                                                    const updated = {...selectedTask, status: e.target.value as TaskStatus};
                                                    onUpdateTask(updated);
                                                    setSelectedTask(updated);
                                                }}
                                             >
                                                 {COLUMNS.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                                             </select>
                                         </div>
                                         <div>
                                             <label className={`${metallicLabelClass} mb-2 block`}>Deadline</label>
                                             <div className={`${metallicInputClass} p-3 text-xs flex items-center gap-3 font-mono font-bold`}>
                                                 <CalendarIcon className="w-4 h-4 text-slate-400" />
                                                 {selectedTask.dueDate}
                                             </div>
                                         </div>
                                     </div>

                                     <div className="flex-1 flex flex-col min-h-0 bg-slate-900/10 border border-slate-900/10 rounded-sm overflow-hidden backdrop-blur-sm shadow-md">
                                         <div className="p-4 bg-slate-900/20 border-b border-slate-900/10 text-[10px] font-bold text-slate-800 uppercase tracking-widest flex items-center gap-2">
                                             <MessageSquare className="w-3 h-3"/> Feed Attività
                                         </div>
                                         <div className="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar">
                                             {selectedTask.comments?.map(comment => (
                                                 <div key={comment.id} className="flex gap-3 items-start">
                                                     <div className="w-6 h-6 rounded bg-slate-800 flex-shrink-0 flex items-center justify-center text-[9px] text-white font-bold mt-1 shadow-sm border border-slate-600">M</div>
                                                     <div className="flex-1 min-w-0">
                                                         <div className="bg-white/60 p-3 rounded-sm rounded-tl-none shadow-sm border border-white/60">
                                                             <p className="text-[11px] text-slate-900 leading-relaxed font-medium">{comment.content}</p>
                                                         </div>
                                                         <span className="text-[9px] text-slate-600 mt-1 block font-mono">{new Date(comment.date).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</span>
                                                     </div>
                                                 </div>
                                             ))}
                                         </div>
                                         <div className="p-3 border-t border-slate-900/10 bg-slate-900/20">
                                             <div className="relative">
                                                 <input 
                                                    className={`${metallicInputClass} w-full pl-4 pr-10 py-2 text-xs`}
                                                    placeholder="Scrivi un commento..."
                                                    value={commentInput}
                                                    onChange={(e) => setCommentInput(e.target.value)}
                                                    onKeyDown={(e) => e.key === 'Enter' && handleAddComment()}
                                                 />
                                                 <button onClick={handleAddComment} className="absolute right-2 top-1/2 -translate-y-1/2 p-1 text-slate-400 hover:text-white transition-colors"><Send className="w-3 h-3"/></button>
                                             </div>
                                         </div>
                                     </div>
                                 </div>
                             </div>
                        </div>
                    </div>
               </div>
          </div>
      )}
    </div>
  );
};
