
import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, Lock, Trash2, Mail, User, Calendar, Download } from 'lucide-react';
import { Lead } from '../types';

const MotionDiv = motion.div as any;
const MotionP = motion.p as any;

interface TeamDashboardProps {
  isOpen: boolean;
  onClose: () => void;
}

export const TeamDashboard: React.FC<TeamDashboardProps> = ({ isOpen, onClose }) => {
  const [pin, setPin] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [leads, setLeads] = useState<Lead[]>([]);
  const [error, setError] = useState('');

  // Load leads when authenticated
  useEffect(() => {
    if (isAuthenticated) {
      const storedLeads = localStorage.getItem('digital_empire_leads');
      if (storedLeads) {
        setLeads(JSON.parse(storedLeads));
      }
    }
  }, [isAuthenticated]);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (pin === '369369') {
      setIsAuthenticated(true);
      setError('');
    } else {
      setError('CODICE ERRATO. ACCESSO NEGATO.');
      setPin('');
    }
  };

  const handleDelete = (id: string) => {
    if (confirm('Sei sicuro di voler eliminare questo lead dal database?')) {
      const updatedLeads = leads.filter(lead => lead.id !== id);
      setLeads(updatedLeads);
      localStorage.setItem('digital_empire_leads', JSON.stringify(updatedLeads));
    }
  };

  const handleExport = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(leads, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", `leads_digital_empire_${new Date().toISOString().slice(0,10)}.json`);
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  };

  if (!isOpen) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
        {/* Backdrop */}
        <MotionDiv
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="absolute inset-0 bg-black-950/95 backdrop-blur-lg"
        />

        {/* Container */}
        <MotionDiv
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          exit={{ scale: 0.9, opacity: 0 }}
          className="relative z-10 w-full max-w-6xl bg-black-900 border border-gold-500/30 shadow-[0_0_50px_rgba(0,0,0,0.8)] flex flex-col max-h-[90vh] overflow-hidden"
        >
          {/* Header */}
          <div className="flex justify-between items-center p-6 border-b border-gray-800 bg-black-950">
             <div className="flex items-center gap-3">
                <div className="w-8 h-8 bg-gold-500 flex items-center justify-center rounded-sm">
                   <Lock size={16} className="text-black-950" />
                </div>
                <h2 className="font-serif text-xl text-white tracking-widest">
                  DIGITAL EMPIRE <span className="text-gold-500">HQ</span>
                </h2>
             </div>
             <button onClick={onClose} className="text-gray-500 hover:text-white transition-colors">
               <X size={24} />
             </button>
          </div>

          <div className="p-6 md:p-12 flex-grow overflow-y-auto custom-scrollbar">
            {!isAuthenticated ? (
              /* Login Screen */
              <div className="flex flex-col items-center justify-center h-full min-h-[400px]">
                <div className="w-20 h-20 bg-black-800 rounded-full flex items-center justify-center mb-8 border border-gold-500/20 shadow-[0_0_30px_rgba(253,185,19,0.1)]">
                   <Lock size={32} className="text-gold-500" />
                </div>
                <h3 className="text-3xl text-white font-serif mb-2">Area Riservata Team</h3>
                <p className="text-gray-500 mb-8 font-mono text-xs uppercase tracking-widest">Inserire Protocollo di Sicurezza</p>
                
                <form onSubmit={handleLogin} className="w-full max-w-xs flex flex-col items-center">
                  <input
                    type="password"
                    value={pin}
                    onChange={(e) => setPin(e.target.value)}
                    placeholder="• • • • • •"
                    maxLength={6}
                    className="w-full bg-black-950 border border-gray-700 text-center text-3xl text-gold-500 px-4 py-4 rounded mb-6 focus:border-gold-500 focus:outline-none tracking-[0.5em] placeholder-gray-800 transition-all focus:shadow-[0_0_20px_rgba(253,185,19,0.2)]"
                    autoFocus
                  />
                  <button 
                    type="submit"
                    className="w-full bg-gold-500 text-black-950 font-bold py-4 hover:bg-gold-400 transition-all tracking-widest uppercase text-sm"
                  >
                    Accedi al Database
                  </button>
                  {error && (
                    <MotionP 
                      initial={{ opacity: 0, y: -10 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="text-red-500 font-mono text-xs mt-6 border border-red-900/50 bg-red-900/10 px-4 py-2"
                    >
                      {error}
                    </MotionP>
                  )}
                </form>
              </div>
            ) : (
              /* Dashboard Screen */
              <div className="h-full flex flex-col">
                 <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
                    <div>
                      <h3 className="text-2xl text-white font-serif">Lista Leads ({leads.length})</h3>
                      <p className="text-gray-500 text-sm mt-1">Gestione contatti in tempo reale.</p>
                    </div>
                    <button 
                      onClick={handleExport}
                      className="flex items-center gap-2 text-gold-500 text-xs border border-gold-500/50 px-4 py-2 hover:bg-gold-500 hover:text-black-950 transition-colors uppercase tracking-wider"
                    >
                      <Download size={14} />
                      Esporta Dati
                    </button>
                 </div>

                 {leads.length === 0 ? (
                   <div className="flex flex-col items-center justify-center py-20 text-gray-500 border border-dashed border-gray-800 rounded bg-black-950/50">
                     <User size={48} className="mb-4 opacity-20" />
                     <p>Nessun lead presente nel database.</p>
                     <p className="text-xs mt-2 opacity-50">I nuovi contatti appariranno qui automaticamente.</p>
                   </div>
                 ) : (
                   <div className="overflow-x-auto border border-gray-800 rounded bg-black-950">
                     <table className="w-full text-left border-collapse">
                       <thead>
                         <tr className="bg-black-900 border-b border-gray-800 text-gray-400 text-xs uppercase tracking-wider font-mono">
                           <th className="p-4 font-normal">Data</th>
                           <th className="p-4 font-normal">Contatto</th>
                           <th className="p-4 font-normal">Obiettivo</th>
                           <th className="p-4 w-1/3 font-normal">Messaggio</th>
                           <th className="p-4 text-right font-normal">Azioni</th>
                         </tr>
                       </thead>
                       <tbody className="text-gray-300 text-sm">
                         {leads.map((lead) => (
                           <tr key={lead.id} className="border-b border-gray-800 hover:bg-white/5 transition-colors group">
                             <td className="p-4 whitespace-nowrap text-gray-500 font-mono text-xs">
                               <div className="flex items-center gap-2">
                                 <Calendar size={12} />
                                 {lead.date}
                               </div>
                             </td>
                             <td className="p-4">
                               <div className="font-bold text-white mb-1">{lead.name}</div>
                               <a href={`mailto:${lead.email}`} className="text-gold-500/80 text-xs hover:text-gold-500 hover:underline flex items-center gap-1">
                                 <Mail size={10} /> {lead.email}
                               </a>
                             </td>
                             <td className="p-4">
                               <span className={`px-2 py-1 rounded text-xs border uppercase tracking-wider ${
                                 lead.goal === 'consultation' 
                                   ? 'bg-gold-900/30 text-gold-500 border-gold-500/30' 
                                   : 'bg-gray-800 text-gray-300 border-gray-700'
                               }`}>
                                 {lead.goal === 'consultation' ? 'Consulenza Gratuita' :
                                  lead.goal === 'web' ? 'Sito Web' : 
                                  lead.goal === 'automation' ? 'Automazione AI' : 
                                  lead.goal === 'social' ? 'Social Growth' : 'Full Empire'}
                               </span>
                             </td>
                             <td className="p-4 text-gray-400">
                               <div className="max-h-16 overflow-y-auto text-xs leading-relaxed custom-scrollbar pr-2">
                                 {lead.message}
                               </div>
                             </td>
                             <td className="p-4 text-right">
                               <button 
                                 onClick={() => handleDelete(lead.id)}
                                 className="p-2 hover:bg-red-900/20 text-gray-600 hover:text-red-500 rounded transition-colors"
                                 title="Elimina Lead"
                               >
                                 <Trash2 size={16} />
                               </button>
                             </td>
                           </tr>
                         ))}
                       </tbody>
                     </table>
                   </div>
                 )}
              </div>
            )}
          </div>
        </MotionDiv>
      </div>
    </AnimatePresence>
  );
};
