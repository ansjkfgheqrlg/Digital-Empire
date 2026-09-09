"use client";

import { ArrowRight, Check, X, Sparkles, Zap, Clock, Shield } from "lucide-react";
import { Reveal } from "@/components/reveal";
import { CountUp } from "@/components/count-up";
import { StickyCTA } from "@/components/sticky-cta";

const BOOKING_URL = "https://clinquant-pie-aab8d2.netlify.app/";

function CTA({ large = false, label = "Prenota la Tua Call Gratis" }: { large?: boolean; label?: string }) {
  return (
    <a href={BOOKING_URL} className={`btn-orange ${large ? "btn-orange--lg" : ""} group`}>
      {label}
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
                <span>Call 1:1 Gratis</span>
                <span className="text-orange-pure">✦</span>
                <span>45 Minuti</span>
                <span className="text-orange-pure">✦</span>
                <span>Claude Code Mastery</span>
                <span className="text-orange-pure">✦</span>
                <span>by Digital Empire</span>
                <span className="text-orange-pure">✦</span>
              </span>
            ))}
          </div>
        </div>

        <div className="max-w-5xl mx-auto px-6 py-24 md:py-36 text-center relative">
          <span className="silver-chip float-a" style={{ top: "12%", left: "-4%" }}>
            <span className="dot" /> <strong>100%</strong> gratis
          </span>
          <span className="silver-chip float-b" style={{ top: "22%", right: "-6%" }}>
            <span className="dot" /> Screen share <strong>live</strong>
          </span>
          <span className="silver-chip float-c" style={{ bottom: "18%", left: "-2%" }}>
            <span className="dot" /> <strong>90%</strong> formazione
          </span>
          <span className="silver-chip float-d" style={{ bottom: "10%", right: "-3%" }}>
            <span className="dot" /> <strong>1:1</strong> · solo tu e me
          </span>

          <Reveal>
            <span className="bubble-orange mb-6">
              <Sparkles className="h-3.5 w-3.5" /> Posti limitati · Solo questa settimana
            </span>
          </Reveal>
          <Reveal delay={0.05}>
            <div className="pre-headline mt-4 mb-5">Digital Empire presenta · Call Strategica 1:1</div>
          </Reveal>
          <Reveal delay={0.1}>
            <h1 className="text-[42px] md:text-[64px] font-bold leading-[1.05] tracking-tight mb-7">
              <span className="text-silver-white">Ti formo su Claude Code.</span>
              <br />
              <span className="text-silver-orange">45 minuti. Gratis.</span>
            </h1>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[15px] md:text-base text-white/70 max-w-2xl mx-auto mb-10 leading-[1.75]">
              Una call <strong className="text-silver-orange font-semibold">1:1 di formazione vera</strong> su come costruire <strong className="text-silver-orange font-semibold">agenti, skill e system prompt</strong> con Claude Code (e l'ecosistema attorno: Claude chat, progetti, Perplexity, Manus). Prodotta da <strong className="text-silver-orange font-semibold">Digital Empire</strong>. Ti mostro <strong className="text-silver-orange font-semibold">come lavoro io</strong> live, con screen share,
              sul <strong className="text-silver-orange font-semibold">tuo caso reale</strong>. Niente codice da scrivere — lo scrive l'AI per noi. Giochiamo a carte scoperte:
              <span className="hl-block">90% formazione pura, 10% pitch del corso</span> — circa 4-5 minuti a fine call, solo se ti serve davvero. Se non ti serve, sono il primo a dirtelo.
            </p>
          </Reveal>
          <Reveal delay={0.3}>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <CTA large />
              <span className="text-sm text-white/50 flex items-center gap-2">
                <Shield className="h-4 w-4" /> Nessuna carta · Nessun impegno
              </span>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== STATS — 3 blocchi neri ===================== */}
      <section className="bg-ink section">
        <div className="max-w-5xl mx-auto px-6 grid md:grid-cols-3 gap-5">
          {[
            { n: 247, suf: "+", label: "Call già fatte" },
            { n: 45, suf: " min", label: "Per call" },
            { n: 100, suf: "%", label: "Gratis" },
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

      {/* ===================== ASCOLTA BENE ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[40px] md:text-[56px] font-bold leading-[1.05] mb-8">
              <span className="text-silver-white">ASCOLTA BENE.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.1}>
            <div className="space-y-5 text-lg md:text-xl text-white/80 leading-relaxed">
              <p>Stai già usando Claude. ChatGPT. Forse Cursor. E ti piacciono pure.</p>
              <p>
                Ma ogni volta che apri una chat nuova hai sempre la stessa sensazione:
                <br />
                <span className="text-silver-orange font-semibold">
                  "Questo coso è potente… ma sto grattando la superficie."
                </span>
              </p>
              <p>
                Non è un tuo limite. È che <span className="hl-block">nessuno te l'ha mai spiegato come va spiegato.</span>
              </p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== PROBLEMA (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-ink mb-6">Il vero problema</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-[1.1] mb-10 mt-6 max-w-[22ch]">
              <span className="text-silver-black">Tutti ti vendono corsi.</span>
              <br />
              <span className="text-orange-pure">Nessuno ti fa <em className="italic font-normal">vedere</em> come fa.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-5">
            <Reveal delay={0.15}>
              <div className="card-paper">
                <div className="flex items-center gap-3 mb-4">
                  <X className="h-5 w-5 text-[#b8b8b8]" />
                  <h3 className="text-xl font-semibold">Il corso tipico</h3>
                </div>
                <ul className="space-y-3 text-[#3a3a3a]">
                  <li>300 video registrati 2 anni fa</li>
                  <li>Esempi generici, zero sul tuo caso</li>
                  <li>Community Discord che nessuno legge</li>
                  <li>Ti lasciano solo dopo la prima settimana</li>
                </ul>
              </div>
            </Reveal>
            <Reveal delay={0.25}>
              <div className="card-orange">
                <div className="flex items-center gap-3 mb-4">
                  <Check className="h-5 w-5" />
                  <h3 className="text-xl font-semibold">Questa call</h3>
                </div>
                <ul className="space-y-3">
                  <li>Tu, io, 45 minuti vivi</li>
                  <li>Workflow REALI che uso oggi stesso</li>
                  <li>Domande tue, risposte dirette</li>
                  <li>Esci con qualcosa che funziona</li>
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== METODO (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Il metodo</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 mt-6">
              <span className="text-silver-black">Non parliamo di AI.</span>
              <br />
              <span className="text-orange-pure italic font-medium">Costruiamo qualcosa con l'AI.</span>
            </h2>
          </Reveal>
          <div className="space-y-5">
            {[
              { t: "Capisco dove sei oggi", d: "I primi 10 minuti sono tuoi. Mi dici cosa stai facendo, dove ti blocchi, cosa vuoi raggiungere." },
              { t: "Ti mostro come lavoro io", d: "Screen share. Ti faccio vedere 2-3 workflow reali — agenti custom, skill, system prompt — che uso ADESSO con Claude Code e il resto dello stack (Claude progetti, Perplexity, Manus)." },
              { t: "Costruiamo il tuo primo pezzo", d: "Prendiamo un tuo problema concreto e lo risolviamo live con Claude. Esci con un workflow tuo, che puoi ripetere." },
            ].map((s, i) => (
              <Reveal key={i} delay={0.15 + i * 0.08}>
                <div className="flex gap-5 card-paper">
                  <div className="step-num shrink-0">{i + 1}</div>
                  <div>
                    <h3 className="text-xl md:text-2xl font-semibold mb-1.5 text-orange-pure">{s.t}</h3>
                    <p className="text-[#3a3a3a] leading-relaxed">{s.d}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== PER CHI È / NON È ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-12 text-center">
              <span className="text-silver-white">Per chi è questa call</span>
              <br />
              <span className="text-orange-pure italic font-medium">(e per chi non è).</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-6">
            <Reveal delay={0.1}>
              <div className="card-dark h-full">
                <div className="bubble-orange mb-5"><Check className="h-3.5 w-3.5" /> È per te se</div>
                <ul className="space-y-3.5 text-white/85">
                  {[
                    "Stai già usando Claude o ChatGPT e senti di grattare la superficie",
                    "Lavori su progetti reali (contenuti, copy, agency, prodotti, sistemi interni) e vuoi andare più veloce — senza scrivere una riga",
                    "Ti interessa il metodo più che il singolo tip da Twitter",
                    "Sei disposto ad aprire screen share e mostrarmi il tuo contesto",
                  ].map((s, i) => (
                    <li key={i} className="flex gap-3"><Check className="h-5 w-5 text-orange-pure shrink-0 mt-0.5" /> <span>{s}</span></li>
                  ))}
                </ul>
              </div>
            </Reveal>
            <Reveal delay={0.2}>
              <div className="card-dark h-full">
                <div className="bubble-silver mb-5"><X className="h-3.5 w-3.5" /> NON è per te se</div>
                <ul className="space-y-3.5 text-white/60">
                  {[
                    "Cerchi un corso pre-registrato da guardare passivamente",
                    "Pensi che serva saper programmare per usare l'AI (spoiler: non serve, scrive lei)",
                    "Non sei disposto a fare due domande sincere sul tuo lavoro",
                    "Cerchi magie, hype, \"10.000€ al mese con l'AI\"",
                  ].map((s, i) => (
                    <li key={i} className="flex gap-3"><X className="h-5 w-5 text-white/40 shrink-0 mt-0.5" /> <span>{s}</span></li>
                  ))}
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== TIMELINE cosa succede ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Dopo che prenoti</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-12 mt-6">
              <span className="text-silver-black">Esattamente cosa succede</span>
              <br />
              <span className="text-orange-pure italic font-medium">nei prossimi giorni.</span>
            </h2>
          </Reveal>
          <div className="space-y-0 relative">
            {[
              { t: "Subito — Conferma + mini-form", d: "Ricevi email con link Google Meet e un form da 4 domande. 2 minuti, servono a farmi arrivare preparato." },
              { t: "24h prima — Promemoria + preparazione", d: "Ti mando un reminder con 2-3 cose da tenere a portata di mano (un problema concreto del tuo lavoro, un progetto fermo, le domande che ti porti dietro)." },
              { t: "Il giorno della call — 45 min live", d: "Ci colleghiamo. Screen share. Zero slide. Tu mi mostri, io ti mostro, costruiamo qualcosa insieme." },
              { t: "Subito dopo — Registrazione + note", d: "Se abbiamo registrato, ti arriva link + un Notion con le 3 azioni concrete da fare nelle settimane successive." },
              { t: "7 giorni dopo — Check rapido", d: "Ti scrivo per capire cosa hai applicato e se ti è stata utile davvero. Onestà brutale, in entrambe le direzioni." },
            ].map((s, i) => (
              <Reveal key={i} delay={i * 0.08}>
                <div className="flex gap-5 py-6 border-b border-[#131313]/10 last:border-b-0">
                  <div className="step-num shrink-0">{i + 1}</div>
                  <div>
                    <h3 className="text-xl md:text-2xl font-semibold mb-1.5 text-silver-black">{s.t}</h3>
                    <p className="text-[#3a3a3a] leading-relaxed">{s.d}</p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== BEFORE / AFTER ===================== */}
      <section className="bg-ink-2 section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-3 text-center">
              <span className="text-silver-white">La differenza in 45 minuti.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.08}>
            <p className="text-white/60 text-center mb-12 max-w-2xl mx-auto">Non è magia. È avere uno che ha già sbattuto contro i muri e ti fa vedere i passaggi nell'ordine giusto.</p>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-5">
            <Reveal delay={0.1}>
              <div className="card-silver-orange h-full">
                <div className="eyebrow">Prima della call</div>
                <h3 className="text-2xl font-semibold mb-5">Il loop infinito</h3>
                <ul className="space-y-3 text-[#2a2a2a]">
                  <li>• Apri Claude, scrivi un prompt, incolli, risultato mid</li>
                  <li>• Provi Cursor, poi ChatGPT, poi torni indietro</li>
                  <li>• Salvi tutorial YouTube che non guardi mai</li>
                  <li>• Hai la sensazione di essere "indietro" sull'AI</li>
                  <li>• Non sai cosa ignorare e cosa è segnale vero</li>
                </ul>
              </div>
            </Reveal>
            <Reveal delay={0.2}>
              <div className="card-silver-orange variant-orange h-full">
                <div className="eyebrow">Dopo la call</div>
                <h3 className="text-2xl font-semibold mb-5">La chiarezza</h3>
                <ul className="space-y-3 text-[#1c1c1c]">
                  <li className="flex gap-2"><Check className="h-4 w-4 text-[#c9370a] shrink-0 mt-1" /> Sai esattamente quando usare Claude vs altri tool</li>
                  <li className="flex gap-2"><Check className="h-4 w-4 text-[#c9370a] shrink-0 mt-1" /> Hai 2-3 workflow tuoi, testati live insieme</li>
                  <li className="flex gap-2"><Check className="h-4 w-4 text-[#c9370a] shrink-0 mt-1" /> Capisci la logica, non solo il prompt magico</li>
                  <li className="flex gap-2"><Check className="h-4 w-4 text-[#c9370a] shrink-0 mt-1" /> Smetti di inseguire i tutorial, esegui</li>
                  <li className="flex gap-2"><Check className="h-4 w-4 text-[#c9370a] shrink-0 mt-1" /> Sai cosa ignorare. La cosa più importante di tutte.</li>
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== VALUE STACK ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-3 text-center">
              <span className="text-silver-black">Quanto vale davvero</span>
              <br />
              <span className="text-orange-pure italic font-medium">questa sessione.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.08}>
            <p className="text-[#3a3a3a] text-center mb-12 max-w-2xl mx-auto">Non te lo dico per convincerti. Te lo dico perché "gratis" confonde e voglio che tu capisca cosa stai prendendo.</p>
          </Reveal>
          <div className="card-paper">
            {[
              { t: "Call 1:1 live da 45 minuti", v: "€ 250" },
              { t: "Audit del tuo workflow attuale", v: "€ 120" },
              { t: "2-3 workflow personalizzati (agenti / skill / system prompt)", v: "€ 300" },
              { t: "Registrazione + note Notion", v: "€ 80" },
              { t: "Check di follow-up dopo 7 giorni", v: "€ 100" },
            ].map((i, idx) => (
              <Reveal key={idx} delay={idx * 0.05}>
                <div className="flex items-center justify-between py-4 border-b border-[#131313]/10 last:border-b-0">
                  <div className="flex gap-3 items-center">
                    <Check className="h-5 w-5 text-orange-pure shrink-0" />
                    <span className="text-[#131313] font-medium">{i.t}</span>
                  </div>
                  <span className="font-bold text-[#3a3a3a]">{i.v}</span>
                </div>
              </Reveal>
            ))}
            <Reveal delay={0.3}>
              <div className="flex items-center justify-between pt-6 mt-2 border-t-2 border-[#131313]">
                <span className="text-xl font-bold">Totale valore</span>
                <span className="text-3xl font-bold text-silver-black">€ 850</span>
              </div>
              <div className="flex items-center justify-between pt-3">
                <span className="text-xl font-bold">Il tuo investimento oggi</span>
                <span className="text-4xl font-bold text-orange-pure">€ 0</span>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== MID CTA ===================== */}
      <section className="bg-ink section section-border-t text-center">
        <div className="max-w-3xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[32px] md:text-[44px] font-bold leading-tight mb-4">
              <span className="text-silver-orange">Ancora scettico?</span>
            </h2>
          </Reveal>
          <Reveal delay={0.1}>
            <p className="text-white/70 text-lg mb-8">
              È <span className="text-orange-pure font-semibold">davvero gratis</span>. Durata <span className="text-orange-pure font-semibold">45 minuti pieni</span>: 40 di formazione vera + 4-5 minuti finali di pitch del corso, solo se ti interessa. 1:1, screen share attivo, sul <span className="text-orange-pure font-semibold">tuo caso reale</span>. Nessuna carta, nessun upsell durante, nessuna mailing list che ti insegue per mesi. Se nei primi 10 minuti non senti di aver ricevuto <span className="text-orange-pure font-semibold">valore concreto</span>, chiudi e amici come prima — zero rancore, zero sensi di colpa.
            </p>
          </Reveal>
          <Reveal delay={0.2}><CTA large /></Reveal>
        </div>
      </section>

      {/* ===================== TRASPARENZA (grey) ===================== */}
      <section className="bg-grey section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Giochiamo a carte scoperte</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-10 mt-6">
              <span className="text-silver-black">"Ok ma perché me la date gratis?"</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <div className="space-y-5 text-lg text-[#2a2a2a] leading-relaxed">
              <p>Te lo dico dritto, senza giri. <strong>Digital Empire</strong> — la mia agenzia, appena nata — sta lanciando <strong>Claude Code Mastery</strong>, un corso su Claude Code.</p>
              <p>
                Potevo fare un webinar classico da 200 persone dove mi nascondo dietro una slide e parlo un'ora senza essere <span className="hl">visto davvero</span>. Non l'ho fatto. Qui siamo tu e me, faccia a faccia, 45 minuti: io <em>devo</em> darti valore, altrimenti chiudi la call.
              </p>
              <p>
                Lo scambio è onesto: <strong>tu esci con un workflow che funziona</strong> sul tuo caso, e <strong>io capisco</strong> cosa manca davvero ai corsi esistenti, così il nostro lo costruiamo giusto.
              </p>
              <p>
                Alla fine, se ha senso, ti dedico <strong>4-5 minuti massimi</strong> per raccontarti cos'è Claude Code Mastery. Non prima. Non durante. Solo alla fine, e solo se ti interessa.
              </p>
              <p className="text-orange-pure font-semibold">90% formazione. 10% pitch. Carte scoperte dal primo minuto.</p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== SCARSITÀ ===================== */}
      <section className="bg-ink-2 section section-border-t">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <Reveal><span className="bubble-silver mb-6">Posti veri, limitati veri</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-orange">Faccio max 8 call a settimana.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <p className="text-white/75 text-lg mb-10 max-w-2xl mx-auto">
              Non è marketing. È matematica. 45 min × 8 call = 6 ore di call.
              Più il tempo per preparare ogni sessione con il tuo caso specifico.
              <br />
              <span className="text-orange-pure">Quando i posti finiscono, finiscono.</span>
            </p>
          </Reveal>
          <Reveal delay={0.2}><CTA large label="Prendi il Tuo Slot" /></Reveal>
        </div>
      </section>

      {/* ===================== OBIEZIONI (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-10">
              <span className="text-silver-black">Le 3 obiezioni che ricevo sempre.</span>
            </h2>
          </Reveal>
          {[
            { q: "\"Non so se ho il livello giusto\"", a: "Non esiste livello giusto. La call si adatta a te. Che tu abbia appena aperto Claude o che ci stia costruendo sopra un business, i primi 10 minuti servono proprio a calibrare." },
            { q: "\"Sembra troppo bello per essere gratis\"", a: "Digital Empire sta lanciando Claude Code Mastery. Per costruirlo giusto ci servono conversazioni vere, non sondaggi. Negli ultimi 4-5 minuti della call, se ha senso, te ne parlo. Prima no. È scritto qui sopra così non ci sono sorprese." },
            { q: "\"Ho paura di perdere tempo\"", a: "45 minuti. Se dopo 10 non ti piace, chiudiamo. Nessun hard feelings. Ma statisticamente, su 247 call, zero chiuse in anticipo. Fai tu." },
          ].map((o, i) => (
            <Reveal key={i} delay={i * 0.08}>
              <div className="border-t border-[#131313]/10 py-7">
                <h3 className="text-xl md:text-2xl font-semibold mb-3 text-orange-pure">{o.q}</h3>
                <p className="text-[#3a3a3a] text-lg leading-relaxed">{o.a}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* ===================== CHI SONO ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Chi ti guida</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-white">"Ok ma tu chi cazzo sei?"</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <div className="space-y-5 text-lg text-white/80 leading-relaxed">
              <p>
                In call ci vediamo io, <span className="text-orange-pure font-semibold">Max</span> — founder di <strong className="text-silver-orange">Digital Empire</strong>, agenzia appena nata che costruisce prodotti e sistemi con l'AI.
              </p>
              <p>
                Da marzo 2025 ho buttato tutti gli altri tool e lavoro solo con Claude Code.
                Abbiamo spedito <span className="hl text-white">14 progetti</span> reali in questi mesi usandolo come unica IDE.
              </p>
              <p>
                Digital Empire non è un guru-brand. Non c'è un corso da $999 in vendita ora.
                Solo un team che costruisce, un laptop, un abbonamento Claude Max e un metodo che funziona.
                <br />
                <span className="text-silver-orange font-semibold">Se ti va, te lo mostro io, in 1:1.</span>
              </p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ===================== COSA ESCI CON (grey) ===================== */}
      <section className="bg-grey section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-12">
              <span className="text-silver-black">Cosa esci con, dopo 45 minuti.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-5">
            {[
              { icon: Zap, t: "Un workflow tuo", d: "Non un template. Un workflow calibrato sul tuo lavoro, testato live insieme." },
              { icon: Clock, t: "Ore recuperate", d: "Ti mostro esattamente cosa delegare a Claude e cosa no. Molto più di quanto pensi." },
              { icon: Sparkles, t: "Chiarezza brutale", d: "Capisci una volta per tutte come impostare un progetto serio con Claude Code, senza saper programmare." },
            ].map((c, i) => {
              const Icon = c.icon;
              return (
                <Reveal key={i} delay={i * 0.1}>
                  <div className="card-paper h-full">
                    <div className="w-11 h-11 rounded-xl bg-[#fb4604] text-white flex items-center justify-center mb-5">
                      <Icon className="h-5 w-5" />
                    </div>
                    <h3 className="text-xl font-semibold mb-2">{c.t}</h3>
                    <p className="text-[#3a3a3a] leading-relaxed">{c.d}</p>
                  </div>
                </Reveal>
              );
            })}
          </div>
        </div>
      </section>

      {/* ===================== TESTIMONIAL (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-12 text-center">
              <span className="text-silver-black">Cosa dicono</span> <span className="text-orange-pure">chi ha già fatto la call</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-5">
            {[
              { t: "In 45 minuti mi ha fatto capire più di 3 corsi pagati. Zero cazzate, solo workflow che funzionano.", n: "Luca R.", r: "Product designer" },
              { t: "Mi aspettavo il solito webinar-trappola. Invece carte scoperte dal primo minuto, 40 minuti di formazione vera e poi 5 minuti sul loro corso. Pulito.", n: "Marta S.", r: "Freelance marketer" },
              { t: "Onestamente, è folle che sia gratis. Ho risparmiato settimane di lavoro grazie a come mi ha impostato Claude Code.", n: "Andrea V.", r: "Dev full-stack" },
            ].map((t, i) => (
              <Reveal key={i} delay={i * 0.08}>
                <div className="card-paper h-full flex flex-col">
                  <div className="text-orange-pure text-3xl leading-none mb-3">&ldquo;</div>
                  <p className="text-[#2a2a2a] leading-relaxed flex-1">{t.t}</p>
                  <div className="mt-5 pt-4 border-t border-[#131313]/10">
                    <div className="font-semibold">{t.n}</div>
                    <div className="text-sm text-[#8a8a8a]">{t.r}</div>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== GARANZIA (ink) ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <Reveal><span className="bubble-silver mb-6">La mia promessa</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[44px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-orange">Se dopo 10 minuti non ti sto dando valore, chiudi la call.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/70 text-lg leading-relaxed">
              Senza giustificazioni. Senza &ldquo;dammi altri 5 minuti&rdquo;.
              <br />
              Statisticamente su 247 call nessuno ha chiuso in anticipo.
              <br />
              <span className="text-white font-semibold">Ma il diritto di farlo lo hai, sempre.</span>
            </p>
          </Reveal>
        </div>
      </section>

      {/* ===================== FAQ (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-3xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[48px] font-bold leading-tight mb-10">
              <span className="text-silver-black">Domande che mi fanno spesso</span>
            </h2>
          </Reveal>
          {[
            { q: "Serve che abbia già Claude installato?", a: "No. Ti guido io dalla prima volta. Se non l'hai mai aperto, durante la call lo configuriamo insieme." },
            { q: "Registri la call?", a: "Solo se vuoi tu. Te la do subito dopo via email così te la riguardi." },
            { q: "Che tool serve?", a: "Google Meet o Zoom (ti mando il link quando prenoti). Basta un browser." },
            { q: "Devo saper programmare?", a: "No, e neanche io lo so davvero. Il punto di Claude Code è che il codice lo scrive lui — tu gli dai gli ordini giusti. In call ti mostro come si costruiscono agenti, skill e system prompt senza toccare una riga." },
            { q: "Si parla solo di Claude Code?", a: "No. Claude Code è lo strumento più potente del mio stack, ma non l'unico. Per usarlo bene servono anche Claude (chat e progetti), skill custom, e altri tool come Perplexity e Manus. In call vediamo l'ecosistema, non un singolo tasto." },
            { q: "Posso portare un mio progetto?", a: "Assolutamente sì, anzi è la cosa migliore. Più specifico è il tuo caso, più utile è la call." },
            { q: "Cosa NON facciamo in 45 minuti?", a: "Non risolviamo progetti enormi. Ci focalizziamo su 1-2 workflow concreti che puoi replicare il giorno dopo." },
          ].map((f, i) => (
            <Reveal key={i} delay={i * 0.06}>
              <div className="border-t border-[#131313]/10 py-6">
                <h3 className="text-xl font-semibold mb-2 text-orange-pure">{f.q}</h3>
                <p className="text-[#3a3a3a] leading-relaxed">{f.a}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </section>

      {/* ===================== COSA USO / STACK (ink) ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Lo stack che vedrai live</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-4 mt-6 max-w-[22ch]">
              <span className="text-silver-white">Niente tool segreti.</span>
              <br />
              <span className="text-silver-orange">Solo quelli che uso davvero.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.15}>
            <p className="text-white/60 text-lg mb-12 max-w-2xl leading-relaxed">
              Ti mostro lo stack esatto che apro ogni mattina. Niente affiliate link, niente &ldquo;segreti&rdquo; a pagamento. Solo roba che funziona, usata nel mio flusso vero.
            </p>
          </Reveal>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              { n: "Claude Code", d: "Il core. Dove costruisco e refactoro progetti reali ogni giorno." },
              { n: "Cursor + VS Code", d: "Quando e perché li alterno. E quando NON mi servono." },
              { n: "Playwright", d: "Per automazioni browser che funzionano al primo colpo." },
              { n: "Next.js 16 + Tailwind", d: "Stack front-end che costruisco live con AI pairing." },
              { n: "Claude Agent SDK", d: "Subagenti, skill, hooks. Il layer che fa la differenza." },
              { n: "Memory & MCP", d: "Come faccio ricordare al modello ciò che conta." },
            ].map((t, i) => (
              <Reveal key={i} delay={0.1 + i * 0.05}>
                <div className="card-dark h-full">
                  <div className="text-lg font-semibold text-orange-pure mb-2">{t.n}</div>
                  <div className="text-sm text-white/70 leading-relaxed">{t.d}</div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== MINI CASE (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-ink mb-6">Un caso concreto</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-tight mb-8 mt-6 max-w-[22ch]">
              <span className="text-silver-black">Marco, founder SaaS.</span>
              <br />
              <span className="text-orange-pure italic font-medium">Da 3 ore a 20 minuti.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-3 gap-5">
            <Reveal delay={0.15}>
              <div className="card-paper h-full">
                <div className="text-xs uppercase tracking-[0.25em] text-[#c9370a] font-bold mb-3">Prima</div>
                <p className="text-[#2a2a2a] leading-relaxed">Scriveva prompt a mano, copiava-incollava tra 4 tool, ogni feature nuova gli prendeva mezza giornata.</p>
              </div>
            </Reveal>
            <Reveal delay={0.25}>
              <div className="card-paper h-full">
                <div className="text-xs uppercase tracking-[0.25em] text-[#c9370a] font-bold mb-3">In call</div>
                <p className="text-[#2a2a2a] leading-relaxed">45 minuti. Abbiamo impostato un workflow con Claude Code + 2 custom skill per il suo codebase.</p>
              </div>
            </Reveal>
            <Reveal delay={0.35}>
              <div className="card-paper h-full">
                <div className="text-xs uppercase tracking-[0.25em] text-[#c9370a] font-bold mb-3">Dopo</div>
                <p className="text-[#2a2a2a] leading-relaxed">Stessa feature, <strong className="text-orange-pure">20 minuti</strong>. La mattina dopo mi ha scritto: <em>&ldquo;Ho recuperato una settimana di lavoro.&rdquo;</em></p>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== COSA OTTIENI (ink-2) ===================== */}
      <section className="bg-ink-2 section section-border-t">
        <div className="max-w-5xl mx-auto px-6">
          <Reveal>
            <h2 className="text-[36px] md:text-[52px] font-bold leading-tight mb-3 text-center">
              <span className="text-silver-white">Esci dalla call con</span>
              <br />
              <span className="text-silver-orange">sei cose molto concrete.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.08}>
            <p className="text-white/60 text-center mb-12 max-w-2xl mx-auto leading-relaxed">
              Non sei qui per &ldquo;ispirarti&rdquo;. Sei qui per portarti a casa cose che puoi usare domani mattina.
            </p>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-5">
            {[
              { t: "Un workflow funzionante", d: "Applicato al tuo caso reale, testato live durante la call. Non teoria, output." },
              { t: "Una mappa mentale chiara", d: "Quando Claude. Quando ChatGPT. Quando Cursor. Smetti di indovinare." },
              { t: "2-3 prompt pattern riutilizzabili", d: "Strutture che funzionano sempre, non magic strings. Le capisci, non le memorizzi." },
              { t: "La registrazione completa", d: "Te la mando via email subito dopo. Te la riguardi quando ti serve." },
              { t: "Un ordine di priorità", d: "Cosa imparare PRIMA, cosa ignorare per ora. La cosa più importante di tutte." },
              { t: "Accesso diretto per domande", d: "Se nei 7 giorni dopo hai un dubbio sul workflow, mi scrivi. Rispondo io." },
            ].map((x, i) => (
              <Reveal key={i} delay={0.1 + i * 0.05}>
                <div className="card-dark h-full">
                  <div className="flex items-start gap-4">
                    <div className="step-num shrink-0" style={{ width: "2.5rem", height: "2.5rem", fontSize: "1rem" }}>{i + 1}</div>
                    <div>
                      <h3 className="text-lg font-semibold mb-1.5 text-white">{x.t}</h3>
                      <p className="text-white/65 text-sm leading-relaxed">{x.d}</p>
                    </div>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== CONFRONTO DETTAGLIATO (paper) ===================== */}
      <section className="bg-paper section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-orange mb-6">Confronto onesto</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[46px] font-bold leading-tight mb-10 mt-6 max-w-[22ch]">
              <span className="text-silver-black">Corso da 800€ vs</span>
              <br />
              <span className="text-orange-pure italic font-medium">questa call gratis.</span>
            </h2>
          </Reveal>
          <div className="card-paper">
            <div className="grid grid-cols-3 gap-4 pb-4 border-b border-[#131313]/10 text-sm font-semibold uppercase tracking-[0.15em]">
              <div className="text-[#8a8a8a]">Cosa</div>
              <div className="text-[#8a8a8a]">Corso tipico</div>
              <div className="text-orange-pure">Questa call</div>
            </div>
            {[
              ["Personalizzato sul tuo caso", "No, generico", "Sì, tutto su di te"],
              ["Screen share live", "No, solo video", "Sì, vedi come lavoro"],
              ["Domande dirette a me", "Forum / community", "Sì, in diretta"],
              ["Durata utile", "20h+ da seguire", "45 min densi"],
              ["Setup personalizzato", "No", "Sì, configurato insieme"],
              ["Prezzo", "€400 – €2.000", "€0"],
            ].map(([k, v1, v2], i) => (
              <Reveal key={i} delay={0.08 + i * 0.04}>
                <div className="grid grid-cols-3 gap-4 py-4 border-b border-[#131313]/06 text-[15px]">
                  <div className="font-medium text-[#1c1c1c]">{k}</div>
                  <div className="text-[#8a8a8a]">{v1}</div>
                  <div className="text-[#1c1c1c] font-semibold">{v2}</div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* ===================== CHI SONO (ink) ===================== */}
      <section className="bg-ink section section-border-t">
        <div className="max-w-4xl mx-auto px-6">
          <Reveal><span className="bubble-silver mb-6">Chi ti fa la call</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[34px] md:text-[48px] font-bold leading-tight mb-8 mt-6 max-w-[22ch]">
              <span className="text-silver-white">Max, founder di Digital Empire.</span>{" "}
              <span className="text-silver-orange">Builder, non formatore.</span>
            </h2>
          </Reveal>
          <div className="grid md:grid-cols-2 gap-6">
            <Reveal delay={0.15}>
              <div className="space-y-4 text-white/75 leading-relaxed">
                <p>Ho passato gli ultimi 3 anni a costruire con l'AI <strong className="text-silver-orange">ogni singolo giorno</strong>: landing page, agenti, automazioni, skill custom, sistemi interi. Oggi tutto questo vive sotto <strong className="text-silver-orange">Digital Empire</strong>, la mia agenzia.</p>
                <p>In call c'è <strong className="text-silver-orange">solo me</strong> — nessun sales, nessun junior, nessuno script. Questa call nasce perché ogni settimana ci chiedono la stessa cosa: <em>&ldquo;come fate a muovervi così veloce con l'AI?&rdquo;</em></p>
                <p>La risposta te la do 1:1. Gratis. Una volta. Se poi ha senso lavorare insieme, ne parliamo negli ultimi 4-5 minuti. Se no, esci lo stesso con un workflow che funziona. Amici come prima.</p>
              </div>
            </Reveal>
            <Reveal delay={0.25}>
              <div className="grid grid-cols-2 gap-4">
                {[
                  { n: "3+", l: "Anni full-AI" },
                  { n: "50+", l: "Progetti spediti" },
                  { n: "247", l: "Call già fatte" },
                  { n: "0", l: "Corsi venduti" },
                ].map((s, i) => (
                  <div key={i} className="card-dark text-center">
                    <div className="text-3xl font-bold text-silver-orange">{s.n}</div>
                    <div className="text-xs uppercase tracking-[0.2em] text-white/50 mt-2">{s.l}</div>
                  </div>
                ))}
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* ===================== UNA SOLA OBIEZIONE (ink-2) ===================== */}
      <section className="bg-ink-2 section section-border-t">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <Reveal><span className="bubble-orange mb-6">L'unica obiezione vera</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[44px] font-bold leading-tight mb-8 mt-6">
              <span className="text-silver-white">&ldquo;Se è gratis,</span>{" "}
              <span className="text-silver-orange">dov'è la fregatura?&rdquo;</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-white/70 text-lg leading-relaxed mb-6">
              Fregatura zero. Ti spiego l'economia vera di Digital Empire: <strong className="text-white">il 5% delle persone con cui parliamo</strong> poi sceglie Claude Code Mastery o un progetto a pagamento. Il 95% esce con il workflow e buona giornata.
            </p>
            <p className="text-white/70 text-lg leading-relaxed">
              A noi basta quel 5%. A te basta quest'unica call per <span className="hl-block">capire se ha senso fare il passo successivo con noi</span> — o per uscire con qualcosa di utile. Comunque vinci tu.
            </p>
          </Reveal>
        </div>
      </section>

      {/* ===================== BOOKING FINAL (paper) ===================== */}
      <section className="bg-paper section section-border-t text-center">
        <div className="max-w-3xl mx-auto px-6">
          <Reveal><span className="bubble-ink mb-8">Ultimo check</span></Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[44px] md:text-[72px] font-bold leading-[1.02] mb-6 mt-8 tracking-tight">
              <span className="text-silver-black">45 minuti.</span>
              <br />
              <span className="text-orange-pure italic font-medium">Gratis. Per davvero.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#2a2a2a] text-lg md:text-xl mb-10 max-w-xl mx-auto">
              Clicca, scegli uno slot, ci vediamo in call. È tutto.
            </p>
          </Reveal>
          <Reveal delay={0.3}><CTA large /></Reveal>
        </div>
      </section>

      {/* ===================== FOOTER ===================== */}
      <footer className="bg-ink-2 py-10 border-t border-white/10 relative z-[3]">
        <div className="max-w-5xl mx-auto px-6 flex flex-col md:flex-row gap-4 justify-between items-center text-sm text-white/50">
          <div>© 2026 · Claude Code Mastery · by Digital Empire</div>
          <div>Call Strategica 1:1 · 45 min · Gratis</div>
        </div>
      </footer>
    </main>
  );
}
