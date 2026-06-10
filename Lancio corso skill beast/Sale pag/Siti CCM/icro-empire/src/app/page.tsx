"use client";

import { Check, X, Sparkles, Shield, Zap } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { OptinForm } from "@/components/optin-form";

const ICRO = [
  {
    letter: "I",
    name: "identità",
    desc: (
      <>
        definisci <strong className="text-silver-orange font-semibold">chi</strong> sei e cosa fai.
        Claude Code lavora <strong className="text-silver-orange font-semibold">meglio</strong> quando
        sa con chi sta parlando.
      </>
    ),
  },
  {
    letter: "C",
    name: "contesto",
    desc: (
      <>
        dai il <strong className="text-silver-orange font-semibold">contesto</strong> del progetto.
        più contesto dai, più l'output è{" "}
        <strong className="text-silver-orange font-semibold">preciso</strong>.
      </>
    ),
  },
  {
    letter: "R",
    name: "regole",
    desc: (
      <>
        stabilisci le <strong className="text-silver-orange font-semibold">regole</strong> del gioco.
        vincoli, formati, tono di voce, cosa{" "}
        <strong className="text-silver-orange font-semibold">non</strong> fare.
      </>
    ),
  },
  {
    letter: "O",
    name: "output",
    desc: (
      <>
        descrivi l'<strong className="text-silver-orange font-semibold">output</strong> esatto che
        vuoi. l'AI non indovina, va{" "}
        <strong className="text-silver-orange font-semibold">guidata</strong>.
      </>
    ),
  },
];

const PROBLEMS = [
  {
    title: "Output Generici e Mediocri",
    bullets: [
      "Apri ChatGPT, scrivi un prompt, ma il risultato è sempre troppo basico.",
      "Riscrivi e modifichi all'infinito, per copiare infine un testo mediocre.",
    ],
  },
  {
    title: "Prompt Magici Fallimentari",
    bullets: [
      "Usi template trovati nei video su YouTube che promettono miracoli.",
      "I risultati sul tuo caso specifico sono scadenti e non applicabili in azienda.",
    ],
  },
  {
    title: "Assenza di Metodo Strutturato",
    bullets: [
      "Il problema non è mai lo strumento, sei tu a pilotarlo in modo casuale.",
      "Manca una logica sistematica che assicuri efficienza e risultati prevedibili.",
    ],
  },
];

const OBJECTIONS = [
  {
    q: "Ma è davvero ",
    qi: "gratis?",
    cards: [
      {
        label: "01 // claim",
        title: "zero costi nascosti",
        text: (
          <>
            Sì. <strong>12 pagine</strong>, 1 framework, 1 template. Nessun costo nascosto, nessun{" "}
            <strong>upsell</strong> forzato.
          </>
        ),
      },
      {
        label: "02 // proof",
        title: "nome, email, ricevi",
        text: (
          <>
            Inserisci <strong>nome</strong> e email, ricevi il PDF in <strong>inbox</strong>. Fine.
            Nessuna carta di credito richiesta.
          </>
        ),
      },
      {
        label: "03 // benefit",
        title: "applicabile istantaneamente",
        text: (
          <>
            Un <strong>sistema</strong> che puoi applicare in <strong>10 minuti</strong>. Valore
            immediato, zero rischio ed estrema fluidità operativa.
          </>
        ),
      },
    ],
  },
  {
    q: "Serve saper ",
    qi: "programmare?",
    cards: [
      {
        label: "01 // claim",
        title: "zero codice richiesto",
        text: (
          <>
            <strong>Zero</strong> codice richiesto. Il framework funziona con{" "}
            <strong>istruzioni</strong> in italiano, se sai parlare sai generare risultati.
          </>
        ),
      },
      {
        label: "02 // proof",
        title: "si compila con parole",
        text: (
          <>
            Il template CLAUDE.md si compila con <strong>parole</strong> e definizioni strategiche
            basate sulla logica.
          </>
        ),
      },
      {
        label: "03 // benefit",
        title: "accessibile a chiunque",
        text: (
          <>
            L'intelligenza artificiale lavora e scrive per te, tu devi solo applicare le logiche{" "}
            <strong>comunicative e operative</strong> corrette descritte.
          </>
        ),
      },
    ],
  },
];

export default function Page() {
  return (
    <main className="relative">
      {/* HEADER */}
      <header className="relative z-10 pt-10 pb-2 bg-ink">
        <div className="max-w-5xl mx-auto px-6 flex items-center justify-center gap-3">
          <div
            className="w-9 h-9 rounded-lg flex items-center justify-center text-[11px] font-bold text-black"
            style={{ background: "linear-gradient(145deg, #e8e3ef, #ff8a4a)" }}
            aria-hidden
          >
            CC
          </div>
          <span className="text-sm tracking-[0.12em] uppercase text-white/60">
            Claude Code Mastery
          </span>
        </div>
      </header>

      {/* HERO */}
      <section className="bg-ink relative overflow-hidden">
        <div
          className="border-b border-white/20 overflow-hidden py-3 relative mt-6"
          style={{
            backgroundImage:
              "linear-gradient(135deg, #ffffff 0%, #e8e3ef 25%, #d9d4e1 45%, #ff8a4a 80%, #fb4604 100%)",
            boxShadow:
              "0 2px 0 rgba(255,255,255,0.6) inset, 0 -2px 0 rgba(201,55,10,0.25) inset",
          }}
        >
          <div
            className="marquee flex gap-10 whitespace-nowrap text-xs uppercase tracking-[0.25em] font-bold text-[#1c1c1c]"
            style={{ width: "max-content" }}
          >
            {Array.from({ length: 12 }).map((_, i) => (
              <span key={i} className="flex items-center gap-10">
                <span>Framework I.C.R.O.</span>
                <span className="text-[#c9370a]">✦</span>
                <span>12 pagine · gratis</span>
                <span className="text-[#c9370a]">✦</span>
                <span>Template CLAUDE.md incluso</span>
                <span className="text-[#c9370a]">✦</span>
                <span>by Digital Empire</span>
                <span className="text-[#c9370a]">✦</span>
              </span>
            ))}
          </div>
        </div>

        <div className="max-w-3xl mx-auto px-6 py-20 md:py-28 text-center relative">
          <span className="silver-chip float-a" style={{ top: "10%", left: "-4%" }}>
            <span className="dot" /> <strong>zero</strong> codice
          </span>
          <span className="silver-chip float-b" style={{ top: "20%", right: "-14%" }}>
            <span className="dot" /> <strong>12</strong> pagine
          </span>
          <span className="silver-chip float-c" style={{ bottom: "22%", left: "-2%" }}>
            <span className="dot" /> <strong>10 min</strong> per compilare
          </span>
          <span className="silver-chip float-d" style={{ bottom: "12%", right: "-3%" }}>
            <span className="dot" /> <strong>100%</strong> gratis
          </span>

          <Reveal>
            <span className="bubble-orange mb-6">
              <Sparkles className="h-3.5 w-3.5" /> il primo percorso italiano completo su Claude Code
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-[40px] md:text-[60px] font-bold leading-[1.08] tracking-tight mb-7 mt-4">
              <span className="text-silver-white">il Framework I.C.R.O.</span>
              <br />
              <span className="text-silver-orange">
                il metodo in 1 pagina che trasforma Claude Code nel tuo collaboratore perfetto
              </span>
            </h1>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[15px] md:text-base text-white/70 max-w-2xl mx-auto mb-10 leading-[1.75]">
              <strong className="text-silver-orange font-semibold">12 pagine.</strong> 1 framework.{" "}
              <strong className="text-silver-orange font-semibold">1 template</strong> pronto.{" "}
              <span className="hl-block">gratis.</span>
            </p>
          </Reveal>

          <Reveal delay={0.25}>
            <ul className="max-w-xl mx-auto text-left flex flex-col gap-4 mb-10">
              {[
                <>
                  il framework <strong className="text-silver-orange font-semibold">I.C.R.O.</strong>{" "}
                  in 4 step: la{" "}
                  <strong className="text-silver-orange font-semibold">struttura esatta</strong> per
                  dare istruzioni che producono output prevedibili
                </>,
                <>
                  1 template <strong className="text-silver-orange font-semibold">CLAUDE.md</strong>{" "}
                  compilabile, lo compili in{" "}
                  <strong className="text-silver-orange font-semibold">10 minuti</strong>
                </>,
                <>
                  per chi usa l'AI ma{" "}
                  <strong className="text-silver-orange font-semibold">non sa</strong> come andare
                  oltre{" "}
                  <strong className="text-silver-orange font-semibold">
                    "copia incolla da ChatGPT"
                  </strong>
                </>,
                <>
                  <strong className="text-silver-orange font-semibold">zero codice</strong>{" "}
                  richiesto, applicabile dal{" "}
                  <strong className="text-silver-orange font-semibold">primo minuto</strong>
                </>,
              ].map((item, i) => (
                <li key={i} className="flex items-start gap-3 text-white/85 leading-relaxed">
                  <span className="shrink-0 mt-1 w-5 h-5 rounded-md border border-orange-pure/30 bg-orange-pure/10 flex items-center justify-center">
                    <Check className="h-3 w-3 text-orange-pure" strokeWidth={2.5} />
                  </span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </Reveal>

          <Reveal delay={0.3}>
            <OptinForm id="hero" />
          </Reveal>

          <Reveal delay={0.35}>
            <p className="mt-6 text-xs text-white/50 flex items-center justify-center gap-2">
              <Shield className="h-3.5 w-3.5" /> i tuoi dati sono al sicuro.
            </p>
          </Reveal>
        </div>
      </section>

      {/* STATS */}
      <section className="bg-ink section">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-3 gap-5">
          {[
            { n: 40, suf: "+", label: "Ore Risparmiate / Mese" },
            { n: 99, suf: "%", label: "Errori Operativi Eliminati" },
            { n: 3, suf: "x", label: "Velocità di Delivery" },
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

      {/* PROBLEMA */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal>
            <span className="bubble-ink mb-6">il vero problema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-[1.1] mb-6 mt-6 max-w-[22ch]">
              <span className="text-silver-black">stai usando l'AI nel</span>{" "}
              <span className="text-orange-pure italic font-medium">modo sbagliato.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <p className="text-lg text-[#3a3a3a] mb-10 max-w-[60ch] leading-relaxed">
              e non è <strong>colpa</strong> tua. tutti ti dicono "usa l'AI", ma nessuno ti dà un{" "}
              <strong>sistema</strong> per farlo davvero.
            </p>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-5">
            {PROBLEMS.map((p, i) => (
              <Reveal key={i} delay={0.15 + i * 0.08}>
                <div className="card-paper h-full">
                  <h3 className="text-lg font-semibold mb-3 text-[#1a1a1a]">{p.title}</h3>
                  <ul className="space-y-2 text-[#3a3a3a] text-[15px] leading-relaxed">
                    {p.bullets.map((b, j) => (
                      <li key={j} className="flex gap-2">
                        <span className="text-orange-pure">•</span>
                        <span>{b}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* SOLUZIONE ICRO */}
      <section id="soluzione" className="bg-ink section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Zap className="h-3.5 w-3.5" /> la soluzione
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6 max-w-[18ch]">
              <span className="text-silver-white">il framework</span>{" "}
              <span className="text-silver-orange">I.C.R.O.</span>
              <br />
              <span className="text-silver-white">cambia</span>{" "}
              <span className="text-silver-orange italic font-medium">tutto.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-5">
            {ICRO.map((f, i) => (
              <Reveal key={f.letter} delay={0.1 + i * 0.08}>
                <div className="card-dark h-full text-center">
                  <div className="text-6xl font-bold text-silver-orange leading-none mb-3">
                    {f.letter}
                  </div>
                  <p className="text-base font-semibold text-white/90 mb-2">{f.name}</p>
                  <p className="text-sm text-white/65 leading-relaxed">{f.desc}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* COSA CONTIENE */}
      <section id="contenuto" className="bg-paper section section-border-t">
        <div className="max-w-3xl mx-auto px-6">
          <Reveal>
            <span className="bubble-orange mb-6">cosa contiene</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-[1.1] mb-10 mt-6">
              <span className="text-silver-black">12 pagine, 1 sistema</span>{" "}
              <span className="text-orange-pure italic font-medium">completo.</span>
            </h2>
          </Reveal>
          <ul className="flex flex-col gap-3">
            {[
              <>
                il framework <strong>I.C.R.O.</strong> spiegato step by step con{" "}
                <strong>esempi</strong> reali
              </>,
              <>
                1 template <strong>CLAUDE.md</strong> pronto da compilare in{" "}
                <strong>10 minuti</strong>
              </>,
              <>
                la differenza tra <strong>chattare</strong> con l'AI e <strong>costruire</strong> con
                l'AI
              </>,
              <>
                come passare da <strong>prompt</strong> casuali a istruzioni{" "}
                <strong>prevedibili</strong>
              </>,
              <>
                applicabile da <strong>subito</strong>, zero codice, zero{" "}
                <strong>esperienza</strong> tecnica richiesta
              </>,
            ].map((item, i) => (
              <Reveal key={i} delay={0.1 + i * 0.05}>
                <li className="card-paper flex items-start gap-3 text-[15px] text-[#3a3a3a] leading-relaxed">
                  <Check className="h-5 w-5 text-orange-pure shrink-0 mt-0.5" strokeWidth={2.5} />
                  <span>{item}</span>
                </li>
              </Reveal>
            ))}
          </ul>
        </div>
      </section>

      {/* PER CHI È */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <span className="bubble-orange mb-6">è per te?</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6 max-w-[22ch]">
              <span className="text-silver-white">questo PDF è per chi vuole</span>{" "}
              <span className="text-silver-orange">risultati</span>
              <span className="text-silver-white">, non</span>{" "}
              <span className="text-silver-orange italic font-medium">teoria.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-6">
            <Reveal delay={0.1}>
              <div className="card-silver-fill h-full">
                <div className="bubble-orange mb-5">
                  <Check className="h-3.5 w-3.5" /> è per te se
                </div>
                <ul className="space-y-3.5 text-[#1c1c1c]">
                  {[
                    <>
                      usi <strong className="text-orange-pure font-bold">ChatGPT</strong> o
                      Claude ma i risultati sono{" "}
                      <strong className="text-orange-pure font-bold">inconsistenti</strong>
                    </>,
                    <>
                      vuoi un <strong className="text-orange-pure font-bold">metodo</strong>{" "}
                      chiaro, non l'ennesimo{" "}
                      <strong className="text-orange-pure font-bold">tutorial</strong>
                    </>,
                    <>
                      non sai{" "}
                      <strong className="text-orange-pure font-bold">programmare</strong> e non
                      vuoi <strong className="text-orange-pure font-bold">imparare</strong>
                    </>,
                  ].map((s, i) => (
                    <li key={i} className="flex gap-3">
                      <Check className="h-5 w-5 text-orange-pure shrink-0 mt-0.5" />
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>
            <Reveal delay={0.2}>
              <div className="card-silver-fill h-full">
                <div className="bubble-ink mb-5">
                  <X className="h-3.5 w-3.5" /> NON è per te se
                </div>
                <ul className="space-y-3.5 text-[#1c1c1c]">
                  {[
                    <>
                      sei già un <strong>developer</strong> esperto di Claude <strong>Code</strong>
                    </>,
                    <>
                      cerchi un corso <strong>completo</strong>, questo è un{" "}
                      <strong>punto di partenza</strong>
                    </>,
                  ].map((s, i) => (
                    <li key={i} className="flex gap-3">
                      <X className="h-5 w-5 text-[#1c1c1c]/50 shrink-0 mt-0.5" />
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* OBIEZIONI CPB */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <span className="bubble-ink mb-6">gestione obiezioni // protocollo CPB</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-[1.1] mb-14 mt-6">
              <span className="text-silver-black">le obiezioni più comuni</span>{" "}
              <span className="text-orange-pure italic font-medium">(e le risposte).</span>
            </h2>
          </Reveal>

          <div className="flex flex-col gap-16">
            {OBJECTIONS.map((obj, idx) => (
              <div key={idx}>
                <Reveal>
                  <h3 className="text-[26px] md:text-[38px] font-extrabold uppercase text-[#1a1924] text-center mb-10 leading-tight tracking-tight">
                    "{obj.q}
                    <em
                      className="italic text-[#7b7582] font-extrabold"
                      style={{ fontFamily: "serif" }}
                    >
                      {obj.qi}
                    </em>
                    "
                  </h3>
                </Reveal>
                <div className="grid md:grid-cols-3 gap-5">
                  {obj.cards.map((c, i) => {
                    const isProof = c.label.includes("proof");
                    return (
                      <Reveal key={i} delay={i * 0.08}>
                        <div
                          className={`${isProof ? "" : "card-paper"} h-full rounded-2xl p-7 ${
                            isProof ? "" : ""
                          }`}
                          style={
                            isProof
                              ? {
                                  background:
                                    "linear-gradient(145deg, #fce19a 0%, #e6a845 100%)",
                                  boxShadow:
                                    "12px 16px 36px rgba(230,168,69,0.25), -10px -10px 30px rgba(255,255,255,0.9)",
                                  border: "1px solid rgba(255,255,255,0.6)",
                                  color: "#2a1f0a",
                                }
                              : undefined
                          }
                        >
                          <span
                            className={`text-[11px] font-bold uppercase tracking-[0.15em] ${
                              isProof ? "text-[#5c4115]" : "text-[#6a6570]"
                            } block mb-3`}
                          >
                            {c.label}
                          </span>
                          <h4
                            className={`text-base md:text-lg font-extrabold uppercase leading-tight mb-3 ${
                              isProof ? "text-[#2a1f0a]" : "text-[#1a1924]"
                            }`}
                          >
                            {c.title}
                          </h4>
                          <p
                            className={`text-[14px] leading-relaxed ${
                              isProof ? "text-[#2a1f0a]" : "text-[#3a3530]"
                            }`}
                          >
                            {c.text}
                          </p>
                        </div>
                      </Reveal>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA FINALE */}
      <section id="scarica" className="bg-ink-2 section section-border-t">
        <div className="max-w-2xl mx-auto px-6 text-center">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Sparkles className="h-3.5 w-3.5" /> scarica ora
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-6 mt-6">
              <span className="text-silver-white">scarica il framework</span>{" "}
              <span className="text-silver-orange italic font-medium">I.C.R.O.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <p className="text-white/70 mb-10 leading-relaxed">
              <strong className="text-silver-orange font-semibold">12 pagine</strong>, 1 template
              pronto, <strong className="text-silver-orange font-semibold">zero codice</strong>. il
              sistema per dare istruzioni che funzionano.
            </p>
          </Reveal>
          <Reveal delay={0.2}>
            <OptinForm id="final" />
          </Reveal>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-ink-2 py-10 text-center text-xs text-white/40 tracking-wider">
        © 2026 Digital Empire
      </footer>
    </main>
  );
}
