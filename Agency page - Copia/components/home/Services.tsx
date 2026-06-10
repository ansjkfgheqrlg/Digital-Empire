import React from 'react';
import { motion } from 'framer-motion';
import {
  BrainCircuit, PenTool, Monitor,
  Zap, Smartphone, Search, MousePointer2, ArrowRight, MousePointerClick, Eye, ShoppingBag, X, Check,
  Flame, AlertOctagon, Lightbulb, ShieldCheck, CheckCircle2
} from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';

const MotionDiv = motion.div as any;

export const Services: React.FC = () => {

  const pureSilverGradient = {
    background: 'linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    textShadow: '0 0 30px rgba(255,255,255,0.1)'
  };

  const champagneGradient = {
    background: 'linear-gradient(135deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  };

  const silverPureStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 25%, #CBD5E1 50%, #94A3B8 75%, #475569 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.2))',
  };

  // APSOC STEPS DATA
  const apsocSteps = [
    { letter: "A", title: "Attenzione (The Hook)", desc: "Ferma lo scroll. Rompi il pattern. L'obiettivo della prima frase è solo far leggere la seconda.", icon: Flame, color: "text-red-600", bullets: ["Stop Scrolling", "Rottura Pattern", "Impatto Visivo"] },
    { letter: "P", title: "Problema (The Pain)", desc: "Agita il dolore. Mostra al cliente che capisci il suo problema meglio di lui.", icon: AlertOctagon, color: "text-orange-600", bullets: ["Empatia Profonda", "Agitazione", "Validazione"] },
    { letter: "S", title: "Soluzione (The Product)", desc: "Presenta il tuo prodotto non come un 'oggetto', ma come l'unica via d'uscita logica al dolore.", icon: Lightbulb, color: "text-amber-600", bullets: ["Nuovo Veicolo", "Logica Unica", "Beneficio Primario"] },
    { letter: "O", title: "Obiezioni (The Shield)", desc: "'Costa troppo?', 'Funzionerà?'. Anticipa ogni dubbio e distruggilo prima che nasca.", icon: ShieldCheck, color: "text-blue-600", bullets: ["Garanzia Ferro", "Riprova Sociale", "Zero Rischi"] },
    { letter: "C", title: "Call to Action (The Command)", desc: "Dì loro esattamente cosa fare. Usa imperativi. La confusione uccide la conversione.", icon: MousePointerClick, color: "text-yellow-700", bullets: ["Comando Diretto", "Urgenza", "Chiarezza"] }
  ];

  // WEB DESIGN FEATURES DATA
  const webFeatures = [
    { title: "Velocità Istantanea", desc: "Sotto i 0.2s. Se è lento, il cliente esce.", icon: Zap },
    { title: "Mobile First", desc: "Il 90% compra da telefono. Progettiamo per il pollice.", icon: Smartphone },
    { title: "SEO Semantico", desc: "Codice che Google ama. Posizionamento organico.", icon: Search },
    { title: "Design Persuasivo", desc: "Layout psicologici che guidano l'occhio al 'Compra'.", icon: MousePointer2 }
  ];

  return (
    <section id="services" className="py-32 pb-24 relative border-t border-white/5 scroll-mt-20 bg-[#000000] overflow-hidden">

      {/* --- UNIFIED GRAINY BACKGROUND --- */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none bg-[#000000]">
        {/* Layer 1: Sharp Static Noise */}
        <div
          className="absolute inset-0 opacity-[0.35]"
          style={{
            backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
            filter: 'contrast(170%) brightness(150%) invert(100%)'
          }}
        />
        {/* Layer 2: Coarse Digital Grain */}
        <div
          className="absolute inset-0 opacity-[0.25] mix-blend-screen"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
            backgroundSize: '150px 150px',
            filter: 'contrast(150%)'
          }}
        />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#000000_100%)] opacity-40" />
      </div>

      <div className="container mx-auto px-6 max-w-6xl relative z-10">

        {/* =========================================================================
            HEADER & 3 PILLARS
           ========================================================================= */}
        <div className="text-center mb-16 relative">
          <motion.h2 className="font-serif text-4xl md:text-6xl lg:text-7xl font-light tracking-tight lowercase leading-[0.9]">
            <span style={pureSilverGradient as any}>un solo</span>
            <span className="mx-2 md:mx-4 text-white/10 font-thin">|</span>
            <span style={champagneGradient as any} className="font-black">ecosistema.</span>
          </motion.h2>
        </div>

        <motion.div className="relative p-[1px] rounded-[32px] overflow-hidden bg-gradient-to-br from-white via-gray-400 to-gray-900 shadow-2xl mb-12">
          <div className="bg-[#080808] rounded-[31px] p-8 md:p-16 relative overflow-hidden">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 relative z-10">
              {/* LEFT: THE PHILOSOPHY */}
              <div className="flex flex-col justify-center space-y-8">
                <div>
                  <h3 className="text-3xl font-serif text-white mb-4 leading-tight">
                    Non vendiamo <span className="text-red-500 line-through decoration-red-500/50">pezzi di ricambio</span>.
                  </h3>
                  <p className="text-gray-400 text-lg leading-relaxed font-light">
                    La maggior parte delle agenzie ti vende un sito, poi ti vende le ads, poi ti vende la gestione social. Tutto separato. Tutto disconnesso.
                  </p>
                  <p className="text-gray-400 text-lg leading-relaxed font-light mt-4">
                    Noi abbiamo creato un <span className="text-white font-medium">protocollo integrato</span>. Strategia, Parole e Tecnologia che lavorano all'unisono per un unico obiettivo:
                    <span className="text-gold-400 font-bold block mt-2 text-2xl">Vendere.</span>
                  </p>
                </div>
              </div>

              {/* RIGHT: THE 3 SILVER PILLARS */}
              <div className="flex flex-col gap-4">
                {[
                  { title: "Consulenza Strategica", sub: "Il cervello operativo", icon: BrainCircuit, color: "text-red-600" },
                  { title: "Copywriting Scientifico", sub: "La voce persuasiva", icon: PenTool, color: "text-red-600" },
                  { title: "Web Design & Engineering", sub: "Il corpo infrastrutturale", icon: Monitor, color: "text-red-600" }
                ].map((item, idx) => (
                  <div key={idx} className="p-6 rounded-2xl bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] border border-white/40 flex items-center gap-6 shadow-[0_4px_20px_rgba(255,255,255,0.2)] relative overflow-hidden group">
                    <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                    <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                    <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>
                    <div className="w-12 h-12 rounded-full bg-slate-900 flex items-center justify-center border border-gray-400 text-white shadow-inner relative z-10 shrink-0">
                      <item.icon size={20} />
                    </div>
                    <div className="relative z-10">
                      <h4 className="text-xl text-slate-900 font-serif mb-1 lowercase font-bold tracking-tight">{item.title}</h4>
                      <p className="text-xs text-slate-600 font-mono uppercase tracking-wider font-bold">{item.sub}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </motion.div>

        {/* =========================================================================
            THE VITAL ORGANS QUOTE (Requested Text)
           ========================================================================= */}
        <div className="max-w-4xl mx-auto py-16 text-center">
          <h3 className="font-serif text-2xl md:text-4xl text-gray-300 leading-tight lowercase">
            copywriting, design e strategia <span className="text-red-400 line-through decoration-2 decoration-red-500/50">non sono optional</span> da scegliere sul menu.
          </h3>
          <p className="mt-6 text-xl md:text-2xl text-white font-light leading-relaxed max-w-3xl mx-auto">
            sono <span className="font-bold text-gold-400">organi vitali dello stesso corpo</span>. <br />
            Se ne togli uno, l'organismo muore. <br />
            Noi ti diamo l'organismo completo, <span className="italic text-emerald-400">vivo e pronto a cacciare.</span>
          </p>
        </div>


        {/* =========================================================================
            HOW IT WORKS (IMPROVED GRAPHICS)
           ========================================================================= */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-20 mb-40 max-w-5xl mx-auto text-center"
        >
          <h3 className="font-serif text-3xl md:text-5xl text-white mb-20 lowercase">Come funziona <span className="italic text-gold-500">veramente?</span></h3>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative px-4">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-[2.5rem] left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/20 to-transparent z-0"></div>

            {/* STEP 1 */}
            <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] border border-white/40 shadow-xl transition-all duration-500 hover:scale-[1.02]">
              <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
              <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                <span className="font-serif text-2xl text-white">01</span>
              </div>
              <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Briefing Call <span className="text-red-600 text-xs ml-1">(Gratis)</span></h4>
              <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                Nessuna vendita. È una diagnosi. Individuiamo il problema reale che blocca la tua crescita e spieghiamo soluzioni realistiche per risolverlo.
              </p>
            </div>

            {/* STEP 2 */}
            <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] border border-white/40 shadow-xl transition-all duration-500 hover:scale-[1.02]">
              <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
              <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                <span className="font-serif text-2xl text-white">02</span>
              </div>
              <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Offerta e Preventivo</h4>
              <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                Qui è dove si decide se iniziare o meno. Impostiamo un obiettivo concreto che deve risolvere il problema e dichiariamo il minimo risultato che otterrai.
              </p>
            </div>

            {/* STEP 3 */}
            <div className="relative z-10 flex flex-col items-center group p-8 rounded-2xl bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] border border-white/40 shadow-xl transition-all duration-500 hover:scale-[1.02]">
              <div className="absolute inset-0 opacity-20 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
              <div className="w-16 h-16 rounded-full bg-slate-900 border border-white/20 flex items-center justify-center mb-6 shadow-2xl relative z-10">
                <span className="font-serif text-2xl text-white">03</span>
              </div>
              <h4 className="text-slate-900 font-bold text-lg mb-4 uppercase tracking-wider relative z-10">Strategy Call</h4>
              <p className="text-slate-700 text-sm leading-relaxed max-w-xs mx-auto font-medium relative z-10">
                Seconda call. Ti presentiamo la strategia completa per raggiungere l'obiettivo concordato.
              </p>
            </div>
          </div>
        </motion.div>


        {/* =========================================================================
            DEEP DIVE 1: COPYWRITING (APSOC)
           ========================================================================= */}
        <div className="mb-40 pt-10 border-t border-white/5">
          <div className="text-center mb-20 mt-10">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 mb-6">
              <PenTool size={16} className="text-gold-500" />
              <span className="text-xs font-mono uppercase tracking-widest text-white">Pilastro 1: La Voce</span>
            </div>
            <h3 className="font-serif text-4xl md:text-6xl text-white mb-6">copywriting <span className="text-transparent bg-clip-text bg-gradient-to-r from-gold-200 to-gold-600">scientifico</span></h3>
            <p className="text-gray-400 max-w-2xl mx-auto leading-relaxed text-lg">
              Dimentica la creatività. Qui si parla di ingegneria. Usiamo il protocollo A.P.S.O.C. per guidare l'utente dall'attenzione all'acquisto senza attrito.
            </p>
          </div>

          {/* APSOC CARDS */}
          <div className="grid gap-6">
            {apsocSteps.map((step, idx) => (
              <div key={idx} className="group relative p-6 md:p-8 rounded-2xl transition-all duration-500 overflow-hidden shadow-2xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.01] hover:shadow-[0_0_40px_rgba(255,255,255,0.3)] flex flex-col items-start gap-8">
                <div className="absolute inset-0 opacity-40 mix-blend-overlay pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
                <div className="absolute top-0 left-0 w-full h-[1px] bg-white/80 z-20"></div>
                <div className="absolute bottom-0 left-0 w-full h-[1px] bg-slate-400/50 z-20"></div>

                <div className="flex flex-col md:flex-row gap-8 items-start md:items-center relative z-10 w-full">
                  {/* Letter Big */}
                  <div className="shrink-0">
                    <span className="font-serif font-black text-6xl md:text-8xl text-slate-900/10 group-hover:text-red-600/20 transition-colors duration-500 cursor-default select-none">
                      {step.letter}
                    </span>
                  </div>

                  {/* Content */}
                  <div className="grow">
                    <div className="flex items-center gap-3 mb-2">
                      <step.icon size={20} className="text-red-600" />
                      <h4 className="text-xl font-bold text-slate-900 lowercase">{step.title}</h4>
                    </div>
                    <p className="text-slate-700 font-medium text-sm leading-relaxed max-w-3xl">
                      {step.desc}
                    </p>
                  </div>

                  {/* Bullets (Desktop) */}
                  <div className="hidden md:block shrink-0 border-l border-slate-900/10 pl-6 w-48">
                    <ul className="space-y-2">
                      {step.bullets.map((b, i) => (
                        <li key={i} className="text-[10px] font-mono text-slate-500 uppercase tracking-widest flex items-center gap-2 font-bold">
                          <div className="w-1.5 h-1.5 rounded-full bg-red-600"></div>
                          {b}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>


        {/* =========================================================================
            DEEP DIVE 2: WEB DESIGN (SHOWCASE)
           ========================================================================= */}
        <div className="mb-40 pt-10 border-t border-white/5">
          <div className="text-center mb-20 mt-10">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 mb-6">
              <Monitor size={16} className="text-blue-400" />
              <span className="text-xs font-mono uppercase tracking-widest text-white">Pilastro 2: L'Infrastruttura</span>
            </div>

            {/* --- "NON VENDIAMO SITI WEB..." HEADER --- */}
            <h2 className="font-playfair text-4xl md:text-7xl text-white tracking-tight leading-[0.9] mb-8">
              <span className="font-thin italic tracking-normal text-gray-400">non vendiamo</span> <span className="font-black text-white">siti web.</span><br />
              <span className="font-thin italic tracking-normal text-gray-400">vendiamo</span> <span style={silverPureStyle as any} className="font-black">risultati.</span>
            </h2>
            <p className="max-w-2xl mx-auto text-gray-400 text-lg font-light leading-relaxed">
              Il sito bello non serve a niente se non fattura. Noi costruiamo macchine da guerra digitali ottimizzate per la conversione.
            </p>
          </div>

          {/* BROWSER / CTR SECTION */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center mb-20 bg-[#0a0a0a]/30 p-8 rounded-3xl border border-white/5">
            {/* Browser Mockup */}
            <div className="relative aspect-[4/3] bg-[#050505] rounded-xl border border-white/10 shadow-2xl overflow-hidden group">
              {/* Browser UI */}
              <div className="h-8 border-b border-white/5 bg-[#0a0a0a] flex items-center px-4 gap-2">
                <div className="w-2.5 h-2.5 rounded-full bg-red-500/20"></div>
                <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/20"></div>
                <div className="w-2.5 h-2.5 rounded-full bg-green-500/20"></div>
              </div>
              <div className="p-8 flex flex-col items-center justify-center h-full relative">
                <div className="w-3/4 h-6 bg-white/5 rounded mb-4 animate-pulse"></div>
                <div className="w-1/2 h-3 bg-white/5 rounded mb-8"></div>
                <div className="px-6 py-2 bg-gold-500 text-black font-bold uppercase tracking-widest text-[10px] rounded shadow-[0_0_20px_rgba(212,175,55,0.2)]">
                  Acquista Ora
                </div>
              </div>
            </div>

            {/* CTR Explanation */}
            <div className="flex flex-col justify-center">
              <h3 className="text-2xl font-serif text-white font-bold mb-6 flex items-center gap-3">
                <Eye className="text-gold-500" size={24} /> Cos'è il CTR?
              </h3>
              <div className="space-y-6 text-gray-400 leading-relaxed">
                <p>
                  Il <strong>Click-Through Rate</strong> è la differenza tra un sito vetrina e un sito che vende. È la percentuale di persone che cliccano dove vuoi tu.
                </p>
                <ul className="space-y-4 border-l border-white/10 pl-6">
                  <li className="flex items-start gap-3">
                    <X size={18} className="text-red-500 shrink-0 mt-1" />
                    <span>Se su 100 visitatori compra 1 persona (1%), stai sprecando budget.</span>
                  </li>
                  <li className="flex items-start gap-3">
                    <CheckCircle2 size={18} className="text-emerald-500 shrink-0 mt-1" />
                    <span>Se ne comprano 5 (5%), il tuo fatturato fa <strong>x5</strong> senza spendere un euro in più in ads.</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          {/* 4 FEATURES GRID */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {webFeatures.map((f, idx) => (
              <div key={idx} className="p-6 rounded-xl transition-all duration-500 overflow-hidden shadow-xl border border-white/40 bg-gradient-to-br from-[#ffffff] via-[#fef2f2] to-[#cbd5e1] hover:scale-[1.05]">
                <f.icon className="text-red-900 mb-4" size={24} />
                <h4 className="text-slate-900 font-bold mb-2">{f.title}</h4>
                <p className="text-xs text-slate-600 leading-relaxed font-mono font-bold uppercase tracking-tighter">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>


        {/* =========================================================================
            DEEP DIVE 3: STRATEGIA (BRIEF)
           ========================================================================= */}
        <div className="pt-10 border-t border-white/5 pb-0">
          <div className="text-center max-w-3xl mx-auto mt-10">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 mb-6">
              <BrainCircuit size={16} className="text-purple-400" />
              <span className="text-xs font-mono uppercase tracking-widest text-white">Pilastro 3: La Mente</span>
            </div>
            <h3 className="font-serif text-3xl md:text-5xl text-white mb-8 lowercase">Consulenza Strategica</h3>
            <p className="text-gray-400 leading-relaxed text-lg mb-8">
              Tutto parte da qui. Prima di scrivere una riga di codice o una parola di copy, dobbiamo capire chi sei e chi vuoi distruggere (sul mercato).
            </p>
            <div className="p-8 rounded-2xl bg-gradient-to-br from-purple-900/10 to-blue-900/10 border border-white/10 relative overflow-hidden">
              <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8">
                <div className="text-left">
                  <h4 className="text-white font-bold mb-2">Diagnosi Profonda</h4>
                  <p className="text-gray-500 text-sm">Analisi dei colli di bottiglia attuali.</p>
                </div>
                <ArrowRight className="text-white/20 hidden md:block" />
                <div className="text-left">
                  <h4 className="text-white font-bold mb-2">Piano d'Attacco</h4>
                  <p className="text-gray-500 text-sm">La roadmap passo-passo per scalare.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* =========================================================================
            CLASSIFIED CITATION (Moved from Philosophy)
           ========================================================================= */}
        <div className="max-w-3xl mx-auto mt-12 px-6">
          <MotionDiv
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="relative p-[1px] rounded-xl overflow-hidden bg-gradient-to-r from-gray-400 via-[#FDB913] to-gray-400 shadow-[0_0_20px_rgba(253,185,19,0.15)]"
          >
            <div className="bg-[#0a0a0a] rounded-xl p-8 md:p-10 relative overflow-hidden flex flex-col items-center text-center">

              {/* Background Noise for texture consistency */}
              <div
                className="absolute inset-0 opacity-[0.3]"
                style={{
                  backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                  filter: 'contrast(150%) brightness(130%)'
                }}
              />

              <div className="relative z-10">
                <p className="font-mono text-xs text-gold-500 mb-4 tracking-[0.2em] uppercase font-bold">
                      // status: classified
                </p>
                <p className="text-gray-300 text-lg md:text-xl font-light leading-relaxed lowercase font-serif italic">
                  "abbiamo eliminato la variabile <span className="text-white font-bold not-italic">fortuna</span> dall'equazione. <br className="hidden md:block" />
                  costruiamo sistemi <span className="text-white font-bold not-italic">deterministici</span> che producono risultati prevedibili."
                </p>
              </div>
            </div>
          </MotionDiv>
        </div>

      </div>
    </section>
  );
};
