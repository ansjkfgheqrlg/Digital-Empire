"use client";

import { Server, Shield, Plus, Trash2, RefreshCw, CheckCircle2, XCircle, RotateCw } from "lucide-react";
import { Reveal } from "@/components/reveal";

const ACCOUNTS = [
  { id: 1, email: "max.infoproducer@gmail.com",  status: "Throttled", limit: 100, sent: 100, health: 12 },
  { id: 2, email: "agency.outreach@gmail.com",    status: "Active",    limit: 100, sent: 34,  health: 98 },
  { id: 3, email: "marketing.node@gmail.com",     status: "Active",    limit: 100, sent: 12,  health: 100 },
];

export default function AccountsPage() {
  const totalSent    = ACCOUNTS.reduce((s, a) => s + a.sent, 0);
  const totalLimit   = ACCOUNTS.reduce((s, a) => s + a.limit, 0);
  const activeCount  = ACCOUNTS.filter(a => a.status === "Active").length;
  const throttledList = ACCOUNTS.filter(a => a.status === "Throttled");
  const clusterPct   = Math.round((totalSent / totalLimit) * 100);

  return (
    <div className="flex flex-col min-h-screen bg-ink">

      {/* Header */}
      <header className="h-14 border-b border-white/[0.08] flex items-center justify-between px-8 bg-ink-2 sticky top-0 z-40 shrink-0">
        <div className="flex items-center gap-3">
          <Server className="w-4 h-4 text-[#fb4604]" />
          <span className="text-sm font-black text-white uppercase tracking-widest">SMTP Accounts</span>
        </div>
        <div className="flex items-center gap-2">
          <button onClick={() => window.location.reload()} className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white/[0.06] border border-white/[0.12] text-white/60 text-[10px] font-black uppercase tracking-widest hover:bg-white/10 transition-all">
            <RotateCw className="w-3 h-3" />
          </button>
          <button className="flex items-center gap-2 px-4 py-1.5 rounded-xl bg-[#fb4604]/15 border border-[#fb4604]/40 text-[#ff8a4a] text-[10px] font-black uppercase tracking-widest hover:bg-[#fb4604]/25 transition-all">
            <Plus className="w-3 h-3" /> Aggiungi Account
          </button>
        </div>
      </header>

      <div className="p-8 space-y-5">

        {/* Summary stats */}
        <Reveal>
          <div className="grid grid-cols-3 gap-4">
            {[
              { label: "Email Inviate Oggi", value: totalSent,  accent: "#fb4604" },
              { label: "Capacità Giornaliera", value: totalLimit, accent: "#60a5fa" },
              { label: "Account Attivi",     value: ACCOUNTS.filter(a => a.status === "Active").length, accent: "#4ade80" },
            ].map((s) => (
              <div
                key={s.label}
                className="py-5 px-4 text-center rounded-[20px]"
                style={{
                  background: "linear-gradient(135deg, #ffffff 0%, #f4f1f7 55%, #e0dbe8 100%)",
                  border: "1px solid rgba(255,255,255,0.85)",
                  boxShadow: "0 16px 40px -16px rgba(0,0,0,0.45), 0 2px 0 rgba(255,255,255,0.9) inset",
                }}
              >
                <div className="text-3xl font-black" style={{ color: s.accent }}>{s.value}</div>
                <div className="text-[10px] uppercase font-black tracking-wider mt-2" style={{ color: "#333333" }}>{s.label}</div>
              </div>
            ))}
          </div>
        </Reveal>

        {/* Account cards */}
        <div className="space-y-3">
          {ACCOUNTS.map((acc, i) => {
            const isThrottled = acc.status === "Throttled";
            const pct = Math.round((acc.sent / acc.limit) * 100);

            return (
              <Reveal key={acc.id} delay={i * 0.06}>
                <div className="card-dark flex items-center gap-6" style={{ padding: "1.25rem 1.5rem" }}>

                  {/* Icon */}
                  <div className={`w-11 h-11 rounded-2xl flex items-center justify-center shrink-0 ${
                    isThrottled ? "bg-red-500/15" : "bg-green-500/15"
                  }`}>
                    <Server className={`w-5 h-5 ${isThrottled ? "text-red-400" : "text-green-400"}`} />
                  </div>

                  {/* Email + status */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-sm font-black text-white truncate">{acc.email}</span>
                      <span className={`px-2.5 py-0.5 rounded-full text-[9px] font-black uppercase tracking-widest border shrink-0 ${
                        isThrottled
                          ? "bg-red-500/15 border-red-500/40 text-red-300"
                          : "bg-green-500/15 border-green-500/40 text-green-300"
                      }`}>
                        {acc.status}
                      </span>
                    </div>

                    {/* Progress bar */}
                    <div className="flex items-center gap-3">
                      <div className="flex-1 bg-white/[0.07] h-1.5 rounded-full overflow-hidden">
                        <div
                          className="h-full rounded-full transition-all"
                          style={{
                            width: `${pct}%`,
                            background: isThrottled
                              ? "linear-gradient(90deg,#ef4444,#f87171)"
                              : "linear-gradient(90deg,#fb4604,#ff8a4a)",
                          }}
                        />
                      </div>
                      <span className="text-[10px] font-black text-white/60 shrink-0">{acc.sent}/{acc.limit}</span>
                    </div>
                  </div>

                  {/* Health */}
                  <div className="flex items-center gap-2 shrink-0">
                    <Shield className={`w-4 h-4 ${acc.health > 80 ? "text-green-400" : "text-red-400"}`} />
                    <span className={`text-sm font-black ${acc.health > 80 ? "text-green-400" : "text-red-400"}`}>
                      {acc.health}%
                    </span>
                    <span className="text-[10px] text-white/45 font-bold">salute</span>
                  </div>

                  {/* Actions */}
                  <div className="flex gap-2 shrink-0">
                    <button className="px-3 py-1.5 rounded-xl bg-white/[0.06] border border-white/[0.1] text-white/65 text-[10px] font-black uppercase hover:bg-white/10 hover:text-white transition-all">Log</button>
                    <button className="p-2 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 hover:bg-red-500 hover:text-white transition-all">
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              </Reveal>
            );
          })}
        </div>

        {/* Cluster health */}
        <Reveal delay={0.3}>
          <div className="card-dark text-center py-8" style={{ padding: "2rem" }}>
            <div className="flex items-center justify-center gap-3 mb-4">
              <RefreshCw className="w-5 h-5 text-[#fb4604]" />
              <h2 className="text-lg font-black text-white">Global Cluster Health</h2>
            </div>
            <p className="text-white/65 text-sm max-w-md mx-auto mb-5 leading-relaxed">
              Il cluster opera al{" "}
              <strong className="text-white">{clusterPct}%</strong>.
              {throttledList.length > 0 && (
                <> Account{" "}
                  {throttledList.map(a => (
                    <span key={a.email} className="text-red-400 font-black">{a.email}</span>
                  ))}{" "}
                  {throttledList.length === 1 ? "ha raggiunto" : "hanno raggiunto"} il limite giornaliero.
                </>
              )}
              {throttledList.length === 0 && " Tutti gli account sono operativi."}
            </p>
            <div className="flex items-center justify-center gap-6">
              <div className="flex items-center gap-2 text-xs font-black text-green-400 uppercase tracking-widest">
                <CheckCircle2 className="w-3.5 h-3.5" /> {activeCount} {activeCount === 1 ? "attivo" : "attivi"}
              </div>
              <div className="flex items-center gap-2 text-xs font-black text-red-400 uppercase tracking-widest">
                <XCircle className="w-3.5 h-3.5" /> {throttledList.length} throttled
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </div>
  );
}
