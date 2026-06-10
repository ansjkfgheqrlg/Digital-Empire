"use client";

import { useState, useRef } from "react";
import { toJpeg } from "html-to-image";
import { jsPDF } from "jspdf";
import { Reveal } from "./reveal";
import { CountUp } from "./count-up";
import {
  ArrowRight, Check, ChevronRight, Clock, Code, Database,
  Download, FileText, Layers, Mail, Send, Settings, Shield,
  Sparkles, TrendingUp, Users, Zap, Calendar, Target, Package,
  BarChart3, MessageSquare, Star, AlertCircle, RefreshCw,
} from "lucide-react";

const BOOKING_URL = "https://calendly.com/max-infoproducer/30min";
const VALIDITY_DATE = "7 Giugno 2026";
const EMIT_DATE = "24 Maggio 2026";

export default function Preventivo() {
  const [generating, setGenerating] = useState(false);
  const [pdfProgress, setPdfProgress] = useState("");
  const [pdfErr, setPdfErr] = useState("");
  const mainRef = useRef<HTMLElement>(null);

  async function downloadPDF() {
    setGenerating(true);
    setPdfErr("");
    setPdfProgress("Attivando…");

    let origHtmlWidth = "";
    let origBodyOverflow = "";

    try {
      // ── 1. Step-scroll to trigger ALL IntersectionObservers ──
      // A single jump to bottom skips middle sections — step through them.
      const viewH = window.innerHeight;
      const stepPx = Math.max(1, Math.floor(viewH * 0.7));
      let scrollY = 0;
      while (scrollY <= document.body.scrollHeight) {
        window.scrollTo({ top: scrollY, behavior: "instant" });
        await new Promise(r => setTimeout(r, 80));
        scrollY += stepPx;
      }

      // ── 2. Wait for ALL animations to complete ──────────────
      // CountUp: duration 1.8s | Reveal: max 1.1s → need ≥ 2s
      setPdfProgress("Animazioni…");
      await new Promise(r => setTimeout(r, 2200));

      window.scrollTo({ top: 0, behavior: "instant" });
      await new Promise(r => setTimeout(r, 300));

      // ── 2. Force 1200px consistent layout width ──────────────
      origHtmlWidth = document.documentElement.style.width;
      origBodyOverflow = document.body.style.overflowX;
      document.documentElement.style.width = "1200px";
      document.body.style.overflowX = "hidden";
      await new Promise(r => setTimeout(r, 350));

      // ── 3. Apply compact PDF CSS (removes min-h-screen etc.) ─
      document.body.classList.add("pdf-capture");
      await new Promise(r => setTimeout(r, 250));

      const mainEl = document.querySelector("main") as HTMLElement;
      const sections = Array.from(mainEl.querySelectorAll("section"));
      if (sections.length === 0) throw new Error("Nessuna section trovata");

      // ── 4. Per-section capture: each section → own JPEG ─────
      // Captures every section independently → exact pixel height,
      // no estimation, no empty space, no mis-measurement.
      const PDF_W   = 210;   // mm — A4 width
      const PDF_MAX = 297;   // mm — A4 height (page budget)

      type SecImg = { dataUrl: string; heightMm: number };
      const secImgs: SecImg[] = [];

      const captureOpts = {
        quality: 0.93,
        pixelRatio: 1.5,
        cacheBust: true,
        skipFonts: false,
        filter: (node: Node) => {
          const el = node as HTMLElement;
          if (el.id === "pdf-btn-wrapper") return false;
          return true;
        },
      };

      for (let i = 0; i < sections.length; i++) {
        setPdfProgress(`Sezione ${i + 1} / ${sections.length}…`);
        const url = await toJpeg(sections[i] as HTMLElement, captureOpts);
        const img = new Image();
        await new Promise<void>((res, rej) => { img.onload = () => res(); img.onerror = () => rej(); img.src = url; });
        const heightMm = (img.naturalHeight * PDF_W) / img.naturalWidth;
        secImgs.push({ dataUrl: url, heightMm });
      }

      // ── 5. Bin-pack sections → pages (greedy, never split) ──
      type PageGroup = { secs: SecImg[]; totalMm: number };
      const pages: PageGroup[] = [];
      let curSecs: SecImg[] = [];
      let curMm = 0;

      for (const si of secImgs) {
        if (curMm + si.heightMm > PDF_MAX && curSecs.length > 0) {
          pages.push({ secs: curSecs, totalMm: curMm });
          curSecs = [si];
          curMm   = si.heightMm;
        } else {
          curSecs.push(si);
          curMm += si.heightMm;
        }
      }
      if (curSecs.length > 0) pages.push({ secs: curSecs, totalMm: curMm });

      // ── 6. Assemble PDF with exact-fit pages ─────────────────
      const pdf = new jsPDF({ unit: "mm", format: [PDF_W, pages[0].totalMm] });

      for (let pi = 0; pi < pages.length; pi++) {
        const page = pages[pi];
        if (pi > 0) pdf.addPage([PDF_W, page.totalMm]);
        let yMm = 0;
        for (const si of page.secs) {
          pdf.addImage(si.dataUrl, "JPEG", 0, yMm, PDF_W, si.heightMm);
          yMm += si.heightMm;
        }
      }

      setPdfProgress("Assemblo…");
      pdf.save("Preventivo-EXPONIUM-Digital-Empire.pdf");

    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : String(err);
      console.error("PDF error:", msg);
      setPdfErr(msg.slice(0, 80));
    } finally {
      document.body.classList.remove("pdf-capture");
      document.documentElement.style.width = origHtmlWidth;
      document.body.style.overflowX = origBodyOverflow;
      setGenerating(false);
      setPdfProgress("");
    }
  }

  return (
    <div className="flex flex-col min-h-screen">

      {/* ── Download PDF Button ── */}
      <div id="pdf-btn-wrapper" className="fixed top-4 right-4 z-50 print:hidden flex flex-col items-end gap-1">
        <button
          onClick={downloadPDF}
          disabled={generating}
          className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white/10 border border-white/15 text-white/70 text-xs font-semibold hover:bg-white/15 hover:text-white transition-all backdrop-blur-sm disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {generating
            ? <RefreshCw className="h-3.5 w-3.5 animate-spin" />
            : <Download className="h-3.5 w-3.5" />}
          {generating ? (pdfProgress || "Avvio…") : "Scarica PDF"}
        </button>
        {pdfErr && (
          <span className="text-[10px] text-red-400 bg-black/80 rounded px-2 py-1 backdrop-blur-sm max-w-[220px] text-right leading-tight">
            {pdfErr}
          </span>
        )}
      </div>

      <main ref={mainRef} className="flex flex-col flex-1">

        {/* ══════════════════════════════════════════════
            SEZIONE 1: COVER
        ══════════════════════════════════════════════ */}
        <section className="bg-ink-2 relative overflow-hidden min-h-screen flex flex-col justify-center">
          <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 900px 600px at 20% 50%, rgba(251,70,4,0.12) 0%, transparent 65%), radial-gradient(ellipse 500px 400px at 85% 20%, rgba(217,212,225,0.06) 0%, transparent 60%)' }} />

          <div className="max-w-4xl mx-auto px-6 py-24 relative z-10 w-full">
            {/* Top bar */}
            <Reveal>
              <div className="flex items-center justify-between mb-16 pb-6 border-b border-white/8">
                <div className="text-xs font-mono text-white/35 tracking-widest uppercase">Digital Empire</div>
                <div className="text-xs font-mono text-white/35 tracking-widest uppercase">RISERVATO · {EMIT_DATE}</div>
              </div>
            </Reveal>

            <Reveal delay={0.1}>
              <div className="pre-headline mb-3">Preventivo · N° EXP-2605</div>
              <div className="flex flex-wrap gap-2 mb-6">
                <span className="text-[9px] font-mono font-bold tracking-widest px-2.5 py-1.5 rounded border border-orange-pure/30 bg-orange-pure/8 text-orange-pure/90">OUTREACH FACTORY</span>
                <span className="text-white/25 text-sm self-center">+</span>
                <span className="text-[9px] font-mono font-bold tracking-widest px-2.5 py-1.5 rounded border border-white/15 bg-white/4 text-white/45">CONTENT FACTORY</span>
                <span className="text-white/25 text-sm self-center">+</span>
                <span className="text-[9px] font-mono font-bold tracking-widest px-2.5 py-1.5 rounded border border-white/15 bg-white/4 text-white/45">SECOND BRAIN</span>
                <span className="text-white/25 text-sm self-center">+</span>
                <span className="text-[9px] font-mono font-bold tracking-widest px-2.5 py-1.5 rounded border border-white/15 bg-white/4 text-white/45">ENGINE ROOM (BUNDLE)</span>
              </div>
            </Reveal>

            <Reveal delay={0.2}>
              <h1 className="font-black tracking-tight mb-6" style={{ lineHeight: 0.92 }}>
                <div className="text-silver-white" style={{ fontSize: 'clamp(40px, 5.5vw, 80px)' }}>
                  Infrastruttura AI
                </div>
                <div className="text-silver-orange italic" style={{ fontSize: 'clamp(40px, 5.5vw, 80px)', filter: 'drop-shadow(0 0 60px rgba(251,70,4,0.25))' }}>
                  per EXPONIUM.
                </div>
              </h1>
            </Reveal>

            <Reveal delay={0.35}>
              <p className="text-white/55 text-base md:text-lg max-w-2xl leading-relaxed mb-12">
                Questo preventivo copre l&apos;installazione di tre sistemi AI — outreach automatico su Gmail e Social Media,
                motore di produzione contenuti su pilota automatico e Second Brain per la memoria permanente del business — sui server di EXPONIUM. <strong className="text-white/80">Codice vostro per sempre. €0 mensili.</strong>
              </p>
            </Reveal>

            {/* Proof bar */}
            <Reveal delay={0.45}>
              <div className="flex flex-wrap gap-0 max-w-lg overflow-hidden mb-16" style={{ background:'radial-gradient(ellipse 110% 80% at 100% 0%,rgba(251,100,30,0.18) 0%,transparent 50%),radial-gradient(ellipse 80% 110% at 0% 100%,rgba(217,212,225,0.55) 0%,transparent 55%),linear-gradient(145deg,#f8f4ef 0%,#ede8f0 100%)', border:'1px solid rgba(255,255,255,0.85)', borderRadius:'16px', boxShadow:'0 4px 24px -6px rgba(0,0,0,0.1),0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(138,133,148,0.15) inset,0 0 0 1px rgba(138,133,148,0.1)' }}>
                {[
                  { value: "7", suffix: " gg", label: "Setup" },
                  { value: "€0", suffix: "", label: "Canoni" },
                  { value: "100", suffix: "%", label: "Tuo" },
                ].map((s, i) => (
                  <div key={i} className="flex-1 text-center py-4 px-3 last:border-r-0" style={{ borderRight: i < 2 ? '1px solid rgba(138,133,148,0.15)' : 'none' }}>
                    <div className="text-2xl font-black text-orange-pure leading-[1.2]">
                      {s.value === "€0" ? "€0" : <CountUp to={parseInt(s.value)} suffix={s.suffix} />}
                    </div>
                    <div className="text-[10px] text-neutral-500 uppercase tracking-wider mt-1 font-semibold">{s.label}</div>
                  </div>
                ))}
              </div>
            </Reveal>

            {/* Validity warning */}
            <Reveal delay={0.55}>
              <div className="flex items-center gap-3 max-w-md" style={{ background:'rgba(220,38,38,0.06)', border:'1px solid rgba(220,38,38,0.38)', borderRadius:'12px', padding:'0.875rem 1.25rem', boxShadow:'0 2px 16px -4px rgba(220,38,38,0.12),0 1px 0 rgba(255,255,255,0.05) inset,0 -1px 0 rgba(0,0,0,0.18) inset' }}>
                <div className="shrink-0 w-7 h-7 rounded-lg flex items-center justify-center" style={{ background:'rgba(220,38,38,0.14)' }}>
                  <Clock className="h-3.5 w-3.5 text-red-400" />
                </div>
                <p className="text-xs font-semibold text-white/65 leading-relaxed">
                  Offerta riservata — scade il <span className="text-red-400 font-bold">{VALIDITY_DATE}</span>. Restano solo <span className="text-red-400 font-bold">2 slot</span> disponibili per Giugno.
                </p>
              </div>
            </Reveal>
          </div>

          <div className="divider-gradient absolute bottom-0 inset-x-0" />
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 2: PERCHÉ DIGITAL EMPIRE (USP)
        ══════════════════════════════════════════════ */}
        <section className="bg-paper section section-border-t">
          <div className="max-w-4xl mx-auto px-6">
            <div className="grid md:grid-cols-2 gap-12 items-center">
              <Reveal variant="left">
                <div className="bubble-silver mb-5">
                  <Star className="h-4 w-4 text-orange-pure" />
                  <span>Perché Digital Empire</span>
                </div>
                <h2 className="text-3xl md:text-4xl font-bold tracking-tight text-silver-black mb-6">
                  Non installiamo software che non abbiamo usato.
                  <br />
                  <span className="text-orange-pure italic font-semibold">Installiamo la nostra infrastruttura.</span>
                </h2>
                <p className="text-neutral-600 text-sm leading-relaxed mb-4">
                  Questi sistemi non sono stati progettati per EXPONIUM. Sono i motori operativi che usiamo ogni giorno nella nostra agenzia per generare lead qualificati e produrre contenuti ad alta conversione per i nostri clienti.
                </p>
                <p className="text-neutral-600 text-sm leading-relaxed mb-6">
                  Quello che facciamo è preciso: prendiamo un&apos;infrastruttura già battle-tested in produzione reale, la adattiamo al brand e all&apos;ICP di EXPONIUM, e la installiamo sui vostri server. In 7 giorni.
                </p>
                <div className="flex items-start gap-3 bg-orange-pure/6 border border-orange-pure/15 rounded-xl p-4">
                  <TrendingUp className="h-4 w-4 text-orange-pure mt-0.5 shrink-0" />
                  <p className="text-xs text-neutral-700 leading-relaxed">
                    <strong>Risultato attivo su clienti simili:</strong> 300+ contatti qualificati a settimana e produzione di 4-5 settimane di contenuti in un pomeriggio, a costo mensile zero.
                  </p>
                </div>
              </Reveal>

              <Reveal variant="right">
                <div className="grid grid-cols-1 gap-4">
                  {[
                    { icon: Zap, value: 7, suffix: " gg", label: "Setup medio garantito", sub: "Dall'accordo al sistema live e operativo" },
                    { icon: Shield, value: 0, suffix: "", prefix: "€", label: "Canoni mensili post-setup", sub: "Zero dipendenze da tool di terze parti" },
                    { icon: TrendingUp, value: 100, suffix: "%", label: "Proprietà del codice", sub: "Tuo per sempre, sul tuo server" },
                  ].map((s, i) => (
                    <div key={i} className="stat-card-silver flex items-center gap-4 text-left">
                      <div className="w-10 h-10 rounded-xl bg-orange-pure/10 flex items-center justify-center shrink-0">
                        <s.icon className="h-5 w-5 text-orange-pure" />
                      </div>
                      <div>
                        <div className="text-2xl font-black text-silver-black leading-none">
                          {s.prefix}<CountUp to={s.value} suffix={s.suffix} />
                        </div>
                        <div className="text-xs font-bold text-neutral-700 mt-0.5">{s.label}</div>
                        <div className="text-[10px] text-neutral-400 mt-0.5">{s.sub}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </Reveal>
            </div>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 3: IL PROBLEMA (problem-centric)
        ══════════════════════════════════════════════ */}
        <section className="bg-ink section section-border-t relative overflow-hidden">
          <div className="divider-gradient absolute top-0 inset-x-0" />
          <div className="divider-gradient absolute bottom-0 inset-x-0" />
          <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 600px 400px at 80% 50%, rgba(251,70,4,0.06) 0%, transparent 70%)' }} />
          <div className="max-w-4xl mx-auto px-6 relative z-10">

            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-ink mb-5">
                  <AlertCircle className="h-4 w-4 text-orange-pure" />
                  <span>Il problema reale</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight mb-5">
                  <span className="text-silver-white">EXPONIUM ha un prodotto solido.</span>
                  <br />
                  <span className="text-orange-pure italic">Il problema è il tempo per scalarlo.</span>
                </h2>
              </div>
            </Reveal>

            {/* Narrative block */}
            <div className="max-w-2xl mx-auto space-y-4">
              <Reveal>
                <div className="hover:-translate-y-1" style={{ borderRadius:'20px', padding:'2.5rem 2.25rem', border:'1px solid rgba(255,255,255,0.85)', background:'radial-gradient(ellipse 110% 80% at 100% 0%,rgba(251,100,30,0.18) 0%,transparent 50%),radial-gradient(ellipse 80% 110% at 0% 100%,rgba(217,212,225,0.55) 0%,transparent 55%),linear-gradient(145deg,#f8f4ef 0%,#ede8f0 100%)', boxShadow:'0 4px 24px -6px rgba(0,0,0,0.1),0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(138,133,148,0.15) inset,0 0 0 1px rgba(138,133,148,0.1)', transition:'border-color 0.35s,transform 0.35s cubic-bezier(0.22,1,0.36,1)' }}>
                  <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 mt-0.5" style={{ background:'rgba(251,70,4,0.12)' }}>
                      <Mail className="h-5 w-5 text-orange-pure" />
                    </div>
                    <div>
                      <h3 className="font-bold text-neutral-800 text-base mb-2">L&apos;outreach manuale non è scalabile</h3>
                      <p className="text-neutral-500 text-sm leading-relaxed">
                        Contattare lead a mano su Gmail e Social Media richiede 2-3 ore ogni mattina — e il tasso di risposta rimane basso perché i messaggi sembrano template. Perché lo sono. Il sistema ti limita a 20-30 contatti al giorno quando il mercato ne richiede centinaia.
                      </p>
                      <div className="mt-4 pt-4 border-t border-neutral-200 flex items-baseline gap-2">
                        <span className="text-2xl font-black text-orange-pure">780 ore</span>
                        <span className="text-xs text-neutral-400 uppercase tracking-wider">all&apos;anno sprecate in outreach manuale</span>
                      </div>
                    </div>
                  </div>
                </div>
              </Reveal>

              <Reveal>
                <div className="hover:-translate-y-1" style={{ borderRadius:'20px', padding:'2.5rem 2.25rem', border:'1px solid rgba(255,255,255,0.85)', background:'radial-gradient(ellipse 110% 80% at 100% 0%,rgba(251,100,30,0.18) 0%,transparent 50%),radial-gradient(ellipse 80% 110% at 0% 100%,rgba(217,212,225,0.55) 0%,transparent 55%),linear-gradient(145deg,#f8f4ef 0%,#ede8f0 100%)', boxShadow:'0 4px 24px -6px rgba(0,0,0,0.1),0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(138,133,148,0.15) inset,0 0 0 1px rgba(138,133,148,0.1)', transition:'border-color 0.35s,transform 0.35s cubic-bezier(0.22,1,0.36,1)' }}>
                  <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 mt-0.5" style={{ background:'rgba(99,102,241,0.12)' }}>
                      <Sparkles className="h-5 w-5" style={{ color:'#6366f1' }} />
                    </div>
                    <div>
                      <h3 className="font-bold text-neutral-800 text-base mb-2">La produzione contenuti frena la visibilità</h3>
                      <p className="text-neutral-500 text-sm leading-relaxed">
                        Creare un carosello professionale, script video, caption e hashtag richiede ore per ogni singolo pezzo. Moltiplicalo per la frequenza necessaria a costruire una presenza social seria: il team finisce per non pubblicare abbastanza, e il profilo non cresce.
                      </p>
                      <div className="mt-4 pt-4 border-t border-neutral-200 flex items-baseline gap-2">
                        <span className="text-2xl font-black" style={{ color:'#6366f1' }}>4-6h</span>
                        <span className="text-xs text-neutral-400 uppercase tracking-wider">per ogni pezzo di contenuto creato a mano</span>
                      </div>
                    </div>
                  </div>
                </div>
              </Reveal>

              <Reveal>
                <div className="hover:-translate-y-1" style={{ borderRadius:'20px', padding:'2.5rem 2.25rem', border:'1px solid rgba(255,255,255,0.85)', background:'radial-gradient(ellipse 110% 80% at 100% 0%,rgba(251,100,30,0.18) 0%,transparent 50%),radial-gradient(ellipse 80% 110% at 0% 100%,rgba(217,212,225,0.55) 0%,transparent 55%),linear-gradient(145deg,#f8f4ef 0%,#ede8f0 100%)', boxShadow:'0 4px 24px -6px rgba(0,0,0,0.1),0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(138,133,148,0.15) inset,0 0 0 1px rgba(138,133,148,0.1)', transition:'border-color 0.35s,transform 0.35s cubic-bezier(0.22,1,0.36,1)' }}>
                  <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 mt-0.5" style={{ background:'rgba(20,184,166,0.12)' }}>
                      <BarChart3 className="h-5 w-5" style={{ color:'#0d9488' }} />
                    </div>
                    <div>
                      <h3 className="font-bold text-neutral-800 text-base mb-2">I tool SaaS costano e non appartengono a EXPONIUM</h3>
                      <p className="text-neutral-500 text-sm leading-relaxed">
                        I tool di automazione di terze parti costano €150-400 al mese, cambiano le API senza preavviso, alzano i prezzi ogni anno. E il giorno in cui chiudono o bloccano l&apos;account, perdi tutto: sequenze, dati, infrastruttura. Tutto in mano ad altri.
                      </p>
                      <div className="mt-4 pt-4 border-t border-neutral-200 flex items-baseline gap-2">
                        <span className="text-2xl font-black" style={{ color:'#0d9488' }}>€200+</span>
                        <span className="text-xs text-neutral-400 uppercase tracking-wider">mensili in strumenti che non possiedi</span>
                      </div>
                    </div>
                  </div>
                </div>
              </Reveal>

              <Reveal>
                <div className="hover:-translate-y-1" style={{ borderRadius:'20px', padding:'2.5rem 2.25rem', border:'1px solid rgba(255,255,255,0.85)', background:'radial-gradient(ellipse 110% 80% at 100% 0%,rgba(251,100,30,0.18) 0%,transparent 50%),radial-gradient(ellipse 80% 110% at 0% 100%,rgba(217,212,225,0.55) 0%,transparent 55%),linear-gradient(145deg,#f8f4ef 0%,#ede8f0 100%)', boxShadow:'0 4px 24px -6px rgba(0,0,0,0.1),0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(138,133,148,0.15) inset,0 0 0 1px rgba(138,133,148,0.1)', transition:'border-color 0.35s,transform 0.35s cubic-bezier(0.22,1,0.36,1)' }}>
                  <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 mt-0.5" style={{ background:'rgba(42,80,144,0.12)' }}>
                      <Database className="h-5 w-5" style={{ color:'#2a5090' }} />
                    </div>
                    <div>
                      <h3 className="font-bold text-neutral-800 text-base mb-2">L&apos;AI non ha memoria del business di EXPONIUM</h3>
                      <p className="text-neutral-500 text-sm leading-relaxed">
                        Ogni conversazione con un&apos;AI parte da zero. Il tono di voce, il posizionamento, i clienti ideali, le obiezioni ricorrenti, le decisioni prese: tutto svanisce alla chiusura della scheda. Il team rispende ogni volta lo stesso tempo a ricontestualizzare — e i risultati restano generici, lontani dalla realt&agrave; specifica di EXPONIUM.
                      </p>
                      <div className="mt-4 pt-4 border-t border-neutral-200 flex items-baseline gap-2">
                        <span className="text-2xl font-black" style={{ color:'#2a5090' }}>0%</span>
                        <span className="text-xs text-neutral-400 uppercase tracking-wider">della conoscenza aziendale trasferita all&apos;AI oggi</span>
                      </div>
                    </div>
                  </div>
                </div>
              </Reveal>
            </div>

            {/* Livello 3 — Emozione */}
            <Reveal>
              <div className="mt-8 max-w-2xl mx-auto text-center">
                <p className="text-white/60 text-sm leading-relaxed">
                  La cosa più frustrante? <strong className="text-white/80">Sai che il prodotto funziona. Sai che il mercato c&apos;è.</strong> Ma ogni mattina il team perde ore in attività che potrebbero girare da sole — e quella energia non viene spesa sulla cosa che conta: vendere e scalare.
                </p>
              </div>
            </Reveal>

            {/* Competitor gap — Loss Aversion quantificato */}
            <Reveal>
              <div className="mt-6 max-w-2xl mx-auto">
                <div className="grid grid-cols-2 gap-4 mb-4">
                  <div className="hover:-translate-y-1 transition-all duration-300" style={{ background:'rgba(239,68,68,0.05)', border:'1px solid rgba(239,68,68,0.30)', borderRadius:'16px', padding:'1.5rem 1.25rem', textAlign:'center', boxShadow:'0 2px 12px -3px rgba(0,0,0,0.22),0 1px 0 rgba(255,255,255,0.04) inset,0 -1px 0 rgba(0,0,0,0.28) inset' }}>
                    <div className="text-[9px] text-red-400/55 uppercase tracking-wider font-bold mb-2">Oggi · Manuale</div>
                    <div className="text-3xl font-black text-red-400/80 mb-1">7.300</div>
                    <div className="text-[10px] text-white/35 font-semibold">contatti all&apos;anno</div>
                  </div>
                  <div className="hover:-translate-y-1 transition-all duration-300" style={{ background:'rgba(251,70,4,0.06)', border:'1px solid rgba(239,68,68,0.30)', borderRadius:'16px', padding:'1.5rem 1.25rem', textAlign:'center', boxShadow:'0 2px 12px -3px rgba(0,0,0,0.22),0 1px 0 rgba(255,255,255,0.06) inset,0 -1px 0 rgba(0,0,0,0.28) inset' }}>
                    <div className="text-[9px] text-orange-pure/65 uppercase tracking-wider font-bold mb-2">Con sistema · Automatizzato</div>
                    <div className="text-3xl font-black text-orange-pure mb-1">109.500</div>
                    <div className="text-[10px] text-white/35 font-semibold">contatti all&apos;anno</div>
                  </div>
                </div>
                <p className="text-center text-xs text-white/30 font-medium">+102.200 contatti l&apos;anno — un vantaggio competitivo che cresce ogni mese che passa.</p>
              </div>
            </Reveal>

            {/* Cost of inaction */}
            <Reveal>
              <div className="mt-6 max-w-2xl mx-auto rounded-2xl border border-orange-pure/20 bg-orange-pure/5 p-6 text-center hover:-translate-y-1 transition-all duration-300">
                <p className="text-white/70 text-sm leading-relaxed">
                  Non è un problema di volontà. È un problema strutturale: stai competendo su un campo inclinato con chi ha già automatizzato le stesse operazioni che il tuo team fa ancora a mano.
                  <br />
                  <span className="text-white/90 font-semibold mt-2 block">Ogni settimana che passa, quella distanza cresce.</span>
                </p>
              </div>
            </Reveal>

          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 4: RISULTATI ATTESI
        ══════════════════════════════════════════════ */}
        <section className="bg-paper section section-border-t">
          <div className="max-w-4xl mx-auto px-6">
            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-silver mb-5">
                  <TrendingUp className="h-4 w-4 text-orange-pure" />
                  <span>Cosa cambia per EXPONIUM</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black mb-5">
                  Dopo il setup, la situazione
                  <br />
                  <span className="text-orange-pure italic font-semibold">è strutturalmente diversa.</span>
                </h2>
                <p className="text-neutral-600 text-sm max-w-xl leading-relaxed">
                  Non parliamo di feature. Parliamo di quello che succede concretamente ogni giorno dopo che i sistemi sono operativi.
                </p>
              </div>
            </Reveal>

            <div className="grid md:grid-cols-2 gap-6">
              {[
                {
                  before: "20-30 contatti al giorno, a mano, 2-3h di lavoro",
                  after: "300+ contatti qualificati ogni mattina, in automatico",
                  icon: Send,
                  metric: "10×",
                  metricLabel: "volume outreach",
                  color: "orange" as const,
                },
                {
                  before: "4-6h per creare un carosello, script e caption",
                  after: "Settimane di contenuti pronti in un pomeriggio",
                  icon: Sparkles,
                  metric: "20×",
                  metricLabel: "velocità produzione",
                  color: "silver" as const,
                },
                {
                  before: "€150-400/mese in tool SaaS che non possiedi",
                  after: "€0 mensili. Il sistema gira sui tuoi server",
                  icon: Shield,
                  metric: "€0",
                  metricLabel: "costi ricorrenti",
                  color: "orange" as const,
                },
                {
                  before: "Dipendenza totale da tool di terze parti",
                  after: "Codice tuo, documentato, modificabile in autonomia",
                  icon: Code,
                  metric: "100%",
                  metricLabel: "proprietà",
                  color: "silver" as const,
                },
                {
                  before: "Ogni sessione AI parte da zero: tono, positioning e contesto da riscrivere ogni volta",
                  after: "Il Second Brain alimenta ogni conversazione — l'AI sa già chi è EXPONIUM, cosa vende e come parla",
                  icon: Database,
                  metric: "0",
                  metricLabel: "briefing ripetuti",
                  color: "orange" as const,
                },
                {
                  before: "Copy e messaggi AI generici, non calibrati sulla realtà specifica del business",
                  after: "Ogni output riflette il brand: voce, valori, differenziatori e clienti ideali di EXPONIUM",
                  icon: Database,
                  metric: "100%",
                  metricLabel: "contesto applicato",
                  color: "silver" as const,
                },
              ].map((item, i) => (
                <Reveal key={i} delay={i * 0.08}>
                  <div className="rounded-2xl overflow-hidden hover:-translate-y-0.5 transition-all duration-300 h-full" style={{ background:'linear-gradient(160deg,#ffffff 0%,#faf8f6 38%,#f4f1f7 100%)', border:'1px solid rgba(28,28,28,0.09)', boxShadow:'0 3px 20px -4px rgba(0,0,0,0.08),0 1px 0 rgba(255,255,255,0.95) inset' }}>
                    {/* Before */}
                    <div className="px-5 pt-5 pb-4 border-b border-neutral-100/80">
                      <div className="flex items-center gap-2 mb-2">
                        <div className="w-1.5 h-1.5 rounded-full bg-red-400/70" />
                        <span className="text-[9px] font-mono font-bold tracking-widest text-red-400/80 uppercase">Prima</span>
                      </div>
                      <p className="text-neutral-500 text-xs leading-relaxed line-through decoration-red-500/50">{item.before}</p>
                    </div>
                    {/* After */}
                    <div className="px-5 pt-4 pb-5">
                      <div className="flex items-center gap-2 mb-2">
                        <item.icon className="h-3.5 w-3.5 text-orange-pure" />
                        <span className="text-[9px] font-mono font-bold tracking-widest text-orange-pure uppercase">Dopo</span>
                      </div>
                      <p className="text-neutral-800 text-sm font-semibold leading-relaxed mb-4">{item.after}</p>
                      <div className="flex items-baseline gap-1.5">
                        <span className="text-3xl font-black text-orange-pure">{item.metric}</span>
                        <span className="text-xs text-neutral-500 uppercase tracking-wider">{item.metricLabel}</span>
                      </div>
                    </div>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 5: DELIVERABLE
        ══════════════════════════════════════════════ */}
        <section className="bg-grey section section-border-t relative">
          <div className="divider-gradient--silver absolute top-0 inset-x-0" />
          <div className="max-w-4xl mx-auto px-6">
            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-orange mb-4">
                  <Package className="h-4 w-4" />
                  <span>Cosa riceve EXPONIUM</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                  Ogni deliverable,
                  <br />
                  <span className="text-orange-pure italic font-semibold">documentato e consegnato.</span>
                </h2>
              </div>
            </Reveal>

            <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-5">
              {[
                { icon: Code, title: "Codice Sorgente Completo", body: "L'intero codice di entrambi i motori, commentato e documentato. Installato sui tuoi server. Tuo al 100% per sempre, senza licenze.", tag: "PROPRIETÀ TOTALE", iconBg: "rgba(251,70,4,0.13)", iconColor: "#fb4604", tagColor: "#fb4604" },
                { icon: Settings, title: "Setup & Configurazione", body: "Configurazione completa su misura: ICP di EXPONIUM, tono di voce del brand, sequenze email personalizzate e proxy dedicati configurati.", tag: "CHIAVI IN MANO", iconBg: "rgba(99,102,241,0.13)", iconColor: "#818cf8", tagColor: "#6366f1" },
                { icon: FileText, title: "Documentazione Tecnica", body: "Manuale operativo completo per gestire, modificare e scalare i sistemi in autonomia. Nessuna dipendenza da noi dopo la consegna.", tag: "AUTONOMIA TOTALE", iconBg: "rgba(16,185,129,0.13)", iconColor: "#10b981", tagColor: "#10b981" },
                { icon: Users, title: "Dashboard Web Custom", body: "Interfaccia web per gestire lead, monitorare risposte, generare contenuti e supervisionare tutti i flussi. Tutto in un unico pannello.", tag: "PIATTAFORMA DEDICATA", iconBg: "rgba(217,119,6,0.13)", iconColor: "#d97706", tagColor: "#d97706" },
                { icon: MessageSquare, title: "3 Sequenze di Ingaggio", body: "Tre sequenze email scritte su misura per l'ICP di EXPONIUM, ottimizzate con framework CRO per massimizzare il tasso di risposta.", tag: "COPY INCLUSO", iconBg: "rgba(239,68,68,0.13)", iconColor: "#ef4444", tagColor: "#dc2626" },
                { icon: Shield, title: "30 Giorni di Supporto", body: "Supporto post-setup prioritario per 30 giorni. Risposta entro 24h lavorative, ottimizzazioni incluse, zero costi extra.", tag: "SUPPORTO DEDICATO", iconBg: "rgba(139,92,246,0.13)", iconColor: "#8b5cf6", tagColor: "#8b5cf6" },
              ].map((d, i) => (
                <Reveal key={i} delay={0.05 * i}>
                  <div className="rounded-2xl p-6 h-full transition-all duration-500 hover:-translate-y-1 flex flex-col" style={{ background:`linear-gradient(145deg,#ffffff 0%,#f8f7f5 50%,#f1efec 100%)`, border:`1px solid rgba(28,28,28,0.11)`, boxShadow:`0 2px 10px -3px rgba(0,0,0,0.07),0 1px 0 rgba(255,255,255,0.9) inset` }}>
                    <div className="w-10 h-10 rounded-xl flex items-center justify-center mb-4" style={{ background: d.iconBg }}>
                      <d.icon className="h-5 w-5" style={{ color: d.iconColor }} />
                    </div>
                    <span className="text-[9px] font-mono font-bold tracking-widest mb-2" style={{ color: d.tagColor }}>[ {d.tag} ]</span>
                    <h4 className="font-bold text-neutral-800 text-sm mb-2">{d.title}</h4>
                    <p className="text-neutral-500 text-xs leading-relaxed flex-1">{d.body}</p>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 6: TIMELINE
        ══════════════════════════════════════════════ */}
        <section className="bg-paper section section-border-t relative">
          <div className="max-w-4xl mx-auto px-6">
            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-silver mb-4">
                  <Calendar className="h-4 w-4 text-orange-pure" />
                  <span>Piano di Implementazione</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                  Operativo in
                  <span className="text-orange-pure italic font-semibold"> 7 giorni.</span>
                </h2>
                <p className="text-neutral-600 text-sm mt-4 max-w-lg leading-relaxed">
                  Nessun mese di attesa. Nessun progetto interminabile. Dall&apos;accordo al sistema live in una settimana lavorativa.
                </p>
              </div>
            </Reveal>

            <div className="max-w-2xl mx-auto">
              <div className="space-y-0 relative pl-12 before:absolute before:left-4 before:top-4 before:bottom-4 before:w-0.5 before:bg-gradient-to-b before:from-orange-pure/60 before:via-orange-pure/30 before:to-transparent">
                {[
                  {
                    days: "Giorno 1", title: "Call di Briefing",
                    body: "Call di 60 minuti per raccogliere tutti i dettagli: ICP, tono di voce, obiettivi di crescita, canali prioritari e credenziali tecniche.",
                    tag: "KICK-OFF",
                    numBg: 'linear-gradient(135deg,#ff8a4a 0%,#fb4604 50%,#c9370a 100%)',
                    numShadow: 'rgba(251,70,4,0.45)',
                    cardBg: 'linear-gradient(145deg,#ffffff 0%,#fff6f0 30%,#ffe8d8 60%,rgba(217,212,225,0.22) 100%)',
                    borderColor: 'rgba(251,70,4,0.28)',
                    shadowColor: 'rgba(251,70,4,0.12)',
                    tagColor: '#fb4604',
                  },
                  {
                    days: "Giorno 2-3", title: "Sviluppo & Configurazione",
                    body: "Configurazione dei motori AI sul vostro ambiente, impostazione delle sequenze email personalizzate e setup dell'infrastruttura tecnica dedicata.",
                    tag: "SVILUPPO",
                    numBg: 'linear-gradient(135deg,#a5b4fc 0%,#6366f1 50%,#4338ca 100%)',
                    numShadow: 'rgba(99,102,241,0.45)',
                    cardBg: 'linear-gradient(145deg,#ffffff 0%,#f5f5ff 30%,#e8e8ff 60%,rgba(217,212,225,0.22) 100%)',
                    borderColor: 'rgba(99,102,241,0.28)',
                    shadowColor: 'rgba(99,102,241,0.12)',
                    tagColor: '#6366f1',
                  },
                  {
                    days: "Giorno 4-5", title: "Installazione & Test",
                    body: "Installazione sui vostri server, test end-to-end di tutti i flussi, validazione delle sequenze email e verifica della sicurezza degli account.",
                    tag: "TESTING",
                    numBg: 'linear-gradient(135deg,#6ee7b7 0%,#10b981 50%,#059669 100%)',
                    numShadow: 'rgba(16,185,129,0.45)',
                    cardBg: 'linear-gradient(145deg,#ffffff 0%,#f0fdf8 30%,#d8faf0 60%,rgba(217,212,225,0.22) 100%)',
                    borderColor: 'rgba(16,185,129,0.28)',
                    shadowColor: 'rgba(16,185,129,0.12)',
                    tagColor: '#10b981',
                  },
                  {
                    days: "Giorno 6-7", title: "Go-Live & Consegna",
                    body: "Avvio della prima sessione live, consegna del codice sorgente, documentazione completa e sessione di formazione con il team EXPONIUM.",
                    tag: "LIVE",
                    numBg: 'linear-gradient(135deg,#fde68a 0%,#f59e0b 50%,#b45309 100%)',
                    numShadow: 'rgba(245,158,11,0.45)',
                    cardBg: 'linear-gradient(145deg,#ffffff 0%,#fffceb 30%,#fef5c0 60%,rgba(217,212,225,0.22) 100%)',
                    borderColor: 'rgba(217,119,6,0.32)',
                    shadowColor: 'rgba(217,119,6,0.12)',
                    tagColor: '#d97706',
                  },
                ].map((step, i) => (
                  <Reveal key={i} delay={i * 0.1}>
                    <div className="relative pb-8 last:pb-0">
                      <div
                        className="absolute -left-12 top-0 w-8 h-8 rounded-full border-4 border-[#fafafa] flex items-center justify-center"
                        style={{ background: step.numBg, boxShadow: `0 4px 14px -4px ${step.numShadow}` }}
                      >
                        <span className="text-white text-[10px] font-black">{i + 1}</span>
                      </div>
                      <div
                        className="rounded-2xl p-5 hover:-translate-y-0.5 transition-all duration-300"
                        style={{ background: step.cardBg, border: `1px solid ${step.borderColor}`, boxShadow: `0 6px 24px -6px ${step.shadowColor},0 2px 0 rgba(255,255,255,0.95) inset,0 -1px 0 rgba(217,212,225,0.2) inset` }}
                      >
                        <div className="flex items-center justify-between mb-2">
                          <span className="text-[9px] font-mono font-bold tracking-widest" style={{ color: step.tagColor }}>[ {step.tag} ] · {step.days}</span>
                        </div>
                        <h4 className="font-bold text-neutral-800 text-sm mb-1.5">{step.title}</h4>
                        <p className="text-neutral-500 text-xs leading-relaxed">{step.body}</p>
                      </div>
                    </div>
                  </Reveal>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 7: OBIEZIONI FREQUENTI
        ══════════════════════════════════════════════ */}
        <section className="bg-paper section section-border-t relative">
          <div className="max-w-4xl mx-auto px-6">
            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-silver mb-5">
                  <MessageSquare className="h-4 w-4 text-orange-pure" />
                  <span>Le domande che probabilmente hai</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight text-silver-black">
                  Hai dubbi.{" "}
                  <span className="text-orange-pure italic font-semibold">Risposte dirette.</span>
                </h2>
                <p className="text-neutral-500 text-sm mt-4 max-w-lg leading-relaxed">
                  Prima di vedere i numeri, ecco le obiezioni più comuni — e perché non reggono al confronto con i dati.
                </p>
              </div>
            </Reveal>

            <div className="space-y-5 max-w-3xl mx-auto">
              {[
                {
                  num: "01",
                  q: `"Uso già Apollo / Instantly / Phantombuster — perché cambiare?"`,
                  body: `Ottima domanda. Quei tool costano tra €100 e €300 al mese — e non possiedi niente. Quando cambiano le API (succede ogni anno), quando alzano i prezzi, quando bannano l'account, perdi tutto: sequenze, dati, infrastruttura. Zero portabilità, zero controllo.`,
                  ctaIcon: Check,
                  ctaText: `Con il nostro sistema: stesso risultato (300+ contatti/giorno), ma il codice gira sul server di EXPONIUM. €0 mensili per sempre. Nessuno può togliervi nulla.`,
                },
                {
                  num: "02",
                  q: `"L'investimento è alto per noi in questo momento."`,
                  body: `Facciamo i conti. 780 ore/anno di outreach manuale a €30/h = €23.400 all'anno in tempo operativo. Tool SaaS a €200/mese = €2.400 all'anno in strumenti che non possedete. Il costo totale del "non fare" supera il setup in meno di 3 mesi — e poi continua ad accumularsi ogni anno.`,
                  ctaIcon: TrendingUp,
                  ctaText: `Non è una spesa. È il modo di eliminare tutti i costi precedenti in un colpo unico. Il sistema si ripaga da solo entro 8-10 settimane di utilizzo.`,
                },
                {
                  num: "03",
                  q: `"Come so che funziona davvero nel nostro caso?"`,
                  body: `Questi non sono sistemi progettati per voi su carta. Sono i motori che usiamo ogni giorno nella nostra agenzia — per acquisire lead e produrre contenuti per i clienti reali. Li adattiamo all'ICP, al tone of voice e agli account di EXPONIUM. Il principio di funzionamento è lo stesso.`,
                  ctaIcon: Zap,
                  ctaText: `Nella call vi mostro i sistemi live mentre girano. Dashboard reali, dati reali, flussi attivi. Non slide — la macchina in funzione, in tempo reale.`,
                },
                {
                  num: "04",
                  q: `"E se dopo il setup siamo soli con qualcosa che non funziona?"`,
                  body: `Includiamo 30 giorni (60 con Engine Room) di supporto post-setup prioritario. Ogni problema riceve risposta entro 24h lavorative, ottimizzazioni incluse, zero costi extra. Consegniamo anche documentazione tecnica completa per gestire il sistema in piena autonomia.`,
                  ctaIcon: Shield,
                  ctaText: `L'obiettivo è che EXPONIUM gestisca tutto in autonomia entro 30 giorni. Non vogliamo clienti dipendenti da noi — vogliamo clienti che scalano da soli.`,
                },
              ].map((obj, i) => (
                <Reveal key={i} delay={i * 0.07}>
                  <div className="rounded-2xl border border-neutral-100 overflow-hidden shadow-sm hover:-translate-y-1 transition-all duration-300" style={{ background: 'linear-gradient(145deg, #ffffff 0%, #f7f5f2 100%)' }}>
                    <div className="p-6">
                      <div className="flex items-start gap-4">
                        <div className="text-3xl font-black text-neutral-200 leading-none shrink-0 mt-0.5">{obj.num}</div>
                        <div className="flex-1">
                          <h3 className="font-bold text-neutral-800 text-base mb-3 italic">{obj.q}</h3>
                          <p className="text-neutral-600 text-sm leading-relaxed mb-4">{obj.body}</p>
                          <div className="flex items-start gap-3 bg-orange-pure/6 border border-orange-pure/15 rounded-xl p-4">
                            <obj.ctaIcon className="h-4 w-4 text-orange-pure mt-0.5 shrink-0" />
                            <p className="text-xs text-neutral-700 leading-relaxed"><strong>La risposta:</strong> {obj.ctaText}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 8: INVESTIMENTO
        ══════════════════════════════════════════════ */}
        <section className="bg-ink section section-border-t relative overflow-hidden">
          <div className="divider-gradient absolute top-0 inset-x-0" />
          <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 800px 500px at 50% 100%, rgba(251,70,4,0.1) 0%, transparent 65%)' }} />

          <div className="max-w-4xl mx-auto px-6 relative z-10">
            <Reveal>
              <div className="flex flex-col items-center text-center mb-14">
                <div className="bubble-orange mb-4">
                  <TrendingUp className="h-4 w-4" />
                  <span>Il Tuo Investimento</span>
                </div>
                <h2 className="text-3xl md:text-5xl font-bold tracking-tight">
                  <span className="text-silver-white">Scegli la configurazione</span>
                  <br />
                  <span className="text-orange-pure italic font-semibold">giusta per EXPONIUM.</span>
                </h2>
                <p className="text-white/55 text-sm mt-5 max-w-xl leading-relaxed">
                  Pagamento unico. Nessun canone mensile. Nessuna dipendenza. Il sistema è tuo per sempre.
                </p>
              </div>
            </Reveal>

            <div className="divider-gradient--subtle w-full h-px mb-12" />

            {/* Benchmark — social proof vicino al prezzo */}
            <Reveal delay={0.15}>
              <div className="max-w-2xl mx-auto mb-12 text-center">
                <div className="rounded-2xl bg-white/3 border border-white/8 px-8 py-6 hover:-translate-y-1 transition-all duration-300">
                  <div className="flex items-center justify-center gap-2 mb-3">
                    <TrendingUp className="h-3.5 w-3.5 text-orange-pure/60" />
                    <span className="text-[10px] text-orange-pure/60 font-mono tracking-widest uppercase">Benchmark su installazioni simili</span>
                  </div>
                  <p className="text-white/55 text-sm leading-relaxed">
                    Su installazioni con profilo simile a EXPONIUM, il sistema genera{" "}
                    <strong className="text-white/80">300+ contatti qualificati a settimana in automatico</strong>,{" "}
                    permette di produrre{" "}
                    <strong className="text-white/80">settimane di contenuti in un pomeriggio</strong>{" "}
                    e alimenta ogni conversazione AI con{" "}
                    <strong className="text-white/80">contesto permanente sul business</strong>{" "}
                    — a costo mensile zero dopo il setup unico.
                  </p>
                </div>
              </div>
            </Reveal>

            {/* 3 individual product cards */}
            <div className="grid md:grid-cols-3 gap-6 items-stretch">
              {/* Outreach Factory */}
              <Reveal delay={0.1} className="card-tier flex flex-col justify-between">
                <div>
                  <div className="w-12 h-12 rounded-2xl bg-orange-pure/10 flex items-center justify-center mb-5">
                    <Send className="h-6 w-6 text-orange-pure" />
                  </div>
                  <div className="text-[10px] text-orange-pure/70 font-mono tracking-widest mb-1">[ MOTORE 01 ]</div>
                  <h3 className="text-xl font-bold text-white mt-2 mb-3">Outreach Factory</h3>
                  <p className="text-white/55 text-xs leading-relaxed mb-5">
                    Setup completo del motore di automazione su Gmail e Social Media, configurazione proxy dedicati, 3 sequenze di copy di ingaggio scritte su misura e dashboard di gestione lead inclusa.
                  </p>
                  <ul className="space-y-2 mb-6">
                    {["300+ contatti/gg automatici", "Gmail + Social Media DM", "3 sequenze copy CRO incluse", "Dashboard lead management", "Proxy residenziali dedicati", "30gg supporto post-setup"].map((f, i) => (
                      <li key={i} className="flex items-center gap-2 text-xs text-white/60">
                        <Check className="h-3.5 w-3.5 text-orange-pure shrink-0" />{f}
                      </li>
                    ))}
                  </ul>
                </div>
                <div>
                  <div className="border-t border-white/5 pt-5 mb-4">
                    <div className="text-3xl font-black text-white">€4.000</div>
                    <div className="text-xs text-white/35 mt-1">Pagamento unico · 50% acconto, 50% consegna</div>
                  </div>
                  <div className="text-xs text-orange-pure font-bold font-mono tracking-widest">INSTALLA L&apos;OUTREACH →</div>
                </div>
              </Reveal>

              {/* Second Brain */}
              <Reveal delay={0.2} className="card-tier flex flex-col justify-between">
                <div>
                  <div className="w-12 h-12 rounded-2xl bg-orange-pure/10 flex items-center justify-center mb-5">
                    <Database className="h-6 w-6 text-orange-pure" />
                  </div>
                  <div className="text-[10px] text-orange-pure/70 font-mono tracking-widest mb-1">[ MOTORE 02 ]</div>
                  <h3 className="text-xl font-bold text-white mt-2 mb-3">Second Brain</h3>
                  <p className="text-white/55 text-xs leading-relaxed mb-5">
                    Costruzione della knowledge base aziendale di EXPONIUM come grafo di connessioni semantiche. L&apos;AI smette di dimenticare e ogni conversazione parte calibrata sulla vostra realt&agrave;.
                  </p>
                  <ul className="space-y-2 mb-6">
                    {["Knowledge base a grafo relazionale", "Contesto permanente per ogni AI", "Integrazione LLM su misura", "Workflow di aggiornamento continuo", "Zero briefing ripetuti", "30gg supporto post-setup"].map((f, i) => (
                      <li key={i} className="flex items-center gap-2 text-xs text-white/60">
                        <Check className="h-3.5 w-3.5 text-orange-pure shrink-0" />{f}
                      </li>
                    ))}
                  </ul>
                </div>
                <div>
                  <div className="border-t border-white/5 pt-5 mb-4">
                    <div className="text-3xl font-black text-white">€2.500</div>
                    <div className="text-xs text-white/35 mt-1">Pagamento unico · 50% acconto, 50% consegna</div>
                  </div>
                  <div className="text-xs text-orange-pure font-bold font-mono tracking-widest">INSTALLA IL SECOND BRAIN →</div>
                </div>
              </Reveal>

              {/* Content Factory */}
              <Reveal delay={0.3} className="card-tier flex flex-col justify-between">
                <div>
                  <div className="w-12 h-12 rounded-2xl bg-orange-pure/10 flex items-center justify-center mb-5">
                    <Sparkles className="h-6 w-6 text-orange-pure" />
                  </div>
                  <div className="text-[10px] text-orange-pure/70 font-mono tracking-widest mb-1">[ MOTORE 03 ]</div>
                  <h3 className="text-xl font-bold text-white mt-2 mb-3">Content Factory</h3>
                  <p className="text-white/55 text-xs leading-relaxed mb-5">
                    Setup completo del motore di produzione contenuti AI: caroselli Instagram, script video, caption e hashtag. Configurazione del tono di voce di EXPONIUM e 1 lancio pilota completo incluso.
                  </p>
                  <ul className="space-y-2 mb-6">
                    {["Caroselli IG con grafica automatica", "Script video Reels / TikTok / YouTube", "Caption + hashtag ottimizzati", "Upload automatico su cloud drive", "1 lancio pilota completo incluso", "30gg supporto post-setup"].map((f, i) => (
                      <li key={i} className="flex items-center gap-2 text-xs text-white/60">
                        <Check className="h-3.5 w-3.5 text-orange-pure shrink-0" />{f}
                      </li>
                    ))}
                  </ul>
                </div>
                <div>
                  <div className="border-t border-white/5 pt-5 mb-4">
                    <div className="text-3xl font-black text-white">€3.500</div>
                    <div className="text-xs text-white/35 mt-1">Pagamento unico · 50% acconto, 50% consegna</div>
                  </div>
                  <div className="text-xs text-orange-pure font-bold font-mono tracking-widest">INSTALLA LA CONTENT FACTORY →</div>
                </div>
              </Reveal>
            </div>

            {/* Engine Room — FEATURED full-width bundle */}
            <Reveal delay={0.4} className="mt-6">
              <div className="card-tier--featured relative">
                <div className="tier-badge">✦ MIGLIOR VALORE ✦</div>
                <div className="flex flex-col md:flex-row md:items-start gap-6 pt-4">
                  <div className="w-14 h-14 rounded-2xl bg-orange-pure/15 flex items-center justify-center flex-shrink-0">
                    <Layers className="h-7 w-7 text-orange-pure" />
                  </div>
                  <div className="flex-1">
                    <div className="text-[10px] text-orange-pure font-mono font-bold tracking-widest mb-1">[ INTEGRAZIONE TOTALE ]</div>
                    <h3 className="text-2xl font-black text-neutral-800 mb-3">Engine Room</h3>
                    <p className="text-neutral-700 text-xs leading-relaxed mb-5 font-medium max-w-2xl">
                      Tutti e tre i motori centralizzati in un&apos;unica Dashboard premium. I lead caldi dell&apos;outreach, i contenuti ottimizzati e la memoria del business lavorano in sinergia totale — ogni motore alimenta gli altri in tempo reale.
                    </p>
                    <ul className="grid grid-cols-2 md:grid-cols-3 gap-x-6 gap-y-2 mb-0">
                      {["Tutto di Outreach Factory incluso", "Tutto di Second Brain incluso", "Tutto di Content Factory incluso", "Dashboard unificata con sinergia AI", "Sessione strategica di mappatura funnel", "60gg supporto prioritario + formazione team"].map((f, i) => (
                        <li key={i} className="flex items-center gap-2 text-xs text-neutral-600 font-medium">
                          <Check className="h-3.5 w-3.5 text-orange-pure shrink-0" />{f}
                        </li>
                      ))}
                    </ul>
                  </div>
                  <div className="flex-shrink-0 md:text-right">
                    <div className="flex items-baseline gap-2 md:justify-end">
                      <div className="text-3xl font-black text-neutral-800">€8.000</div>
                      <div className="text-sm text-neutral-400 line-through">€10.000</div>
                    </div>
                    <div className="text-xs text-neutral-500 mt-1">Risparmio €2.000 · 50% acconto, 50% consegna</div>
                    <div className="text-xs text-orange-pure font-bold font-mono tracking-widest mt-4">SISTEMA COMPLETO →</div>
                  </div>
                </div>
              </div>
            </Reveal>

            <div className="divider-gradient--subtle w-full h-px mt-12" />

            <Reveal delay={0.4}>
              <p className="text-center text-xs text-white/30 mt-6">
                Modalità di pagamento: 50% all&apos;accordo (bonifico bancario), 50% alla consegna e go-live del sistema.
                Fattura con IVA al 22%.
              </p>
            </Reveal>
          </div>
        </section>

        {/* ══════════════════════════════════════════════
            SEZIONE 8: CTA FINALE + TERMINI
        ══════════════════════════════════════════════ */}
        <section id="accetta" className="bg-ink-2 section section-border-t relative overflow-hidden">
          <div className="divider-gradient absolute top-0 inset-x-0" />
          <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 900px 600px at 50% calc(100% + 100px), rgba(251,70,4,0.16) 0%, transparent 65%)' }} />

          <div className="max-w-3xl mx-auto px-6 text-center relative z-10">
            <Reveal delay={0.05}>
              <div className="pre-headline mb-5">Prossimo Passo · Zero Rischio</div>
            </Reveal>

            <Reveal delay={0.1}>
              <div className="flex justify-center mb-8">
                <div className="bubble-orange">
                  <Clock className="h-4 w-4" />
                  <span>Valida fino al {VALIDITY_DATE} · 2 slot disponibili</span>
                </div>
              </div>
            </Reveal>

            <Reveal delay={0.2}>
              <h2 className="font-black tracking-tight mb-6" style={{ fontSize: 'clamp(36px, 5.5vw, 72px)', lineHeight: 1.1 }}>
                <span className="text-silver-white">Prenota 30 minuti.</span>
                <br />
                <span className="text-silver-orange italic">Ti mostro tutto in azione.</span>
              </h2>
            </Reveal>

            <Reveal delay={0.3}>
              <p className="text-white/60 text-base max-w-xl mx-auto mb-10 leading-relaxed">
                Una call di 30 minuti in cui mostro i sistemi live mentre girano.
                Se c&apos;è un fit, connetto i motori a EXPONIUM entro 48 ore.
                Se non c&apos;è, rimane comunque una roadmap di automazione chiara e senza costi.
              </p>
            </Reveal>

            <Reveal delay={0.4}>
              <a href={BOOKING_URL} className="btn-orange btn-orange--lg group" target="_blank" rel="noopener noreferrer">
                Prenota la call di presentazione
                <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-0.5" />
              </a>

              <p className="text-xs text-white/30 mt-5">
                Oppure rispondi direttamente a questa proposta via email: max.infoproducer@gmail.com
              </p>

              <div className="flex flex-wrap justify-center gap-6 mt-8">
                <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                  <Check className="h-3.5 w-3.5 text-emerald-500" /> Risposta entro 24h
                </span>
                <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                  <Shield className="h-3.5 w-3.5 text-orange-pure" /> Nessun impegno prima della call
                </span>
                <span className="flex items-center gap-1.5 text-[11px] text-white/35">
                  <Layers className="h-3.5 w-3.5 text-orange-pure" /> Roadmap inclusa anche senza acquisto
                </span>
              </div>
            </Reveal>

            {/* Termini essenziali */}
            <Reveal delay={0.5}>
              <div className="mt-16 pt-10 border-t border-white/6 text-left">
                <div className="text-[10px] text-white/20 font-mono tracking-widest uppercase mb-5">Termini Essenziali</div>
                <div className="grid md:grid-cols-2 gap-x-10 gap-y-3">
                  {[
                    { label: "Pagamento", value: "50% all'accettazione · 50% al go-live" },
                    { label: "Tempi di consegna", value: "7 giorni lavorativi dall'acconto ricevuto" },
                    { label: "Revisioni incluse", value: "2 round di revisione per sequenze e configurazione" },
                    { label: "Ritardi materiali cliente", value: "Le scadenze slittano proporzionalmente" },
                    { label: "Proprietà output", value: "100% cliente dopo saldo della seconda rata" },
                    { label: "Cancellazione", value: "L'acconto non è rimborsabile dopo l'avvio del lavoro" },
                    { label: "Supporto post-consegna", value: "30 gg (Outreach / Content) · 60 gg (Engine Room)" },
                    { label: "Validità proposta", value: `Fino al ${VALIDITY_DATE} — prezzi soggetti a variazione` },
                  ].map((t, i) => (
                    <div key={i} className="flex items-start gap-2">
                      <ChevronRight className="h-3.5 w-3.5 text-orange-pure/50 mt-0.5 shrink-0" />
                      <div>
                        <span className="text-[10px] text-white/40 font-semibold">{t.label}:</span>
                        <span className="text-[10px] text-white/25 ml-1">{t.value}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </Reveal>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-ink-2 py-8 border-t border-white/5 text-center text-xs text-white/25">
          <p className="mb-1">✦ DIGITAL EMPIRE © 2026 ✦ · Proposta Riservata per EXPONIUM</p>
          <p>Documento confidenziale. Non distribuire. Validità: {VALIDITY_DATE}.</p>
        </footer>


      </main>
    </div>
  );
}
