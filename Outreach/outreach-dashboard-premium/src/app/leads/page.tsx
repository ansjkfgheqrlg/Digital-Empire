"use client";

import {
  Users, Search, Mail, MapPin, Phone, Download, Trash2, Filter, RefreshCw,
} from "lucide-react";
import { Reveal } from "@/components/reveal";
import { useState, useEffect, useCallback } from "react";

interface Lead {
  id: number; name: string; email: string;
  city: string; phone: string; niche: string; status: string;
}

const STATUS_STYLE: Record<string, string> = {
  Ready:  "bg-blue-500/15 border-blue-500/40 text-blue-300",
  Sent:   "bg-green-500/15 border-green-500/40 text-green-300",
  Failed: "bg-red-500/15 border-red-500/40 text-red-300",
};

export default function LeadExplorer() {
  const [leads, setLeads]         = useState<Lead[]>([]);
  const [search, setSearch]       = useState("");
  const [page, setPage]           = useState(1);
  const [total, setTotal]         = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading]     = useState(true);
  const LIMIT = 20;

  const fetchLeads = useCallback(async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams({ search, page: String(page), limit: String(LIMIT) });
      const res = await fetch(`/api/leads?${params}`);
      if (res.ok) {
        const data = await res.json();
        setLeads(data.leads); setTotal(data.total); setTotalPages(data.totalPages);
      }
    } catch {} finally { setLoading(false); }
  }, [search, page]);

  useEffect(() => { const t = setTimeout(fetchLeads, 300); return () => clearTimeout(t); }, [fetchLeads]);
  useEffect(() => { setPage(1); }, [search]);

  const exportCsv = () => {
    const rows = [["ID","Azienda","Email","Nicchia","Città","Telefono","Stato"], ...leads.map(l => [l.id,l.name,l.email,l.niche,l.city,l.phone,l.status])];
    const csv = rows.map(r => r.join(",")).join("\n");
    const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(new Blob([csv],{type:"text/csv"})), download: `leads-${new Date().toISOString().split("T")[0]}.csv` });
    a.click();
  };

  return (
    <div className="flex flex-col min-h-screen bg-ink">
      <header className="h-14 border-b border-white/[0.08] flex items-center justify-between px-8 bg-ink-2 sticky top-0 z-40 shrink-0">
        <div className="flex items-center gap-3">
          <Users className="w-4 h-4 text-[#fb4604]" />
          <span className="text-sm font-black text-white uppercase tracking-widest">Lead Explorer</span>
          <span className="text-[10px] text-white/50 font-bold">{total} records</span>
        </div>
        <div className="flex items-center gap-2">
          <button onClick={fetchLeads} className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white/[0.06] border border-white/[0.12] text-white/70 text-[10px] font-black uppercase tracking-widest hover:bg-white/10 transition-all">
            <RefreshCw className={`w-3 h-3 ${loading ? "animate-spin" : ""}`} />
          </button>
          <button onClick={exportCsv} className="flex items-center gap-2 px-4 py-1.5 rounded-xl bg-white/[0.06] border border-white/[0.12] text-white/70 text-[10px] font-black uppercase tracking-widest hover:bg-white/10 transition-all">
            <Download className="w-3.5 h-3.5" /> Export CSV
          </button>
        </div>
      </header>

      <div className="p-8 space-y-5">
        <Reveal>
          <div className="flex gap-3">
            <div className="relative flex-1">
              <Search className="w-4 h-4 absolute left-4 top-1/2 -translate-y-1/2 text-white/40" />
              <input type="text" placeholder="Cerca per nome, nicchia, città o email..."
                value={search} onChange={(e) => setSearch(e.target.value)}
                className="w-full bg-white/[0.05] border border-white/[0.12] rounded-2xl py-3 pl-12 pr-4 text-sm text-white/85 placeholder:text-white/30 focus:outline-none focus:border-white/30 transition-all" />
            </div>
            <button className="flex items-center gap-2 px-5 py-3 rounded-2xl bg-white/[0.05] border border-white/[0.12] text-white/70 text-[10px] font-black uppercase tracking-widest hover:bg-white/10 transition-all">
              <Filter className="w-3.5 h-3.5" /> Filtri
            </button>
          </div>
        </Reveal>

        <Reveal delay={0.05}>
          <div className="card-dark p-0 overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="text-[10px] font-black uppercase tracking-[0.18em] text-white/45 border-b border-white/[0.08] bg-white/[0.02]">
                    <th className="px-6 py-4">Azienda</th>
                    <th className="px-6 py-4">Email</th>
                    <th className="px-6 py-4">Nicchia</th>
                    <th className="px-6 py-4">Città</th>
                    <th className="px-6 py-4">Stato</th>
                    <th className="px-6 py-4 text-right">Azioni</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-white/[0.05]">
                  {loading ? (
                    <tr><td colSpan={6} className="px-6 py-12 text-center">
                      <div className="flex items-center justify-center gap-3 text-white/40 text-sm">
                        <RefreshCw className="w-4 h-4 animate-spin" /> Caricamento lead...
                      </div>
                    </td></tr>
                  ) : leads.length === 0 ? (
                    <tr><td colSpan={6} className="px-6 py-12 text-center text-white/40 text-sm">Nessun lead trovato</td></tr>
                  ) : leads.map((lead) => (
                    <tr key={lead.id} className="hover:bg-white/[0.03] transition-colors group">
                      <td className="px-6 py-4">
                        <div className="text-sm font-black text-white">{lead.name}</div>
                        <div className="text-[10px] text-white/40 font-bold mt-0.5 uppercase tracking-widest">DE-LEAD-{lead.id}</div>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-2 text-sm text-white/75 font-medium">
                          <Mail className="w-3.5 h-3.5 text-[#a78bfa]" /> {lead.email}
                        </div>
                        {lead.phone && <div className="flex items-center gap-2 text-[10px] text-white/40 mt-1"><Phone className="w-3 h-3" /> {lead.phone}</div>}
                      </td>
                      <td className="px-6 py-4"><div className="text-[11px] font-black text-white/80 uppercase tracking-widest">{lead.niche}</div></td>
                      <td className="px-6 py-4"><div className="flex items-center gap-1.5 text-[11px] text-white/60 font-bold"><MapPin className="w-3 h-3 text-white/40" /> {lead.city || "—"}</div></td>
                      <td className="px-6 py-4">
                        <span className={`px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest border ${STATUS_STYLE[lead.status] || STATUS_STYLE.Ready}`}>
                          {lead.status}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-right">
                        <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-all">
                          <button className="p-2 rounded-xl bg-white/[0.06] hover:bg-[#fb4604]/20 text-white/60 hover:text-[#fb4604] transition-all"><Mail className="w-3.5 h-3.5" /></button>
                          <button className="p-2 rounded-xl bg-white/[0.06] hover:bg-red-500/20 text-white/60 hover:text-red-400 transition-all"><Trash2 className="w-3.5 h-3.5" /></button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="px-6 py-4 border-t border-white/[0.06] bg-white/[0.02] flex items-center justify-between">
              <div className="text-[10px] font-black text-white/45 uppercase tracking-widest">
                {total > 0 ? `Pagina ${page} di ${totalPages} — ${total} records totali` : "Nessun record"}
              </div>
              <div className="flex gap-2">
                <button onClick={() => setPage(p => Math.max(1, p-1))} disabled={page <= 1}
                  className="px-4 py-2 rounded-xl bg-white/[0.05] border border-white/[0.1] text-white/60 text-[10px] font-black uppercase tracking-widest hover:text-white hover:border-white/25 transition-all disabled:opacity-30 disabled:cursor-not-allowed">Prec</button>
                <button onClick={() => setPage(p => Math.min(totalPages, p+1))} disabled={page >= totalPages}
                  className="px-4 py-2 rounded-xl bg-white/[0.05] border border-white/[0.1] text-white/60 text-[10px] font-black uppercase tracking-widest hover:text-white hover:border-white/25 transition-all disabled:opacity-30 disabled:cursor-not-allowed">Succ</button>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </div>
  );
}
