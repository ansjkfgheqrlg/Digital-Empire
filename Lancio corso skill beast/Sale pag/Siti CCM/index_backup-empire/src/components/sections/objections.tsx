"use client";

import { Reveal } from "@/components/reveal";
import { ShieldCheck, Zap, Sparkles, Target } from "lucide-react";

const groups = [
  {
    icon: Zap,
    eyebrow: "Obiezione #01 · Il tempo",
    title: "\u201CNon ho tempo per un altro corso.\u201D",
    kicker: "Non è un corso. È un moltiplicatore.",
    cards: [
      { kind: "CLAIM", t: "L'AI è il tuo leverage, non un impegno.", d: "Non aggiungi lavoro: sottrai ore. Orchestri Agenti e Skill che eseguono al posto tuo mentre ti occupi di strategia.", w: "C" },
      { kind: "PROOF", t: "Framework W.O.R.K. — 10× sul tempo.", d: "Task da 4 ore compressi in 12 minuti di esecuzione deterministica. Misurato, non promesso.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Libertà operativa totale.", d: "I tuoi System AI lavorano in background: tu resti sulla strategia, sulle vendite e sui clienti.", w: "B" },
    ],
  },
  {
    icon: Sparkles,
    eyebrow: "Obiezione #02 · La tecnica",
    title: "\u201CNon sono un programmatore, è troppo tecnico.\u201D",
    kicker: "Zero righe da scrivere. Tu dirigi, l'AI esegue.",
    cards: [
      { kind: "CLAIM", t: "Non si programma. Si architetta.", d: "Impari a progettare Agenti, Skill e System Prompt nell'ecosistema Claude. L'AI scrive il codice al posto tuo.", w: "C" },
      { kind: "PROOF", t: "Framework I.C.R.O. come bussola.", d: "Binari testati su Claude Code, Projects, Cowork, Perplexity e Manus. Risultati pro senza una riga di Python o JS.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Ti posizioni sopra il 99%.", d: "Diventi chi costruisce sistemi, non chi chatta. È la differenza tra utente e architetto.", w: "B" },
    ],
  },
  {
    icon: Target,
    eyebrow: "Obiezione #03 · Il prezzo",
    title: "\u201CIl prezzo è troppo alto per un corso.\u201D",
    kicker: "Non compri un corso. Compri una skill perpetua.",
    cards: [
      { kind: "CLAIM", t: "Un singolo asset ripaga 2× il corso.", d: "Un System AI venduto a un cliente copre due volte l'investimento totale. Bastano uno o due progetti.", w: "C" },
      { kind: "PROOF", t: "Prima commessa entro le 6 settimane.", d: "Molti Builder chiudono la prima commessa da €500 prima ancora di finire il percorso core. Modulo 5 dedicato alla monetizzazione.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Stampi valore on-demand.", d: "In un mercato vergine, questa è la skill che non si svaluta: più l'AI cresce, più vale chi sa architettarla.", w: "B" },
    ],
  },
  {
    icon: ShieldCheck,
    eyebrow: "Obiezione #04 · L'obsolescenza",
    title: "\u201CL'AI cambia ogni mese. Quello che imparo diventa obsoleto.\u201D",
    kicker: "Impari a leggere il mercato, non a inseguire i tool.",
    cards: [
      { kind: "CLAIM", t: "Metodo, non moda.", d: "Framework proprietari (I.C.R.O., S.K.I.L.L., W.O.R.K., D.A.N.) restano validi indipendentemente dal modello sotto. Cambia il tool, non l'architettura.", w: "C" },
      { kind: "PROOF", t: "Modulo Ricerca di Mercato.", d: "La verità che nessuno spiega: come validare domanda reale prima di costruire. La skill più importante del futuro.", w: "P", isGold: true },
      { kind: "BENEFIT", t: "Anti-fragile per costruzione.", d: "Più il mercato accelera, più vale chi sa orchestrare. Tu non rincorri: detti il ritmo.", w: "B" },
    ],
  },
];

export function Objections() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-20">
          <Reveal>
            <span className="bubble-orange mb-6">Gestione Obiezioni // Elite Builder</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Le 4 obiezioni che </span>
              <span className="text-orange-pure italic font-medium">demoliamo</span>
              <span className="text-silver-black"> prima di iniziare.</span>
            </h2>
          </Reveal>
        </div>

        {groups.map((g, gi) => {
          const Icon = g.icon;
          return (
            <div key={gi} className={gi !== 0 ? "mt-28" : ""}>
              <Reveal>
                <div className="relative max-w-3xl mx-auto mb-12">
                  <div
                    aria-hidden="true"
                    className="absolute -top-6 -left-2 md:-left-6 select-none pointer-events-none"
                    style={{
                      fontFamily: "var(--font-serif), Georgia, serif",
                      fontStyle: "italic",
                      fontSize: "140px",
                      lineHeight: 1,
                      color: "#fb4604",
                      opacity: 0.18,
                    }}
                  >
                    &ldquo;
                  </div>
                  <div className="relative text-center">
                    <div className="flex items-center justify-center gap-2 mb-4">
                      <Icon className="h-4 w-4 text-orange-pure" />
                      <span className="text-[11px] uppercase tracking-[0.25em] font-black text-orange-pure">
                        {g.eyebrow}
                      </span>
                    </div>
                    <h3
                      className="text-[22px] md:text-[32px] leading-tight text-[#1c1c1c] mb-4"
                      style={{
                        fontFamily: "var(--font-serif), Georgia, serif",
                        fontStyle: "italic",
                        fontWeight: 400,
                        letterSpacing: "-0.01em",
                      }}
                    >
                      {g.title}
                    </h3>
                    <p className="text-[15px] md:text-[16px] text-[#fb4604] font-bold uppercase tracking-[0.12em]">
                      → {g.kicker}
                    </p>
                  </div>
                </div>
              </Reveal>

              <div className="grid md:grid-cols-3 gap-5">
                {g.cards.map((c, i) => (
                  <Reveal key={i} delay={0.15 + i * 0.1}>
                    <div
                      className={`relative overflow-hidden p-8 rounded-2xl border h-full transition-all duration-300 hover:-translate-y-1.5 ${
                        c.isGold
                          ? "bg-gradient-to-br from-orange-pure/10 via-orange-pure/5 to-transparent border-orange-pure/40 shadow-[0_8px_30px_-12px_rgba(251,70,4,0.35)]"
                          : "bg-white/60 border-[#1c1c1c]/10 hover:border-[#1c1c1c]/25 shadow-[0_4px_20px_-8px_rgba(0,0,0,0.12)]"
                      }`}
                    >
                      <div className="flex items-center gap-2 mb-6">
                        <span
                          className={`inline-block w-6 h-[2px] ${
                            c.isGold ? "bg-orange-pure" : "bg-[#1c1c1c]/40"
                          }`}
                        />
                        <span
                          className={`text-[10px] uppercase tracking-[0.22em] font-black ${
                            c.isGold ? "text-orange-pure" : "text-[#1c1c1c]/55"
                          }`}
                        >
                          0{i + 1} // {c.kind}
                        </span>
                      </div>
                      <h4 className="text-lg font-black text-silver-black mb-4 leading-tight">
                        {c.t}
                      </h4>
                      <p className="text-[#2a2a2a] text-sm leading-relaxed relative z-10">
                        {c.d}
                      </p>
                      <div className="absolute bottom-[-14px] right-1 text-[130px] font-black leading-none pointer-events-none select-none"
                        style={{
                          color: c.isGold ? "rgba(251,70,4,0.08)" : "rgba(28,28,28,0.035)",
                          fontFamily: "var(--font-serif), Georgia, serif",
                          fontStyle: "italic",
                        }}
                      >
                        {c.w}
                      </div>
                    </div>
                  </Reveal>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
