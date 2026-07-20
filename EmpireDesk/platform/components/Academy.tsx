
import React, { useState } from 'react';
import { AcademyCategory, AcademyModule, AcademyLesson } from '../types';
import { 
  BookOpen, 
  ChevronRight, 
  Layout, 
  Cpu, 
  FileType, 
  Terminal, 
  Smartphone, 
  ShoppingCart, 
  DollarSign, 
  Folder,
  PlayCircle,
  FileText,
  CheckCircle2,
  Search,
  ArrowLeft,
  Brain,
  Edit3,
  Plus,
  Trash2,
  Book,
  ChevronDown,
  MonitorPlay,
  Menu,
  X
} from 'lucide-react';
import { Button } from './ui/Button';

interface AcademyProps {
  categories: AcademyCategory[];
  modules: AcademyModule[];
  isAdmin: boolean;
  onToggleLessonComplete: (moduleId: string, lessonId: string) => void;
  // Management Functions
  onAddModule: (categoryId: string, title: string) => void;
  onUpdateModule: (moduleId: string, updates: Partial<AcademyModule>) => void;
  onDeleteModule: (moduleId: string) => void;
  onAddLesson: (moduleId: string, title: string) => void;
  onUpdateLesson: (moduleId: string, lessonId: string, updates: Partial<AcademyLesson>) => void;
  onDeleteLesson: (moduleId: string, lessonId: string) => void;
}

export const Academy: React.FC<AcademyProps> = ({ 
    categories, modules, isAdmin, 
    onToggleLessonComplete, onAddModule, onUpdateModule, onDeleteModule,
    onAddLesson, onUpdateLesson, onDeleteLesson
}) => {
  // Navigation State
  const [activeCategoryId, setActiveCategoryId] = useState<string | null>(null);
  const [activeModuleId, setActiveModuleId] = useState<string | null>(null);
  const [activeLessonId, setActiveLessonId] = useState<string | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(true); // For the internal course sidebar
  
  // Editor State
  const [isCreatorMode, setIsCreatorMode] = useState(false);
  const [newModuleTitle, setNewModuleTitle] = useState('');
  const [newLessonTitle, setNewLessonTitle] = useState('');
  const [isAddingModule, setIsAddingModule] = useState(false);
  const [isAddingLessonToModuleId, setIsAddingLessonToModuleId] = useState<string | null>(null);

  // Helper to get icons
  const getIconForCategory = (iconName: string) => {
      switch(iconName) {
          case 'Brain': return Brain;
          case 'PlayCircle': return PlayCircle;
          case 'Smartphone': return Smartphone;
          case 'BookOpen': return BookOpen;
          case 'ShoppingCart': return ShoppingCart;
          case 'MonitorPlay': return Terminal; 
          case 'Book': return Book;
          case 'DollarSign': return DollarSign;
          default: return Folder;
      }
  };

  // --- THEME ENGINE: HIGH FIDELITY METALLIC (NO BORDERS) ---
  const getCardTheme = (iconName: string) => {
      switch(iconName) {
          case 'Brain': // PLATINUM SILVER (HQ)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8]',
                  // Removed explicit border, kept soft inset for 3D feel without outline
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]', 
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(255,255,255,0.2)]',
                  cardText: 'text-slate-900',
                  cardMuted: 'text-slate-600',
                  cardIconBg: 'bg-gradient-to-br from-white to-slate-200 text-slate-900 shadow-inner',
                  accentColor: 'bg-slate-900'
              };
          case 'ShoppingCart': // AMETHYST SILVER (UGC)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#faf5ff] via-[#e9d5ff] to-[#a855f7]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(168,85,247,0.3)]',
                  cardText: 'text-purple-950',
                  cardMuted: 'text-purple-800',
                  cardIconBg: 'bg-gradient-to-br from-white to-purple-100 text-purple-900 shadow-inner',
                  accentColor: 'bg-purple-900'
              };
          case 'BookOpen': // EMERALD SILVER (Storytelling)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#f0fdf4] via-[#bbf7d0] to-[#10b981]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(16,185,129,0.3)]',
                  cardText: 'text-emerald-950',
                  cardMuted: 'text-emerald-800',
                  cardIconBg: 'bg-gradient-to-br from-white to-emerald-100 text-emerald-900 shadow-inner',
                  accentColor: 'bg-emerald-900'
              };
          case 'MonitorPlay': // TITANIUM CYAN (Funnel)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#ecfeff] via-[#a5f3fc] to-[#06b6d4]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(6,182,212,0.3)]',
                  cardText: 'text-cyan-950',
                  cardMuted: 'text-cyan-800',
                  cardIconBg: 'bg-gradient-to-br from-white to-cyan-100 text-cyan-900 shadow-inner',
                  accentColor: 'bg-cyan-900'
              };
          case 'PlayCircle': // ANODIZED RED (YouTube)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#fff1f2] via-[#fecdd3] to-[#f43f5e]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(244,63,94,0.3)]',
                  cardText: 'text-rose-950',
                  cardMuted: 'text-rose-800',
                  cardIconBg: 'bg-gradient-to-br from-white to-rose-100 text-rose-900 shadow-inner',
                  accentColor: 'bg-rose-900'
              };
          case 'Book': // BRUSHED BRONZE (KDP)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#fff7ed] via-[#fed7aa] to-[#f97316]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(249,115,22,0.3)]',
                  cardText: 'text-orange-950',
                  cardMuted: 'text-orange-900',
                  cardIconBg: 'bg-gradient-to-br from-white to-orange-100 text-orange-900 shadow-inner',
                  accentColor: 'bg-orange-900'
              };
          case 'DollarSign': // GOLD METALLIC (Sales)
              return {
                  cardGradient: 'bg-gradient-to-br from-[#fffbeb] via-[#fcd34d] to-[#d97706]',
                  cardBorder: 'shadow-[inset_0_1px_0_0_rgba(255,255,255,0.5)]',
                  cardShadow: 'shadow-[0_15px_35px_-5px_rgba(217,119,6,0.3)]',
                  cardText: 'text-amber-950',
                  cardMuted: 'text-amber-900',
                  cardIconBg: 'bg-gradient-to-br from-white to-amber-100 text-amber-800 shadow-inner',
                  accentColor: 'bg-amber-900'
              };
          default: return {
              cardGradient: 'bg-[#111]',
              cardBorder: '',
              cardShadow: '',
              cardText: 'text-white',
              cardMuted: 'text-platinum-500',
              cardIconBg: 'bg-white/10',
              accentColor: 'bg-white'
          };
      }
  };

  // --- TEXT RENDERER ENGINE ---
  const renderContent = (content: string) => {
    const lines = content.split('\n');
    return lines.map((line, idx) => {
        if (line.startsWith('# ')) return <h1 key={idx} className="text-3xl font-bold text-white mb-6 mt-10 border-b border-white/10 pb-4 tracking-tight">{processLineText(line.replace('# ', ''))}</h1>;
        if (line.startsWith('## ')) return <h2 key={idx} className="text-2xl font-semibold text-platinum-200 mb-4 mt-8 tracking-wide">{processLineText(line.replace('## ', ''))}</h2>;
        if (line.startsWith('### ')) return <h3 key={idx} className="text-lg font-bold text-platinum-400 mb-3 mt-6 uppercase tracking-wider">{processLineText(line.replace('### ', ''))}</h3>;
        if (line.startsWith('- ') || line.startsWith('○ ')) return <li key={idx} className="ml-6 list-disc text-platinum-300 mb-2 pl-2 marker:text-silver-dark">{processLineText(line.replace(/^[-○] /, ''))}</li>;
        if (/^\d+\.\s/.test(line)) return <div key={idx} className="ml-6 mb-2 flex gap-3 text-platinum-300"><span className="font-bold text-white min-w-[20px]">{line.match(/^\d+\./)?.[0]}</span><span>{processLineText(line.replace(/^\d+\.\s/, ''))}</span></div>;
        if (line.trim() === '') return <div key={idx} className="h-4"></div>;
        return <p key={idx} className="mb-4 leading-8 text-platinum-300 font-light tracking-wide text-base">{processLineText(line)}</p>;
    });
  };

  const processLineText = (text: string): React.ReactNode => {
      const parts = text.split(/(\*\*.*?\*\*)/g);
      return parts.map((part, i) => {
          if (part.startsWith('**') && part.endsWith('**')) return <strong key={i} className="font-bold text-white">{part.slice(2, -2)}</strong>;
          return part;
      });
  };

  // --- ACTIONS ---
  const handleCreateModule = () => {
      if (newModuleTitle.trim() && activeCategoryId) {
          onAddModule(activeCategoryId, newModuleTitle);
          setNewModuleTitle('');
          setIsAddingModule(false);
      }
  };

  const handleCreateLesson = (moduleId: string) => {
      if (newLessonTitle.trim()) {
          onAddLesson(moduleId, newLessonTitle);
          setNewLessonTitle('');
          setIsAddingLessonToModuleId(null);
      }
  };

  // --- VIEW 1: THE LIBRARY (Main Dashboard View) ---
  if (!activeCategoryId) {
    return (
      <div className="space-y-10 animate-in fade-in duration-500 pb-10">
        <div className="flex justify-between items-end border-b border-white/5 pb-6">
           <div>
              <h1 className="text-4xl font-bold text-silver-gradient mb-2 tracking-tight">Academy & Formazione</h1>
              <p className="text-platinum-500 text-sm">Seleziona un'area tematica per accedere ai manuali operativi e alle guide.</p>
           </div>
           
           <div className="flex gap-4">
               {isAdmin && (
                   <button 
                      onClick={() => setIsCreatorMode(!isCreatorMode)}
                      className={`
                        px-4 py-2 rounded-sm text-xs font-bold uppercase tracking-widest border transition-all flex items-center gap-2
                        ${isCreatorMode ? 'bg-diamond-950 text-diamond-400 border-diamond-500 shadow-[0_0_15px_rgba(34,211,238,0.2)]' : 'bg-[#111] text-platinum-500 border-white/10 hover:text-white'}
                      `}
                   >
                       <Edit3 className="w-4 h-4" /> Modalità Creatore
                   </button>
               )}
               <div className="relative group">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-platinum-600 group-hover:text-platinum-400 transition-colors" />
                  <input 
                    type="text" 
                    placeholder="Cerca argomento..." 
                    className="bg-[#0A0A0A] border border-white/10 rounded-full py-2 pl-10 pr-4 text-sm text-platinum-300 focus:border-white/30 focus:w-64 w-48 transition-all outline-none"
                  />
               </div>
           </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {categories.map((cat) => {
                const catModules = modules.filter(m => m.categoryId === cat.id);
                const Icon = getIconForCategory(cat.icon);
                const theme = getCardTheme(cat.icon);
                
                return (
                  <button 
                    key={cat.id}
                    onClick={() => {
                        setActiveCategoryId(cat.id);
                        if (catModules.length > 0) {
                            setActiveModuleId(catModules[0].id);
                            if (catModules[0].lessons.length > 0) {
                                setActiveLessonId(catModules[0].lessons[0].id);
                            }
                        }
                    }}
                    className={`
                        group relative rounded-lg p-8 text-left transition-all duration-500 overflow-hidden flex flex-col h-64
                        ${theme.cardGradient} ${theme.cardBorder} ${theme.cardShadow} 
                        hover:scale-[1.02] hover:-translate-y-1 border-0 ring-0 outline-none
                    `}
                  >
                      {/* 1. Metallic Shine Overlay (Top Left Light Source) */}
                      <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-white/40 via-transparent to-black/10 opacity-60 pointer-events-none rounded-lg"></div>
                      
                      {/* 2. Noise Texture for Realism (Brushed Metal) */}
                      <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] pointer-events-none mix-blend-overlay"></div>
                      
                      {/* 3. Bottom Reflection */}
                      <div className="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-black/10 to-transparent pointer-events-none"></div>

                      <div className="flex justify-between items-start mb-auto relative z-10">
                           <div className={`p-4 rounded-xl transition-transform duration-500 group-hover:scale-110 shadow-lg ${theme.cardIconBg}`}>
                              <Icon className="w-8 h-8" strokeWidth={2} />
                           </div>
                           <span className={`text-[10px] font-bold px-3 py-1 rounded-full uppercase backdrop-blur-md shadow-sm border-0 bg-white/30 ${theme.cardText}`}>
                              {catModules.length} Moduli
                           </span>
                      </div>

                      <div className="relative z-10 mt-6">
                        <h3 className={`text-2xl font-black mb-2 tracking-tight drop-shadow-sm ${theme.cardText}`}>
                            {cat.title}
                        </h3>
                        <p className={`text-xs font-medium leading-relaxed line-clamp-2 opacity-90 ${theme.cardMuted}`}>
                            {cat.description}
                        </p>
                      </div>

                      <div className={`mt-6 flex items-center gap-2 text-[10px] font-bold uppercase tracking-wider relative z-10 ${theme.cardText}`}>
                          Entra nel Corso <ChevronRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" strokeWidth={3} />
                      </div>
                  </button>
                );
            })}
        </div>
      </div>
    );
  }

  // --- VIEW 2: COURSE CONTENT (Standard or Full Screen) ---
  const activeCategory = categories.find(c => c.id === activeCategoryId);
  const categoryModules = modules.filter(m => m.categoryId === activeCategoryId);
  const currentModule = modules.find(m => m.id === activeModuleId);
  const currentLesson = currentModule?.lessons.find(l => l.id === activeLessonId);
  
  // *** SPECIAL THEME FOR "HQ" (PLATINUM/SILVER) - FULL SCREEN PAGE ***
  const isHQ = activeCategory?.icon === 'Brain';
  
  if (isHQ && activeCategory) {
      return (
          <div className="fixed inset-0 z-[9999] flex flex-col bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8] animate-in fade-in duration-500">
              
              {/* Minimal Top Header for Exit */}
              <div className="absolute top-6 left-6 z-50">
                  <button 
                      onClick={() => setActiveCategoryId(null)}
                      className="flex items-center gap-2 px-6 py-3 bg-white/30 hover:bg-white/50 backdrop-blur-md rounded-full text-slate-900 text-xs font-bold uppercase tracking-widest transition-all shadow-[0_4px_20px_rgba(0,0,0,0.1)] border border-white/40 hover:scale-105"
                  >
                      <ArrowLeft className="w-4 h-4" /> Torna Indietro
                  </button>
              </div>

              {/* Main Content Area - Empty as requested */}
              <div className="flex-1 flex items-center justify-center relative">
                  {/* Subtle noise texture to match the card feel */}
                  <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.15] pointer-events-none mix-blend-overlay"></div>
                  
                  {/* Placeholder for the 'Empty' state */}
                  <div className="text-center opacity-10 select-none pointer-events-none">
                      <Brain className="w-64 h-64 text-slate-900 mx-auto mb-8" strokeWidth={0.5} />
                      <h1 className="text-4xl font-black text-slate-900 uppercase tracking-[0.5em]">Mappa Organizzativa</h1>
                  </div>
              </div>
          </div>
      );
  }

  // Fallback Theme for other courses (Dark Mode Standard)
  const playerTheme = {
      bgMain: 'bg-[#000000]',
      sidebarBg: 'bg-[#111] border-r border-white/10',
      sidebarText: 'text-white',
      sidebarBorder: 'border-white/10',
      activeItemBg: 'bg-white/10 border-l-4 border-white',
      itemHover: 'hover:bg-white/5',
      headerBg: 'bg-[#0A0A0A] border-b border-white/10',
      headerText: 'text-white',
      menuButton: 'text-white hover:bg-white/10'
  };

  return (
    // Z-INDEX 9999 ensures it covers the Layout Sidebar
    <div className={`fixed inset-0 z-[9999] flex flex-col ${playerTheme.bgMain} animate-in zoom-in-95 duration-300 font-sans`}>
        
        {/* --- TOP BAR (COURSE HEADER) --- */}
        <div className={`h-16 shrink-0 flex items-center justify-between px-6 ${playerTheme.headerBg} shadow-xl relative z-20`}>
            <div className="flex items-center gap-4">
                <button 
                    onClick={() => setActiveCategoryId(null)}
                    className={`flex items-center gap-2 px-4 py-2 rounded-sm text-xs font-bold uppercase tracking-widest transition-all hover:scale-105 ${playerTheme.headerText} bg-black/5 hover:bg-black/10 border-0`}
                >
                    <ArrowLeft className="w-4 h-4" /> Torna alla Base
                </button>
                <div className="h-6 w-[1px] bg-black/10"></div>
                <div className="flex items-center gap-3">
                    {activeCategory && React.createElement(getIconForCategory(activeCategory.icon), { className: `w-5 h-5 ${playerTheme.headerText}` })}
                    <h2 className={`text-lg font-black tracking-tight uppercase ${playerTheme.headerText}`}>
                        {activeCategory?.title}
                    </h2>
                </div>
            </div>

            <div className="flex items-center gap-4">
                <button onClick={() => setSidebarOpen(!sidebarOpen)} className={`p-2 rounded transition-colors ${playerTheme.menuButton}`}>
                    {sidebarOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
                </button>
            </div>
        </div>

        {/* --- MAIN PLAYER BODY --- */}
        <div className="flex flex-1 overflow-hidden relative">
            
            {/* SIDEBAR (NAVIGATION) */}
            <div className={`
                ${sidebarOpen ? 'w-80 translate-x-0' : 'w-0 -translate-x-full opacity-0'} 
                flex flex-col shrink-0 overflow-y-auto custom-scrollbar transition-all duration-300 ease-in-out
                ${playerTheme.sidebarBg} ${playerTheme.sidebarBorder} relative z-10
            `}>
                <div className="p-6 pb-2 relative z-10">
                    <p className={`text-[10px] uppercase tracking-[0.2em] font-bold opacity-60 mb-4 border-b border-black/10 pb-2 ${playerTheme.sidebarText}`}>Programma</p>
                </div>

                <div className="space-y-1 px-2 pb-10 relative z-10">
                    {categoryModules.map(module => {
                        const isModuleActive = activeModuleId === module.id;
                        return (
                            <div key={module.id} className="mb-2">
                                {/* Module Title */}
                                <button
                                    onClick={() => setActiveModuleId(isModuleActive ? null : module.id)}
                                    className={`
                                        w-full text-left px-4 py-3 flex items-center justify-between font-bold text-xs uppercase tracking-wide rounded-sm transition-all
                                        ${isModuleActive ? 'bg-black/10 shadow-inner' : 'hover:bg-black/5'}
                                        ${playerTheme.sidebarText}
                                    `}
                                >
                                    <span className="truncate">{module.title}</span>
                                    {isModuleActive ? <ChevronDown className="w-3 h-3"/> : <ChevronRight className="w-3 h-3"/>}
                                </button>

                                {/* Lessons List */}
                                {isModuleActive && (
                                    <div className="mt-1 space-y-0.5 animate-in slide-in-from-top-2 duration-200">
                                        {module.lessons.map(lesson => {
                                            const isLessonActive = activeLessonId === lesson.id;
                                            return (
                                                <button
                                                    key={lesson.id}
                                                    onClick={() => setActiveLessonId(lesson.id)}
                                                    className={`
                                                        w-full text-left px-6 py-3 text-xs flex items-center gap-3 transition-all relative overflow-hidden group
                                                        ${isLessonActive ? playerTheme.activeItemBg : `${playerTheme.sidebarText} ${playerTheme.itemHover}`}
                                                    `}
                                                >
                                                    <div className={`w-1.5 h-1.5 rounded-full ${lesson.isCompleted ? 'bg-green-500' : 'bg-black/40'}`}></div>
                                                    <span className={`truncate flex-1 ${isLessonActive ? 'font-bold' : 'font-medium opacity-80'}`}>{lesson.title}</span>
                                                    {lesson.type === 'VIDEO' && <PlayCircle className="w-3 h-3 opacity-50"/>}
                                                </button>
                                            );
                                        })}
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>
            </div>

            {/* CONTENT AREA (RIGHT) */}
            <div className="flex-1 overflow-y-auto custom-scrollbar relative bg-[#0f172a] text-platinum-100 flex flex-col items-center">
                
                {/* Background Decor for Depth */}
                <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-white/5 via-transparent to-transparent pointer-events-none mix-blend-overlay"></div>

                {currentLesson ? (
                    <div className="max-w-4xl w-full p-12 min-h-full flex flex-col relative z-10 animate-in fade-in slide-in-from-bottom-4 duration-500">
                        
                        {/* Content Header */}
                        <div className="mb-10 pb-6 border-b border-white/10">
                            <div className="flex items-center gap-3 mb-4">
                                <span className="text-[10px] font-bold uppercase tracking-[0.2em] px-3 py-1 rounded-full border border-white/20 text-slate-300 bg-white/5">
                                    {currentModule?.title}
                                </span>
                                {currentLesson.isCompleted && (
                                    <span className="text-[10px] font-bold uppercase tracking-widest text-green-400 flex items-center gap-1 bg-green-900/20 px-2 py-1 rounded-full">
                                        <CheckCircle2 className="w-3 h-3"/> Completato
                                    </span>
                                )}
                            </div>
                            <h1 className="text-4xl font-bold text-white tracking-tight leading-tight">{currentLesson.title}</h1>
                        </div>

                        {/* Content Body (Markdown Render) */}
                        <div className="prose prose-invert prose-lg max-w-none prose-headings:text-white prose-p:text-slate-300 prose-li:text-slate-300">
                            {renderContent(currentLesson.content)}
                        </div>

                        {/* Navigation Footer */}
                        <div className="mt-20 pt-10 border-t border-white/10 flex justify-between items-center">
                            <div className="flex gap-4">
                                <Button 
                                    variant="outline" 
                                    className="border-slate-600 text-slate-400 hover:text-white"
                                    disabled
                                >
                                    Precedente
                                </Button>
                            </div>

                            {!isCreatorMode && (
                                <button 
                                    onClick={() => currentModule && onToggleLessonComplete(currentModule.id, currentLesson.id)}
                                    className={`
                                        flex items-center gap-3 px-8 py-4 rounded-sm font-bold uppercase tracking-widest transition-all shadow-lg text-xs
                                        ${currentLesson.isCompleted 
                                            ? 'bg-green-600 text-white hover:bg-green-500 shadow-green-900/20' 
                                            : `bg-gradient-to-r from-slate-200 to-white text-black hover:scale-105 hover:shadow-white/20`}
                                    `}
                                >
                                    {currentLesson.isCompleted ? 'Segna come da rivedere' : 'Completa Lezione'}
                                    <ChevronRight className="w-4 h-4" />
                                </button>
                            )}
                        </div>
                    </div>
                ) : (
                    <div className="flex flex-col items-center justify-center h-full opacity-30 select-none">
                        <MonitorPlay className="w-32 h-32 mb-6 text-white stroke-1" />
                        <p className="text-sm uppercase tracking-[0.3em] text-white font-light">Seleziona una lezione dal menu</p>
                    </div>
                )}
            </div>
        </div>
    </div>
  );
};
