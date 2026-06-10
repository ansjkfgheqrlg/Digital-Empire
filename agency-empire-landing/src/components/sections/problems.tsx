"use client";

import { X, Check } from "lucide-react";
import { Reveal } from "@/components/reveal";

export function Problems() {
  return (
    <section className="bg-paper section section-border-t">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-16">
          <Reveal>
            <span className="bubble-orange mb-6">Il vero problema</span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-3xl md:text-5xl font-bold mt-4 text-silver-black">
              Il problema non è &ldquo;non avere tempo&rdquo;.<br />
              <span className="text-orange-pure italic font-medium">È fare a mano ciò che un sistema AI fa da solo.</span>
            </h2>
          </Reveal>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <Reveal delay={0.2}>
            <div className="card-paper h-full">
              <div className="flex items-center gap-3 mb-6">
                <X className="h-5 w-5 text-[#b8b8b8]" />
                <h3 className="text-xl font-bold text-ink">L&apos;operatività manuale</h3>
              </div>
              <ul className="space-y-4 text-ink/70">
                <li>Mandi 30 DM al giorno a mano. Ci vogliono 2-3 ore, ogni mattina. Non scala.</li>
                <li>Crei contenuti social slide per slide, caption dopo caption. Settimane di lavoro che spariscono.</li>
                <li>Le informazioni del tuo business sono disperse tra note, chat, Google Drive e memoria.</li>
                <li>Risultato: <span className="font-bold">Sei tu il collo di bottiglia del tuo stesso business.</span></li>
              </ul>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="card-orange h-full">
              <div className="flex items-center gap-3 mb-6">
                <Check className="h-5 w-5" />
                <h3 className="text-xl font-bold">Con un sistema AI proprietario</h3>
              </div>
              <ul className="space-y-4">
                <li>300+ messaggi personalizzati inviati ogni mattina. In automatico. Mentre dormi.</li>
                <li>Caroselli, script video e caption generati in pochi minuti su richiesta. Settimane di contenuti all&apos;istante.</li>
                <li>Una knowledge base intelligente risponde in tempo reale a qualsiasi domanda sul tuo business.</li>
                <li>Risultato: <span className="font-bold">Tu ti concentri sulla strategia. Il sistema esegue.</span></li>
              </ul>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
