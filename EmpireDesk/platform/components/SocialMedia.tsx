
import React, { useState } from 'react';
import { SocialPost, SocialPlatform, SocialStatus } from '../types';
import { Instagram, Video, Image, Calendar as CalendarIcon, Plus, X, List, Grid3X3, ChevronLeft, ChevronRight, Sparkles } from 'lucide-react';
import { Button } from './ui/Button';

interface SocialMediaProps {
  posts: SocialPost[];
  onAddPost: (post: SocialPost) => void;
  onUpdateStatus: (id: string, status: SocialStatus) => void;
}

export const SocialMedia: React.FC<SocialMediaProps> = ({ posts, onAddPost, onUpdateStatus }) => {
  const [viewMode, setViewMode] = useState<'LIST' | 'CALENDAR'>('LIST');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newPost, setNewPost] = useState<Partial<SocialPost>>({ title: '', platform: 'INSTAGRAM_REEL', scheduledDate: '' });
  const [isGenerating, setIsGenerating] = useState(false);
  
  // Calendar State
  const [currentDate, setCurrentDate] = useState(new Date());

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (newPost.title && newPost.scheduledDate) {
      onAddPost({
        id: `post-${Date.now()}`,
        title: newPost.title,
        platform: newPost.platform as SocialPlatform,
        status: 'IDEA',
        scheduledDate: newPost.scheduledDate,
      });
      setIsModalOpen(false);
      setNewPost({ title: '', platform: 'INSTAGRAM_REEL', scheduledDate: '' });
    }
  };

  const handleAIGenerate = () => {
      setIsGenerating(true);
      // Simulate AI delay
      setTimeout(() => {
          const topics = [
              "3 Errori da evitare nel Dropshipping",
              "Come scalare a 10k/mese con l'AI",
              "Il segreto della Vendita Subconscia",
              "Dietro le quinte dell'Agenzia",
              "Q&A Risposte alle domande frequenti"
          ];
          const randomTopic = topics[Math.floor(Math.random() * topics.length)];
          const today = new Date();
          const nextWeek = new Date(today);
          nextWeek.setDate(today.getDate() + 7);
          
          setNewPost({
              ...newPost,
              title: randomTopic,
              scheduledDate: nextWeek.toISOString().split('T')[0]
          });
          setIsGenerating(false);
      }, 1500);
  };

  const statusStyles = {
    IDEA: 'text-slate-600 border-slate-400 bg-white/50',
    SCRIPTING: 'text-blue-700 border-blue-300 bg-blue-100/50',
    EDITING: 'text-purple-700 border-purple-300 bg-purple-100/50',
    READY: 'text-yellow-700 border-yellow-300 bg-yellow-100/50',
    PUBLISHED: 'text-green-700 border-green-300 bg-green-100/50',
  };

  // Calendar Helpers
  const getDaysInMonth = (date: Date) => {
      const year = date.getFullYear();
      const month = date.getMonth();
      const firstDay = new Date(year, month, 1);
      const lastDay = new Date(year, month + 1, 0);
      const days = [];
      
      const startDay = firstDay.getDay() || 7; // 1 (Mon) - 7 (Sun)
      for(let i=1; i<startDay; i++) days.push(null);
      for(let i=1; i<=lastDay.getDate(); i++) days.push(new Date(year, month, i));
      return days;
  };

  const getPostsForDate = (date: Date) => {
      const dateStr = date.toISOString().split('T')[0];
      return posts.filter(p => p.scheduledDate === dateStr);
  };

  // COMMON STYLE FOR METALLIC MODALS
  const metallicModalClass = "bg-gradient-to-br from-[#cbd5e1] via-[#94a3b8] to-[#64748b] border-t border-l border-white/40 border-b border-r border-black/40 rounded-sm shadow-2xl relative overflow-hidden";
  const metallicInputClass = "bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner";
  const metallicLabelClass = "text-slate-800 font-bold uppercase tracking-widest text-[10px]";

  return (
    <div className="space-y-8 animate-in fade-in">
      <div className="flex justify-between items-end border-b border-white/5 pb-8">
        <div>
           <h2 className="text-4xl font-bold text-silver-gradient mb-2 tracking-tight">Social Media</h2>
           <p className="text-platinum-500 text-xs uppercase tracking-widest">Piano Editoriale Instagram</p>
        </div>
        <div className="flex gap-4">
             <div className="bg-[#0A0A0A] border border-white/10 rounded-sm p-1 flex">
                <button onClick={() => setViewMode('LIST')} className={`p-2 rounded-sm transition-colors ${viewMode === 'LIST' ? 'bg-white/10 text-white' : 'text-platinum-600 hover:text-white'}`}><List className="w-4 h-4"/></button>
                <button onClick={() => setViewMode('CALENDAR')} className={`p-2 rounded-sm transition-colors ${viewMode === 'CALENDAR' ? 'bg-white/10 text-white' : 'text-platinum-600 hover:text-white'}`}><Grid3X3 className="w-4 h-4"/></button>
             </div>
             <Button onClick={() => setIsModalOpen(true)} className="bg-white text-black hover:bg-platinum-200" icon={<Plus className="w-4 h-4"/>}>NUOVO CONTENUTO</Button>
        </div>
      </div>

      {viewMode === 'LIST' && (
          <div className="border border-white/10 rounded-sm overflow-hidden bg-[#0A0A0A]">
                <div className="grid grid-cols-12 gap-4 p-4 border-b border-white/10 bg-[#0F0F0F] text-[10px] font-bold text-platinum-500 uppercase tracking-widest">
                    <div className="col-span-1 text-center">Tipo</div>
                    <div className="col-span-5">Titolo Contenuto</div>
                    <div className="col-span-3">Data Pianificata</div>
                    <div className="col-span-3 text-right">Stato</div>
                </div>
                
                <div className="p-3 space-y-3">
                    {posts.length === 0 ? (
                        <div className="p-12 text-center text-platinum-700 text-xs uppercase tracking-widest">Nessun contenuto pianificato.</div>
                    ) : (
                        posts.map(post => (
                            <div key={post.id} className="grid grid-cols-12 gap-4 p-4 items-center bg-gradient-to-r from-[#E0F2FE] via-[#CBD5E1] to-[#94A3B8] border-t border-l border-white/50 border-b border-r border-slate-400/30 rounded-sm hover:-translate-y-0.5 transition-all shadow-md group relative overflow-hidden">
                                {/* Texture */}
                                <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.08] pointer-events-none mix-blend-overlay"></div>
                                
                                <div className="col-span-1 flex justify-center relative z-10">
                                    <div className="w-8 h-8 flex items-center justify-center bg-slate-900/10 border border-slate-900/10 rounded-sm text-slate-900">
                                        {post.platform === 'INSTAGRAM_REEL' ? <Video className="w-4 h-4"/> : <Image className="w-4 h-4"/>}
                                    </div>
                                </div>
                                <div className="col-span-5 relative z-10">
                                    <h4 className="text-sm font-black text-slate-900 drop-shadow-sm">{post.title}</h4>
                                </div>
                                <div className="col-span-3 flex items-center gap-2 text-slate-700 text-xs font-mono font-bold relative z-10">
                                    <CalendarIcon className="w-3 h-3"/> {post.scheduledDate}
                                </div>
                                <div className="col-span-3 flex justify-end relative z-10">
                                    <select 
                                        value={post.status}
                                        onChange={(e) => onUpdateStatus(post.id, e.target.value as SocialStatus)}
                                        className={`text-[10px] font-bold px-3 py-1 rounded-sm border uppercase outline-none cursor-pointer transition-colors shadow-sm ${statusStyles[post.status]}`}
                                    >
                                        <option value="IDEA" className="bg-white text-black">Idea</option>
                                        <option value="SCRIPTING" className="bg-white text-black">Scripting</option>
                                        <option value="EDITING" className="bg-white text-black">Editing</option>
                                        <option value="READY" className="bg-white text-black">Pronto</option>
                                        <option value="PUBLISHED" className="bg-white text-black">Pubblicato</option>
                                    </select>
                                </div>
                            </div>
                        ))
                    )}
                </div>
          </div>
      )}

      {viewMode === 'CALENDAR' && (
          <div className="border border-white/10 rounded-sm bg-[#0A0A0A] flex flex-col h-[600px]">
               <div className="p-4 flex justify-between items-center border-b border-white/10 bg-[#0F0F0F]">
                    <h3 className="text-lg font-bold text-white uppercase tracking-wider flex items-center gap-4">
                        <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1))} className="hover:text-silver-accent transition-colors"><ChevronLeft/></button>
                        {currentDate.toLocaleDateString('it-IT', { month: 'long', year: 'numeric' })}
                        <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1))} className="hover:text-silver-accent transition-colors"><ChevronRight/></button>
                    </h3>
               </div>
               <div className="flex-1 grid grid-cols-7 grid-rows-6 gap-[1px] bg-white/5 border-b border-white/10">
                   {['LUN', 'MAR', 'MER', 'GIO', 'VEN', 'SAB', 'DOM'].map(d => (
                       <div key={d} className="bg-[#0F0F0F] h-8 flex items-center justify-center text-[10px] font-bold text-platinum-500">{d}</div>
                   ))}
                   {getDaysInMonth(currentDate).map((date, i) => {
                       if (!date) return <div key={i} className="bg-[#0A0A0A]"></div>;
                       const dayPosts = getPostsForDate(date);
                       return (
                           <div key={i} className="bg-[#0A0A0A] p-2 hover:bg-white/5 transition-colors overflow-hidden group">
                               <div className="text-right text-[10px] text-platinum-600 mb-1 group-hover:text-white transition-colors">{date.getDate()}</div>
                               <div className="space-y-1">
                                   {dayPosts.map(p => (
                                       <div key={p.id} className={`text-[8px] px-1.5 py-1 rounded-sm truncate border flex items-center gap-1 ${p.platform === 'INSTAGRAM_REEL' ? 'bg-purple-900/20 border-purple-500/30 text-purple-300' : 'bg-blue-900/20 border-blue-500/30 text-blue-300'}`}>
                                           {p.platform === 'INSTAGRAM_REEL' ? <Video className="w-2 h-2"/> : <Image className="w-2 h-2"/>}
                                           {p.title}
                                       </div>
                                   ))}
                               </div>
                           </div>
                       );
                   })}
               </div>
          </div>
      )}

       {isModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
              <div className={`${metallicModalClass} w-full max-w-md p-8`}>
                  {/* Texture */}
                  <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>

                  <button onClick={() => setIsModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20">
                    <X className="w-6 h-6" />
                  </button>
                  <h3 className="text-2xl font-black text-slate-900 mb-8 uppercase tracking-widest relative z-10">Pianifica Contenuto</h3>
                  
                  <div className="mb-6 relative z-10">
                      <Button 
                        type="button" 
                        variant="diamond" 
                        className="w-full flex items-center justify-center gap-2 bg-slate-900 text-white border-transparent hover:bg-slate-800"
                        onClick={handleAIGenerate}
                        disabled={isGenerating}
                      >
                          <Sparkles className={`w-4 h-4 ${isGenerating ? 'animate-spin' : ''}`} />
                          {isGenerating ? 'Aureus sta pensando...' : 'Genera con Aureus'}
                      </Button>
                  </div>

                  <form onSubmit={handleSubmit} className="space-y-6 relative z-10">
                      <div className="space-y-2">
                        <label className={metallicLabelClass}>Titolo / Idea</label>
                        <input 
                            className={`${metallicInputClass} w-full p-4`}
                            placeholder="Titolo del Reel..."
                            value={newPost.title}
                            onChange={(e) => setNewPost({...newPost, title: e.target.value})}
                            required
                        />
                      </div>
                      <div className="grid grid-cols-2 gap-6">
                             <div className="space-y-2">
                                <label className={metallicLabelClass}>Formato</label>
                                <select className={`${metallicInputClass} w-full p-4`} value={newPost.platform} onChange={(e) => setNewPost({...newPost, platform: e.target.value as any})}>
                                    <option value="INSTAGRAM_REEL">Reel</option>
                                    <option value="INSTAGRAM_POST">Post</option>
                                    <option value="INSTAGRAM_STORY">Storia</option>
                                </select>
                             </div>
                             <div className="space-y-2">
                                <label className={metallicLabelClass}>Data</label>
                                <input type="date" className={`${metallicInputClass} w-full p-4`} value={newPost.scheduledDate} onChange={(e) => setNewPost({...newPost, scheduledDate: e.target.value})} required />
                             </div>
                      </div>
                      <button type="submit" className="w-full py-4 mt-4 bg-slate-900 text-white font-bold tracking-[0.2em] uppercase hover:bg-slate-800 transition-colors shadow-lg rounded-sm">
                          Crea Contenuto
                      </button>
                  </form>
              </div>
          </div>
       )}
    </div>
  );
};
