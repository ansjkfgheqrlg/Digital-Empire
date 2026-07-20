
import React, { useState } from 'react';
import { InfobusinessProduct, Funnel, ProductCategory, ServiceType } from '../types';
import { MonitorPlay, Plus, Video, Box, ArrowRight, X, Briefcase, Bot, Smartphone, Edit3, TrendingUp, Layers, MousePointer } from 'lucide-react';
import { Button } from './ui/Button';
import { FunnelBuilder } from './FunnelBuilder';
import { CourseBuilder } from './CourseBuilder';

interface InfobusinessProps {
  products: InfobusinessProduct[];
  funnels: Funnel[];
  onAddProduct: (prod: InfobusinessProduct) => void;
  onAddFunnel: (funnel: Funnel) => void;
  onUpdateFunnel: (funnel: Funnel) => void;
}

type ViewMode = 'DASHBOARD' | 'FUNNELS' | 'PRODUCTS' | 'FUNNEL_EDITOR' | 'COURSE_EDITOR';
type ProductFilter = 'ALL' | 'AGENCY' | 'INFO';

export const Infobusiness: React.FC<InfobusinessProps> = ({ 
    products, funnels, onAddProduct, onAddFunnel, onUpdateFunnel 
}) => {
  const [view, setView] = useState<ViewMode>('DASHBOARD');
  const [prodFilter, setProdFilter] = useState<ProductFilter>('ALL');
  const [editingFunnelId, setEditingFunnelId] = useState<string | null>(null);
  const [editingProductId, setEditingProductId] = useState<string | null>(null);
  
  // Modal States
  const [isFunnelModalOpen, setIsFunnelModalOpen] = useState(false);
  const [isProdModalOpen, setIsProdModalOpen] = useState(false);
  
  // Form States
  const [newFunnelName, setNewFunnelName] = useState('');
  const [newProduct, setNewProduct] = useState<{
      title: string; 
      price: string; 
      category: ProductCategory; 
      serviceType: ServiceType
  }>({
      title: '',
      price: '',
      category: 'INFO',
      serviceType: 'CONSULTING'
  });

  const handleCreateFunnel = (e: React.FormEvent) => {
      e.preventDefault();
      onAddFunnel({
          id: `funnel-${Date.now()}`,
          name: newFunnelName,
          status: 'DRAFT',
          steps: [{ 
              id: 'start', 
              type: 'LANDING', 
              label: 'Landing Page', 
              x: 100, y: 100, 
              metrics: { trafficIn: 0, conversionRate: 0, trafficOut: 0, revenue: 0, cost: 0, profit: 0 },
              config: {}
          }],
          connections: []
      });
      setIsFunnelModalOpen(false);
      setNewFunnelName('');
  };

  const handleCreateProduct = (e: React.FormEvent) => {
      e.preventDefault();
      onAddProduct({
          id: `prod-${Date.now()}`,
          title: newProduct.title,
          price: Number(newProduct.price),
          sales: 0,
          modules: [],
          category: newProduct.category,
          serviceType: newProduct.category === 'AGENCY' ? newProduct.serviceType : undefined
      });
      setIsProdModalOpen(false);
      setNewProduct({ title: '', price: '', category: 'INFO', serviceType: 'CONSULTING' });
  };

  const openFunnelEditor = (funnelId: string) => {
      setEditingFunnelId(funnelId);
      setView('FUNNEL_EDITOR');
  };

  const openCourseEditor = (productId: string) => {
      setEditingProductId(productId);
      setView('COURSE_EDITOR');
  };

  const handleUpdateProduct = (updatedProduct: InfobusinessProduct) => {
      console.log("Saving product structure:", updatedProduct);
  };

  // Derived Metrics
  const infoRevenue = products
    .filter(p => p.category !== 'AGENCY')
    .reduce((acc, curr) => acc + (Number(curr.sales) * Number(curr.price)), 0);
    
  const agencyRevenue = products
    .filter(p => p.category === 'AGENCY')
    .reduce((acc, curr) => acc + (Number(curr.sales) * Number(curr.price)), 0);

  const filteredProducts = products.filter(p => {
      if (prodFilter === 'ALL') return true;
      if (prodFilter === 'AGENCY') return p.category === 'AGENCY';
      return p.category !== 'AGENCY'; // INFO or undefined (legacy)
  });

  const getServiceIcon = (type?: ServiceType) => {
      switch(type) {
          case 'WEBSITE': return <Box className="w-5 h-5"/>;
          case 'AUTOMATION': return <Bot className="w-5 h-5"/>;
          case 'SOCIAL_GROWTH': return <Smartphone className="w-5 h-5"/>;
          default: return <Briefcase className="w-5 h-5"/>;
      }
  };

  if (view === 'FUNNEL_EDITOR' && editingFunnelId) {
      const activeFunnel = funnels.find(f => f.id === editingFunnelId);
      if (!activeFunnel) return <div>Errore</div>;
      return <FunnelBuilder funnel={activeFunnel} onUpdate={onUpdateFunnel} onBack={() => setView('FUNNELS')} />;
  }

  if (view === 'COURSE_EDITOR' && editingProductId) {
      const activeProduct = products.find(p => p.id === editingProductId);
      if (!activeProduct) return <div>Errore</div>;
      return <CourseBuilder product={activeProduct} onUpdate={handleUpdateProduct} onBack={() => setView('PRODUCTS')} />;
  }

  // --- METALLIC THEME SYSTEM ---
  
  // AZURE SILVER METALLIC STYLE (Previously used in DashboardHome, now moved here)
  // Gradient from Ice Blue (#D6E6F2) -> Azure Silver (#94BBD9) -> Steel Blue (#5D8AA8)
  const azureSilverBlock = "bg-gradient-to-br from-[#D6E6F2] via-[#94BBD9] to-[#5D8AA8] border-t border-l border-white/50 border-b border-r border-[#466D87]/50 shadow-2xl relative overflow-hidden group transition-all duration-300";
  const azureTextMain = "text-[#0B1621]"; // Midnight Metal for contrast
  const azureTextSub = "text-[#1F3A4D]"; // Dark Blue-ish Slate

  // Common Texture Overlay
  const MetallicTexture = () => (
      <>
        <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.12] pointer-events-none mix-blend-overlay"></div>
        <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-[0.15] rounded-full blur-3xl -translate-y-10 translate-x-10 group-hover:opacity-[0.25] transition-opacity pointer-events-none"></div>
        <div className="absolute bottom-0 left-0 w-full h-1/3 bg-gradient-to-t from-[#0B1621]/10 to-transparent pointer-events-none"></div>
      </>
  );

  // --- DYNAMIC PRODUCT STYLING ---
  // Calculates rank based on price to assign specific metallic themes
  const sortedUniquePrices = Array.from(new Set(filteredProducts.map(p => Number(p.price)))).sort((a: number, b: number) => a - b);

  const getProductThemeKey = (price: number) => {
      const rank = sortedUniquePrices.indexOf(price);
      const total = sortedUniquePrices.length;
      
      // If only 1 product -> Silver
      if (total === 1) return 'SILVER';
      
      // Lowest Price -> Standard Silver
      if (rank === 0) return 'SILVER';
      
      // Highest Price -> Gold
      if (rank === total - 1) return 'GOLD';
      
      // Middle Prices -> Purple
      return 'PURPLE';
  };

  const THEMES = {
      SILVER: {
          block: "bg-gradient-to-br from-[#F1F5F9] via-[#CBD5E1] to-[#64748B] border-white/60",
          textMain: "text-slate-900",
          textSub: "text-slate-700",
          iconBg: "bg-slate-900/5 border border-slate-900/10 text-slate-900",
          pill: "bg-white/40 text-slate-800 border border-white/50 shadow-sm",
          button: "border border-slate-900/20 text-slate-900 hover:bg-slate-900 hover:text-white"
      },
      PURPLE: {
          // Amethyst Silver: Metallic Purple
          block: "bg-gradient-to-br from-[#F3E8FF] via-[#D8B4FE] to-[#7E22CE] border-purple-200/50",
          textMain: "text-[#3B0764]", // Deep Indigo
          textSub: "text-[#581C87]",
          iconBg: "bg-[#581C87]/10 border border-[#581C87]/20 text-[#581C87]",
          pill: "bg-white/40 text-[#4C1D95] border border-white/50 shadow-sm",
          button: "border border-[#581C87]/20 text-[#581C87] hover:bg-[#581C87] hover:text-[#F3E8FF]"
      },
      GOLD: {
          // Champagne Gold: Metallic Gold
          block: "bg-gradient-to-br from-[#FFFBEB] via-[#FCD34D] to-[#B45309] border-yellow-200/50",
          textMain: "text-[#451a03]", // Deep Bronze
          textSub: "text-[#78350f]",
          iconBg: "bg-[#78350f]/10 border border-[#78350f]/20 text-[#78350f]",
          pill: "bg-white/40 text-[#451a03] border border-white/50 shadow-sm",
          button: "border border-[#78350f]/20 text-[#78350f] hover:bg-[#78350f] hover:text-white"
      }
  };

  return (
    <div className="space-y-10 animate-in fade-in duration-500">
      
      {/* Tab Navigation - AZURE SILVER BUTTONS */}
      <div className="flex flex-wrap gap-4">
          {['DASHBOARD', 'FUNNELS', 'PRODUCTS'].map(v => (
             <button 
                key={v}
                onClick={() => setView(v as ViewMode)}
                className={`
                    px-8 py-3 rounded-sm text-[10px] font-bold uppercase tracking-[0.2em] transition-all duration-300
                    border relative overflow-hidden
                    ${view === v 
                        ? `${azureSilverBlock} ${azureTextMain} border-white/50 shadow-lg scale-105` 
                        : 'bg-transparent text-neutral-500 border-white/10 hover:text-white hover:bg-white/5 hover:border-white/20'}
                `}
             >
                {view === v && <div className="absolute inset-0 bg-white/20 mix-blend-overlay"></div>}
                {v}
             </button>
          ))}
      </div>

      {view === 'DASHBOARD' && (
          <div className="space-y-6">
               <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                   {/* Card 1: Agency Services Revenue */}
                   <div className={`${azureSilverBlock} p-8 rounded-sm`}>
                       <MetallicTexture />
                       <h3 className={`${azureTextSub} text-[10px] font-bold uppercase tracking-[0.2em] mb-4 flex items-center gap-2 relative z-10`}>
                           <div className="p-1.5 rounded-full bg-[#0B1621]/10"><Briefcase className={`w-3 h-3 ${azureTextMain}`} /></div>
                           Entrate Servizi
                       </h3>
                       <p className={`text-4xl font-black ${azureTextMain} tracking-tighter relative z-10`}>€{agencyRevenue.toLocaleString()}</p>
                       <div className="mt-4 h-1 w-full bg-[#0B1621]/10 rounded-full overflow-hidden relative z-10">
                           <div className="h-full bg-[#0B1621] w-2/3"></div>
                       </div>
                   </div>
                   
                   {/* Card 2: Info Products Revenue */}
                   <div className={`${azureSilverBlock} p-8 rounded-sm`}>
                       <MetallicTexture />
                       <h3 className={`${azureTextSub} text-[10px] font-bold uppercase tracking-[0.2em] mb-4 flex items-center gap-2 relative z-10`}>
                           <div className="p-1.5 rounded-full bg-[#0B1621]/10"><MonitorPlay className={`w-3 h-3 ${azureTextMain}`} /></div>
                           Entrate Info
                       </h3>
                       <p className={`text-4xl font-black ${azureTextMain} tracking-tighter relative z-10`}>€{infoRevenue.toLocaleString()}</p>
                       <div className="mt-4 h-1 w-full bg-[#0B1621]/10 rounded-full overflow-hidden relative z-10">
                           <div className="h-full bg-[#0B1621] w-1/3"></div>
                       </div>
                   </div>

                   {/* Card 3: Active Funnels */}
                   <div className={`${azureSilverBlock} p-8 rounded-sm`}>
                       <MetallicTexture />
                       <h3 className={`${azureTextSub} text-[10px] font-bold uppercase tracking-[0.2em] mb-4 flex items-center gap-2 relative z-10`}>
                            <div className="p-1.5 rounded-full bg-[#0B1621]/10"><Layers className={`w-3 h-3 ${azureTextMain}`} /></div>
                            Funnels Attivi
                       </h3>
                       <p className={`text-4xl font-black ${azureTextMain} tracking-tighter relative z-10`}>{funnels.length}</p>
                       <div className="mt-4 flex items-center gap-2 text-[9px] font-bold text-[#1F3A4D] relative z-10">
                           <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
                           SYSTEM OPERATIONAL
                       </div>
                   </div>
               </div>
               
               {/* Hero Banner - Azure Silver */}
               <div className={`${azureSilverBlock} p-12 rounded-sm flex flex-col items-center justify-center text-center`}>
                    <MetallicTexture />
                    <div className="p-4 rounded-full bg-[#0B1621]/10 border border-[#0B1621]/5 mb-6 shadow-inner relative z-10 backdrop-blur-sm">
                        <MonitorPlay className={`w-8 h-8 ${azureTextMain}`} />
                    </div>
                    <h2 className={`text-3xl font-black ${azureTextMain} mb-2 tracking-wide relative z-10`}>Centro Infobusiness & Servizi</h2>
                    <p className={`${azureTextSub} text-sm max-w-md relative z-10 font-medium`}>Gestisci l'ecosistema digitale, dividendo i servizi d'agenzia dai prodotti scalabili.</p>
               </div>
          </div>
      )}

      {view === 'FUNNELS' && (
          <div className="space-y-8">
              <div className="flex justify-between items-end border-b border-white/5 pb-4">
                  <h2 className="text-3xl font-bold text-white tracking-tight">Funnel Attivi</h2>
                  <Button onClick={() => setIsFunnelModalOpen(true)} className="bg-white text-black font-bold hover:bg-platinum-200 shadow-lg" icon={<Plus className="w-4 h-4" />}>NUOVO FUNNEL</Button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {funnels.map(funnel => (
                      <div key={funnel.id} className={`${azureSilverBlock} p-8 rounded-sm hover:-translate-y-1`}>
                          <MetallicTexture />
                          
                          <div className="flex justify-between items-start mb-6 relative z-10">
                              <h3 className={`text-xl font-black ${azureTextMain}`}>{funnel.name}</h3>
                              <span className="text-[9px] font-bold text-[#0B1621] bg-white/40 border border-white/60 px-2 py-0.5 rounded-sm uppercase tracking-wider shadow-sm">
                                {funnel.status}
                              </span>
                          </div>
                          
                          <div className={`flex gap-4 text-xs ${azureTextSub} mb-8 font-mono font-bold relative z-10`}>
                              <div className="flex items-center gap-2"><Box className={`w-3 h-3 ${azureTextMain}`}/> {funnel.steps.length} STEPS</div>
                          </div>

                          <button 
                            onClick={() => openFunnelEditor(funnel.id)} 
                            className="w-full py-3 bg-[#0B1621] text-white font-bold uppercase tracking-widest text-[10px] rounded-sm hover:bg-[#162a3f] transition-colors shadow-lg flex items-center justify-center gap-2 relative z-10"
                          >
                              Apri Mappa <ArrowRight className="w-3 h-3" />
                          </button>
                      </div>
                  ))}
              </div>
          </div>
      )}

      {view === 'PRODUCTS' && (
          <div className="space-y-8">
              <div className="flex justify-between items-end border-b border-white/5 pb-4">
                <div>
                    <h2 className="text-3xl font-bold text-white tracking-tight mb-4">Listino Prodotti</h2>
                    <div className="flex gap-2">
                         <button onClick={() => setProdFilter('ALL')} className={`text-[10px] font-bold uppercase px-3 py-1 rounded-sm border ${prodFilter === 'ALL' ? 'bg-white text-black border-white' : 'border-white/10 text-neutral-500 hover:text-white'}`}>Tutti</button>
                         <button onClick={() => setProdFilter('AGENCY')} className={`text-[10px] font-bold uppercase px-3 py-1 rounded-sm border ${prodFilter === 'AGENCY' ? 'bg-white text-black border-white' : 'border-white/10 text-neutral-500 hover:text-white'}`}>Servizi Agenzia</button>
                         <button onClick={() => setProdFilter('INFO')} className={`text-[10px] font-bold uppercase px-3 py-1 rounded-sm border ${prodFilter === 'INFO' ? 'bg-white text-black border-white' : 'border-white/10 text-neutral-500 hover:text-white'}`}>Infobusiness</button>
                    </div>
                </div>
                <Button onClick={() => setIsProdModalOpen(true)} className="bg-white text-black font-bold hover:bg-platinum-200 shadow-lg" icon={<Plus className="w-4 h-4"/>}>NUOVO PRODOTTO</Button>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {filteredProducts.map(prod => {
                    const themeKey = getProductThemeKey(prod.price);
                    const styles = THEMES[themeKey];

                    return (
                        <div key={prod.id} className={`${styles.block} border-t border-l border-b border-r shadow-2xl relative overflow-hidden group transition-all duration-300 p-6 rounded-sm hover:-translate-y-1 flex flex-col h-full`}>
                            <MetallicTexture />
                            
                            <div className="flex justify-between items-start mb-4 relative z-10">
                                <div className={`p-2 rounded-sm ${styles.iconBg}`}>
                                    {prod.category === 'AGENCY' ? getServiceIcon(prod.serviceType) : <Video className="w-5 h-5" />}
                                </div>
                                <span className={`text-2xl font-black ${styles.textMain} tracking-tighter`}>€{prod.price.toLocaleString()}</span>
                            </div>
                            
                            <h3 className={`text-lg font-bold ${styles.textMain} mb-2 relative z-10 leading-tight`}>{prod.title}</h3>
                            
                            <div className="flex justify-between items-center text-[10px] mt-2 mb-6 font-mono font-bold relative z-10">
                                 <span className={styles.textSub}>VENDITE: {prod.sales}</span>
                                 <span className={`px-2 py-0.5 rounded-sm uppercase tracking-wider ${styles.pill}`}>
                                    {prod.category === 'AGENCY' ? 'SERVIZIO' : 'CORSO'}
                                 </span>
                            </div>
                            
                            {prod.category !== 'AGENCY' && (
                                <div className="mt-auto relative z-10">
                                    <button 
                                        onClick={() => openCourseEditor(prod.id)} 
                                        className={`w-full py-2 text-[10px] font-bold uppercase tracking-widest rounded-sm transition-colors flex items-center justify-center gap-2 ${styles.button}`}
                                    >
                                        <Edit3 className="w-3 h-3" /> Gestisci Contenuti
                                    </button>
                                </div>
                            )}
                        </div>
                    );
                })}
              </div>
          </div>
      )}

      {/* Modals - Azure Silver Style */}
      {isFunnelModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm">
             <div className={`${azureSilverBlock} w-full max-w-md p-10 !border-white/80`}>
                 <MetallicTexture />

                 <button onClick={() => setIsFunnelModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20"><X className="w-5 h-5"/></button>
                 <h3 className={`text-2xl font-black ${azureTextMain} mb-8 uppercase tracking-widest flex items-center gap-2 relative z-10`}>
                     <span className="w-2 h-2 bg-[#0B1621] rounded-full"></span>
                     Nuovo Funnel
                 </h3>
                 <form onSubmit={handleCreateFunnel} className="space-y-6 relative z-10">
                     <div className="space-y-2">
                         <label className="text-xs font-bold text-slate-800 uppercase tracking-widest">Nome Progetto</label>
                         <input 
                            className="w-full bg-[#0B1621] border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner p-4"
                            placeholder="Funnel lancio..." 
                            value={newFunnelName} 
                            onChange={e => setNewFunnelName(e.target.value)} 
                            required 
                        />
                     </div>
                     <Button type="submit" className="w-full py-4 tracking-widest font-bold text-white bg-[#0B1621] hover:bg-[#162a3f] shadow-xl transition-colors border-none">INIZIALIZZA</Button>
                 </form>
             </div>
          </div>
      )}
      
      {isProdModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm">
             <div className={`${azureSilverBlock} w-full max-w-md p-10 !border-white/80`}>
                 <MetallicTexture />

                 <button onClick={() => setIsProdModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20"><X className="w-5 h-5"/></button>
                 <h3 className={`text-2xl font-black ${azureTextMain} mb-8 uppercase tracking-widest relative z-10`}>Nuovo Elemento</h3>
                 
                 <form onSubmit={handleCreateProduct} className="space-y-6 relative z-10">
                      <div className="space-y-2">
                         <label className="text-xs font-bold text-slate-800 uppercase tracking-widest">Nome Prodotto / Servizio</label>
                         <input className="w-full bg-[#0B1621] border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner p-3"
                           value={newProduct.title} onChange={e => setNewProduct({...newProduct, title: e.target.value})} required />
                      </div>
                      
                      <div className="space-y-2">
                         <label className="text-xs font-bold text-slate-800 uppercase tracking-widest">Prezzo (€)</label>
                         <input type="number" className="w-full bg-[#0B1621] border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner p-3"
                           value={newProduct.price} onChange={e => setNewProduct({...newProduct, price: e.target.value})} required />
                      </div>

                      <div className="space-y-2">
                         <label className="text-xs font-bold text-slate-800 uppercase tracking-widest">Categoria</label>
                         <div className="flex gap-4">
                              <button type="button" onClick={() => setNewProduct({...newProduct, category: 'AGENCY'})} className={`flex-1 py-3 text-xs font-bold uppercase border rounded-sm transition-all shadow-sm ${newProduct.category === 'AGENCY' ? 'bg-[#0B1621] border-[#0B1621] text-white' : 'border-slate-400 text-slate-700 bg-white/50 hover:bg-white'}`}>
                                  Servizi Agenzia
                              </button>
                              <button type="button" onClick={() => setNewProduct({...newProduct, category: 'INFO'})} className={`flex-1 py-3 text-xs font-bold uppercase border rounded-sm transition-all shadow-sm ${newProduct.category === 'INFO' ? 'bg-[#0B1621] border-[#0B1621] text-white' : 'border-slate-400 text-slate-700 bg-white/50 hover:bg-white'}`}>
                                  Infobusiness
                              </button>
                         </div>
                      </div>

                      {newProduct.category === 'AGENCY' && (
                          <div className="space-y-2 animate-in fade-in slide-in-from-top-2">
                             <label className="text-xs font-bold text-slate-800 uppercase tracking-widest">Tipo Servizio</label>
                             <select className="w-full bg-[#0B1621] border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner p-3"
                                value={newProduct.serviceType} onChange={e => setNewProduct({...newProduct, serviceType: e.target.value as any})}>
                                 <option value="CONSULTING">Consulenza / Generale</option>
                                 <option value="WEBSITE">Sviluppo Web</option>
                                 <option value="AUTOMATION">Automazioni AI</option>
                                 <option value="SOCIAL_GROWTH">Crescita Social</option>
                             </select>
                          </div>
                      )}

                      <Button type="submit" className="w-full py-4 mt-2 font-bold tracking-[0.2em] uppercase bg-[#0B1621] text-white hover:bg-[#162a3f] shadow-xl border-none">AGGIUNGI A LISTINO</Button>
                 </form>
             </div>
          </div>
      )}
    </div>
  );
};
