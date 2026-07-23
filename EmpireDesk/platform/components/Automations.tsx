
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { AutomationRule, TriggerType, ActionType, AutomationLog } from '../types';
import { Zap, Plus, Play, MoreVertical, ArrowRight, Activity, Bell, Mail, CheckCircle2, Clock, Terminal, X, Radio, AlertTriangle, Youtube } from 'lucide-react';
import { Button } from './ui/Button';
import { EmpireApi, EmpireTile } from '../utils/empireApi';

interface AutomationsProps {
    rules: AutomationRule[];
    logs?: AutomationLog[]; // Added logs prop
    onToggleRule: (id: string) => void;
    onAddRule: (rule: AutomationRule) => void;
    onTestRule?: (id: string) => void; // Added test function
}

export const Automations: React.FC<AutomationsProps> = ({ rules, logs = [], onToggleRule, onAddRule, onTestRule }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newRule, setNewRule] = useState<Partial<AutomationRule>>({ name: '', trigger: 'LEAD_CREATED', action: 'NOTIFY_SLACK' });

  // --- OPERAZIONI REALI (Digital Empire) — U1: wiring dati reali dentro Aureus (dossier 17 §0-bis) ---
  // Le 8 automazioni reali (outreach, PreventivoForge, caroselli, Empire Studio...) via app.py.
  // Additivo: non tocca il motore di automazioni mock sopra (regole trigger->action, ancora valido).
  const [empireAvailable, setEmpireAvailable] = useState<boolean | null>(null); // null = verifica in corso
  const [empireTiles, setEmpireTiles] = useState<EmpireTile[]>([]);
  const [empireInputs, setEmpireInputs] = useState<Record<string, string>>({});
  const [empireLogs, setEmpireLogs] = useState<Record<string, string[]>>({});
  const [empireErrors, setEmpireErrors] = useState<Record<string, string>>({});
  const pollingRef = useRef<Set<string>>(new Set());

  // --- YouTube Automation Factory (modulo youtube) — tool deterministici della skill /yt-factory ---
  const [ytOut, setYtOut] = useState<string>('Premi un pulsante per usare la fabbrica.');
  const [ytBusy, setYtBusy] = useState<boolean>(false);
  const [ytSeo, setYtSeo] = useState({ title: '', keyword: '', description: '', tags: '', thumbnail: false, subtitles: false });
  const [ytVideos, setYtVideos] = useState<string>('[{"views":120000,"age_hours":800,"errors":[]},{"views":300000,"age_hours":1500,"errors":[]}]');

  const ytRun = useCallback(async (fn: () => Promise<Record<string, unknown>>) => {
    setYtBusy(true);
    try {
      const r = await fn();
      setYtOut(JSON.stringify(r, null, 2));
    } catch {
      setYtOut('Backend non raggiungibile: avvia Empire Desk (app.py / avvia-app.bat) per usare i tool.');
    } finally {
      setYtBusy(false);
    }
  }, []);

  const refreshEmpireTiles = useCallback(async () => {
    try {
      const tiles = await EmpireApi.getTiles();
      setEmpireTiles(tiles);
      setEmpireAvailable(true);
    } catch {
      setEmpireAvailable(false);
    }
  }, []);

  useEffect(() => {
    refreshEmpireTiles();
    const t = setInterval(refreshEmpireTiles, 4000);
    return () => clearInterval(t);
  }, [refreshEmpireTiles]);

  const pollEmpireTile = useCallback((id: string) => {
    if (pollingRef.current.has(id)) return;
    pollingRef.current.add(id);
    const tick = async () => {
      try {
        const r = await EmpireApi.poll(id);
        if (r.lines.length) {
          setEmpireLogs(prev => {
            const merged = [...(prev[id] || []), ...r.lines];
            return { ...prev, [id]: merged.slice(-200) };
          });
        }
        if (r.running) {
          setTimeout(tick, 700);
        } else {
          pollingRef.current.delete(id);
          if (r.exit_code !== null) {
            setEmpireLogs(prev => ({
              ...prev,
              [id]: [...(prev[id] || []), `--- terminato, exit code: ${r.exit_code} ---`].slice(-200),
            }));
          }
          refreshEmpireTiles();
        }
      } catch {
        pollingRef.current.delete(id);
      }
    };
    tick();
  }, [refreshEmpireTiles]);

  const launchEmpireTile = async (tile: EmpireTile) => {
    setEmpireErrors(prev => ({ ...prev, [tile.id]: '' }));
    const input = tile.input ? (empireInputs[tile.id] || '') : undefined;
    if (tile.input && !input?.trim()) {
      setEmpireErrors(prev => ({ ...prev, [tile.id]: 'serve un input (vedi il campo sulla card)' }));
      return;
    }
    setEmpireLogs(prev => ({ ...prev, [tile.id]: [] }));
    const r = await EmpireApi.launch(tile.id, input);
    if (!r.ok) {
      setEmpireErrors(prev => ({ ...prev, [tile.id]: r.error || 'avvio fallito' }));
      return;
    }
    await refreshEmpireTiles();
    pollEmpireTile(tile.id);
  };

  const empireInputPlaceholder: Record<string, string> = { url: 'URL YouTube…', path: 'Percorso file carosello.json…' };

  const handleCreateRule = (e: React.FormEvent) => {
      e.preventDefault();
      onAddRule({
          id: `rule-${Date.now()}`,
          name: newRule.name || 'Nuova Regola',
          trigger: newRule.trigger as TriggerType,
          action: newRule.action as ActionType,
          active: true,
          runCount: 0,
          lastRun: 'Mai'
      });
      setIsModalOpen(false);
      setNewRule({ name: '', trigger: 'LEAD_CREATED', action: 'NOTIFY_SLACK' });
  };

  const getTriggerLabel = (t: TriggerType) => {
      switch(t) {
          case 'LEAD_CREATED': return 'Nuovo Lead Creato';
          case 'LEAD_WON': return 'Lead Vinto (Deal)';
          case 'TASK_COMPLETED': return 'Task Completato';
          default: return t;
      }
  };

  const getActionLabel = (a: ActionType) => {
      switch(a) {
          case 'CREATE_TASK': return 'Crea Task Onboarding';
          case 'NOTIFY_SLACK': return 'Invia Notifica Slack';
          case 'SEND_EMAIL': return 'Invia Email Automatica';
          default: return a;
      }
  };

  // COMMON STYLE FOR METALLIC MODALS
  const metallicModalClass = "bg-gradient-to-br from-[#cbd5e1] via-[#94a3b8] to-[#64748b] border-t border-l border-white/40 border-b border-r border-black/40 rounded-sm shadow-2xl relative overflow-hidden";
  const metallicInputClass = "bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:border-white/50 focus:ring-0 outline-none rounded-sm shadow-inner";
  const metallicLabelClass = "text-slate-800 font-bold uppercase tracking-widest text-[10px]";

  return (
    <div className="space-y-8 animate-in fade-in duration-500 pb-20">
        <div className="flex justify-between items-end border-b border-white/5 pb-8">
            <div>
                <h1 className="text-4xl font-bold text-silver-gradient mb-2 tracking-tight">Automation Hub</h1>
                <p className="text-platinum-500 text-sm">Automatizza i flussi di lavoro ripetitivi per scalare l'agenzia.</p>
            </div>
            <Button onClick={() => setIsModalOpen(true)} className="bg-white text-black hover:bg-platinum-200" icon={<Plus className="w-4 h-4"/>}>NUOVA REGOLA</Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {rules.map((rule, index) => {
                const silverMixes = [
                    'from-[#1e3a8a] via-[#cbd5e1] to-[#3b82f6] shadow-[0_10px_20px_rgba(30,58,138,0.4)]', // Blue + Silver
                    'from-[#881337] via-[#e2e8f0] to-[#e11d48] shadow-[0_10px_20px_rgba(136,19,55,0.4)]', // Red + Silver
                    'from-[#064e3b] via-[#94a3b8] to-[#10b981] shadow-[0_10px_20px_rgba(6,78,59,0.4)]', // Green + Silver
                    'from-[#78350f] via-[#cbd5e1] to-[#d97706] shadow-[0_10px_20px_rgba(120,53,15,0.4)]', // Amber + Silver
                    'from-[#4c1d95] via-[#e2e8f0] to-[#8b5cf6] shadow-[0_10px_20px_rgba(76,29,149,0.4)]'  // Purple + Silver
                ];
                const activeStyle = silverMixes[index % silverMixes.length];

                return (
                    <div key={rule.id} className={`
                        relative overflow-hidden border p-5 rounded-xl flex flex-col justify-between transition-all duration-300 group min-h-[170px]
                        ${rule.active 
                            ? `bg-gradient-to-br ${activeStyle} border-white/60 hover:-translate-y-1 hover:shadow-[0_15px_30px_rgba(0,0,0,0.6)]` 
                            : 'bg-[#0A0A0A] border-white/10 opacity-60 hover:opacity-100'}
                    `}>
                        {/* Metallic Grain Layer */}
                        {rule.active && <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.25] pointer-events-none mix-blend-multiply"></div>}
                        {rule.active && <div className="absolute top-[-50%] right-[-50%] w-[200%] h-[200%] bg-gradient-to-b from-white/40 via-transparent to-transparent rotate-45 pointer-events-none"></div>}

                        <div className="flex items-start justify-between relative z-10 mb-4">
                            <div className="flex items-center gap-3">
                                <div className={`w-10 h-10 rounded-full flex items-center justify-center border shadow-inner shrink-0
                                    ${rule.active ? 'bg-black/40 border-white/50 text-white backdrop-blur-md' : 'bg-white/5 border-white/10 text-platinum-600'}
                                `}>
                                    <Zap className="w-5 h-5 drop-shadow-md" />
                                </div>
                                <div className="min-w-0">
                                    <div className="flex items-center gap-2 mb-0.5">
                                        <h3 className={`text-sm font-bold tracking-wide truncate ${rule.active ? 'text-white drop-shadow-md' : 'text-platinum-500'}`}>{rule.name}</h3>
                                        {rule.active && <span className="px-1.5 py-0.5 rounded-full bg-black/50 border border-white/30 text-white text-[8px] font-bold uppercase tracking-widest flex items-center gap-1 shrink-0"><Activity className="w-2.5 h-2.5"/> ON</span>}
                                    </div>
                                    <p className={`text-[9px] uppercase font-bold tracking-widest truncate ${rule.active ? 'text-white/80' : 'text-platinum-600'}`}>
                                        <Bell className="w-2.5 h-2.5 inline mr-1" />{getTriggerLabel(rule.trigger)}
                                    </p>
                                </div>
                            </div>
                            <button onClick={() => onToggleRule(rule.id)} className={`w-10 h-5 rounded-full p-0.5 transition-colors border shrink-0 relative z-20 ${rule.active ? 'bg-emerald-500 border-emerald-400 shadow-[0_0_10px_rgba(16,185,129,0.5)]' : 'bg-platinum-800 border-transparent'}`}>
                                <div className={`w-4 h-4 rounded-full shadow-md transform duration-300 bg-white ${rule.active ? 'translate-x-5' : 'translate-x-0'}`}></div>
                            </button>
                        </div>

                        <div className="flex flex-col gap-3 relative z-10 mt-auto">
                            <div className={`p-2 rounded-lg flex items-center gap-2 text-[10px] font-bold tracking-wider ${rule.active ? 'bg-black/40 text-white border border-white/20 backdrop-blur-sm' : 'bg-white/5 text-platinum-500 border border-transparent'}`}>
                                <ArrowRight className="w-3 h-3 opacity-70 shrink-0"/>
                                <CheckCircle2 className="w-3 h-3 shrink-0"/> 
                                <span className="truncate">{getActionLabel(rule.action)}</span>
                            </div>
                            
                            <div className="flex items-center justify-between mt-1">
                                <div className="flex gap-4">
                                    <div>
                                        <p className="text-[8px] uppercase tracking-widest text-white/70 mb-0.5">Esecuzioni</p>
                                        <p className={`text-xs font-mono font-bold ${rule.active ? 'text-white' : 'text-platinum-500'}`}>{rule.runCount}</p>
                                    </div>
                                    <div>
                                        <p className="text-[8px] uppercase tracking-widest text-white/70 mb-0.5">Ultimo Run</p>
                                        <p className={`text-xs font-mono font-bold ${rule.active ? 'text-white' : 'text-platinum-500'}`}>{rule.lastRun}</p>
                                    </div>
                                </div>
                                {onTestRule && (
                                    <button onClick={() => onTestRule(rule.id)} className={`px-3 py-1.5 text-[9px] font-bold uppercase tracking-widest border rounded-md transition-all z-20 relative ${rule.active ? 'bg-white/20 hover:bg-white/30 text-white border-white/40 backdrop-blur-md shadow-sm' : 'bg-white/5 text-platinum-500 border-white/10 hover:bg-white/10 hover:text-white'}`}>
                                        Test Run
                                    </button>
                                )}
                            </div>
                        </div>
                    </div>
                );
            })}
        </div>

        {/* OPERAZIONI REALI (Digital Empire) — subprocess veri via app.py, exit code sempre visibile.
            Additivo alla sezione sopra: qui non sono "regole" ma le automazioni operative reali. */}
        <div className="border-t border-white/5 pt-8">
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h2 className="text-2xl font-bold text-silver-gradient tracking-tight flex items-center gap-3">
                        <Radio className="w-5 h-5 text-diamond-400" /> Operazioni Reali — Digital Empire
                    </h2>
                    <p className="text-platinum-500 text-xs mt-1">Ogni card lancia un processo reale del monorepo. Zero bottoni finti: exit code sempre visibile.</p>
                </div>
                {empireAvailable === false && (
                    <span className="flex items-center gap-2 px-3 py-1.5 rounded-sm bg-amber-950/40 border border-amber-800/50 text-amber-400 text-[10px] font-bold uppercase tracking-wider">
                        <AlertTriangle className="w-3.5 h-3.5" /> Backend non raggiungibile
                    </span>
                )}
            </div>

            {empireAvailable === false && (
                <div className="p-6 rounded-sm bg-[#0A0A0A] border border-white/5 text-platinum-500 text-sm">
                    Aureus non è servita da Empire Desk (app.py) in questo momento — le operazioni reali
                    richiedono l'app avviata da <code className="text-platinum-300">EmpireDesk/avvia-app.bat</code> o l'.exe.
                </div>
            )}

            {empireAvailable !== false && (
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                    {empireTiles.map(tile => {
                        const running = tile.running;
                        const err = empireErrors[tile.id];
                        const lines = empireLogs[tile.id] || [];
                        const lastExit = tile.exit_code;
                        return (
                            <div key={tile.id} className={`
                                relative overflow-hidden border p-5 rounded-sm flex flex-col gap-3 transition-all duration-300
                                ${running
                                    ? 'bg-gradient-to-br from-diamond-300 via-diamond-400 to-diamond-500 border-white/50 shadow-[0_0_30px_rgba(93,138,168,0.3)]'
                                    : 'bg-[#0A0A0A] border-white/5'}
                            `}>
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-3">
                                        <div className={`w-10 h-10 rounded-full flex items-center justify-center border shadow-inner text-lg
                                            ${running ? 'bg-white/20 border-white/40' : 'bg-white/5 border-white/10'}`}>
                                            {tile.icon}
                                        </div>
                                        <div>
                                            <h4 className={`text-sm font-bold ${running ? 'text-slate-900' : 'text-white'}`}>{tile.name}</h4>
                                            <p className={`text-[11px] ${running ? 'text-slate-800' : 'text-platinum-500'}`}>{tile.desc}</p>
                                        </div>
                                    </div>
                                    {running ? (
                                        <span className="px-2 py-0.5 rounded-full bg-slate-900/10 border border-slate-900/20 text-slate-900 text-[9px] font-bold uppercase tracking-wider flex items-center gap-1 shrink-0">
                                            <Activity className="w-3 h-3" /> In corso
                                        </span>
                                    ) : lastExit === 0 ? (
                                        <span className="px-2 py-0.5 rounded-full bg-emerald-900/20 border border-emerald-800/50 text-emerald-400 text-[9px] font-bold uppercase tracking-wider shrink-0">Ultimo OK</span>
                                    ) : lastExit !== null && lastExit !== undefined ? (
                                        <span className="px-2 py-0.5 rounded-full bg-red-950/40 border border-red-800/50 text-red-400 text-[9px] font-bold uppercase tracking-wider shrink-0">Errore ({lastExit})</span>
                                    ) : (
                                        <span className="px-2 py-0.5 rounded-full bg-white/5 border border-white/10 text-platinum-500 text-[9px] font-bold uppercase tracking-wider shrink-0">Idle</span>
                                    )}
                                </div>

                                {tile.kind === 'readonly' ? (
                                    <div className="text-[10px] text-platinum-600 uppercase tracking-widest font-mono">Sola lettura — vedi STATO Empire</div>
                                ) : (
                                    <>
                                        {tile.input && (
                                            <input
                                                className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60"
                                                placeholder={empireInputPlaceholder[tile.input] || 'Input…'}
                                                value={empireInputs[tile.id] || ''}
                                                onChange={e => setEmpireInputs(prev => ({ ...prev, [tile.id]: e.target.value }))}
                                                disabled={running}
                                            />
                                        )}
                                        <button
                                            onClick={() => launchEmpireTile(tile)}
                                            disabled={running}
                                            className={`px-4 py-2 text-[10px] font-bold uppercase tracking-widest border rounded-sm transition-colors shadow-sm self-start
                                                ${running
                                                    ? 'bg-slate-900/20 text-slate-800 border-slate-900/20 cursor-default'
                                                    : 'bg-white/5 hover:bg-white/10 border-white/10 text-platinum-300 hover:text-white'}`}
                                        >
                                            {running ? 'In corso…' : 'Avvia'}
                                        </button>
                                        {err && <p className="text-[10px] text-red-400 font-mono">{err}</p>}
                                    </>
                                )}

                                {lines.length > 0 && (
                                    <pre className="mt-1 max-h-28 overflow-y-auto custom-scrollbar bg-black/40 border border-white/10 rounded-sm p-2 text-[10px] font-mono text-platinum-300 whitespace-pre-wrap">
                                        {lines.slice(-12).join('\n')}
                                    </pre>
                                )}
                            </div>
                        );
                    })}
                    {empireAvailable === true && empireTiles.length === 0 && (
                        <p className="text-platinum-600 text-xs col-span-full">Nessuna automazione registrata.</p>
                    )}
                </div>
            )}
        </div>

        {/* YOUTUBE AUTOMATION FACTORY — modulo youtube (skill /yt-factory).
            Additivo: tool deterministici (SEO score, Cash Cow) usabili qui; la parte agentica gira in Claude Code.
            MAI numeri inventati: se il backend non risponde, lo dichiara. */}
        <div className="border-t border-white/5 pt-8">
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h2 className="text-2xl font-bold text-silver-gradient tracking-tight flex items-center gap-3">
                        <Youtube className="w-5 h-5 text-diamond-400" /> YouTube Automation Factory
                    </h2>
                    <p className="text-platinum-500 text-xs mt-1">Fabbrica cash cow: analisi SEO e indice canale su dati reali che inserisci. Pipeline completa con agenti via <code className="text-platinum-300">/yt-factory</code>.</p>
                </div>
                <Button onClick={() => ytRun(() => EmpireApi.youtubeInfo())} disabled={ytBusy}
                    className="bg-white/5 hover:bg-white/10 border border-white/10 text-platinum-300 hover:text-white" icon={<Radio className="w-4 h-4"/>}>
                    Mostra fabbrica
                </Button>
            </div>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-4">
                {/* Card 1 — Punteggio SEO */}
                <div className="bg-[#0A0A0A] border border-white/5 rounded-sm p-5 flex flex-col gap-3">
                    <h4 className="text-sm font-bold text-white flex items-center gap-2"><CheckCircle2 className="w-4 h-4 text-diamond-400"/> Punteggio SEO di un video</h4>
                    <input className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60"
                        placeholder="Titolo del video" value={ytSeo.title} onChange={e => setYtSeo({ ...ytSeo, title: e.target.value })} />
                    <input className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60"
                        placeholder="Keyword principale" value={ytSeo.keyword} onChange={e => setYtSeo({ ...ytSeo, keyword: e.target.value })} />
                    <textarea className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60 min-h-[64px]"
                        placeholder="Descrizione (prime 2 righe = hook + valore)" value={ytSeo.description} onChange={e => setYtSeo({ ...ytSeo, description: e.target.value })} />
                    <input className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60"
                        placeholder="Tag separati da virgola" value={ytSeo.tags} onChange={e => setYtSeo({ ...ytSeo, tags: e.target.value })} />
                    <div className="flex items-center gap-4 text-[11px] text-platinum-400">
                        <label className="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked={ytSeo.thumbnail} onChange={e => setYtSeo({ ...ytSeo, thumbnail: e.target.checked })} /> miniatura pronta</label>
                        <label className="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked={ytSeo.subtitles} onChange={e => setYtSeo({ ...ytSeo, subtitles: e.target.checked })} /> sottotitoli</label>
                    </div>
                    <button onClick={() => ytRun(() => EmpireApi.youtubeSeoScore(ytSeo))} disabled={ytBusy}
                        className="px-4 py-2 text-[10px] font-bold uppercase tracking-widest border rounded-sm self-start bg-white/5 hover:bg-white/10 border-white/10 text-platinum-300 hover:text-white transition-colors">
                        {ytBusy ? 'Calcolo…' : 'Calcola SEO'}
                    </button>
                </div>

                {/* Card 2 — Indice Cash Cow */}
                <div className="bg-[#0A0A0A] border border-white/5 rounded-sm p-5 flex flex-col gap-3">
                    <h4 className="text-sm font-bold text-white flex items-center gap-2"><Activity className="w-4 h-4 text-diamond-400"/> Indice Cash Cow di un canale</h4>
                    <p className="text-[11px] text-platinum-500">Incolla i video del canale (views + età in ore, letti con Video IQ da account neutro).</p>
                    <textarea className="bg-black/30 border border-white/10 text-white placeholder-platinum-600 text-xs font-mono rounded-sm px-3 py-2 outline-none focus:border-diamond-500/60 min-h-[120px]"
                        value={ytVideos} onChange={e => setYtVideos(e.target.value)} />
                    <button onClick={() => ytRun(() => EmpireApi.youtubeCashcow({ channel: 'canale', videos: ytVideos }))} disabled={ytBusy}
                        className="px-4 py-2 text-[10px] font-bold uppercase tracking-widest border rounded-sm self-start bg-white/5 hover:bg-white/10 border-white/10 text-platinum-300 hover:text-white transition-colors">
                        {ytBusy ? 'Calcolo…' : 'Calcola Cash Cow'}
                    </button>
                </div>
            </div>

            <pre className="mt-4 max-h-64 overflow-y-auto custom-scrollbar bg-black/40 border border-white/10 rounded-sm p-3 text-[11px] font-mono text-platinum-300 whitespace-pre-wrap">
                {ytOut}
            </pre>
        </div>

        {/* LOGS PANEL */}
        <div className="mt-12 border border-white/10 rounded-sm overflow-hidden bg-[#050505]">
            <div className="p-4 bg-[#0F0F0F] border-b border-white/10 flex items-center gap-2">
                <Terminal className="w-4 h-4 text-platinum-500" />
                <h3 className="text-xs font-bold text-white uppercase tracking-widest">Registro Esecuzioni (Live Logs)</h3>
            </div>
            <div className="max-h-60 overflow-y-auto custom-scrollbar p-0">
                {logs.length === 0 ? (
                    <div className="p-8 text-center text-[10px] text-platinum-600 uppercase tracking-widest font-mono">
                        In attesa di eventi...
                    </div>
                ) : (
                    <table className="w-full text-left text-xs font-mono">
                        <thead className="bg-[#0A0A0A] text-platinum-600 sticky top-0">
                            <tr>
                                <th className="p-3 w-32 border-b border-white/5">Orario</th>
                                <th className="p-3 w-48 border-b border-white/5">Regola</th>
                                <th className="p-3 w-24 border-b border-white/5">Stato</th>
                                <th className="p-3 border-b border-white/5">Dettagli Azione</th>
                            </tr>
                        </thead>
                        <tbody>
                            {logs.map(log => (
                                <tr key={log.id} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                                    <td className="p-3 text-platinum-500">{log.date}</td>
                                    <td className="p-3 text-white font-bold">{log.ruleName}</td>
                                    <td className="p-3">
                                        <span className="text-green-400 bg-green-900/20 px-2 py-0.5 rounded text-[9px] border border-green-900/50 uppercase tracking-wide">
                                            {log.status}
                                        </span>
                                    </td>
                                    <td className="p-3 text-platinum-300">{log.details}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>

        {isModalOpen && (
             <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
                <div className={`${metallicModalClass} w-full max-w-lg p-10`}>
                     {/* Texture */}
                     <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-overlay"></div>

                     <button onClick={() => setIsModalOpen(false)} className="absolute top-6 right-6 text-slate-700 hover:text-red-600 transition-colors z-20"><X className="w-6 h-6"/></button>
                     <h3 className="text-2xl font-black text-slate-900 mb-8 uppercase tracking-widest flex items-center gap-3 relative z-10">
                         <Zap className="w-6 h-6 text-slate-800" /> Nuova Automazione
                     </h3>
                     
                     <form onSubmit={handleCreateRule} className="space-y-6 relative z-10">
                         <div className="space-y-2">
                             <label className={metallicLabelClass}>Nome Regola</label>
                             <input className={`${metallicInputClass} w-full p-3`} 
                                value={newRule.name} onChange={e => setNewRule({...newRule, name: e.target.value})} placeholder="Es. Notifica Slack per nuovi lead" required />
                         </div>
                         <div className="grid grid-cols-2 gap-6">
                             <div className="space-y-2">
                                 <label className={metallicLabelClass}>Trigger (Quando)</label>
                                 <select className={`${metallicInputClass} w-full p-3`} 
                                    value={newRule.trigger} onChange={e => setNewRule({...newRule, trigger: e.target.value as any})}>
                                     <option value="LEAD_CREATED">Nuovo Lead Creato</option>
                                     <option value="LEAD_WON">Lead Vinto</option>
                                     <option value="TASK_COMPLETED">Task Completato</option>
                                 </select>
                             </div>
                             <div className="space-y-2">
                                 <label className={metallicLabelClass}>Action (Fai)</label>
                                 <select className={`${metallicInputClass} w-full p-3`} 
                                    value={newRule.action} onChange={e => setNewRule({...newRule, action: e.target.value as any})}>
                                     <option value="NOTIFY_SLACK">Notifica Slack</option>
                                     <option value="SEND_EMAIL">Invia Email</option>
                                     <option value="CREATE_TASK">Crea Task</option>
                                 </select>
                             </div>
                         </div>
                         <div className="flex gap-4 pt-4">
                             <Button type="submit" className="w-full py-4 font-bold tracking-[0.2em] uppercase bg-slate-900 text-white hover:bg-slate-800 border-none shadow-lg">Crea Automazione</Button>
                         </div>
                     </form>
                </div>
             </div>
        )}
    </div>
  );
};
