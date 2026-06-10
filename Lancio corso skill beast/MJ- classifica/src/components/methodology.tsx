import { Reveal } from "./reveal";
import { Database, Search, Cpu, ShieldCheck } from "lucide-react";

const steps = [
  {
    title: "Data Ingestion",
    desc: "Il nostro motore aggrega API stream da oltre 50 fonti globali ogni 15 minuti.",
    icon: Database
  },
  {
    title: "Pattern Analysis",
    desc: "Algoritmi IA filtrano bot e manipolazioni per garantire dati reali al 100%.",
    icon: Search
  },
  {
    title: "Global Normalization",
    desc: "Unifichiamo l'impatto di TikTok, radio e vendite fisiche in un unico punteggio live.",
    icon: Cpu
  },
  {
    title: "Empire Verification",
    desc: "Ogni sorpasso in classifica viene validato da un doppio layer di controllo crittografico.",
    icon: ShieldCheck
  }
];

export function Methodology() {
  return (
    <section id="methodology" className="section bg-ink-2 section-border-t">
      <div className="max-w-6xl mx-auto px-6 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
          <Reveal>
            <div className="space-y-6">
              <span className="pre-headline">Inside the Engine</span>
              <h2 className="text-4xl md:text-6xl font-bold">
                <span className="text-silver-white">Come analizziamo</span><br />
                <span className="text-silver-purple">la scena musicale.</span>
              </h2>
              <p className="text-lg text-gray-400 font-medium leading-relaxed">
                Non ci limitiamo a contare i click. Analizziamo l'impatto culturale e la persistenza digitale di ogni artista per definire chi domina davvero l'impero della musica.
              </p>
              <div className="p-8 rounded-3xl bg-white/5 border border-white/10 flex items-center gap-6">
                <div className="w-16 h-16 rounded-2xl bg-purple/20 flex items-center justify-center shrink-0">
                  <Cpu className="w-8 h-8 text-purple" />
                </div>
                <div>
                  <h4 className="text-white font-bold text-lg mb-1">Motore IA "Empire Core"</h4>
                  <p className="text-gray-500 text-sm font-medium">99.9% accuratezza nei dati di streaming globali.</p>
                </div>
              </div>
            </div>
          </Reveal>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {steps.map((step, idx) => (
              <Reveal key={step.title} delay={idx * 0.1}>
                <div className="card-premium p-8 border-t-2 border-t-purple/20 h-full hover:border-t-purple transition-all">
                  <step.icon className="w-8 h-8 text-purple mb-6 relative z-10" />
                  <div className="relative z-10">
                    <h3 className="text-ink font-bold text-xl mb-3">{step.title}</h3>
                    <p className="text-gray-600 text-sm font-medium leading-relaxed">
                      {step.desc}
                    </p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
