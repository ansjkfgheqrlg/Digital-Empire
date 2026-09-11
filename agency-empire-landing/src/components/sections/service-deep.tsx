"use client";

import { Reveal } from "@/components/reveal";
import { Check } from "lucide-react";

// ── Outreach data ─────────────────────────────────────────────
const outreachSteps = [
  { t: "Targeting", d: "Il sistema estrae o riceve i profili dei tuoi clienti ideali tramite filtri AI calibrati sul tuo ICP." },
  { t: "Primo Contatto", d: "Invio del primo messaggio ad altissimo valore e non commerciale — scritto da GPT-4o, non da un template." },
  { t: "Follow-up Automatico", d: "Chi non risponde riceve fino a 3 sequenze automatiche, spaziate e personalizzate." },
  { t: "Qualificazione AI e CRM", d: "L'AI estrae i lead caldi e li passa con notifiche Slack/CRM in tempo reale." },
];
const outreachFeatures = [
  { t: "Cold-Emailing Sincronizzato", d: "Touchpoint e follow-up coordinati su Gmail, con comportamento umano protetto." },
  { t: "Instagram DM Safe", d: "Proxy residenziali dedicati, velocità di digitazione variabile — mai rilevato come bot." },
  { t: "Qualificazione Semantica", d: "Scarta i \"non ora\" e isola solo chi dice \"Sì, approfondiamo.\" Notifica immediata." },
];

// ── Content Factory data ───────────────────────────────────────
const contentSteps = [
  { n: 1, t: "AI genera il copy delle slide", d: "Il motore AI scrive il testo di ogni slide del carosello usando il framework CRO APSOC, calibrato sul tuo ICP e argomento." },
  { n: 2, t: "Il motore costruisce le grafiche automaticamente", d: "Un browser reale si apre e genera automaticamente le slide visive del carosello, senza alcun intervento umano." },
  { n: 3, t: "Upload automatico su Google Drive", d: "I caroselli finiti vengono caricati e organizzati per argomento su Google Drive. Pronti da scaricare o programmare." },
];

// ── Second Brain data ──────────────────────────────────────────
const brainSteps = [
  { t: "Cattura della Conoscenza", d: "Ogni decisione, cliente, insight e processo viene strutturato in nodi collegati — costruendo la mappa semantica del business." },
  { t: "Costruzione del Grafo", d: "I nodi si linkano tra loro — ogni cliente connesso ai suoi progetti, ogni progetto al suo contesto storico. Rete navigabile visivamente." },
  { t: "Iniezione del Contesto", d: "Ogni volta che lavori con un LLM, il Second Brain inietta il contesto rilevante automaticamente. L'AI risponde come se conoscesse il business da anni." },
  { t: "Crescita Continua", d: "Ogni sessione arricchisce la knowledge base. Il Second Brain diventa più preciso nel tempo — un asset che cresce con il business." },
];
const brainFeatures = [
  { t: "Memoria Permanente", d: "ogni insight, cliente e processo accessibile all'AI per sempre." },
  { t: "Grafo di Connessioni", d: "ogni nodo linkato ad altri. Vedi le relazioni tra clienti, progetti e strategie." },
  { t: "Zero Briefing Ripetuti", d: "l'AI conosce già il brand, l'ICP, il tono di voce. Niente da rispiegare." },
];

// ─────────────────────────────────────────────────────────────

export function OutreachDeep() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-2 gap-12 md:gap-16 items-center">
          <div>
            <Reveal>
              <span className="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.20em] text-white rounded-full px-3 py-1.5 mb-6" style={{ background: "#fb4604" }}>
                ✉ Service #01 · Acquisizione lead
              </span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-[2.1rem] md:text-[2.9rem] font-black leading-[1.06] tracking-tight text-ink mb-6 mt-3">
                Outreach automatico<br />
                <span style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400 }}>su Gmail e Social.</span>
              </h2>
            </Reveal>
            <Reveal delay={0.17}>
              <p className="text-ink/82 text-[1.02rem] leading-relaxed mb-4">
                Mandare 30 DM al giorno a mano richiede 2-3 ore, ogni mattina. Con un tasso di risposta tra il <strong className="text-ink">3% e il 7%</strong> perché i messaggi sembrano template. Perché lo sono.
              </p>
              <p className="text-ink/82 text-[1.02rem] leading-relaxed mb-7">
                Il nostro motore sostituisce tutto questo: avvia sessioni browser reali e protette, <strong className="text-ink">agisce in modo umano così da non risultare mai un bot</strong>, compila i campi, digita a velocità variabile e invia messaggi di ingaggio personalizzati — senza toccare API sospette.
              </p>
            </Reveal>
            <Reveal delay={0.24}>
              <ul className="space-y-4">
                {outreachFeatures.map((f, i) => (
                  <li key={i} className="flex items-start gap-3 text-[0.98rem] text-ink/88 leading-relaxed">
                    <Check className="h-4 w-4 text-orange-pure shrink-0 mt-0.5" strokeWidth={3} />
                    <span><strong className="text-ink font-bold">{f.t}</strong>: {f.d}</span>
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>

          <Reveal delay={0.18}>
            <div className="rounded-2xl overflow-hidden" style={{
              background: "linear-gradient(152deg, #4e1400 0%, #862200 26%, #c24000 56%, #7e2000 82%, #280a00 100%)",
              border: "1px solid rgba(255,120,60,0.38)",
              boxShadow: ["0 28px 64px -18px rgba(0,0,0,0.55)", "0 0 44px -16px rgba(150,44,0,0.32)", "0 2px 0 rgba(255,255,255,0.16) inset"].join(", "),
              padding: "1.75rem",
            }}>
              <div className="flex items-center gap-2.5 mb-5 pb-4" style={{ borderBottom: "1px solid rgba(255,255,255,0.11)" }}>
                <span className="text-[11px] font-black uppercase tracking-[0.20em] text-white/90">⚡ Come funziona il workflow</span>
              </div>
              <div className="flex flex-col gap-4">
                {outreachSteps.map((step, i) => (
                  <div key={i} className="flex items-start gap-3.5">
                    <span className="w-2 h-2 rounded-full shrink-0 mt-[7px]" style={{ background: "rgba(255,160,100,0.85)" }} />
                    <div>
                      <div className="text-[0.95rem] font-bold text-white leading-tight mb-0.5">Step {i + 1}: {step.t}</div>
                      <div className="text-[0.95rem] text-white/80 leading-snug">{step.d}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}

export function ContentDeep() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-2 gap-12 md:gap-16 items-center">
          <Reveal delay={0.1}>
            <div className="rounded-2xl overflow-hidden" style={{
              background: "linear-gradient(152deg, #3c1e00 0%, #6e3800 28%, #b06200 58%, #6c3c00 82%, #200e00 100%)",
              border: "1px solid rgba(255,180,80,0.36)",
              boxShadow: ["0 28px 64px -18px rgba(0,0,0,0.48)", "0 0 40px -14px rgba(120,72,0,0.30)", "0 2px 0 rgba(255,255,255,0.14) inset"].join(", "),
              padding: "1.75rem",
            }}>
              <div className="flex items-center gap-2.5 mb-5 pb-4" style={{ borderBottom: "1px solid rgba(255,255,255,0.11)" }}>
                <span className="text-[11px] font-black uppercase tracking-[0.20em] text-white/90">✦ Come funziona la fabbrica</span>
              </div>
              <div className="flex flex-col gap-5">
                {contentSteps.map((step, i) => (
                  <div key={i} className="flex items-start gap-4">
                    <span className="w-8 h-8 rounded-lg flex items-center justify-center text-[0.9rem] font-black text-white shrink-0" style={{ background: "rgba(255,180,80,0.22)", border: "1px solid rgba(255,190,90,0.42)" }}>
                      {step.n}
                    </span>
                    <div>
                      <div className="text-[0.95rem] font-bold text-white leading-tight mb-1">{step.t}</div>
                      <div className="text-[0.95rem] text-white/80 leading-snug">{step.d}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </Reveal>

          <div>
            <Reveal>
              <span className="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.20em] text-white rounded-full px-3 py-1.5 mb-6" style={{ background: "#fb4604" }}>
                ✦ Service #02 · Content Factory
              </span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-[2.1rem] md:text-[2.9rem] font-black leading-[1.06] tracking-tight text-ink mb-6 mt-3">
                Fabbrica di Contenuti<br />
                <span style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400 }}>social su pilota automatico.</span>
              </h2>
            </Reveal>
            <Reveal delay={0.17}>
              <p className="text-ink/82 text-[1.02rem] leading-relaxed mb-4">
                Creare un carosello professionale a mano richiede ore: copy per ogni slide, design, caption, hashtag. Moltiplicalo per 4 post a settimana. Risultato: non pubblichi mai abbastanza, il profilo dorme e la concorrenza cresce.
              </p>
              <p className="text-ink/82 text-[1.02rem] leading-relaxed mb-4">
                Questo workflow fa tutto in automatico: l&apos;AI genera il copy CRO-ottimizzato per ogni slide, poi il motore di automazione costruisce le grafiche visive senza che tu tocchi nulla. Stessa logica per gli script video.
              </p>
              <p className="text-ink/82 text-[1.02rem] leading-relaxed">
                Output finale: caroselli visivi pronti, script video, caption con hashtag e upload organizzato su Google Drive. Puoi programmare la pubblicazione o scaricare e postare in 30 secondi.
              </p>
            </Reveal>
          </div>
        </div>
      </div>
    </section>
  );
}

export function BrainDeep() {
  return (
    <section className="bg-ink section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-2 gap-12 md:gap-16 items-center">
          <div>
            <Reveal>
              <span className="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.20em] text-white/85 rounded-full px-3 py-1.5 mb-6" style={{ background: "rgba(255,255,255,0.08)", border: "1px solid rgba(255,255,255,0.18)" }}>
                ⊟ Service #03 · Memoria AI
              </span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-[2.1rem] md:text-[2.9rem] font-black leading-[1.06] tracking-tight text-white mb-6 mt-3">
                Second Brain:<br />
                <span className="text-white/85" style={{ fontFamily: "var(--font-serif), Georgia, serif", fontStyle: "italic", fontWeight: 400 }}>l&apos;AI non dimentica più.</span>
              </h2>
            </Reveal>
            <Reveal delay={0.17}>
              <p className="text-white/85 text-[1.02rem] leading-relaxed mb-4">
                Ogni tool AI che usi ha un problema fondamentale: dimentica tutto. Ogni sessione reimposta. Brand voice, ICP, decisioni strategiche, clienti — tutto evaporato. Mesi di lavoro che non entrano mai nell&apos;intelligenza artificiale che usi ogni giorno.
              </p>
              <p className="text-white/85 text-[1.02rem] leading-relaxed mb-4">
                Prima c&apos;era il RAG: ricerca vettoriale su documenti, potente ma meccanico.{" "}
                <strong className="text-white">Poi è arrivato il Second Brain</strong>: una knowledge base interconnessa visualizzabile come grafo di relazioni. Andrej Karpathy ha chiamato questo approccio{" "}
                <span className="text-orange-pure font-bold">Context Engineering</span>: l&apos;arte di costruire il contesto giusto perché ogni conversazione con un LLM sia davvero calibrata sulla tua realtà.
              </p>
            </Reveal>
            <Reveal delay={0.24}>
              <ul className="space-y-4">
                {brainFeatures.map((f, i) => (
                  <li key={i} className="flex items-start gap-3 text-[0.98rem] text-white/90 leading-relaxed">
                    <Check className="h-4 w-4 text-[#90c8ff] shrink-0 mt-0.5" strokeWidth={3} />
                    <span><strong className="text-white font-bold">{f.t}</strong> — {f.d}</span>
                  </li>
                ))}
              </ul>
            </Reveal>
          </div>

          <Reveal delay={0.18}>
            <div className="rounded-2xl overflow-hidden" style={{
              background: "linear-gradient(152deg, #020c22 0%, #081a3c 26%, #102e6c 54%, #082048 80%, #020a18 100%)",
              border: "1px solid rgba(100,160,255,0.30)",
              boxShadow: ["0 28px 64px -18px rgba(0,0,0,0.70)", "0 0 40px -14px rgba(0,36,150,0.28)", "0 2px 0 rgba(255,255,255,0.12) inset"].join(", "),
              padding: "1.75rem",
            }}>
              <div className="flex items-center gap-2.5 mb-5 pb-4" style={{ borderBottom: "1px solid rgba(255,255,255,0.09)" }}>
                <span className="text-[11px] font-black uppercase tracking-[0.20em] text-white/90">⊟ Come funziona il workflow</span>
              </div>
              <div className="flex flex-col gap-4">
                {brainSteps.map((step, i) => (
                  <div key={i} className="flex items-start gap-3.5">
                    <span className="w-2 h-2 rounded-full shrink-0 mt-[7px]" style={{ background: "rgba(100,180,255,0.78)" }} />
                    <div>
                      <div className="text-[0.95rem] font-bold text-white leading-tight mb-0.5">Step {i + 1}: {step.t}</div>
                      <div className="text-[0.95rem] text-white/80 leading-snug">{step.d}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
