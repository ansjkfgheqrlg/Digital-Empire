
import React, { useState, useEffect } from 'react';
import { Lead, LeadStage, Funnel, InfobusinessProduct, LeadActivity, Task } from '../types';
import { 
  DollarSign, User, Mail, Plus, X, Search, Kanban, List, 
  BarChart3, Clock, Briefcase, Filter, ArrowRight, CheckCircle2, 
  TrendingUp, Sparkles, MoreHorizontal, Phone, Globe, Tag, Target, Save
} from 'lucide-react';
import { Button } from './ui/Button';

interface SalesPipelineProps {
  leads: Lead[];
  funnels: Funnel[];
  products: InfobusinessProduct[];
  tasks?: Task[];
  onAddLead: (lead: Lead) => void;
  onUpdateLead: (lead: Lead) => void;
}

// STAGE CONFIGURATION WITH METALLIC ACCENTS
const STAGES = [
  { id: LeadStage.NEW, label: 'QUALIFICAZIONE', color: 'text-platinum-400', accent: 'bg-platinum-400', glow: 'shadow-platinum-400/20' },
  { id: LeadStage.CONTACTED, label: 'CONTATTATO', color: 'text-blue-300', accent: 'bg-blue-400', glow: 'shadow-blue-400/20' },
  { id: LeadStage.PROPOSAL, label: 'PROPOSTA', color: 'text-yellow-200', accent: 'bg-yellow-400', glow: 'shadow-yellow-400/20' },
  { id: LeadStage.NEGOTIATION, label: 'NEGOZIAZIONE', color: 'text-purple-300', accent: 'bg-purple-400', glow: 'shadow-purple-400/20' },
  { id: LeadStage.CLOSED_WON, label: 'CHIUSO VINTO', color: 'text-emerald-300', accent: 'bg-emerald-400', glow: 'shadow-emerald-400/20' },
];

type CrmView = 'PIPELINE' | 'DATABASE';

export const SalesPipeline: React.FC<SalesPipelineProps> = ({ leads, funnels, products, onAddLead, onUpdateLead }) => {
  const [activeView, setActiveView] = useState<CrmView>('PIPELINE');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedLead, setSelectedLead] = useState<Lead | null>(null);
  const [draggedLeadId, setDraggedLeadId] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  
  // Creation Form State
  const [newLead, setNewLead] = useState<Partial<Lead>>({
    companyName: '', contactPerson: '', email: '', phone: '', website: '', value: 0, stage: LeadStage.NEW, sourceFunnelId: '', interestedProductId: '', notes: ''
  });
  const [tagInput, setTagInput] = useState('');

  // Editing State (For Detail Modal)
  const [editValues, setEditValues] = useState<Partial<Lead>>({});

  // Sync editValues when a lead is selected
  useEffect(() => {
      if (selectedLead) {
          setEditValues({ ...selectedLead });
      }
  }, [selectedLead]);

  const totalValue = leads.reduce((acc, l) => acc + l.value, 0);
  const totalDeals = leads.length;

  // --- DRAG & DROP LOGIC ---
  const handleDragStart = (e: React.DragEvent, leadId: string) => {
    setDraggedLeadId(leadId);
    e.dataTransfer.effectAllowed = 'move';
    const el = e.target as HTMLElement;
    setTimeout(() => { el.style.opacity = '0.4'; }, 0);
  };

  const handleDragEnd = (e: React.DragEvent) => {
     const el = e.target as HTMLElement;
     el.style.opacity = '1';
     setDraggedLeadId(null);
  };

  const handleDrop = (e: React.DragEvent, stage: LeadStage) => {
    e.preventDefault();
    if (draggedLeadId) {
        const lead = leads.find(l => l.id === draggedLeadId);
        if (lead && lead.stage !== stage) {
            const updates: Partial<Lead> = { 
                stage, 
                probability: stage === 'CLOSED_WON' ? 100 : stage === 'NEGOTIATION' ? 80 : stage === 'PROPOSAL' ? 60 : lead.probability 
            };
            const activity: LeadActivity = { 
                id: `act-${Date.now()}`, 
                type: 'STATUS_CHANGE', 
                content: `Deal spostato in ${stage}`, 
                date: new Date().toISOString(), 
                author: 'Maximilian' 
            };
            updates.history = [activity, ...(lead.history || [])];
            onUpdateLead({ ...lead, ...updates });
        }
        setDraggedLeadId(null);
    }
  };

  // --- FORM SUBMIT (CREATION) ---
  const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      const tags = tagInput ? tagInput.split(',').map(t => t.trim()).filter(t => t !== '') : ['Nuovo'];
      onAddLead({
          id: `lead-${Date.now()}`,
          companyName: newLead.companyName || 'Nuova Azienda',
          contactPerson: newLead.contactPerson || 'Referente',
          email: newLead.email || '',
          phone: newLead.phone || '',
          website: newLead.website || '',
          value: Number(newLead.value),
          stage: LeadStage.NEW,
          serviceInterest: 'CONSULTING',
          lastContact: new Date().toISOString().split('T')[0],
          tags: tags,
          score: 20,
          probability: 20,
          notes: newLead.notes || '',
          sourceFunnelId: newLead.sourceFunnelId,
          interestedProductId: newLead.interestedProductId,
          history: [],
          ...newLead
      } as Lead);
      
      setIsModalOpen(false);
      setNewLead({ companyName: '', value: 0, contactPerson: '', email: '', phone: '', website: '', notes: '', sourceFunnelId: '', interestedProductId: '' });
      setTagInput('');
  };

  // --- FORM SUBMIT (EDITING) ---
  const handleSaveChanges = () => {
      if (!selectedLead || !editValues) return;
      
      const updatedLead = { ...selectedLead, ...editValues } as Lead;
      onUpdateLead(updatedLead);
      setSelectedLead(null); // Close modal on save
  };

  const filteredLeads = leads.filter(l => 
      l.companyName.toLowerCase().includes(searchTerm.toLowerCase()) || 
      l.contactPerson.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const getFunnelName = (id?: string) => funnels.find(f => f.id === id)?.name || 'N/A';
  const getProductName = (id?: string) => products.find(p => p.id === id)?.title || 'N/A';

  // --- ULTRA QUALITY METALLIC STYLING SYSTEM ---
  
  const getStageTheme = (stage: LeadStage) => {
      // CLEAN SHADOWS: No colored glow, just depth.
      const baseLayout = "rounded-sm relative overflow-hidden group hover:-translate-y-1 transition-all duration-500 cursor-grab active:cursor-grabbing border-t border-l border-b border-r";
      
      const cleanShadow = "shadow-[0_4px_6px_-1px_rgba(0,0,0,0.3)] hover:shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5)]";

      switch (stage) {
          case LeadStage.CONTACTED:
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#E0F2FE] via-[#BAE6FD] to-[#38BDF8] border-white/60 border-b-[#0284C7]/30 ${cleanShadow}`,
                  textPrimary: "text-[#0C4A6E]", 
                  textSecondary: "text-[#0284C7]",
                  iconBg: "bg-[#0EA5E9]/10 border-[#0EA5E9]/20 text-[#0369A1]",
                  barColor: "bg-[#0284C7]",
                  tag: "bg-[#F0F9FF] text-[#0369A1] border-[#BAE6FD]"
              };
          case LeadStage.PROPOSAL:
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#FFFBEB] via-[#FDE68A] to-[#D97706] border-white/60 border-b-[#B45309]/30 ${cleanShadow}`,
                  textPrimary: "text-[#451a03]",
                  textSecondary: "text-[#92400e]",
                  iconBg: "bg-[#D97706]/10 border-[#D97706]/20 text-[#92400e]",
                  barColor: "bg-[#B45309]",
                  tag: "bg-[#FFF7ED] text-[#9A3412] border-[#FED7AA]"
              };
          case LeadStage.NEGOTIATION:
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#F3E8FF] via-[#D8B4FE] to-[#9333EA] border-white/60 border-b-[#7E22CE]/30 ${cleanShadow}`,
                  textPrimary: "text-[#3B0764]",
                  textSecondary: "text-[#6B21A8]",
                  iconBg: "bg-[#9333EA]/10 border-[#9333EA]/20 text-[#6B21A8]",
                  barColor: "bg-[#7E22CE]",
                  tag: "bg-[#FAF5FF] text-[#7E22CE] border-[#E9D5FF]"
              };
          case LeadStage.CLOSED_WON:
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#ECFDF5] via-[#6EE7B7] to-[#059669] border-white/60 border-b-[#047857]/30 ${cleanShadow}`,
                  textPrimary: "text-[#022c22]",
                  textSecondary: "text-[#047857]",
                  iconBg: "bg-[#059669]/10 border-[#059669]/20 text-[#047857]",
                  barColor: "bg-[#065f46]",
                  tag: "bg-[#F0FDF4] text-[#15803d] border-[#BBF7D0]"
              };
          default: // NEW
              return {
                  card: `${baseLayout} bg-gradient-to-br from-[#F8FAFC] via-[#CBD5E1] to-[#64748B] border-white/60 border-b-[#475569]/30 ${cleanShadow}`,
                  textPrimary: "text-[#0f172a]",
                  textSecondary: "text-[#334155]",
                  iconBg: "bg-[#334155]/5 border-[#334155]/10 text-[#334155]",
                  barColor: "bg-[#334155]",
                  tag: "bg-[#F1F5F9] text-[#475569] border-[#E2E8F0]"
              };
      }
  };

  const inputClass = "w-full bg-white/70 border border-slate-300 rounded-sm p-2 text-slate-900 font-bold focus:border-slate-500 outline-none shadow-inner transition-all focus:bg-white text-sm";
  const labelClass = "text-[9px] font-bold text-slate-500 uppercase tracking-widest block mb-1";

  return (
    <div className="h-[calc(100vh-140px)] flex flex-col animate-in fade-in duration-500">
      
      {/* 1. HEADER */}
      <div className="h-20 flex items-center justify-between border-b border-white/5 pb-4 shrink-0">
          <div>
              <h1 className="text-3xl font-bold text-silver-gradient tracking-tight flex items-center gap-3">
                  Deal Flow
                  <span className="text-[10px] font-mono text-platinum-500 bg-white/5 px-2 py-1 rounded border border-white/5 tracking-widest">
                      PIPELINE VALUE: €{totalValue.toLocaleString()}
                  </span>
              </h1>
          </div>

          <div className="flex items-center gap-4">
              {/* View Toggle */}
              <div className="flex bg-[#0A0A0A] border border-white/10 rounded-sm p-1 shadow-inner">
                  {[ {id: 'PIPELINE', icon: Kanban}, {id: 'DATABASE', icon: List} ].map(view => (
                      <button 
                          key={view.id}
                          onClick={() => setActiveView(view.id as CrmView)}
                          className={`p-2 rounded-sm transition-all duration-300 ${activeView === view.id ? 'bg-gradient-to-b from-[#E2E8F0] to-[#94A3B8] text-black shadow-[0_2px_5px_rgba(0,0,0,0.2)]' : 'text-platinum-600 hover:text-white hover:bg-white/5'}`}
                      >
                          <view.icon className="w-4 h-4" />
                      </button>
                  ))}
              </div>

              {/* Search */}
              <div className="relative group">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-3 h-3 text-platinum-600 group-hover:text-white transition-colors" />
                  <input 
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      placeholder="CERCA DEAL..."
                      className="bg-[#0A0A0A] border border-white/10 rounded-sm pl-9 pr-4 py-2 text-[10px] text-white focus:border-white/40 w-48 font-bold uppercase tracking-wider placeholder:text-platinum-700 transition-all outline-none"
                  />
              </div>

              <Button variant="diamond" size="sm" onClick={() => setIsModalOpen(true)} icon={<Plus className="w-4 h-4" />}>
                  NUOVO DEAL
              </Button>
          </div>
      </div>

      {/* 2. MAIN CONTENT AREA */}
      <div className="flex-1 overflow-hidden relative mt-4">
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

          {activeView === 'PIPELINE' && (
              <div className="h-full overflow-x-auto overflow-y-hidden flex pb-4 gap-8 custom-scrollbar relative z-10 px-2">
                  {STAGES.map(stage => {
                      const stageLeads = filteredLeads.filter(l => l.stage === stage.id);
                      const stageValue = stageLeads.reduce((acc, l) => acc + l.value, 0);

                      return (
                          <div key={stage.id} className="flex-shrink-0 w-[320px] flex flex-col h-full" onDragOver={(e) => e.preventDefault()} onDrop={(e) => handleDrop(e, stage.id)}>
                              <div className="mb-6 flex items-center justify-between border-b border-white/10 pb-2 mx-1">
                                  <div className="flex items-center gap-2">
                                      <div className={`w-1.5 h-1.5 rounded-full ${stage.accent} ${stage.glow} shadow-[0_0_10px_currentColor]`}></div>
                                      <h3 className={`text-[11px] font-black tracking-[0.2em] uppercase ${stage.color}`}>{stage.label}</h3>
                                  </div>
                                  <span className="text-[9px] font-mono text-platinum-600">{stageLeads.length} / €{stageValue > 1000 ? (stageValue/1000).toFixed(0) + 'K' : stageValue}</span>
                              </div>

                              <div className="flex-1 overflow-y-auto custom-scrollbar pr-2 space-y-4 pb-10">
                                  {stageLeads.map(lead => {
                                      const theme = getStageTheme(lead.stage);
                                      return (
                                          <div
                                              key={lead.id}
                                              draggable
                                              onDragStart={(e) => handleDragStart(e, lead.id)}
                                              onDragEnd={handleDragEnd}
                                              onClick={() => setSelectedLead(lead)}
                                              className={theme.card}
                                          >
                                              <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.08] pointer-events-none mix-blend-overlay"></div>
                                              <div className="absolute top-0 right-0 w-32 h-32 bg-white/30 rounded-full blur-3xl -translate-y-10 translate-x-10 pointer-events-none group-hover:bg-white/50 transition-colors"></div>

                                              <div className="p-5 relative z-10">
                                                  <div className="flex justify-between items-start mb-3">
                                                      <h4 className={`text-sm font-black leading-tight drop-shadow-sm ${theme.textPrimary}`}>{lead.companyName}</h4>
                                                      <div className={`p-1.5 rounded-full border ${theme.iconBg}`}>
                                                          {lead.value > 5000 ? <Sparkles className="w-3 h-3" /> : <Briefcase className="w-3 h-3" />}
                                                      </div>
                                                  </div>
                                                  <div className="flex flex-col gap-1 mb-4">
                                                      <div className={`text-2xl font-black tracking-tighter ${theme.textPrimary}`}>€{lead.value.toLocaleString()}</div>
                                                      <div className={`text-[10px] font-bold uppercase tracking-wider flex items-center gap-1 ${theme.textSecondary}`}><User className="w-3 h-3"/> {lead.contactPerson}</div>
                                                  </div>
                                                  <div className="flex items-center justify-between pt-3 border-t border-black/5">
                                                      <span className={`text-[9px] font-mono font-bold ${theme.textSecondary} opacity-70`}>{new Date(lead.lastContact).toLocaleDateString(undefined, {month:'short', day:'numeric'})}</span>
                                                      <div className="flex gap-1">
                                                          {lead.tags.slice(0,2).map(t => <span key={t} className={`text-[8px] px-1.5 py-0.5 rounded border font-bold uppercase ${theme.tag}`}>{t}</span>)}
                                                      </div>
                                                  </div>
                                              </div>
                                              <div className="absolute bottom-0 left-0 w-full h-1 bg-black/10"><div className={`h-full ${theme.barColor}`} style={{width: `${lead.probability}%`}}></div></div>
                                          </div>
                                      );
                                  })}
                              </div>
                          </div>
                      );
                  })}
              </div>
          )}

          {activeView === 'DATABASE' && (
              <div className="h-full bg-[#F8FAFC] border border-white/10 rounded-sm overflow-hidden flex flex-col shadow-2xl relative">
                  <div className="grid grid-cols-12 gap-4 p-4 bg-[#E2E8F0] border-b border-slate-300 text-[10px] font-black text-slate-600 uppercase tracking-widest sticky top-0 z-10">
                      <div className="col-span-3">Company</div><div className="col-span-2">Contact</div><div className="col-span-2">Source</div><div className="col-span-1">Stage</div><div className="col-span-2 text-right">Value</div><div className="col-span-2 text-right">Updated</div>
                  </div>
                  <div className="flex-1 overflow-y-auto custom-scrollbar bg-[#F1F5F9]">
                      {filteredLeads.map(lead => (
                          <div key={lead.id} onClick={() => setSelectedLead(lead)} className="grid grid-cols-12 gap-4 p-4 border-b border-slate-200 items-center hover:bg-white transition-colors cursor-pointer group text-sm">
                              <div className="col-span-3 font-bold text-slate-900 group-hover:text-blue-600 transition-colors">{lead.companyName}</div>
                              <div className="col-span-2 text-slate-600 text-xs font-medium flex items-center gap-2">{lead.contactPerson}</div>
                              <div className="col-span-2 text-[10px] text-slate-500 font-bold uppercase">{getFunnelName(lead.sourceFunnelId)}</div>
                              <div className="col-span-1"><span className="text-[9px] font-bold uppercase px-2 py-1 rounded-sm border border-slate-300 bg-slate-100 text-slate-700">{STAGES.find(s => s.id === lead.stage)?.label.substring(0,3)}</span></div>
                              <div className="col-span-2 text-right font-mono font-bold text-slate-900">€{lead.value.toLocaleString()}</div>
                              <div className="col-span-2 text-right text-xs font-mono text-slate-500">{lead.lastContact}</div>
                          </div>
                      ))}
                  </div>
              </div>
          )}
      </div>

      {/* --- CREATION MODAL --- */}
      {isModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-md animate-in fade-in duration-200">
              <div className="bg-gradient-to-br from-[#F8FAFC] via-[#E2E8F0] to-[#CBD5E1] rounded-sm w-full max-w-xl shadow-2xl relative overflow-hidden flex flex-col max-h-[90vh]">
                  <div className="p-6 border-b border-slate-300 flex justify-between items-center bg-white/50 backdrop-blur-sm">
                      <h2 className="text-xl font-black text-slate-900 tracking-wide flex items-center gap-2"><Plus className="w-5 h-5"/> NUOVO ASSET</h2>
                      <button onClick={() => setIsModalOpen(false)}><X className="text-slate-500 hover:text-red-500 transition-colors w-5 h-5"/></button>
                  </div>

                  <div className="overflow-y-auto p-8 custom-scrollbar">
                      <form onSubmit={handleSubmit} className="space-y-6">
                          <div className="space-y-2">
                              <label className={labelClass}>Nome Azienda</label>
                              <input className={inputClass} placeholder="Inserisci nome..." value={newLead.companyName} onChange={e => setNewLead({...newLead, companyName: e.target.value})} required autoFocus />
                          </div>
                          
                          <div className="grid grid-cols-2 gap-4">
                              <div className="space-y-2">
                                  <label className={labelClass}>Referente</label>
                                  <input className={inputClass} value={newLead.contactPerson} onChange={e => setNewLead({...newLead, contactPerson: e.target.value})} required />
                              </div>
                              <div className="space-y-2">
                                  <label className={labelClass}>Valore Deal (€)</label>
                                  <input type="number" className={inputClass} value={newLead.value} onChange={e => setNewLead({...newLead, value: Number(e.target.value)})} />
                              </div>
                          </div>

                          <div className="grid grid-cols-2 gap-4">
                              <div className="space-y-2">
                                  <label className={labelClass}>Email Contatto</label>
                                  <input type="email" className={inputClass} value={newLead.email} onChange={e => setNewLead({...newLead, email: e.target.value})} />
                              </div>
                              <div className="space-y-2">
                                  <label className={labelClass}>Telefono</label>
                                  <input type="tel" className={inputClass} value={newLead.phone} onChange={e => setNewLead({...newLead, phone: e.target.value})} />
                              </div>
                          </div>

                          {/* Website Field Added Here */}
                          <div className="space-y-2">
                              <label className={labelClass}>Sito Web</label>
                              <input className={inputClass} placeholder="www.azienda.com" value={newLead.website} onChange={e => setNewLead({...newLead, website: e.target.value})} />
                          </div>

                          <div className="grid grid-cols-2 gap-4">
                              <div className="space-y-2">
                                  <label className={labelClass}>Funnel Provenienza</label>
                                  <select className={inputClass} value={newLead.sourceFunnelId} onChange={e => setNewLead({...newLead, sourceFunnelId: e.target.value})}>
                                      <option value="">-- Nessuno --</option>
                                      {funnels.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
                                  </select>
                              </div>
                              <div className="space-y-2">
                                  <label className={labelClass}>Prodotto Interesse</label>
                                  <select className={inputClass} value={newLead.interestedProductId} onChange={e => setNewLead({...newLead, interestedProductId: e.target.value})}>
                                      <option value="">-- Nessuno --</option>
                                      {products.map(p => <option key={p.id} value={p.id}>{p.title} (€{p.price})</option>)}
                                  </select>
                              </div>
                          </div>

                          <div className="space-y-2">
                              <label className={labelClass}>Note Strategiche</label>
                              <textarea className={`${inputClass} h-24 resize-none leading-relaxed`} placeholder="Dettagli aggiuntivi..." value={newLead.notes} onChange={e => setNewLead({...newLead, notes: e.target.value})} />
                          </div>

                          <Button type="submit" className="w-full py-4 mt-4 font-bold tracking-widest shadow-lg bg-slate-900 text-white hover:bg-slate-800 border-none">REGISTRA DEAL</Button>
                      </form>
                  </div>
              </div>
          </div>
      )}

      {/* --- EDITABLE LEAD DETAIL DOSSIER --- */}
      {selectedLead && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/95 backdrop-blur-md animate-in fade-in duration-200">
               <div className="w-full max-w-4xl h-[85vh] bg-gradient-to-br from-[#F8FAFC] via-[#E2E8F0] to-[#CBD5E1] rounded-sm flex flex-col shadow-2xl overflow-hidden relative">
                   
                   {/* Editable Header */}
                   <div className="p-8 border-b border-slate-300 flex justify-between items-start bg-white/50 backdrop-blur-sm">
                        <div className="flex-1 mr-8">
                            <div className="flex items-center gap-3 mb-4">
                                <span className="px-3 py-1 rounded-sm bg-slate-900 text-white text-[9px] font-bold uppercase tracking-widest shrink-0">
                                    {STAGES.find(s => s.id === editValues.stage)?.label}
                                </span>
                                <select 
                                    className="bg-transparent border border-slate-400 rounded-sm text-[10px] font-bold uppercase text-slate-700 outline-none p-1 focus:bg-white focus:border-slate-600"
                                    value={editValues.stage}
                                    onChange={(e) => setEditValues({...editValues, stage: e.target.value as LeadStage})}
                                >
                                    {STAGES.map(s => <option key={s.id} value={s.id}>{s.label}</option>)}
                                </select>
                            </div>
                            <div className="space-y-3">
                                <input 
                                    className="text-4xl font-black text-slate-900 tracking-tight bg-transparent border-b-2 border-transparent hover:border-slate-300 focus:border-slate-900 outline-none w-full transition-all placeholder:text-slate-400"
                                    value={editValues.companyName}
                                    onChange={(e) => setEditValues({...editValues, companyName: e.target.value})}
                                    placeholder="Nome Azienda"
                                />
                                <div className="flex gap-4 items-center">
                                    <User className="w-4 h-4 text-slate-500"/>
                                    <input 
                                        className="text-sm font-bold text-slate-700 bg-transparent border-b border-transparent hover:border-slate-300 focus:border-slate-900 outline-none w-64"
                                        value={editValues.contactPerson}
                                        onChange={(e) => setEditValues({...editValues, contactPerson: e.target.value})}
                                        placeholder="Nome Referente"
                                    />
                                </div>
                            </div>
                        </div>
                        <div className="flex flex-col items-end gap-3">
                            <button onClick={() => setSelectedLead(null)} className="p-2 hover:bg-slate-200 rounded-full text-slate-500 hover:text-slate-900 transition-colors">
                                <X className="w-6 h-6"/>
                            </button>
                            <Button onClick={handleSaveChanges} className="bg-slate-900 text-white hover:bg-slate-800 shadow-lg px-6 py-2" icon={<Save className="w-4 h-4"/>}>
                                SALVA MODIFICHE
                            </Button>
                        </div>
                   </div>
                   
                   <div className="flex-1 p-8 overflow-y-auto custom-scrollbar bg-white/30">
                       <div className="grid grid-cols-3 gap-8">
                           {/* Left Column: Data & Notes */}
                           <div className="col-span-2 space-y-6">
                               <div className="bg-white/60 p-6 border border-white/80 rounded-sm shadow-sm">
                                   <h3 className="text-xs font-black text-slate-800 uppercase tracking-widest mb-4 flex items-center gap-2"><Target className="w-4 h-4"/> Dettagli Strategici</h3>
                                   
                                   <div className="space-y-4">
                                       <div>
                                           <label className={labelClass}>Note & Appunti</label>
                                           <textarea 
                                               className={`${inputClass} h-32 bg-white/50 resize-none leading-relaxed text-sm`}
                                               value={editValues.notes}
                                               onChange={(e) => setEditValues({...editValues, notes: e.target.value})}
                                               placeholder="Inserisci note strategiche..."
                                           />
                                       </div>
                                       
                                       <div className="grid grid-cols-2 gap-4 pt-4 border-t border-slate-200">
                                           <div>
                                               <label className={labelClass}>Valore Deal (€)</label>
                                               <input 
                                                   type="number"
                                                   className={inputClass}
                                                   value={editValues.value}
                                                   onChange={(e) => setEditValues({...editValues, value: Number(e.target.value)})}
                                               />
                                           </div>
                                           <div>
                                               <label className={labelClass}>Origine</label>
                                               <select className={inputClass} value={editValues.sourceFunnelId} onChange={e => setEditValues({...editValues, sourceFunnelId: e.target.value})}>
                                                  <option value="">-- Nessuno --</option>
                                                  {funnels.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
                                              </select>
                                           </div>
                                       </div>
                                   </div>
                               </div>
                               
                               <div className="bg-white/60 p-6 border border-white/80 rounded-sm shadow-sm">
                                   <h3 className="text-xs font-black text-slate-800 uppercase tracking-widest mb-4 flex items-center gap-2"><Clock className="w-4 h-4"/> Timeline Attività</h3>
                                   <div className="space-y-4 border-l border-slate-300 ml-2 pl-6 relative">
                                       {selectedLead.history && selectedLead.history.map((h, i) => (
                                           <div key={i} className="relative">
                                               <div className="absolute -left-[29px] top-1.5 w-2 h-2 bg-slate-400 rounded-full border border-white"></div>
                                               <p className="text-xs text-slate-800 font-medium mb-1">{h.content}</p>
                                               <p className="text-[9px] text-slate-500 font-mono uppercase">{new Date(h.date).toLocaleString()}</p>
                                           </div>
                                       ))}
                                       {(!selectedLead.history || selectedLead.history.length === 0) && <p className="text-xs text-slate-500 italic">Nessuna attività recente.</p>}
                                   </div>
                               </div>
                           </div>
                           
                           {/* Right Column: Contact Info */}
                           <div className="col-span-1 space-y-6">
                               <div className="bg-white/60 p-4 border border-white/80 rounded-sm shadow-sm space-y-4">
                                   <h3 className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2 border-b border-slate-200 pb-2">Contatti & Web</h3>
                                   
                                   <div>
                                       <label className={labelClass}>Email</label>
                                       <div className="relative">
                                           <Mail className="absolute left-2 top-2.5 w-3 h-3 text-slate-400"/>
                                           <input className={`${inputClass} pl-7`} value={editValues.email} onChange={(e) => setEditValues({...editValues, email: e.target.value})} />
                                       </div>
                                   </div>
                                   
                                   <div>
                                       <label className={labelClass}>Telefono</label>
                                       <div className="relative">
                                           <Phone className="absolute left-2 top-2.5 w-3 h-3 text-slate-400"/>
                                           <input className={`${inputClass} pl-7`} value={editValues.phone} onChange={(e) => setEditValues({...editValues, phone: e.target.value})} />
                                       </div>
                                   </div>

                                   <div>
                                       <label className={labelClass}>Sito Web</label>
                                       <div className="relative">
                                           <Globe className="absolute left-2 top-2.5 w-3 h-3 text-slate-400"/>
                                           <input className={`${inputClass} pl-7`} value={editValues.website} onChange={(e) => setEditValues({...editValues, website: e.target.value})} placeholder="www.example.com" />
                                       </div>
                                   </div>
                               </div>

                               <div className="bg-white/60 p-4 border border-white/80 rounded-sm shadow-sm">
                                   <label className={labelClass}>Tags</label>
                                   <div className="flex flex-wrap gap-2 mb-2">
                                       {editValues.tags?.map(tag => (
                                           <span key={tag} className="text-[9px] bg-slate-100 border border-slate-200 px-2 py-1 rounded text-slate-600 font-bold uppercase flex items-center gap-1 group">
                                               <Tag className="w-2 h-2"/> {tag}
                                               <button 
                                                  onClick={() => setEditValues({...editValues, tags: editValues.tags?.filter(t => t !== tag)})}
                                                  className="ml-1 text-slate-400 hover:text-red-500"
                                               ><X className="w-2 h-2"/></button>
                                           </span>
                                       ))}
                                   </div>
                                   <input 
                                      className={`${inputClass} text-[10px]`} 
                                      placeholder="Aggiungi tag + invio"
                                      onKeyDown={(e) => {
                                          if (e.key === 'Enter') {
                                              const val = e.currentTarget.value.trim();
                                              if (val && !editValues.tags?.includes(val)) {
                                                  setEditValues({...editValues, tags: [...(editValues.tags || []), val]});
                                                  e.currentTarget.value = '';
                                              }
                                          }
                                      }}
                                   />
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
