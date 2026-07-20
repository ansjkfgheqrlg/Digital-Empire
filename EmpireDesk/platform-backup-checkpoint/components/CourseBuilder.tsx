
import React, { useState } from 'react';
import { InfobusinessProduct, CourseModule, CourseLesson } from '../types';
import { Button } from './ui/Button';
import { 
  Plus, Trash2, GripVertical, ChevronDown, ChevronRight, Video, FileText, 
  HelpCircle, Save, ArrowLeft, LayoutList, MoreHorizontal, X
} from 'lucide-react';

interface CourseBuilderProps {
  product: InfobusinessProduct;
  onUpdate: (updatedProduct: InfobusinessProduct) => void;
  onBack: () => void;
}

export const CourseBuilder: React.FC<CourseBuilderProps> = ({ product, onUpdate, onBack }) => {
  const [modules, setModules] = useState<CourseModule[]>(product.modules || []);
  const [expandedModules, setExpandedModules] = useState<string[]>([]);
  const [isSaved, setIsSaved] = useState(true);

  const toggleModule = (id: string) => {
    setExpandedModules(prev => 
      prev.includes(id) ? prev.filter(m => m !== id) : [...prev, id]
    );
  };

  const addModule = () => {
    const newModule: CourseModule = {
      id: `mod-${Date.now()}`,
      title: 'Nuovo Modulo',
      status: 'PLANNED',
      lessons: []
    };
    const updated = [...modules, newModule];
    setModules(updated);
    setIsSaved(false);
    // Auto expand
    setExpandedModules(prev => [...prev, newModule.id]);
  };

  const deleteModule = (id: string) => {
    const updated = modules.filter(m => m.id !== id);
    setModules(updated);
    setIsSaved(false);
  };

  const updateModuleTitle = (id: string, title: string) => {
    setModules(modules.map(m => m.id === id ? { ...m, title } : m));
    setIsSaved(false);
  };

  const addLesson = (moduleId: string) => {
    const newLesson: CourseLesson = {
      id: `les-${Date.now()}`,
      title: 'Nuova Lezione',
      type: 'VIDEO',
      status: 'DRAFT',
      duration: '10:00'
    };
    
    setModules(modules.map(m => {
      if (m.id !== moduleId) return m;
      return { ...m, lessons: [...(m.lessons || []), newLesson] };
    }));
    setIsSaved(false);
  };

  const deleteLesson = (moduleId: string, lessonId: string) => {
    setModules(modules.map(m => {
      if (m.id !== moduleId) return m;
      return { ...m, lessons: m.lessons.filter(l => l.id !== lessonId) };
    }));
    setIsSaved(false);
  };

  const updateLesson = (moduleId: string, lessonId: string, updates: Partial<CourseLesson>) => {
    setModules(modules.map(m => {
        if (m.id !== moduleId) return m;
        return { 
            ...m, 
            lessons: m.lessons.map(l => l.id === lessonId ? { ...l, ...updates } : l) 
        };
    }));
    setIsSaved(false);
  };

  const saveChanges = () => {
    onUpdate({ ...product, modules });
    setIsSaved(true);
  };

  return (
    <div className="h-[calc(100vh-140px)] flex flex-col bg-[#050505] rounded-sm overflow-hidden border border-diamond-500/20 animate-in fade-in duration-300">
      
      {/* Header */}
      <div className="bg-[#08090A] p-4 border-b border-diamond-500/20 flex items-center justify-between shrink-0 shadow-xl z-10">
         <div className="flex items-center gap-6">
             <Button variant="outline" size="sm" onClick={onBack} className="border-diamond-500/20 text-diamond-500 hover:bg-diamond-500 hover:text-black">
                 <ArrowLeft className="w-4 h-4 mr-2" /> LISTINO
             </Button>
             <div>
                <h2 className="font-bold text-white text-sm uppercase tracking-widest">{product.title}</h2>
                <span className="text-[10px] text-diamond-500 font-mono">COURSE BUILDER • {modules.reduce((acc, m) => acc + (m.lessons?.length || 0), 0)} LEZIONI</span>
             </div>
         </div>
         <div className="flex gap-4">
             <div className="text-[10px] text-neutral-500 flex items-center font-mono uppercase">
                {isSaved ? 'Tutte le modifiche salvate' : 'Modifiche non salvate'}
             </div>
             <Button 
                variant="diamond" 
                size="sm" 
                onClick={saveChanges} 
                className={!isSaved ? 'animate-pulse' : ''}
                icon={<Save className="w-4 h-4"/>}
             >
                 SALVA STRUTTURA
             </Button>
         </div>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 overflow-y-auto custom-scrollbar p-8 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-diamond-950/10 via-[#050505] to-[#050505]">
          <div className="max-w-4xl mx-auto space-y-6">
             
             {modules.length === 0 && (
                 <div className="text-center py-20 border-2 border-dashed border-white/5 rounded-sm">
                     <LayoutList className="w-16 h-16 text-neutral-700 mx-auto mb-4" />
                     <h3 className="text-xl font-bold text-neutral-400 mb-2">Curriculum Vuoto</h3>
                     <p className="text-neutral-600 mb-6">Inizia aggiungendo il primo modulo del corso.</p>
                     <Button variant="outline" onClick={addModule} icon={<Plus className="w-4 h-4"/>}>Crea Primo Modulo</Button>
                 </div>
             )}

             {modules.map((module, index) => (
                 <div key={module.id} className="bg-[#0A0A0A] border border-white/10 rounded-sm overflow-hidden group hover:border-diamond-500/20 transition-all duration-300">
                     
                     {/* Module Header */}
                     <div className="p-4 bg-[#0F0F0F] flex items-center gap-4 cursor-pointer select-none" onClick={() => toggleModule(module.id)}>
                         <GripVertical className="w-4 h-4 text-neutral-700 cursor-grab active:cursor-grabbing hover:text-white" />
                         <button className="text-neutral-400 hover:text-white transition-colors">
                             {expandedModules.includes(module.id) ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                         </button>
                         <div className="flex-1">
                             <input 
                                onClick={(e) => e.stopPropagation()}
                                className="bg-transparent border-none p-0 text-sm font-bold text-white uppercase tracking-wider w-full focus:ring-0 placeholder:text-neutral-600"
                                value={module.title}
                                onChange={(e) => updateModuleTitle(module.id, e.target.value)}
                                placeholder="Titolo Modulo"
                             />
                         </div>
                         <div className="flex items-center gap-4">
                             <div className="px-2 py-0.5 rounded-sm bg-neutral-900 border border-white/5 text-[9px] font-bold text-neutral-500 uppercase">
                                 {module.lessons?.length || 0} Lezioni
                             </div>
                             <div className="h-4 w-[1px] bg-white/10"></div>
                             <button onClick={(e) => { e.stopPropagation(); deleteModule(module.id); }} className="text-neutral-600 hover:text-red-500 transition-colors">
                                 <Trash2 className="w-4 h-4" />
                             </button>
                         </div>
                     </div>

                     {/* Lessons Area */}
                     {expandedModules.includes(module.id) && (
                         <div className="p-4 bg-[#050505] space-y-2 border-t border-white/5">
                             {module.lessons?.map((lesson, lIndex) => (
                                 <div key={lesson.id} className="flex items-center gap-3 p-3 bg-[#0A0A0A] border border-white/5 rounded-sm hover:border-white/10 transition-colors group/lesson">
                                     <div className="w-6 flex justify-center"><div className="w-1.5 h-1.5 bg-neutral-700 rounded-full group-hover/lesson:bg-diamond-500 transition-colors"></div></div>
                                     <div className="w-8 flex justify-center">
                                         {lesson.type === 'VIDEO' && <Video className="w-4 h-4 text-blue-400" />}
                                         {lesson.type === 'TEXT' && <FileText className="w-4 h-4 text-neutral-400" />}
                                         {lesson.type === 'QUIZ' && <HelpCircle className="w-4 h-4 text-yellow-400" />}
                                     </div>
                                     <input 
                                         className="flex-1 bg-transparent border-none text-xs text-neutral-300 focus:text-white p-0"
                                         value={lesson.title}
                                         onChange={(e) => updateLesson(module.id, lesson.id, { title: e.target.value })}
                                     />
                                     
                                     {/* Controls */}
                                     <div className="flex items-center gap-3 opacity-0 group-hover/lesson:opacity-100 transition-opacity">
                                         <select 
                                            className="bg-[#111] border border-white/10 text-[9px] text-neutral-400 rounded-sm px-2 py-1 outline-none uppercase font-bold"
                                            value={lesson.type}
                                            onChange={(e) => updateLesson(module.id, lesson.id, { type: e.target.value as any })}
                                         >
                                             <option value="VIDEO">Video</option>
                                             <option value="TEXT">Testo</option>
                                             <option value="QUIZ">Quiz</option>
                                         </select>
                                         <select 
                                            className={`bg-[#111] border border-white/10 text-[9px] rounded-sm px-2 py-1 outline-none uppercase font-bold ${lesson.status === 'PUBLISHED' ? 'text-green-400' : 'text-neutral-500'}`}
                                            value={lesson.status}
                                            onChange={(e) => updateLesson(module.id, lesson.id, { status: e.target.value as any })}
                                         >
                                             <option value="DRAFT">Bozza</option>
                                             <option value="RECORDED">Registrato</option>
                                             <option value="PUBLISHED">Pubblico</option>
                                         </select>
                                         <button onClick={() => deleteLesson(module.id, lesson.id)} className="text-neutral-600 hover:text-red-500">
                                             <X className="w-3 h-3" />
                                         </button>
                                     </div>
                                 </div>
                             ))}
                             
                             <button 
                                onClick={() => addLesson(module.id)}
                                className="w-full py-2 border border-dashed border-white/10 rounded-sm text-[10px] text-neutral-500 font-bold uppercase hover:bg-white/5 hover:text-diamond-400 transition-all flex items-center justify-center gap-2"
                             >
                                 <Plus className="w-3 h-3" /> Aggiungi Lezione
                             </button>
                         </div>
                     )}
                 </div>
             ))}

             <div className="pt-6 flex justify-center">
                 <Button variant="outline" onClick={addModule} className="border-diamond-500/20 text-diamond-500 hover:text-black hover:bg-diamond-500" icon={<Plus className="w-4 h-4"/>}>
                     AGGIUNGI NUOVO MODULO
                 </Button>
             </div>
          </div>
      </div>
    </div>
  );
};
