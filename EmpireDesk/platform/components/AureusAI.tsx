
import React, { useState, useRef, useEffect } from 'react';
import { Diamond, Send, X, Sparkles, Bot } from 'lucide-react';
import { Button } from './ui/Button';

export const AureusAI: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<{role: 'user' | 'ai', text: string}[]>([
      { role: 'ai', text: 'Benvenuto in Aureus Intelligence. Come posso ottimizzare la tua agenzia oggi?' }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages, isTyping]);

  const handleSend = async (e: React.FormEvent) => {
      e.preventDefault();
      if (!input.trim()) return;

      const userMsg = input;
      setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
      setInput('');
      setIsTyping(true);

      // Simulate AI Latency
      setTimeout(() => {
          let response = "Sto analizzando i dati...";
          if (userMsg.toLowerCase().includes('lead') || userMsg.toLowerCase().includes('vendit')) {
              response = "Analisi Pipeline: Ho rilevato 3 lead caldi in fase di 'Negoziazione'. Ti consiglio di inviare un follow-up con il case study 'E-commerce Fashion'. Vuoi che prepari una bozza?";
          } else if (userMsg.toLowerCase().includes('post') || userMsg.toLowerCase().includes('social')) {
              response = "Certamente. Ecco 3 idee per Reel basate sui trend attuali: \n1. '3 Errori fatali nel Dropshipping' (Hook visivo forte)\n2. 'Dietro le quinte dell'agenzia' (Vlog style)\n3. 'Risultati cliente: da 0 a 10k in 30 giorni'. Quale preferisci sviluppare?";
          } else {
              response = "Ricevuto. Sto elaborando la richiesta incrociando i dati finanziari e operativi del sistema Aureus.";
          }
          
          setIsTyping(false);
          setMessages(prev => [...prev, { role: 'ai', text: response }]);
      }, 1500);
  };

  return (
    <div className="fixed bottom-8 right-8 z-50 flex flex-col items-end">
        {/* Chat Window */}
        {isOpen && (
            <div className="mb-4 w-96 h-[500px] bg-[#050505]/95 backdrop-blur-xl border border-diamond-500/30 rounded-lg shadow-[0_0_50px_rgba(34,211,238,0.15)] flex flex-col overflow-hidden animate-in slide-in-from-bottom-5 duration-300 origin-bottom-right">
                {/* Header */}
                <div className="p-4 border-b border-white/10 bg-gradient-to-r from-diamond-950/50 to-transparent flex justify-between items-center">
                    <div className="flex items-center gap-2">
                        <Sparkles className="w-4 h-4 text-diamond-400 animate-pulse" />
                        <span className="font-bold text-white text-sm tracking-wide">AUREUS INTELLIGENCE</span>
                    </div>
                    <button onClick={() => setIsOpen(false)} className="text-platinum-500 hover:text-white"><X className="w-4 h-4"/></button>
                </div>

                {/* Messages */}
                <div className="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar bg-[radial-gradient(circle_at_center,rgba(34,211,238,0.03),transparent)]">
                    {messages.map((msg, idx) => (
                        <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                            <div className={`
                                max-w-[85%] p-3 text-xs leading-relaxed rounded-lg 
                                ${msg.role === 'user' 
                                    ? 'bg-white/10 text-white rounded-br-none border border-white/5' 
                                    : 'bg-diamond-950/40 text-platinum-100 rounded-bl-none border border-diamond-500/20 shadow-[0_0_10px_rgba(34,211,238,0.05)]'}
                            `}>
                                {msg.text.split('\n').map((line, i) => <p key={i} className="mb-1 last:mb-0">{line}</p>)}
                            </div>
                        </div>
                    ))}
                    {isTyping && (
                        <div className="flex justify-start">
                             <div className="bg-diamond-950/40 border border-diamond-500/20 p-3 rounded-lg rounded-bl-none flex items-center gap-1">
                                 <div className="w-1.5 h-1.5 bg-diamond-400 rounded-full animate-bounce"></div>
                                 <div className="w-1.5 h-1.5 bg-diamond-400 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                                 <div className="w-1.5 h-1.5 bg-diamond-400 rounded-full animate-bounce [animation-delay:0.4s]"></div>
                             </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>

                {/* Input */}
                <form onSubmit={handleSend} className="p-3 border-t border-white/10 bg-[#0A0A0A]">
                    <div className="relative">
                        <input 
                            className="w-full bg-[#111] border border-white/10 rounded-full pl-4 pr-10 py-3 text-xs text-white placeholder:text-neutral-500 focus:border-diamond-500/50 outline-none shadow-inner"
                            placeholder="Chiedi ad Aureus..."
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                        />
                        <button type="submit" className="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 bg-diamond-500 text-black rounded-full hover:bg-white transition-colors">
                            <Send className="w-3 h-3" />
                        </button>
                    </div>
                </form>
            </div>
        )}

        {/* Toggle Button */}
        <button 
            onClick={() => setIsOpen(!isOpen)}
            className={`
                group relative flex items-center justify-center w-14 h-14 rounded-full transition-all duration-300 shadow-[0_0_20px_rgba(0,0,0,0.5)]
                ${isOpen ? 'bg-[#111] border border-white/20 rotate-90' : 'bg-gradient-to-br from-diamond-400 to-diamond-600 hover:scale-110'}
            `}
        >
            {isOpen ? <X className="w-6 h-6 text-white" /> : <Bot className="w-7 h-7 text-black fill-current" />}
            
            {/* Ping Effect */}
            {!isOpen && (
                <span className="absolute -top-1 -right-1 flex h-3 w-3">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-3 w-3 bg-white"></span>
                </span>
            )}
        </button>
    </div>
  );
};
