"use client";

import { useState } from "react";
import { Menu, X, LayoutDashboard, Users, Server, Terminal, BookOpen } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";

const NAV = [
  { label: "Dashboard",      icon: LayoutDashboard, href: "/"         },
  { label: "Lead Explorer",  icon: Users,            href: "/leads"    },
  { label: "SMTP Accounts",  icon: Server,           href: "/accounts" },
  { label: "Terminal Logs",  icon: Terminal,         href: "/logs"     },
  { label: "Guida",          icon: BookOpen,         href: "/guide"    },
];

export function MobileNav() {
  const [open, setOpen] = useState(false);
  const pathname = usePathname();

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="md:hidden fixed top-4 left-4 z-[200] w-10 h-10 rounded-xl flex items-center justify-center"
        style={{ background: "#111111", border: "1px solid rgba(255,255,255,0.1)", boxShadow: "0 4px 16px rgba(0,0,0,0.5)" }}
      >
        <Menu className="w-5 h-5 text-white/70" />
      </button>

      {open && (
        <div className="md:hidden fixed inset-0 z-[199] bg-black/60 backdrop-blur-sm" onClick={() => setOpen(false)} />
      )}

      <div
        className={`md:hidden fixed top-0 left-0 h-full w-72 z-[200] flex flex-col transition-transform duration-300 ${open ? "translate-x-0" : "-translate-x-full"}`}
        style={{ background: "#111111", borderRight: "1px solid rgba(255,255,255,0.07)" }}
      >
        <div className="px-6 py-6 border-b border-white/[0.07] flex items-center justify-between">
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
          <button onClick={() => setOpen(false)} className="p-1.5 rounded-lg text-white/40 hover:text-white transition-colors">
            <X className="w-4 h-4" />
          </button>
        </div>

        <nav className="flex-1 px-4 py-5 space-y-1 overflow-y-auto">
          {NAV.map((item) => {
            const active = pathname === item.href;
            return (
              <Link key={item.href} href={item.href} onClick={() => setOpen(false)}
                className={`flex items-center gap-3 px-3.5 py-3 rounded-xl text-sm font-semibold transition-all duration-200 ${active ? "bg-[#fb4604] text-white" : "text-white/65 hover:text-white hover:bg-white/[0.07]"}`}
                style={active ? { boxShadow: "0 8px 24px -8px rgba(251,70,4,0.55)" } : {}}>
                <item.icon className={`w-4 h-4 shrink-0 ${active ? "text-white" : "text-white/55"}`} />
                {item.label}
              </Link>
            );
          })}
        </nav>

        <div className="px-5 py-5 border-t border-white/[0.07]">
          <div className="flex items-center gap-3 px-1">
            <div className="w-8 h-8 rounded-full bg-white/[0.07] border border-white/10 flex items-center justify-center">
              <span className="text-white/60 text-xs font-black">M</span>
            </div>
            <div>
              <div className="text-xs font-bold text-white/80">max.infoproducer</div>
              <div className="text-[10px] text-white/50">Admin</div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
