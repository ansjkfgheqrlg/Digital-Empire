"use client";

import { ArrowRight, Check, Sparkles, Zap, Shield, BookOpen, Rocket, Terminal, Layers, DollarSign, Target, X } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { StickyCTA } from "@/components/sticky-cta";

const ENROLL_URL = "#enroll"; // Placeholder for stripe/checkout
const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";

function CTA({ large = false, label = "Inizia il Percorso CCM" }: { large?: boolean; label?: string }) {
  return (
    <a href={ENROLL_URL} className={`btn-orange ${large ? "btn-orange--lg" : ""} group`}>
      {label}
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}

function CourseCTA({ large = false, variant = "dark" }: { large?: boolean; variant?: "dark" | "light" }) {
  const base = "inline-flex items-center gap-2 rounded-full border font-semibold transition-all duration-200 group";
  const size = large ? "px-8 py-[14px] text-[15px]" : "px-6 py-3 text-sm";
  const dark = "border-white/20 bg-white/[0.04] text-white/70 hover:border-[#fb4604]/70 hover:text-[#fb4604] hover:bg-[#fb4604]/[0.06] backdrop-blur-sm";
  const light = "border-[#1c1c1c]/20 bg-black/[0.03] text-[#3a3a3a] hover:border-[#fb4604]/60 hover:text-[#fb4604] hover:bg-[#fb4604]/[0.05]";
  return (
    <a href={COURSE_URL} target="_blank" rel="noopener noreferrer" className={`${base} ${size} ${variant === "light" ? light : dark}`}>
      Diventa System Architect
      <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
    </a>
  );
}

export default function Page() {
  return (
    <main className="relative">
      <StickyCTA />

      {/* ===================== HERO ===================== */}
      <section className="bg-ink relative overflow-hidden">
        <div className="border-b border-white/10 overflow-hidden py-3">
          <div className="marquee flex gap-10 whitespace-nowrap text-xs uppercase tracking-[0.2em] text-white/40" style={{ width: "max-content" }}>
            {Array.from({ length: 12 }).map((_, i) => (
              <span key={i} className="flex items-center gap-10">
                <span>Claude Code Mastery</span>
                <span className="text-orange-pure">✦</span>
                <span>Prossima Cohort Disponibile</span>
                <span className="text-orange-pure">✦</span>
                <span>by Digital Empire</span>
                <span className="text-orange-pure">✦</span>
              </span>
            ))}
          </div>
        </div>

        <div className="max-w-5xl mx-auto px-6 py-24 md:py-36 text-center relative">
          <span className="silver-chip float-a" style={{ top: "12%", left: "-4%" }}>
            <span className="dot" /> <strong>6</strong> Moduli
          </span>
          <span className="silver-chip float-b" style={{ top: "22%", right: "-6%" }}>
            <span className="dot" /> <strong>18</strong> Template
          </span>
          <span className="silver-chip float-c" style={{ bottom: "18%", left: "-2%" }}>
            <span className="dot" /> <strong>3</strong> Progetti Portfolio
          </span>
          <span className="silver-chip float-d" style={{ bottom: "10%", right: "-3%" }}>
            <span className="dot" /> Supporto <strong>AI-Pairing</strong>
          </span>

          <Reveal>
            <span className="bubble-orange mb-6">
              <Sparkles className="h-3.5 w-3.5" /> La Skill più richiesta del 2026
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <div className="pre-headline mt-4 mb-5">Digital Empire presenta · Claude Code Mastery</div>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-[42px] md:text-[72px] font-bold leading-[1.02] tracking-tight mb-7">
              <span className="text-silver-white">Domina Claude Code.</span>
              <br />
              <span className="text-silver-orange italic">Crea Sistemi, non prompt.</span>
            </h1>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[17px] md:text-xl text-white/75 max-w-2xl mx-auto mb-10 leading-relaxed font-light">
              L'unico percorso ultra-premium che ti trasforma da "utenti di chatbot" in un <strong className="text-silver-orange font-semibold">AI Builder professionista</strong>. Impara a costruire agenti, skill personalizzate e workflow complessi capaci di <span className="hl-block">generare valore reale per il mercato.</span>
            </p>
          </Reveal>
          <Reveal delay={0.3}>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <CTA large />
              <CourseCTA />
              <span className="text-sm text-white/50 flex items-center gap-2">
                <Shield className="h-4 w-4" /> Qualità Digital Empire · Supporto Continuo
              </span>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== STATS ===================== */}
      <section className="bg-ink section">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-3 gap-5">
          {[
            { n: 21, suf: "", label: "Lezioni Intensive" },
            { n: 18, suf: "", label: "Template Pronti all'Uso" },
            { n: 6, suf: " Sett", label: "Durata Percorso" },
          ].map((s, i) => (
            <Reveal key={i} delay={i * 0.1}>
              <div className="stat-card-silver">
                <div className="text-5xl md:text-6xl font-bold text-orange-pure leading-none">
                  <CountUp to={s.n} suffix={s.suf} />
                </div>
                <div className="mt-4 text-xs md:text-sm uppercase tracking-[0.2em] text-[#5a5560] font-semibold">
                  {s.label}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* ===================== IL PROBLEMA ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Il mercato AI oggi</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-[1.1] mb-10 mt-6 max-w-[22ch]">
              <span className="text-silver-black">Tutti usano l'AI.</span>
              <br />
              <span className="text-orange-pure">Pochi sanno <em className="italic font-normal">costruire</em> con essa.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-5">
            <Reveal delay={0.15}>
              <div className="card-paper">
                <div className="flex items-center gap-3 mb-4">
                  <X className="h-5 w-5 text-[#b8b8b8]" />
                  <h3 className="text-xl font-semibold">L'utente medio</h3>
                </div>
                <p className="text-[#3a3a3a] mb-4">Copia i prompt, ottiene risultati mediocri e spera che il modello faccia tutto da solo.</p>
                <ul className="space-y-2 text-sm text-[#5a5560]">
                  <li>• Dipende dal "prompt magico"</li>
                  <li>• Non ha un metodo replicabile</li>
                  <li>• Non sa gestire progetti complessi</li>
                  <li>• Valore di mercato basso</li>
                </ul>
              </div>
            </Reveal>
            <Reveal delay={0.25}>
              <div className="card-orange">
                <div className="flex items-center gap-3 mb-4">
                  <Check className="h-5 w-5" />
                  <h3 className="text-xl font-semibold">L'AI Builder (CCM)</h3>
                </div>
                <p className="mb-4">Progetta architetture, istruisce agenti specializzati e orchestra workflow che risolvono problemi reali.</p>
                <ul className="space-y-2 text-sm">
                  <li>• Crea asset digitali proprietari</li>
                  <li>• Framework S.K.I.L.L. & W.O.R.K.</li>
                  <li>• Workflow multi-agente complessi</li>
                  <li>• Professionista da €2000+ a progetto</li>
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== CURRICULUM ===================== */}
      <section className="bg-grey section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal><span className="bubble-ink mb-6">Il Percorso</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6">
              <span className="text-silver-black">6 Moduli per la</span>
              <br />
              <span className="text-orange-pure italic font-medium">Massima Maestria.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { id: "0", t: "Setup & Start", i: <Terminal className="h-5 w-5" />, d: "Dall'installazione di Claude Code al tuo primo agente funzionante in 15 minuti." },
              { id: "1", t: "Fondamenta & I.C.R.O.", i: <Layers className="h-5 w-5" />, d: "Domina la struttura di CLAUDE.md per dare un'anima e un metodo al tuo assistente." },
              { id: "2", t: "Skill Library", i: <BookOpen className="h-5 w-5" />, d: "Costruisci la tua libreria di abilità custom con il framework S.K.I.L.L." },
              { id: "3", t: "Workflow & Agenti", i: <Zap className="h-5 w-5" />, d: "Orchestra sistemi complessi con il framework W.O.R.K e pattern di collaborazione." },
              { id: "4", t: "Progetti Portfolio", i: <Target className="h-5 w-5" />, d: "Costruisci 3 asset reali: Content System, Data Analyzer, Business Automation." },
              { id: "5", t: "Monetizzazione", i: <DollarSign className="h-5 w-5" />, d: "Trasforma la competenza in business: offerta, portfolio e primi 10 clienti." },
            ].map((m, i) => (
              <Reveal key={i} delay={i * 0.05}>
                <div className="card-paper h-full flex flex-col group hover:border-[#fb4604] transition-colors">
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-10 h-10 rounded-lg bg-ink text-white flex items-center justify-center">
                      {m.i}
                    </div>
                    <span className="text-xs font-bold text-orange-pure opacity-50 uppercase tracking-widest">Mod {m.id}</span>
                  </div>
                  <h3 className="text-xl font-bold mb-3">{m.t}</h3>
                  <p className="text-sm text-[#3a3a3a] leading-relaxed flex-1">{m.d}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== PORTFOLIO HIGHLIGHT ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <Reveal><span className="bubble-orange mb-6">Non solo teoria</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-white">Esci con un Portfolio di</span>
              <br />
              <span className="text-silver-orange italic">Progetti Reali.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-4 mt-12 text-left">
            {[
              { t: "Content System", d: "Produzione contenuti multi-piattaforma automatizzata." },
              { t: "Analisi Dati", d: "Report automatici da dati complessi e competitor." },
              { t: "Business Automation", d: "Qualificazione lead e gestione email agentica." },
            ].map((p, i) => (
              <Reveal key={i} delay={i * 0.1}>
                <div className="card-dark h-full border-l-2 border-l-orange-pure">
                  <h4 className="text-lg font-bold text-white mb-2">{p.t}</h4>
                  <p className="text-sm text-white/60 leading-relaxed">{p.d}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== VALUE STACK ===================== */}
      <section id="enroll" className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 text-center">
              <span className="text-silver-black">Ottieni Accesso a Tutto</span>
              <br />
              <span className="text-orange-pure italic font-medium">per un unico investimento.</span>
            </h2>
          </Reveal>
          <div className="card-paper !p-0 overflow-hidden">
            <div className="bg-ink p-8 text-white border-b border-white/10">
              <div className="flex justify-between items-end">
                <div>
                  <h3 className="text-2xl font-bold mb-2">Claude Code Mastery</h3>
                  <p className="text-white/50 text-sm">Full Educational System + Assets</p>
                </div>
                <div className="text-right">
                  <div className="text-sm text-white/40 line-through">Valore Totale € 2.450</div>
                  <div className="text-4xl font-bold text-orange-pure">€ 497</div>
                </div>
              </div>
            </div>
            <div className="p-8 space-y-4">
              {[
                "Accesso a vita ai 6 moduli CCM",
                "18 Template Framework (S.K.I.L.L, W.O.R.K, etc.)",
                "Community Esclusiva AI Builders",
                "Aggiornamenti continui (Claude Code evolve, noi con lui)",
                "Esercizi pratici con feedback",
                "Guida alla monetizzazione & outreach",
              ].map((item, i) => (
                <div key={i} className="flex gap-4 items-center border-b border-[#131313]/05 pb-4 last:border-0 last:pb-0">
                  <Check className="h-5 w-5 text-orange-pure shrink-0" />
                  <span className="font-medium text-[#1c1c1c]">{item}</span>
                </div>
              ))}
              <div className="pt-6">
                <CTA large label="Iscriviti Ora all'Academy" />
                <div className="flex justify-center mt-3">
                  <CourseCTA variant="light" />
                </div>
                <p className="text-center text-xs text-[#8a8a8a] mt-4">Pagamento unico · Fattura disponibile · Accesso immediato</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ===================== GARANZIA ===================== */}
      <section className="bg-ink-2 section section-border-t text-center">
        <div className="max-w-3xl mx-auto px-6">
          <Reveal><span className="bubble-silver mb-8">Nessun Rischio</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[44px] font-bold leading-tight mb-6 mt-8 tracking-tight">
              <span className="text-silver-white">Garanzia "Zero Errori".</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/70 text-lg md:text-xl mb-10 max-w-xl mx-auto leading-relaxed">
              Se dopo 14 giorni non senti di aver imparato a costruire sistemi AI che valgono 10x il costo del corso, <strong className="text-silver-orange">ti rimborsiamo fino all'ultimo centesimo</strong>. Senza domande.
            </p>
          </Reveal>
        </div>
      </section>

      {/* ===================== FOOTER ===================== */}
      <footer className="bg-ink-2 py-12 border-t border-white/10 relative z-[3]">
        <div className="max-w-5xl mx-auto px-6">
          <div className="flex flex-col md:flex-row gap-8 justify-between items-center mb-10">
            <div className="text-2xl font-bold text-silver-white">Claude Code Mastery</div>
            <div className="flex gap-8 text-sm text-white/60">
              <a href="/call" className="hover:text-orange-pure transition-colors underline underline-offset-4">Prenota Call 1:1</a>
              <a href="/platform" className="hover:text-orange-pure transition-colors">Accesso Studenti</a>
              <a href="#" className="hover:text-orange-pure transition-colors">Termini & Privacy</a>
            </div>
          </div>
          <div className="flex flex-col md:flex-row gap-4 justify-between items-center text-xs text-white/30 pt-8 border-t border-white/05">
            <div>© 2026 Digital Empire S.r.l. · P.IVA 1234567890</div>
            <div className="flex gap-2 items-center">
              <Shield className="h-3 w-3" /> Made with Claude Code & Passion
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}
