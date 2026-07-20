
import React, { useState } from 'react';
import { User } from '../types';
import { MOCK_USERS } from '../constants';
import { Hexagon, ArrowRight, Lock, ShieldCheck, Users, Briefcase } from 'lucide-react';

interface LoginScreenProps {
  onLogin: (user: User) => void;
}

type LoginType = 'TEAM' | 'CLIENT';

export const LoginScreen: React.FC<LoginScreenProps> = ({ onLogin }) => {
  const [loginType, setLoginType] = useState<LoginType>('TEAM');
  
  // Team State
  const teamUsers = MOCK_USERS.filter(u => u.role !== 'CLIENT');
  const [selectedTeamUserId, setSelectedTeamUserId] = useState<string>(teamUsers[0]?.id || '');

  // Client State
  const [clientCode, setClientCode] = useState('');
  const [error, setError] = useState('');

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (loginType === 'TEAM') {
        const user = MOCK_USERS.find(u => u.id === selectedTeamUserId);
        if (user) {
            onLogin(user);
        }
    } else {
        // Client Login Logic
        const client = MOCK_USERS.find(u => u.role === 'CLIENT' && u.accessCode === clientCode);
        if (client) {
            onLogin(client);
        } else {
            setError('Codice di accesso non valido.');
        }
    }
  };

  return (
    <div className="min-h-screen bg-black flex items-center justify-center p-4 relative overflow-hidden">
      
      {/* Ambient background light */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-white opacity-[0.03] rounded-full blur-[100px] pointer-events-none"></div>

      <div className="w-full max-w-md relative z-10">
        
        {/* Card Container - DARK SILVER / TITANIUM BLOCK */}
        <div className="bg-gradient-to-br from-[#cbd5e1] via-[#94a3b8] to-[#64748b] border-t border-l border-white/40 border-b border-r border-black/40 p-10 rounded-sm shadow-2xl relative overflow-hidden metallic-panel">
          
          {/* Metallic Noise Texture */}
          <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.12] pointer-events-none mix-blend-overlay"></div>
          
          {/* Shine */}
          <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-white/20 via-transparent to-black/10 pointer-events-none"></div>

          <div className="text-center mb-8 relative z-10">
            <div className="inline-flex p-4 bg-slate-900/10 border border-slate-900/10 rounded-sm mb-6 shadow-inner backdrop-blur-sm">
              <Hexagon className="w-10 h-10 text-slate-900" strokeWidth={1.5} />
            </div>
            <h1 className="text-4xl font-black text-slate-900 tracking-widest mb-2 drop-shadow-sm">AUREUS</h1>
            <p className="text-slate-700 text-xs font-bold uppercase tracking-[0.3em]">Enterprise OS v2.0</p>
          </div>

          {/* Login Type Selector - Etched style */}
          <div className="grid grid-cols-2 gap-2 mb-8 p-1 bg-slate-900/10 rounded-sm border border-slate-900/5 shadow-inner relative z-10">
              <button 
                type="button"
                onClick={() => { setLoginType('TEAM'); setError(''); }}
                className={`flex items-center justify-center gap-2 py-2 text-[10px] font-bold uppercase tracking-widest rounded-sm transition-all ${loginType === 'TEAM' ? 'bg-slate-800 text-white shadow-lg' : 'text-slate-700 hover:bg-white/10 hover:text-slate-900'}`}
              >
                  <Users className="w-3 h-3" /> Area Team
              </button>
              <button 
                type="button"
                onClick={() => { setLoginType('CLIENT'); setError(''); }}
                className={`flex items-center justify-center gap-2 py-2 text-[10px] font-bold uppercase tracking-widest rounded-sm transition-all ${loginType === 'CLIENT' ? 'bg-slate-800 text-white shadow-lg' : 'text-slate-700 hover:bg-white/10 hover:text-slate-900'}`}
              >
                  <Briefcase className="w-3 h-3" /> Portale Clienti
              </button>
          </div>

          <form onSubmit={handleLogin} className="space-y-6 relative z-10">
            
            {loginType === 'TEAM' ? (
                // TEAM LOGIN UI
                <>
                    <div className="space-y-2 animate-in fade-in slide-in-from-left-4 duration-300">
                      <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                        <ShieldCheck className="w-3 h-3" /> Identità Operativa
                      </label>
                      <div className="relative group">
                        {/* Dark Input on Silver Background for high contrast */}
                        <select 
                          value={selectedTeamUserId}
                          onChange={(e) => setSelectedTeamUserId(e.target.value)}
                          className="w-full bg-slate-900 border border-slate-700 text-white py-4 px-4 appearance-none focus:border-white/50 transition-colors rounded-sm shadow-inner outline-none font-medium"
                        >
                          {teamUsers.map(user => (
                            <option key={user.id} value={user.id} className="bg-slate-900">
                              {user.name} — {user.title}
                            </option>
                          ))}
                        </select>
                        <div className="absolute inset-y-0 right-4 flex items-center pointer-events-none">
                          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse shadow-[0_0_5px_#22c55e]"></div>
                        </div>
                      </div>
                    </div>

                    <div className="space-y-2">
                      <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                        <Lock className="w-3 h-3" /> Password
                      </label>
                      <input 
                        type="password" 
                        value="******************"
                        disabled
                        className="w-full bg-slate-900/80 border border-slate-700/50 text-slate-400 py-4 px-4 rounded-sm cursor-not-allowed font-mono text-sm tracking-widest shadow-inner"
                      />
                    </div>
                </>
            ) : (
                // CLIENT LOGIN UI
                <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-300">
                    <div className="space-y-2">
                      <label className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                        <Lock className="w-3 h-3" /> Codice Accesso Cliente
                      </label>
                      <input 
                        type="password" 
                        value={clientCode}
                        onChange={(e) => setClientCode(e.target.value)}
                        placeholder="Inserisci il codice privato..."
                        className="w-full bg-slate-900 border border-slate-700 text-white py-4 px-4 rounded-sm focus:border-white/50 outline-none shadow-inner font-mono text-center tracking-[0.5em] text-lg placeholder:tracking-normal placeholder:text-sm placeholder:text-slate-500"
                        autoFocus
                      />
                    </div>
                    {error && (
                        <div className="text-red-900 text-xs text-center font-bold bg-red-100 p-2 border border-red-300 rounded-sm">
                            {error}
                        </div>
                    )}
                </div>
            )}

            <button 
              type="submit"
              className={`
                w-full font-bold py-4 rounded-sm hover:brightness-110 transition-all flex items-center justify-center gap-3 mt-4 shadow-xl border
                ${loginType === 'TEAM' 
                    ? 'bg-gradient-to-r from-slate-900 to-slate-800 text-white border-slate-700' 
                    : 'bg-gradient-to-r from-emerald-900 to-emerald-800 text-white border-emerald-800'}
              `}
            >
              <span>{loginType === 'TEAM' ? 'ACCEDI AL SISTEMA' : 'ENTRA NEL PORTALE'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </form>

          <div className="mt-10 pt-6 border-t border-slate-500/20 text-center relative z-10">
            <p className="text-[10px] text-slate-700 font-mono font-bold flex justify-center items-center gap-2">
              <span className={`w-2 h-2 rounded-full ${loginType === 'TEAM' ? 'bg-slate-800' : 'bg-emerald-600'}`}></span>
              SECURE CONNECTION ESTABLISHED
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
