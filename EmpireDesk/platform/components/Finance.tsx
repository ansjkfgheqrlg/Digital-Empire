
import React, { useState } from 'react';
import { DollarSign, TrendingDown, TrendingUp, Wallet, Download, ArrowUpRight, ArrowDownRight } from 'lucide-react';
import { Button } from './ui/Button';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface Transaction {
    id: string;
    date: string;
    description: string;
    category: 'INCOME' | 'EXPENSE_ADS' | 'EXPENSE_SOFTWARE' | 'EXPENSE_TEAM' | 'EXPENSE_OTHER';
    amount: number;
    status: 'COMPLETED' | 'PENDING';
}

const MOCK_TRANSACTIONS: Transaction[] = [
    { id: 'tx-1', date: '2024-03-15', description: 'Pagamento Cliente: Digital Spa', category: 'INCOME', amount: 2500, status: 'COMPLETED' },
    { id: 'tx-2', date: '2024-03-14', description: 'Meta Ads Spending', category: 'EXPENSE_ADS', amount: -450, status: 'COMPLETED' },
    { id: 'tx-3', date: '2024-03-12', description: 'Abbonamento OpenAI', category: 'EXPENSE_SOFTWARE', amount: -20, status: 'COMPLETED' },
    { id: 'tx-4', date: '2024-03-10', description: 'Freelance Copywriter', category: 'EXPENSE_TEAM', amount: -300, status: 'PENDING' },
    { id: 'tx-5', date: '2024-03-08', description: 'Vendita Corso: YouTube Auto', category: 'INCOME', amount: 997, status: 'COMPLETED' },
    { id: 'tx-6', date: '2024-03-05', description: 'Shopify Subscription', category: 'EXPENSE_SOFTWARE', amount: -29, status: 'COMPLETED' },
];

const CHART_DATA = [
    { name: 'Gen', profit: 1200 }, { name: 'Feb', profit: 3500 }, { name: 'Mar', profit: 2800 },
    { name: 'Apr', profit: 4500 }, { name: 'Mag', profit: 4200 }, { name: 'Giu', profit: 5800 },
];

export const Finance: React.FC = () => {
  const [filter, setFilter] = useState<'ALL' | 'INCOME' | 'EXPENSE'>('ALL');

  const income = MOCK_TRANSACTIONS.filter(t => t.amount > 0).reduce((acc, t) => acc + t.amount, 0);
  const expenses = MOCK_TRANSACTIONS.filter(t => t.amount < 0).reduce((acc, t) => acc + Math.abs(t.amount), 0);
  const balance = income - expenses;

  const filteredTransactions = MOCK_TRANSACTIONS.filter(t => {
      if (filter === 'INCOME') return t.amount > 0;
      if (filter === 'EXPENSE') return t.amount < 0;
      return true;
  });

  const getCategoryLabel = (cat: string) => {
      switch(cat) {
          case 'INCOME': return { label: 'Entrata', color: 'text-emerald-700 bg-emerald-100 border-emerald-200' };
          case 'EXPENSE_ADS': return { label: 'Ads', color: 'text-blue-700 bg-blue-100 border-blue-200' };
          case 'EXPENSE_SOFTWARE': return { label: 'Software', color: 'text-purple-700 bg-purple-100 border-purple-200' };
          case 'EXPENSE_TEAM': return { label: 'Team', color: 'text-orange-700 bg-orange-100 border-orange-200' };
          default: return { label: 'Altro', color: 'text-slate-600 bg-slate-100 border-slate-200' };
      }
  };

  // --- TRUE METAL STYLES ---
  
  // 1. Pure Silver (Netto & Main Blocks)
  const pureSilverBlock = `
    bg-gradient-to-br from-[#ffffff] via-[#e2e8f0] to-[#94a3b8] 
    border-t border-l border-white/90 border-b border-r border-slate-500/60
    rounded-sm p-6 shadow-[0_10px_20px_-5px_rgba(0,0,0,0.5),inset_0_1px_0_rgba(255,255,255,0.8)]
    relative overflow-hidden group
  `;
  const silverTextMain = "text-slate-900 drop-shadow-[0_1px_0_rgba(255,255,255,0.5)]";
  const silverTextSub = "text-slate-600 font-medium";

  // 2. Green Silver (Argento Verde - Metallic Emerald)
  const greenSilverBlock = `
    bg-gradient-to-br from-[#ecfdf5] via-[#a7f3d0] to-[#059669]
    border-t border-l border-white/70 border-b border-r border-emerald-800/50
    rounded-sm p-6 shadow-[0_10px_20px_-5px_rgba(5,150,105,0.4),inset_0_1px_0_rgba(255,255,255,0.6)]
    relative overflow-hidden group
  `;
  const greenTextMain = "text-emerald-950 drop-shadow-[0_1px_0_rgba(255,255,255,0.3)]";
  const greenTextSub = "text-emerald-900 font-bold";

  // 3. Red Silver (Argento Rosso - Metallic Rose)
  const redSilverBlock = `
    bg-gradient-to-br from-[#fff1f2] via-[#fecdd3] to-[#e11d48]
    border-t border-l border-white/70 border-b border-r border-rose-800/50
    rounded-sm p-6 shadow-[0_10px_20px_-5px_rgba(225,29,72,0.4),inset_0_1px_0_rgba(255,255,255,0.6)]
    relative overflow-hidden group
  `;
  const redTextMain = "text-rose-950 drop-shadow-[0_1px_0_rgba(255,255,255,0.3)]";
  const redTextSub = "text-rose-900 font-bold";

  const MetallicTexture = () => (
      <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.1] pointer-events-none mix-blend-multiply"></div>
  );

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
        <div className="flex justify-between items-end border-b border-white/10 pb-6">
            <div>
                <h1 className="text-4xl font-black text-silver-gradient mb-2 tracking-tight">
                    Tesoreria & Finanza
                </h1>
                <p className="text-platinum-500 text-sm">Monitoraggio Cash Flow e gestione spese operative.</p>
            </div>
            <div className="flex gap-3">
                <Button variant="outline" icon={<Download className="w-4 h-4"/>}>Report Fiscale</Button>
                <Button variant="diamond" icon={<DollarSign className="w-4 h-4"/>}>Registra Movimento</Button>
            </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            
            {/* Card 1: PURE SILVER (Net) */}
            <div className={pureSilverBlock}>
                <MetallicTexture />
                <div className="flex justify-between items-start mb-4 relative z-10">
                    <span className={`text-[10px] font-bold uppercase tracking-widest ${silverTextSub}`}>Saldo Netto</span>
                    <div className="p-2 bg-slate-900/5 rounded-full border border-slate-900/10 shadow-sm">
                        <Wallet className="w-5 h-5 text-slate-900"/>
                    </div>
                </div>
                <div className={`text-4xl font-black mb-2 tracking-tighter relative z-10 ${silverTextMain}`}>€{balance.toLocaleString()}</div>
                <div className="flex items-center gap-1 text-[10px] text-slate-800 font-bold bg-white/40 px-2 py-1 rounded-sm w-fit border border-white/50 relative z-10 shadow-sm">
                    <ArrowUpRight className="w-3 h-3" /> +12% vs mese scorso
                </div>
            </div>

            {/* Card 2: GREEN SILVER (Income) */}
            <div className={greenSilverBlock}>
                <MetallicTexture />
                <div className="flex justify-between items-start mb-4 relative z-10">
                    <span className={`text-[10px] font-bold uppercase tracking-widest ${greenTextSub}`}>Entrate (Mese)</span>
                    <div className="p-2 bg-emerald-900/10 rounded-full border border-emerald-900/10 shadow-sm">
                        <TrendingUp className="w-5 h-5 text-emerald-900"/>
                    </div>
                </div>
                <div className={`text-4xl font-black mb-2 tracking-tighter relative z-10 ${greenTextMain}`}>€{income.toLocaleString()}</div>
                <div className="w-full bg-emerald-900/10 h-1.5 rounded-full mt-4 overflow-hidden relative z-10 border-b border-white/20">
                    <div className="bg-emerald-800 h-full w-[70%] shadow-[0_0_5px_rgba(6,78,59,0.5)]"></div>
                </div>
            </div>

            {/* Card 3: RED SILVER (Expenses) */}
            <div className={redSilverBlock}>
                <MetallicTexture />
                <div className="flex justify-between items-start mb-4 relative z-10">
                    <span className={`text-[10px] font-bold uppercase tracking-widest ${redTextSub}`}>Uscite (Mese)</span>
                    <div className="p-2 bg-rose-900/10 rounded-full border border-rose-900/10 shadow-sm">
                        <TrendingDown className="w-5 h-5 text-rose-900"/>
                    </div>
                </div>
                <div className={`text-4xl font-black mb-2 tracking-tighter relative z-10 ${redTextMain}`}>€{expenses.toLocaleString()}</div>
                <div className="w-full bg-rose-900/10 h-1.5 rounded-full mt-4 overflow-hidden relative z-10 border-b border-white/20">
                    <div className="bg-rose-800 h-full w-[30%] shadow-[0_0_5px_rgba(136,19,55,0.5)]"></div>
                </div>
            </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className={`lg:col-span-2 ${pureSilverBlock} flex flex-col h-[400px]`}>
                <MetallicTexture />
                <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 relative z-10 ${silverTextMain}`}>Cash Flow Trend</h3>
                <div className="flex-1 w-full min-h-0 relative z-10">
                    <ResponsiveContainer width="100%" height="100%">
                        <AreaChart data={CHART_DATA}>
                            <defs>
                                <linearGradient id="colorProfitLight" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="5%" stopColor="#0F172A" stopOpacity={0.2}/>
                                    <stop offset="95%" stopColor="#0F172A" stopOpacity={0}/>
                                </linearGradient>
                            </defs>
                            <CartesianGrid strokeDasharray="3 3" stroke="#94a3b8" vertical={false} opacity={0.5} />
                            <XAxis dataKey="name" stroke="#475569" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} axisLine={false} tickLine={false} dy={10} />
                            <YAxis stroke="#475569" tick={{fill: '#475569', fontSize: 10, fontWeight: 'bold'}} tickFormatter={(val) => `€${val}`} axisLine={false} tickLine={false} dx={-10} />
                            <Tooltip contentStyle={{ backgroundColor: '#fff', borderColor: '#cbd5e1', borderRadius: '4px', color: '#0f172a', fontWeight: 'bold', boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)' }} />
                            <Area type="monotone" dataKey="profit" stroke="#0F172A" strokeWidth={3} fillOpacity={1} fill="url(#colorProfitLight)" />
                        </AreaChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* Breakdown Spese - Also Pure Silver now for consistency */}
            <div className={`${pureSilverBlock} p-6`}>
                <MetallicTexture />
                <h3 className={`text-xs font-bold uppercase tracking-widest mb-6 relative z-10 ${silverTextMain}`}>Breakdown Spese</h3>
                <div className="space-y-6 relative z-10">
                    {[{ label: 'Ads Spending', amount: 1200, color: 'bg-blue-600' }, { label: 'Team & Payroll', amount: 800, color: 'bg-orange-600' }, { label: 'Software & Tools', amount: 350, color: 'bg-purple-600' }, { label: 'Ufficio & Varie', amount: 150, color: 'bg-slate-600' }].map((item, idx) => (
                        <div key={idx} className="group">
                            <div className="flex justify-between text-xs mb-2">
                                <span className={`font-bold uppercase tracking-wide ${silverTextSub}`}>{item.label}</span>
                                <span className={`font-black font-mono ${silverTextMain}`}>€{item.amount}</span>
                            </div>
                            <div className="w-full bg-slate-200 h-2 rounded-full overflow-hidden border border-white/50 shadow-inner">
                                <div className={`h-full ${item.color} shadow-[0_0_5px_currentColor]`} style={{width: `${(item.amount / 2500) * 100}%`}}></div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>

        {/* --- ULTIMI MOVIMENTI --- */}
        <div className={pureSilverBlock}>
            <MetallicTexture />
            
            <div className="p-4 border-b border-slate-300/50 bg-white/40 flex justify-between items-center relative z-10 backdrop-blur-sm rounded-t-sm">
                <h3 className={`text-xs font-bold uppercase tracking-widest ${silverTextMain}`}>Ultimi Movimenti</h3>
                <div className="flex bg-slate-200/50 rounded-sm p-0.5 border border-white/50 shadow-inner">
                    <button onClick={() => setFilter('ALL')} className={`px-3 py-1 text-[10px] font-bold uppercase rounded-sm transition-all ${filter === 'ALL' ? 'bg-white text-slate-900 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-900'}`}>Tutti</button>
                    <button onClick={() => setFilter('INCOME')} className={`px-3 py-1 text-[10px] font-bold uppercase rounded-sm transition-all ${filter === 'INCOME' ? 'bg-white text-slate-900 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-900'}`}>Entrate</button>
                    <button onClick={() => setFilter('EXPENSE')} className={`px-3 py-1 text-[10px] font-bold uppercase rounded-sm transition-all ${filter === 'EXPENSE' ? 'bg-white text-slate-900 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-900'}`}>Uscite</button>
                </div>
            </div>
            
            <table className="w-full text-left relative z-10">
                <thead className="bg-slate-100/50 text-[9px] font-bold text-slate-500 uppercase tracking-widest border-b border-slate-300">
                    <tr>
                        <th className="px-6 py-4">Data</th>
                        <th className="px-6 py-4">Descrizione</th>
                        <th className="px-6 py-4">Categoria</th>
                        <th className="px-6 py-4 text-right">Importo</th>
                        <th className="px-6 py-4 text-right">Stato</th>
                    </tr>
                </thead>
                <tbody className="divide-y divide-slate-300/50 text-xs font-medium">
                    {filteredTransactions.map(tx => {
                        const catStyle = getCategoryLabel(tx.category);
                        return (
                            <tr key={tx.id} className="hover:bg-white/40 transition-colors">
                                <td className="px-6 py-4 font-mono font-bold text-slate-500">{tx.date}</td>
                                <td className="px-6 py-4 font-bold text-slate-900">{tx.description}</td>
                                <td className="px-6 py-4">
                                    <span className={`px-2 py-0.5 rounded-sm border text-[9px] font-bold uppercase shadow-sm ${catStyle.color}`}>
                                        {catStyle.label}
                                    </span>
                                </td>
                                <td className={`px-6 py-4 text-right font-mono font-black text-sm ${tx.amount > 0 ? 'text-emerald-700' : 'text-slate-900'}`}>
                                    {tx.amount > 0 ? '+' : ''}€{tx.amount.toLocaleString()}
                                </td>
                                <td className="px-6 py-4 text-right">
                                    {tx.status === 'COMPLETED' ? (
                                        <span className="text-emerald-700 font-black text-[9px] uppercase tracking-wider bg-emerald-100 px-2 py-1 rounded border border-emerald-200">
                                            Completo
                                        </span>
                                    ) : (
                                        <span className="text-amber-700 font-black text-[9px] uppercase tracking-wider bg-amber-100 px-2 py-1 rounded border border-amber-200">
                                            In Attesa
                                        </span>
                                    )}
                                </td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    </div>
  );
};
