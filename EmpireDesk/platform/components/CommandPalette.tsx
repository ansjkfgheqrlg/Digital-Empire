
import React, { useEffect, useState } from 'react';
import { Search, LayoutDashboard, Briefcase, Calendar, Settings, Users, ArrowRight } from 'lucide-react';

interface CommandPaletteProps {
  onNavigate: (path: string) => void;
}

const COMMANDS = [
    { id: 'home', label: 'Vai alla Dashboard', icon: LayoutDashboard, path: '/' },
    { id: 'tasks', label: 'Gestione Task', icon: Briefcase, path: '/tasks' },
    { id: 'crm', label: 'Sales Pipeline (CRM)', icon: Users, path: '/crm' },
    { id: 'cal', label: 'Master Calendar', icon: Calendar, path: '/calendar' },
    { id: 'settings', label: 'Impostazioni', icon: Settings, path: '/settings' },
];

export const CommandPalette: React.FC<CommandPaletteProps> = ({ onNavigate }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [selectedIndex, setSelectedIndex] = useState(0);

  const filteredCommands = COMMANDS.filter(cmd => 
      cmd.label.toLowerCase().includes(query.toLowerCase())
  );

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setIsOpen(prev => !prev);
      }
      if (e.key === 'Escape') {
          setIsOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const handleSelect = (path: string) => {
      onNavigate(path);
      setIsOpen(false);
      setQuery('');
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm flex items-start justify-center pt-[15vh] animate-in fade-in duration-200">
        <div className="w-full max-w-xl bg-[#0A0A0A] border border-white/10 rounded-lg shadow-2xl overflow-hidden animate-in zoom-in-95 duration-200">
            {/* Input */}
            <div className="flex items-center px-4 py-4 border-b border-white/5">
                <Search className="w-5 h-5 text-platinum-500 mr-3" />
                <input 
                    className="flex-1 bg-transparent border-none outline-none text-white text-lg placeholder:text-platinum-600 focus:ring-0"
                    placeholder="Cerca comando o pagina..."
                    value={query}
                    onChange={(e) => { setQuery(e.target.value); setSelectedIndex(0); }}
                    autoFocus
                />
                <span className="text-[10px] text-platinum-600 border border-white/10 px-2 py-1 rounded bg-white/5">ESC</span>
            </div>

            {/* List */}
            <div className="max-h-[300px] overflow-y-auto py-2">
                {filteredCommands.length > 0 ? filteredCommands.map((cmd, idx) => (
                    <button
                        key={cmd.id}
                        onClick={() => handleSelect(cmd.path)}
                        onMouseEnter={() => setSelectedIndex(idx)}
                        className={`w-full text-left px-4 py-3 flex items-center justify-between transition-colors ${idx === selectedIndex ? 'bg-white/10' : 'hover:bg-white/5'}`}
                    >
                        <div className="flex items-center gap-3">
                            <cmd.icon className={`w-4 h-4 ${idx === selectedIndex ? 'text-white' : 'text-platinum-500'}`} />
                            <span className={`text-sm ${idx === selectedIndex ? 'text-white font-medium' : 'text-platinum-300'}`}>{cmd.label}</span>
                        </div>
                        {idx === selectedIndex && <ArrowRight className="w-3 h-3 text-platinum-400" />}
                    </button>
                )) : (
                    <div className="px-4 py-8 text-center text-platinum-600 text-sm">
                        Nessun risultato trovato.
                    </div>
                )}
            </div>
            
            <div className="px-4 py-2 bg-[#050505] border-t border-white/5 text-[10px] text-platinum-600 flex justify-between">
                <span>Aureus OS Command</span>
                <span>v2.1</span>
            </div>
        </div>
    </div>
  );
};
