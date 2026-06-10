"use client";

import { useEffect, useRef, useState } from "react";
import { Terminal, Trash2, Circle } from "lucide-react";

function stripAnsi(str: string): string {
  // eslint-disable-next-line no-control-regex
  return str.replace(/\x1B\[[0-9;]*[mGKHFJsu]|\x1B\[[0-9;]*[A-Za-z]/g, "");
}

function lineStyle(line: string): { color: string; weight?: string } {
  const l = line.toLowerCase();
  if (l.includes("errore") || l.includes("error") || l.includes("[err]") || l.includes("✗") || l.includes("exit") && l.includes("1"))
    return { color: "#f87171" };
  if (l.includes("✓") || l.includes("completato") || l.includes("inviata") || l.includes("-> ok") || l.includes("fine -> ok"))
    return { color: "#4ade80" };
  if (l.includes("═") || l.includes("─") || l.includes("dashboard"))
    return { color: "rgba(255,255,255,0.12)", weight: "400" };
  if (l.includes("[email") || l.includes("email-gen") || l.includes("email-invia") || l.includes("[writer]") || l.includes("[qualifier]"))
    return { color: "#a78bfa" };
  if (l.includes("[ig") || l.includes("instagram") || l.includes("[dm]") || l.includes("fase"))
    return { color: "#fb923c" };
  if (l.includes("[linkedin") || l.includes("[comment") || l.includes("[connection]"))
    return { color: "#60a5fa" };
  if (l.includes("[extractor]") || l.includes("[scraper]") || l.includes("[maps]"))
    return { color: "#22d3ee" };
  if (l.includes("warn") || l.includes("attenzione") || l.includes("⚠"))
    return { color: "#fbbf24" };
  return { color: "rgba(255,255,255,0.55)" };
}

export function LiveTerminal() {
  const [lines, setLines] = useState<string[]>([]);
  const [connected, setConnected] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const esRef = useRef<EventSource | null>(null);

  const connect = () => {
    if (esRef.current) esRef.current.close();
    const es = new EventSource("/api/logs");
    esRef.current = es;
    es.onopen = () => setConnected(true);
    es.onerror = () => { setConnected(false); setTimeout(connect, 3000); };
    es.onmessage = (evt) => {
      try {
        const raw: string = JSON.parse(evt.data);
        const clean = stripAnsi(raw).trimEnd();
        if (clean) setLines((p) => [...p.slice(-799), clean]);
      } catch { /* skip */ }
    };
  };

  useEffect(() => {
    connect();
    return () => esRef.current?.close();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [lines]);

  return (
    <div className="flex flex-col h-full" style={{ background: "#080808" }}>
      {/* Header bar */}
      <div className="px-5 py-3.5 flex items-center justify-between border-b shrink-0"
        style={{ borderColor: "rgba(255,255,255,0.06)", background: "rgba(255,255,255,0.025)" }}>
        <div className="flex items-center gap-3">
          <Terminal className="w-3.5 h-3.5" style={{ color: "#fb4604" }} />
          <span className="text-[10px] font-black uppercase tracking-[0.22em]"
            style={{ color: "rgba(255,255,255,0.35)" }}>
            Live Console
          </span>
          {/* Connection dot */}
          <div className={`flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[9px] font-black uppercase tracking-widest ${
            connected
              ? "text-green-400 bg-green-400/10 border border-green-400/20"
              : "text-red-400/60 bg-red-400/5 border border-red-400/10"
          }`}>
            <Circle className={`w-1.5 h-1.5 fill-current ${connected ? "animate-pulse" : ""}`} />
            {connected ? "Live" : "Reconnecting"}
          </div>
        </div>
        <div className="flex items-center gap-4">
          <span className="text-[9px] font-mono" style={{ color: "rgba(255,255,255,0.15)" }}>
            {lines.length} ln
          </span>
          <button
            onClick={() => setLines([])}
            className="transition-colors"
            style={{ color: "rgba(255,255,255,0.2)" }}
            onMouseEnter={(e) => (e.currentTarget.style.color = "rgba(255,255,255,0.5)")}
            onMouseLeave={(e) => (e.currentTarget.style.color = "rgba(255,255,255,0.2)")}
            title="Clear"
          >
            <Trash2 className="w-3.5 h-3.5" />
          </button>
          {/* Traffic lights */}
          <div className="flex gap-1.5">
            <div className="w-2.5 h-2.5 rounded-full bg-red-500/60" />
            <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/60" />
            <div className="w-2.5 h-2.5 rounded-full bg-green-500/60" />
          </div>
        </div>
      </div>

      {/* Log output */}
      <div className="flex-1 overflow-y-auto p-5 font-mono text-[11.5px] leading-relaxed space-y-0.5 scrollbar-hide">
        {lines.length === 0 ? (
          <div className="flex items-center gap-2 mt-2" style={{ color: "rgba(255,255,255,0.18)" }}>
            <span className="text-[#fb4604]">❯</span>
            <span className="italic">In attesa di un processo da avviare...</span>
            <span className="animate-pulse">_</span>
          </div>
        ) : (
          lines.map((line, i) => {
            const { color, weight } = lineStyle(line);
            return (
              <div
                key={i}
                className="whitespace-pre-wrap break-all"
                style={{ color, fontWeight: weight ?? "400" }}
              >
                {line}
              </div>
            );
          })
        )}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}
