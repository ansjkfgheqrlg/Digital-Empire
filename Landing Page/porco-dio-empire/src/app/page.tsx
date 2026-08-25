"use client";

import { ArrowRight, Check, X, Sparkles, Zap, Clock, Shield, ChevronDown, BookOpen, Cpu, BarChart, Layers, FileText, Users, Crosshair, Braces, ArrowDown } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { StickyCTA } from "@/components/sticky-cta";
import { useState, FormEvent, useRef } from "react";

const API_KEY = "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";
const LIST_ID = 3;

function BrevoForm({ product, redirect }: { product: string; redirect: string }) {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState("");
  const [statusType, setStatusType] = useState<"error" | "loading" | "">("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    if (!nome.trim()) {
      setStatus("inserisci il tuo nome.");
      setStatusType("error");
      return;
    }

    if (!email.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setStatus("inserisci un indirizzo email valido.");
      setStatusType("error");
      return;
    }

    setLoading(true);
    setStatusType("loading");

    try {
      const response = await fetch("https://api.brevo.com/v3/contacts", {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
          "api-key": API_KEY
        },
        body: JSON.stringify({
          email: email,
          attributes: { FIRSTNAME: nome, SELECTED_GUIDE: product },
          listIds: [LIST_ID],
          updateEnabled: true
        })
      });

      if (response.ok || response.status === 204) {
        window.location.href = redirect;
      } else {
        setStatus("errore. riprova.");
        setStatusType("error");
        setLoading(false);
      }
    } catch (error) {
      setStatus("errore di connessione. riprova.");
      setStatusType("error");
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <div className="flex flex-col">
        <input 
          type="text" 
          value={nome}
          onChange={(e) => { setNome(e.target.value); setStatus(""); }}
          placeholder="il tuo nome" 
          required 
          disabled={loading}
          className="w-full px-5 py-4 bg-black/[0.03] border border-black/10 rounded-xl text-[#2a2a2a] placeholder:text-[#6a6a6a] outline-none focus:border-orange-pure focus:bg-white/50 transition-all font-medium text-[15px]" 
        />
      </div>
      <div className="flex flex-col mb-1">
        <input 
          type="email" 
          value={email}
          onChange={(e) => { setEmail(e.target.value); setStatus(""); }}
          placeholder="la tua email migliore" 
          required 
          disabled={loading}
          className="w-full px-5 py-4 bg-black/[0.03] border border-black/10 rounded-xl text-[#2a2a2a] placeholder:text-[#6a6a6a] outline-none focus:border-orange-pure focus:bg-white/50 transition-all font-medium text-[15px]" 
        />
      </div>
      <div className="flex flex-col">
        <button type="submit" disabled={loading} className="w-full py-4 rounded-xl font-bold text-white tracking-wide text-base bg-gradient-to-r from-[#ff5a2e] to-[#cc3700] hover:to-[#ff5a2e] shadow-[0_15px_30px_-5px_rgba(251,70,4,0.4)] transition-all hover:scale-[1.02] flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed">
          <span>{loading ? "INVIO..." : (product.includes("I.C.R.O.") ? "scarica il framework avanzato" : product.includes("Cowork") ? "ottieni il metodo intermedio" : "scarica la guida base")}</span> 
          {!loading && <ArrowRight className="w-4 h-4" />}
        </button>
      </div>
      <p className="text-center text-[13px] text-[#6a6a6a] font-medium mb-4">niente spam. cancellati quando vuoi.</p>
      
      {product.includes("I.C.R.O.") && (
        <a href="https://formazione-systemarchitect.netlify.app/" target="_blank" className="w-full flex items-center justify-between px-6 py-4 rounded-xl bg-black/[0.04] border border-black/10 hover:bg-black/[0.06] hover:border-black/20 transition-all group mt-2">
          <div className="flex flex-col">
              <span className="text-[#2a2a2a] font-bold text-base">Vai al corso completo</span>
              <span className="text-[#5a5a5a] text-[10px] font-bold uppercase tracking-widest mt-0.5">SYSTEM ARCHITECT · ACCEDI ORA</span>
          </div>
          <ArrowRight className="w-5 h-5 text-[#5a5a5a] group-hover:text-black transition-colors" />
        </a>
      )}

      {status && (
        <div className={`mt-1 text-center font-bold text-sm min-h-[20px] ${statusType === "error" ? "text-red-500" : "text-green-700"}`}>
          {status}
        </div>
      )}
    </form>
  );
}

export default function Page() {
  const [selectedProduct, setSelectedProduct] = useState<"base" | "intermedio" | "avanzato" | null>(null);
  
  const formBaseRef = useRef<HTMLElement>(null);
  const formIntermedioRef = useRef<HTMLElement>(null);
  const formAvanzatoRef = useRef<HTMLElement>(null);
  const detailRef = useRef<HTMLDivElement>(null);

  const toggleProductDetails = (product: "base" | "intermedio" | "avanzato") => {
    setSelectedProduct(product);
    setTimeout(() => {
      detailRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
    }, 50);
  };

  const openForm = (selectionStr: string) => {
    let targetRef;
    if (selectionStr.includes('Claude') || selectionStr.includes('Cowork') || selectionStr.includes('Intermedio')) {
      targetRef = formIntermedioRef;
    } else if (selectionStr.includes('ICRO') || selectionStr.includes('Avanzato') || selectionStr.includes('Framework')) {
      targetRef = formAvanzatoRef;
    } else {
      targetRef = formBaseRef;
    }

    targetRef?.current?.scrollIntoView({ behavior: "smooth", block: "start" });
    
    setTimeout(() => {
      const input = targetRef?.current?.querySelector('input[name="fname"]') as HTMLInputElement;
      if (input) input.focus();
    }, 1000);
  };

  return (
    <main className="relative">
      <StickyCTA href="#percorsi" label="Scegli un Percorso" secondaryHref="https://formazione-systemarchitect.netlify.app/" secondaryLabel="Corso Completo" />

      {/* ===================== HERO (bg-ink) ===================== */}
      <section className="bg-ink relative overflow-hidden">
        <div className="border-b border-white/10 overflow-hidden py-3 relative shadow-[0_10px_40px_-10px_rgba(251,70,4,0.15)]" style={{ background: "linear-gradient(90deg, #1c1c1c 0%, rgba(217,212,225,0.06) 25%, rgba(251,70,4,0.12) 50%, rgba(217,212,225,0.06) 75%, #1c1c1c 100%)" }}>
          <div className="marquee flex gap-10 whitespace-nowrap text-[13px] uppercase tracking-[0.2em] text-[#e8e3ef] font-semibold" style={{ width: "max-content" }}>
            {Array.from({ length: 3 }).map((_, i) => (
              <span key={i} className="flex items-center gap-10">
                <span>Intelligenza Artificiale</span><span className="text-orange-pure drop-shadow-[0_0_8px_rgba(251,70,4,0.8)]">✦</span>
                <span>Claude Code Mastery</span><span className="text-orange-pure drop-shadow-[0_0_8px_rgba(251,70,4,0.8)]">✦</span>
                <span>Prompt Engineering</span><span className="text-orange-pure drop-shadow-[0_0_8px_rgba(251,70,4,0.8)]">✦</span>
                <span>Digital Empire</span><span className="text-orange-pure drop-shadow-[0_0_8px_rgba(251,70,4,0.8)]">✦</span>
              </span>
            ))}
          </div>
        </div>

        <div className="max-w-5xl mx-auto px-6 py-24 md:py-36 text-center relative">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Sparkles className="h-3.5 w-3.5" /> Aggiornato per il 2026
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <div className="pre-headline mt-4 mb-5">I 3 PERCORSI FORMATIVI PREMIUM</div>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-[42px] md:text-[64px] font-bold leading-[1.05] tracking-tight mb-7">
              <span className="text-silver-white">Diventa un System Architect.</span>
              <br />
              <span className="text-silver-orange">Evolvi il tuo team AI con 3 percorsi misurabili.</span>
            </h1>
          </Reveal>

          <Reveal delay={0.15}>
            <p className="text-[17px] md:text-xl text-white/70 max-w-2xl mx-auto mb-6 leading-[1.75] font-light">
              <strong>Passa dal prompting casuale ai sistemi aziendali.</strong> Scegli il tuo livello tra le <strong className="text-white font-medium">3 guide operative disponibili</strong> per <strong className="text-white font-medium">allineare i collaboratori</strong>, gestire <strong className="text-white font-medium">knowledge base senza codice</strong> o scalare con <strong className="text-silver-orange font-semibold">architetture deterministiche</strong>. <strong className="text-white">Cessa di essere un prompt engineer passivo.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.2}>
            <ul className="inline-flex flex-col gap-4 mb-10 text-left max-w-2xl mx-auto">
              {[
                { text: 'Accesso Immediato al <strong class="text-silver-orange font-semibold">Framework Avanzato I.C.R.O.</strong> (12 pag. e template).' },
                { text: 'Evoluzione a <strong class="text-silver-orange font-semibold">Claude Cowork</strong>: creazione di knowledge base potenti senza righe di codice.' },
                { text: 'Accesso Bonus al <strong class="text-white font-semibold">Modulo Fondazioni</strong> per allineare i membri junior su logiche stabili.' }
              ].map((item, i) => (
                <li key={i} className="flex gap-4 text-[15px] md:text-base text-white/80 font-light items-start">
                  <div className="w-5 h-5 rounded flex items-center justify-center shrink-0 border border-[#c9a07a]/40 bg-[#c9a07a]/10 mt-1">
                    <Check className="h-3.5 w-3.5 text-[#c9a07a]" />
                  </div>
                  <span dangerouslySetInnerHTML={{ __html: item.text }} className="leading-relaxed" />
                </li>
              ))}
            </ul>
          </Reveal>

          <Reveal delay={0.25}>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <a href="#percorsi" className="btn-orange text-lg px-8 py-4 w-full md:w-auto justify-center">
                Scegli il tuo Percorso <ArrowDown className="ml-2 w-5 h-5" />
              </a>
              <a href="https://formazione-systemarchitect.netlify.app/" target="_blank" className="text-lg px-8 py-4 w-full md:w-auto flex items-center justify-center gap-2 rounded-xl font-bold uppercase tracking-wider text-white bg-white/5 border border-white/20 hover:bg-white/10 hover:border-white/40 transition-all text-center shadow-[0_4px_14px_rgba(0,0,0,0.1)]">
                Scopri il Corso Completo
              </a>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== DIVISORE ===================== */}
      <div className="h-1 w-full bg-gradient-to-r from-ink via-orange-pure to-ink opacity-90"></div>

      {/* ===================== I 3 PERCORSI ===================== */}
      <section id="percorsi" className="bg-paper section section-border-t">
        <div className="max-w-6xl mx-auto px-6">
          <Reveal>
            <div className="text-center">
              <span className="bubble-ink mb-6">Scegli il tuo livello</span>
              <h2 className="text-[34px] md:text-[52px] font-bold leading-[1.1] mb-12 mt-6">
                <span className="text-silver-black">3 Guide Tecniche Operative.</span><br />
                <span className="text-orange-pure italic font-medium">Scegli dove posizionarti.</span>
              </h2>
            </div>
          </Reveal>
          
          <div className="grid lg:grid-cols-3 gap-6">

            {/* Livello BASE */}
            <Reveal delay={0}>
              <div className="card-paper flex flex-col justify-between border-t-8 border-t-silver-dim h-full">
                <div>
                  <div className="uppercase tracking-widest text-xs font-bold text-silver-dim mb-2">Livello Zero/Base</div>
                  <h3 className="text-2xl font-black text-black mb-4">Fondazioni AI &<br/>System Prompts</h3>
                </div>
                <div className="mt-4 flex flex-col gap-3">
                  <button onClick={() => toggleProductDetails('base')} className="btn-secondary border-silver-dim/20 w-full justify-center">Spiegazione Prodotto</button>
                </div>
              </div>
            </Reveal>

            {/* Livello INTERMEDIO */}
            <Reveal delay={0.1}>
              <div className="card-paper bg-[#fdfcfa] flex flex-col justify-between border-t-8 border-t-silver-dim relative h-full">
                <div>
                  <div className="flex flex-col mb-4">
                    <div className="flex justify-between items-center mb-2">
                       <div className="uppercase tracking-widest text-xs font-bold text-silver-dim">Livello Intermedio</div>
                    </div>
                    <h3 className="text-2xl font-black text-black leading-[1.1]">Mastering<br/>Claude Cowork</h3>
                  </div>
                </div>
                <div className="mt-4 flex flex-col gap-3">
                  <button onClick={() => toggleProductDetails('intermedio')} className="btn-secondary border-silver-dim/20 w-full justify-center">Spiegazione Prodotto</button>
                </div>
              </div>
            </Reveal>

            {/* Livello AVANZATO */}
            <Reveal delay={0.2}>
              <div className="card-dark-featured flex flex-col justify-between border-t-8 border-t-orange-pure text-white relative shadow-2xl h-full" style={{ zIndex: 10 }}>
                <div>
                   <div className="flex justify-between items-center mb-2">
                     <div className="uppercase tracking-widest text-xs font-bold text-silver-white">Livello Esperto/Tech</div>
                     <span className="text-[10px] bg-orange-pure text-white px-2 py-1 rounded font-bold uppercase tracking-wider hidden lg:inline-block shadow-[0_0_15px_rgba(251,70,4,0.4)]">PIÙ RICHIESTO</span>
                   </div>
                   <h3 className="text-3xl font-black mb-4 text-transparent bg-clip-text bg-gradient-to-br from-white to-silver">Il Framework<br/>I.C.R.O.</h3>
                </div>
                <div className="mt-4 flex flex-col gap-3">
                   <button onClick={() => toggleProductDetails('avanzato')} className="btn-orange w-full justify-center text-white border-none shadow-[0_0_20px_rgba(251,70,4,0.3)]">Spiegazione Prodotto</button>
                </div>
              </div>
            </Reveal>

          </div>

          {/* CONTENITORE DETTAGLI PRODOTTI SCORREVOLE */}
          <div ref={detailRef} className={`mt-16 w-full max-w-4xl mx-auto relative pb-4 transition-all duration-500 ${selectedProduct ? "block" : "hidden"}`}>
             
             {/* DETTAGLIO BASE */}
             {selectedProduct === "base" && (
               <div className="product-detail animate-[fadeIn_0.5s_ease-out]">
                 <div className="card-paper bg-white text-black !px-6 md:!px-12 !py-10 border-l-8 border-l-silver-dim shadow-xl">
                   <div className="uppercase tracking-widest text-sm font-bold text-silver-dim mb-3">Guida Base / PDF</div>
                   <h3 className="text-3xl md:text-4xl font-black mb-6">Fondazioni AI & System Prompts</h3>
                   <p className="text-[#3a3a3a] text-lg md:text-xl leading-relaxed mb-8 font-serif">
                     Non sai da dove iniziare? In questa guida di base esploriamo <strong>i migliori modelli</strong> attualmente sul mercato, impariamo i concetti base della logica del <strong>Prompt Engineering</strong> e come organizzare in maniera perfetta la comunicazione con l'AI.
                   </p>
                   <ul className="space-y-4 mb-10">
                     <li className="flex items-start gap-4">
                       <div className="w-8 h-8 rounded bg-gray-100 flex items-center justify-center shrink-0 my-1">
                         <BookOpen className="w-4 h-4 text-silver-dim" />
                       </div>
                       <span className="text-[#3a3a3a] font-medium leading-relaxed">Glossario modelli e scelta giusta in base al budget e al bisogno.</span>
                     </li>
                     <li className="flex items-start gap-4">
                       <div className="w-8 h-8 rounded bg-gray-100 flex items-center justify-center shrink-0 my-1">
                         <Cpu className="w-4 h-4 text-silver-dim" />
                       </div>
                       <span className="text-[#3a3a3a] font-medium leading-relaxed">Architettura base di un prompt funzionante senza allucinazioni.</span>
                     </li>
                     <li className="flex items-start gap-4">
                       <div className="w-8 h-8 rounded bg-gray-100 flex items-center justify-center shrink-0 my-1">
                         <BarChart className="w-4 h-4 text-silver-dim" />
                       </div>
                       <span className="text-[#3a3a3a] font-medium leading-relaxed">Come pre-allineare il modello usando i primi System Prompt.</span>
                     </li>
                   </ul>
                   <button onClick={() => openForm('Fondazioni AI')} className="btn-orange w-full md:w-auto px-10 text-lg shadow-lg">Scarica la Guida Base Zero</button>
                 </div>
               </div>
             )}

             {/* DETTAGLIO INTERMEDIO */}
             {selectedProduct === "intermedio" && (
               <div className="product-detail animate-[fadeIn_0.5s_ease-out]">
                 <div className="card-paper bg-[#fdfcfa] text-black !px-6 md:!px-12 !py-10 border-l-8 border-l-orange-pure shadow-xl">
                   <div className="flex items-center gap-4 mb-3">
                     <div className="uppercase tracking-widest text-sm font-bold text-orange-pure">Guida Intermedia / Metodo</div>
                   </div>
                   <h3 className="text-3xl md:text-5xl font-black mb-6">Mastering<br/>Claude Cowork</h3>
                   <p className="text-[#3a3a3a] text-lg md:text-xl leading-relaxed mb-8 font-serif">
                     Usi già l'AI per lavoro ma il risultato è disordinato. Questa guida sblocca il vero potenziale dei <strong>Workspace di Claude (Cowork)</strong>. Impara a gestire knowledge base aziendali caricate su progetti chiusi senza usare codice.
                   </p>
                   <ul className="space-y-4 mb-10 border-l-2 border-orange-100 pl-4 py-2">
                     <li className="flex items-start gap-4">
                       <div className="w-6 h-6 rounded bg-orange-100 flex items-center justify-center shrink-0 my-1">
                         <Layers className="w-3.5 h-3.5 text-orange-pure" />
                       </div>
                       <span className="text-[#2a2a2a] font-bold leading-relaxed">Setup ottimizzato e gestione progetti fluidi in Claude Cow Work.</span>
                     </li>
                     <li className="flex items-start gap-4">
                       <div className="w-6 h-6 rounded bg-orange-100 flex items-center justify-center shrink-0 my-1">
                         <FileText className="w-3.5 h-3.5 text-orange-pure" />
                       </div>
                       <span className="text-[#2a2a2a] font-bold leading-relaxed">Artefatti avanzati e puro Knowledge Injecting documentale.</span>
                     </li>
                     <li className="flex items-start gap-4">
                       <div className="w-6 h-6 rounded bg-orange-100 flex items-center justify-center shrink-0 my-1">
                         <Users className="w-3.5 h-3.5 text-orange-pure" />
                       </div>
                       <span className="text-[#2a2a2a] font-bold leading-relaxed">Condivisione asincrona dei System Prompt interni con il team operativo.</span>
                     </li>
                   </ul>
                   <button onClick={() => openForm('Claude Cowork')} className="btn-orange w-full md:w-auto px-10 py-4 text-lg shadow-xl hover:scale-[1.02]">Ottieni la Guida Claude Cowork</button>
                 </div>
               </div>
             )}

             {/* DETTAGLIO AVANZATO */}
             {selectedProduct === "avanzato" && (
               <div className="product-detail animate-[fadeIn_0.5s_ease-out]">
                 <div className="card-dark !px-6 md:!px-12 !py-10 text-white shadow-[0_40px_100px_-20px_rgba(0,0,0,0.9)] relative overflow-hidden">
                   {/* watermak text */}
                   <div className="absolute top-[-50px] right-[-20px] p-0 m-0 opacity-[0.03] pointer-events-none text-[250px] font-black italic tracking-tighter leading-none select-none">ICRO</div>
                   
                   <div className="relative z-10">
                     <div className="uppercase tracking-widest text-sm font-bold text-silver-white mb-3">Masterclass / Template</div>
                     <h3 className="text-3xl md:text-5xl font-black mb-6 text-transparent bg-clip-text bg-gradient-to-br from-white to-silver drop-shadow-sm">Il Framework I.C.R.O.</h3>
                     <p className="text-white/80 text-lg md:text-xl leading-relaxed mb-8 font-serif">
                       Il metodo esatto per architetti in 12 pagine grafiche e 4 fasi logico-sequenziali, per chi pretende risultati <strong>marcatamente prevedibili e deterministici</strong>. Abbandona il prompting creativo amatoriale e impara subito l'ingegnerizzazione degli output. Contiene il super template "CLAUDE.md".
                     </p>
                     <ul className="space-y-4 mb-10 p-5 bg-white/5 rounded-2xl border border-white/10">
                       <li className="flex items-start gap-4">
                         <div className="w-6 h-6 rounded bg-white/10 flex items-center justify-center shrink-0 my-1">
                           <Crosshair className="w-3.5 h-3.5 text-white" />
                         </div>
                         <span className="text-white/90 font-medium leading-relaxed"><strong className="text-white">4 Step Irrinunciabili:</strong> Identità, Contesto, Regole, Output.</span>
                       </li>
                       <li className="flex items-start gap-4">
                         <div className="w-6 h-6 rounded bg-white/10 flex items-center justify-center shrink-0 my-1">
                           <Braces className="w-3.5 h-3.5 text-white" />
                         </div>
                         <span className="text-white/90 font-medium leading-relaxed"><strong className="text-white">Template "CLAUDE.md":</strong> Il file markdown copiabile e iniettabile.</span>
                       </li>
                       <li className="flex items-start gap-4">
                         <div className="w-6 h-6 rounded mb-1 bg-white/10 flex items-center justify-center shrink-0 my-1">
                           <Cpu className="w-3.5 h-3.5 text-white" />
                         </div>
                         <span className="text-white/90 font-medium leading-relaxed"><strong className="text-white">Paradigma Tech-Lux:</strong> Da banali scambi in chat a Sistemi Agentici puri.</span>
                       </li>
                     </ul>
                     <button onClick={() => openForm('Framework ICRO')} className="btn-orange bg-white text-black hover:bg-gray-100 hover:text-black w-full md:w-auto px-10 py-5 text-xl font-bold shadow-[0_0_40px_rgba(255,255,255,0.2)] border-none ring-4 ring-white/20 ring-offset-4 ring-offset-ink">Scarica il Framework Supremo</button>
                   </div>
                 </div>
               </div>
             )}

          </div>
        </div>
      </section>

      {/* ===================== FORM BASE ===================== */}
      <section ref={formBaseRef} className={`product-form-section bg-ink-2 section section-border-t pb-16 ${selectedProduct === "base" ? "block" : "hidden"}`}>
        <div className="max-w-xl mx-auto px-6 text-center">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-4">
              <span className="text-silver-white">Ricevi la tua</span><br/>
              <span className="text-silver-orange mt-2 inline-block">Guida Base</span>
            </h2>
            <p className="text-white/60 text-lg mb-10 max-w-lg mx-auto">
              Compila il form per ricevere <strong className="text-white">Fondazioni AI & System Prompts</strong> e imparare i veri fondamenti del Prompt Engineering.
            </p>
          </Reveal>
          <Reveal delay={0.1}>
            <div className="stat-card-silver w-full max-w-xl left-0 mx-auto relative overflow-visible text-left z-10 !px-6 md:!px-10 !py-10">
              <h3 className="text-xs font-bold text-[#4a4a4a] mb-8 uppercase tracking-[0.2em] text-center">SCARICA IL PDF GRATUITO</h3>
              <BrevoForm product="Guida Base: Fondamenti e Prompting" redirect="thank-you-base.html" />
              <div className="mt-6 flex justify-center">
                <span className="text-[12px] font-medium text-[#4a4a4a] flex items-center gap-2">
                  <Shield className="h-4 w-4" /> i tuoi dati sono protetti
                </span>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== FORM INTERMEDIO ===================== */}
      <section ref={formIntermedioRef} className={`product-form-section bg-ink-2 section section-border-t pb-16 ${selectedProduct === "intermedio" ? "block" : "hidden"}`}>
        <div className="max-w-xl mx-auto px-6 text-center">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-4">
              <span className="text-silver-white">Sblocca il</span><br/>
              <span className="text-orange-pure mt-2 inline-block">Metodo Cowork</span>
            </h2>
            <p className="text-white/60 text-lg mb-10 max-w-lg mx-auto">
              Compila il form per accedere alla guida <strong className="text-white">Mastering Claude Cowork</strong> e iniziare a gestire knowledge base aziendali.
            </p>
          </Reveal>
          <Reveal delay={0.1}>
            <div className="stat-card-silver w-full max-w-xl right-0 mx-auto text-left relative overflow-visible z-10 !px-6 md:!px-10 !py-10">
              <h3 className="text-xs font-bold text-[#4a4a4a] mb-8 uppercase tracking-[0.2em] text-center">RICEVI IL METODO GRATIS</h3>
              <BrevoForm product="Guida Intermedia: Claude Cowork" redirect="thank-you-intermedio.html" />
              <div className="mt-6 flex justify-center">
                <span className="text-[12px] font-medium text-[#4a4a4a] flex items-center gap-2">
                  <Shield className="h-4 w-4" /> i tuoi dati sono protetti
                </span>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== FORM AVANZATO ===================== */}
      <section ref={formAvanzatoRef} className={`product-form-section bg-ink-2 section section-border-t pb-16 ${selectedProduct === "avanzato" ? "block" : "hidden"}`}>
        <div className="max-w-xl mx-auto px-6 text-center">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-4">
              <span className="text-silver-white">Scarica il</span><br/>
              <span className="text-white mt-2 inline-block relative after:content-[''] after:absolute after:-bottom-2 after:left-0 after:w-full after:h-2 after:bg-orange-pure after:-z-10">Framework Supremo</span>
            </h2>
            <p className="text-white/60 text-lg mb-10 max-w-lg mx-auto">
              Compila il form per ottenere il <strong className="text-white">Framework I.C.R.O.</strong> e imparare l'ingegnerizzazione degli output deterministici.
            </p>
          </Reveal>
          <Reveal delay={0.1}>
            <div className="absolute top-1/2 left-[-10px] md:left-[-60px] -translate-y-1/2 z-20 hidden md:flex items-center gap-2 bg-gradient-to-r from-[#e8e8e8] to-[#f4f1f7] border border-white/50 shadow-[0_10px_25px_-5px_rgba(0,0,0,0.2)] rounded-full px-4 py-2 font-semibold text-sm text-[#1c1c1c] tracking-tight">
              <div className="w-1.5 h-1.5 rounded-full bg-orange-pure animate-pulse"></div>
              <span className="text-orange-pure font-bold">10 sec</span> per compilare
            </div>
            <div className="stat-card-silver w-full max-w-xl mx-auto text-left relative overflow-visible z-10 !px-6 md:!px-10 !py-10">
              <h3 className="text-xs font-bold text-[#4a4a4a] mb-8 uppercase tracking-[0.2em] text-center">SCARICA IL FRAMEWORK</h3>
              <BrevoForm product="Guida Esperti: Il Framework I.C.R.O." redirect="thank-you-avanzato.html" />
              <div className="mt-6 flex justify-center">
                <span className="text-[12px] font-medium text-[#4a4a4a] flex items-center gap-2">
                  <Shield className="h-4 w-4" /> i tuoi dati sono protetti
                </span>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== FOOTER ===================== */}
      <footer className="bg-ink-2 py-12 md:pb-12 pb-24 text-center text-white/30 text-xs tracking-widest border-t border-white/5 uppercase font-medium">
         © 2026 Digital Empire Labs
      </footer>
    </main>
  );
}
