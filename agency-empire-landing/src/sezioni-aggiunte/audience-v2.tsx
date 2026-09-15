"use client";

import type { ReactNode } from "react";
import { Reveal } from "@/components/reveal";

/* F6 (ordine di Max 15/09, dossier 41 blocco C1) — «Per chi è» v2. `Audience` (giugno,
   src/components/sections/audience.tsx) NON si tocca: 0 righe cambiate, si nasconde da CSS
   (f6-copy.css, selettore :has(+ .f6-marker-audience)). Questo componente monta SUBITO dopo
   <Audience /> in page.tsx (deroga dichiarata, come A2/hero). Stesso testo di giugno, PAROLA PER
   PAROLA (vedi COPY-F6-gamma.md §C1 — nessuna frase nuova): via i blocchi/card, restano titolo,
   le due etichette mono e le liste come righe di testo con i termini importanti in <b>. Nessun
   fondo, nessun bordo. Stili in f6-copy.css (prefisso .av2-). */

// Testo IDENTICO a src/components/sections/audience.tsx (giugno) — solo <b> aggiunti sui termini importanti.
const SI: ReactNode[] = [
  <>Promuovi prodotti digitali, servizi o consulenza high ticket e vuoi più <b>conversazioni qualificate</b> ogni settimana.</>,
  <>Hai già un prodotto sul mercato e vuoi <b>scalare il volume di contatti</b> senza assumere un team sales.</>,
  <>La prospezione ti prosciuga ore ogni mattina, oppure non lo fai affatto perché è <b>insostenibile a mano</b>.</>,
  <>Vuoi <b>possedere i tuoi strumenti</b> — non affittarli da un SaaS che può alzare i prezzi o sparire.</>,
  <>Ogni lancio ti costa <b>2-3 settimane</b> solo per produrre il copy. Sai che così non può continuare.</>,
];

const NO: ReactNode[] = [
  <>Non hai ancora un prodotto valido sul mercato — l&apos;automazione <b>amplifica solo ciò che già funziona</b>.</>,
  <>Cerchi un&apos;estensione Chrome da <b>€10 al mese</b> da installare e dimenticare nel browser.</>,
  <>Vuoi <b>delegare interamente</b> il marketing senza comprendere o supervisionare i tuoi flussi.</>,
];

export function AudienceV2() {
  return (
    <div className="vivo f6-marker-audience">
      <section id="audience-v2" className="av2-sezione" aria-labelledby="audience-v2-h2">
        <div className="av2-container">
          <Reveal>
            <h2 id="audience-v2-h2" className="av2-titolo">
              Ideato su misura per <span className="av2-titolo-it">Creator, Coach &amp; Business Owner.</span>
            </h2>
          </Reveal>

          <div className="av2-grid">
            <Reveal delay={0.15}>
              <div>
                <span className="av2-etichetta">È per te se:</span>
                <ul className="av2-lista">
                  {SI.map((frase, i) => (
                    <li key={i}>{frase}</li>
                  ))}
                </ul>
              </div>
            </Reveal>

            <Reveal delay={0.25}>
              <div>
                <span className="av2-etichetta av2-etichetta--no">Non è per te se:</span>
                <ul className="av2-lista av2-lista--no">
                  {NO.map((frase, i) => (
                    <li key={i}>{frase}</li>
                  ))}
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>
    </div>
  );
}
