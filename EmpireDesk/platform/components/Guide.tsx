
import React from 'react';
import { HelpCircle, LayoutDashboard, KanbanSquare, Briefcase, MonitorPlay, BookOpen, Instagram, Users, Info, ShieldCheck, Trophy, Wallet, Zap, HardDrive, Monitor } from 'lucide-react';

export const Guide: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-10 animate-in fade-in duration-500">
       <div className="text-center mb-10">
           <h1 className="text-3xl font-bold text-silver-gradient mb-2">Guida Operativa Aureus</h1>
           <p className="text-platinum-400">Manuale d'uso completo per l'ecosistema Agency OS v2.0.</p>
       </div>

       <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
           <GuideSection 
             icon={LayoutDashboard} 
             title="Dashboard" 
             text="Panoramica finanziaria e operativa. I dati (Fatturato, Lead, Task) sono calcolati in tempo reale."
           />
           <GuideSection 
             icon={Trophy} 
             title="The Arena" 
             text="Modulo di Gamification. Guadagna XP completando Task e chiudendo Deal. Scala i ranghi da Bronze ad Aureus Legend."
           />
           <GuideSection 
             icon={KanbanSquare} 
             title="Attività (Tasks)" 
             text="Kanban Board per il flusso di lavoro. Gestisci priorità e scadenze. Le task completate generano XP."
           />
           <GuideSection 
             icon={Briefcase} 
             title="CRM & Vendite" 
             text="Gestione Lead e Pipeline. Crea Preventivi PDF direttamente dalla scheda cliente e traccia le conversioni."
           />
           <GuideSection 
             icon={Wallet} 
             title="Finanza" 
             text="Monitoraggio Cash Flow, entrate e uscite operative. Grafici in tempo reale per il controllo tesoreria."
           />
           <GuideSection 
             icon={HardDrive} 
             title="The Vault" 
             text="Archivio sicuro per file, contratti e asset digitali. Organizza tutto in cartelle per cliente o progetto."
           />
           <GuideSection 
             icon={Zap} 
             title="Automazioni" 
             text="Configura regole 'Se succede questo, allora fai quello' per risparmiare tempo (es. Email automatica ai nuovi Lead)."
           />
           <GuideSection 
             icon={MonitorPlay} 
             title="Infobusiness" 
             text="Costruttore di Corsi e Funnel. Gestisci il catalogo prodotti e analizza le performance di vendita."
           />
           <GuideSection 
             icon={Monitor} 
             title="War Room" 
             text="Modalità Full Screen per il monitoraggio live in ufficio. Dati in tempo reale, feed attività e leaderboard."
           />
           <GuideSection 
             icon={ShieldCheck} 
             title="Client Portal" 
             text="Accesso dedicato per i clienti VIP. Permette loro di approvare contenuti e visualizzare i risultati senza vedere i dati interni."
           />
       </div>
       
       <div className="mt-12 pt-8 border-t border-white/10 text-center">
           <p className="text-xs text-platinum-600 font-mono uppercase tracking-widest">Aureus Operating System • Developed for Digital Empire</p>
       </div>
    </div>
  );
};

const GuideSection: React.FC<{icon: any, title: string, text: string, highlight?: boolean}> = ({icon: Icon, title, text, highlight}) => {
    // DARK SILVER / BLACK TITANIUM STYLE
    const metallicBlockClass = "bg-gradient-to-br from-[#334155] via-[#1e293b] to-[#0f172a] border-t border-l border-white/10 border-b border-r border-black/60 shadow-[0_10px_30px_-10px_rgba(0,0,0,0.8)] relative overflow-hidden group hover:-translate-y-1 hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,1)] transition-all duration-300";
    
    return (
        <div className={`p-6 rounded-sm flex gap-4 items-start ${metallicBlockClass}`}>
            {/* Brushed Metal Texture Overlay */}
            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.07] pointer-events-none mix-blend-overlay"></div>
            
            {/* Dark Shine Effect */}
            <div className="absolute top-0 right-0 w-32 h-32 bg-white/5 opacity-[0.2] rounded-full blur-3xl -translate-y-10 translate-x-10 group-hover:opacity-[0.4] transition-opacity pointer-events-none"></div>

            <div className="p-3 bg-black/20 rounded-sm shrink-0 border border-white/5 shadow-inner relative z-10">
                <Icon className="w-6 h-6 text-white" />
            </div>
            <div className="relative z-10">
                <h3 className="text-sm font-black mb-2 text-white uppercase tracking-wider drop-shadow-md">{title}</h3>
                <p className="text-platinum-400 text-xs leading-relaxed font-medium">{text}</p>
            </div>
            
            <div className="absolute bottom-0 left-0 w-full h-[2px] bg-black/40 border-b border-white/5">
                <div className="h-full bg-platinum-400 w-1/3 group-hover:w-full transition-all duration-1000 shadow-[0_0_10px_rgba(255,255,255,0.3)]"></div>
            </div>
        </div>
    );
};
