"use client";

import React, { useState, useEffect, useRef } from "react";
import { 
  Play, 
  Terminal, 
  Settings, 
  FolderOpen, 
  CheckCircle, 
  ExternalLink, 
  RefreshCw, 
  Eye, 
  ChevronRight, 
  ChevronLeft, 
  X, 
  Save, 
  Info, 
  Zap, 
  Sparkles,
  ShieldAlert,
  Sliders,
  LogOut,
  FolderClosed
} from "lucide-react";
import { Reveal } from "@/components/reveal";

export default function DashboardPage() {
  // Stati di Generazione
  const [topic, setTopic] = useState("");
  const [visibleMode, setVisibleMode] = useState(false);
  const [workflowStatus, setWorkflowStatus] = useState<any>({
    status: "idle",
    lastTopic: "",
    isRunning: false
  });
  const [logs, setLogs] = useState("In attesa di attività...");
  const [activeSetup, setActiveSetup] = useState<"arena" | "drive" | null>(null);

  // Stati dell'Esploratore File
  const [caroselli, setCaroselli] = useState<any[]>([]);
  const [selectedCarosello, setSelectedCarosello] = useState<any | null>(null);
  const [activeSlideIndex, setActiveSlideIndex] = useState(0);

  // Stati dell'Editor di Config
  const [selectedConfigFile, setSelectedConfigFile] = useState<"prompt" | "regole" | "config">("prompt");
  const [configContent, setConfigContent] = useState("");
  const [saveStatus, setSaveStatus] = useState<string | null>(null);

  // Polling ref per logs
  const terminalEndRef = useRef<HTMLDivElement>(null);
  const [isPollingLogs, setIsPollingLogs] = useState(true);

  // 1. Carica lo stato del workflow e i log iniziali
  const fetchWorkflowStatus = async () => {
    try {
      const res = await fetch("/api/run-workflow");
      const data = await res.json();
      setWorkflowStatus(data);
      
      // Se c'è un setup in corso, sincronizza lo stato locale
      if (data.status === "setup_arena") {
        setActiveSetup("arena");
      } else if (data.status === "setup_drive") {
        setActiveSetup("drive");
      } else {
        setActiveSetup(null);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const fetchLogs = async () => {
    try {
      const res = await fetch("/api/logs");
      const data = await res.json();
      if (data.logs) {
        setLogs(data.logs);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const fetchCaroselli = async () => {
    try {
      const res = await fetch("/api/caroselli");
      const data = await res.json();
      if (data.caroselli) {
        setCaroselli(data.caroselli);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const fetchConfigFile = async (fileKey: string) => {
    try {
      const res = await fetch(`/api/config?file=${fileKey}`);
      const data = await res.json();
      if (data.content !== undefined) {
        setConfigContent(data.content);
      }
    } catch (e) {
      console.error(e);
    }
  };

  // Caricamento iniziale e polling
  useEffect(() => {
    fetchWorkflowStatus();
    fetchLogs();
    fetchCaroselli();
    fetchConfigFile("prompt");
  }, []);

  // Polling dei log e dello stato ogni 1.5 secondi se c'è un processo attivo
  useEffect(() => {
    let interval: any;
    if (isPollingLogs || workflowStatus.isRunning || activeSetup) {
      interval = setInterval(() => {
        fetchWorkflowStatus();
        fetchLogs();
        fetchCaroselli();
      }, 1500);
    }
    return () => clearInterval(interval);
  }, [isPollingLogs, workflowStatus.isRunning, activeSetup]);

  // Scroll automatico del terminale
  useEffect(() => {
    if (terminalEndRef.current) {
      terminalEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [logs]);

  // 2. Azioni di Trigger
  const handleLaunchWorkflow = async () => {
    if (!topic || topic.trim() === "") {
      alert("Inserisci un argomento valido per il carosello!");
      return;
    }
    try {
      setLogs("Preparazione del processo in corso...\n");
      const res = await fetch("/api/run-workflow", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, visible: visibleMode })
      });
      const data = await res.json();
      if (data.success) {
        fetchWorkflowStatus();
      } else {
        alert(`Errore: ${data.error}`);
      }
    } catch (e: any) {
      alert(`Errore di rete: ${e.message}`);
    }
  };

  const handleStartSetup = async (target: "arena" | "drive") => {
    try {
      setActiveSetup(target);
      const res = await fetch("/api/setup-session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target })
      });
      const data = await res.json();
      if (data.success) {
        fetchWorkflowStatus();
      } else {
        alert(`Errore: ${data.error}`);
        setActiveSetup(null);
      }
    } catch (e: any) {
      alert(`Errore di rete: ${e.message}`);
      setActiveSetup(null);
    }
  };

  const handleCompleteSetup = async () => {
    try {
      const res = await fetch("/api/submit-stdin", { method: "POST" });
      const data = await res.json();
      if (data.success) {
        setActiveSetup(null);
        fetchWorkflowStatus();
      } else {
        alert(`Errore: ${data.error}`);
      }
    } catch (e: any) {
      alert(`Errore di rete: ${e.message}`);
    }
  };

  const handleClearLogs = async () => {
    try {
      await fetch("/api/logs", { method: "DELETE" });
      setLogs("Console ripulita.");
    } catch (e) {
      console.error(e);
    }
  };

  const handleSaveConfig = async () => {
    try {
      setSaveStatus("Salvataggio in corso...");
      const res = await fetch("/api/config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fileKey: selectedConfigFile, content: configContent })
      });
      const data = await res.json();
      if (data.success) {
        setSaveStatus("Salvato con successo!");
        setTimeout(() => setSaveStatus(null), 3000);
      } else {
        setSaveStatus(`Errore: ${data.error}`);
      }
    } catch (e: any) {
      setSaveStatus(`Errore di rete: ${e.message}`);
    }
  };

  return (
    <div className="flex-1 w-full max-w-7xl mx-auto px-4 md:px-8 py-10 z-10">
      
      {/* 4 Silver-chips Flottanti */}
      <div className="hidden lg:block">
        <div className="silver-chip float-a top-32 left-10">
          <div className="dot"></div>
          Status: <strong>ArenaAI</strong> {workflowStatus.status === "setup_arena" ? "Setup" : "Pronto"}
        </div>
        <div className="silver-chip float-b top-32 right-10">
          <div className="dot bg-orange-pure"></div>
          Node.js <strong>v24.11.1</strong>
        </div>
        <div className="silver-chip float-c bottom-40 left-10">
          <div className="dot"></div>
          Engine: <strong>Playwright</strong>
        </div>
        <div className="silver-chip float-d bottom-40 right-10">
          <div className="dot bg-orange-pure"></div>
          Status: <strong>GDrive</strong> {workflowStatus.status === "setup_drive" ? "Setup" : "Attivo"}
        </div>
      </div>

      {/* Hero Section */}
      <div className="text-center mb-16 relative">
        <Reveal variant="scale" delay={0.1}>
          <div className="inline-flex mb-4">
            <span className="bubble-orange gap-2">
              <Sparkles className="h-4 w-4" />
              Digital Empire Premium Platform
            </span>
          </div>
        </Reveal>
        
        <Reveal variant="up" delay={0.2}>
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight mb-4">
            <span className="text-silver-white">PRODUZIONE CAROSELLI</span>
            <br />
            <span className="text-silver-orange">AGENCY AUTOMATION</span>
          </h1>
        </Reveal>
        
        <Reveal variant="up" delay={0.3}>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            L'orchestratore intelligente che unisce il team dei <strong className="text-silver-orange font-semibold">Nemotron AI Agents</strong>, 
            l'automazione grafica di <strong className="text-silver-orange font-semibold">Arena AI</strong> e l'upload su Google Drive.
          </p>
        </Reveal>
      </div>

      {/* Sezione Stato Attivo Live */}
      {workflowStatus.status !== "idle" && (
        <Reveal variant="fade" delay={0.1}>
          <div className="mb-10 card-orange flex flex-col md:flex-row items-center justify-between gap-6 relative overflow-hidden border border-white/20">
            <div className="flex items-center gap-4">
              <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-white"></div>
              <div>
                <h3 className="font-bold text-lg text-white">
                  {workflowStatus.status === "running" && `Generazione attiva per: "${workflowStatus.lastTopic}"`}
                  {workflowStatus.status === "setup_arena" && "Configurazione manuale Sessione Arena AI"}
                  {workflowStatus.status === "setup_drive" && "Configurazione manuale Sessione Google Drive"}
                </h3>
                <p className="text-white/80 text-sm">
                  {workflowStatus.status === "running" && "Il Team Agenti sta scrivendo il copy o Playwright sta registrando le immagini delle slide..."}
                  {(workflowStatus.status === "setup_arena" || workflowStatus.status === "setup_drive") && 
                    "Il browser visibile è aperto sul tuo computer. Effettua l'accesso nella finestra, poi clicca il bottone qui a destra!"}
                </p>
              </div>
            </div>
            
            {(workflowStatus.status === "setup_arena" || workflowStatus.status === "setup_drive") && (
              <button 
                onClick={handleCompleteSetup}
                className="w-full md:w-auto px-6 py-3 rounded-lg bg-white text-ink font-bold hover:scale-[1.02] active:scale-[0.98] transition-transform duration-200 shadow-lg flex items-center justify-center gap-2 cursor-pointer"
              >
                <CheckCircle className="h-5 w-5 text-orange" />
                Completa & Salva Sessione
              </button>
            )}
          </div>
        </Reveal>
      )}

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16">
        
        {/* Colonne di Sinistra - Controlli */}
        <div className="lg:col-span-5 flex flex-col gap-8">
          
          {/* Card 1: Avvio Workflow */}
          <Reveal variant="left" delay={0.2} className="h-full">
            <div className="card-dark h-full flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-xl font-bold text-silver-white">Lancia Carosello</h2>
                  <span className="bubble-ink text-xs gap-1">
                    <Sliders className="h-3 w-3 text-orange" />
                    Workflow Ibrido
                  </span>
                </div>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-xs font-semibold uppercase tracking-wider text-muted-foreground mb-2">
                      Argomento (Topic)
                    </label>
                    <textarea
                      placeholder="Es: Funnel di Conversione Strategico per vendere servizi High Ticket..."
                      value={topic}
                      onChange={(e) => setTopic(e.target.value)}
                      disabled={workflowStatus.isRunning}
                      className="w-full h-24 p-3 rounded-lg bg-ink-2 border border-white/10 text-white placeholder-white/30 focus:border-orange focus:outline-none transition-colors duration-200 resize-none text-sm"
                    />
                  </div>

                  <div className="flex items-center justify-between p-3 rounded-lg bg-ink-2/50 border border-white/5">
                    <div className="flex items-center gap-2">
                      <Eye className="h-4 w-4 text-orange" />
                      <span className="text-sm font-medium">Mostra browser durante la generazione</span>
                    </div>
                    <input 
                      type="checkbox"
                      checked={visibleMode}
                      onChange={(e) => setVisibleMode(e.target.checked)}
                      disabled={workflowStatus.isRunning}
                      className="w-4 h-4 accent-orange cursor-pointer"
                    />
                  </div>
                </div>
              </div>

              <div className="mt-8">
                <button
                  onClick={handleLaunchWorkflow}
                  disabled={workflowStatus.isRunning || !topic}
                  className="btn-orange w-full flex items-center justify-center gap-2 group disabled:opacity-50 disabled:pointer-events-none"
                >
                  <Play className="h-4 w-4 transition-transform group-hover:scale-110" />
                  Avvia Automazione Carosello
                </button>
              </div>
            </div>
          </Reveal>

          {/* Card 2: Setup Sessioni */}
          <Reveal variant="left" delay={0.3}>
            <div className="card-dark">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-xl font-bold text-silver-white">Configura Account</h2>
                <span className="bubble-ink text-xs gap-1">
                  <Zap className="h-3 w-3 text-orange" />
                  Session Cookie Setup
                </span>
              </div>
              
              <p className="text-muted-foreground text-xs mb-6">
                Lancia i browser interattivi per autenticare le sessioni in modalità visiva. 
                I file cookie verranno salvati in locale per i successivi utilizzi automatici.
              </p>

              <div className="grid grid-cols-2 gap-4">
                <button
                  onClick={() => handleStartSetup("arena")}
                  disabled={workflowStatus.isRunning}
                  className="btn-ghost flex flex-col py-4 items-center justify-center gap-2 text-center hover:border-orange/50 hover:bg-orange/5 transition-all duration-300 disabled:opacity-50"
                >
                  <ExternalLink className="h-5 w-5 text-orange" />
                  <span className="text-xs font-semibold">Setup Arena AI</span>
                </button>

                <button
                  onClick={() => handleStartSetup("drive")}
                  disabled={workflowStatus.isRunning}
                  className="btn-ghost flex flex-col py-4 items-center justify-center gap-2 text-center hover:border-orange/50 hover:bg-orange/5 transition-all duration-300 disabled:opacity-50"
                >
                  <FolderOpen className="h-5 w-5 text-orange" />
                  <span className="text-xs font-semibold">Setup Drive</span>
                </button>
              </div>
            </div>
          </Reveal>

        </div>

        {/* Colonna di Destra - Console Log */}
        <div className="lg:col-span-7">
          <Reveal variant="right" delay={0.2} className="h-full">
            <div className="card-dark h-full flex flex-col relative overflow-hidden border-orange/20">
              
              {/* Corner Brackets */}
              <div className="corner-bracket corner-tl"></div>
              <div className="corner-bracket corner-tr"></div>
              <div className="corner-bracket corner-bl"></div>
              <div className="corner-bracket corner-br"></div>
              
              <div className="flex items-center justify-between mb-4 border-b border-white/10 pb-4 z-10">
                <div className="flex items-center gap-2">
                  <Terminal className="h-5 w-5 text-orange" />
                  <h2 className="text-lg font-bold text-silver-white font-mono">live_automation.log</h2>
                </div>
                
                <div className="flex items-center gap-2">
                  <button 
                    onClick={handleClearLogs}
                    className="p-1.5 rounded bg-ink-2 hover:bg-white/5 border border-white/10 text-muted-foreground hover:text-white text-xs font-mono transition-colors duration-200 cursor-pointer"
                    title="Pulisci log"
                  >
                    Clear Console
                  </button>
                  <button 
                    onClick={() => setIsPollingLogs(!isPollingLogs)}
                    className={`p-1.5 rounded border text-xs font-mono transition-colors duration-200 cursor-pointer ${
                      isPollingLogs 
                        ? "bg-orange/10 border-orange text-orange" 
                        : "bg-ink-2 border-white/10 text-muted-foreground hover:text-white"
                    }`}
                  >
                    {isPollingLogs ? "Autorefresh: ON" : "Autorefresh: OFF"}
                  </button>
                </div>
              </div>

              {/* Terminal Screen */}
              <div className="flex-1 w-full bg-black/85 rounded-lg border border-white/5 p-4 font-mono text-xs text-green-400 overflow-y-auto max-h-[380px] h-[380px] z-10 custom-scrollbar shadow-inner">
                <pre className="whitespace-pre-wrap word-break break-all">
                  {logs}
                </pre>
                <div ref={terminalEndRef} />
              </div>

            </div>
          </Reveal>
        </div>

      </div>

      {/* Sezione: Media Explorer (Caroselli Generati) */}
      <Reveal variant="up" delay={0.4}>
        <div className="section section-border-t">
          <div className="flex items-center justify-between mb-8">
            <div>
              <span className="bubble-silver gap-1 mb-2">
                <FolderOpen className="h-3 w-3 text-orange" />
                Galleria Output
              </span>
              <h2 className="text-3xl font-extrabold text-silver-white">
                CAROSELLI GENERATI IN LOCALE
              </h2>
            </div>
            <button 
              onClick={fetchCaroselli}
              className="p-2 rounded bg-ink-2 border border-white/10 text-muted-foreground hover:text-white hover:border-orange/30 transition-all cursor-pointer flex items-center gap-2 text-xs"
            >
              <RefreshCw className="h-3 w-3" />
              Aggiorna Galleria
            </button>
          </div>

          {caroselli.length === 0 ? (
            <div className="card-dark flex flex-col items-center justify-center py-16 text-center">
              <FolderClosed className="h-16 w-16 text-muted-foreground mb-4" />
              <h3 className="font-bold text-lg text-silver-white mb-2">Nessun carosello generato in locale</h3>
              <p className="text-muted-foreground text-sm max-w-md">
                Lancia un'automazione utilizzando il pannello dei controlli per generare le slide grafiche e visualizzarle qui.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {caroselli.map((car, idx) => (
                <div 
                  key={idx} 
                  className="card-dark flex flex-col justify-between hover:border-orange transition-all duration-300"
                >
                  <div>
                    <div className="flex items-center justify-between mb-4">
                      <span className="text-[10px] uppercase tracking-wider text-orange font-bold font-mono">
                        {new Date(car.createdAt).toLocaleDateString("it-IT", {
                          day: "2-digit",
                          month: "short",
                          hour: "2-digit",
                          minute: "2-digit"
                        })}
                      </span>
                      <span className="bubble-ink text-[10px] py-0.5 px-2">
                        {car.slides.length} Slide
                      </span>
                    </div>

                    <h3 className="font-bold text-base text-silver-white line-clamp-2 mb-4">
                      {car.folderName.replace(/_/g, " ")}
                    </h3>
                  </div>

                  <div className="mt-4 flex items-center justify-between border-t border-white/10 pt-4">
                    <button
                      onClick={() => {
                        setSelectedCarosello(car);
                        setActiveSlideIndex(0);
                      }}
                      className="text-xs font-bold text-orange hover:text-white transition-colors duration-200 flex items-center gap-1 cursor-pointer"
                    >
                      <Eye className="h-4 w-4" />
                      Visualizza Slide
                    </button>
                    
                    <span className="text-[10px] text-muted-foreground font-mono">
                      /output_caroselli/...
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </Reveal>

      {/* Sezione: Editor File Config */}
      <Reveal variant="up" delay={0.5}>
        <div className="section section-border-t">
          <div className="mb-8">
            <span className="bubble-silver gap-1 mb-2">
              <Settings className="h-3 w-3 text-orange" />
              Editor Config
            </span>
            <h2 className="text-3xl font-extrabold text-silver-white">
              TEMPLATE PROMPT & REGOLE
            </h2>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
            
            {/* Pulsanti file */}
            <div className="lg:col-span-3 flex flex-col gap-3">
              {[
                { key: "prompt", label: "Template Prompt", desc: "I tre prompt principali" },
                { key: "regole", label: "Regole Generali (REGOLE.md)", desc: "Linee guida dei caroselli" },
                { key: "config", label: "Config Python (config.py)", desc: "Chiavi API e costanti" }
              ].map((item) => (
                <button
                  key={item.key}
                  onClick={() => {
                    setSelectedConfigFile(item.key as any);
                    fetchConfigFile(item.key);
                  }}
                  className={`w-full text-left p-4 rounded-xl border transition-all duration-200 cursor-pointer ${
                    selectedConfigFile === item.key
                      ? "bg-orange/10 border-orange text-white shadow-md shadow-orange/10"
                      : "bg-ink border-white/10 text-muted-foreground hover:text-white hover:border-white/20"
                  }`}
                >
                  <h3 className="font-bold text-sm">{item.label}</h3>
                  <p className="text-[11px] text-muted-foreground mt-1">{item.desc}</p>
                </button>
              ))}
            </div>

            {/* Editor Area */}
            <div className="lg:col-span-9 card-dark">
              <div className="flex items-center justify-between mb-4 pb-4 border-b border-white/10">
                <span className="font-mono text-xs text-orange">
                  {selectedConfigFile === "prompt" && "Template-prompt.md"}
                  {selectedConfigFile === "regole" && "REGOLE.md"}
                  {selectedConfigFile === "config" && "config.py"}
                </span>
                
                {saveStatus && (
                  <span className={`text-xs font-semibold font-mono ${
                    saveStatus.includes("successo") ? "text-green-400" : "text-amber-400"
                  }`}>
                    {saveStatus}
                  </span>
                )}
              </div>

              <textarea
                value={configContent}
                onChange={(e) => setConfigContent(e.target.value)}
                className="w-full h-[320px] p-4 bg-ink-2 border border-white/10 text-white rounded-lg font-mono text-xs focus:outline-none focus:border-orange resize-none custom-scrollbar mb-4"
              />

              <div className="flex justify-end">
                <button
                  onClick={handleSaveConfig}
                  className="btn-orange text-xs py-2 px-4 flex items-center gap-1.5"
                >
                  <Save className="h-4 w-4" />
                  Salva Modifiche File
                </button>
              </div>
            </div>

          </div>
        </div>
      </Reveal>

      {/* Overlay Modal: Visualizzatore Carosello Slide */}
      {selectedCarosello && (
        <div className="fixed inset-0 bg-black/90 z-[300] flex items-center justify-center p-4 backdrop-blur-sm">
          <div className="relative w-full max-w-4xl bg-ink rounded-2xl border border-white/15 overflow-hidden flex flex-col max-h-[90vh]">
            
            {/* Header Modal */}
            <div className="flex items-center justify-between p-4 border-b border-white/10 bg-black/40">
              <div>
                <h3 className="font-bold text-base text-silver-white line-clamp-1">
                  {selectedCarosello.folderName.replace(/_/g, " ")}
                </h3>
                <p className="text-[10px] text-muted-foreground font-mono">
                  Slide {activeSlideIndex + 1} di {selectedCarosello.slides.length}
                </p>
              </div>
              <button 
                onClick={() => setSelectedCarosello(null)}
                className="p-1 rounded-lg bg-ink-2 hover:bg-white/5 text-muted-foreground hover:text-white border border-white/10 cursor-pointer"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            {/* Slide Body */}
            <div className="flex-1 flex items-center justify-center p-6 bg-black/35 min-h-[300px]">
              {selectedCarosello.slides.length > 0 ? (
                <div className="relative max-w-full max-h-[50vh] flex items-center justify-center">
                  <img
                    src={`/api/caroselli?folder=${encodeURIComponent(selectedCarosello.folderName)}&file=${encodeURIComponent(selectedCarosello.slides[activeSlideIndex])}`}
                    alt={`Slide ${activeSlideIndex + 1}`}
                    className="max-w-full max-h-[50vh] object-contain rounded-xl border border-white/10 shadow-2xl"
                  />
                </div>
              ) : (
                <div className="text-center text-muted-foreground">Nessuna slide generata in questa cartella.</div>
              )}
            </div>

            {/* Controlli Modal */}
            <div className="p-4 border-t border-white/10 bg-black/40 flex items-center justify-between">
              <button
                disabled={activeSlideIndex === 0}
                onClick={() => setActiveSlideIndex(activeSlideIndex - 1)}
                className="btn-ghost py-2 px-4 text-xs flex items-center gap-1 hover:border-orange/30 disabled:opacity-30 disabled:pointer-events-none"
              >
                <ChevronLeft className="h-4 w-4" />
                Precedente
              </button>

              <div className="flex items-center gap-1.5 max-w-[50%] overflow-x-auto">
                {selectedCarosello.slides.map((_: any, idx: number) => (
                  <button
                    key={idx}
                    onClick={() => setActiveSlideIndex(idx)}
                    className={`w-2.5 h-2.5 rounded-full transition-all duration-300 ${
                      activeSlideIndex === idx ? "bg-orange scale-125" : "bg-white/20 hover:bg-white/50"
                    }`}
                  />
                ))}
              </div>

              <button
                disabled={activeSlideIndex === selectedCarosello.slides.length - 1}
                onClick={() => setActiveSlideIndex(activeSlideIndex + 1)}
                className="btn-ghost py-2 px-4 text-xs flex items-center gap-1 hover:border-orange/30 disabled:opacity-30 disabled:pointer-events-none"
              >
                Successiva
                <ChevronRight className="h-4 w-4" />
              </button>
            </div>

          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="mt-20 border-t border-white/10 pt-8 text-center text-xs text-muted-foreground">
        <p>© 2026 Digital Empire. Tutti i diritti riservati.</p>
        <p className="mt-2 font-mono text-[10px] text-white/20">
          Engineered by Antigravity · pair-programmed with VIP User
        </p>
      </footer>

    </div>
  );
}
