"use client";

import { Reveal } from "@/components/reveal";
import { motion } from "framer-motion";
import { Eye, Brain, Book, Gem } from "lucide-react";

const cards = [
  { rank: "I", title: "I.C.R.O.", icon: Eye, d: "L'anima del Context Engineering. Definisci identità e regole per trasformare Claude in un operatore infallibile." },
  { rank: "S", title: "S.K.I.L.L.", icon: Brain, d: "Il cervello della Entity Logic. Costruisci librerie di competenze verticali che Claude richiama on-demand." },
  { rank: "W", title: "W.O.R.K.", icon: Book, d: "I muscoli del Workflow Power. Connetti le skill in flussi automatici che divorano ore di lavoro manuale." },
  { rank: "D", title: "D.A.N.", icon: Gem, d: "La chiave della Monetizzazione. Trasforma il tuo portfolio tecnico in commesse reali da €500 a progetto." },
];

export function PowerDeck() {
  return (
    <section className="bg-ink section section-border-t overflow-hidden">
      <div className="max-w-6xl mx-auto px-6 grid lg:grid-cols-2 gap-20 items-center">
        <div>
          <Reveal>
            <span className="bubble-orange mb-6">Il cuore del metodo</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-5xl md:text-7xl font-black mb-10 text-white">
              I 4 Pilastri del <br/>
              <span className="text-silver-orange italic">Potere.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-xl text-white/60 mb-12 leading-relaxed">
              Ogni sistema che costruirai poggia su questi 4 asset proprietari. Non sono solo concetti, sono <strong className="text-orange">armi operative</strong>.
            </p>
          </Reveal>
          
          <div className="grid sm:grid-cols-2 gap-6 reveal">
            {cards.slice(0, 2).map((c, i) => (
              <div key={i} className="p-6 border border-white/5 rounded-2xl bg-white/5 group hover:border-orange/30 transition-colors">
                <h4 className="text-orange font-black text-2xl mb-2 italic tracking-tighter">{c.title}</h4>
                <p className="text-[11px] text-white/40 uppercase font-bold tracking-widest">{c.d.split('.')[0]}.</p>
              </div>
            ))}
          </div>
        </div>

        <div className="relative h-[500px] md:h-[600px] flex items-center justify-center group cursor-crosshair px-10">
          {cards.map((c, i) => {
            const Icon = c.icon;
            return (
              <motion.div
                key={i}
                className="card-dark absolute w-full max-w-[340px] shadow-2xl"
                initial={{ rotate: 0, y: 0, x: 0 }}
                whileInView={{ 
                  rotate: (i - 1.5) * 6, 
                  x: (i - 1.5) * 40,
                  y: Math.abs(i - 1.5) * 15
                }}
                whileHover={{ 
                  rotate: 0, 
                  y: -40, 
                  x: (i - 1.5) * 20,
                  zIndex: 50,
                  scale: 1.05,
                  transition: { duration: 0.3 }
                }}
                viewport={{ once: false, margin: "-100px" }}
                style={{ zIndex: i }}
              >
                <div className="absolute top-8 right-10 text-orange font-black text-4xl italic opacity-40">{c.rank}</div>
                <div className="w-14 h-14 rounded-2xl bg-orange flex items-center justify-center mb-8 shadow-lg">
                  <Icon className="h-7 w-7 text-white" />
                </div>
                <h3 className="text-3xl font-black text-white mb-6 italic tracking-tight">{c.title}</h3>
                <p className="text-white/60 leading-relaxed font-medium">
                  {c.d}
                </p>
                <div className="mt-8 pt-6 border-t border-white/10 flex justify-between items-center">
                  <span className="text-[10px] font-black uppercase tracking-[.2em] text-white/30 italic">Empire Pillar</span>
                  <div className="flex gap-1">
                    {Array.from({ length: 3 }).map((_, j) => (
                      <div key={j} className="w-1 h-1 rounded-full bg-orange/40" />
                    ))}
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
