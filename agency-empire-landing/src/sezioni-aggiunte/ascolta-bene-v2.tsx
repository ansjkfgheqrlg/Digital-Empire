"use client";

import { Reveal } from "@/components/reveal";

/* F6 (ordine di Max 15/09, dossier 41 blocco E2) — «ASCOLTA BENE» v2. `ListenUp` (giugno,
   src/components/sections/listen-up.tsx) NON si tocca: 0 righe cambiate, si nasconde da CSS
   (f6-copy.css, selettore :has(+ .f6-marker-ascolta) — la classe sotto è il marker). Questo componente
   monta SUBITO dopo <ListenUp /> in page.tsx (deroga dichiarata, come A2/l'hero: legge del copy generico,
   niente «Outreach», niente «lavora mentre dormono» — non è sempre vero). Stessa forma di giugno: titolo
   maiuscolo, 5 paragrafi, una citazione grande. Copy in brief/COPY-F6-gamma.md §E2. Stili in f6-copy.css
   (prefisso .ab2-), scopati dentro #ascolta-bene-v2. */
export function AscoltaBeneV2() {
  return (
    <div className="vivo f6-marker-ascolta">
      <section id="ascolta-bene-v2" className="ab2-sezione" aria-labelledby="ascolta-bene-v2-h2">
        <div className="ab2-container">
          <Reveal>
            <h2 id="ascolta-bene-v2-h2" className="ab2-titolo">ASCOLTA BENE.</h2>
          </Reveal>

          <div className="ab2-corpo">
            <Reveal delay={0.1}>
              <p>
                Che tu sia un coach, un social media manager, un imprenditore o una piccola agenzia — il
                problema è lo stesso ovunque: <b>troppi processi meccanici</b>, poco tempo per quello che
                conta davvero.
              </p>
            </Reveal>

            <Reveal delay={0.2}>
              <p>
                Ogni mattina la stessa routine: messaggi da scrivere, contenuti da preparare, informazioni
                da cercare a mano. Ti svegli già in ritardo sul lavoro che conta.
              </p>
            </Reveal>

            <Reveal delay={0.3}>
              <p>
                E ogni volta che guardi un competitor crescere più veloce di te, sai già la risposta:
                <span className="ab2-citazione">
                  &ldquo;Loro hanno smesso di fare a mano quello che una macchina fa{" "}
                  <span className="ab2-citazione-it">uguale.</span>&rdquo;
                </span>
              </p>
            </Reveal>

            <Reveal delay={0.4}>
              <p className="ab2-riga-forte">
                Non è fortuna. <span className="ab2-hl">È un sistema. E noi lo costruiamo per te.</span>
              </p>
            </Reveal>

            <Reveal delay={0.5}>
              <p>
                Online trovi mille SaaS a canone mensile, tool generici che non conoscono il tuo business,
                agenzie che ti vendono consulenza infinita. <b>Tutto rumore. Nessuna soluzione reale.</b>
              </p>
            </Reveal>

            <Reveal delay={0.6}>
              <p>
                Quello che ti serve non è un altro abbonamento da pagare. È un&apos;infrastruttura AI
                proprietaria — installata sui tuoi server, calibrata sul tuo business e{" "}
                <b>tua per sempre</b>. Con <b>zero canoni mensili</b> dopo il setup.
              </p>
            </Reveal>
          </div>
        </div>
      </section>
    </div>
  );
}
