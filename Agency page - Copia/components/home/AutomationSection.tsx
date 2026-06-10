
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import {
   Bot, Zap, Activity, ShieldAlert, Cpu, ArrowRight, Database, XCircle, CheckCircle2, TrendingUp, Scale, AlertTriangle, Clock, Ban
} from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';
import { AutomationHeader, UserIcon } from './AutomationParts';

const MotionDiv = motion.div as any;

export const AutomationSection: React.FC = () => {
   const [activeCrime, setActiveCrime] = useState<number>(0);

   const crimes = [
      {
         id: "C-01",
         title: "Lentezza Operativa",
         desc: "Un umano impiega in media 25 minuti per rispondere a un lead. In quel tempo, il cliente ha già comprato dal concorrente.",
         penalty: "Perdita del 60% delle conversioni.",
         icon: Clock
      },
      {
         id: "C-02",
         title: "Errore di Trascrizione",
         desc: "Copiare dati da Excel al CRM porta a un tasso di errore del 18%. Numeri sbagliati, email perse, fatture errate.",
         penalty: "Danno d'immagine e contabile.",
         icon: Activity
      },
      {
         id: "C-03",
         title: "Burnout del Personale",
         desc: "Costringere talenti creativi a fare data-entry ripetitivo uccide la produttività e aumenta il turnover.",
         penalty: "Costi di riassunzione elevati.",
         icon: UserIcon
      }
   ];

   return (
      <section id="automation" className="py-20 md:py-32 relative overflow-hidden bg-[#020617]">
         <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#020617]">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_30%,#0f2e4a_0%,#020617_70%)] opacity-100" />
            <div className="absolute inset-0 opacity-[0.35]" style={{ backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")', filter: 'contrast(170%) brightness(150%) invert(100%)' }} />
            <div className="absolute inset-0 opacity-[0.3] mix-blend-screen" style={{ backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`, backgroundSize: '150px 150px', filter: 'contrast(150%)' }} />
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#020617_100%)] opacity-50" />
         </div>

         <div className="container mx-auto px-6 md:px-12 relative z-10 max-w-7xl">
            <AutomationHeader />

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-24 mb-32 items-start relative">
               <div className="lg:col-span-7 flex flex-col gap-6 relative z-10">
                  <div className="flex items-center gap-4 mb-4 border-b border-white/10 pb-4">
                     <ShieldAlert size={20} className="text-sky-300" />
                     <h3 className="font-mono text-xs font-bold uppercase tracking-[0.3em] text-sky-200/60">Registro Inefficienze</h3>
                  </div>

                  {crimes.map((crime, idx) => (
                     <div key={idx} onClick={() => setActiveCrime(idx)} className={`relative p-[1px] group cursor-pointer transition-all duration-500 rounded-xl ${activeCrime === idx ? 'scale-[1.02] z-20 shadow-[0_10px_40px_rgba(255,255,255,0.1)]' : 'hover:opacity-80 z-10'}`} style={{ background: activeCrime === idx ? 'linear-gradient(135deg, #FFFFFF 0%, #94A3B8 50%, #475569 100%)' : 'linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%)' }}>
                        <div className={`relative h-full p-6 md:p-8 bg-[#020617]/90 backdrop-blur-md rounded-xl transition-colors duration-300 overflow-hidden ${activeCrime === idx ? 'bg-[#0f172a]/95' : ''}`}>
                           <div className="flex flex-col md:flex-row items-start gap-6 relative z-10">
                              <div className={`p-3 rounded-lg border flex-shrink-0 transition-colors duration-300 ${activeCrime === idx ? 'border-slate-300 text-white bg-slate-700/50 shadow-[0_0_20px_rgba(255,255,255,0.2)]' : 'border-white/10 text-gray-500 bg-white/5'}`}>
                                 <crime.icon size={28} />
                              </div>
                              <div className="flex-grow">
                                 <div className="flex flex-wrap justify-between items-center mb-3 gap-2">
                                    <h4 className={`text-xl font-serif font-bold ${activeCrime === idx ? 'text-white' : 'text-gray-400'}`}>{crime.title}</h4>
                                    <span className={`font-mono text-[10px] font-bold tracking-widest py-1 px-2 border rounded ${activeCrime === idx ? 'text-white border-white' : 'text-gray-600 border-white/5'}`}>{crime.id}</span>
                                 </div>
                                 <p className="text-sm text-gray-400 leading-relaxed mb-5 font-light">{crime.desc}</p>
                                 <div className={`inline-flex items-center gap-2 text-[10px] font-mono uppercase tracking-widest font-bold border-l-2 pl-3 ${activeCrime === idx ? 'text-slate-300 border-slate-300' : 'text-gray-600 border-gray-700'}`}>
                                    <Ban size={12} /> PENALITÀ: <span className="text-white">{crime.penalty}</span>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  ))}
               </div>

               <div className="lg:col-span-5 relative h-full min-h-[500px]">
                  <div className="sticky top-32 w-full">
                     <div className="p-[2px] bg-gradient-to-b from-white via-slate-400 to-slate-800 shadow-[0_0_60px_rgba(255,255,255,0.1)] rounded-2xl">
                        <div className="bg-[#020617]/95 backdrop-blur-xl p-8 md:p-10 relative overflow-hidden rounded-2xl">
                           <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_50%,rgba(0,0,0,0.25)_50%),linear-gradient(90deg,rgba(255,255,255,0.03),rgba(255,255,255,0.01))] z-0 bg-[length:100%_2px,3px_100%] pointer-events-none opacity-50"></div>
                           <div className="relative z-10">
                              <div className="flex items-center gap-3 mb-8 text-slate-200 border-b border-white/10 pb-4">
                                 <AlertTriangle size={20} className="text-white animate-pulse" />
                                 <span className="font-mono text-[10px] font-black uppercase tracking-[0.3em]">Allerta Critica</span>
                              </div>
                              <h3 className="font-serif text-2xl md:text-3xl text-white mb-2 leading-tight">STAI BRUCIANDO</h3>
                              <div className="text-5xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white via-slate-200 to-slate-500 tracking-tighter mb-4 filter drop-shadow-[0_0_15px_rgba(255,255,255,0.4)]">€4.500</div>
                              <p className="text-[10px] font-mono text-gray-500 uppercase tracking-[0.2em] mb-10">Al Mese in Inefficienza Operativa</p>
                              <div className="space-y-4 font-mono text-xs mb-10">
                                 <div className="flex justify-between items-center py-2 border-b border-dashed border-gray-800"><span className="text-gray-500">COSTO STAFF MANUALE</span><span className="text-white font-bold">€3.200</span></div>
                                 <div className="flex justify-between items-center py-2 border-b border-dashed border-gray-800"><span className="text-gray-500">LEAD PERSI (STIMATI)</span><span className="text-white font-bold">€1.300</span></div>
                                 <div className="flex justify-between items-center py-4 border-t border-white/20 mt-4 bg-white/5 px-4 -mx-4 rounded"><span className="text-slate-300 font-bold uppercase">Totale Spreco Annuo</span><span className="text-white font-black text-sm">€54.000</span></div>
                              </div>
                              <div className="text-center pt-4"><div className="flex justify-center"><div className="p-3 border border-white/30 rounded-full animate-bounce text-white bg-white/10 hover:bg-white/20 transition-colors cursor-pointer shadow-[0_0_15px_rgba(255,255,255,0.2)]"><ArrowRight size={20} className="rotate-90" /></div></div></div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>

            <div className="relative mt-20 border-t border-white/5 pt-24 text-center mb-20 relative z-10">
               <span className="px-4 py-2 border border-slate-500/30 bg-[#0f2e4a]/60 backdrop-blur-md text-sky-200 font-mono text-[10px] font-black uppercase tracking-[0.2em] mb-8 inline-block rounded-full shadow-[0_0_15px_rgba(14,165,233,0.1)]">Protocollo Correttivo Attivato</span>
               <h2 className="text-4xl md:text-6xl lg:text-7xl font-serif font-black text-white mb-8 tracking-tight drop-shadow-xl">L'ERA DELL' <span className="text-transparent bg-clip-text bg-gradient-to-r from-slate-200 to-white drop-shadow-lg">AUTOMAZIONE</span></h2>
               <p className="max-w-2xl mx-auto text-lg text-gray-300 font-light leading-relaxed">Sostituiamo processi umani fallibili con infrastrutture digitali perfette.<br />Più veloce. Più economico. Senza errori.</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
               {[
                  { title: "Agente Neurale H24", desc: "Mentre tu dormi, il nostro sistema qualifica i lead, risponde alle domande e fissa appuntamenti sul tuo calendario.", icon: Bot, check: "Zero Tempi Morti" },
                  { title: "Sync Istantaneo", desc: "Colleghiamo Ads, Sito e CRM. I dati scorrono fluidi come acqua. Nessun copia-incolla. Nessun dato perso.", icon: Database, zap: "Real-Time Processing", active: true },
                  { title: "Margine Puro", desc: "Riducendo i costi operativi del 70% e aumentando la conversione dei lead, il tuo margine netto esplode.", icon: TrendingUp, scale: "ROI Massimizzato" }
               ].map((card, i) => (
                  <div key={i} className={`p-10 transition-all duration-500 group relative overflow-hidden rounded-xl shadow-2xl ${card.active ? 'bg-gradient-to-b from-[#1e293b]/90 to-[#020617]/90 border border-slate-400/30' : 'bg-[#020617]/80 backdrop-blur-md border border-white/10'}`}>
                     {card.active && <div className="absolute top-0 left-0 w-full h-[1px] bg-white/50"></div>}
                     <div className="absolute top-4 right-4 text-white animate-pulse"><Activity size={18} /></div>
                     <div className={`w-16 h-16 rounded-xl flex items-center justify-center mb-8 border transition-all ${card.active ? 'bg-slate-900/50 border-slate-400/30 text-white shadow-[0_0_20px_rgba(255,255,255,0.1)]' : 'bg-white/5 border-white/10 group-hover:bg-white/10 group-hover:text-white'}`}><card.icon size={32} /></div>
                     <h3 className="text-2xl font-bold font-serif text-white mb-4">{card.title}</h3>
                     <p className={`text-sm leading-relaxed mb-8 ${card.active ? 'text-gray-300 font-medium' : 'text-gray-400 font-light'}`}>{card.desc}</p>
                     <div className="flex items-center gap-2 text-[10px] font-mono uppercase font-bold text-gray-600 group-hover:text-white transition-colors">
                        {card.check && <CheckCircle2 size={12} />} {card.zap && <Zap size={12} />} {card.scale && <Scale size={12} />}
                        {card.check || card.zap || card.scale}
                     </div>
                  </div>
               ))}
            </div>

            <div className="mt-32 md:mt-40 border border-white/10 bg-[#020617]/80 backdrop-blur-md relative rounded-2xl overflow-hidden shadow-2xl">
               <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 bg-black rounded-full flex items-center justify-center border border-white/20 shadow-xl z-20 font-black text-white italic text-lg">VS</div>
               <div className="grid grid-cols-1 md:grid-cols-2 gap-0 divide-y md:divide-y-0 md:divide-x divide-white/10">
                  <div className="p-12 md:p-16 text-center opacity-50 hover:opacity-100 transition-opacity duration-500 bg-[#0a0a0a]">
                     <div className="inline-block p-5 border border-dashed border-gray-700 rounded-full mb-8"><UserIcon size={40} className="text-gray-500" /></div>
                     <h4 className="text-xl font-bold uppercase tracking-widest text-gray-500 mb-8">Il Vecchio Metodo</h4>
                     <ul className="space-y-4 text-xs font-mono text-gray-500 text-left mx-auto max-w-xs">
                        <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700" /> Costi Fissi Alti</li>
                        <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700" /> Lento (9-18h)</li>
                        <li className="flex items-center gap-4"><XCircle size={16} className="text-slate-700" /> Emotivo/Stanco</li>
                     </ul>
                  </div>
                  <div className="p-12 md:p-16 text-center relative overflow-hidden bg-slate-900/20">
                     <div className="absolute inset-0 bg-white/5 z-0 animate-pulse"></div>
                     <div className="relative z-10">
                        <div className="inline-block p-5 border border-white/50 rounded-full mb-8 bg-white/10 shadow-[0_0_30px_rgba(255,255,255,0.2)]"><Cpu size={40} className="text-white" /></div>
                        <h4 className="text-xl font-black uppercase tracking-widest text-white mb-8">Empire System</h4>
                        <ul className="space-y-4 text-xs font-mono text-gray-300 font-bold text-left mx-auto max-w-xs">
                           <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white" /> Costo Marginale Zero</li>
                           <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white" /> Istantaneo (0.2s)</li>
                           <li className="flex items-center gap-4"><CheckCircle2 size={16} className="text-white" /> Perfezione Logica</li>
                        </ul>
                     </div>
                  </div>
               </div>
            </div>

            <div className="mt-32 text-center pb-20 relative z-10">
               <h3 className="font-serif text-3xl md:text-4xl font-bold text-white mb-10">Smetti di pagare per l'inefficienza.</h3>
               <GoldButton href="#contact" variant="silver" className="shadow-[0_0_50px_rgba(255,255,255,0.15)] border-white/30 px-10 py-5 text-sm">INSTALLA AUTOMAZIONE ORA</GoldButton>
               <p className="mt-8 text-[10px] text-gray-600 font-mono uppercase tracking-widest">Configurazione in 7 giorni lavorativi.</p>
            </div>
         </div>
      </section>
   );
};
