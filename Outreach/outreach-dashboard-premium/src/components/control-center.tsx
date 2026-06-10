"use client";

import { useState, useEffect, useCallback } from "react";
import { Mail, Camera, BriefcaseBusiness, Zap, Play, Square, Loader2, CheckCircle2, XCircle, Clock, ArrowRight } from "lucide-react";

type Mode = "email" | "instagram" | "linkedin" | "email+instagram" | "all";
type Status = "idle" | "running" | "done" | "error";

interface StatsData {
  process: { mode: string; status: Status; startTime: string | null; exitCode: number | null };
  stats: {
    email: { sent: number; total: number };
    ig: { dmToday: number; f1Today: number; total: number };
  };
}

const MODES: {
  id: Mode; label: string; sub: string;
  icon: React.ElementType; accent: string; glow: string;
}[] = [
  { id: "email",           label: "Email",             sub: "Scraping → Qualifier → Writer → Invio",    icon: Mail,            accent: "from-violet-500 to-purple-600", glow: "rgba(139,92,246,0.4)" },
  { id: "instagram",       label: "Instagram",          sub: "Scout → Qualifier → DM → Follow-up",       icon: Camera,          accent: "from-orange-500 to-red-500",    glow: "rgba(251,70,4,0.45)" },
  { id: "linkedin",        label: "LinkedIn",           sub: "Commenti + Connessioni + Messaggi",         icon: BriefcaseBusiness,accent: "from-blue-500 to-cyan-500",     glow: "rgba(59,130,246,0.4)" },
  { id: "email+instagram", label: "Email + Instagram",  sub: "Entrambe le catene in parallelo",           icon: Zap,             accent: "from-yellow-400 to-orange-500", glow: "rgba(251,191,36,0.4)" },
  { id: "all",             label: "Tutto — Full Stack", sub: "LinkedIn · Email · Instagram in simultanea", icon: Play,            accent: "from-green-500 to-emerald-400", glow: "rgba(34,197,94,0.4)" },
];

const TARGETS = [50, 100, 150, 200, 300];

export function ControlCenter() {
  const [data, setData] = useState<StatsData | null>(null);
  const [target, setTarget] = useState(150);
  const [launching, setLaunching] = useState<Mode | null>(null);

  const fetchStatus = useCallback(async () => {
    try {
      const res = await fetch("/api/status");
      if (res.ok) setData(await res.json());
    } catch { /* silent */ }
  }, []);

  useEffect(() => {
    fetchStatus();
    const id = setInterval(fetchStatus, 3000);
    return () => clearInterval(id);
  }, [fetchStatus]);

  const status: Status = data?.process.status ?? "idle";
  const activeMode = data?.process.mode ?? "";
  const isRunning = status === "running";

  const launch = async (mode: Mode) => {
    if (isRunning) return;
    setLaunching(mode);
    try {
      await fetch("/api/launch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mode, target }),
      });
      await fetchStatus();
    } finally {
      setLaunching(null);
    }
  };

  const stop = async () => {
    await fetch("/api/stop", { method: "POST" });
    await fetchStatus();
  };

  const StatusConfig = {
    idle:    { icon: Clock,        color: "text-white/55",  bg: "bg-white/[0.04]",   label: "Inattivo — pronto al lancio" },
    running: { icon: Loader2,      color: "text-[#fb4604]", bg: "bg-[#fb4604]/10",   label: "In esecuzione..." },
    done:    { icon: CheckCircle2, color: "text-green-400", bg: "bg-green-400/10",   label: "Completato con successo" },
    error:   { icon: XCircle,      color: "text-red-400",   bg: "bg-red-400/10",     label: "Errore — controlla i log" },
  }[status];

  const StatusIcon = StatusConfig.icon;

  return (
    <div className="space-y-5">

      {/* ── STATUS BAR ─────────────────────────────────────────────── */}
      <div className={`flex items-center justify-between px-4 py-3.5 rounded-2xl border border-white/[0.12] ${StatusConfig.bg}`}>
        <div className="flex items-center gap-3">
          <StatusIcon className={`w-5 h-5 shrink-0 ${StatusConfig.color} ${isRunning ? "animate-spin" : ""}`} />
          <div>
            <div className={`text-sm font-black ${StatusConfig.color}`}>
              {StatusConfig.label}
            </div>
            {activeMode && (
              <div className="text-[11px] text-white/60 font-bold mt-0.5">
                {activeMode.replace("+", " + ").toUpperCase()}
              </div>
            )}
          </div>
        </div>
        {isRunning && (
          <button
            onClick={stop}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-red-500/15 border border-red-500/40 text-red-300 text-xs font-black uppercase tracking-widest hover:bg-red-500/25 transition-all"
          >
            <Square className="w-3 h-3 fill-current" /> Stop
          </button>
        )}
      </div>

      {/* ── TARGET EMAIL ───────────────────────────────────────────── */}
      <div>
        <div className="text-[11px] font-black text-white/60 uppercase tracking-[0.2em] mb-2.5">
          Target Email
        </div>
        <div className="flex gap-2">
          {TARGETS.map((t) => (
            <button
              key={t}
              onClick={() => setTarget(t)}
              className={`flex-1 py-2 rounded-xl text-xs font-black transition-all border ${
                target === t
                  ? "text-white border-transparent"
                  : "border-white/20 text-white/60 hover:border-white/40 hover:text-white/85"
              }`}
              style={target === t ? {
                background: "linear-gradient(135deg,#fb4604 0%,#ff8a4a 100%)",
                boxShadow: "0 8px 24px -8px rgba(251,70,4,0.5)",
              } : {}}
            >
              {t}
            </button>
          ))}
        </div>
      </div>

      {/* ── LAUNCH BUTTONS ─────────────────────────────────────────── */}
      <div className="space-y-2">
        {MODES.map((m) => {
          const Icon = m.icon;
          const isActive = isRunning && activeMode === m.id;
          const isLoading = launching === m.id;
          const disabled = isRunning || !!launching;

          return (
            <button
              key={m.id}
              onClick={() => launch(m.id)}
              disabled={disabled}
              className={`w-full flex items-center gap-4 px-4 py-3.5 rounded-2xl border text-left transition-all duration-300 ${
                disabled && !isActive ? "opacity-40 cursor-not-allowed" : "cursor-pointer"
              } ${
                isActive
                  ? "border-[#fb4604]/60 bg-[#fb4604]/12"
                  : "border-white/[0.12] bg-white/[0.04] hover:bg-white/[0.08] hover:border-white/25"
              }`}
            >
              {/* Icona colorata */}
              <div
                className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 bg-gradient-to-br ${m.accent}`}
                style={{ boxShadow: `0 6px 18px -6px ${m.glow}` }}
              >
                {isLoading
                  ? <Loader2 className="w-4 h-4 text-white animate-spin" />
                  : <Icon className="w-4 h-4 text-white" />
                }
              </div>

              {/* Testo */}
              <div className="flex-1 min-w-0">
                <div className="text-sm font-black text-white leading-tight">{m.label}</div>
                <div className="text-[11px] text-white/55 font-medium mt-0.5">{m.sub}</div>
              </div>

              {/* Badge stato */}
              {isActive ? (
                <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-[#fb4604]/25 border border-[#fb4604]/50 shrink-0">
                  <div className="w-1.5 h-1.5 rounded-full bg-[#fb4604] animate-pulse" />
                  <span className="text-[9px] font-black text-[#ff8a4a] uppercase tracking-widest">Live</span>
                </div>
              ) : (
                <ArrowRight className="w-4 h-4 text-white/35 shrink-0" />
              )}
            </button>
          );
        })}
      </div>

      {/* ── MINI STATS ─────────────────────────────────────────────── */}
      {data && (
        <div className="grid grid-cols-3 gap-2 pt-1">
          {[
            { label: "Email oggi", value: data.stats.email.sent,   accent: "#a78bfa" },
            { label: "IG DM oggi", value: data.stats.ig.dmToday,   accent: "#fb4604" },
            { label: "Lead DB",    value: data.stats.ig.total,     accent: "#60a5fa" },
          ].map((s) => (
            <div
              key={s.label}
              className="py-3.5 px-3 text-center rounded-2xl"
              style={{
                background: "linear-gradient(135deg, #ffffff 0%, #f4f1f7 60%, #e0dbe8 100%)",
                border: "1px solid rgba(255,255,255,0.85)",
                boxShadow: "0 8px 24px -8px rgba(0,0,0,0.45), 0 2px 0 rgba(255,255,255,0.9) inset",
              }}
            >
              <div className="text-2xl font-black" style={{ color: s.accent }}>{s.value}</div>
              <div className="text-[9px] font-black uppercase tracking-wider mt-1 leading-tight" style={{ color: "#333333" }}>{s.label}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
