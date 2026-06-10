
import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrowRight, Zap, Hash, User, Clock, Layers, ShieldAlert, BookOpen, Fingerprint, Eye, Minus, ArrowLeft, Share2, TrendingUp, Check, X, Activity, Cpu, Lock, MousePointer2, Quote, Book, Target, Bot, Monitor } from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';

const MotionDiv = motion.div as any;

// --- ULTRA HIGH-RES COSMIC ATMOSPHERE WITH HEAVY GRAIN ---
const CosmicAtmosphere = () => (
  <div className="fixed inset-0 w-full h-full overflow-hidden pointer-events-none z-0 bg-[#020003]">
    
    {/* 1. DEEP SPACE BASE (Gradient Mesh) */}
    <div 
        className="absolute inset-0 z-0 opacity-60"
        style={{
            background: `
                radial-gradient(circle at 50% 50%, #1a103c 0%, transparent 100%),
                radial-gradient(circle at 0% 100%, #0c0a20 0%, transparent 50%),
                radial-gradient(circle at 100% 0%, #1e1b4b 0%, transparent 50%)
            `
        }}
    />

    {/* 2. HIGH-FIDELITY STARS */}
    <div className="absolute inset-0 z-1 opacity-70"
         style={{
             backgroundImage: 'radial-gradient(1px 1px at 20px 30px, #ffffff, rgba(0,0,0,0)), radial-gradient(1px 1px at 40px 70px, #ffffff, rgba(0,0,0,0)), radial-gradient(1.5px 1.5px at 90px 40px, #fff, rgba(0,0,0,0)), radial-gradient(1px 1px at 160px 120px, #ddd, rgba(0,0,0,0))',
             backgroundSize: '350px 350px',
             backgroundRepeat: 'repeat'
         }}
    />
    
    {/* 3. VOLUMETRIC NEBULAS */}
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 0.5, scale: [1, 1.1, 1], rotate: [0, 5, 0] }}
      transition={{ duration: 20, repeat: Infinity, ease: "easeInOut" }}
      className="absolute top-[-10%] right-[-10%] w-[90vw] h-[90vh] rounded-full blur-[140px] mix-blend-screen"
      style={{
        background: 'radial-gradient(circle at center, rgba(109, 40, 217, 0.25) 0%, rgba(76, 29, 149, 0.1) 40%, transparent 80%)',
      }}
    />

    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 0.4, scale: [1, 1.2, 1], rotate: [0, -5, 0] }}
      transition={{ duration: 25, repeat: Infinity, ease: "easeInOut", delay: 2 }}
      className="absolute bottom-[-10%] left-[-20%] w-[100vw] h-[80vh] rounded-full blur-[150px] mix-blend-screen"
      style={{
        background: 'radial-gradient(circle at center, rgba(30, 58, 138, 0.3) 0%, rgba(23, 37, 84, 0.15) 50%, transparent 80%)',
      }}
    />

    {/* 4. HEAVY FILM GRAIN (Consistent with Home) */}
    <div 
      className="absolute inset-0 opacity-[0.35]" 
      style={{ 
          backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
          filter: 'contrast(170%) brightness(150%) invert(100%)',
          mixBlendMode: 'overlay' 
      }} 
    />
    
    {/* 5. DIGITAL CRISP NOISE */}
    <div 
      className="absolute inset-0 opacity-[0.25] mix-blend-screen"
      style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
          backgroundSize: '150px 150px',
          filter: 'contrast(150%)'
      }}
    />
    
    {/* 6. VIGNETTE */}
    <div className="absolute inset-0 bg-[radial-gradient(transparent_40%,#020003_100%)] z-10 pointer-events-none opacity-80" />
  </div>
);

// --- 1. TYPOGRAPHY SYSTEM ---
const silverGradientStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 60%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    textShadow: '0px 2px 4px rgba(0,0,0,0.3)'
};

const goldGradientStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFF7ED 0%, #FDE68A 30%, #D4AF37 70%, #B45309 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 0px rgba(0,0,0,0.5))'
};

interface SilverBodyProps {
  children?: React.ReactNode;
  className?: string;
}

const SilverBody: React.FC<SilverBodyProps> = ({ children, className = "" }) => (
  <div className={`font-sans font-light tracking-wide leading-relaxed text-lg md:text-xl lowercase ${className}`}>
    <span style={silverGradientStyle as any}>
      {children}
    </span>
  </div>
);

const ChapterTitle = ({ children, number }: { children?: React.ReactNode, number: string }) => (
    <div className="mt-20 mb-10 border-t border-white/10 pt-10 relative z-10">
        <span className="font-mono text-xs uppercase tracking-[0.4em] block mb-3 lowercase" style={goldGradientStyle as any}>capitolo {number}</span>
        <h3 className="text-3xl md:text-5xl font-serif font-black tracking-tight leading-none lowercase">
            <span style={silverGradientStyle as any}>{children}</span>
        </h3>
    </div>
);

// --- 2. MICRO-COMPONENTS ---

const DataBlock = ({ label, value, delta, color = "gold" }: { label: string, value: string, delta: string, color?: "gold" | "red" | "blue" | "green" | "purple" }) => {
    const borderClasses = {
        gold: "border-gold-500/30 bg-gold-950/20",
        red: "border-red-500/30 bg-red-950/20",
        blue: "border-cyan-500/30 bg-cyan-950/20",
        green: "border-emerald-500/30 bg-emerald-950/20",
        purple: "border-purple-500/30 bg-purple-950/20"
    };
    
    return (
        <div className={`my-12 p-8 rounded-xl border ${borderClasses[color]} backdrop-blur-md relative overflow-hidden group z-10 shadow-xl`}>
             <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity text-white">
                <Activity size={64} />
             </div>
             <div className="text-xs font-mono uppercase tracking-widest text-slate-400 mb-3 lowercase">{label}</div>
             <div className="flex items-end gap-6">
                 <div className="text-4xl md:text-6xl font-black lowercase" style={silverGradientStyle as any}>{value}</div>
                 <div className={`text-lg font-bold flex items-center gap-1 mb-2 lowercase`} style={goldGradientStyle as any}>
                    <TrendingUp size={20} className="text-gold-500" /> {delta}
                 </div>
             </div>
        </div>
    );
};

interface InsightBoxProps {
  title: string;
  children?: React.ReactNode;
}

const InsightBox: React.FC<InsightBoxProps> = ({ title, children }) => (
    <div className="my-12 p-8 md:p-10 border-l-2 border-gold-500 bg-black/40 backdrop-blur-md rounded-r-xl relative z-10 shadow-lg">
        <h4 className="flex items-center gap-3 font-mono text-sm uppercase tracking-[0.2em] font-bold mb-6 lowercase" style={goldGradientStyle as any}>
            <Zap size={16} className="text-gold-500" /> {title}
        </h4>
        <div className="font-serif text-xl italic leading-relaxed lowercase" style={silverGradientStyle as any}>
            {children}
        </div>
    </div>
);

const StoryBox = ({ title, children }: { title: string, children?: React.ReactNode }) => (
    <div className="my-20 relative z-10">
        <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-slate-500 to-transparent opacity-30"></div>
        <div className="absolute bottom-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-slate-500 to-transparent opacity-30"></div>
        <div className="py-12 px-6 md:px-16 bg-[#080808]/60 backdrop-blur-md border-y border-white/5">
            <div className="flex items-center justify-center gap-4 mb-8 opacity-60">
                <Book size={20} className="text-slate-400" />
                <span className="text-xs font-mono uppercase tracking-[0.3em] text-slate-400 lowercase">storytelling archive</span>
            </div>
            <h4 className="text-3xl text-center font-serif mb-10 tracking-tight lowercase" style={silverGradientStyle as any}>{title}</h4>
            <div className="silver-prose italic lowercase">
                {children}
            </div>
        </div>
    </div>
);

const StrategyCard = ({ title, steps }: { title: string, steps: string[] }) => (
    <div className="my-12 bg-black/40 backdrop-blur-md border border-slate-700/50 p-8 rounded-xl shadow-2xl relative z-10">
        <h4 className="flex items-center gap-3 text-xl font-bold mb-8 lowercase">
            <Target className="text-red-500" /> 
            <span style={silverGradientStyle as any}>{title}</span>
        </h4>
        <div className="space-y-6">
            {steps.map((step, i) => (
                <div key={i} className="flex gap-5">
                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-slate-900 border border-slate-600 flex items-center justify-center text-sm font-bold text-slate-300 shadow-inner">
                        {i + 1}
                    </div>
                    <p style={silverGradientStyle as any} className="text-lg lowercase">{step}</p>
                </div>
            ))}
        </div>
    </div>
);

const EmpireQuote = ({ text, author }: { text: string, author?: string }) => (
    <div className="relative my-20 py-16 px-8 md:px-24 text-center bg-black/30 backdrop-blur-sm rounded-2xl border border-white/5 shadow-2xl z-10">
        <Quote className="absolute top-8 left-8 text-gold-500/20 w-16 h-16 transform -scale-x-100" />
        <h3 className="text-3xl md:text-5xl font-serif font-medium leading-tight mb-8 relative z-10 lowercase">
            <span style={silverGradientStyle as any}>"{text}"</span>
        </h3>
        {author && <div className="text-xs font-mono uppercase tracking-[0.3em] opacity-70 lowercase" style={goldGradientStyle as any}>— {author}</div>}
    </div>
);

const ActionList = ({ items }: { items: string[] }) => (
    <div className="my-16 bg-[#030303]/60 backdrop-blur-md border border-gold-500/30 rounded-xl p-8 md:p-12 shadow-[0_0_60px_rgba(0,0,0,0.5)] relative z-10">
        <h4 className="font-serif text-2xl text-white mb-8 border-b border-white/5 pb-4 flex justify-between items-center lowercase">
            <span style={silverGradientStyle as any}>protocollo di implementazione</span>
            <span className="text-[10px] font-mono uppercase tracking-widest bg-gold-950/30 px-3 py-1 rounded text-gold-500 border border-gold-500/20 lowercase">actionable</span>
        </h4>
        <ul className="space-y-6">
            {items.map((item, i) => (
                <li key={i} className="flex items-start gap-4 group">
                    <div className="mt-1 w-6 h-6 rounded-full border border-gold-500 flex items-center justify-center group-hover:bg-gold-500 transition-colors flex-shrink-0 shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                        <Check size={12} className="text-gold-500 group-hover:text-black-900 transition-colors" />
                    </div>
                    <span className="text-lg leading-relaxed group-hover:translate-x-1 transition-transform duration-300 lowercase" style={silverGradientStyle as any}>{item}</span>
                </li>
            ))}
        </ul>
    </div>
);

// --- 3. STRUCTURAL COMPONENTS ---

interface MetallicFrameProps {
  children?: React.ReactNode;
  className?: string;
  intensity?: 'silver' | 'gold' | 'red' | 'blue' | 'purple' | 'emerald';
}

const MetallicFrame: React.FC<MetallicFrameProps> = ({ children, className = "", intensity = "silver" }) => {
  const gradients = {
    silver: "from-slate-300 via-slate-500 to-slate-800",
    gold: "from-yellow-200 via-yellow-600 to-slate-800",
    red: "from-red-300 via-red-600 to-slate-900",
    blue: "from-cyan-300 via-cyan-600 to-slate-900",
    purple: "from-purple-300 via-purple-600 to-slate-900",
    emerald: "from-emerald-300 via-emerald-600 to-slate-900"
  };

  return (
    <div className={`relative p-[1px] rounded-sm group overflow-hidden ${className}`}>
      <div className={`absolute inset-0 bg-gradient-to-br ${gradients[intensity] || gradients.silver} opacity-100 z-0`}></div>
      <div className="relative z-10 bg-[#050505] h-full w-full rounded-sm overflow-hidden">
        <div className="absolute inset-0 opacity-20 pointer-events-none mix-blend-overlay bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>
        <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-white/5 to-transparent pointer-events-none"></div>
        {children}
      </div>
    </div>
  );
};

// --- DATA ---
const blogPosts = [
  {
    id: 1,
    title: "la macchina da soldi: copywriting scientifico",
    excerpt: "perché le aziende bruciano budget in marketing inutile e come l'arte della persuasione scritta è l'unica competenza che ti separa dal fallimento.",
    readTime: "25 min",
    category: "strategia",
    image: "https://images.unsplash.com/photo-1610375460993-d2d7b50075b4?auto=format&fit=crop&q=80&w=1600", 
    highlight: "PlatinumGold",
    themeColor: "gold",
    content: (
        <>
            <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-gold-500 pl-6 lowercase">
                "se i copywriter non esistessero, le aziende farebbero prima a bruciare i soldi al posto di investirli in marketing."
            </p>

            <p>immagina di essere il titolare di <strong>wiko</strong>, un'azienda che crea e vende smartphone. sul mercato la concorrenza è feroce: apple, samsung, xiaomi, huawei. hai bisogno di una strategia che ti aiuti a diventare rilevante e acquisire nuovi clienti.</p>
            <p>certamente, puoi creare prodotti più economici, migliori, più belli... ma c’è un limite. non puoi ridurre il prezzo oltre un certo limite altrimenti andrai in perdita. non puoi creare telefoni tecnologicamente superiori a samsung se hai un decimo del loro budget r&d.</p>
            <p>quindi... cosa fai? <strong>il prodotto non si vende da solo.</strong> contrariamente a ciò che dicono i "guru" della silicon valley, un ottimo prodotto senza un ottimo marketing è solo un magazzino pieno di merce invenduta.</p>

            <ChapterTitle number="01">il ruolo del copywriter</ChapterTitle>
            <p>assumi una grande agenzia di marketing per delle pubblicità su facebook, instagram, pinterest. ma la domanda è... <strong>chi scriverà i testi che verranno inseriti dentro questi contenuti?</strong></p>
            <p>non può farlo il tuo designer: lui si occupa di estetica, non di psicologia della vendita. non puoi farlo tu: sei troppo coinvolto emotivamente nel prodotto.</p>
            <p>ti serve un <strong>copywriter</strong>. una persona che nella vita fa solo una cosa: usa le parole per spostare soldi dalle tasche dei clienti alle tue.</p>

            <DataBlock label="roi incremento medio (copy pro)" value="+340%" delta="vs testi generici" color="gold" />

            <ChapterTitle number="02">la sacra formula: a.p.s.o.c.</ChapterTitle>
            <p>non scriviamo a caso. usiamo protocolli. il 99% del marketing di successo della storia segue questa formula, direttamente o indirettamente. memorizzala, tatuala, fanne il tuo mantra.</p>
            
            <StrategyCard 
                title="protocollo apsoc" 
                steps={[
                    "attenzione: se non ti guardano, non puoi vendere. devi fermare lo scroll.",
                    "problema: definisci il dolore del cliente meglio di come saprebbe farlo lui.",
                    "soluzione: presenta il tuo prodotto non come un oggetto, ma come l'unica via d'uscita logica al problema.",
                    "obiezioni: anticipa i dubbi (costo, fiducia, tempo) e distruggili prima che nascano.",
                    "call to action (cta): dì loro esattamente cosa fare. le persone hanno bisogno di ordini."
                ]} 
            />

            <ChapterTitle number="03">la differenza tra problema e pain point</ChapterTitle>
            <p>molti marketer falliscono qui. confondono l'evento con il dolore. se vendi un servizio finanziario, il problema è "non ho soldi". ma il <strong>pain point</strong> è "la vergogna che provo quando la mia carta viene rifiutata al ristorante davanti alla mia fidanzata".</p>
            <p>vedi la differenza? il problema è logico. il pain point è viscerale. noi vendiamo risolvendo il dolore, non il problema matematico.</p>

            <StoryBox title="l'esempio del ginocchio">
                <p>immagina di essere caduto dalle scale. <br/><br/>
                <strong>l'evento:</strong> caduta.<br/>
                <strong>il problema:</strong> ginocchio rotto, non riesci a camminare.<br/>
                <strong>il pain point:</strong> il dolore fisico atroce, certo. ma soprattutto il fatto che <em>non potrai giocare la finale del torneo di calcetto</em> per cui ti sei allenato un anno. la frustrazione di guardare i tuoi amici giocare dalla panchina.<br/><br/>
                un cattivo copywriter ti vende "gesso per ginocchia rotte".<br/>
                un copywriter d'élite ti vende "torna in campo prima della finale".</p>
            </StoryBox>

            <ChapterTitle number="04">headline: il tuo unico obiettivo</ChapterTitle>
            <p>un famoso dato statistico dice che l'80% delle persone si fermano ai titoli. solo il 20% legge il resto. se il tuo titolo fa schifo, hai buttato l'80% del tuo budget media.</p>
            <p>usa la curiosità. usa la controversia. usa la paura.</p>
            <p><em>esempio banale:</em> "nuovo metodo per dimagrire". (noioso, ignorato).<br/>
            <em>esempio copywriter:</em> "mangia di più e perdi peso: la dieta che i nutrizionisti odiano". (stop allo scroll).</p>

            <ActionList items={[
                "riscrivi la headline della tua landing page usando la formula 'come [risultato] senza [sacrificio]'.",
                "identifica 3 pain point emotivi profondi del tuo target, non solo problemi superficiali.",
                "controlla se il tuo copy attuale segue la struttura apsoc. se manca uno step, riscrivilo."
            ]} />
        </>
    )
  },
  {
    id: 2,
    title: "psicologia della vendita: manipolare eticamente",
    excerpt: "le persone comprano con le emozioni e giustificano con la logica. impara a bypassare la corteccia prefrontale per parlare direttamente al cervello rettiliano.",
    readTime: "22 min",
    category: "psicologia",
    image: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&q=80&w=1600",
    highlight: "AnodizedRed",
    themeColor: "red",
    content: (
        <>
            <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-red-500 pl-6 lowercase">
                "non stiamo vendendo prodotti. stiamo vendendo <strong className="text-red-500">dopamina</strong> confezionata."
            </p>

            <p>il tuo cliente non è un essere razionale. è una scimmia evoluta che indossa un completo. se cerchi di vendere usando solo dati, specifiche tecniche e logica, stai parlando alla parte sbagliata del suo cervello. stai parlando alla corteccia prefrontale, che è scettica, lenta e analitica.</p>
            <p>per vendere davvero, devi parlare al <strong>cervello rettiliano</strong>. quella parte antica che gestisce la sopravvivenza, la paura, il sesso e lo status. quella parte decide in millisecondi.</p>

            <ChapterTitle number="01">il mito della razionalità</ChapterTitle>
            <p>neuroscienze applicate: il 95% delle decisioni d'acquisto avviene nel subconscio. la logica interviene solo <strong>dopo</strong> per giustificare la scelta emotiva che è già stata fatta.</p>
            <p>nessuno compra una ferrari perché "ha un motore efficiente". la comprano per lo status, per sentirsi potenti, per attrarre partner. poi, quando glielo chiedi, ti parleranno dei cavalli e dell'aerodinamica per non sembrare superficiali.</p>

            <InsightBox title="principio fondamentale">
                <p>vendi l'emozione (il 'perché'), giustifica con la logica (il 'cosa'). invertire questo ordine è fatale.</p>
            </InsightBox>

            <ChapterTitle number="02">scarsità e urgenza: la paura di perdere</ChapterTitle>
            <p>l'essere umano ha più paura di perdere 100€ che desiderio di guadagnarne 100. si chiama <strong>loss aversion</strong>. se il tuo prodotto è sempre disponibile per tutti, non ha valore percepito.</p>
            <p>devi creare scarsità reale. non finta. "solo 3 posti rimasti" funziona solo se è vero. se domani sono ancora lì, hai perso la tua credibilità.</p>

            <DataBlock label="tasso conversione con scarsità" value="+220%" delta="vs offerta aperta" color="red" />

            <ChapterTitle number="03">social proof: il gregge ha sempre ragione</ChapterTitle>
            <p>se entri in una città sconosciuta e vedi due ristoranti: uno vuoto e uno con la fila fuori, dove vai? vai dove c'è la fila. anche se il cibo fa schifo. il nostro cervello è programmato per seguire la massa per sopravvivere.</p>
            <p>sul tuo sito, le testimonianze non sono un "extra". sono la <strong>prova</strong> che non sei un predatore. usa video. usa screenshot reali. niente frasi finte tipo "ottimo servizio - mario rossi".</p>

            <ActionList items={[
                "inserisci un elemento di scarsità (tempo o quantità) nella tua offerta principale.",
                "sostituisci le descrizioni tecniche con descrizioni dei benefici emotivi.",
                "raccogli 5 video-testimonianze di clienti che parlano del risultato emotivo, non del servizio."
            ]} />
        </>
    )
  },
  {
    id: 3,
    title: "direct response: la matematica del profitto",
    excerpt: "basta branding vago. il direct response marketing è l'unica disciplina che ti permette di tracciare ogni centesimo. impara a vendere in modo binario: sì o no.",
    readTime: "18 min",
    category: "tecnica",
    image: "https://images.unsplash.com/photo-1611974765270-ca12586343bb?auto=format&fit=crop&q=80&w=1600",
    highlight: "DeepEmerald",
    themeColor: "blue",
    content: (
        <>
             <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-cyan-500 pl-6 lowercase">
                "la creatività senza conversione è solo <strong className="text-cyan-500">arte costosa</strong>. noi non siamo artisti, siamo banchieri."
            </p>

            <p>coca-cola può permettersi di fare "branding". può spendere milioni per mostrare orsi polari che bevono bibite solo per "essere top of mind". tu no. se non sei una multinazionale con budget infinito, ogni euro che spendi in pubblicità deve portarti indietro almeno due euro. subito. non tra un anno.</p>
            <p>questo è il <strong>direct response marketing</strong>. marketing progettato per evocare una risposta immediata e tracciabile.</p>

            <ChapterTitle number="01">la regola dell'uno</ChapterTitle>
            <p>la complessità uccide la conversione. se la tua pubblicità cerca di vendere 3 cose diverse, non ne venderà nessuna. la regola aurea del direct response è:</p>
            <p><strong>un annuncio, un obiettivo, una call to action.</strong></p>
            <p>non chiedere di "mettere like, condividere e comprare". chiedi di comprare. punto.</p>

            <StrategyCard 
                title="il ciclo del profitto" 
                steps={[
                    "acquisizione: comprare un cliente a breakeven (o leggera perdita) sulla prima transazione.",
                    "monetizzazione: vendere un upsell immediato per andare in profitto.",
                    "ritenzione: vendere ripetutamente alla lista clienti a costo zero.",
                    "riattivazione: recuperare i clienti persi con offerte irresistibili."
                ]} 
            />

            <ChapterTitle number="02">se non puoi misurarlo, non esiste</ChapterTitle>
            <p>nel branding, il successo è vago ("ci conoscono di più"). nel direct response, il successo è binario. cpa (costo per acquisizione) vs ltv (lifetime value).</p>
            <p>se ti costa 50€ acquisire un cliente e lui te ne porta 100€ nel tempo, hai una macchina da soldi infinita. puoi spendere quanto vuoi. se te ne porta 40€, stai fallendo. non servono opinioni, serve un foglio excel.</p>

            <DataBlock label="precisione tracciamento" value="99.9%" delta="pixel based" color="blue" />

            <StoryBox title="la lezione di claude hopkins">
                <p>claude hopkins, padre del marketing scientifico, usava i coupon nei giornali nel 1920 per tracciare quale titolo funzionasse meglio. se il titolo a portava 500 coupon e il titolo b ne portava 200, il titolo b veniva eliminato. <br/><br/>
                oggi facciamo lo stesso con facebook ads e google analytics. la tecnologia cambia, la matematica resta.</p>
            </StoryBox>

            <ActionList items={[
                "installa pixel di tracciamento su ogni pagina del tuo funnel.",
                "calcola il tuo cpa (costo per acquisizione) attuale. se non lo sai, ferma le ads.",
                "crea un'offerta di front-end a basso costo per acquisire clienti, poi vendi il servizio costoso."
            ]} />
        </>
    )
  },
  {
    id: 4,
    title: "storytelling: il cavallo di troia",
    excerpt: "i dati attivano la logica, le storie attivano i sogni. come strutturare narrazioni che bypassano le difese critiche e installano il desiderio d'acquisto.",
    readTime: "20 min",
    category: "copywriting",
    image: "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&q=80&w=1600",
    highlight: "PlatinumGold",
    themeColor: "gold",
    content: (
        <>
            <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-gold-500 pl-6 lowercase">
                "i fatti raccontano, le storie vendono. nessuno ha mai marciato in guerra per un grafico a torta."
            </p>

            <p>quando presenti dei dati a un cliente, il suo cervello entra in modalità analitica. alza le difese. cerca l'errore. vuole smentirti.</p>
            <p>quando racconti una storia, il cervello entra in modalità passiva. abbassa le difese. vuole sapere come va a finire. la storia è un <strong>cavallo di troia</strong>: usi la narrazione per trasportare il tuo messaggio di vendita oltre le mura della diffidenza.</p>

            <ChapterTitle number="01">il viaggio dell'eroe (cliente)</ChapterTitle>
            <p>l'errore numero uno delle aziende: si pongono come l'eroe della storia. "siamo leader dal 1990", "abbiamo vinto premi", "siamo fantastici".</p>
            <p>al cliente non frega niente di te. lui vuole essere l'eroe. tu non sei luke skywalker. tu sei yoda. tu sei la guida. il tuo prodotto è la spada laser.</p>

            <InsightBox title="ruoli narrativi">
                <p><strong>eroe:</strong> il tuo cliente (confuso, con un problema). <br/>
                <strong>villain:</strong> il problema (esterno, interno, filosofico). <br/>
                <strong>guida:</strong> il tuo brand (empatico, autoritario). <br/>
                <strong>piano:</strong> il tuo prodotto.</p>
            </InsightBox>

            <ChapterTitle number="02">conflitto = interesse</ChapterTitle>
            <p>una storia senza conflitto è noiosa. "mario si è alzato, ha comprato il nostro software e vissero felici" non funziona.</p>
            <p>devi drammatizzare il problema. devi mostrare cosa succede se <strong>non</strong> comprano. il fallimento deve essere un'opzione reale e spaventosa. solo così il successo finale ha valore.</p>

            <EmpireQuote text="se non c'è rischio di morte (fisica o sociale), non è una storia. è un verbale." author="Robert McKee" />

            <ChapterTitle number="03">la trasformazione</ChapterTitle>
            <p>non vendi il prodotto, vendi la trasformazione dell'identità del cliente. da "imprenditore stressato che non dorme" a "ceo in controllo che fa scalare l'azienda". il prodotto è solo il ponte tra lo stato a e lo stato b.</p>

            <ActionList items={[
                "riscrivi la tua 'chi siamo' page mettendo il cliente al centro, non l'azienda.",
                "identifica il 'villain' nella vita del tuo cliente. cosa gli impedisce di dormire?",
                "mostra il 'paradiso' (dopo l'acquisto) e l' 'inferno' (senza acquisto) nei tuoi materiali."
            ]} />
        </>
    )
  },
  {
    id: 5,
    title: "l'era dell'inutilità umana: ai & automazione",
    excerpt: "perché assumere staff quando il software lavora gratis, non dorme e non sbaglia mai? benvenuti nella rivoluzione industriale digitale.",
    readTime: "15 min",
    category: "automazione",
    image: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&q=80&w=1600",
    highlight: "NeonPurple",
    themeColor: "purple",
    content: (
        <>
            <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-purple-500 pl-6 lowercase">
                "l'essere umano è lento, emotivo, costoso e incline all'errore. l'ai è istantanea, stoica, economica e perfetta. <strong className="text-purple-500">fai la tua scelta.</strong>"
            </p>

            <p>non è cattiveria, è darwinismo aziendale. se il tuo concorrente usa l'ai per qualificare i lead in 3 secondi a costo zero, e tu paghi una segretaria per richiamarli il giorno dopo... sei estinto. non lo sai ancora, ma sei già morto.</p>
            <p>stiamo vivendo la più grande ridistribuzione di ricchezza della storia. chi automatizza vince tutto. chi resiste perde tutto.</p>

            <ChapterTitle number="01">velocità di esecuzione</ChapterTitle>
            <p>un lead che compila un form online si aspetta una risposta immediata. dopo 5 minuti, la probabilità di contatto scende del 90%. un umano non può competere. un'automazione ti manda un whatsapp, una mail e un sms nell'istante in cui premono "invio".</p>

            <DataBlock label="tempo risposta medio umano" value="48 min" delta="vs 2 sec AI" color="purple" />

            <ChapterTitle number="02">eliminare l'errore umano</ChapterTitle>
            <p>quante volte un venditore si è dimenticato di richiamare? quante volte un dato è stato trascritto male nel crm? l'automazione non dimentica. non ha "giornate no". non ha mal di testa. esegue il protocollo con precisione militare, ogni singola volta.</p>

            <StrategyCard 
                title="stack automazione base" 
                steps={[
                    "lead capture: i dati dal sito finiscono automaticamente nel crm.",
                    "nurturing: sequenze email automatiche educano il cliente per mesi.",
                    "booking: l'ai propone slot liberi e fissa appuntamenti sul calendario.",
                    "onboarding: appena pagano, ricevono contratti e accessi senza che tu muova un dito."
                ]} 
            />

            <ChapterTitle number="03">scalabilità infinita</ChapterTitle>
            <p>se vuoi gestire 10 volte più clienti con il metodo tradizionale, devi assumere 10 volte più staff. costi enormi, problemi di gestione. con l'automazione, gestire 10 clienti o 10.000 clienti costa quasi uguale. il software scala, le persone no.</p>

            <ActionList items={[
                "mappa tutti i processi ripetitivi della tua azienda.",
                "implementa un autoresponder immediato per ogni richiesta di contatto.",
                "collega il tuo calendario al sito per eliminare il ping-pong di email per fissare appuntamenti."
            ]} />
        </>
    )
  },
  {
    id: 6,
    title: "il tuo sito è un cimitero?",
    excerpt: "il 99% dei siti web sono bellissimi funerali digitali. nessuno li visita, nessuno compra. ecco come trasformare una vetrina statica in una macchina da guerra.",
    readTime: "19 min",
    category: "web design",
    image: "https://images.unsplash.com/photo-1550439062-609e1531270e?auto=format&fit=crop&q=80&w=1600",
    highlight: "MatrixGreen",
    themeColor: "emerald",
    content: (
        <>
            <p className="lead text-2xl md:text-3xl font-serif mb-12 italic border-l-4 border-emerald-500 pl-6 lowercase">
                "il web design non è arte. è architettura di vendita. se è bello ma non converte, è solo <strong className="text-emerald-500">spazzatura decorativa</strong>."
            </p>

            <p>la maggior parte delle web agency ti truffa. ti vendono siti "vetrina". belli, pieni di animazioni, con foto stock sorridenti. ma completamente inutili. un sito vetrina aspetta che qualcuno entri. un sito <strong>funnel</strong> prende il visitatore per il collo e lo trascina alla cassa.</p>
            <p>il tuo sito ha un solo compito: convertire traffico freddo in lead caldi. tutto il resto è vanità.</p>

            <ChapterTitle number="01">la regola dei 3 secondi</ChapterTitle>
            <p>un utente decide se restare sul tuo sito in meno di 3 secondi. se in quel tempo non capisce: 1) cosa fai, 2) perché serve a lui, 3) cosa deve fare... se ne va. </p>
            <p>elimina slider, video pesanti in autoplay, menu complessi. headline chiara. sottotitolo di beneficio. bottone enorme.</p>

            <InsightBox title="morte allo slider">
                <p>gli slider in home page sono il cancro della conversione. nessuno guarda la seconda slide. nascondono le informazioni vitali. usa una <strong>hero section</strong> statica e potente.</p>
            </InsightBox>

            <ChapterTitle number="02">mobile first o morte</ChapterTitle>
            <p>il 90% del tuo traffico arriva da smartphone. eppure i designer progettano su schermi da 27 pollici. follia. il tuo sito deve essere perfetto su un iphone vecchio, con connessione lenta, mentre l'utente è distratto in metro. se funziona lì, funziona ovunque.</p>

            <DataBlock label="traffico mobile globale" value="92%" delta="trend in crescita" color="green" />

            <ChapterTitle number="03">ogni pagina ha un solo scopo</ChapterTitle>
            <p>la home page serve a smistare. la landing page serve a vendere. il blog serve a educare. non mischiare gli obiettivi. su una landing page di vendita, togli il menu di navigazione. non dare vie di fuga. o comprano o chiudono.</p>

            <ActionList items={[
                "controlla la velocità del tuo sito su google pagespeed. se è sotto 90, stai perdendo soldi.",
                "togli ogni link social dall'header. perché vuoi mandarli via dal tuo sito?",
                "metti una call to action chiara in ogni singola sezione della pagina."
            ]} />
        </>
    )
  }
];

export const Blog: React.FC = () => {
  const [activePost, setActivePost] = useState<typeof blogPosts[0] | null>(null);

  // Scroll to top when opening a post
  useEffect(() => {
    if (activePost) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [activePost]);

  const getThemeStyles = (color: string) => {
    switch (color) {
      case 'red':
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(153, 27, 27, 0.4) 0%, transparent 60%)' };
      case 'blue':
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(14, 116, 144, 0.4) 0%, transparent 60%)' };
      case 'gold':
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(133, 77, 14, 0.4) 0%, transparent 60%)' };
      case 'purple':
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(107, 33, 168, 0.4) 0%, transparent 60%)' };
      case 'emerald':
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(6, 95, 70, 0.4) 0%, transparent 60%)' };
      default:
        return { bgOverlay: 'radial-gradient(circle at 50% -20%, rgba(51, 65, 85, 0.4) 0%, transparent 60%)' };
    }
  };

  const currentTheme = activePost ? getThemeStyles(activePost.themeColor || 'silver') : null;

  return (
    <AnimatePresence mode="wait">
        {!activePost ? (
            // --- VIEW 1: LISTA (GRID) ---
            <MotionDiv 
                key="list"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="pt-32 pb-40 relative min-h-screen bg-[#030303] overflow-hidden"
            >
                <CosmicAtmosphere />

                <div className="container mx-auto px-4 relative z-10 max-w-7xl">
                    {/* Header */}
                    <div className="flex flex-col items-center justify-center mb-40 mt-10">
                        <div className="w-[1px] h-20 bg-gradient-to-b from-transparent via-slate-400 to-transparent mb-8"></div>
                        <MotionDiv initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="relative border border-slate-700/50 bg-black/40 backdrop-blur-xl px-8 py-3 rounded-full mb-10">
                            <div className="flex items-center gap-4">
                                <div className="w-2 h-2 bg-slate-200 rounded-full animate-pulse shadow-[0_0_10px_white]"></div>
                                <span className="text-[10px] font-mono text-slate-300 uppercase tracking-[0.4em] font-bold lowercase">
                                    intelligence archive
                                </span>
                                <div className="w-2 h-2 bg-slate-200 rounded-full animate-pulse shadow-[0_0_10px_white]"></div>
                            </div>
                        </MotionDiv>
                        <h1 className="text-center">
                            <span className="block font-serif text-6xl md:text-9xl font-black tracking-tighter leading-[0.85] mb-2 mix-blend-luminosity opacity-30 text-slate-600 lowercase">empire</span>
                            <span className="block font-serif text-6xl md:text-9xl font-black tracking-tighter leading-[0.85] text-transparent bg-clip-text bg-gradient-to-b from-white via-slate-300 to-slate-600 drop-shadow-[0_10px_20px_rgba(0,0,0,1)] relative z-10 -mt-8 md:-mt-16 lowercase">insights</span>
                        </h1>
                    </div>

                    {/* Featured Post (Hero) */}
                    <div className="mb-40 relative cursor-pointer" onClick={() => setActivePost(blogPosts[0])}>
                         <MetallicFrame intensity="gold" className="w-full min-h-[750px] md:min-h-[80vh] relative group shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                            <div className="absolute inset-0 group-hover:scale-105 transition-transform duration-[1.5s] ease-out">
                               <img src={blogPosts[0].image} alt="Featured" className="w-full h-full object-cover opacity-90 transition-all duration-1000" />
                               {/* LIGHTER GRADIENTS FOR VISIBILITY */}
                               <div className="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent"></div>
                               <div className="absolute inset-0 bg-gradient-to-r from-[#050505] via-[#050505]/20 to-transparent"></div>
                            </div>
                            <div className="absolute bottom-0 left-0 p-8 md:p-16 w-full md:w-4/5 lg:w-2/3 z-20 flex flex-col justify-end h-full">
                               <div className="flex items-center gap-6 mb-8">
                                  <div className="px-4 py-1 border border-gold-500/50 bg-black/50 text-gold-500 font-mono text-[9px] uppercase tracking-[0.3em] backdrop-blur-md lowercase">strategy core</div>
                                  <div className="h-[1px] w-20 bg-gold-500"></div>
                                </div>
                               <h2 className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-slate-500 leading-[0.9] mb-8 drop-shadow-lg tracking-tighter lowercase">copywriting:<br/>macchina da soldi</h2>
                               <SilverBody className="max-w-xl text-lg md:text-2xl mb-12 lowercase border-l-2 border-gold-500/50 pl-6 backdrop-blur-sm bg-black/20 p-4 rounded-r-lg">
                                  se i copywriter non esistessero, le aziende farebbero prima a bruciare i soldi.
                               </SilverBody>
                               <div className="flex items-center gap-4 group/btn">
                                  <div className="w-14 h-14 border border-gold-400 rounded-full flex items-center justify-center bg-white/5 backdrop-blur group-hover/btn:bg-white group-hover/btn:text-black transition-all duration-500"><ArrowRight size={24} /></div>
                                  <span className="font-mono text-sm uppercase tracking-[0.3em] text-gold-400 group-hover/btn:text-white transition-colors font-bold lowercase">accedi al manuale</span>
                               </div>
                            </div>
                         </MetallicFrame>
                    </div>

                    {/* Grid List */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-16 mb-40">
                        {blogPosts.slice(1).map((post) => (
                            <MotionDiv
                                key={post.id}
                                initial={{ opacity: 0, y: 50 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                className="group flex flex-col gap-6 cursor-pointer"
                                onClick={() => setActivePost(post as any)}
                            >
                                <MetallicFrame intensity={post.themeColor as any} className="aspect-[16/10] shadow-2xl">
                                    <div className="absolute inset-0 overflow-hidden">
                                        <img src={post.image} alt={post.title} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 opacity-90 group-hover:opacity-100" />
                                        <div className="absolute inset-0 bg-gradient-to-tr from-black/80 via-transparent to-transparent z-10" />
                                        <div className="absolute top-0 left-0 w-full h-[1px] bg-white/30 z-20 group-hover:top-full transition-all duration-[1.5s] ease-in-out opacity-0 group-hover:opacity-100"></div>
                                    </div>
                                </MetallicFrame>
                                <div className="px-2">
                                    <div className="flex justify-between items-end mb-4 border-b border-slate-800 pb-4">
                                        <span className="font-mono text-[9px] uppercase tracking-[0.2em] text-slate-500 font-bold group-hover:text-white transition-colors lowercase">{post.category}</span>
                                        <span className="font-mono text-[9px] text-slate-600">{post.readTime}</span>
                                    </div>
                                    <h3 className="font-serif text-3xl md:text-4xl font-bold leading-none mb-4 group-hover:text-slate-200 transition-colors lowercase">{post.title}</h3>
                                    <SilverBody className="text-sm md:text-base mb-6 lowercase opacity-70 group-hover:opacity-100 transition-opacity">{post.excerpt}</SilverBody>
                                    <div className="flex items-center gap-2 text-[9px] font-mono uppercase tracking-widest text-slate-500 group-hover:text-white transition-colors lowercase">
                                        <Zap size={10} className={post.themeColor === "red" ? "text-red-500" : post.themeColor === "blue" ? "text-cyan-500" : post.themeColor === "purple" ? "text-purple-500" : post.themeColor === "emerald" ? "text-emerald-500" : "text-yellow-500"} />
                                        read data
                                    </div>
                                </div>
                            </MotionDiv>
                        ))}
                    </div>
                </div>
            </MotionDiv>
        ) : (
            // --- VIEW 2: DETTAGLIO POST ---
            <MotionDiv
                key="detail"
                initial={{ opacity: 0, scale: 0.98 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, y: 50 }}
                transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }} 
                className={`pt-0 relative min-h-screen overflow-hidden selection:bg-gold-500/30 selection:text-white`}
            >
                <CosmicAtmosphere />
                
                {/* 
                   --------------------------------------------------
                   NEW HERO COVER SECTION
                   "Ogni Copertina del blog dell'articolo deve avere un'immagine di sfondo"
                   --------------------------------------------------
                */}
                <div className="relative w-full min-h-[70vh] flex flex-col items-center justify-center mb-0 mt-0">
                    
                    {/* Background Image Container */}
                    <div className="absolute inset-0 w-full h-full z-0 overflow-hidden">
                        <motion.div 
                           initial={{ scale: 1.1 }}
                           animate={{ scale: 1 }}
                           transition={{ duration: 2, ease: "easeOut" }}
                           className="w-full h-full"
                        >
                            <img 
                              src={activePost.image} 
                              alt={activePost.title} 
                              className="w-full h-full object-cover opacity-50"
                            />
                        </motion.div>
                        
                        {/* Gradients for readability */}
                        <div className="absolute inset-0 bg-[#020202]/40 mix-blend-multiply"></div>
                        <div className="absolute inset-0 bg-gradient-to-t from-[#020202] via-[#020202]/50 to-transparent"></div>
                        <div className="absolute inset-0 bg-gradient-to-b from-[#020202]/80 via-transparent to-[#020202]/20"></div>
                    </div>

                    {/* Navigation Back Button (Floating on Cover) */}
                    <div className="absolute top-32 left-4 md:left-8 z-50">
                        <button 
                            onClick={() => setActivePost(null)}
                            className="group flex items-center gap-4 text-white hover:text-slate-300 transition-colors"
                        >
                            <div className={`w-12 h-12 rounded-full border bg-black/50 backdrop-blur-md flex items-center justify-center transition-colors group-hover:bg-white/10 border-white/20`}>
                                <ArrowLeft size={20} className="text-white" />
                            </div>
                            <span className="font-mono text-xs uppercase tracking-[0.2em] font-bold hidden md:inline-block text-shadow-sm lowercase">torna all'archivio</span>
                        </button>
                    </div>

                    {/* Hero Content */}
                    <div className="relative z-10 container mx-auto px-4 max-w-5xl text-center pt-32">
                        <motion.div 
                           initial={{ opacity: 0, y: 20 }}
                           animate={{ opacity: 1, y: 0 }}
                           transition={{ delay: 0.3 }}
                           className="flex items-center justify-center gap-4 mb-8"
                        >
                            <span className={`font-mono text-[10px] uppercase tracking-widest px-4 py-1.5 rounded-full border bg-black/40 backdrop-blur-md border-white/20 text-white shadow-lg lowercase`}>
                              {activePost.category}
                            </span>
                        </motion.div>

                        <motion.h1 
                            initial={{ opacity: 0, scale: 0.95 }}
                            animate={{ opacity: 1, scale: 1 }}
                            transition={{ delay: 0.4 }}
                            className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-white leading-[0.9] tracking-tighter mb-8 drop-shadow-2xl lowercase"
                        >
                            {activePost.title}
                        </motion.h1>
                        
                        <motion.div 
                           initial={{ opacity: 0 }}
                           animate={{ opacity: 1 }}
                           transition={{ delay: 0.5 }}
                           className="flex items-center justify-center gap-6 text-[10px] font-mono uppercase tracking-widest text-gray-200 lowercase"
                        >
                             <span className="flex items-center gap-2"><User size={12}/> empire intelligence</span>
                             <span className="flex items-center gap-2"><Clock size={12}/> {activePost.readTime} read</span>
                        </motion.div>
                    </div>
                </div>

                <div 
                    className="fixed inset-0 pointer-events-none z-0 mix-blend-screen opacity-40 transition-all duration-1000"
                    style={{ background: currentTheme?.bgOverlay }}
                />

                <style dangerouslySetInnerHTML={{ __html: `
                    .silver-prose p, .silver-prose li, .silver-prose span {
                        background: linear-gradient(180deg, #FFFFFF 0%, #CBD5E1 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        text-shadow: 0px 0px 20px rgba(255,255,255,0.1);
                        font-weight: 300;
                        line-height: 1.8;
                    }
                    .silver-prose strong, .silver-prose b, .silver-prose em {
                        background: linear-gradient(180deg, #FDE68A 0%, #D4AF37 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        font-weight: 900;
                        letter-spacing: 0.05em;
                        font-style: normal;
                        text-shadow: 0px 0px 15px rgba(212,175,55,0.3);
                        text-transform: uppercase;
                        font-size: 0.95em;
                    }
                    .silver-prose h1, .silver-prose h2, .silver-prose h3, .silver-prose h4 {
                        background: linear-gradient(180deg, #FFFFFF 0%, #94A3B8 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                    }
                `}} />

                <div className="absolute inset-0 opacity-[0.07] mix-blend-soft-light pointer-events-none z-0" style={{ backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")' }}></div>
                
                <div className="container mx-auto px-4 relative z-20 max-w-4xl pt-20">
                    
                    <div className="max-w-3xl mx-auto pb-40">
                        <div className="silver-prose prose prose-invert prose-lg max-w-none">
                            <p className="lead text-xl md:text-2xl font-serif italic text-white/80 border-l-4 border-white/20 pl-6 mb-16 lowercase">
                                {activePost.excerpt}
                            </p>
                            {activePost.content || (
                                <p>Contenuto completo del dossier in fase di decrittazione...</p>
                            )}
                            <div className="mt-24 pt-10 border-t border-white/10 flex items-center justify-between">
                                <div>
                                    <div className="h-12 w-32 bg-white/10 mask-signature opacity-50"></div> 
                                    <p className="text-[10px] font-mono uppercase tracking-widest text-slate-500 mt-2 lowercase">chief strategy officer</p>
                                </div>
                                <Fingerprint size={40} className={`opacity-20 text-white`} />
                            </div>
                        </div>
                        
                        <div className={`mt-24 p-12 rounded-2xl border bg-black/40 backdrop-blur-md text-center border-white/10 shadow-[0_0_50px_rgba(0,0,0,0.5)]`}>
                             <h3 className="font-serif text-3xl text-white mb-4 lowercase">non rimanere teorico</h3>
                             <p className="text-slate-400 text-sm mb-10 max-w-md mx-auto lowercase">la conoscenza senza esecuzione è intrattenimento. hai appena letto come dominare il tuo mercato. ora fallo.</p>
                             <GoldButton href="#contact" variant={activePost.themeColor === 'blue' ? 'cyan' : activePost.themeColor === 'purple' ? 'purple' : activePost.themeColor === 'emerald' ? 'emerald' : 'gold'}>
                                 applica protocollo ora
                             </GoldButton>
                        </div>
                    </div>
                </div>

            </MotionDiv>
        )}
    </AnimatePresence>
  );
};
