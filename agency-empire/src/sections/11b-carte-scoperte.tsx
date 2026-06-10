"use client";

import { Sparkles } from "lucide-react";
import { Reveal } from "@/components/reveal";

export function CarteScoperte() {
  return (
    <section className="bg-ink section" aria-labelledby="carte-h2">
      <div className="container-tight">
        <Reveal>
          <span className="bubble-gold mb-6">
            <Sparkles className="h-3.5 w-3.5" />
            Giochiamo a carte scoperte
          </span>
        </Reveal>

        <Reveal delay={0.10} className="mt-6 mb-10">
          <h2 id="carte-h2">
            <span className="text-silver-white block">&ldquo;Ok, ma cosa include</span>
            <span className="text-silver-gold font-accent italic block">
              davvero il workflow?&rdquo;
            </span>
          </h2>
        </Reveal>

        <Reveal delay={0.15}>
          <div className="space-y-6 text-[1.05rem] md:text-[1.125rem] text-white/90 leading-[1.85]">
            <p>
              Risposta diretta:{" "}
              <strong className="text-white/90">tutto quello che serve per farlo girare da solo</strong>.
              E quello che non è incluso, te lo diciamo chiaramente prima di firmare.
            </p>
            <p>
              <strong className="text-white/90">Cosa includiamo:</strong> setup completo del workflow,
              integrazione con i tuoi strumenti esistenti (CRM, email, social,
              database), test su dati reali, go-live, formazione (1 ora),
              e 30 giorni di supporto post-consegna. Non hai bisogno di altro
              per farlo partire.
            </p>
            <p>
              <strong className="text-white/90">Cosa non includiamo:</strong> le piattaforme stesse
              (Instantly, Apollo, Make, ecc. A tuo carico, sono subscription mensili)
              e il traffico pubblicitario se il workflow ne richiede.
              Stiamo parlando di costi operativi standard,{" "}
              <em className="italic text-white/85">non di sorprese nascoste</em>.
            </p>
            <p>
              <strong className="text-white/90">Il pricing è chiaro:</strong> si parte da 5.000€ per
              workflow single-channel. I workflow multi-canale o con integrazioni
              custom arrivano fino a 15.000€. La demo è gratuita. In 30 minuti
              ti dico esattamente a quale range appartiene il tuo caso specifico.
            </p>
            <p>
              Alla fine della demo, se quello che ti mostro non ha senso per
              il tuo business,{" "}
              <strong className="text-white/90">non firmi niente</strong>. Zero
              impegno, zero pressione.{" "}
              <span className="hl-block">
                Il nostro obiettivo è darti valore reale dal primo contatto. Se non succede, non meritiamo il tuo tempo.
              </span>
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
