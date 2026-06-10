"use client";

import { Activity, Users, Server, Terminal, BookOpen, LayoutDashboard } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";

const NAV = [
  { label: "Dashboard", icon: LayoutDashboard, href: "/" },
  { label: "Lead Explorer", icon: Users, href: "/leads" },
  { label: "SMTP Accounts", icon: Server, href: "/accounts" },
  { label: "Terminal Logs", icon: Terminal, href: "/logs" },
  { label: "Guida", icon: BookOpen, href: "/guide" },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-60 shrink-0 hidden md:flex flex-col bg-ink-2 border-r border-white/[0.07] h-screen sticky top-0 z-50">
      {/* Logo */}
      <div className="px-6 py-7 border-b border-white/[0.07]">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl flex items-center justify-center shrink-0"
            style={{ background: "linear-gradient(135deg,#fb4604 0%,#ff8a4a 100%)", boxShadow: "0 8px 24px -8px rgba(251,70,4,0.6)" }}>
            <span className="text-white font-black text-sm">DE</span>
          </div>
          <div>
            <div className="text-[11px] font-black uppercase tracking-[0.22em] text-white/55">Digital Empire</div>
            <div className="text-sm font-black text-white leading-tight">Outreach CMD</div>
          </div>
        </div>
      </div>

      {/* Nav */}
      <nav className="flex-1 px-4 py-5 space-y-1">
        {NAV.map((item) => {
          const active = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm font-semibold transition-all duration-200 ${
                active
                  ? "bg-[#fb4604] text-white shadow-lg"
                  : "text-white/65 hover:text-white hover:bg-white/[0.07]"
              }`}
              style={active ? { boxShadow: "0 8px 24px -8px rgba(251,70,4,0.55)" } : {}}
            >
              <item.icon className={`w-4 h-4 shrink-0 ${active ? "text-white" : "text-white/55"}`} />
              {item.label}
            </Link>
          );
        })}
      </nav>

      {/* Status footer */}
      <div className="px-5 py-5 border-t border-white/[0.07] space-y-4">
        <div className="p-3.5 rounded-2xl bg-white/[0.04] border border-white/[0.07]">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[10px] font-black text-white/55 uppercase tracking-[0.2em]">System</span>
            <div className="flex items-center gap-1.5">
              <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
              <span className="text-[10px] font-black text-green-500">Online</span>
            </div>
          </div>
          <div className="w-full bg-white/[0.06] h-1 rounded-full overflow-hidden">
            <div className="h-full rounded-full" style={{ width: "98%", background: "linear-gradient(90deg,#fb4604,#ff8a4a)" }} />
          </div>
        </div>

        <div className="flex items-center gap-3 px-1">
          <div className="w-8 h-8 rounded-full bg-white/[0.07] border border-white/10 flex items-center justify-center">
            <Activity className="w-3.5 h-3.5 text-white/40" />
          </div>
          <div className="flex-1 min-w-0">
            <div className="text-xs font-bold text-white/80 truncate">max.infoproducer</div>
            <div className="text-[10px] text-white/50 truncate">Admin</div>
          </div>
        </div>
      </div>
    </aside>
  );
}
