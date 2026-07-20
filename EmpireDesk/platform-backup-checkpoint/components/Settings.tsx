
import React, { useState, useRef } from 'react';
import { User, Integration, BillingInvoice } from '../types';
import { Button } from './ui/Button';
import { 
  Settings as SettingsIcon, Users, CreditCard, Link as LinkIcon, 
  Shield, Bell, Save, Power, CheckCircle2, AlertTriangle, RefreshCw, 
  Slack, Mail, MessageCircle, DollarSign, Database, Trash2, Download, Upload,
  HardDrive
} from 'lucide-react';
import { MOCK_USERS } from '../constants';
import { DB } from '../utils/database'; // Import DB logic

interface SettingsProps {
  currentUser: User;
}

type SettingsTab = 'GENERAL' | 'TEAM' | 'INTEGRATIONS' | 'BILLING' | 'DATABASE';

// Mock Data for Settings
const MOCK_INTEGRATIONS: Integration[] = [
    { id: 'int-1', name: 'Stripe Payments', provider: 'STRIPE', status: 'CONNECTED', lastSync: '2 min fa' },
    { id: 'int-2', name: 'Google Workspace', provider: 'GOOGLE', status: 'CONNECTED', lastSync: '1 ora fa' },
    { id: 'int-3', name: 'Slack Notifications', provider: 'SLACK', status: 'DISCONNECTED' },
    { id: 'int-4', name: 'WhatsApp Business', provider: 'WHATSAPP', status: 'ERROR', lastSync: 'Ieri' },
    { id: 'int-5', name: 'OpenAI API (GPT-4)', provider: 'OPENAI', status: 'CONNECTED', lastSync: 'Ora' },
];

const MOCK_INVOICES: BillingInvoice[] = [
    { id: 'inv-001', date: '01/03/2024', amount: 299, status: 'PAID', plan: 'Enterprise Monthly' },
    { id: 'inv-002', date: '01/02/2024', amount: 299, status: 'PAID', plan: 'Enterprise Monthly' },
    { id: 'inv-003', date: '01/01/2024', amount: 299, status: 'PAID', plan: 'Enterprise Monthly' },
];

export const Settings: React.FC<SettingsProps> = ({ currentUser }) => {
  const [activeTab, setActiveTab] = useState<SettingsTab>('GENERAL');
  const [companyName, setCompanyName] = useState('Digital Empire SpA');
  const [integrations, setIntegrations] = useState(MOCK_INTEGRATIONS);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const toggleIntegration = (id: string) => {
      setIntegrations(prev => prev.map(int => {
          if (int.id !== id) return int;
          return {
              ...int,
              status: int.status === 'CONNECTED' ? 'DISCONNECTED' : 'CONNECTED'
          };
      }));
  };

  const handleSystemReset = () => {
      if (confirm('Sei ASSOLUTAMENTE sicuro? Questo cancellerà tutti i dati locali (Task, Lead, Post, ecc.) e ripristinerà lo stato iniziale della demo. Questa azione è irreversibile.')) {
          DB.factoryReset();
      }
  };

  const handleDownloadBackup = () => {
      DB.downloadBackup();
  };

  const handleUploadClick = () => {
      fileInputRef.current?.click();
  };

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (!file) return;

      if (confirm('Attenzione: Il ripristino sovrascriverà tutti i dati attuali con quelli presenti nel file di backup. Vuoi procedere?')) {
          try {
              await DB.restoreBackup(file);
              alert('Database ripristinato con successo! Il sistema verrà ricaricato.');
              window.location.reload();
          } catch (err) {
              alert('Errore durante il ripristino: File non valido.');
              console.error(err);
          }
      }
      // Reset input
      if (fileInputRef.current) fileInputRef.current.value = '';
  };

  const getProviderIcon = (provider: string) => {
      switch(provider) {
          case 'STRIPE': return <CreditCard className="w-6 h-6 text-purple-400"/>;
          case 'GOOGLE': return <Mail className="w-6 h-6 text-blue-400"/>;
          case 'SLACK': return <Slack className="w-6 h-6 text-yellow-400"/>;
          case 'WHATSAPP': return <MessageCircle className="w-6 h-6 text-green-400"/>;
          case 'OPENAI': return <Database className="w-6 h-6 text-emerald-400"/>;
          default: return <LinkIcon className="w-6 h-6 text-white"/>;
      }
  };

  return (
    <div className="flex h-[calc(100vh-140px)] gap-8 animate-in fade-in duration-500">
        
        {/* Sidebar Navigation */}
        <div className="w-64 flex flex-col gap-2 shrink-0">
            <h2 className="text-sm font-bold text-platinum-500 uppercase tracking-widest px-4 mb-4">Configurazione</h2>
            
            <button onClick={() => setActiveTab('GENERAL')} className={`flex items-center gap-3 px-4 py-3 rounded-sm text-sm font-medium transition-all ${activeTab === 'GENERAL' ? 'bg-white/10 text-white border-l-2 border-white' : 'text-platinum-400 hover:text-white hover:bg-white/5'}`}>
                <SettingsIcon className="w-4 h-4"/> Generale
            </button>
            <button onClick={() => setActiveTab('DATABASE')} className={`flex items-center gap-3 px-4 py-3 rounded-sm text-sm font-medium transition-all ${activeTab === 'DATABASE' ? 'bg-white/10 text-white border-l-2 border-white' : 'text-platinum-400 hover:text-white hover:bg-white/5'}`}>
                <HardDrive className="w-4 h-4"/> Database & Backup
            </button>
            <button onClick={() => setActiveTab('TEAM')} className={`flex items-center gap-3 px-4 py-3 rounded-sm text-sm font-medium transition-all ${activeTab === 'TEAM' ? 'bg-white/10 text-white border-l-2 border-white' : 'text-platinum-400 hover:text-white hover:bg-white/5'}`}>
                <Users className="w-4 h-4"/> Membri & Permessi
            </button>
            <button onClick={() => setActiveTab('INTEGRATIONS')} className={`flex items-center gap-3 px-4 py-3 rounded-sm text-sm font-medium transition-all ${activeTab === 'INTEGRATIONS' ? 'bg-white/10 text-white border-l-2 border-white' : 'text-platinum-400 hover:text-white hover:bg-white/5'}`}>
                <LinkIcon className="w-4 h-4"/> Integrazioni API
            </button>
            <button onClick={() => setActiveTab('BILLING')} className={`flex items-center gap-3 px-4 py-3 rounded-sm text-sm font-medium transition-all ${activeTab === 'BILLING' ? 'bg-white/10 text-white border-l-2 border-white' : 'text-platinum-400 hover:text-white hover:bg-white/5'}`}>
                <CreditCard className="w-4 h-4"/> Billing & Piano
            </button>
        </div>

        {/* Main Content */}
        <div className="flex-1 bg-[#0A0A0A] border border-white/10 rounded-sm p-8 overflow-y-auto custom-scrollbar relative">
            
            {/* GENERAL SETTINGS */}
            {activeTab === 'GENERAL' && (
                <div className="space-y-8 max-w-2xl">
                    <div className="border-b border-white/10 pb-6">
                        <h1 className="text-2xl font-bold text-white mb-2">Impostazioni Generali</h1>
                        <p className="text-platinum-500 text-sm">Gestisci le informazioni principali dell'azienda.</p>
                    </div>

                    <div className="space-y-6">
                        <div className="space-y-2">
                            <label className="text-[10px] uppercase tracking-widest text-platinum-500 font-bold">Nome Azienda</label>
                            <input 
                                className="w-full bg-[#111] border border-[#222] rounded-sm p-4 text-white focus:border-white/30 outline-none" 
                                value={companyName} 
                                onChange={(e) => setCompanyName(e.target.value)}
                            />
                        </div>
                        
                        <div className="grid grid-cols-2 gap-6">
                             <div className="space-y-2">
                                <label className="text-[10px] uppercase tracking-widest text-platinum-500 font-bold">Lingua Sistema</label>
                                <select className="w-full bg-[#111] border border-[#222] rounded-sm p-4 text-white focus:border-white/30 outline-none">
                                    <option>Italiano</option>
                                    <option>English</option>
                                </select>
                            </div>
                            <div className="space-y-2">
                                <label className="text-[10px] uppercase tracking-widest text-platinum-500 font-bold">Valuta Default</label>
                                <select className="w-full bg-[#111] border border-[#222] rounded-sm p-4 text-white focus:border-white/30 outline-none">
                                    <option>EUR (€)</option>
                                    <option>USD ($)</option>
                                </select>
                            </div>
                        </div>

                        <div className="pt-6 flex gap-4">
                            <Button icon={<Save className="w-4 h-4"/>}>Salva Modifiche</Button>
                        </div>
                    </div>
                </div>
            )}

            {/* DATABASE & BACKUP */}
            {activeTab === 'DATABASE' && (
                <div className="space-y-8 max-w-2xl">
                    <div className="border-b border-white/10 pb-6">
                        <h1 className="text-2xl font-bold text-white mb-2">Gestione Database & Backup</h1>
                        <p className="text-platinum-500 text-sm">I tuoi dati sono preziosi. Esegui backup regolari per evitare perdite accidentali.</p>
                    </div>

                    {/* Status Card */}
                    <div className="bg-[#0F0F0F] border border-white/10 p-6 rounded-sm flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className="p-3 bg-green-900/20 rounded-full border border-green-500/30">
                                <HardDrive className="w-6 h-6 text-green-400" />
                            </div>
                            <div>
                                <h3 className="text-white font-bold">Stato Database Locale</h3>
                                <p className="text-xs text-platinum-500">I dati vengono salvati automaticamente nel browser.</p>
                            </div>
                        </div>
                        <div className="flex items-center gap-2 px-3 py-1 bg-green-900/10 border border-green-900/30 rounded-full">
                            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                            <span className="text-[10px] font-bold text-green-400 uppercase tracking-widest">ONLINE</span>
                        </div>
                    </div>

                    {/* Actions */}
                    <div className="grid grid-cols-2 gap-6">
                        <div className="bg-[#0F0F0F] border border-white/10 p-6 rounded-sm flex flex-col items-center text-center hover:border-diamond-500/30 transition-all">
                            <Download className="w-8 h-8 text-diamond-400 mb-4" />
                            <h3 className="text-white font-bold mb-2">Esporta Database</h3>
                            <p className="text-xs text-platinum-500 mb-6">Scarica un file .json con tutti i tuoi dati (Clienti, Task, Impostazioni).</p>
                            <Button variant="diamond" onClick={handleDownloadBackup} className="w-full">Scarica Backup</Button>
                        </div>

                        <div className="bg-[#0F0F0F] border border-white/10 p-6 rounded-sm flex flex-col items-center text-center hover:border-white/30 transition-all">
                            <Upload className="w-8 h-8 text-platinum-400 mb-4" />
                            <h3 className="text-white font-bold mb-2">Ripristina Dati</h3>
                            <p className="text-xs text-platinum-500 mb-6">Carica un file di backup precedente per ripristinare il sistema.</p>
                            <input type="file" ref={fileInputRef} className="hidden" onChange={handleFileChange} accept=".json" />
                            <Button variant="outline" onClick={handleUploadClick} className="w-full">Carica File</Button>
                        </div>
                    </div>

                    {/* Danger Zone */}
                    <div className="mt-12 pt-8 border-t border-red-900/30">
                        <h3 className="text-red-400 font-bold uppercase tracking-widest text-xs mb-4">Zona Pericolo</h3>
                        <div className="flex items-center justify-between">
                            <p className="text-sm text-platinum-500">Cancella definitivamente tutti i dati e resetta l'applicazione.</p>
                            <Button variant="danger" onClick={handleSystemReset} icon={<Trash2 className="w-4 h-4"/>}>Factory Reset</Button>
                        </div>
                    </div>
                </div>
            )}

            {/* TEAM & PERMISSIONS */}
            {activeTab === 'TEAM' && (
                 <div className="space-y-8">
                    <div className="border-b border-white/10 pb-6 flex justify-between items-center">
                        <div>
                            <h1 className="text-2xl font-bold text-white mb-2">Gestione Team</h1>
                            <p className="text-platinum-500 text-sm">Controlla l'accesso e i ruoli degli utenti.</p>
                        </div>
                        <Button variant="outline" icon={<Users className="w-4 h-4"/>}>Invita Utente</Button>
                    </div>

                    <div className="border border-white/10 rounded-sm overflow-hidden">
                        <table className="w-full text-left text-sm text-platinum-300">
                            <thead className="bg-[#111] text-[10px] font-bold text-platinum-500 uppercase tracking-widest">
                                <tr>
                                    <th className="px-6 py-4">Utente</th>
                                    <th className="px-6 py-4">Ruolo</th>
                                    <th className="px-6 py-4">Stato</th>
                                    <th className="px-6 py-4">Ultimo Accesso</th>
                                    <th className="px-6 py-4 text-right">Azioni</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-white/5">
                                {MOCK_USERS.map(user => (
                                    <tr key={user.id} className="hover:bg-white/5 transition-colors">
                                        <td className="px-6 py-4">
                                            <div className="flex items-center gap-3">
                                                <div className="w-8 h-8 rounded bg-white/10 flex items-center justify-center text-white font-bold">{user.name.substring(0,1)}</div>
                                                <div>
                                                    <div className="font-bold text-white">{user.name}</div>
                                                    <div className="text-[10px] text-platinum-600">{user.email || `${user.name.toLowerCase()}@aureus.com`}</div>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="px-6 py-4">
                                            <span className={`px-2 py-1 rounded-sm text-[10px] font-bold uppercase border ${user.role === 'ADMIN' ? 'border-purple-500/30 text-purple-400 bg-purple-900/20' : 'border-blue-500/30 text-blue-400 bg-blue-900/20'}`}>
                                                {user.role}
                                            </span>
                                        </td>
                                        <td className="px-6 py-4">
                                            <span className="flex items-center gap-2 text-[10px] text-green-400 font-mono">
                                                <span className="w-1.5 h-1.5 rounded-full bg-green-400 shadow-[0_0_5px_#4ade80]"></span>
                                                ATTIVO
                                            </span>
                                        </td>
                                        <td className="px-6 py-4 font-mono text-xs text-platinum-500">Oggi, 10:42</td>
                                        <td className="px-6 py-4 text-right">
                                            <button className="text-platinum-500 hover:text-white underline text-xs">Modifica</button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                 </div>
            )}

            {/* INTEGRATIONS */}
            {activeTab === 'INTEGRATIONS' && (
                <div className="space-y-8">
                    <div className="border-b border-white/10 pb-6">
                        <h1 className="text-2xl font-bold text-white mb-2">Integrazioni</h1>
                        <p className="text-platinum-500 text-sm">Collega Aureus ai tuoi strumenti esterni preferiti.</p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {integrations.map(int => (
                            <div key={int.id} className="bg-[#0F0F0F] border border-white/10 p-6 rounded-sm flex items-start justify-between group hover:border-white/30 transition-all">
                                <div className="flex gap-4">
                                    <div className="p-3 bg-white/5 rounded-sm h-fit group-hover:bg-white/10 transition-colors">
                                        {getProviderIcon(int.provider)}
                                    </div>
                                    <div>
                                        <h3 className="text-lg font-bold text-white mb-1">{int.name}</h3>
                                        <div className="flex items-center gap-2 mb-4">
                                            {int.status === 'CONNECTED' && <span className="text-[10px] text-green-400 font-bold bg-green-900/20 px-2 py-0.5 rounded-sm flex items-center gap-1"><CheckCircle2 className="w-3 h-3"/> CONNESSO</span>}
                                            {int.status === 'DISCONNECTED' && <span className="text-[10px] text-platinum-600 font-bold bg-white/5 px-2 py-0.5 rounded-sm">NON CONNESSO</span>}
                                            {int.status === 'ERROR' && <span className="text-[10px] text-red-400 font-bold bg-red-900/20 px-2 py-0.5 rounded-sm flex items-center gap-1"><AlertTriangle className="w-3 h-3"/> ERRORE</span>}
                                        </div>
                                        {int.lastSync && <p className="text-[10px] text-platinum-600 font-mono">Ultima Sync: {int.lastSync}</p>}
                                    </div>
                                </div>
                                <div className="flex items-center">
                                    <button 
                                        onClick={() => toggleIntegration(int.id)}
                                        className={`w-12 h-6 rounded-full p-1 transition-colors duration-300 ease-in-out ${int.status === 'CONNECTED' ? 'bg-green-500' : 'bg-platinum-700'}`}
                                    >
                                        <div className={`bg-white w-4 h-4 rounded-full shadow-md transform duration-300 ease-in-out ${int.status === 'CONNECTED' ? 'translate-x-6' : 'translate-x-0'}`}></div>
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* BILLING */}
            {activeTab === 'BILLING' && (
                <div className="space-y-8 max-w-4xl">
                     <div className="border-b border-white/10 pb-6">
                        <h1 className="text-2xl font-bold text-white mb-2">Billing & Piani</h1>
                        <p className="text-platinum-500 text-sm">Gestisci il tuo abbonamento Aureus Enterprise.</p>
                    </div>

                    <div className="grid grid-cols-2 gap-6">
                        <div className="bg-gradient-to-br from-[#0F0F0F] to-[#1a1a1a] border border-white/10 p-6 rounded-sm relative overflow-hidden">
                             <div className="absolute top-0 right-0 p-4 opacity-10"><Shield className="w-24 h-24 text-white"/></div>
                             <h3 className="text-[10px] font-bold text-platinum-500 uppercase tracking-widest mb-2">Piano Attivo</h3>
                             <div className="text-3xl font-bold text-white mb-1">Enterprise</div>
                             <p className="text-platinum-400 text-xs mb-6">Fatturazione Mensile</p>
                             <div className="flex gap-4">
                                 <Button size="sm" variant="outline">Cambia Piano</Button>
                                 <Button size="sm" variant="ghost" className="text-red-400 hover:bg-red-900/10 hover:text-red-300">Disdici</Button>
                             </div>
                        </div>
                        <div className="bg-[#0F0F0F] border border-white/10 p-6 rounded-sm flex flex-col justify-center">
                             <div className="flex justify-between items-center mb-4">
                                 <span className="text-platinum-400 text-sm">Metodo di Pagamento</span>
                                 <span className="text-white font-bold text-sm">•••• 4242</span>
                             </div>
                             <div className="flex justify-between items-center mb-4">
                                 <span className="text-platinum-400 text-sm">Prossimo Rinnovo</span>
                                 <span className="text-white font-bold text-sm">01 Aprile 2024</span>
                             </div>
                             <div className="flex justify-between items-center">
                                 <span className="text-platinum-400 text-sm">Importo</span>
                                 <span className="text-emerald-400 font-bold text-lg">€299.00</span>
                             </div>
                        </div>
                    </div>

                    <div className="mt-8">
                        <h3 className="text-lg font-bold text-white mb-4">Storico Fatture</h3>
                        <div className="border border-white/10 rounded-sm overflow-hidden">
                            <table className="w-full text-left text-sm text-platinum-300">
                                <thead className="bg-[#111] text-[10px] font-bold text-platinum-500 uppercase tracking-widest">
                                    <tr>
                                        <th className="px-6 py-4">Data</th>
                                        <th className="px-6 py-4">Piano</th>
                                        <th className="px-6 py-4">Importo</th>
                                        <th className="px-6 py-4">Stato</th>
                                        <th className="px-6 py-4 text-right">Download</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-white/5">
                                    {MOCK_INVOICES.map(inv => (
                                        <tr key={inv.id} className="hover:bg-white/5 transition-colors">
                                            <td className="px-6 py-4 font-mono text-xs">{inv.date}</td>
                                            <td className="px-6 py-4">{inv.plan}</td>
                                            <td className="px-6 py-4 font-bold text-white">€{inv.amount.toFixed(2)}</td>
                                            <td className="px-6 py-4">
                                                <span className="text-[10px] text-green-400 font-bold bg-green-900/20 px-2 py-1 rounded-sm">PAGATO</span>
                                            </td>
                                            <td className="px-6 py-4 text-right">
                                                <button className="text-platinum-500 hover:text-white transition-colors"><Save className="w-4 h-4"/></button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            )}
        </div>
    </div>
  );
};
