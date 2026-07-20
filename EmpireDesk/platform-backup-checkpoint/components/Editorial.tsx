
import React, { useState } from 'react';
import { EditorialItem, EditorialType } from '../types';
import { BookOpen, FileText, CheckCircle, Plus, X, Sparkles } from 'lucide-react';
import { Button } from './ui/Button';

interface EditorialProps {
  items: EditorialItem[];
  onAddItem: (item: EditorialItem) => void;
  onUpdateStatus: (id: string, status: any) => void;
}

export const Editorial: React.FC<EditorialProps> = ({ items, onAddItem, onUpdateStatus }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newItem, setNewItem] = useState({ title: '', type: 'BOOK_CHAPTER' });
  const [isGenerating, setIsGenerating] = useState(false);

  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();
    onAddItem({
      id: `ed-${Date.now()}`,
      title: newItem.title,
      type: newItem.type as EditorialType,
      status: 'DRAFT',
      wordCount: 0
    });
    setIsModalOpen(false);
    setNewItem({ title: '', type: 'BOOK_CHAPTER' });
  };

  const handleAIGenerate = () => {
      setIsGenerating(true);
      setTimeout(() => {
          const titles = [
              "Capitolo 1: I Fondamenti della Persuasione",
              "Introduzione al Deep Work per CEO",
              "Caso Studio: Da 0 a 1M in 12 Mesi",
              "La Psicologia dei Prezzi High Ticket",
              "Bonus: 50 Hook per Viralità Immediata"
          ];
          setNewItem({
              ...newItem,
              title: titles[Math.floor(Math.random() * titles.length)]
          });
          setIsGenerating(false);
      }, 1200);
  };

  const getTypeLabel = (type: string) => {
      switch(type) {
          case 'BOOK_CHAPTER': return 'Capitolo Libro';
          case 'PDF_MAGNET': return 'PDF / Magnet';
          default: return 'Articolo';
      }
  };

  // COMMON STYLE FOR METALLIC MODALS
  const metallicModalClass = "bg-gradient-to-br from-[#cbd5e1] via-[#94a3b8] to-[#64748b] border-t border-l border-white/40 border-b border-r border-black/40 rounded-sm shadow-2xl relative overflow-hidden";
  const metallicInputClass = "bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner";
  const metallicLabelClass = "text-slate-800 font-bold uppercase tracking-widest text-[10px]";

  // CARD STYLE: AZURE SILVER METALLIC
  const silverCardClass = "group p-6 rounded-sm bg-gradient-to-br from-[#E0F2FE] via-[#CBD5E1] to-[#64748B] border-t border-l border-white/60 border-b border-r border-slate-600/40 hover:-translate-y-1 hover:shadow-[0_10px_20px_rgba(0,0,0,0.2)] transition-all duration-300 shadow-xl relative overflow-hidden";

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <div className="flex justify-between items-end border-b border-white/5 pb-8">
        <div>
           <h2 className="text-4xl font-bold text-silver-gradient mb-2 tracking-tight">Editoriale</h2>
           <p className="text-platinum-500 text-xs uppercase tracking-widest">Produzione Contenuti Scritturale</p>
        </div>
        <Button onClick={() => setIsModalOpen(true)} className="bg-white text-black hover:bg-platinum-200" icon={<Plus className="w-4 h-4"/>}>NUOVO PROGETTO</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {['DRAFT', 'REVIEW', 'EDITING', 'COMPLETED'].map((status) => (
             <div key={status} className="bg-transparent">
                <div className="flex justify-between items-center mb-6 border-b border-white/10 pb-2">
                    <h3 className="text-[10px] font-bold text-platinum-400 uppercase tracking-[0.2em]">{status}</h3>
                    <span className="text-[10px] text-platinum-600 font-mono">
                        {items.filter(i => i.status === status).length}
                    </span>
                </div>
                <div className="space-y-4">
                    {items.filter(i => i.status === status).map(item => (
                        <div 
                            key={item.id} 
                            className={silverCardClass}
                        >
                            {/* Realistic Noise & Shine Texture */}
                            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>
                            <div className="absolute top-0 right-0 w-32 h-32 bg-white/30 rounded-full blur-3xl -translate-y-10 translate-x-10 pointer-events-none group-hover:bg-white/40 transition-colors"></div>

                            <div className="flex justify-between items-start mb-4 relative z-10">
                                <span className="text-[9px] uppercase tracking-wider text-slate-800 font-bold border border-slate-900/10 bg-slate-900/5 px-2 py-1 rounded-sm">
                                    {getTypeLabel(item.type)}
                                </span>
                                {status !== 'COMPLETED' && (
                                    <button onClick={() => onUpdateStatus(item.id, 'COMPLETED')} className="text-slate-600 hover:text-emerald-700 transition-colors bg-white/20 p-1 rounded-full">
                                        <CheckCircle className="w-4 h-4" />
                                    </button>
                                )}
                            </div>
                            
                            <h4 className="text-sm font-black text-slate-900 leading-snug mb-4 drop-shadow-sm relative z-10">
                                {item.title}
                            </h4>
                            
                            <div className="h-[1px] w-full bg-slate-900/10 group-hover:bg-slate-900/20 transition-colors relative z-10"></div>
                            
                            {/* Optional Footer Metadata */}
                            {item.wordCount ? (
                                <div className="mt-3 text-[9px] font-mono text-slate-700 font-bold text-right relative z-10">
                                    {item.wordCount} parole
                                </div>
                            ) : null}
                        </div>
                    ))}
                    {items.filter(i => i.status === status).length === 0 && (
                        <div className="h-24 border border-dashed border-white/5 rounded-sm flex items-center justify-center">
                            <span className="text-[9px] text-platinum-800 uppercase tracking-widest">Vuoto</span>
                        </div>
                    )}
                </div>
             </div>
          ))}
      </div>

      {isModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
             <div className={`${metallicModalClass} p-10 w-full max-w-md`}>
                 {/* Texture */}
                 <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>

                 <button onClick={() => setIsModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20">
                    <X className="w-6 h-6" />
                 </button>
                 
                 <h3 className="text-2xl font-black text-slate-900 mb-8 uppercase tracking-widest relative z-10">Aggiungi Elemento</h3>
                 
                 <div className="mb-6 relative z-10">
                      <Button 
                        type="button" 
                        variant="diamond" 
                        className="w-full flex items-center justify-center gap-2 bg-slate-900 text-white border-transparent hover:bg-slate-800"
                        onClick={handleAIGenerate}
                        disabled={isGenerating}
                      >
                          <Sparkles className={`w-4 h-4 ${isGenerating ? 'animate-spin' : ''}`} />
                          {isGenerating ? 'Aureus sta ideando...' : 'Genera con Aureus'}
                      </Button>
                  </div>

                 <form onSubmit={handleAdd} className="space-y-6 relative z-10">
                     <div className="space-y-2">
                        <label className={metallicLabelClass}>Titolo</label>
                        <input 
                            className={`${metallicInputClass} w-full p-4`} 
                            placeholder="Titolo del capitolo o articolo..." 
                            value={newItem.title} 
                            onChange={e => setNewItem({...newItem, title: e.target.value})} 
                            required 
                        />
                     </div>
                     <div className="space-y-2">
                        <label className={metallicLabelClass}>Tipologia</label>
                        <select 
                            className={`${metallicInputClass} w-full p-4`} 
                            value={newItem.type} 
                            onChange={e => setNewItem({...newItem, type: e.target.value})}
                        >
                            <option value="BOOK_CHAPTER">Capitolo Libro</option>
                            <option value="PDF_MAGNET">PDF / E-book</option>
                            <option value="ARTICLE">Articolo</option>
                        </select>
                     </div>
                     <button type="submit" className="w-full py-4 mt-4 bg-slate-900 text-white font-bold tracking-[0.2em] uppercase hover:bg-slate-800 transition-colors shadow-lg rounded-sm">
                         Salva Progetto
                     </button>
                 </form>
             </div>
          </div>
      )}
    </div>
  );
};
