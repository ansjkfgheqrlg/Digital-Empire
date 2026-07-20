import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Funnel, FunnelStep, FunnelConnection, FunnelStepType, ConnectionType, FunnelPageElement } from '../types';
import { Button } from './ui/Button';
import { 
  Plus, X, ArrowRight, Layout, CreditCard, Mail, CheckCircle, 
  MousePointer, ZoomIn, ZoomOut, Move, Zap, Globe, MessageSquare, 
  ShoppingCart, Shield, Smartphone, Trash2, Settings, Save, 
  FileText, Video, Tag, Target, Play, Pause, Layers, DollarSign,
  Clock, Split, AlertTriangle, TrendingUp, BarChart3, Eye, Box
} from 'lucide-react';

interface FunnelBuilderProps {
  funnel: Funnel;
  onUpdate: (updatedFunnel: Funnel) => void;
  onBack: () => void;
}

// DEFINIZIONE BLOCCHI AVANZATA
interface StepDefinition {
  type: FunnelStepType;
  label: string;
  icon: any;
  category: 'TRAFFIC' | 'PAGE' | 'ACTION' | 'LOGIC';
  color: string;
  description: string;
  defaultConfig: any;
}

const STEP_DEFINITIONS: StepDefinition[] = [
  // TRAFFIC
  { 
    type: 'TRAFFIC', label: 'Traffic Source', icon: Globe, category: 'TRAFFIC', 
    color: 'text-blue-400 border-blue-500/50 bg-blue-900/10', 
    description: 'Punto di ingresso (Ads, Organic, Email). Definisce il volume iniziale.',
    defaultConfig: { trafficSource: 'META', cpc: 1.50, budget: 100 } 
  },
  
  // PAGES
  { 
    type: 'LANDING', label: 'Landing / Opt-in', icon: Layout, category: 'PAGE', 
    color: 'text-diamond-400 border-diamond-500/50 bg-diamond-900/10', 
    description: 'Pagina cattura contatti. Focus su Conversion Rate.',
    defaultConfig: { conversionGoal: 20 } 
  },
  { 
    type: 'VSL', label: 'VSL / Sales Page', icon: Video, category: 'PAGE', 
    color: 'text-purple-400 border-purple-500/50 bg-purple-900/10', 
    description: 'Video Sales Letter. Pagina educativa pre-vendita.',
    defaultConfig: { conversionGoal: 5, videoDuration: '15:00' } 
  },
  { 
    type: 'CHECKOUT', label: 'Checkout', icon: CreditCard, category: 'PAGE', 
    color: 'text-green-400 border-green-500/50 bg-green-900/10', 
    description: 'Pagina di pagamento. Genera Revenue.',
    defaultConfig: { conversionGoal: 40, price: 97, productName: 'Main Offer' } 
  },
  { 
    type: 'UPSELL', label: 'Upsell (OTO)', icon: TrendingUp, category: 'PAGE', 
    color: 'text-orange-400 border-orange-500/50 bg-orange-900/10', 
    description: 'Offerta One-Time post acquisto. Aumenta AOV.',
    defaultConfig: { conversionGoal: 15, price: 47, productName: 'OTO #1' } 
  },
  { 
    type: 'THANK_YOU', label: 'Thank You Page', icon: CheckCircle, category: 'PAGE', 
    color: 'text-slate-400 border-slate-500/50 bg-slate-900/10', 
    description: 'Pagina di conferma e consegna.',
    defaultConfig: {} 
  },

  // ACTIONS
  { 
    type: 'EMAIL', label: 'Email', icon: Mail, category: 'ACTION', 
    color: 'text-yellow-400 border-yellow-500/50 bg-yellow-900/10', 
    description: 'Invio email singola o sequenza.',
    defaultConfig: { openRate: 30, ctr: 5 } 
  },
  
  // LOGIC
  { 
    type: 'WAIT', label: 'Wait / Delay', icon: Clock, category: 'LOGIC', 
    color: 'text-gray-400 border-gray-500/50 bg-gray-900/10', 
    description: 'Pausa nel flusso temporale.',
    defaultConfig: { delayHours: 24 } 
  },
];

const GRID_SIZE = 20;

export const FunnelBuilder: React.FC<FunnelBuilderProps> = ({ funnel, onUpdate, onBack }) => {
  // CORE STATE
  const [steps, setSteps] = useState<FunnelStep[]>(funnel.steps);
  const [connections, setConnections] = useState<FunnelConnection[]>(funnel.connections);
  
  // UI STATE
  const [viewport, setViewport] = useState({ x: 0, y: 0, zoom: 1 });
  const [isPanning, setIsPanning] = useState(false);
  const [lastMousePos, setLastMousePos] = useState({ x: 0, y: 0 });
  const [draggingId, setDraggingId] = useState<string | null>(null);
  const [selectedStepId, setSelectedStepId] = useState<string | null>(null);
  
  // CONNECTION STATE
  const [connectingFrom, setConnectingFrom] = useState<{id: string, type: ConnectionType} | null>(null);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 }); 
  
  // SIMULATION STATE
  const [isSimulating, setIsSimulating] = useState(false);
  const [simulationData, setSimulationData] = useState({
      totalTraffic: 0,
      totalRevenue: 0,
      totalCost: 0,
      totalProfit: 0,
      roas: 0
  });

  const canvasRef = useRef<HTMLDivElement>(null);

  // --- SIMULATION ENGINE ---
  const runSimulation = useCallback(() => {
      // 1. Reset Metrics
      let newSteps = steps.map(s => ({
          ...s,
          metrics: { trafficIn: 0, conversionRate: s.config.conversionGoal || 0, trafficOut: 0, revenue: 0, cost: 0, profit: 0 }
      }));

      let totalRevenue = 0;
      let totalCost = 0;

      // 2. Identify Traffic Sources (Roots)
      const trafficSources = newSteps.filter(s => s.type === 'TRAFFIC');

      // 3. Process Flow (Simple BFS for Demo)
      const queue = [...trafficSources];
      const visited = new Set<string>(); // Avoid infinite loops

      while (queue.length > 0) {
          const current = queue.shift();
          if (!current) continue;

          // Calculate Node Metrics
          if (current.type === 'TRAFFIC') {
              current.metrics.trafficIn = current.config.budget && current.config.cpc ? Math.floor(current.config.budget / current.config.cpc) : 0;
              current.metrics.cost = current.config.budget || 0;
              current.metrics.trafficOut = current.metrics.trafficIn; // Pass through
          } else {
              // Standard Conversion Logic
              const conversionDecimal = (current.metrics.conversionRate || 0) / 100;
              const conversions = Math.floor(current.metrics.trafficIn * conversionDecimal);
              
              if (current.type === 'CHECKOUT' || current.type === 'UPSELL') {
                  current.metrics.revenue = conversions * (current.config.price || 0);
                  current.metrics.trafficOut = conversions; // Only buyers pass through "Success" path (usually)
              } else {
                  current.metrics.trafficOut = conversions; // Leads/Clicks pass through
              }
          }

          // Aggregate Globals
          totalRevenue += current.metrics.revenue || 0;
          totalCost += current.metrics.cost || 0;

          // Find Outgoing Connections
          const outgoing = connections.filter(c => c.fromStepId === current.id);
          
          outgoing.forEach(conn => {
              const targetIndex = newSteps.findIndex(s => s.id === conn.toStepId);
              if (targetIndex !== -1) {
                  const target = newSteps[targetIndex];
                  
                  // Logic for Split Paths
                  if (conn.type === 'YES_PATH' || conn.type === 'STANDARD') {
                      target.metrics.trafficIn += current.metrics.trafficOut;
                  } else if (conn.type === 'NO_PATH') {
                      // Logic: Traffic In - Traffic Out (Buyers) = Non Buyers
                      target.metrics.trafficIn += (current.metrics.trafficIn - current.metrics.trafficOut);
                  }

                  if (!visited.has(target.id)) {
                      queue.push(target);
                      visited.add(target.id); // Simple loop prevention, in real app need improved graph traversal
                  }
              }
          });
      }

      setSteps(newSteps);
      setSimulationData({
          totalTraffic: trafficSources.reduce((acc, s) => acc + s.metrics.trafficIn, 0),
          totalRevenue,
          totalCost,
          totalProfit: totalRevenue - totalCost,
          roas: totalCost > 0 ? totalRevenue / totalCost : 0
      });

  }, [steps, connections]); // Dependency implies run on structure change, but we trigger manually or on value change

  // Auto-run simulation when values change if mode is active
  useEffect(() => {
      if (isSimulating) {
          runSimulation();
      }
  }, [isSimulating]);

  // --- CANVAS HANDLERS ---
  const handleCanvasMouseMove = (e: React.MouseEvent) => {
    if (canvasRef.current) {
        const rect = canvasRef.current.getBoundingClientRect();
        setMousePos({
            x: (e.clientX - rect.left - viewport.x) / viewport.zoom,
            y: (e.clientY - rect.top - viewport.y) / viewport.zoom
        });
    }

    if (isPanning) {
      setViewport(prev => ({ 
          ...prev, 
          x: prev.x + e.clientX - lastMousePos.x, 
          y: prev.y + e.clientY - lastMousePos.y 
      }));
      setLastMousePos({ x: e.clientX, y: e.clientY });
    }

    if (draggingId) {
      setSteps(prev => prev.map(step => {
        if (step.id === draggingId) {
          const rawX = mousePos.x - 100; 
          const rawY = mousePos.y - 40; 
          return { 
              ...step, 
              x: Math.round(rawX / GRID_SIZE) * GRID_SIZE, 
              y: Math.round(rawY / GRID_SIZE) * GRID_SIZE 
          };
        }
        return step;
      }));
    }
  };

  const handleWheel = (e: React.WheelEvent) => {
    if (e.ctrlKey || e.metaKey) {
      // Zoom
      const zoomSensitivity = 0.001;
      const newZoom = Math.min(Math.max(0.1, viewport.zoom - e.deltaY * zoomSensitivity), 5);
      setViewport(prev => ({ ...prev, zoom: newZoom }));
    } else {
      // Pan
      setViewport(prev => ({ ...prev, x: prev.x - e.deltaX, y: prev.y - e.deltaY }));
    }
  };

  // --- CONNECTION LOGIC ---
  const startConnection = (e: React.MouseEvent, id: string, type: ConnectionType) => {
    e.stopPropagation();
    setConnectingFrom({ id, type });
  };

  const finishConnection = (e: React.MouseEvent, targetId: string) => {
    e.stopPropagation();
    if (connectingFrom && connectingFrom.id !== targetId) {
      // Prevent duplicate
      if (!connections.find(c => c.fromStepId === connectingFrom.id && c.toStepId === targetId && c.type === connectingFrom.type)) {
          setConnections([...connections, { 
              id: `conn-${Date.now()}`, 
              fromStepId: connectingFrom.id, 
              toStepId: targetId, 
              type: connectingFrom.type 
          }]);
      }
    }
    setConnectingFrom(null);
  };

  // --- ACTIONS ---
  const addStep = (def: StepDefinition) => {
    const centerX = (-viewport.x + 600) / viewport.zoom;
    const centerY = (-viewport.y + 400) / viewport.zoom;
    
    const newStep: FunnelStep = {
      id: `step-${Date.now()}`,
      type: def.type,
      label: def.label,
      x: centerX, y: centerY,
      metrics: { trafficIn:0, trafficOut:0, conversionRate: def.defaultConfig.conversionGoal || 0, revenue:0, cost:0, profit:0 },
      config: { ...def.defaultConfig },
      elements: []
    };
    
    setSteps([...steps, newStep]);
    setSelectedStepId(newStep.id);
  };

  const deleteStep = (id: string) => {
    setSteps(prev => prev.filter(s => s.id !== id));
    setConnections(prev => prev.filter(c => c.fromStepId !== id && c.toStepId !== id));
    if (selectedStepId === id) setSelectedStepId(null);
  };

  const updateStepConfig = (stepId: string, key: string, value: any) => {
    setSteps(prev => prev.map(s => {
      if (s.id === stepId) {
        return { ...s, config: { ...s.config, [key]: value } };
      }
      return s;
    }));
  };

  const togglePageElement = (element: FunnelPageElement['type']) => {
      if(!selectedStepId) return;
      setSteps(prev => prev.map(s => {
          if(s.id !== selectedStepId) return s;
          const exists = s.elements?.find(e => e.type === element);
          const newElements = exists 
              ? s.elements?.filter(e => e.type !== element)
              : [...(s.elements || []), { id: `el-${Date.now()}`, type: element, label: element }];
          return { ...s, elements: newElements };
      }));
  };

  // --- DRAWING ---
  const getPath = (start: {x:number, y:number, w:number, h:number}, end: {x:number, y:number}, type: ConnectionType) => {
      // Calculate output port position based on type
      let startX = start.x + start.w;
      let startY = start.y + (start.h / 2);
      
      if (type === 'YES_PATH') {
          startY = start.y + (start.h * 0.25); // Top right
      } else if (type === 'NO_PATH') {
          startY = start.y + (start.h * 0.75); // Bottom right
      }

      const endX = end.x;
      const endY = end.y + 40; // Approx middle of input

      const dist = Math.abs(endX - startX) * 0.5;
      const cp1 = { x: startX + dist, y: startY };
      const cp2 = { x: endX - dist, y: endY };

      return `M ${startX} ${startY} C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${endX} ${endY}`;
  };

  const getConnectionColor = (type: ConnectionType) => {
      switch(type) {
          case 'YES_PATH': return '#4ade80'; // Green
          case 'NO_PATH': return '#f87171'; // Red
          default: return '#5D8AA8'; // Blue
      }
  };

  const selectedStep = steps.find(s => s.id === selectedStepId);

  return (
    <div className="h-[calc(100vh-140px)] flex bg-[#020202] rounded-sm overflow-hidden border border-diamond-500/20 relative animate-in fade-in duration-500">
      
      {/* 1. TOOLBAR (Left) */}
      <div className="absolute left-4 top-4 bottom-4 w-60 z-20 flex flex-col gap-4 pointer-events-none">
          <div className="bg-[#0A0A0A]/95 backdrop-blur-md border border-white/10 rounded-sm p-4 shadow-2xl pointer-events-auto flex flex-col gap-6 overflow-y-auto custom-scrollbar h-full">
              <div className="flex items-center gap-3 border-b border-white/10 pb-4">
                  <div className="p-2 bg-diamond-950/50 rounded-sm border border-diamond-500/30">
                      <Layers className="w-5 h-5 text-diamond-400" />
                  </div>
                  <div>
                      <h2 className="text-xs font-bold text-white uppercase tracking-widest">Components</h2>
                      <p className="text-[9px] text-platinum-500">Drag & Drop Logic</p>
                  </div>
              </div>

              {['TRAFFIC', 'PAGE', 'ACTION', 'LOGIC'].map(cat => (
                  <div key={cat}>
                      <h3 className="text-[9px] font-bold text-platinum-600 uppercase tracking-[0.2em] mb-2 pl-1">{cat}</h3>
                      <div className="grid grid-cols-1 gap-2">
                          {STEP_DEFINITIONS.filter(d => d.category === cat).map(def => (
                              <button
                                  key={def.type}
                                  onClick={() => addStep(def)}
                                  className="group flex items-center gap-3 p-2 rounded-sm border border-white/5 hover:bg-white/5 hover:border-diamond-500/30 transition-all text-left relative overflow-hidden"
                              >
                                  <div className={`p-1.5 rounded-sm ${def.color.replace('text-', 'bg-').replace('border-', '').split(' ')[2]} border border-white/10`}>
                                      {React.createElement(def.icon, { size: 14, className: def.color.split(' ')[0] })}
                                  </div>
                                  <div>
                                      <span className="text-xs text-platinum-300 group-hover:text-white font-medium block">{def.label}</span>
                                      <span className="text-[8px] text-platinum-600 block leading-tight mt-0.5">{def.description.substring(0, 25)}...</span>
                                  </div>
                              </button>
                          ))}
                      </div>
                  </div>
              ))}
          </div>
      </div>

      {/* 2. TOP HUD (Simulation & Actions) */}
      <div className="absolute top-4 left-72 right-80 h-16 z-20 pointer-events-none flex justify-between items-start">
          {/* Simulation Stats Bar */}
          <div className="bg-[#0A0A0A]/90 backdrop-blur border border-white/10 rounded-sm px-6 py-2 shadow-xl pointer-events-auto flex items-center gap-8 h-14">
              <div className="flex items-center gap-2">
                  <div className={`w-2 h-2 rounded-full ${isSimulating ? 'bg-green-500 animate-pulse' : 'bg-platinum-600'}`}></div>
                  <span className="text-[10px] font-bold text-platinum-400 uppercase tracking-wider">
                      {isSimulating ? 'SIMULATION LIVE' : 'DESIGN MODE'}
                  </span>
              </div>
              
              <div className="h-8 w-[1px] bg-white/10"></div>

              <div className="flex gap-6">
                  <div>
                      <p className="text-[9px] text-platinum-600 uppercase">Spesa Ad</p>
                      <p className="text-sm font-bold text-white">€{simulationData.totalCost.toLocaleString()}</p>
                  </div>
                  <div>
                      <p className="text-[9px] text-platinum-600 uppercase">Fatturato</p>
                      <p className="text-sm font-bold text-emerald-400">€{simulationData.totalRevenue.toLocaleString()}</p>
                  </div>
                  <div>
                      <p className="text-[9px] text-platinum-600 uppercase">Profitto</p>
                      <p className={`text-sm font-bold ${simulationData.totalProfit > 0 ? 'text-emerald-400' : 'text-red-400'}`}>
                          €{simulationData.totalProfit.toLocaleString()}
                      </p>
                  </div>
                  <div>
                      <p className="text-[9px] text-platinum-600 uppercase">ROAS</p>
                      <p className="text-sm font-bold text-diamond-400">{simulationData.roas.toFixed(2)}x</p>
                  </div>
              </div>

              <div className="h-8 w-[1px] bg-white/10"></div>

              <div className="flex gap-2">
                  <Button 
                    size="sm" 
                    variant={isSimulating ? "outline" : "diamond"} 
                    onClick={() => { setIsSimulating(!isSimulating); if(!isSimulating) runSimulation(); }}
                    icon={isSimulating ? <Pause className="w-3 h-3"/> : <Play className="w-3 h-3"/>}
                  >
                      {isSimulating ? 'STOP' : 'SIMULA'}
                  </Button>
                  <Button 
                    size="sm" 
                    variant="ghost" 
                    onClick={() => onUpdate({ ...funnel, steps, connections })}
                    icon={<Save className="w-3 h-3"/>}
                  >
                      SALVA
                  </Button>
              </div>
          </div>

          {/* View Controls */}
          <div className="bg-[#0A0A0A]/90 backdrop-blur border border-white/10 rounded-sm p-2 shadow-xl pointer-events-auto flex gap-2">
              <button onClick={() => setViewport(v => ({...v, zoom: v.zoom + 0.1}))} className="p-2 hover:bg-white/10 rounded text-platinum-400 hover:text-white"><ZoomIn size={18}/></button>
              <button onClick={() => setViewport(v => ({...v, zoom: v.zoom - 0.1}))} className="p-2 hover:bg-white/10 rounded text-platinum-400 hover:text-white"><ZoomOut size={18}/></button>
              <button onClick={() => setViewport({x:0, y:0, zoom:1})} className="p-2 hover:bg-white/10 rounded text-platinum-400 hover:text-white"><Move size={18}/></button>
          </div>
      </div>

      {/* 3. INFINITE CANVAS */}
      <div 
        ref={canvasRef}
        className={`flex-1 relative overflow-hidden cursor-crosshair bg-[#050505]`}
        onMouseDown={(e) => {
            if (e.button === 1 || e.button === 0 && !draggingId) {
                setIsPanning(true);
                setLastMousePos({ x: e.clientX, y: e.clientY });
                if (!draggingId) setSelectedStepId(null);
            }
        }}
        onMouseMove={handleCanvasMouseMove}
        onMouseUp={() => { setIsPanning(false); setDraggingId(null); setConnectingFrom(null); }}
        onMouseLeave={() => { setIsPanning(false); setDraggingId(null); }}
        onWheel={handleWheel}
      >
          {/* Grid Pattern */}
          <div 
            className="absolute inset-0 pointer-events-none z-0 opacity-10"
            style={{
                transform: `translate(${viewport.x}px, ${viewport.y}px) scale(${viewport.zoom})`,
                transformOrigin: '0 0',
                backgroundImage: `linear-gradient(#333 1px, transparent 1px), linear-gradient(90deg, #333 1px, transparent 1px)`,
                backgroundSize: `${GRID_SIZE}px ${GRID_SIZE}px`
            }}
          ></div>

          <div 
            className="absolute inset-0 origin-top-left z-10"
            style={{ transform: `translate(${viewport.x}px, ${viewport.y}px) scale(${viewport.zoom})` }}
          >
              {/* SVG Layer for Connections */}
              <svg className="absolute top-0 left-0 w-[50000px] h-[50000px] pointer-events-none overflow-visible">
                  <defs>
                      <marker id="arrowhead" markerWidth="5" markerHeight="5" refX="5" refY="2.5" orient="auto">
                          <polygon points="0 0, 5 2.5, 0 5" fill="#52606D" />
                      </marker>
                  </defs>
                  
                  {/* Draft Line */}
                  {connectingFrom && (
                      <path 
                          d={getPath(
                              { 
                                  x: steps.find(s => s.id === connectingFrom.id)?.x || 0, 
                                  y: steps.find(s => s.id === connectingFrom.id)?.y || 0, 
                                  w: 220, h: 120 
                              }, 
                              mousePos, 
                              connectingFrom.type
                          )}
                          stroke={getConnectionColor(connectingFrom.type)}
                          strokeWidth="2" 
                          strokeDasharray="5,5" 
                          fill="none"
                      />
                  )}

                  {/* Real Connections */}
                  {connections.map(conn => {
                      const from = steps.find(s => s.id === conn.fromStepId);
                      const to = steps.find(s => s.id === conn.toStepId);
                      if (!from || !to) return null;
                      
                      return (
                          <g key={conn.id} onClick={(e) => { if(e.shiftKey) setConnections(prev => prev.filter(c => c.id !== conn.id)) }} className="pointer-events-auto cursor-pointer group">
                              <path 
                                  d={getPath({x:from.x, y:from.y, w:220, h:120}, {x:to.x, y:to.y}, conn.type)} 
                                  stroke={getConnectionColor(conn.type)} 
                                  strokeWidth="2" 
                                  fill="none"
                                  markerEnd="url(#arrowhead)"
                                  className="group-hover:stroke-white transition-colors"
                              />
                              {isSimulating && from.metrics.trafficOut > 0 && (
                                  <circle r="3" fill="#fff">
                                      <animateMotion dur={`${Math.max(0.5, 2 - (from.metrics.trafficOut/1000))}s`} repeatCount="indefinite" path={getPath({x:from.x, y:from.y, w:220, h:120}, {x:to.x, y:to.y}, conn.type)} />
                                  </circle>
                              )}
                          </g>
                      );
                  })}
              </svg>

              {/* Nodes */}
              {steps.map(step => {
                  const def = STEP_DEFINITIONS.find(d => d.type === step.type);
                  const isSelected = selectedStepId === step.id;
                  
                  // Render DNA Elements
                  const renderDNA = () => (
                      <div className="flex flex-wrap gap-1 mt-3 px-3">
                          {step.elements?.map(el => (
                              <div key={el.id} className="w-4 h-4 bg-white/10 rounded-sm flex items-center justify-center text-[8px] text-platinum-400 border border-white/5" title={el.label}>
                                  {el.type === 'VIDEO' && <Video size={8} />}
                                  {el.type === 'TEXT' && <FileText size={8} />}
                                  {el.type === 'BUTTON' && <MousePointer size={8} />}
                                  {el.type === 'TIMER' && <Clock size={8} />}
                              </div>
                          ))}
                      </div>
                  );

                  return (
                      <div
                          key={step.id}
                          className={`
                              absolute w-[220px] rounded-sm bg-[#0F0F0F] border-2 transition-all duration-200 select-none group
                              ${isSelected ? 'border-diamond-400 shadow-[0_0_20px_rgba(34,211,238,0.2)]' : 'border-white/10 hover:border-white/30'}
                          `}
                          style={{ transform: `translate(${step.x}px, ${step.y}px)` }}
                          onMouseDown={(e) => { e.stopPropagation(); setDraggingId(step.id); setSelectedStepId(step.id); }}
                          onMouseUp={(e) => { e.stopPropagation(); finishConnection(e, step.id); }}
                      >
                          {/* Header */}
                          <div className={`px-3 py-2 border-b border-white/5 flex items-center gap-2 bg-gradient-to-r ${def?.color.replace('text-', 'from-').replace('border-', '').split(' ')[2]} to-transparent`}>
                              {def && React.createElement(def.icon, { size: 14, className: 'text-white' })}
                              <span className="text-[10px] font-bold text-white uppercase tracking-wider truncate">{step.label}</span>
                          </div>

                          {/* Body */}
                          <div className="py-3">
                              {/* Simulation Stats (if running) */}
                              {isSimulating ? (
                                  <div className="px-3 space-y-1">
                                      <div className="flex justify-between text-[10px] text-platinum-400">
                                          <span>Traffico:</span>
                                          <span className="text-white font-mono">{step.metrics.trafficIn}</span>
                                      </div>
                                      {(step.type === 'CHECKOUT' || step.type === 'UPSELL') && (
                                          <div className="flex justify-between text-[10px] text-platinum-400">
                                              <span>Revenue:</span>
                                              <span className="text-emerald-400 font-mono font-bold">€{step.metrics.revenue}</span>
                                          </div>
                                      )}
                                      <div className="flex justify-between text-[10px] text-platinum-400">
                                          <span>Conv. Rate:</span>
                                          <span className="text-yellow-400 font-mono">{step.metrics.conversionRate}%</span>
                                      </div>
                                  </div>
                              ) : (
                                  // Edit Mode Stats
                                  <div className="px-3 text-center">
                                      <p className="text-[9px] text-platinum-500 uppercase tracking-widest mb-1">Target Conversion</p>
                                      <p className="text-xl font-bold text-white">{step.config.conversionGoal || 0}%</p>
                                  </div>
                              )}
                              
                              {/* Page DNA Visualization */}
                              {renderDNA()}
                          </div>

                          {/* Ports */}
                          {/* Input (Left) */}
                          <div className="absolute -left-2 top-1/2 -translate-y-1/2 w-4 h-4 bg-[#0A0A0A] border border-white/30 rounded-full hover:bg-diamond-500 transition-colors z-20"></div>

                          {/* Outputs (Right) */}
                          {step.type === 'CHECKOUT' || step.type === 'UPSELL' ? (
                              // Split Path Outputs
                              <div className="absolute -right-3 top-0 bottom-0 flex flex-col justify-around py-4">
                                  <button 
                                    onMouseDown={(e) => startConnection(e, step.id, 'YES_PATH')}
                                    className="w-4 h-4 rounded-full bg-[#0A0A0A] border-2 border-green-500 hover:bg-green-500 transition-colors z-20"
                                    title="Success / Purchase"
                                  ></button>
                                  <button 
                                    onMouseDown={(e) => startConnection(e, step.id, 'NO_PATH')}
                                    className="w-4 h-4 rounded-full bg-[#0A0A0A] border-2 border-red-500 hover:bg-red-500 transition-colors z-20"
                                    title="Fail / Reject"
                                  ></button>
                              </div>
                          ) : (
                              // Standard Output
                              <button 
                                onMouseDown={(e) => startConnection(e, step.id, 'STANDARD')}
                                className="absolute -right-2 top-1/2 -translate-y-1/2 w-4 h-4 rounded-full bg-[#0A0A0A] border border-diamond-500 hover:bg-diamond-500 transition-colors z-20"
                              ></button>
                          )}
                      </div>
                  );
              })}
          </div>
      </div>

      {/* 4. INSPECTOR PANEL (Right) */}
      <div className={`
          absolute top-4 right-4 bottom-4 w-80 bg-[#0A0A0A]/95 backdrop-blur-xl border border-white/10 rounded-sm shadow-2xl z-30 transition-transform duration-300
          flex flex-col
          ${selectedStep ? 'translate-x-0' : 'translate-x-[120%]'}
      `}>
          {selectedStep && (
              <>
                  <div className="p-5 border-b border-white/10 flex justify-between items-center bg-[#0F0F0F]">
                      <div>
                          <h3 className="text-sm font-bold text-white uppercase tracking-widest">{selectedStep.label}</h3>
                          <p className="text-[9px] text-platinum-500">{selectedStep.type}</p>
                      </div>
                      <button onClick={() => deleteStep(selectedStep.id)} className="text-red-400 hover:text-red-300"><Trash2 size={16}/></button>
                  </div>

                  <div className="flex-1 overflow-y-auto custom-scrollbar p-5 space-y-8">
                      
                      {/* 1. CONFIGURAZIONE BASE */}
                      <div className="space-y-4">
                          <h4 className="text-[10px] font-bold text-diamond-400 uppercase tracking-widest border-b border-white/5 pb-2">Parametri Base</h4>
                          
                          <div className="space-y-2">
                              <label className="text-[9px] text-platinum-400 font-bold uppercase">Nome Step</label>
                              <input 
                                className="w-full bg-[#111] border border-white/10 rounded-sm p-2 text-xs text-white focus:border-diamond-500/50 outline-none"
                                value={selectedStep.label}
                                onChange={(e) => setSteps(prev => prev.map(s => s.id === selectedStep.id ? {...s, label: e.target.value} : s))}
                              />
                          </div>

                          {selectedStep.type === 'TRAFFIC' && (
                              <div className="grid grid-cols-2 gap-2">
                                  <div className="space-y-1">
                                      <label className="text-[9px] text-platinum-400 font-bold uppercase">Budget (€)</label>
                                      <input type="number" className="w-full bg-[#111] border border-white/10 rounded-sm p-2 text-xs text-white outline-none"
                                          value={selectedStep.config.budget || 0}
                                          onChange={(e) => updateStepConfig(selectedStep.id, 'budget', Number(e.target.value))}
                                      />
                                  </div>
                                  <div className="space-y-1">
                                      <label className="text-[9px] text-platinum-400 font-bold uppercase">CPC (€)</label>
                                      <input type="number" step="0.1" className="w-full bg-[#111] border border-white/10 rounded-sm p-2 text-xs text-white outline-none"
                                          value={selectedStep.config.cpc || 0}
                                          onChange={(e) => updateStepConfig(selectedStep.id, 'cpc', Number(e.target.value))}
                                      />
                                  </div>
                              </div>
                          )}

                          {['CHECKOUT', 'UPSELL'].includes(selectedStep.type) && (
                              <div className="space-y-2">
                                  <label className="text-[9px] text-platinum-400 font-bold uppercase">Prezzo Prodotto (€)</label>
                                  <input type="number" className="w-full bg-[#111] border border-white/10 rounded-sm p-2 text-xs text-white outline-none focus:border-green-500/50"
                                      value={selectedStep.config.price || 0}
                                      onChange={(e) => updateStepConfig(selectedStep.id, 'price', Number(e.target.value))}
                                  />
                              </div>
                          )}
                      </div>

                      {/* 2. PAGE DNA (COMPOSER) */}
                      {!['TRAFFIC', 'ACTION', 'LOGIC'].includes(selectedStep.type) && (
                          <div className="space-y-4">
                              <h4 className="text-[10px] font-bold text-purple-400 uppercase tracking-widest border-b border-white/5 pb-2">Page DNA (Elementi)</h4>
                              <div className="grid grid-cols-3 gap-2">
                                  {[
                                      {id: 'VIDEO', icon: Video, label: 'VSL'},
                                      {id: 'TEXT', icon: FileText, label: 'Copy'},
                                      {id: 'BUTTON', icon: MousePointer, label: 'CTA'},
                                      {id: 'TIMER', icon: Clock, label: 'Timer'},
                                      {id: 'TESTIMONIAL', icon: MessageSquare, label: 'Review'},
                                      {id: 'FAQ', icon: AlertTriangle, label: 'FAQ'},
                                  ].map(el => {
                                      const isActive = selectedStep.elements?.some(e => e.type === el.id);
                                      return (
                                          <button 
                                              key={el.id}
                                              onClick={() => togglePageElement(el.id as any)}
                                              className={`flex flex-col items-center justify-center p-2 rounded-sm border transition-all ${isActive ? 'bg-white/10 border-white/30 text-white' : 'bg-[#111] border-white/5 text-platinum-600 hover:text-white'}`}
                                          >
                                              <el.icon size={14} className="mb-1" />
                                              <span className="text-[8px] font-bold uppercase">{el.label}</span>
                                          </button>
                                      );
                                  })}
                              </div>
                          </div>
                      )}

                      {/* 3. SIMULATION & KPI */}
                      <div className="space-y-4">
                          <h4 className="text-[10px] font-bold text-yellow-400 uppercase tracking-widest border-b border-white/5 pb-2">Target & Simulation</h4>
                          
                          <div className="space-y-2">
                              <div className="flex justify-between">
                                  <label className="text-[9px] text-platinum-400 font-bold uppercase">Conversion Rate Atteso</label>
                                  <span className="text-[9px] text-white font-mono">{selectedStep.config.conversionGoal || 0}%</span>
                              </div>
                              <input 
                                  type="range" min="0" max="100" 
                                  className="w-full accent-yellow-500 h-1 bg-white/10 rounded-lg appearance-none cursor-pointer"
                                  value={selectedStep.config.conversionGoal || 0}
                                  onChange={(e) => {
                                      updateStepConfig(selectedStep.id, 'conversionGoal', Number(e.target.value));
                                      if(isSimulating) runSimulation(); // Live update
                                  }}
                              />
                          </div>

                          {isSimulating && (
                              <div className="bg-white/5 p-3 rounded-sm border border-white/5 space-y-2 font-mono text-[10px]">
                                  <div className="flex justify-between">
                                      <span className="text-platinum-500">Input:</span>
                                      <span className="text-white">{selectedStep.metrics.trafficIn} visitatori</span>
                                  </div>
                                  <div className="flex justify-between">
                                      <span className="text-platinum-500">Output:</span>
                                      <span className="text-white">{selectedStep.metrics.trafficOut} leads/buyers</span>
                                  </div>
                                  {selectedStep.metrics.revenue > 0 && (
                                      <div className="flex justify-between pt-2 border-t border-white/5">
                                          <span className="text-platinum-500">Revenue:</span>
                                          <span className="text-emerald-400 font-bold">€{selectedStep.metrics.revenue.toLocaleString()}</span>
                                      </div>
                                  )}
                              </div>
                          )}
                      </div>

                  </div>
              </>
          )}
      </div>

    </div>
  );
};