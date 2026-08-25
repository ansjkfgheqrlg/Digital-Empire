"use client";

import {
  ArrowRight,
  ArrowDown,
  ArrowUpRight,
  Check,
  BookOpen,
  Download,
  Shield,
  Terminal,
  SquareSlash,
  Users,
  Webhook,
  PlugZap,
  FileCode2,
  Settings2,
  GitBranch,
  Gauge,
  Code2,
  Briefcase,
  Layers,
  ListChecks,
  Target,
} from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { StickyCTA } from "@/components/sticky-cta";
import { FormEvent, useState } from "react";

const COURSE_URL = "https://formazione-systemarchitect.netlify.app/";
const API_KEY =
  "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";
const LIST_ID = 3;

function BrevoForm() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState("");
  const [statusType, setStatusType] = useState<"error" | "loading" | "">("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    if (!nome.trim()) {
      setStatus("inserisci il tuo nome.");
      setStatusType("error");
      return;
    }

    if (!email.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setStatus("inserisci un indirizzo email valido.");
      setStatusType("error");
      return;
    }

    setLoading(true);
    setStatus("invio in corso...");
    setStatusType("loading");

    try {
      const response = await fetch("https://api.brevo.com/v3/contacts", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "api-key": API_KEY,
        },
        body: JSON.stringify({
          email,
          attributes: { FIRSTNAME: nome, SELECTED_GUIDE: "Claude Code Mastery" },
          listIds: [LIST_ID],
          updateEnabled: true,
        }),
      });

      if (response.ok || response.status === 204) {
        try {
          localStorage.setItem("ccm_offer_start", String(Date.now()));
        } catch {}
        window.location.href = "/thank-you";
      } else {
        setStatus("errore. riprova.");
        setStatusType("error");
        setLoading(false);
      }
    } catch {
      setStatus("errore di connessione. riprova.");
      setStatusType("error");
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <input
        type="text"
        value={nome}
        onChange={(e) => {
          setNome(e.target.value);
          setStatus("");
        }}
        placeholder="il tuo nome"
        required
        disabled={loading}
        className="w-full px-5 py-4 bg-black/[0.03] border border-black/10 rounded-xl text-[#1c1c1c] placeholder:text-[#6a6a6a] outline-none focus:border-[#fb4604] focus:bg-white/50 transition-all font-medium text-[15px] disabled:opacity-50"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => {
          setEmail(e.target.value);
          setStatus("");
        }}
        placeholder="la tua email migliore"
        required
        disabled={loading}
        className="w-full px-5 py-4 bg-black/[0.03] border border-black/10 rounded-xl text-[#1c1c1c] placeholder:text-[#6a6a6a] outline-none focus:border-[#fb4604] focus:bg-white/50 transition-all font-medium text-[15px] disabled:opacity-50"
      />
      <button
        type="submit"
        disabled={loading}
        className="btn-orange btn-orange--lg w-full justify-center disabled:opacity-60 disabled:cursor-not-allowed"
      >
        {loading ? "invio..." : "scarica ora l'ebook"}
        <ArrowRight className="h-4 w-4" />
      </button>
      {status && (
        <p
          className={`text-center text-sm font-semibold ${
            statusType === "error" ? "text-red-600" : "text-[#5a5a5a]"
          }`}
        >
          {status}
        </p>
      )}
      <p className="text-center text-[13px] text-[#6a6a6a] font-medium">
        niente spam. cancellati quando vuoi.
      </p>

      <a
        href={COURSE_URL}
        target="_blank"
        rel="noopener noreferrer"
        className="w-full flex items-center justify-between px-5 py-3.5 rounded-xl bg-black/[0.04] border border-black/10 hover:bg-black/[0.07] hover:border-black/25 transition-all group mt-1 no-underline"
      >
        <div className="flex flex-col text-left">
          <span className="text-[#1c1c1c] font-bold text-sm">
            Oppure scopri il corso completo
          </span>
          <span className="text-[#5a5a5a] text-[10px] font-bold uppercase tracking-widest mt-0.5">
            DA AI USER A SYSTEM ARCHITECT
          </span>
        </div>
        <ArrowUpRight className="w-4 h-4 text-[#5a5a5a] group-hover:text-black transition-colors" />
      </a>
    </form>
  );
}

const TOPICS: {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  body: string;
}[] = [
  { icon: Terminal, title: "Setup & Installazione", body: "Configurazione ottimale, autenticazione, modelli disponibili, IDE integration. Parti con la configurazione dei professionisti." },
  { icon: SquareSlash, title: "Slash Command & Skill", body: "Creazione, struttura e attivazione dei comandi custom. Skill modulari che si auto-invocano in base al contesto." },
  { icon: Users, title: "Sub-Agent & Orchestration", body: "Delega intelligente, agent specializzati, gestione del contesto in parallelo. Più istanze di Claude che collaborano." },
  { icon: Webhook, title: "Hook di sistema", body: "Automazioni deterministiche agganciate a eventi reali: before/after tool, user-prompt-submit, stop. Il vero controllo." },
  { icon: PlugZap, title: "MCP Server", body: "Collegamento a tool esterni reali, database, API, filesystem remoti. Come estendere Claude al tuo ecosistema." },
  { icon: FileCode2, title: "CLAUDE.md & Memory", body: "Il file che definisce l'identità operativa di Claude. Memory persistente, policy, contesto long-term." },
  { icon: Settings2, title: "Settings & Permessi", body: "Configurazione di settings.json, gestione dei tool permessi, env var, policy di sicurezza. Zero prompt inutili." },
  { icon: GitBranch, title: "Workflow Git & PR", body: "Dal commit pulito alla review di una pull request. Claude come reviewer senior, non come autocomplete." },
  { icon: Gauge, title: "Performance & Context", body: "Gestione del context window, caching, compaction, parallel tool use. Usa Claude al massimo senza sprecare token." },
];

export default function Page() {
  return (
    <main className="relative">
      <StickyCTA href="#form" label="Scarica l'Ebook Gratis" />

      {/* ===================== HERO ===================== */}
      <section className="bg-ink relative overflow-hidden">
        <div className="border-b border-white/10 overflow-hidden py-3 relative">
          <div
            className="marquee flex gap-10 whitespace-nowrap text-[13px] uppercase tracking-[0.2em] text-[#e8e3ef] font-semibold"
            style={{ width: "max-content" }}
          >
            {Array.from({ length: 12 }).map((_, i) => (
              <span key={i} className="flex items-center gap-10">
                <span>Claude Code Mastery</span>
                <span className="text-orange-pure">✦</span>
                <span>206 Pagine · Gratis</span>
                <span className="text-orange-pure">✦</span>
                <span>Manuale Operativo</span>
                <span className="text-orange-pure">✦</span>
                <span>Digital Empire</span>
                <span className="text-orange-pure">✦</span>
              </span>
            ))}
          </div>
        </div>

        <div className="max-w-6xl mx-auto px-6 py-20 md:py-28 relative grid lg:grid-cols-[1.2fr_0.9fr] gap-14 items-center">
          <span className="silver-chip float-a" style={{ top: "10%", left: "-4%" }}>
            <span className="dot" /> <strong>206</strong> pagine
          </span>
          <span className="silver-chip float-b" style={{ top: "22%", right: "-2%" }}>
            <span className="dot" /> <strong>100%</strong> gratis
          </span>
          <span className="silver-chip float-c" style={{ bottom: "18%", left: "-2%" }}>
            <span className="dot" /> Solo <strong>Claude Code</strong>
          </span>
          <span className="silver-chip float-d" style={{ bottom: "6%", right: "-3%" }}>
            <span className="dot" /> Edizione <strong>2026</strong>
          </span>

          <div>
            <Reveal>
              <span className="bubble-orange mb-6">
                <BookOpen className="h-3.5 w-3.5" /> Ebook Gratuito · Edizione 2026
              </span>
            </Reveal>
            <Reveal delay={0.05}>
              <div className="pre-headline mt-4 mb-5">Claude Code Mastery</div>
            </Reveal>
            <Reveal delay={0.1}>
              <h1 className="text-[44px] md:text-[66px] font-bold leading-[1.03] tracking-tight mb-7">
                <span className="text-silver-white">Il manuale di 206 pagine</span>
                <br />
                <span className="text-silver-orange">
                  che ti rende padrone di Claude Code.
                </span>
              </h1>
            </Reveal>
            <Reveal delay={0.2}>
              <p className="text-[17px] md:text-xl text-white/70 max-w-xl mb-8 leading-[1.75] font-light">
                Una{" "}
                <strong className="text-silver-orange font-semibold">
                  guida completa e pratica
                </strong>{" "}
                che copre ogni singolo concetto che conta di Claude Code.
                Dall'installazione al controllo totale di sub-agent, hook, skill
                e MCP. <span className="hl-block">Zero fumo, solo operatività.</span>
              </p>
            </Reveal>

            <Reveal delay={0.25}>
              <ul className="flex flex-col gap-3 mb-10 max-w-xl">
                {[
                  "206 pagine di formazione densa, senza riempitivi.",
                  "Ogni concetto importante di Claude Code: agent, hook, skill, MCP, slash command.",
                  "Esempi concreti, comandi reali, workflow pronti da replicare.",
                  "100% gratuito. Arriva subito nella tua email.",
                ].map((t, i) => (
                  <li
                    key={i}
                    className="flex gap-4 text-[15px] md:text-base text-white/80 font-light items-start"
                  >
                    <div className="w-5 h-5 rounded flex items-center justify-center shrink-0 border border-[#fb4604]/50 bg-[#fb4604]/10 mt-1">
                      <Check className="h-3.5 w-3.5 text-[#ff6a2e]" />
                    </div>
                    <span className="leading-relaxed">{t}</span>
                  </li>
                ))}
              </ul>
            </Reveal>

            <Reveal delay={0.3}>
              <div className="flex flex-col sm:flex-row gap-4">
                <a
                  href="#form"
                  className="btn-orange btn-orange--lg group justify-center"
                >
                  Scarica l&apos;Ebook Gratis
                  <ArrowDown className="h-5 w-5 transition-transform group-hover:translate-y-0.5" />
                </a>
                <a
                  href={COURSE_URL}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-ghost group justify-center"
                >
                  Scopri il corso completo
                  <ArrowUpRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </a>
              </div>
            </Reveal>
          </div>

          {/* Book cover mock */}
          <Reveal delay={0.35} variant="scale">
            <div className="relative flex items-center justify-center min-h-[440px]">
              <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_rgba(251,70,4,0.22)_0%,_transparent_65%)]" />
              <div
                className="relative book-float"
                style={{
                  filter:
                    "drop-shadow(0 40px 50px rgba(0,0,0,0.55)) drop-shadow(0 0 60px rgba(251,70,4,0.2))",
                }}
              >
                <div
                  className="relative w-[260px] md:w-[320px] h-[370px] md:h-[450px] rounded-[6px] overflow-hidden"
                  style={{
                    background:
                      "linear-gradient(135deg, #0f0f0f 0%, #1c1c1c 40%, #2a2a2a 100%)",
                    border: "1px solid rgba(255,255,255,0.14)",
                    boxShadow:
                      "inset 0 0 0 1px rgba(255,255,255,0.05), inset -3px 0 6px rgba(0,0,0,0.5)",
                  }}
                >
                  <div className="absolute left-0 top-0 bottom-0 w-[10px] bg-gradient-to-r from-black/70 to-transparent" />
                  <div className="relative z-10 flex flex-col justify-between h-full p-7 md:p-8">
                    <div>
                      <div className="text-[10px] uppercase tracking-[0.3em] text-white/50 font-semibold mb-4">
                        Digital Empire
                      </div>
                      <div className="w-10 h-[2px] bg-[#fb4604] mb-6" />
                      <h3 className="text-3xl md:text-4xl font-black leading-[1.05] tracking-tight mb-3">
                        <span className="text-silver-white">Claude</span>
                        <br />
                        <span className="text-silver-white">Code</span>
                        <br />
                        <span className="text-silver-orange italic">Mastery</span>
                      </h3>
                    </div>
                    <div>
                      <div className="text-[11px] uppercase tracking-[0.22em] text-white/40 font-semibold mb-1">
                        Manuale Pratico
                      </div>
                      <div className="text-[13px] text-white/60 font-medium">
                        206 pagine · Edizione 2026
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== STATS ===================== */}
      <section className="bg-ink section">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <div className="text-center mb-12">
              <span className="bubble-silver mb-6">Cosa contiene</span>
              <h2 className="text-[34px] md:text-[52px] font-bold leading-[1.1] mt-6">
                <span className="text-silver-white">Un manuale serio,</span>
                <br />
                <span className="text-orange-pure italic font-medium">
                  scritto da chi usa Claude Code ogni giorno.
                </span>
              </h2>
            </div>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-5">
            {[
              { n: 206, suf: "", label: "Pagine operative" },
              { n: 12, suf: "+", label: "Macro-argomenti" },
              { n: 0, suf: "€", label: "Il tuo investimento" },
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
        </div>
      </section>

      {/* ===================== COSA IMPARI ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-6xl mx-auto px-6">
          <Reveal>
            <div className="text-center mb-14">
              <span className="bubble-orange mb-6">
                <ListChecks className="w-3.5 h-3.5" /> Contenuto
              </span>
              <h2 className="text-[34px] md:text-[52px] font-bold leading-[1.1] mt-6 mb-5">
                <span className="text-silver-white">Tutto quello che conta</span>
                <br />
                <span className="text-silver-orange">
                  su Claude Code. In un solo ebook.
                </span>
              </h2>
              <p className="text-white/65 text-lg max-w-2xl mx-auto font-light">
                Il manuale è costruito{" "}
                <strong className="text-silver-orange font-semibold">
                  pagina dopo pagina
                </strong>{" "}
                per portarti dal setup iniziale alla padronanza totale dei
                sistemi agentici più avanzati.
              </p>
            </div>
          </Reveal>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
            {TOPICS.map((t, i) => {
              const Icon = t.icon;
              return (
                <Reveal key={i} delay={(i % 3) * 0.1}>
                  <div className="card-dark h-full" style={{ padding: "1.75rem" }}>
                    <div className="w-11 h-11 rounded-xl bg-[#fb4604]/15 border border-[#fb4604]/30 flex items-center justify-center mb-5">
                      <Icon className="w-5 h-5 text-[#ff6a2e]" />
                    </div>
                    <h3 className="text-xl font-bold mb-3 text-white">
                      {t.title}
                    </h3>
                    <p className="text-white/65 text-[15px] leading-relaxed font-light">
                      {t.body}
                    </p>
                  </div>
                </Reveal>
              );
            })}
          </div>
        </div>
      </section>

      {/* ===================== PER CHI È ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-6xl mx-auto px-6">
          <Reveal>
            <div className="text-center mb-14">
              <span className="bubble-ink mb-6">
                <Target className="w-3.5 h-3.5" /> Per chi è
              </span>
              <h2 className="text-[34px] md:text-[52px] font-bold leading-[1.1] mt-6">
                <span className="text-silver-black">È scritto per te</span>
                <br />
                <span className="text-orange-pure italic font-medium">
                  se vuoi fare sul serio con l&apos;AI.
                </span>
              </h2>
            </div>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                icon: Code2,
                title: "Sviluppatori",
                body: "Che vogliono portare Claude Code nel proprio flusso quotidiano e smettere di usare AI come copia-incolla.",
              },
              {
                icon: Briefcase,
                title: "Founder & Solopreneur",
                body: "Che costruiscono prodotti digitali e vogliono moltiplicare la propria capacità operativa con un agente reale, non un chatbot.",
              },
              {
                icon: Layers,
                title: "Team tecnici",
                body: "Che vogliono standardizzare l'uso di Claude Code internamente con skill, hook e CLAUDE.md condivisi e versionati.",
              },
            ].map((p, i) => {
              const Icon = p.icon;
              return (
                <Reveal key={i} delay={i * 0.1}>
                  <div className="card-paper h-full">
                    <div className="w-12 h-12 rounded-xl bg-[#fb4604]/10 border border-[#fb4604]/30 flex items-center justify-center mb-5">
                      <Icon className="w-5 h-5 text-[#fb4604]" />
                    </div>
                    <h3 className="text-xl font-bold mb-3 text-[#1c1c1c]">
                      {p.title}
                    </h3>
                    <p className="text-[#3a3a3a] text-[15px] leading-relaxed">
                      {p.body}
                    </p>
                  </div>
                </Reveal>
              );
            })}
          </div>
        </div>
      </section>

      {/* ===================== CTA CORSO secondaria ===================== */}
      <section className="bg-ink-2 section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <div className="card-dark relative overflow-hidden">
              <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,rgba(251,70,4,0.18)_0%,transparent_60%)] pointer-events-none" />
              <div className="relative z-10 grid md:grid-cols-[1.2fr_auto] gap-8 items-center">
                <div>
                  <span className="bubble-silver mb-5 text-xs">
                    PERCORSO AVANZATO
                  </span>
                  <h3 className="text-2xl md:text-3xl font-bold mt-4 mb-3 text-silver-white">
                    Vuoi già andare oltre l&apos;ebook?
                  </h3>
                  <p className="text-white/70 font-light leading-relaxed">
                    Il corso{" "}
                    <strong className="text-silver-orange font-semibold">
                      Da AI User a System Architect
                    </strong>{" "}
                    è il percorso completo: architetture deterministiche,
                    sistemi agentici reali, workflow aziendali. Un salto di
                    categoria.
                  </p>
                </div>
                <div>
                  <a
                    href={COURSE_URL}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn-ghost group whitespace-nowrap"
                  >
                    Scopri il corso
                    <ArrowUpRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </a>
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== FORM ===================== */}
      <section id="form" className="bg-ink-2 section section-border-t pb-20">
        <div className="max-w-xl mx-auto px-6 text-center">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Download className="w-3.5 h-3.5" /> Accesso gratuito
            </span>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mt-6 mb-4">
              <span className="text-silver-white">Ottieni subito</span>
              <br />
              <span className="text-silver-orange">Claude Code Mastery</span>
            </h2>
            <p className="text-white/60 text-lg mb-10 max-w-lg mx-auto font-light">
              Inserisci nome e email. Riceverai l&apos;ebook{" "}
              <strong className="text-silver-orange font-semibold">
                entro pochi minuti
              </strong>{" "}
              direttamente nella tua casella di posta.
            </p>
          </Reveal>
          <Reveal delay={0.1}>
            <div className="stat-card-silver !py-10 !px-6 md:!px-10 text-left">
              <h3 className="text-xs font-bold text-[#4a4a4a] mb-6 uppercase tracking-[0.2em] text-center">
                SCARICA IL PDF GRATUITO
              </h3>
              <BrevoForm />
              <div className="mt-6 flex justify-center">
                <span className="text-[12px] font-medium text-[#4a4a4a] flex items-center gap-2">
                  <Shield className="h-4 w-4" /> i tuoi dati sono protetti
                </span>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== FOOTER ===================== */}
      <footer className="bg-ink-2 py-12 md:pb-12 pb-24 text-center text-white/30 text-xs tracking-widest border-t border-white/5 uppercase font-medium">
        © 2026 Digital Empire Labs
      </footer>
    </main>
  );
}
