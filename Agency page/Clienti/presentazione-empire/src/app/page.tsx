"use client";

import { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { 
  ArrowRight, 
  ArrowLeft, 
  Check, 
  X, 
  Sparkles, 
  Zap, 
  Clock, 
  Shield, 
  Play, 
  Maximize2, 
  Minimize2, 
  Monitor, 
  Send, 
  MessageSquare, 
  Layers, 
  Settings, 
  Users, 
  TrendingUp, 
  ChevronRight, 
  Code, 
  Database, 
  Lock, 
  Mail,
  HelpCircle
} from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";

// URL per la prenotazione (CTA)
const BOOKING_URL = "https://calendly.com/max-infoproducer/30min";

// Mappatura sfondi per ciascuna delle 17 sezioni
const slideBackgrounds = [
  "bg-ink",      // Section 1: Hero Cover
  "bg-ink-2",    // Section 2: Il Problema
  "bg-ink",      // Section 3: ICP
  "bg-ink-2",    // Section 4: Social Proof Bar
  "bg-paper",    // Section 5: Battle-tested / Quotidianità
  "bg-grey",     // Section 6: Dietro vs Davanti
  "bg-ink-2",    // Section 7: Sdoppiata o Centralizzata
  "bg-paper",    // Section 8: Outreach Workflow
  "bg-grey",     // Section 9: Outreach Dashboard Mockup
  "bg-ink",      // Section 10: Outreach Kit
  "bg-paper",    // Section 11: Content Factory Workflow
  "bg-grey",     // Section 12: Copy Factory Mockup
  "bg-paper",    // Section 13: Content Kit
  "bg-ink",      // Section 14: Second Brain Service (NEW)
  "bg-grey",     // Section 15: Second Brain Kit (NEW)
  "bg-grey",     // Section 16: Comparativa
  "bg-grey",     // Section 17: Obiezioni C-P-B
  "bg-ink",      // Section 18: Offerta Speciale Partner
  "bg-ink-2"     // Section 19: Chiusura / CTA
];

// Mappatura contrasti di colore per i testi dell'interfaccia slide
const slideTextColors = [
  "text-white/60", // Section 1: Dark (bg-ink)
  "text-white/60", // Section 2: Dark (bg-ink-2)
  "text-white/60", // Section 3: Dark (bg-ink)
  "text-white/60", // Section 4: Dark (bg-ink-2)
  "text-neutral-800/80", // Section 5: Light (bg-paper)
  "text-neutral-800/80", // Section 6: Light (bg-grey)
  "text-white/60", // Section 7: Dark (bg-ink-2)
  "text-neutral-800/80", // Section 8: Light (bg-paper)
  "text-neutral-800/80", // Section 9: Light (bg-grey)
  "text-white/60", // Section 10: Dark (bg-ink)
  "text-neutral-800/80", // Section 11: Light (bg-paper)
  "text-neutral-800/80", // Section 12: Light (bg-grey)
  "text-neutral-800/80", // Section 13: Light (bg-paper)
  "text-white/60", // Section 14: Dark (bg-ink) — Second Brain Service
  "text-neutral-800/80", // Section 15: Light (bg-grey) — Second Brain Kit
  "text-neutral-800/80", // Section 16: Light (bg-grey)
  "text-neutral-800/80", // Section 17: Light (bg-grey)
  "text-white/60", // Section 18: Dark (bg-ink)
  "text-white/60"  // Section 19: Dark (bg-ink-2)
];

// Mappatura contrasti di colore per i titoli principali dell'interfaccia slide
const slideHeadingColors = [
  "text-white", // Section 1: Dark (bg-ink)
  "text-white", // Section 2: Dark (bg-ink-2)
  "text-white", // Section 3: Dark (bg-ink)
  "text-white", // Section 4: Dark (bg-ink-2)
  "text-[#1c1c1c]", // Section 5: Light (bg-paper)
  "text-[#1c1c1c]", // Section 6: Light (bg-grey)
  "text-white", // Section 7: Dark (bg-ink-2)
  "text-[#1c1c1c]", // Section 8: Light (bg-paper)
  "text-[#1c1c1c]", // Section 9: Light (bg-grey)
  "text-white", // Section 10: Dark (bg-ink)
  "text-[#1c1c1c]", // Section 11: Light (bg-paper)
  "text-[#1c1c1c]", // Section 12: Light (bg-grey)
  "text-[#1c1c1c]", // Section 13: Light (bg-paper)
  "text-white", // Section 14: Dark (bg-ink) — Second Brain Service
  "text-[#1c1c1c]", // Section 15: Light (bg-grey) — Second Brain Kit
  "text-[#1c1c1c]", // Section 16: Light (bg-grey)
  "text-[#1c1c1c]", // Section 17: Light (bg-grey)
  "text-white", // Section 18: Dark (bg-ink)
  "text-white"  // Section 19: Dark (bg-ink-2)
];

// Struttura dati per il Protocollo Obiezioni C-P-B (Claim, Proof, Benefit)
const OBJECTIONS_DATA = [
  {
    eyebrow: 'Obiezione #01 · Il Costo Opportunità',
    title: '“Uso già ChatGPT e qualche tool esistente.',
    italic: 'Perché questo è diverso?”',
    kicker: 'ChatGPT scrive testo generico. Il nostro sistema conosce il tuo cliente, lo contatta e qualifica ogni risposta.',
    cards: [
      {
        kind: "CLAIM",
        icon: Code,
        title: "I tool generici producono output generici.",
        body: "ChatGPT e i SaaS a canone mensile non conoscono il tuo ICP reale. Generano testi astratti che sembrano template perché lo sono. L'outreach manuale e il copy improvvisato non bastano più per scalare.",
        watermark: "C"
      },
      {
        kind: "PROOF",
        icon: Zap,
        title: "Stack calibrato sul tuo brand in 7 giorni.",
        body: "Ti consegniamo un'infrastruttura pre-addestrata con il vocabolario dei tuoi clienti ideali, i loro dolori reali e il framework APSOC. Non devi impostare prompt ogni volta: funziona autonomamente.",
        watermark: "P",
        highlight: true
      },
      {
        kind: "BENEFIT",
        icon: Check,
        title: "Copy che converte e lead qualificati, su pilota automatico.",
        body: "I testi sono emotivamente risonanti con il tuo specifico ICP. L'outreach simula comportamento umano reale. Zero abbonamenti mensili dopo il setup. Zero.",
        watermark: "B"
      }
    ]
  },
  {
    eyebrow: "Obiezione #02 · La Sicurezza dei Profili",
    title: "“Instagram non banna gli account che fanno",
    italic: "outreach automatico?”",
    kicker: "I bot spam tradizionali usano API non autorizzate. Il nostro motore agisce come un essere umano reale.",
    cards: [
      {
        kind: "CLAIM",
        icon: Shield,
        title: "I filtri antispam bloccano i bot, non gli umani.",
        body: "I software di terze parti fanno chiamate API dirette e ripetitive che allertano l'algoritmo. Noi creiamo flussi indistinguibili dall'attività umana.",
        watermark: "C"
      },
      {
        kind: "PROOF",
        icon: Monitor,
        title: "Bypass hardware tramite simulazione umana.",
        body: "Il nostro motore simula orari variabili, agisce in modo umano, controlla tempi di scrittura fluttuanti e naviga tramite sessioni Chrome reali con proxy residenziali dedicati.",
        watermark: "P",
        highlight: true
      },
      {
        kind: "BENEFIT",
        icon: Check,
        title: "Blindatura totale e risposte sicure.",
        body: "Per la piattaforma Meta c'è un operatore reale dietro allo schermo. Voi ottenete risposte dirette e lead caldi in chat senza alcun rischio di limitazione.",
        watermark: "B"
      }
    ]
  },
  {
    eyebrow: "Obiezione #03 · L'Autenticità del Copy",
    title: "“I contenuti generati con l'AI non sembreranno",
    italic: "robotici e piatti?”",
    kicker: "L'AI scrive male se non ha un briefing qualificato. Noi le diamo la voce del target.",
    cards: [
      {
        kind: "CLAIM",
        icon: MessageSquare,
        title: "L'AI generica non conosce il vostro cliente.",
        body: "Le classiche email di ChatGPT falliscono perché usano parole astratte e toni vuoti. Manca la ricerca semantica delle obiezioni reali.",
        watermark: "C"
      },
      {
        kind: "PROOF",
        icon: Sparkles,
        title: "Scansione semantica nel core del copy.",
        body: "La piattaforma estrae prima i termini esatti ed i dolori espressi online dal vostro ICP. Poi, applica quel vocabolario al framework scientifico APSOC.",
        watermark: "P",
        highlight: true
      },
      {
        kind: "BENEFIT",
        icon: Check,
        title: "Copy da professionisti pronti in 15 minuti.",
        body: "I testi prodotti sono allineati, persuasivi ed emotivamente risonanti. Ottenete email pronte da inviare che convertono il 60% in più.",
        watermark: "B"
      }
    ]
  },
  {
    eyebrow: "Obiezione #04 · La Dipendenza Futura",
    title: "“Saremo dipendenti da te per",
    italic: "manutenzione o costi finti?”",
    kicker: "Consegniamo il codice sorgente in chiaro. Diventa un vostro asset aziendale.",
    cards: [
      {
        kind: "CLAIM",
        icon: Lock,
        title: "Nessun vincolo o abbonamento artificiale.",
        body: "I SaaS tradizionali ti tagliano fuori se smetti di pagare la quota mensile. Ti tengono in ostaggio bloccando i tuoi lead ed i tuoi dati storici.",
        watermark: "C"
      },
      {
        kind: "PROOF",
        icon: Database,
        title: "Proprietà intellettuale totale a vita.",
        body: "Installiamo l'applicazione web ed il database direttamente sui vostri server AWS/Vercel. Vi diamo il codice sorgente e la documentazione completa.",
        watermark: "P",
        highlight: true
      },
      {
        kind: "BENEFIT",
        icon: Check,
        title: "Un asset reale a bilancio aziendale.",
        body: "Niente canoni ricorrenti. Solo costi fissi minimi a consumo per le API di OpenAI (pochi centesimi per lancio). Siete liberi e proprietari a vita.",
        watermark: "B"
      }
    ]
  }
];

const totalSlides = 19;

export default function Home() {
  const [slideMode, setSlideMode] = useState(false);
  const [currentSlide, setCurrentSlide] = useState(0);
  
  // Stati per i mockup interattivi
  const [outreachFilter, setOutreachFilter] = useState("all");
  const [copyAngle, setCopyAngle] = useState("problema"); // problema, scarsita, valore
  const [activeObjection, setActiveObjection] = useState(0); // da 0 a 3 per la slide 13 interattiva

  // Carica la modalità presentazione da URL query se presente (?present=true o ?slide=2)
  useEffect(() => {
    if (typeof window !== "undefined") {
      const params = new URLSearchParams(window.location.search);
      if (params.get("present") === "true" || params.get("mode") === "slide") {
        setSlideMode(true);
      }
      const slideParam = params.get("slide");
      if (slideParam) {
        const slideIdx = parseInt(slideParam, 10);
        if (!isNaN(slideIdx) && slideIdx >= 0 && slideIdx < totalSlides) {
          setCurrentSlide(slideIdx);
          setSlideMode(true);
        }
      }
    }
  }, []);

  // Gestione tastiera per le slide
  useEffect(() => {
    if (!slideMode) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "ArrowRight" || e.key === " ") {
        e.preventDefault();
        setCurrentSlide((prev) => Math.min(prev + 1, totalSlides - 1));
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        setCurrentSlide((prev) => Math.max(prev - 1, 0));
      } else if (e.key === "Escape") {
        setSlideMode(false);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [slideMode]);

  const nextSlide = () => setCurrentSlide((prev) => Math.min(prev + 1, totalSlides - 1));
  const prevSlide = () => setCurrentSlide((prev) => Math.max(prev - 1, 0));

  // Touch swipe per slide mode su mobile
  const touchStartX = useRef(0);
  const touchStartY = useRef(0);
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.touches[0].clientX;
    touchStartY.current = e.touches[0].clientY;
  };
  const handleTouchEnd = (e: React.TouchEvent) => {
    if (!slideMode) return;
    const dx = e.changedTouches[0].clientX - touchStartX.current;
    const dy = e.changedTouches[0].clientY - touchStartY.current;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 45) {
      if (dx < 0) nextSlide();
      else prevSlide();
    }
  };

  // Dati di mock per Outreach Dashboard
  const mockLeads = [
    { name: "SaaSify Inc.", channel: "Gmail", status: "Lead Caldo ✦", score: "A1", date: "Oggi" },
    { name: "GrowthStack", channel: "Instagram", status: "Ha Risposto", score: "A2", date: "Oggi" },
    { name: "CloudVibe SaaS", channel: "Gmail", status: "Follow-up inviato", score: "B", date: "Ieri" },
    { name: "PixelFlow Studio", channel: "Instagram", status: "Lead Caldo ✦", score: "A1", date: "2 giorni fa" },
    { name: "EduNexus Academy", channel: "Gmail", status: "Interessato", score: "A2", date: "3 giorni fa" },
  ];

  const filteredLeads = outreachFilter === "all" 
    ? mockLeads 
    : mockLeads.filter(l => outreachFilter === "hot" ? l.status === "Lead Caldo ✦" : l.score === "B");

  // Contenuti generati per il mockup del Content Factory
  const copyVariants: Record<string, { title: string, text: string, annotation: string }> = {
    problema: {
      title: "Carosello #1 — Argomento: Outreach Automatico",
      text: "[ SLIDE 1 / 3 — Headline ]\nIl 97% degli imprenditori fa outreach a mano e si chiede perché non scala.\n\n[ SLIDE 2 / 3 — Struttura ]\nEcco il sistema: Facebook Ads Library estrae i lead. L'AI scrive ogni email personalizzata con APSOC. Gmail invia 300 al giorno. $0 al giorno.\n\n[ SLIDE 3 / 3 — CTA ]\nScrivimi \"SISTEMA\" in DM per una call gratuita. 90% formazione, 10% vendita.",
      annotation: "Framework: PAS applicato al carosello. Slide 1 aggancia con il problema del target. Slide 2 introduce la struttura del sistema (credibilità + curiosità). Slide 3 CTA diretta che genera risposte in DM."
    },
    scarsita: {
      title: "Script Video — Reels 30 secondi",
      text: "[ HOOK — 0-3 sec ]\nLa verità brutale sull'outreach che nessuno ti dice.\n\n[ CORPO — 3-25 sec ]\nMandare DM a mano non scala. Ecco il sistema che manda 300 email personalizzate al giorno, per zero euro — mentre dormi. Niente abbonamenti. Il codice è tuo per sempre.\n\n[ CTA — 25-30 sec ]\nVuoi vedere come funziona? Link in bio. Commenta \"SISTEMA\".",
      annotation: "Framework: Hook-Corpo-CTA per Reels da 30 secondi. I primi 3 secondi sono critici per il retention rate. La CTA doppia (link + commento) massimizza il segnale di engagement all'algoritmo."
    },
    valore: {
      title: "Caption Instagram — Angolo Educativo",
      text: "Come mandiamo 300 email personalizzate al giorno senza toccare nulla.\n\n📌 Il sistema in 4 passi:\n→ Scrapa la Facebook Ads Library per lead qualificati\n→ Estrae le email dai siti web automaticamente\n→ Scrive ogni email con il framework APSOC via AI\n→ Invia via Gmail. €0 al giorno.\n\nVuoi il setup completo in 7 giorni? Scrivici \"SISTEMA\" in DM 👇\n\n#automazione #marketing #outreach #digitalempire",
      annotation: "Framework: Content Marketing educativo con CTA DM. Rivela abbastanza da generare curiosità e autorevolezza, senza svelare tutto. L'elenco puntato aumenta la leggibilità e le save. Hashtag misti: volume alto + niche."
    }
  };

  // Dinamismo stili per il wrapper della presentazione
  const activeBg = slideBackgrounds[currentSlide];
  const activeText = slideTextColors[currentSlide];
  const activeHeading = slideHeadingColors[currentSlide];
  const isLightSlide = activeBg === "bg-paper" || activeBg === "bg-grey";
  const borderContrast = isLightSlide ? "border-black/10" : "border-white/5";

  return (
    <div className="relative min-h-screen selection:bg-[#fb4604] selection:text-white overflow-x-hidden">
      
      {/* ─── SLIDE NAV OVERLAY ─── */}
      {slideMode && (
        <div className={`fixed bottom-0 inset-x-0 z-[110] h-14 flex items-center justify-between px-4 md:px-10 ${isLightSlide ? 'bg-gradient-to-t from-black/[0.07] to-transparent' : 'bg-gradient-to-t from-black/25 to-transparent'}`}>
          <span className={`text-[10px] font-mono tracking-widest hidden sm:block ${isLightSlide ? 'text-black/30' : 'text-white/30'}`}>
            {String(currentSlide + 1).padStart(2, '0')} / {totalSlides}
          </span>
          <div className={`flex-1 sm:mx-8 mx-2 h-px ${isLightSlide ? 'bg-black/10' : 'bg-white/10'} rounded-full overflow-hidden`}>
            <div className="h-full bg-orange-pure rounded-full transition-all duration-300" style={{ width: `${((currentSlide + 1) / totalSlides) * 100}%` }} />
          </div>
          <div className="flex items-center gap-2">
            <button onClick={prevSlide} disabled={currentSlide === 0}
              className={`w-10 h-10 sm:w-8 sm:h-8 rounded-full border flex items-center justify-center ${isLightSlide ? 'border-black/10 text-black/50 hover:bg-black/5' : 'border-white/10 text-white/40 hover:bg-white/5'} transition disabled:opacity-20 cursor-pointer`}>
              <ArrowLeft className="h-4 w-4 sm:h-3.5 sm:w-3.5" />
            </button>
            <button onClick={nextSlide} disabled={currentSlide === totalSlides - 1}
              className="w-10 h-10 sm:w-8 sm:h-8 rounded-full bg-orange-pure text-white flex items-center justify-center hover:brightness-110 transition disabled:opacity-20 cursor-pointer shadow-md shadow-orange-pure/40">
              <ArrowRight className="h-4 w-4 sm:h-3.5 sm:w-3.5" />
            </button>
          </div>
          <button onClick={() => setSlideMode(false)} className={`ml-3 p-1 ${isLightSlide ? 'text-black/25 hover:text-black/60' : 'text-white/25 hover:text-white/60'} transition cursor-pointer`}>
            <Monitor className="h-4 w-4" />
          </button>
        </div>
      )}

      {/* ─── LANDING PAGE / SLIDE MODE CONTENT ─── */}
      <div className={slideMode ? "slide-viewport" : "w-full flex flex-col"}>

        {/* Header Minimale Fissato (solo in landing mode) */}
        {!slideMode && (
          <header className="fixed top-0 inset-x-0 z-[100] border-b border-white/5 bg-[#1c1c1c]/70 backdrop-blur-md px-4 md:px-6 py-3.5 flex justify-between items-center">
            <div className="flex items-center gap-2 md:gap-3">
              <span className="text-orange-pure font-bold tracking-tight text-base md:text-lg">DIGITAL EMPIRE</span>
              <span className="hidden md:inline text-white/20 text-xs">✦</span>
              <span className="hidden md:inline text-white/50 text-xs tracking-wider uppercase">Sistemi di automazione ed acquisizione</span>
            </div>
            <button
              onClick={() => setSlideMode(true)}
              className="flex items-center gap-1.5 text-[10px] font-mono font-bold tracking-widest text-white px-3 py-1.5 rounded-lg transition cursor-pointer"
              style={{ backgroundColor: '#fb4604', boxShadow: '0 0 20px 0 rgba(251,70,4,0.45), inset 0 1px 0 rgba(255,255,255,0.18)' }}
            >
              <Play className="h-2.5 w-2.5" style={{ fill: 'white', stroke: 'none' }} />
              <span className="hidden sm:inline">PRESENTAZIONE</span>
              <span className="sm:hidden">SLIDE</span>
            </button>
          </header>
        )}

        {/* Wrapper delle sezioni a scorrimento / slide track */}
        <main
          className={slideMode ? "slide-track" : "w-full pt-[73px]"}
          style={slideMode ? { transform: `translateX(-${currentSlide * 100}vw)`, transition: 'transform 0.75s cubic-bezier(0.22, 1, 0.36, 1)' } : undefined}
          onTouchStart={handleTouchStart}
          onTouchEnd={handleTouchEnd}
        >
            
            {/* Section 1: Hero Cover */}
            <section className={`bg-ink relative overflow-hidden section min-h-[90vh] flex flex-col justify-center${slideMode ? ' slide-section-mode' : ''}`}>
              {/* Ambient glow */}
              <div className="absolute inset-0 pointer-events-none z-0" style={{ background: 'radial-gradient(ellipse 900px 700px at -200px -200px, rgba(251,70,4,0.09) 0%, transparent 60%), radial-gradient(ellipse 600px 500px at calc(100% + 120px) calc(100% + 120px), rgba(217,212,225,0.06) 0%, transparent 60%)' }}></div>

              <div className="max-w-4xl mx-auto px-6 text-center relative z-10">

                <Reveal delay={0.1}>
                  <div className="pre-headline mb-8">DIGITAL EMPIRE · AUTOMAZIONE AI PROPRIETARIA</div>
                </Reveal>

                <Reveal delay={0.2}>
                  <h1 className="font-black mb-8" style={{ lineHeight: 1 }}>
                    <div style={{ fontSize: 'clamp(28px, 5vw, 64px)', letterSpacing: '-0.01em', marginBottom: '0.02em' }}>
                      <span className="text-silver-white">Smetti di fare</span>
                    </div>
                    <div style={{ lineHeight: 0.72 }}>
                      <span className="text-silver-white" style={{ fontSize: 'clamp(72px, 21vw, 255px)', letterSpacing: '-0.035em' }}>tutto</span>
                    </div>
                    <div>
                      <span className="text-silver-orange italic" style={{ fontSize: 'clamp(36px, 7.5vw, 92px)', letterSpacing: '-0.01em', filter: 'drop-shadow(0 0 50px rgba(251,70,4,0.25))' }}>a mano.</span>
                    </div>
                  </h1>
                </Reveal>

                <Reveal delay={0.35}>
                  <p className="text-sm md:text-lg text-white/60 max-w-xl mx-auto mb-10 leading-relaxed">
                    Tre motori AI installati sui tuoi server: outreach su Gmail e Social Media, produzione contenuti su pilota automatico e Second Brain per la memoria del business. <strong className="text-white/85 font-semibold">Zero canoni mensili. Codice tuo per sempre.</strong>
                  </p>
                </Reveal>

                <Reveal delay={0.48}>
                  <a href={BOOKING_URL} className="btn-orange btn-orange--lg group">
                    Prenota una chiamata strategica
                    <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-0.5" />
                  </a>
                </Reveal>

                {/* Mini Proof Bar */}
                <Reveal delay={0.6}>
                  <div className="flex justify-center gap-0 mt-12 max-w-sm mx-auto border border-white/[0.07] rounded-2xl overflow-hidden">
                    <div className="flex-1 text-center py-4 px-3 border-r border-white/[0.07]">
                      <div className="text-2xl font-black text-silver-orange leading-[1.2]"><CountUp to={7} suffix=" gg" /></div>
                      <div className="text-[10px] text-white/35 uppercase tracking-wider mt-1 font-semibold">Setup</div>
                    </div>
                    <div className="flex-1 text-center py-4 px-3 border-r border-white/[0.07]">
                      <div className="text-2xl font-black text-silver-orange leading-[1.2]">€0</div>
                      <div className="text-[10px] text-white/35 uppercase tracking-wider mt-1 font-semibold">Canoni</div>
                    </div>
                    <div className="flex-1 text-center py-4 px-3">
                      <div className="text-2xl font-black text-silver-orange leading-[1.2]"><CountUp to={100} suffix="%" /></div>
                      <div className="text-[10px] text-white/35 uppercase tracking-wider mt-1 font-semibold">Tuo</div>
                    </div>
                  </div>
                </Reveal>
              </div>

              {/* Bottom divider */}
              <div className="divider-gradient absolute bottom-0 inset-x-0"></div>
            </section>

            {/* Section 2: Il Collo di Bottiglia */}
            <section className={`bg-ink-2 section section-border-t relative overflow-hidden${slideMode ? ' slide-section-mode' : ''}`}>
              {/* Ambient glow */}
              <div className="absolute inset-0 pointer-events-none z-0" style={{ background: 'radial-gradient(ellipse 700px 350px at 50% 100%, rgba(251,70,4,0.07) 0%, transparent 70%)' }}></div>

              <div className="max-w-4xl mx-auto px-6 relative z-10 w-full">
                <div className={`text-center ${slideMode ? 'mb-6' : 'mb-12'}`}>
                  <div className="bubble-ink mb-3">
                    <Zap className="h-4 w-4 text-orange-pure" />
                    <span>Tre sistemi AI, installati sui tuoi server</span>
                  </div>
                  <h2 className={`font-bold ${slideMode ? 'text-2xl md:text-4xl' : 'text-3xl md:text-5xl'}`}>
                    <span className="text-silver-white">Tre motori che cambiano</span>
                    <br />
                    <span className="text-orange-pure italic">tutta la tua operatività.</span>
                  </h2>
                </div>

                <div className={`grid md:grid-cols-3 gap-6 ${slideMode ? 'mt-4' : 'mt-12'}`}>
                  <Reveal variant="left">
                    <div className="card-silver-orange variant-orange flex flex-col justify-between h-full relative overflow-hidden" style={slideMode ? { padding: '1.25rem 1.5rem' } : undefined}>
                      <span className="absolute bottom-[-20px] right-[-4px] font-black select-none pointer-events-none leading-none text-[120px]" style={{ color: 'rgba(201,55,10,0.07)' }}>01</span>
                      <div className="relative z-10">
                        <div className="inline-flex items-center gap-1.5 bg-white/40 border border-white/60 text-[#7a1f02] text-[10px] font-black tracking-widest uppercase px-3 py-1 rounded-md mb-3">
                          <Send className="h-3 w-3" /> OUTREACH FACTORY
                        </div>
                        <h3 className={`font-bold mb-2 ${slideMode ? 'text-base' : 'text-xl'}`}>Acquisisce clienti in automatico, 24/7</h3>
                        <p className={`leading-relaxed ${slideMode ? 'text-xs' : 'text-sm'}`}>
                          Gmail e Social Media su pilota automatico. Il sistema estrae lead dai profili giusti, personalizza ogni messaggio via AI e invia 300+ email al giorno. Ogni mattina trovi nuove risposte qualificate in inbox.
                        </p>
                      </div>
                      <div className={`border-t border-[#3d1204]/30 text-[#2a0a00] font-mono relative z-10 font-bold text-xs ${slideMode ? 'pt-2 mt-3' : 'pt-4 mt-6'}`}>
                        300+ email/gg · Gmail + Social Media · €0 mensili
                      </div>
                    </div>
                  </Reveal>

                  <Reveal variant="right">
                    <div className="card-silver-orange flex flex-col justify-between h-full relative overflow-hidden" style={slideMode ? { padding: '1.25rem 1.5rem' } : undefined}>
                      <span className="absolute bottom-[-20px] right-[-4px] font-black select-none pointer-events-none leading-none text-[120px]" style={{ color: 'rgba(138,133,148,0.08)' }}>02</span>
                      <div className="relative z-10">
                        <div className="inline-flex items-center gap-1.5 bg-white/50 border border-white/70 text-[#4a3060] text-[10px] font-black tracking-widest uppercase px-3 py-1 rounded-md mb-3">
                          <Sparkles className="h-3 w-3" /> CONTENT FACTORY
                        </div>
                        <h3 className={`font-bold mb-2 ${slideMode ? 'text-base' : 'text-xl'}`}>Genera e pubblica contenuti social in automatico</h3>
                        <p className={`leading-relaxed ${slideMode ? 'text-xs' : 'text-sm'}`}>
                          Pubblichi già? Bene. Questo sistema moltiplica la tua produttività. L&apos;AI genera il copy, il motore di automazione costruisce le grafiche visive e organizza tutto automaticamente. Script video, caption, hashtag. Settimane di contenuti in pochi minuti.
                        </p>
                      </div>
                      <div className={`border-t border-[#1c1c1c]/20 text-[#1c1c1c] font-mono relative z-10 font-bold text-xs ${slideMode ? 'pt-2 mt-3' : 'pt-4 mt-6'}`}>
                        Caroselli IG · Script Video · Caption + Hashtag · Google Drive
                      </div>
                    </div>
                  </Reveal>

                  <Reveal>
                    <div className="card-silver-orange flex flex-col justify-between h-full relative overflow-hidden" style={{ ...(slideMode ? { padding: '1.25rem 1.5rem' } : {}), background: 'linear-gradient(145deg, #ffffff 0%, #eef3ff 40%, #dde6ff 70%, #c8d8f8 100%)', borderColor: 'rgba(74,109,192,0.25)' }}>
                      <span className="absolute bottom-[-20px] right-[-4px] font-black select-none pointer-events-none leading-none text-[120px]" style={{ color: 'rgba(42,80,144,0.07)' }}>03</span>
                      <div className="relative z-10">
                        <div className="inline-flex items-center gap-1.5 bg-white/60 border border-white/70 text-[#1e3a7a] text-[10px] font-black tracking-widest uppercase px-3 py-1 rounded-md mb-3">
                          <Database className="h-3 w-3" /> SECOND BRAIN
                        </div>
                        <h3 className={`font-bold mb-2 ${slideMode ? 'text-base' : 'text-xl'}`}>L&apos;AI che conosce davvero il tuo business</h3>
                        <p className={`leading-relaxed ${slideMode ? 'text-xs' : 'text-sm'}`}>
                          Ogni tool AI dimentica tutto tra una sessione e l&apos;altra. Il Second Brain è la knowledge base interconnessa — visualizzata come grafo — che dà all&apos;LLM il contesto permanente: clienti, processi, brand voice, decisioni. Mai da rispiegare.
                        </p>
                      </div>
                      <div className={`border-t border-[#1e3a7a]/20 text-[#1e3a7a] font-mono relative z-10 font-bold text-xs ${slideMode ? 'pt-2 mt-3' : 'pt-4 mt-6'}`}>
                        Knowledge Graph · Context Engineering · Memoria Permanente
                      </div>
                    </div>
                  </Reveal>
                </div>

                <div className={`max-w-3xl mx-auto border-t border-white/10 ${slideMode ? 'mt-6 pt-5' : 'mt-10 pt-8'}`}>
                  <p className={`text-white/90 leading-relaxed text-center font-medium ${slideMode ? 'text-sm' : 'text-base md:text-lg font-light'}`}>
                    Tutti e tre vengono installati sui tuoi server — <span className="hl-block font-semibold">codice sorgente incluso</span> — e sono tuoi per sempre. Zero canoni mensili. L&apos;outreach gira ogni mattina da solo. La Content Factory produce su richiesta. Il Second Brain ricorda tutto.
                  </p>
                </div>
              </div>
            </section>

            {/* Section 3: Per Chi È (ICP) */}
            <section className={`bg-ink section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-16 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Users className="h-4 w-4" />
                    <span>Ideal Customer Profile</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold">
                    <span className="text-silver-white">Ideato su misura per</span>
                    <br />
                    <span className="text-orange-pure italic font-medium">Creator, Coach & Business Owner.</span>
                  </h2>
                </div>

                <div className="grid md:grid-cols-2 gap-8">
                  {/* Per chi è */}
                  <Reveal variant="left">
                    <div className="card-silver-orange h-full" style={{ borderColor: 'rgba(52,211,153,0.35)' }}>
                      <h3 className="text-base font-bold text-neutral-800 mb-6 flex items-center gap-2">
                        <Check className="h-5 w-5 text-emerald-600" />
                        <span>Questo sistema è perfetto per te se:</span>
                      </h3>
                      <ul className="space-y-4 text-sm text-neutral-800">
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-[#c9370a] mt-0.5 shrink-0" />
                          <span>Promuovi prodotti digitali, servizi o consulenza high ticket.</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-[#c9370a] mt-0.5 shrink-0" />
                          <span>Hai già un prodotto sul mercato e desideri scalare il volume di contatti.</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-[#c9370a] mt-0.5 shrink-0" />
                          <span>L&apos;outreach ti prosciuga tempo e energie, o non lo fai affatto.</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-[#c9370a] mt-0.5 shrink-0" />
                          <span>Capisci il valore della tecnologia proprietaria e non cerchi un SaaS di terze parti instabile.</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-[#c9370a] mt-0.5 shrink-0" />
                          <span>Ogni lancio ti costa 2-3 settimane solo per produrre il copy. Il tempo è denaro. Sai che così non può continuare.</span>
                        </li>
                      </ul>
                    </div>
                  </Reveal>

                  {/* Per chi non è */}
                  <Reveal variant="right">
                    <div className="card-silver-orange h-full opacity-70" style={{ filter: 'grayscale(0.3)' }}>
                      <h3 className="text-base font-bold text-neutral-800 mb-6 flex items-center gap-2">
                        <X className="h-5 w-5 text-red-500" />
                        <span>NON fa assolutamente al caso tuo se:</span>
                      </h3>
                      <ul className="space-y-4 text-sm text-neutral-600">
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-neutral-400 mt-0.5 shrink-0" />
                          <span>Non hai un prodotto valido sul mercato (l&apos;automazione amplifica solo ciò che funziona).</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-neutral-400 mt-0.5 shrink-0" />
                          <span>Cerchi un&apos;estensione Chrome da €10 da dimenticare nel browser.</span>
                        </li>
                        <li className="flex items-start gap-2.5">
                          <ChevronRight className="h-4 w-4 text-neutral-400 mt-0.5 shrink-0" />
                          <span>Vuoi delegare interamente il marketing senza comprendere o supervisionare i tuoi flussi.</span>
                        </li>
                      </ul>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 4: Social Proof Bar */}
            <section className={`bg-ink-2 relative overflow-hidden${slideMode ? ' slide-section-mode' : ' py-12'}`}>
              <div className="divider-gradient absolute top-0 inset-x-0"></div>

              {slideMode && (
                <Reveal className="text-center mb-14">
                  <div className="pre-headline" style={{ color: 'rgba(249,249,249,0.3)' }}>I numeri del sistema</div>
                </Reveal>
              )}

              <div className="w-full px-10">
                <div className="grid grid-cols-2 md:grid-cols-4 gap-0 w-full">
                  {[
                    { to: 7, prefix: "", suffix: " gg", label: "Setup Medio" },
                    { to: 24, prefix: "", suffix: "/7", label: "Outreach Attivo" },
                    { to: 100, prefix: "", suffix: "%", label: "Proprietà Codice" },
                    { to: 0, prefix: "€", suffix: "", label: "Canoni Mensili" },
                  ].map((stat, i) => (
                    <Reveal key={i} delay={i * 0.1} className="text-center px-4 border-r border-white/5 last:border-r-0">
                      <div className="font-black text-silver-orange leading-none tracking-tight whitespace-nowrap" style={{ fontSize: slideMode ? 'clamp(56px, 7vw, 110px)' : 'clamp(36px, 4vw, 56px)' }}>
                        {stat.prefix}<CountUp to={stat.to} suffix={stat.suffix} />
                      </div>
                      <div className={`text-white/50 uppercase tracking-widest font-semibold ${slideMode ? 'text-xs mt-5' : 'text-[9px] mt-2'}`}>{stat.label}</div>
                    </Reveal>
                  ))}
                </div>
              </div>

              <div className="divider-gradient absolute bottom-0 inset-x-0"></div>
            </section>

            {/* Section 5: Battle-Tested / Quotidianità */}
            <section className={`bg-paper section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="grid md:grid-cols-2 gap-12 items-center">
                  <Reveal variant="left">
                    <div className="bubble-silver mb-4">
                      <Shield className="h-4 w-4 text-orange-pure" />
                      <span>Zero Teoria. 100% Campo.</span>
                    </div>
                    <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black mb-6">
                      Prendo quello che uso io
                      <br />
                      <span className="text-orange-pure italic font-semibold">ogni singolo giorno</span>
                      <br />
                      <span className="font-black text-silver-black underline decoration-orange-pure decoration-2 underline-offset-4">e lo adatto a te.</span>
                    </h2>
                    <p className="text-neutral-600 text-sm leading-relaxed mb-6">
                      Non ti sto vendendo codici scritti in laboratorio la notte scorsa o accrocchi instabili assemblati su Zapier che si rompono al primo aggiornamento delle API.
                    </p>
                    <p className="text-neutral-600 text-sm leading-relaxed">
                      Questo stack rappresenta <strong className="text-neutral-800 font-bold">il cuore operativo del mio business — e presto del tuo</strong>. Lo uso per scovare lead per la mia agenzia e generare testi commerciali ad alta conversione per i miei clienti. Non dobbiamo ricreare nulla da zero: prendiamo un&apos;infrastruttura d&apos;acciaio, la cuciamo su misura per il tuo brand e la installiamo sui tuoi sistemi.
                    </p>
                  </Reveal>

                  <Reveal variant="right" className="grid grid-cols-1 gap-3">
                    <div className="stat-card-silver text-center">
                      <div className="w-8 h-8 rounded-lg bg-orange-pure/10 flex items-center justify-center mx-auto mb-2">
                        <Zap className="h-4 w-4 text-orange-pure" />
                      </div>
                      <div className="text-3xl font-black text-silver-black tracking-tight leading-[1.25] pb-1"><CountUp to={7} suffix=" gg" /></div>
                      <div className="text-[9px] text-neutral-400 uppercase tracking-widest mt-1.5 font-semibold">Setup Completo Chiavi in Mano</div>
                    </div>

                    <div className="stat-card-silver text-center">
                      <div className="w-8 h-8 rounded-lg bg-orange-pure/10 flex items-center justify-center mx-auto mb-2">
                        <Lock className="h-4 w-4 text-orange-pure" />
                      </div>
                      <div className="text-3xl font-black text-silver-black tracking-tight leading-[1.25] pb-1">€0</div>
                      <div className="text-[9px] text-neutral-400 uppercase tracking-widest mt-1.5 font-semibold">Canoni o Abbonamenti Mensili</div>
                    </div>

                    <div className="stat-card-silver text-center">
                      <div className="w-8 h-8 rounded-lg bg-orange-pure/10 flex items-center justify-center mx-auto mb-2">
                        <Shield className="h-4 w-4 text-orange-pure" />
                      </div>
                      <div className="text-3xl font-black text-silver-black tracking-tight leading-[1.25] pb-1"><CountUp to={100} suffix="%" /></div>
                      <div className="text-[9px] text-neutral-400 uppercase tracking-widest mt-1.5 font-semibold">Proprietà Intellettuale del Codice</div>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 6: Dietro le quinte vs Davanti */}
            <section className={`bg-grey section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-16 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Layers className="h-4 w-4" />
                    <span>Infrastruttura Visiva</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    Il motore AI lavora per te.
                    <br />
                    <span className="text-orange-pure italic font-medium">Tu vedi solo la piattaforma.</span>
                  </h2>
                  <p className="text-neutral-600 text-sm max-w-xl mx-auto mt-4 leading-relaxed">
                    Abbiamo eliminato il caos delle righe di codice o dei terminali spaventosi. Nascondiamo la complessità tecnica dietro a un'interfaccia premium che amerai utilizzare.
                  </p>
                </div>

                <div className="grid md:grid-cols-2 gap-8 mt-12">
                  <Reveal variant="left" className="card-paper flex flex-col justify-between relative overflow-hidden">
                    <div>
                      <span className="text-neutral-400 text-xs font-mono uppercase tracking-widest">[ Dietro le quinte ]</span>
                      <h3 className="text-2xl font-bold text-neutral-800 mt-2 mb-4">I Motori AI</h3>
                      <p className="text-neutral-600 text-sm leading-relaxed mb-6">
                        Sistemi di automazione avanzati che controllano sessioni browser reali, gestiscono proxy residenziali e agiscono in modo indistinguibile da un operatore umano — superando qualsiasi filtro anti-bot. Motore semantico AI pre-caricato con framework CRO per il copywriting di precisione.
                      </p>
                    </div>
                    <div className="border-t border-neutral-100 pt-4 text-xs text-orange-pure font-bold flex items-center gap-1">
                      <Code className="h-4 w-4" /> Automation & Processing Core
                    </div>
                  </Reveal>

                  <Reveal variant="right" className="card-paper flex flex-col justify-between relative overflow-hidden">
                    <div>
                      <span className="text-neutral-400 text-xs font-mono uppercase tracking-widest">[ Davanti a te ]</span>
                      <h3 className="text-2xl font-bold text-neutral-800 mt-2 mb-4">La Piattaforma Web Custom</h3>
                      <p className="text-neutral-600 text-sm leading-relaxed mb-6">
                        Un&apos;interfaccia web disegnata su misura per te, graficamente perfetta, pulita e minimale. Da qui inserisci i brief dei lanci, modifichi al volo le email rigenerando varianti in tempo reale e monitori lo stato di avanzamento e qualifica dei lead caldi.
                      </p>
                    </div>
                    <div className="border-t border-neutral-100 pt-4 text-xs text-orange-pure font-bold flex items-center gap-1">
                      <Monitor className="h-4 w-4" /> Elegant Front-End UI
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 7: Sdoppiata o Centralizzata */}
            <section className={`bg-ink-2 section section-border-t relative overflow-hidden${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="absolute inset-0 pointer-events-none z-0" style={{ background: 'radial-gradient(ellipse 600px 350px at 50% 50%, rgba(251,70,4,0.06) 0%, transparent 70%)' }}></div>
              
              <div className="max-w-4xl mx-auto px-6 text-center">
                <Reveal delay={0.1}>
                  <div className="bubble-ink mb-4">
                    <Settings className="h-4 w-4 text-orange-pure" />
                    <span>Tailored Architecture</span>
                  </div>
                </Reveal>

                <Reveal delay={0.2}>
                  <h2 className="text-3xl md:text-5xl font-bold mb-6">
                    <span className="text-silver-white">Un'unica cabina di regia o</span>
                    <br />
                    <span className="text-orange-pure italic font-semibold">due piattaforme dedicate.</span>
                  </h2>
                </Reveal>

                <Reveal delay={0.3}>
                  <p className="text-white/70 text-sm max-w-xl mx-auto mb-3 leading-relaxed">
                    Sappiamo che ogni azienda ha la sua struttura organizzativa ed abitudini differenti. La visualizzazione e la gestione dei due motori è flessibile al 100% in base al tuo flusso di lavoro.
                  </p>
                  <p className="text-white/50 text-xs max-w-xl mx-auto mb-12 leading-relaxed font-medium uppercase tracking-widest">
                    In tutti i casi, tutto completamente personalizzato.
                  </p>
                </Reveal>

                <div className="grid md:grid-cols-2 gap-8 text-left mt-8">
                  <Reveal variant="left">
                    <div className="card-silver-orange variant-orange h-full">
                      <div className="inline-flex items-center gap-1.5 bg-[#c9370a]/12 border border-[#c9370a]/25 text-[#c9370a] text-[10px] font-bold tracking-widest uppercase px-3 py-1 rounded-md mb-5">
                        <Layers className="h-3 w-3" /> Opzione A
                      </div>
                      <h3 className="text-lg font-bold text-neutral-800 mb-3">La Dashboard Unificata</h3>
                      <p className="text-neutral-800 text-xs leading-relaxed">
                        Un&apos;unica cabina di regia centralizzata. Trovi il pannello di controllo dell&apos;outreach (leads, status, risposte) e l&apos;interfaccia di generazione del copy in un&apos;unica schermata. Ideale se hai una supervisione centralizzata.
                      </p>
                    </div>
                  </Reveal>

                  <Reveal variant="right">
                    <div className="card-silver-orange h-full">
                      <div className="inline-flex items-center gap-1.5 bg-[#8a8594]/12 border border-[#8a8594]/25 text-[#6a6474] text-[10px] font-bold tracking-widest uppercase px-3 py-1 rounded-md mb-5">
                        <Layers className="h-3 w-3" /> Opzione B
                      </div>
                      <h3 className="text-lg font-bold text-neutral-800 mb-3">Due Piattaforme Separate</h3>
                      <p className="text-neutral-800 text-xs leading-relaxed">
                        Due applicazioni web separate. Una dedicata esclusivamente al team vendite (per scovare lead e rispondere su Gmail/IG) ed una isolata per il team marketing/copy (per produrre i contenuti dei lanci). Sinergiche ma indipendenti.
                      </p>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 8: Servizio Outreach Workflow */}
            <section className={`bg-paper section section-border-t relative${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="divider-gradient absolute top-0 inset-x-0"></div>
              <div className="max-w-4xl mx-auto px-6">
                <div className="grid md:grid-cols-2 gap-12 items-center">
                  <Reveal variant="left">
                    <div className="bubble-orange mb-4">
                      <Mail className="h-4 w-4" />
                      <span>Service #01 · Acquisizione lead</span>
                    </div>
                    <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black mb-6">
                      Outreach automatico
                      <br />
                      <span className="text-orange-pure italic font-semibold">su Gmail e Social.</span>
                    </h2>
                    <p className="text-neutral-600 text-sm leading-relaxed mb-4">
                      Mandare 30 DM al giorno a mano richiede 2-3 ore, ogni mattina. Con un tasso di risposta tra il <strong className="text-neutral-800 font-bold">3% e il 7%</strong> perché i messaggi sembrano template. Perché lo sono.
                    </p>
                    <p className="text-neutral-600 text-sm leading-relaxed mb-6">
                      Il nostro motore di automazione sostituisce tutto questo: avvia sessioni browser reali e protette, <strong className="text-neutral-800 font-bold">agisce in modo umano così da non risultare mai un bot</strong>, compila i campi, digita a velocità variabile e invia messaggi di ingaggio personalizzati — senza toccare API sospette.
                    </p>
                    
                    <div className="space-y-4 text-xs text-neutral-800">
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong>Cold-Emailing Sincronizzato</strong>: Touchpoint e follow-up coordinati su Gmail.</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong>Instagram DM Safe</strong>: Comportamento umano protetto per azzerare i blocchi.</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong>Qualificazione Semantica</strong>: Scarta i no ed estrae solo chi dice "Sì, approfondiamo".</span>
                      </div>
                    </div>
                  </Reveal>

                  <Reveal variant="right" className="card-silver-orange variant-orange shadow-md">
                    <h3 className="font-bold text-neutral-800 text-lg mb-6 border-b border-[#c9370a]/15 pb-3 flex items-center gap-2">
                      <Zap className="h-5 w-5 text-[#c9370a]" />
                      <span>Come funziona il workflow:</span>
                    </h3>
                    
                    <div className="space-y-6 relative pl-6 before:absolute before:left-2 before:top-2 before:bottom-2 before:w-0.5 before:bg-orange/20">
                      <div className="relative">
                        <div className="absolute -left-6 top-0 w-4 h-4 rounded-full bg-[#c9370a] border-4 border-[#ffeedd]"></div>
                        <h4 className="font-bold text-neutral-800 text-sm">Step 1: Targeting</h4>
                        <p className="text-neutral-600 text-xs">Il sistema estrae o riceve i profili dei tuoi clienti ideali.</p>
                      </div>

                      <div className="relative">
                        <div className="absolute -left-6 top-0 w-4 h-4 rounded-full bg-[#c9370a] border-4 border-[#ffeedd]"></div>
                        <h4 className="font-bold text-neutral-800 text-sm">Step 2: Primo Contatto</h4>
                        <p className="text-neutral-600 text-xs">Invio del primo messaggio ad altissimo valore e non commerciale.</p>
                      </div>

                      <div className="relative">
                        <div className="absolute -left-6 top-0 w-4 h-4 rounded-full bg-[#c9370a] border-4 border-[#ffeedd]"></div>
                        <h4 className="font-bold text-neutral-800 text-sm">Step 3: Follow up automatico</h4>
                        <p className="text-neutral-600 text-xs">Chi non risponde riceve fino a 3 sequenze automatiche.</p>
                      </div>

                      <div className="relative">
                        <div className="absolute -left-6 top-0 w-4 h-4 rounded-full bg-[#c9370a] border-4 border-[#ffeedd]"></div>
                        <h4 className="font-bold text-neutral-800 text-sm">Step 4: Qualificazione AI e CRM</h4>
                        <p className="text-neutral-600 text-xs">L'AI estrae i lead caldi e li passa con notifiche Slack/CRM.</p>
                      </div>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 9: Dashboard di Acquisizione (MOCKUP INTERATTIVO) */}
            <section className={`bg-grey section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-10 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Monitor className="h-4 w-4" />
                    <span>Interactive UI Demo</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    La tua dashboard di acquisizione.
                    <br />
                    <span className="text-orange-pure italic font-semibold">Prova a filtrare i lead reali:</span>
                  </h2>
                </div>

                {/* Mockup Interattivo UI */}
                <div className="relative max-w-3xl mx-auto">

                <Reveal delay={0.2} className="w-full bg-[#131313] border border-white/10 rounded-2xl overflow-hidden shadow-2xl shadow-black/60 ring-1 ring-white/[0.08]">
                  {/* Top Bar della Dashboard */}
                  <div className="bg-[#1c1c1c] border-b border-white/5 px-6 py-4 flex flex-col sm:flex-row justify-between items-center gap-4">
                    <div className="flex items-center gap-3">
                      <div className="flex gap-1.5">
                        <span className="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                        <span className="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                        <span className="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                      </div>
                      <span className="text-xs font-mono text-white/50">http://outreach-hq.tuodominio.it</span>
                    </div>

                    {/* Filtri interattivi */}
                    <div className="flex bg-[#0a0a0a] rounded-lg p-1 border border-white/5">
                      <button 
                        onClick={() => setOutreachFilter("all")}
                        className={`text-xs px-3 py-1.5 rounded-md transition font-medium cursor-pointer ${outreachFilter === "all" ? "bg-orange-pure text-white" : "text-white/50 hover:text-white"}`}
                      >
                        Tutti
                      </button>
                      <button 
                        onClick={() => setOutreachFilter("hot")}
                        className={`text-xs px-3 py-1.5 rounded-md transition font-medium cursor-pointer ${outreachFilter === "hot" ? "bg-orange-pure text-white" : "text-white/50 hover:text-white"}`}
                      >
                        Lead Caldi
                      </button>
                      <button 
                        onClick={() => setOutreachFilter("b")}
                        className={`text-xs px-3 py-1.5 rounded-md transition font-medium cursor-pointer ${outreachFilter === "b" ? "bg-orange-pure text-white" : "text-white/50 hover:text-white"}`}
                      >
                        In Follow-up
                      </button>
                    </div>
                  </div>

                  {/* Tabella dei lead */}
                  <div className="p-6 overflow-x-auto">
                    <table className="w-full text-left text-xs border-collapse">
                      <thead>
                        <tr className="border-b border-white/5 text-white/40 pb-2">
                          <th className="font-semibold pb-3">AZIENDA / LEAD</th>
                          <th className="font-semibold pb-3">CANALE</th>
                          <th className="font-semibold pb-3">STATO CONVERSAZIONE</th>
                          <th className="font-semibold pb-3">QUALIFICA AI</th>
                          <th className="font-semibold pb-3 text-right">RICEVUTO</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-white/5">
                        {filteredLeads.map((lead, idx) => (
                          <tr key={idx} className="hover:bg-white/2 transition">
                            <td className="py-4 font-bold text-white flex items-center gap-2">
                              <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                              {lead.name}
                            </td>
                            <td className="py-4 text-white/70">{lead.channel}</td>
                            <td className="py-4">
                              <span className={`px-2 py-1 rounded text-[10px] font-bold ${
                                lead.status.includes("Caldo") 
                                  ? "bg-orange-pure/20 text-orange-pure" 
                                  : lead.status.includes("Ha Risposto")
                                  ? "bg-blue-500/20 text-blue-400"
                                  : "bg-white/10 text-white/60"
                              }`}>
                                {lead.status}
                              </span>
                            </td>
                            <td className="py-4">
                              <span className="px-2 py-0.5 rounded bg-white/5 border border-white/10 font-bold text-white/80 font-mono">
                                {lead.score}
                              </span>
                            </td>
                            <td className="py-4 text-right text-white/40">{lead.date}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </Reveal>
                </div>
              </div>
            </section>

            {/* Section 10: Outreach Kit (Tabella del valore) */}
            <section className={`bg-ink section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-12 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Shield className="h-4 w-4" />
                    <span>What's inside</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-white">
                    Cosa include la tua
                    <br />
                    <span className="text-orange-pure italic font-semibold">piattaforma di Outreach.</span>
                  </h2>
                </div>

                <div className="grid md:grid-cols-3 gap-5 mt-12">
                  <Reveal delay={0.1}>
                    <div className="card-silver-orange variant-orange h-full">
                      <div className="w-12 h-12 rounded-xl bg-[#c9370a]/12 flex items-center justify-center mb-5">
                        <Code className="h-6 w-6 text-[#c9370a]" />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Core Automation Engine</h4>
                      <p className="text-neutral-800 text-xs leading-relaxed">
                        Sviluppo completo degli script di navigazione sicura per Instagram e Gmail, con simulazione delle impronte digitali ed orari variabili.
                      </p>
                    </div>
                  </Reveal>

                  <Reveal delay={0.2}>
                    <div className="card-silver-orange h-full">
                      <div className="w-12 h-12 rounded-xl bg-[#8a8594]/12 flex items-center justify-center mb-5">
                        <Database className="h-6 w-6 text-[#8a8594]" />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Proxy & Account Setup</h4>
                      <p className="text-neutral-800 text-xs leading-relaxed">
                        Integrazione e configurazione di proxy residenziali dedicati per blindare gli account ed eliminare qualsiasi rischio di ban di Meta.
                      </p>
                    </div>
                  </Reveal>

                  <Reveal delay={0.3}>
                    <div className="card-silver-orange h-full" style={{ background: 'linear-gradient(135deg, #ffffff 0%, #e8f5ee 25%, #d4ede2 45%, #a8dfc4 80%, #4ade80 100%)', borderColor: 'rgba(74,222,128,0.3)' }}>
                      <div className="w-12 h-12 rounded-xl bg-emerald-500/12 flex items-center justify-center mb-5">
                        <Settings className="h-6 w-6 text-emerald-600" />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Dashboard UI & CRM</h4>
                      <p className="text-neutral-800 text-xs leading-relaxed">
                        Compilazione dell&apos;applicazione web di gestione e notifica automatica dei lead qualificati verso Slack, email o il tuo CRM preferito.
                      </p>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 11: Servizio Content Factory */}
            <section className={`bg-paper section section-border-t relative${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="divider-gradient absolute top-0 inset-x-0"></div>
              <div className="max-w-4xl mx-auto px-6">
                <div className="grid md:grid-cols-2 gap-12 items-center">
                  <Reveal variant="left" className="card-silver-orange variant-orange shadow-md">
                    <h3 className="font-bold text-neutral-800 text-lg mb-6 border-b border-[#c9370a]/15 pb-3 flex items-center gap-2">
                      <Sparkles className="h-5 w-5 text-[#c9370a]" />
                      <span>Come funziona la fabbrica:</span>
                    </h3>

                    <ul className="space-y-6">
                      <li className="flex items-start gap-4">
                        <div className="step-num shrink-0">1</div>
                        <div>
                          <h4 className="font-bold text-neutral-800 text-sm">AI genera il copy delle slide</h4>
                          <p className="text-neutral-600 text-xs leading-relaxed">Il motore AI scrive il testo di ogni slide del carosello usando il framework CRO APSOC, calibrato sul tuo ICP e argomento.</p>
                        </div>
                      </li>

                      <li className="flex items-start gap-4">
                        <div className="step-num shrink-0">2</div>
                        <div>
                          <h4 className="font-bold text-neutral-800 text-sm">Il motore costruisce le grafiche automaticamente</h4>
                          <p className="text-neutral-600 text-xs leading-relaxed">Un browser reale si apre e genera automaticamente le slide visive del carosello, senza alcun intervento umano.</p>
                        </div>
                      </li>

                      <li className="flex items-start gap-4">
                        <div className="step-num shrink-0">3</div>
                        <div>
                          <h4 className="font-bold text-neutral-800 text-sm">Upload automatico su Google Drive</h4>
                          <p className="text-neutral-600 text-xs leading-relaxed">I caroselli finiti vengono caricati e organizzati per argomento su Google Drive. Pronti da scaricare o programmare per la pubblicazione.</p>
                        </div>
                      </li>
                    </ul>
                  </Reveal>

                  <Reveal variant="right">
                    <div className="bubble-orange mb-4">
                      <Sparkles className="h-4 w-4" />
                      <span>Service #02 · Content Factory</span>
                    </div>
                    <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black mb-6">
                      Fabbrica di Contenuti
                      <br />
                      <span className="text-orange-pure italic font-semibold">social su pilota automatico.</span>
                    </h2>
                    <p className="text-neutral-600 text-sm leading-relaxed mb-4">
                      Creare un carosello professionale a mano richiede ore: copy per ogni slide, design, caption, hashtag. Moltiplicalo per 4 post a settimana. Risultato: non pubblichi mai abbastanza, il profilo dorme e la concorrenza cresce.
                    </p>
                    <p className="text-neutral-600 text-sm leading-relaxed mb-4">
                      Questo workflow fa tutto in automatico: l&apos;AI genera il copy CRO-ottimizzato per ogni slide, poi il motore di automazione costruisce le grafiche visive senza che tu tocchi nulla. Stessa logica per gli script video.
                    </p>
                    <p className="text-neutral-600 text-sm leading-relaxed">
                      Output finale: caroselli visivi pronti, script video, caption con hashtag e upload organizzato su Google Drive. Puoi programmare la pubblicazione o scaricare e postare in 30 secondi.
                    </p>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 12: Content Factory Dashboard (MOCKUP INTERATTIVO) */}
            <section className={`bg-grey section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-10 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Settings className="h-4 w-4" />
                    <span>Interactive UI Demo</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    La tua fabbrica di contenuti.
                    <br />
                    <span className="text-orange-pure italic font-semibold">Clicca un formato per vedere l&apos;output:</span>
                  </h2>
                </div>

                {/* Mockup Interattivo di Content Generation */}
                <div className="relative max-w-4xl mx-auto">

                <Reveal delay={0.2} className="w-full bg-[#131313] border border-white/10 rounded-2xl overflow-hidden shadow-2xl shadow-black/60 ring-1 ring-white/[0.08] flex flex-col md:flex-row h-auto md:h-[480px]">

                  
                  {/* Left Column: Form di Briefing */}
                  <div className="w-full md:w-1/3 bg-[#1c1c1c] border-r border-white/5 p-6 flex flex-col justify-between">
                    <div>
                      <h4 className="text-xs font-mono text-white/40 uppercase tracking-widest mb-6">Configura Contenuto</h4>

                      <div className="space-y-4">
                        <div>
                          <label className="block text-[10px] text-white/50 uppercase mb-1">Argomento</label>
                          <input type="text" disabled value="Outreach Automatico" className="w-full bg-[#0a0a0a] border border-white/10 rounded px-2.5 py-1.5 text-xs text-white" />
                        </div>
                        <div>
                          <label className="block text-[10px] text-white/50 uppercase mb-1">Formato Output</label>
                          <input type="text" disabled value="Carosello 3 slide + Caption" className="w-full bg-[#0a0a0a] border border-white/10 rounded px-2.5 py-1.5 text-xs text-white" />
                        </div>
                        <div>
                          <label className="block text-[10px] text-white/50 uppercase mb-1">Target ICP</label>
                          <input type="text" disabled value="Coach e Imprenditori" className="w-full bg-[#0a0a0a] border border-white/10 rounded px-2.5 py-1.5 text-xs text-white" />
                        </div>
                      </div>
                    </div>

                    {/* Seleziona il formato del contenuto */}
                    <div className="mt-8 border-t border-white/5 pt-4 space-y-2">
                      <label className="block text-[10px] text-white/50 uppercase mb-2">Tipo di Contenuto</label>
                      <button
                        onClick={() => setCopyAngle("problema")}
                        className={`w-full text-left text-xs px-3 py-2 rounded transition flex items-center justify-between cursor-pointer ${copyAngle === "problema" ? "bg-orange-pure text-white font-bold" : "bg-[#0a0a0a] text-white/60 hover:text-white"}`}
                      >
                        <span>1. Carosello Instagram</span>
                        <ChevronRight className="h-3 w-3" />
                      </button>
                      <button
                        onClick={() => setCopyAngle("scarsita")}
                        className={`w-full text-left text-xs px-3 py-2 rounded transition flex items-center justify-between cursor-pointer ${copyAngle === "scarsita" ? "bg-orange-pure text-white font-bold" : "bg-[#0a0a0a] text-white/60 hover:text-white"}`}
                      >
                        <span>2. Script Video (Reels)</span>
                        <ChevronRight className="h-3 w-3" />
                      </button>
                      <button
                        onClick={() => setCopyAngle("valore")}
                        className={`w-full text-left text-xs px-3 py-2 rounded transition flex items-center justify-between cursor-pointer ${copyAngle === "valore" ? "bg-orange-pure text-white font-bold" : "bg-[#0a0a0a] text-white/60 hover:text-white"}`}
                      >
                        <span>3. Caption + Hashtag</span>
                        <ChevronRight className="h-3 w-3" />
                      </button>
                    </div>
                  </div>

                  {/* Right Column: Anteprima Testo Generato */}
                  <div className="w-full md:w-2/3 p-6 flex flex-col justify-between bg-[#0a0a0a]">
                    <div className="flex-1">
                      <div className="flex justify-between items-center border-b border-white/5 pb-3 mb-4">
                        <h4 className="text-sm font-bold text-white flex items-center gap-1.5">
                          <Zap className="h-4 w-4 text-orange-pure" />
                          {copyVariants[copyAngle].title}
                        </h4>
                        <span className="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">GENERATO ✦</span>
                      </div>
                      
                      {/* Il testo che cambia */}
                      <p className="text-white/80 text-sm leading-relaxed whitespace-pre-line bg-[#131313] p-4 rounded-xl border border-white/5">
                        {copyVariants[copyAngle].text}
                      </p>
                    </div>

                    {/* Annotazioni di copy */}
                    <div className="border-t border-white/5 pt-4 mt-4">
                      <h5 className="text-[10px] font-mono text-orange-pure uppercase tracking-wider mb-1 flex items-center gap-1">
                        <Sparkles className="h-3.5 w-3.5" /> Note Strategiche del Copywriter AI:
                      </h5>
                      <p className="text-white/50 text-[11px] leading-relaxed">
                        {copyVariants[copyAngle].annotation}
                      </p>
                    </div>

                  </div>
                </Reveal>
                </div>
              </div>
            </section>

            {/* Section 13: Kit di Content Deliverables */}
            <section className={`bg-paper section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="flex flex-col items-center text-center mb-16">
                  <div className="bubble-orange mb-4">
                    <Layers className="h-4 w-4" />
                    <span>Output del Sistema</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    Cosa produce la tua
                    <br />
                    <span className="text-orange-pure italic font-semibold">fabbrica di contenuti.</span>
                  </h2>
                </div>

                <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-6">
                  {[
                    { num: "01", title: "Caroselli Instagram", body: "L'AI genera il copy CRO per ogni slide, poi il motore di automazione costruisce le grafiche visive complete. Pronto da pubblicare.", grad: "linear-gradient(145deg, #fff8f5 0%, #fff0e8 50%, #ffe4d4 100%)", border: "rgba(251,70,4,0.18)" },
                    { num: "02", title: "Script Video AI", body: "Script parola per parola per Reels, TikTok e YouTube: hook di 3 secondi, corpo strutturato e CTA che genera engagement.", grad: "linear-gradient(145deg, #f5f8ff 0%, #e8f0ff 50%, #d8e8ff 100%)", border: "rgba(99,102,241,0.18)" },
                    { num: "03", title: "Caption + Hashtag", body: "Descrizione del post ottimizzata con emoji, CTA DM e set di hashtag calibrati tra volume alto e nicchia per massimizzare il reach.", grad: "linear-gradient(145deg, #f8fff5 0%, #edfff0 50%, #d8f5e0 100%)", border: "rgba(52,211,153,0.18)" },
                    { num: "04", title: "Upload Google Drive", body: "I contenuti finiti vengono caricati automaticamente su Google Drive, organizzati per argomento e pronti da scaricare o condividere.", grad: "linear-gradient(145deg, #fff5f8 0%, #ffe8f0 50%, #ffd8e8 100%)", border: "rgba(239,68,68,0.15)" },
                    { num: "05", title: "Pubblicazione Programmata", body: "Puoi collegare il workflow a strumenti di scheduling per pubblicare automaticamente sui tuoi canali social senza toccare nulla.", grad: "linear-gradient(145deg, #fffff5 0%, #fffce8 50%, #fff8d4 100%)", border: "rgba(234,179,8,0.2)" },
                  ].map((d, i) => (
                    <Reveal key={i} delay={0.1 + i * 0.08}>
                      <div className="rounded-2xl p-6 h-full transition-all duration-500 hover:-translate-y-1" style={{ background: d.grad, border: `1px solid ${d.border}`, boxShadow: `0 20px 50px -20px rgba(0,0,0,0.12), 0 2px 0 rgba(255,255,255,0.8) inset` }}>
                        <span className="text-[10px] text-orange-pure font-mono font-bold tracking-widest">[ DELIVERABLE {d.num} ]</span>
                        <h4 className="font-bold text-neutral-800 text-base mt-2 mb-3">{d.title}</h4>
                        <p className="text-neutral-600 text-xs leading-relaxed">{d.body}</p>
                      </div>
                    </Reveal>
                  ))}

                  <Reveal delay={0.55}>
                    <div className="rounded-2xl p-6 h-full transition-all duration-500 hover:-translate-y-1" style={{ background: 'linear-gradient(145deg, #f5f5ff 0%, #ece8ff 50%, #e0d8ff 100%)', border: '1px solid rgba(139,92,246,0.18)', boxShadow: '0 20px 50px -20px rgba(0,0,0,0.12), 0 2px 0 rgba(255,255,255,0.8) inset' }}>
                      <span className="text-[10px] text-orange-pure font-mono font-bold tracking-widest">[ DELIVERABLE 06 ]</span>
                      <h4 className="font-bold text-neutral-800 text-base mt-2 mb-3">Batch Produzione Multipla</h4>
                      <p className="text-neutral-600 text-xs leading-relaxed">
                        Il sistema può girare in batch e generare 5, 10 o 20 caroselli in una sola sessione. Settimane di contenuti in pochi minuti.
                      </p>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 14: Second Brain — Servizio */}
            <section className={`bg-ink section section-border-t relative${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="divider-gradient absolute top-0 inset-x-0"></div>
              <div className="absolute inset-0 pointer-events-none z-0" style={{ background: 'radial-gradient(ellipse 700px 400px at 20% 50%, rgba(42,90,180,0.08) 0%, transparent 70%), radial-gradient(ellipse 500px 350px at 90% 30%, rgba(251,70,4,0.05) 0%, transparent 60%)' }}></div>
              <div className="max-w-4xl mx-auto px-6 relative z-10">
                <div className="grid md:grid-cols-2 gap-12 items-center">
                  <Reveal variant="left">
                    <div className="bubble-ink mb-4">
                      <Database className="h-4 w-4 text-orange-pure" />
                      <span>Service #03 · Memoria AI</span>
                    </div>
                    <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-white mb-6">
                      Second Brain:
                      <br />
                      <span className="text-orange-pure italic font-semibold">l&apos;AI non dimentica più.</span>
                    </h2>
                    <p className="text-white/60 text-sm leading-relaxed mb-4">
                      Ogni tool AI che usi ha un problema fondamentale: dimentica tutto. Ogni sessione reimposta. Brand voice, ICP, decisioni strategiche, clienti — tutto evaporato. Mesi di lavoro che non entrano mai nell&apos;intelligenza artificiale che usi ogni giorno.
                    </p>
                    <p className="text-white/60 text-sm leading-relaxed mb-6">
                      Prima c&apos;era il RAG: ricerca vettoriale su documenti, potente ma meccanico, ogni contenuto era un&apos;isola senza connessioni narrative. <strong className="text-white/80">Poi è arrivato il Second Brain</strong>: una knowledge base interconnessa, visualizzabile come grafo di relazioni. Andrej Karpathy — ricercatore AI e co-fondatore di OpenAI — ha chiamato questo approccio <span className="text-orange-pure font-semibold">Context Engineering</span>: l&apos;arte di costruire il contesto giusto perché ogni conversazione con un LLM sia davvero calibrata sulla tua realtà.
                    </p>
                    <div className="space-y-4 text-xs text-white/70">
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong className="text-white/90">Memoria Permanente</strong> — ogni insight, cliente e processo accessibile all&apos;AI per sempre.</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong className="text-white/90">Grafo di Connessioni</strong> — ogni nodo linkato ad altri. Vedi le relazioni tra clienti, progetti e strategie.</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Check className="h-4 w-4 text-orange-pure shrink-0" />
                        <span><strong className="text-white/90">Zero Briefing Ripetuti</strong> — l&apos;AI conosce già il brand, l&apos;ICP, il tono di voce. Niente da rispiegare.</span>
                      </div>
                    </div>
                  </Reveal>

                  <Reveal variant="right">
                    <div className="h-full rounded-2xl p-6 flex flex-col" style={{ background: 'linear-gradient(145deg, #0d1526 0%, #0a1020 50%, #060c18 100%)', border: '1px solid rgba(74,109,192,0.25)', boxShadow: '0 4px 24px -6px rgba(0,0,0,0.4), 0 0 0 1px rgba(74,109,192,0.1)' }}>
                      <h3 className="font-bold text-white text-lg mb-6 border-b border-white/10 pb-3 flex items-center gap-2">
                        <Database className="h-5 w-5" style={{ color: '#4a6dc0' }} />
                        <span>Come funziona il workflow:</span>
                      </h3>
                      <div className="space-y-6 relative pl-6 before:absolute before:left-2 before:top-2 before:bottom-2 before:w-0.5 before:bg-blue-500/20">
                        <div className="relative">
                          <div className="absolute -left-6 top-0 w-4 h-4 rounded-full border-4" style={{ background: '#2a5090', borderColor: '#0d1526' }}></div>
                          <h4 className="font-bold text-white text-sm">Step 1: Cattura della Conoscenza</h4>
                          <p className="text-white/45 text-xs leading-relaxed mt-1">Ogni decisione, cliente, insight e processo viene strutturato in nodi collegati — costruendo la mappa semantica del business.</p>
                        </div>
                        <div className="relative">
                          <div className="absolute -left-6 top-0 w-4 h-4 rounded-full border-4" style={{ background: '#2a5090', borderColor: '#0d1526' }}></div>
                          <h4 className="font-bold text-white text-sm">Step 2: Costruzione del Grafo</h4>
                          <p className="text-white/45 text-xs leading-relaxed mt-1">I nodi si linkano tra loro — ogni cliente connesso ai suoi progetti, ogni progetto al suo contesto storico. Una rete navigabile visivamente.</p>
                        </div>
                        <div className="relative">
                          <div className="absolute -left-6 top-0 w-4 h-4 rounded-full border-4" style={{ background: '#2a5090', borderColor: '#0d1526' }}></div>
                          <h4 className="font-bold text-white text-sm">Step 3: Iniezione del Contesto</h4>
                          <p className="text-white/45 text-xs leading-relaxed mt-1">Ogni volta che lavori con un LLM, il Second Brain inietta il contesto rilevante automaticamente. L&apos;AI risponde come se conoscesse il business da anni.</p>
                        </div>
                        <div className="relative">
                          <div className="absolute -left-6 top-0 w-4 h-4 rounded-full border-4" style={{ background: '#2a5090', borderColor: '#0d1526' }}></div>
                          <h4 className="font-bold text-white text-sm">Step 4: Crescita Continua</h4>
                          <p className="text-white/45 text-xs leading-relaxed mt-1">Ogni sessione arricchisce la knowledge base. Il Second Brain diventa più preciso nel tempo — un asset che cresce con il business.</p>
                        </div>
                      </div>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 15: Second Brain Kit */}
            <section className={`bg-grey section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="text-center mb-12 flex flex-col items-center">
                  <div className="bubble-orange mb-4">
                    <Shield className="h-4 w-4" />
                    <span>What&apos;s inside</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    Cosa include il tuo
                    <br />
                    <span className="text-orange-pure italic font-semibold">Second Brain.</span>
                  </h2>
                </div>
                <div className="grid md:grid-cols-3 gap-5 mt-12">
                  <Reveal delay={0.1}>
                    <div className="card-paper flex flex-col relative overflow-hidden h-full">
                      <div className="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style={{ background: 'rgba(42,80,144,0.1)' }}>
                        <Database className="h-6 w-6" style={{ color: '#2a5090' }} />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Knowledge Base a Grafo</h4>
                      <p className="text-neutral-600 text-xs leading-relaxed flex-1">
                        Costruzione della knowledge base strutturata come rete interconnessa. Ogni nodo collegato agli altri — clienti, progetti, concetti, brand voice — navigabile visivamente come un grafo di relazioni.
                      </p>
                      <div className="border-t border-neutral-100 pt-3 mt-4 text-xs font-bold flex items-center gap-1" style={{ color: '#2a5090' }}>
                        <Database className="h-3.5 w-3.5" /> Struttura &amp; Architettura
                      </div>
                    </div>
                  </Reveal>
                  <Reveal delay={0.2}>
                    <div className="card-paper flex flex-col relative overflow-hidden h-full">
                      <div className="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style={{ background: 'rgba(42,80,144,0.1)' }}>
                        <Settings className="h-6 w-6" style={{ color: '#2a5090' }} />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Integrazione LLM Avanzata</h4>
                      <p className="text-neutral-600 text-xs leading-relaxed flex-1">
                        Configurazione del context engineering: il Second Brain viene collegato ai tuoi strumenti AI. Ad ogni sessione, l&apos;LLM riceve automaticamente il contesto giusto — zero briefing manuali, zero ripetizioni.
                      </p>
                      <div className="border-t border-neutral-100 pt-3 mt-4 text-xs font-bold flex items-center gap-1" style={{ color: '#2a5090' }}>
                        <Code className="h-3.5 w-3.5" /> Context Engineering
                      </div>
                    </div>
                  </Reveal>
                  <Reveal delay={0.3}>
                    <div className="card-paper flex flex-col relative overflow-hidden h-full" style={{ background: 'linear-gradient(145deg, #f5f8ff 0%, #eaefff 50%, #dde6ff 100%)', borderColor: 'rgba(74,109,192,0.2)' }}>
                      <div className="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style={{ background: 'rgba(42,80,144,0.1)' }}>
                        <TrendingUp className="h-6 w-6" style={{ color: '#2a5090' }} />
                      </div>
                      <h4 className="font-bold text-neutral-800 text-base mb-3">Workflow di Aggiornamento</h4>
                      <p className="text-neutral-600 text-xs leading-relaxed flex-1">
                        Sistema per catturare e aggiornare la knowledge base in modo continuativo. Non è un file statico: è un organismo vivo che evolve con il business, sessione dopo sessione, arricchendosi di nuova conoscenza.
                      </p>
                      <div className="border-t border-blue-100 pt-3 mt-4 text-xs font-bold flex items-center gap-1" style={{ color: '#2a5090' }}>
                        <TrendingUp className="h-3.5 w-3.5" /> Asset Permanente
                      </div>
                    </div>
                  </Reveal>
                </div>
              </div>
            </section>

            {/* Section 16: Tabella Comparativa */}
            <section className={`bg-grey section section-border-t relative${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6">
                <div className="flex flex-col items-center text-center mb-12">
                  <div className="bubble-silver mb-4">
                    <TrendingUp className="h-4 w-4 text-orange-pure" />
                    <span>Head-to-head comparison</span>
                  </div>
                  <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                    Un confronto spietato
                    <br />
                    <span className="text-orange-pure italic font-semibold">con qualsiasi altra opzione.</span>
                  </h2>
                </div>

                <Reveal delay={0.2} className="overflow-x-auto mt-12 border border-black/[0.08] rounded-2xl bg-[#ebebeb] overflow-hidden shadow-sm">
                  <table className="comparison-table comparison-table--light">
                    <thead>
                      <tr>
                        <th>CARATTERISTICA</th>
                        <th>SOFTWARE SAAS DI TERZI</th>
                        <th>SVILUPPO INTERNO</th>
                        <th className="col-ours">✦ LE NOSTRE DASHBOARD</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Costi Fissi Mensili</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />€150-€400/mese per utente</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Stipendi Dev per mesi</td>
                        <td className="col-ours"><Check className="h-3.5 w-3.5 text-emerald-400 inline mr-1.5" />€0 (Solo API a consumo)</td>
                      </tr>
                      <tr>
                        <td>Rischio Blocchi / Ban</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Elevatissimo (IP e API tracciate)</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Medio (richiede test continui)</td>
                        <td className="col-ours"><Check className="h-3.5 w-3.5 text-emerald-400 inline mr-1.5" />Nullo (agisce come un umano reale)</td>
                      </tr>
                      <tr>
                        <td>Qualità del Copy</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Generico e piatto (stile bot)</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Dipende dai prompt del team</td>
                        <td className="col-ours"><Check className="h-3.5 w-3.5 text-emerald-400 inline mr-1.5" />Altissima (framework embedded)</td>
                      </tr>
                      <tr>
                        <td>Proprietà Codice</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Nessuna (sei ospite)</td>
                        <td>Totale (ma costi immensi)</td>
                        <td className="col-ours"><Check className="h-3.5 w-3.5 text-emerald-400 inline mr-1.5" />Tua al 100% (sul tuo server)</td>
                      </tr>
                      <tr>
                        <td>Pronto in</td>
                        <td>Subito (da configurare a mano)</td>
                        <td><X className="h-3.5 w-3.5 text-red-400/50 inline mr-1.5" />Mesi di sviluppo e correzione dei bug</td>
                        <td className="col-ours"><Check className="h-3.5 w-3.5 text-emerald-400 inline mr-1.5" />7-10 Giorni · Chiavi in mano</td>
                      </tr>
                    </tbody>
                  </table>
                </Reveal>
              </div>
            </section>

            {/* Section 15: Obiezioni C-P-B */}
            <section className={`bg-grey section section-border-t${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="max-w-4xl mx-auto px-6 w-full">

                {/* Header sempre visibile */}
                <div className={`text-center ${slideMode ? 'mb-3' : 'mb-8'} max-w-3xl mx-auto`}>
                  <span className="bubble-orange">
                    <HelpCircle className="h-4 w-4" />
                    Gestione Obiezioni · Protocollo C·P·B
                  </span>
                  <h2 className="text-2xl md:text-4xl font-bold tracking-tight text-silver-black mt-4 whitespace-nowrap">
                    Le 4 obiezioni che <span className="text-orange-pure italic font-semibold">demoliamo</span> con i dati.
                  </h2>
                  {!slideMode && (
                    <p className="mt-4 text-sm text-neutral-600 leading-relaxed font-light">
                      Non cerchiamo di convincerti con frasi di circostanza. Rispondiamo con la logica scientifica del Protocollo Claim, Proof, Benefit. Niente sales pitch: solo codice, dati e verità.
                    </p>
                  )}
                </div>

                {/* SLIDE MODE: obiezione singola con switcher + AnimatePresence */}
                {slideMode ? (
                  <div className="w-full">
                    {/* Tab switcher obiezioni */}
                    <div className="flex justify-center gap-2 mb-3 flex-wrap">
                      {OBJECTIONS_DATA.map((obj, oi) => (
                        <button
                          key={oi}
                          onClick={() => setActiveObjection(oi)}
                          className={`text-[10px] px-3 py-1.5 rounded-full font-bold uppercase tracking-widest transition cursor-pointer ${activeObjection === oi ? "bg-orange-pure text-white" : "bg-black/10 text-neutral-600 hover:bg-black/15"}`}
                        >
                          #{String(oi + 1).padStart(2, '0')}
                        </button>
                      ))}
                    </div>

                    <AnimatePresence mode="wait">
                      <motion.div
                        key={activeObjection}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -20 }}
                        transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                      >
                        {(() => {
                          const obj = OBJECTIONS_DATA[activeObjection];
                          const HeadIcon = obj.cards[0].icon;
                          return (
                            <>
                              <div className="text-center mb-4" style={{ padding: '0.25rem 0 0.5rem' }}>
                                <div className="flex items-center justify-center gap-2 mb-2">
                                  <HeadIcon className="h-4 w-4 text-orange-pure" />
                                  <span className="text-[10px] uppercase tracking-wider font-mono text-orange-pure font-bold">{obj.eyebrow}</span>
                                </div>
                                <h3 className="text-xl md:text-2xl font-extrabold text-neutral-800">
                                  {obj.title} <span className="text-orange-pure italic font-medium">{obj.italic}</span>
                                </h3>
                                <p className="text-neutral-500 text-xs mt-1 uppercase tracking-wide font-semibold">→ {obj.kicker}</p>
                              </div>
                              <div className="grid md:grid-cols-3 gap-5">
                                {obj.cards.map((c, ci) => {
                                  const CardIcon = c.icon;
                                  return (
                                    <div key={ci} className={`relative overflow-hidden flex flex-col justify-between ${c.highlight ? "card-cpb-highlight" : "card-cpb"}`}>
                                      <div className="relative z-[1]">
                                        <div className="flex items-center justify-between mb-4">
                                          <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 ${c.highlight ? "bg-orange-pure text-white" : "bg-neutral-200 text-neutral-800"}`}>
                                            <CardIcon className="h-5 w-5" />
                                          </div>
                                          <span className={`text-[9px] font-bold tracking-widest ${c.highlight ? "text-orange-pure" : "text-neutral-400"}`}>
                                            0{ci + 1} // {c.kind}
                                          </span>
                                        </div>
                                        <h4 className="font-bold text-neutral-800 text-sm mb-2">{c.title}</h4>
                                        <p className="text-neutral-600 text-xs leading-relaxed">{c.body}</p>
                                      </div>
                                    </div>
                                  );
                                })}
                              </div>
                            </>
                          );
                        })()}
                      </motion.div>
                    </AnimatePresence>
                  </div>
                ) : (
                  /* LANDING MODE: tutte le obiezioni in sequenza */
                  <div className="space-y-20 mt-6">
                    {OBJECTIONS_DATA.map((obj, oi) => {
                      const HeadIcon = obj.cards[0].icon;
                      return (
                        <div key={oi} className="border-b border-black/5 pb-12 last:border-b-0">
                          <Reveal>
                            <div className="objection-header text-center mb-10">
                              <span className="objection-watermark-quote">&ldquo;</span>
                              <div className="flex items-center justify-center gap-2 mb-3">
                                <HeadIcon className="h-4 w-4 text-orange-pure" />
                                <span className="text-[10px] uppercase tracking-wider font-mono text-orange-pure font-bold">{obj.eyebrow}</span>
                              </div>
                              <h3 className="text-2xl md:text-3xl font-extrabold text-neutral-800">
                                {obj.title} <span className="text-orange-pure italic font-medium">{obj.italic}</span>
                              </h3>
                              <p className="text-neutral-500 text-xs mt-2 uppercase tracking-wide font-semibold">→ {obj.kicker}</p>
                            </div>
                          </Reveal>
                          <div className="grid md:grid-cols-3 gap-6 mt-8">
                            {obj.cards.map((c, ci) => {
                              const CardIcon = c.icon;
                              return (
                                <Reveal key={ci} delay={0.1 + ci * 0.1} className="h-full">
                                  <div className={`relative overflow-hidden h-full flex flex-col justify-between ${c.highlight ? "card-cpb-highlight" : "card-cpb"}`}>
                                    <div className="relative z-[1]">
                                      <div className="flex items-center justify-between mb-4">
                                        <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 ${c.highlight ? "bg-orange-pure text-white" : "bg-neutral-200 text-neutral-800"}`}>
                                          <CardIcon className="h-5 w-5" />
                                        </div>
                                        <span className={`text-[9px] font-bold tracking-widest ${c.highlight ? "text-orange-pure" : "text-neutral-400"}`}>
                                          0{ci + 1} // {c.kind}
                                        </span>
                                      </div>
                                      <h4 className="font-bold text-neutral-800 text-sm mb-2">{c.title}</h4>
                                      <p className="text-neutral-600 text-xs leading-relaxed">{c.body}</p>
                                    </div>
                                  </div>
                                </Reveal>
                              );
                            })}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </section>

            {/* Section 16: L'Offerta Speciale Partner */}
            <section className={`bg-ink section section-border-t relative${slideMode ? ' slide-section-mode' : ''}`}>
              <div className="divider-gradient absolute top-0 inset-x-0"></div>
              <div className={`max-w-4xl mx-auto ${slideMode ? 'px-6 py-6 flex flex-col justify-center h-full' : 'px-6'}`}>
                <div className={`text-center flex flex-col items-center ${slideMode ? 'mb-4' : 'mb-16'}`}>
                  {!slideMode && (
                    <div className="bubble-orange mb-4">
                      <Layers className="h-4 w-4" />
                      <span>Configurazioni Disponibili</span>
                    </div>
                  )}
                  <h2 className={`font-bold tracking-tight text-silver-white ${slideMode ? 'text-2xl' : 'text-3xl md:text-5xl'}`}>
                    Scegli l&apos;infrastruttura
                    <span className="text-orange-pure italic font-semibold"> giusta per il tuo business.</span>
                  </h2>
                  {!slideMode && (
                    <p className="text-white/55 text-sm mt-5 max-w-xl leading-relaxed">
                      Setup completo in 7 giorni. Codice sorgente consegnato e installato sui tuoi server. Zero canoni mensili, zero dipendenze da terze parti.
                    </p>
                  )}
                </div>

                {!slideMode && <div className="divider-gradient--subtle w-full h-px mb-12"></div>}

                <div className={`grid md:grid-cols-3 items-stretch ${slideMode ? 'gap-3' : 'gap-6 mt-4'}`}>
                  {/* Outreach Factory */}
                  <Reveal delay={0.1}>
                    <div className="card-tier flex flex-col justify-between h-full" style={slideMode ? { padding: '1rem 1.25rem', borderRadius: '16px' } : {}}>
                      <div>
                        <div className={`rounded-xl bg-orange-pure/10 flex items-center justify-center ${slideMode ? 'w-7 h-7 mb-2' : 'w-12 h-12 mb-5'}`}>
                          <Mail className={`text-orange-pure ${slideMode ? 'h-4 w-4' : 'h-6 w-6'}`} />
                        </div>
                        <div className="text-[9px] text-orange-pure/70 font-mono tracking-widest mb-0.5">[ ENGINE 01 ]</div>
                        <h3 className={`font-bold text-white ${slideMode ? 'text-sm mt-0.5 mb-1.5' : 'text-xl mt-2 mb-4'}`}>Outreach Platform</h3>
                        <p className={`text-white/55 leading-relaxed ${slideMode ? 'text-[10px] mb-2' : 'text-xs mb-6'}`}>
                          Automazione Gmail + Social Media, proxy residenziali, 3 sequenze copy su misura, dashboard inclusa.
                        </p>
                      </div>
                      <div className={`border-t border-white/5 ${slideMode ? 'pt-2' : 'pt-4'}`}>
                        <div className="text-[9px] text-orange-pure font-bold font-mono tracking-widest">INSTALLA L&apos;OUTREACH →</div>
                      </div>
                    </div>
                  </Reveal>

                  {/* Content Factory */}
                  <Reveal delay={0.2}>
                    <div className="card-tier flex flex-col justify-between h-full" style={slideMode ? { padding: '1rem 1.25rem', borderRadius: '16px' } : {}}>
                      <div>
                        <div className={`rounded-xl bg-orange-pure/10 flex items-center justify-center ${slideMode ? 'w-7 h-7 mb-2' : 'w-12 h-12 mb-5'}`}>
                          <Sparkles className={`text-orange-pure ${slideMode ? 'h-4 w-4' : 'h-6 w-6'}`} />
                        </div>
                        <div className="text-[9px] text-orange-pure/70 font-mono tracking-widest mb-0.5">[ ENGINE 02 ]</div>
                        <h3 className={`font-bold text-white ${slideMode ? 'text-sm mt-0.5 mb-1.5' : 'text-xl mt-2 mb-4'}`}>Content Factory</h3>
                        <p className={`text-white/55 leading-relaxed ${slideMode ? 'text-[10px] mb-2' : 'text-xs mb-6'}`}>
                          Motore copywriting con framework embedded, tono di voce del brand, 1 lancio pilota completo incluso.
                        </p>
                      </div>
                      <div className={`border-t border-white/5 ${slideMode ? 'pt-2' : 'pt-4'}`}>
                        <div className="text-[9px] text-orange-pure font-bold font-mono tracking-widest">INSTALLA LA CONTENT FACTORY →</div>
                      </div>
                    </div>
                  </Reveal>

                  {/* Second Brain */}
                  <Reveal delay={0.3}>
                    <div className="card-tier flex flex-col justify-between h-full" style={slideMode ? { padding: '1rem 1.25rem', borderRadius: '16px' } : {}}>
                      <div>
                        <div className={`rounded-xl bg-orange-pure/10 flex items-center justify-center ${slideMode ? 'w-7 h-7 mb-2' : 'w-12 h-12 mb-5'}`}>
                          <Database className={`text-orange-pure ${slideMode ? 'h-4 w-4' : 'h-6 w-6'}`} />
                        </div>
                        <div className="text-[9px] text-orange-pure/70 font-mono tracking-widest mb-0.5">[ ENGINE 03 ]</div>
                        <h3 className={`font-bold text-white ${slideMode ? 'text-sm mt-0.5 mb-1.5' : 'text-xl mt-2 mb-4'}`}>Second Brain</h3>
                        <p className={`text-white/55 leading-relaxed ${slideMode ? 'text-[10px] mb-2' : 'text-xs mb-6'}`}>
                          Knowledge base aziendale a grafo semantico. L&apos;AI conosce il tuo business — zero briefing ripetuti.
                        </p>
                      </div>
                      <div className={`border-t border-white/5 ${slideMode ? 'pt-2' : 'pt-4'}`}>
                        <div className="text-[9px] text-orange-pure font-bold font-mono tracking-widest">INSTALLA IL SECOND BRAIN →</div>
                      </div>
                    </div>
                  </Reveal>
                </div>

                {/* The Engine Room (FEATURED) — full-width bundle */}
                <Reveal delay={0.4} className={slideMode ? 'mt-3' : 'mt-6'}>
                  <div className="card-tier--featured flex flex-col md:flex-row md:items-center gap-4 relative" style={slideMode ? { padding: '1rem 1.5rem', borderRadius: '16px' } : {}}>
                    <div className="tier-badge">✦ ELITE BUNDLE ✦</div>
                    <div className={`rounded-xl bg-orange-pure/15 flex items-center justify-center flex-shrink-0 ${slideMode ? 'w-9 h-9' : 'w-14 h-14'}`}>
                      <Layers className={`text-orange-pure ${slideMode ? 'h-5 w-5' : 'h-7 w-7'}`} />
                    </div>
                    <div className="flex-1">
                      <div className="text-[9px] text-orange-pure font-mono font-bold tracking-widest mb-0.5">[ INTEGRAZIONE TOTALE ]</div>
                      <h3 className={`font-black text-neutral-800 ${slideMode ? 'text-base mb-1' : 'text-2xl mb-2'}`}>The Engine Room</h3>
                      <p className={`text-neutral-800 leading-relaxed font-medium ${slideMode ? 'text-[10px]' : 'text-xs'}`}>
                        Outreach, Content Factory e Second Brain in un&apos;unica Dashboard. I lead, i contenuti e la memoria del business lavorano in sinergia totale.
                      </p>
                    </div>
                    <div className="flex-shrink-0 flex flex-col gap-1">
                      {!slideMode && <div className="text-xs text-neutral-600 font-medium">Sessione strategica di mappatura funnel + 60 giorni di supporto prioritario dedicato.</div>}
                      <div className="text-[9px] text-orange-pure font-bold font-mono tracking-widest">SISTEMA COMPLETO →</div>
                    </div>
                  </div>
                </Reveal>

                {!slideMode && <div className="divider-gradient--subtle w-full h-px mt-12"></div>}
              </div>
            </section>

            {/* Section 17: Chiusura / Call To Action */}
            <section id="prenota" className={`bg-ink-2 section section-border-t relative overflow-hidden min-h-[80vh] flex flex-col justify-center${slideMode ? ' slide-section-mode' : ''}`}>
              {/* Ambient glow bottom center — inline gradients */}
              <div className="absolute inset-0 pointer-events-none z-0" style={{ background: 'radial-gradient(ellipse 800px 500px at 50% calc(100% + 128px), rgba(251,70,4,0.14) 0%, transparent 70%), radial-gradient(ellipse 400px 300px at 95% 0%, rgba(217,212,225,0.06) 0%, transparent 70%)' }}></div>


              <div className="max-w-4xl mx-auto px-6 text-center relative z-10">
                <Reveal delay={0.05}>
                  <div className="pre-headline mb-4">Prossimo Passo · Nessun Impegno</div>
                </Reveal>

                <Reveal delay={0.1}>
                  <div className="bubble-orange mb-6">
                    <Clock className="h-4 w-4" />
                    <span>Risposta in 24 Ore · Zero Rischio</span>
                  </div>
                </Reveal>

                <Reveal delay={0.2}>
                  <h2 className="font-black tracking-tight mb-8" style={{ fontSize: 'clamp(36px, 5.5vw, 72px)', lineHeight: 1.1 }}>
                    <span className="text-silver-white">Prenota 30 minuti.</span>
                    <br />
                    <span className="text-silver-orange italic">Ti mostro il sistema in azione.</span>
                  </h2>
                </Reveal>

                <Reveal delay={0.3}>
                  <p className="text-lg text-white/70 max-w-2xl mx-auto mb-10 leading-relaxed">
                    Facciamo una chiamata strategica di 30 minuti. Ti mostrerò le mie piattaforme reali mentre lavorano. Se c'è un fit, colleghiamo i motori alla tua azienda in meno di 48 ore. Se non c'è, ti lascerò comunque con una chiara roadmap di automazione.
                  </p>
                </Reveal>

                <Reveal delay={0.4}>
                  <div className="flex flex-col sm:flex-row justify-center items-center gap-4">
                    <a href={BOOKING_URL} className="btn-orange btn-orange--lg group cursor-pointer">
                      Prenota la tua chiamata strategica
                      <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-0.5" />
                    </a>
                  </div>
                  <p className="text-xs text-white/40 mt-4">
                    Disponibilità limitata a sole 2 configurazioni questo mese per garantire la massima cura sartoriale del codice.
                  </p>

                  {/* Trust signals */}
                  <div className="flex flex-wrap justify-center gap-6 mt-8">
                    <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                      <Check className="h-3.5 w-3.5 text-emerald-500" /> Risposta entro 24h
                    </span>
                    <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                      <Shield className="h-3.5 w-3.5 text-orange-pure" /> Nessun impegno
                    </span>
                    <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                      <Layers className="h-3.5 w-3.5 text-orange-pure" /> Roadmap inclusa anche se non acquisti
                    </span>
                  </div>
                </Reveal>
              </div>
            </section>

        </main>

        {/* Footer Minimale (solo in landing mode) */}
        {!slideMode && (
          <footer className="bg-ink-2 py-12 border-t border-white/5 text-center text-xs text-white/30">
            <div className="max-w-4xl mx-auto px-6">
              <p className="mb-2">✦ DIGITAL EMPIRE © 2026 ✦</p>
              <p>Infrastrutture di Automazione ed Acquisizione. Tutti i diritti riservati.</p>
            </div>
          </footer>
        )}

      </div>

    </div>
  );
}

