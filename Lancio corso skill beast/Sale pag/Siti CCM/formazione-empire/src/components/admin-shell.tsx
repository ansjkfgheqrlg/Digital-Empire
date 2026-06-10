"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import Wordmark from "./wordmark";
import { cn } from "@/lib/utils";
import type { ReactNode } from "react";

const navItems = [
  { href: "/admin", label: "Dashboard", icon: "dashboard" },
  { href: "/admin/corsi", label: "Corsi", icon: "book" },
  { href: "/admin/studenti", label: "Studenti", icon: "users" },
  { href: "/admin/risorse", label: "Risorse", icon: "file" },
  { href: "/admin/impostazioni", label: "Impostazioni", icon: "settings" },
];

function NavIcon({ name }: { name: string }) {
  const p = { width: 18, height: 18, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const };
  switch (name) {
    case "dashboard": return <svg {...p}><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>;
    case "book": return <svg {...p}><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>;
    case "users": return <svg {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>;
    case "file": return <svg {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>;
    case "settings": return <svg {...p}><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>;
    default: return null;
  }
}

export default function AdminShell({ children, title, subtitle, actions }: { children: ReactNode; title: string; subtitle?: string; actions?: ReactNode }) {
  const pathname = usePathname();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen grid lg:grid-cols-[280px_1fr]" style={{ background: "#1c1c1c" }}>
      {/* Sidebar */}
      <aside
        className={cn(
          "fixed lg:static inset-y-0 left-0 z-50 w-[280px] flex flex-col transition-transform duration-300 border-r",
          sidebarOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"
        )}
        style={{ background: "#141414", borderColor: "rgba(249,249,249,0.08)" }}
      >
        <div className="p-6 border-b" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
          <Wordmark size="sm" href="/admin" />
          <div className="mt-2 flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604", boxShadow: "0 0 8px rgba(251,70,4,0.6)" }} />
            <span className="text-xs uppercase tracking-widest font-semibold" style={{ color: "#ff8a4a" }}>Area Admin</span>
          </div>
        </div>

        <nav className="flex-1 p-4 flex flex-col gap-1 overflow-auto">
          {navItems.map((item) => {
            const active = item.href === "/admin" ? pathname === "/admin" : pathname.startsWith(item.href);
            return (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => setSidebarOpen(false)}
                className={`nav-item ${active ? "active" : ""}`}
              >
                <NavIcon name={item.icon} />
                <span>{item.label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="p-4 border-t" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2 rounded-lg text-sm" style={{ color: "rgba(249,249,249,0.7)" }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M19 12H5"/><polyline points="12 19 5 12 12 5"/></svg>
            Torna al sito
          </Link>
        </div>
      </aside>

      {sidebarOpen && (
        <div className="fixed inset-0 z-40 bg-black/60 lg:hidden" onClick={() => setSidebarOpen(false)} />
      )}

      {/* Main */}
      <main className="min-h-screen">
        <header className="sticky top-0 z-30 border-b" style={{ background: "rgba(26,26,26,0.92)", backdropFilter: "blur(12px)", borderColor: "rgba(249,249,249,0.08)" }}>
          <div className="flex items-center gap-4 px-6 md:px-10 py-5">
            <button
              className="lg:hidden w-10 h-10 rounded-lg flex items-center justify-center"
              style={{ background: "rgba(249,249,249,0.06)", border: "1px solid rgba(249,249,249,0.1)" }}
              onClick={() => setSidebarOpen(true)}
              aria-label="Menu"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f9f9f9" strokeWidth="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            </button>
            <div className="flex-1 min-w-0">
              <h1 className="text-xl md:text-2xl font-extrabold tracking-tight truncate" style={{ color: "#f9f9f9" }}>
                {title}
              </h1>
              {subtitle && <p className="text-sm mt-0.5 truncate" style={{ color: "rgba(249,249,249,0.6)" }}>{subtitle}</p>}
            </div>
            {actions && <div className="flex items-center gap-2">{actions}</div>}
          </div>
        </header>

        <div className="p-6 md:p-10 max-w-6xl">
          {children}
        </div>
      </main>
    </div>
  );
}
