"use client";

import { Mail, TrendingUp, Zap, Shield, Database, Activity } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { ControlCenter } from "@/components/control-center";
import { LiveTerminal } from "@/components/live-terminal";
import { useState, useEffect } from "react";

interface DashStats { emailSent: number; igDm: number; leadDb: number; channels: number; }

export default function Page() {
  const [stats, setStats] = useState<DashStats>({ emailSent: 0, igDm: 0, leadDb: 0, channels: 3 });

  useEffect(() => {
    fetch("/api/status")
      .then(r => r.ok ? r.json() : null)
      .then(data => {
        if (data?.stats) {
          setStats({
            emailSent: data.stats.email?.sent  || 0,
            igDm:      data.stats.ig?.dmToday  || 0,
            leadDb:    data.stats.ig?.total    || 0,
            channels:  3,
          });
        }
      })
      .catch(() => {});
  }, []);
  return (
    <div className="flex flex-col min-h-screen">

      {/* ── HERO / HEADER ──────────────────────────────────────────── */}
      <section className="bg-ink-2 px-8 pt-10 pb-8 relative overflow-hidden">

        {/* Marquee border */}
        <div className="absolute top-0 inset-x-0 h-px overflow-hidden opacity-40">
          <div className="marquee flex whitespace-nowrap">
            {Array(12).fill("EMAIL · INSTAGRAM · LINKEDIN · OUTREACH · DIGITAL EMPIRE · ").map((t, i) => (
              <span key={i} className="text-[10px] font-black tracking-[0.3em] uppercase px-6"
                style={{ color: "#fb4604" }}>{t}</span>
            ))}
          </div>
        </div>

        {/* Corner brackets decorative */}
        <div className="corner-bracket corner-tl" />
        <div className="corner-bracket corner-tr" />

        <Reveal delay={0}>
          <div className="pre-headline mb-4 mt-3">Operational Engine v3.0</div>
        </Reveal>

        <Reveal delay={0.08}>
          <h1 className="text-6xl font-black tracking-[-0.03em] leading-[1.0] mb-4">
            <span className="text-silver-white">Outreach</span>
            <br />
            <span className="text-silver-orange">Dashboard.</span>
          </h1>
        </Reveal>

        <Reveal delay={0.15}>
          <p className="text-white/70 text-base font-medium max-w-md leading-relaxed">
            Avvia, monitora e controlla tutti i flussi di outreach da un solo punto.{" "}
            <strong className="text-white/90">Email · Instagram · LinkedIn.</strong>
          </p>
        </Reveal>

        {/* Stat chips */}
        <Reveal delay={0.22}>
          <div className="flex flex-wrap gap-3 mt-7">
            {[
              { icon: Mail,     label: "Email",   val: String(stats.emailSent), sub: "oggi"    },
              { icon: Activity, label: "IG DM",    val: String(stats.igDm),     sub: "oggi"    },
              { icon: Database, label: "Lead DB",  val: String(stats.leadDb),   sub: "totali"  },
              { icon: Zap,      label: "Canali",   val: String(stats.channels), sub: "attivi"  },
            ].map((chip) => (
              <div
                key={chip.label}
                className="inline-flex items-center gap-2.5 px-4 py-2.5 rounded-2xl"
                style={{
                  background: "linear-gradient(135deg, #ffffff 0%, #f4f1f7 55%, #e0dbe8 100%)",
                  border: "1px solid rgba(255,255,255,0.85)",
                  boxShadow: "0 12px 32px -12px rgba(0,0,0,0.5), 0 2px 0 rgba(255,255,255,0.9) inset",
                }}
              >
                <div style={{ width: 7, height: 7, borderRadius: "50%", background: "#fb4604", boxShadow: "0 0 8px rgba(251,70,4,0.7)", flexShrink: 0 }} />
                <chip.icon className="w-3.5 h-3.5 shrink-0" style={{ color: "#444444" }} />
                <span className="font-bold text-[11px]" style={{ color: "#222222" }}>{chip.label}</span>
                <strong style={{ color: "#fb4604", fontWeight: 700 }}>{chip.val}</strong>
                <span className="text-[10px] font-semibold" style={{ color: "#555555" }}>{chip.sub}</span>
              </div>
            ))}
          </div>
        </Reveal>
      </section>

      {/* ── COMMAND CENTER ─────────────────────────────────────────── */}
      <section className="bg-ink px-8 py-8 flex-1">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

          {/* Launch Control Panel */}
          <Reveal delay={0.05} className="lg:col-span-5">
            <div className="card-dark h-full" style={{ padding: "1.75rem" }}>
              <div className="flex items-center gap-2 mb-5">
                <div className="bubble-orange text-xs">
                  <Zap className="w-3 h-3" /> Launch Control
                </div>
              </div>
              <ControlCenter />
            </div>
          </Reveal>

          {/* Live Terminal */}
          <Reveal delay={0.1} className="lg:col-span-7">
            <div className="h-full rounded-[20px] overflow-hidden border"
              style={{
                minHeight: 580,
                borderColor: "rgba(255,255,255,0.08)",
                boxShadow: "0 40px 80px -40px rgba(0,0,0,0.9), 0 2px 0 rgba(255,255,255,0.04) inset",
              }}>
              <LiveTerminal />
            </div>
          </Reveal>
        </div>
      </section>

      {/* ── STATS CARDS ────────────────────────────────────────────── */}
      <section className="bg-ink-2 section-border-t px-8 py-10">
        <Reveal>
          <div className="pre-headline mb-8">Metriche di Oggi</div>
        </Reveal>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          {[
            { label: "Email Inviate", value: stats.emailSent, suffix: "",  icon: Mail,     accent: "#8b5cf6" },
            { label: "IG DM Oggi",    value: stats.igDm,     suffix: "",  icon: Activity, accent: "#fb4604" },
            { label: "Lead IG in DB", value: stats.leadDb,   suffix: "+", icon: Database, accent: "#3b82f6" },
            { label: "Canali Live",   value: stats.channels, suffix: "",  icon: Zap,      accent: "#4ade80" },
          ].map((s, i) => (
            <Reveal key={s.label} delay={i * 0.07}>
              <div
                className="text-center py-7 px-4 rounded-[20px]"
                style={{
                  background: "linear-gradient(135deg, #ffffff 0%, #f4f1f7 55%, #e0dbe8 100%)",
                  border: "1px solid rgba(255,255,255,0.85)",
                  boxShadow: "0 24px 60px -24px rgba(0,0,0,0.5), 0 2px 0 rgba(255,255,255,0.9) inset",
                }}
              >
                <s.icon className="w-5 h-5 mb-3 mx-auto" style={{ color: s.accent }} />
                <div className="text-4xl font-black mb-2" style={{ color: s.accent }}>
                  <CountUp to={s.value} suffix={s.suffix} />
                </div>
                <div className="text-[10px] font-black uppercase tracking-widest" style={{ color: "#333333" }}>
                  {s.label}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* ── PIPELINE EXPLAINER ─────────────────────────────────────── */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-5xl mx-auto px-8">
          <Reveal>
            <div className="bubble-ink mb-6">
              <TrendingUp className="w-3.5 h-3.5" /> Come Funziona
            </div>
            <h2 className="text-4xl font-black tracking-[-0.03em] mb-10">
              <span className="text-silver-black">Tre flussi,</span>{" "}
              <span className="text-orange-pure italic">un solo pannello.</span>
            </h2>
          </Reveal>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {[
              {
                num: "01", title: "Email",
                color: "#8b5cf6", border: "border-l-violet-500",
                steps: ["Google Maps Browser scraping", "Email extraction (65-80%)", "Qualifier NVIDIA Nemotron", "Writer APSOC+V personalizzato", "Invio Gmail (500/giorno)"],
              },
              {
                num: "02", title: "Instagram",
                color: "#fb4604", border: "border-l-orange-500",
                steps: ["Hashtag Scout (250+ profili)", "Profile Qualifier (bio + keyword)", "Similar Accounts Scout", "DM primo contatto (max 15/giorno)", "Follow-up F1 (giorno 2-3) + F2 (6-7)"],
              },
              {
                num: "03", title: "LinkedIn",
                color: "#3b82f6", border: "border-l-blue-500",
                steps: ["Ricerca per keyword settore", "Commenti personalizzati (100/giorno)", "Connection request automatiche", "Messaggio post-accept", "Follow-up sequenziale"],
              },
            ].map((flow, i) => (
              <Reveal key={flow.num} delay={0.1 * i}>
                <div className={`card-paper border-l-4 ${flow.border} h-full`}>
                  <div className="flex items-center gap-3 mb-5">
                    <div className="step-num text-sm">{flow.num}</div>
                    <h3 className="text-xl font-black text-black/90">{flow.title}</h3>
                  </div>
                  <ol className="space-y-2.5">
                    {flow.steps.map((s, si) => (
                      <li key={si} className="flex items-start gap-2.5 text-sm text-black/72">
                        <span className="text-[10px] font-black mt-0.5 shrink-0" style={{ color: flow.color }}>
                          {si + 1}.
                        </span>
                        {s}
                      </li>
                    ))}
                  </ol>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ── FOOTER ─────────────────────────────────────────────────── */}
      <footer className="bg-ink-2 section-border-t px-8 py-8">
        <Reveal>
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-xl flex items-center justify-center"
                style={{ background: "linear-gradient(135deg,#fb4604 0%,#ff8a4a 100%)" }}>
                <span className="text-white font-black text-xs">DE</span>
              </div>
              <div>
                <div className="text-sm font-black text-white/70">Digital Empire</div>
                <div className="text-[10px] text-white/55 uppercase tracking-widest">Outreach Engine v3.0</div>
              </div>
            </div>
            <div className="flex items-center gap-2 text-[11px] text-white/55">
              <Shield className="w-3.5 h-3.5" />
              Sistema ad uso interno — Admin only
            </div>
          </div>
        </Reveal>
      </footer>
    </div>
  );
}
