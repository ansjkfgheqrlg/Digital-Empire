"use client";

import { Send, Bot } from "lucide-react";
import { useState } from "react";

interface Message { role: "user" | "bot"; content: string; }

export function Chat() {
  const [messages, setMessages] = useState<Message[]>([
    { role: "bot", content: "Ciao! Sono il tuo assistente Outreach. Come posso aiutarti oggi?" },
    { role: "bot", content: "Tutti i task per domani sono già pronti. Batch 5 e 6 inizieranno alle 09:30." },
  ]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    const userMsg: Message = { role: "user", content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput("");
    setTimeout(() => {
      setMessages(prev => [...prev, { role: "bot", content: "Ricevuto. Sto analizzando la tua richiesta per ottimizzare il flusso." }]);
    }, 1000);
  };

  return (
    <div className="flex flex-col h-[500px] rounded-[20px] overflow-hidden"
      style={{ background: "#0d0d0d", border: "1px solid rgba(255,255,255,0.08)" }}>
      <div className="px-5 py-4 border-b shrink-0 flex items-center gap-2"
        style={{ borderColor: "rgba(255,255,255,0.07)", background: "rgba(255,255,255,0.025)" }}>
        <Bot className="w-4 h-4 text-[#fb4604]" />
        <span className="text-xs font-black uppercase tracking-widest text-white/70">Workflow Chat</span>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4 scrollbar-hide">
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`max-w-[80%] p-3 rounded-2xl text-xs leading-relaxed ${
              m.role === "user"
                ? "text-white"
                : "text-white/70"
            }`}
              style={m.role === "user"
                ? { background: "linear-gradient(135deg,#fb4604 0%,#ff8a4a 100%)" }
                : { background: "rgba(255,255,255,0.05)", border: "1px solid rgba(255,255,255,0.08)" }
              }>
              {m.content}
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 border-t shrink-0" style={{ borderColor: "rgba(255,255,255,0.07)", background: "#0a0a0a" }}>
        <div className="relative">
          <input
            type="text"
            placeholder="Chiedi al flusso..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="w-full bg-white/[0.05] border border-white/[0.1] rounded-xl py-2.5 pl-4 pr-12 text-xs text-white/80 placeholder:text-white/30 focus:outline-none focus:border-white/25 transition-all"
          />
          <button onClick={handleSend}
            className="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 rounded-lg text-white transition-opacity hover:opacity-80"
            style={{ background: "linear-gradient(135deg,#fb4604 0%,#ff8a4a 100%)" }}>
            <Send className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
}
