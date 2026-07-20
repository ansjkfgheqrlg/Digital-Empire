
import React, { useState } from 'react';
import { User, SocialPost, Task, Invoice, TaskStatus } from '../types';
import { Button } from './ui/Button';
import { 
  LogOut, LayoutDashboard, CheckSquare, Download, MessageSquare, 
  TrendingUp, Calendar, CheckCircle2, AlertCircle, FileText, Bell, 
  Send, X, ChevronRight, Briefcase, ShieldCheck, CreditCard, Activity,
  ArrowUpRight, Clock
} from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';

interface ClientPortalProps {
  currentUser: User;
  onLogout: () => void;
  posts: SocialPost[]; // For approval workflow
  tasks: Task[]; // For project status
  onUpdatePostStatus: (id: string, status: any) => void;
}

// Mock Client Data
const CLIENT_DATA = {
    companyName: 'Digital Spa',
    projectManager: 'Maximilian',
    nextMeeting: '15 Aprile, 14:00',
    totalSpent: 12500,
    activeProjects: 2,
    kpis: [
        { label: 'Impression (Mensili)', value: '1.2M', change: '+15%', type: 'VOLUME' },
        { label: 'Lead Generati', value: '450', change: '+8%', type: 'VOLUME' },
        { label: 'ROAS Medio', value: '4.2x', change: '+0.5', type: 'EFFICIENCY' },
    ],
    invoices: [
        { id: 'inv-client-1', number: 'FATT-24-001', date: '01/03/2024', amount: 2500, status: 'PAID', desc: 'Canone Mensile Marzo' },
        { id: 'inv-client-2', number: 'FATT-24-002', date: '01/04/2024', amount: 2500, status: 'SENT', desc: 'Canone Mensile Aprile' },
        { id: 'inv-client-3', number: 'FATT-24-003', date: '15/04/2024', amount: 1500, status: 'DRAFT', desc: 'Extra: Setup Funnel' },
    ]
};

const CHART_DATA = [
    { name: 'Sett 1', val: 4000 }, 
    { name: 'Sett 2', val: 3000 }, 
    { name: 'Sett 3', val: 5000 }, 
    { name: 'Sett 4', val: 7500 }
];

export const ClientPortal: React.FC<ClientPortalProps> = ({ currentUser, onLogout, posts, tasks, onUpdatePostStatus }) => {
  const [activeTab, setActiveTab] = useState<'DASHBOARD' | 'APPROVALS' | 'FILES'>('DASHBOARD');
  const [isContactModalOpen, setIsContactModalOpen] = useState(false);
  const [messageText, setMessageText] = useState('');
  const [messageSubject, setMessageSubject] = useState('Richiesta Aggiornamento');
  const [showSuccess, setShowSuccess] = useState(false);

  // Filter posts that need approval (READY status) or are recently approved
  const approvalQueue = posts.filter(p => p.status === 'READY' || p.status === 'APPROVED');
  const projectTasks = tasks.filter(t => t.status !== 'DONE').slice(0, 5); 

  const handleSendMessage = (e: React.FormEvent) => {
      e.preventDefault();
      // Simulate sending logic
      setShowSuccess(true);
      setTimeout(() => {
          setShowSuccess(false);
          setIsContactModalOpen(false);
          setMessageText('');
      }, 2000);
  };

  const handleDownload = (fileName: string) => {
      // Simulate download
      const link = document.createElement('a');
      link.href = '#'; 
      link.download = fileName;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      alert(`Download avviato: ${fileName}`);
  };

  return (
    <div className="min-h-screen bg-[#020202] text-platinum-200 font-sans flex flex-col relative overflow-hidden">
        
        {/* Ambient Silver/Azure Background */}
        <div className="absolute top-0 left-0 w-full h-[600px] bg-gradient-to-b from-[#0F1115] via-[#08090A] to-[#020202] pointer-events-none"></div>
        <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-[radial-gradient(circle_at_center,rgba(93,138,168,0.05),transparent_70%)] pointer-events-none"></div>

        {/* Top Bar - Metallic & Glass */}
        <header className="h-24 px-10 flex items-center justify-between relative z-10 border-b border-white/10 bg-[#050505]/80 backdrop-blur-xl">
            <div className="flex items-center gap-6">
                <div className="w-12 h-12 bg-gradient-to-br from-platinum-300 to-platinum-600 rounded-sm flex items-center justify-center text-[#050505] font-bold shadow-[0_0_20px_rgba(255,255,255,0.2)] border border-white/20">
                    {CLIENT_DATA.companyName.substring(0,2).toUpperCase()}
                </div>
                <div>
                    <h1 className="font-bold text-xl text-white tracking-wide">{CLIENT_DATA.companyName}</h1>
                    <div className="flex items-center gap-2 text-[10px] text-diamond-400 uppercase tracking-widest font-mono">
                        <span className="w-1.5 h-1.5 bg-diamond-400 rounded-full animate-pulse shadow-[0_0_5px_#94BBD9]"></span>
                        Partnership Attiva • {currentUser.name}
                    </div>
                </div>
            </div>
            
            <div className="flex items-center gap-10">
                <nav className="flex gap-1 bg-white/5 p-1 rounded-sm border border-white/5">
                    {[
                        {id: 'DASHBOARD', label: 'Overview', icon: LayoutDashboard},
                        {id: 'APPROVALS', label: 'Approvazioni', icon: CheckSquare},
                        {id: 'FILES', label: 'Documenti', icon: FileText}
                    ].map(tab => (
                        <button 
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id as any)}
                            className={`
                                flex items-center gap-2 px-5 py-2.5 rounded-sm text-xs font-bold uppercase tracking-wider transition-all duration-300
                                ${activeTab === tab.id 
                                    ? 'bg-silver-gradient text-surface-950 shadow-[0_0_15px_rgba(255,255,255,0.3)]' 
                                    : 'text-platinum-500 hover:text-white hover:bg-white/5'}
                            `}
                        >
                            <tab.icon className="w-3 h-3" />
                            {tab.label}
                            {tab.id === 'APPROVALS' && approvalQueue.filter(p => p.status === 'READY').length > 0 && (
                                <span className="flex h-2 w-2 relative ml-1">
                                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-diamond-400 opacity-75"></span>
                                    <span className="relative inline-flex rounded-full h-2 w-2 bg-diamond-500"></span>
                                </span>
                            )}
                        </button>
                    ))}
                </nav>

                <div className="h-8 w-[1px] bg-white/10"></div>

                <div className="flex items-center gap-4">
                    <button className="relative p-2 text-platinum-400 hover:text-white transition-colors group">
                        <Bell className="w-5 h-5 group-hover:scale-110 transition-transform" />
                        <span className="absolute top-2 right-2 w-1.5 h-1.5 bg-diamond-500 rounded-full border border-[#050505]"></span>
                    </button>
                    <button onClick={onLogout} className="flex items-center gap-2 text-xs font-bold text-platinum-500 hover:text-red-400 transition-colors uppercase tracking-wider group">
                        <LogOut className="w-4 h-4 group-hover:-translate-x-1 transition-transform" /> Esci
                    </button>
                </div>
            </div>
        </header>

        {/* Content */}
        <main className="flex-1 overflow-y-auto custom-scrollbar p-10 relative z-10">
            <div className="max-w-[1600px] mx-auto space-y-10">
                
                {/* DASHBOARD TAB */}
                {activeTab === 'DASHBOARD' && (
                    <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
                        {/* Welcome Hero */}
                        <div className="flex justify-between items-end border-b border-white/5 pb-8">
                            <div>
                                <h2 className="text-4xl font-bold text-silver-gradient mb-3 tracking-tight drop-shadow-sm">Performance Hub</h2>
                                <p className="text-platinum-400 text-sm font-light">Monitoraggio in tempo reale dei risultati della tua crescita digitale.</p>
                            </div>
                            <Button 
                                variant="diamond" 
                                onClick={() => setIsContactModalOpen(true)}
                                icon={<MessageSquare className="w-4 h-4"/>}
                                className="shadow-[0_0_20px_rgba(93,138,168,0.3)]"
                            >
                                Contatta Project Manager
                            </Button>
                        </div>

                        {/* KPI Cards - The "Silver & Azure" Logic applied here */}
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                            {CLIENT_DATA.kpis.map((kpi, idx) => (
                                <div key={idx} className="metallic-panel bg-[#0A0A0A] p-8 rounded-sm relative overflow-hidden group hover:border-diamond-500/30 transition-all duration-500">
                                    <div className="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
                                        <TrendingUp className={`w-16 h-16 ${kpi.type === 'EFFICIENCY' ? 'text-diamond-400' : 'text-white'}`} />
                                    </div>
                                    <div className="flex justify-between items-start mb-6">
                                        <span className="text-[10px] text-platinum-400 font-bold uppercase tracking-[0.2em]">{kpi.label}</span>
                                    </div>
                                    
                                    {/* LOGIC: Volumes are Silver (Solid), Ratios/Efficiency are Azure Silver (Electric) */}
                                    <div className={`text-4xl font-bold mb-3 tracking-tighter ${kpi.type === 'VOLUME' ? 'text-silver-gradient' : 'text-diamond-400 drop-shadow-[0_0_10px_rgba(93,138,168,0.3)]'}`}>
                                        {kpi.value}
                                    </div>
                                    
                                    <div className="flex items-center gap-2">
                                        {/* Trends are always Azure Silver to signify positive electric growth, distinct from standard green */}
                                        <span className="text-[10px] font-bold text-black bg-diamond-400 px-2 py-0.5 rounded-sm flex items-center gap-1">
                                            <ArrowUpRight className="w-3 h-3"/> {kpi.change}
                                        </span>
                                        <span className="text-[10px] text-platinum-600 font-mono uppercase">vs mese scorso</span>
                                    </div>
                                    
                                    {/* Progress Bar Decor */}
                                    <div className="absolute bottom-0 left-0 w-full h-1 bg-white/5">
                                        <div className={`h-full w-2/3 opacity-50 ${kpi.type === 'VOLUME' ? 'bg-silver-gradient' : 'bg-diamond-gradient'}`}></div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* Charts & Tasks */}
                        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                            <div className="lg:col-span-2 metallic-panel bg-[#0A0A0A] p-8 rounded-sm flex flex-col relative overflow-hidden">
                                <div className="absolute top-0 right-0 p-4 opacity-5"><Activity className="w-32 h-32 text-white"/></div>
                                <h3 className="text-xs font-bold text-white uppercase tracking-widest mb-8 flex items-center gap-2 relative z-10">
                                    <TrendingUp className="w-4 h-4 text-diamond-400"/> Andamento Campagne
                                </h3>
                                <div className="flex-1 w-full min-h-[300px] relative z-10">
                                    <ResponsiveContainer width="100%" height="100%">
                                        <AreaChart data={CHART_DATA}>
                                            <defs>
                                                <linearGradient id="colorClientChart" x1="0" y1="0" x2="0" y2="1">
                                                    <stop offset="5%" stopColor="#94BBD9" stopOpacity={0.3}/>
                                                    <stop offset="95%" stopColor="#94BBD9" stopOpacity={0}/>
                                                </linearGradient>
                                            </defs>
                                            <CartesianGrid strokeDasharray="3 3" stroke="#1F2933" vertical={false} />
                                            <XAxis dataKey="name" stroke="#52606D" tick={{fill: '#9AA5B1', fontSize: 10}} axisLine={false} tickLine={false} dy={10} />
                                            <Tooltip 
                                                cursor={{stroke: 'rgba(255,255,255,0.1)'}}
                                                contentStyle={{ backgroundColor: '#0A0A0A', borderColor: '#333', borderRadius: '2px', color: '#fff', boxShadow: '0 10px 30px rgba(0,0,0,0.5)' }} 
                                            />
                                            <Area type="monotone" dataKey="val" stroke="#94BBD9" strokeWidth={2} fill="url(#colorClientChart)" />
                                        </AreaChart>
                                    </ResponsiveContainer>
                                </div>
                            </div>

                            <div className="metallic-panel bg-[#0A0A0A] p-8 rounded-sm flex flex-col">
                                <h3 className="text-xs font-bold text-white uppercase tracking-widest mb-8 flex items-center gap-2">
                                    <Briefcase className="w-4 h-4 text-platinum-400"/> Progetti Attivi
                                </h3>
                                <div className="space-y-4 flex-1">
                                    {projectTasks.length > 0 ? projectTasks.map(task => (
                                        <div key={task.id} className="flex items-center gap-4 p-4 bg-white/5 rounded-sm border border-white/5 hover:border-diamond-500/30 transition-colors group">
                                            <div className={`w-1.5 h-1.5 rounded-full ${task.status === 'IN_PROGRESS' ? 'bg-diamond-400 animate-pulse shadow-[0_0_8px_#94BBD9]' : 'bg-platinum-600'}`}></div>
                                            <div className="flex-1 min-w-0">
                                                <div className="text-xs font-bold text-white truncate group-hover:text-diamond-300 transition-colors">{task.title}</div>
                                                <div className="text-[9px] text-platinum-500 uppercase tracking-wider">{task.status.replace('_', ' ')}</div>
                                            </div>
                                            {task.priority === 'HIGH' && <span className="text-[8px] text-black font-bold bg-diamond-400 px-1.5 py-0.5 rounded-sm">PRIORITY</span>}
                                        </div>
                                    )) : (
                                        <div className="text-center py-10 text-platinum-600 text-xs italic">Nessun progetto attivo visibile.</div>
                                    )}
                                </div>
                                <div className="mt-8 pt-6 border-t border-white/10 bg-white/5 -mx-8 -mb-8 p-6">
                                    <div className="flex justify-between items-center text-xs">
                                        <span className="text-platinum-400 uppercase tracking-widest text-[10px]">Project Manager</span>
                                        <div className="flex items-center gap-2">
                                            <div className="w-5 h-5 rounded-full bg-platinum-200 text-black flex items-center justify-center font-bold text-[9px]">M</div>
                                            <span className="text-white font-bold">{CLIENT_DATA.projectManager}</span>
                                        </div>
                                    </div>
                                    <div className="flex justify-between items-center text-xs mt-3">
                                        <span className="text-platinum-400 uppercase tracking-widest text-[10px]">Prossima Call</span>
                                        <span className="text-white font-mono bg-white/10 px-2 py-0.5 rounded-sm border border-white/5">{CLIENT_DATA.nextMeeting}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}

                {/* APPROVALS TAB */}
                {activeTab === 'APPROVALS' && (
                    <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
                        <div className="flex justify-between items-end border-b border-white/5 pb-8">
                            <div>
                                <h2 className="text-3xl font-bold text-white mb-2 tracking-tight">Centro Approvazioni</h2>
                                <p className="text-platinum-400 text-sm">Controlla e approva i contenuti prima della pubblicazione.</p>
                            </div>
                        </div>

                        <div className="grid grid-cols-1 gap-6">
                            {approvalQueue.length > 0 ? approvalQueue.map(post => (
                                <div key={post.id} className="metallic-panel bg-[#0A0A0A] p-6 rounded-sm flex items-center justify-between group hover:border-diamond-500/30 transition-all shadow-lg">
                                    <div className="flex items-center gap-8">
                                        <div className="w-24 h-24 bg-[#111] border border-white/10 rounded-sm flex flex-col items-center justify-center gap-2 group-hover:border-diamond-500/20 transition-colors">
                                            <span className="text-[9px] text-platinum-600 uppercase font-bold tracking-widest">Anteprima</span>
                                            {/* Simulate Video/Image icon */}
                                            <div className="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center text-diamond-400">
                                                <div className="w-0 h-0 border-t-[5px] border-t-transparent border-l-[8px] border-l-current border-b-[5px] border-b-transparent ml-1"></div>
                                            </div>
                                        </div>
                                        <div>
                                            <div className="flex items-center gap-3 mb-2">
                                                <span className="px-2 py-0.5 bg-diamond-950/50 text-diamond-300 border border-diamond-500/30 text-[9px] font-bold uppercase rounded-sm">
                                                    {post.platform.replace('INSTAGRAM_', '')}
                                                </span>
                                                <span className="text-[10px] text-platinum-500 font-mono flex items-center gap-1">
                                                    <Calendar className="w-3 h-3"/> {post.scheduledDate}
                                                </span>
                                            </div>
                                            <h4 className="text-xl font-bold text-white mb-2">{post.title}</h4>
                                            <p className="text-xs text-platinum-400 max-w-xl">
                                                Contenuto pronto per la revisione. Clicca su anteprima per vedere i dettagli completi o procedi con l'approvazione diretta.
                                            </p>
                                        </div>
                                    </div>

                                    <div className="flex flex-col gap-3 min-w-[200px]">
                                        {post.status === 'READY' ? (
                                            <>
                                                <Button size="sm" variant="diamond" onClick={() => onUpdatePostStatus(post.id, 'APPROVED')} icon={<CheckCircle2 className="w-4 h-4"/>} className="w-full justify-center">
                                                    Approva Ora
                                                </Button>
                                                <Button size="sm" variant="outline" className="w-full justify-center border-white/10 text-platinum-300 hover:text-white hover:bg-white/5">
                                                    Richiedi Modifiche
                                                </Button>
                                            </>
                                        ) : (
                                            <div className="flex flex-col items-center justify-center gap-2 p-4 bg-diamond-950/30 border border-diamond-500/30 rounded-sm">
                                                <CheckCircle2 className="w-6 h-6 text-diamond-400" />
                                                <span className="text-[10px] font-bold text-diamond-400 uppercase tracking-widest">Approvato</span>
                                            </div>
                                        )}
                                    </div>
                                </div>
                            )) : (
                                <div className="text-center py-24 border border-dashed border-white/10 rounded-sm bg-white/[0.02]">
                                    <CheckSquare className="w-16 h-16 text-platinum-700 mx-auto mb-4" />
                                    <h3 className="text-lg font-bold text-white mb-2">Tutto aggiornato!</h3>
                                    <p className="text-platinum-500 text-sm uppercase tracking-widest">Nessun contenuto in attesa di approvazione.</p>
                                </div>
                            )}
                        </div>
                    </div>
                )}

                {/* FILES / INVOICES TAB */}
                {activeTab === 'FILES' && (
                    <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
                         <div className="border-b border-white/5 pb-8">
                            <h2 className="text-3xl font-bold text-silver-gradient mb-2 tracking-tight">Documenti & Fatture</h2>
                            <p className="text-platinum-400 text-sm">Archivio amministrativo e contrattuale sicuro.</p>
                        </div>

                        <div className="bg-[#0A0A0A] border border-white/10 rounded-sm overflow-hidden shadow-2xl">
                            <table className="w-full text-left text-sm text-platinum-300">
                                <thead className="bg-[#0F0F0F] text-[10px] font-bold text-platinum-500 uppercase tracking-widest border-b border-white/5">
                                    <tr>
                                        <th className="px-8 py-5">Documento</th>
                                        <th className="px-8 py-5">Data</th>
                                        <th className="px-8 py-5">Descrizione</th>
                                        <th className="px-8 py-5 text-right">Importo</th>
                                        <th className="px-8 py-5 text-center">Stato</th>
                                        <th className="px-8 py-5 text-right">Azioni</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-white/5">
                                    {CLIENT_DATA.invoices.map(inv => (
                                        <tr key={inv.id} className="hover:bg-white/5 transition-colors group">
                                            <td className="px-8 py-5 font-bold text-white flex items-center gap-4">
                                                <div className="p-2 bg-white/5 rounded-sm border border-white/5 group-hover:border-white/20 transition-colors">
                                                    <FileText className="w-4 h-4 text-platinum-400 group-hover:text-white"/>
                                                </div>
                                                {inv.number}
                                            </td>
                                            <td className="px-8 py-5 font-mono text-xs text-platinum-500">{inv.date}</td>
                                            <td className="px-8 py-5 text-xs text-platinum-400">{inv.desc}</td>
                                            <td className="px-8 py-5 text-right font-bold text-silver-gradient tracking-wide">€{inv.amount.toLocaleString()}</td>
                                            <td className="px-8 py-5 text-center">
                                                <span className={`text-[9px] font-bold px-3 py-1 rounded-sm uppercase tracking-wider border ${
                                                    inv.status === 'PAID' ? 'bg-diamond-950/30 text-diamond-400 border-diamond-500/30' : 
                                                    inv.status === 'SENT' ? 'bg-white/5 text-platinum-400 border-white/10' : 
                                                    'bg-yellow-900/10 text-yellow-500 border-yellow-500/20'
                                                }`}>
                                                    {inv.status}
                                                </span>
                                            </td>
                                            <td className="px-8 py-5 text-right">
                                                <button 
                                                    onClick={() => handleDownload(`Fattura_${inv.number}.pdf`)}
                                                    className="p-2 hover:bg-white/10 rounded-sm text-platinum-400 hover:text-white transition-colors border border-transparent hover:border-white/10"
                                                    title="Scarica PDF"
                                                >
                                                    <Download className="w-4 h-4"/>
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                )}

            </div>
        </main>

        {/* MODALE CONTATTA PM - WORKING */}
        {isContactModalOpen && (
            <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-sm animate-in fade-in duration-300">
                <div className="bg-[#0A0A0A] border border-white/10 rounded-sm w-full max-w-lg shadow-[0_0_50px_rgba(93,138,168,0.2)] overflow-hidden relative transform transition-all scale-100 metallic-panel">
                    
                    {/* Header Modale */}
                    <div className="p-6 border-b border-white/10 bg-[#0F0F0F] flex justify-between items-center">
                        <div className="flex items-center gap-3">
                            <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center border border-white/10">
                                <MessageSquare className="w-5 h-5 text-diamond-400" />
                            </div>
                            <div>
                                <h3 className="text-lg font-bold text-white">Contatta {CLIENT_DATA.projectManager}</h3>
                                <p className="text-xs text-platinum-500 uppercase tracking-wider">Project Manager</p>
                            </div>
                        </div>
                        <button onClick={() => setIsContactModalOpen(false)} className="text-platinum-500 hover:text-white transition-colors">
                            <X className="w-6 h-6" />
                        </button>
                    </div>

                    {/* Body Modale */}
                    <div className="p-8 bg-[#050505]">
                        {!showSuccess ? (
                            <form onSubmit={handleSendMessage} className="space-y-6">
                                <div className="space-y-2">
                                    <label className="text-[10px] uppercase tracking-widest text-platinum-500 font-bold">Oggetto</label>
                                    <select 
                                        className="w-full bg-[#111] border border-white/10 rounded-sm p-3 text-white text-sm outline-none focus:border-diamond-500/30 transition-colors"
                                        value={messageSubject}
                                        onChange={(e) => setMessageSubject(e.target.value)}
                                    >
                                        <option>Richiesta Aggiornamento</option>
                                        <option>Problema Urgente</option>
                                        <option>Pianificazione Call</option>
                                        <option>Altro</option>
                                    </select>
                                </div>
                                <div className="space-y-2">
                                    <label className="text-[10px] uppercase tracking-widest text-platinum-500 font-bold">Messaggio</label>
                                    <textarea 
                                        className="w-full h-32 bg-[#111] border border-white/10 rounded-sm p-4 text-white text-sm outline-none focus:border-diamond-500/30 transition-colors resize-none leading-relaxed placeholder:text-platinum-700"
                                        placeholder="Scrivi qui il tuo messaggio..."
                                        value={messageText}
                                        onChange={(e) => setMessageText(e.target.value)}
                                        required
                                    ></textarea>
                                </div>
                                <div className="flex justify-between items-center">
                                    <span className="text-[9px] text-platinum-600 flex items-center gap-1">
                                        <Clock className="w-3 h-3"/> Tempo medio risposta: 2h
                                    </span>
                                    <Button type="submit" variant="diamond" className="px-8 font-bold tracking-widest shadow-lg" icon={<Send className="w-4 h-4"/>}>
                                        INVIA
                                    </Button>
                                </div>
                            </form>
                        ) : (
                            <div className="py-12 text-center flex flex-col items-center animate-in zoom-in duration-300">
                                <div className="w-20 h-20 bg-diamond-950/30 rounded-full flex items-center justify-center mb-4 border border-diamond-500/30 shadow-[0_0_30px_rgba(93,138,168,0.2)]">
                                    <CheckCircle2 className="w-10 h-10 text-diamond-400" />
                                </div>
                                <h3 className="text-xl font-bold text-white mb-2">Messaggio Inviato!</h3>
                                <p className="text-platinum-500 text-sm">Il Project Manager ti risponderà al più presto.</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        )}
    </div>
  );
};
