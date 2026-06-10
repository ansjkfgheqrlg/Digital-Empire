import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { StickyCTA } from "@/components/sticky-cta";
import { ArrowRight, Check, Zap, Shield, Brain, Mail, Layout, Cpu } from "lucide-react";

export default function CarouselPage() {
  return (
    <main className="relative">
      <StickyCTA href="https://calendly.com/max-infoproducer/30min" label="Prenota Call Strategica" />

      {/* SLIDE 1: HERO COVER */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink relative overflow-hidden px-6">
        <div className="corner-tl"></div><div className="corner-tr"></div>
        <div className="corner-bl"></div><div className="corner-br"></div>
        
        <div className="max-w-4xl w-full text-center z-10">
          <Reveal variant="up" delay={0.1}>
            <div className="bubble-orange mx-auto w-fit mb-8">
              <Zap className="w-4 h-4" /> Sistemi AI Proprietari
            </div>
          </Reveal>
          <Reveal variant="up" delay={0.2}>
            <h1 className="text-6xl md:text-8xl font-extrabold tracking-tighter mb-8 leading-[1.08]">
              <span className="text-silver-white">Smetti di fare</span><br />
              <span className="text-silver-orange"> <span className="hl-thin">tutto a mano.</span></span>
            </h1>
          </Reveal>
          <Reveal variant="up" delay={0.3}>
            <p className="text-xl md:text-2xl text-silver-dim max-w-2xl mx-auto mb-12 leading-relaxed">
              Tre motori AI installati sui tuoi server per l'outreach, la produzione contenuti e la memoria del business.
            </p>
          </Reveal>
          <Reveal variant="up" delay={0.4}>
            <div className="text-3xl font-extrabold text-orange-pure tracking-widest uppercase">
              Digital Empire
            </div>
          </Reveal>
        </div>
      </section>

      {/* SLIDE 2: THE PAIN */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink-2 px-6 py-24">
        <div className="max-w-4xl w-full">
          <Reveal variant="up">
            <div className="bubble-silver w-fit mb-8">
              <Shield className="w-4 h-4" /> Il Problema
            </div>
            <h2 className="text-5xl md:text-7xl font-bold tracking-tighter mb-12 leading-[1.08]">
              Il tuo business è <span className="hl-block">ostaggio</span> della manualità?
            </h2>
          </Reveal>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {[
              "L'outreach ti prosciuga tempo ed energie ogni singola mattina.",
              "Ogni lancio richiede settimane di copy e produzione manuale.",
              "L'AI dimentica tutto tra una sessione e l'altra, costringendoti a ripetere tutto.",
              "Dipendi da SaaS instabili con canoni mensili che mangiano il tuo margine."
            ].map((text, i) => (
              <Reveal key={i} variant="up" delay={i * 0.1}>
                <div className="card-dark group hover:border-orange/50 transition-colors">
                  <div className="flex items-start gap-4">
                    <div className="p-2 bg-orange/10 rounded-lg group-hover:bg-orange/20 transition-colors">
                      <Check className="w-5 h-5 text-orange" />
                    </div>
                    <p className="text-lg text-foreground opacity-90">{text}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
          
          <Reveal variant="up" delay={0.5} className="mt-16 text-center">
            <p className="text-2xl text-silver-white italic">
              C'è un'infrastruttura d'acciaio per automatizzare l'eccellenza.
            </p>
          </Reveal>
        </div>
      </section>

      {/* SLIDE 3: OUTREACH FACTORY */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink px-6 py-24">
        <div className="corner-tl"></div><div className="corner-tr"></div>
        <div className="max-w-5xl w-full grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div className="z-10">
            <Reveal variant="left">
              <div className="bubble-orange w-fit mb-8">
                <Mail className="w-4 h-4" /> 01. OUTREACH FACTORY
              </div>
              <h2 className="text-5xl md:text-6xl font-bold tracking-tighter mb-8 leading-[1.08]">
                Acquisisci clienti <br />
                <span className="text-silver-orange hl-thin">in automatico, 24/7</span>
              </h2>
              <p className="text-xl text-silver-dim mb-12 leading-relaxed">
                Gmail e Social Media su pilota automatico. Il sistema estrae i lead dai profili giusti e personalizza ogni messaggio via AI.
              </p>
              <div className="space-y-4">
                {["300+ email/gg", "Comportamento Umano", "Qualificazione AI", "Zero canoni mensili"].map((item, i) => (
                  <Reveal key={i} variant="left" delay={i * 0.1} className="flex items-center gap-3 text-lg font-medium">
                    <div className="w-2 h-2 bg-orange rounded-full shadow-[0_0_8px_#fb4604]" /> {item}
                  </Reveal>
                ))}
              </div>
            </Reveal>
          </div>
          <Reveal variant="right" className="flex justify-center">
            <div className="stat-card-silver w-full max-w-sm transform rotate-3 hover:rotate-0 transition-transform duration-500">
              <div className="text-7xl font-black text-orange mb-2">
                <CountUp to={300} suffix="+" />
              </div>
              <div className="text-sm font-bold uppercase tracking-widest text-ink-2 opacity-60 mb-4">Email / Giorno</div>
              <div className="h-px bg-ink/10 w-full mb-4" />
              <div className="text-ink-2 font-medium">Zero Ban · Safe Automation</div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* SLIDE 4: CONTENT FACTORY */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink-2 px-6 py-24">
        <div className="corner-tl"></div><div className="corner-tr"></div>
        <div className="max-w-5xl w-full grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div className="order-2 md:order-1 flex justify-center">
            <Reveal variant="right">
              <div className="stat-card-silver w-full max-w-sm transform -rotate-3 hover:rotate-0 transition-transform duration-500">
                <div className="text-7xl font-black text-orange mb-2">
                  100%
                </div>
                <div className="text-sm font-bold uppercase tracking-widest text-ink-2 opacity-60 mb-4">Automazione Visiva</div>
                <div className="h-px bg-ink/10 w-full mb-4" />
                <div className="text-ink-2 font-medium">Caroselli · Script · Caption</div>
              </div>
            </Reveal>
          </div>
          <div className="order-1 md:order-2 z-10">
            <Reveal variant="right">
              <div className="bubble-orange w-fit mb-8">
                <Layout className="w-4 h-4" /> 02. CONTENT FACTORY
              </div>
              <h2 className="text-5xl md:text-6xl font-bold tracking-tighter mb-8 leading-[1.08]">
                Genera e pubblica <br />
                <span className="text-silver-orange hl-thin">contenuti in automatico</span>
              </h2>
              <p className="text-xl text-silver-dim mb-12 leading-relaxed">
                L'AI genera il copy, il motore di automazione costruisce le grafiche visive e organizza tutto su Google Drive.
              </p>
              <div className="space-y-4">
                {["Caroselli IG via AI", "Script Video & Caption", "Organizzazione Drive", "Framework CRO"].map((item, i) => (
                  <Reveal key={i} variant="right" delay={i * 0.1} className="flex items-center gap-3 text-lg font-medium">
                    <div className="w-2 h-2 bg-orange rounded-full shadow-[0_0_8px_#fb4604]" /> {item}
                  </Reveal>
                ))}
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* SLIDE 5: SECOND BRAIN */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink px-6 py-24">
        <div className="corner-tl"></div><div className="corner-tr"></div>
        <div className="max-w-5xl w-full grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div className="z-10">
            <Reveal variant="left">
              <div className="bubble-orange w-fit mb-8">
                <Brain className="w-4 h-4" /> 03. SECOND BRAIN
              </div>
              <h2 className="text-5xl md:text-6xl font-bold tracking-tighter mb-8 leading-[1.08]">
                L'AI che <br />
                <span className="text-silver-orange hl-thin">conosce davvero il tuo business</span>
              </h2>
              <p className="text-xl text-silver-dim mb-12 leading-relaxed">
                Una knowledge base interconnessa — visualizzata come grafo — che dà all'LLM il contesto permanente.
              </p>
              <div className="space-y-4">
                {["Knowledge Graph proprietario", "Memoria Permanente", "Context Engineering", "No più prompt ripetitivi"].map((item, i) => (
                  <Reveal key={i} variant="left" delay={i * 0.1} className="flex items-center gap-3 text-lg font-medium">
                    <div className="w-2 h-2 bg-orange rounded-full shadow-[0_0_8px_#fb4604]" /> {item}
                  </Reveal>
                ))}
              </div>
            </Reveal>
          </div>
          <Reveal variant="right" className="flex justify-center">
            <div className="stat-card-silver w-full max-w-sm transform rotate-6 hover:rotate-0 transition-transform duration-500">
              <div className="text-7xl font-black text-orange mb-2">∞</div>
              <div className="text-sm font-bold uppercase tracking-widest text-ink-2 opacity-60 mb-4">Memoria Permanente</div>
              <div className="h-px bg-ink/10 w-full mb-4" />
              <div className="text-ink-2 font-medium">Context Engineering Avanzato</div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* SLIDE 6: THE EDGE */}
      <section className="min-h-screen w-full flex items-center justify-center bg-orange px-6 py-24 relative overflow-hidden">
        <div className="bubble-silver w-fit mb-8 relative z-10">
          <Cpu className="w-4 h-4" /> Il Vantaggio Empire
        </div>
        <div className="max-w-4xl w-full text-center z-10">
          <Reveal variant="up">
            <h2 className="text-6xl md:text-8xl font-black tracking-tighter mb-12 leading-[1.08] text-white">
              Codice tuo <br />
              <span className="underline decoration-white underline-offset-8">per sempre.</span>
            </h2>
            <p className="text-2xl text-white/80 mb-16 max-w-2xl mx-auto">
              Non è un altro SaaS. È un'infrastruttura d'acciaio installata sui <strong>tuoi server</strong>.
            </p>
          </Reveal>
          
          <Reveal variant="up" delay={0.2}>
            <div className="card-dark max-w-2xl mx-auto border-white/20 bg-white/5 backdrop-blur-sm">
              <ul className="grid grid-cols-1 md:grid-cols-3 gap-8">
                {[
                  { t: "Zero canoni", d: "Niente abbonamenti mensili" },
                  { t: "Proprietà", d: "Codice sorgente incluso" },
                  { t: "Privacy", d: "Dati sui tuoi server" }
                ].map((item, i) => (
                  <li key={i} className="text-center">
                    <div className="text-orange font-bold text-xl mb-2">{item.t}</div>
                    <div className="text-sm text-silver-dim">{item.d}</div>
                  </li>
                ))}
              </ul>
            </div>
          </Reveal>
        </div>
      </section>

      {/* SLIDE 7: CTA FINAL */}
      <section className="min-h-screen w-full flex items-center justify-center bg-ink-2 px-6 py-24 relative">
        <div className="corner-tl"></div><div className="corner-tr"></div>
        <div className="corner-bl"></div><div className="corner-br"></div>
        
        <div className="max-w-3xl w-full text-center z-10">
          <Reveal variant="up">
            <div className="bubble-orange mx-auto w-fit mb-8">
              <ArrowRight className="w-4 h-4" /> Ultimo Step
            </div>
            <h2 className="text-6xl md:text-8xl font-bold tracking-tighter mb-8 leading-[1.08]">
              Pronto a <span className="hl-block">scalare</span> l'operatività?
            </h2>
            <p className="text-xl text-silver-dim mb-16 leading-relaxed">
              Prendiamo l'infrastruttura che uso ogni giorno e la cuciamo su misura per il tuo brand.
            </p>
          </Reveal>
          
          <Reveal variant="up" delay={0.2}>
            <a href="https://calendly.com/max-infoproducer/30min" className="btn-orange text-2xl px-12 py-6">
              Prenota Call Strategica
              <ArrowRight className="w-6 h-6" />
            </a>
            <p className="mt-8 text-sm text-silver-dim opacity-60">
              Esclusivamente per Creator, Coach & Business Owner
            </p>
          </Reveal>
        </div>
      </section>
    </main>
  );
}