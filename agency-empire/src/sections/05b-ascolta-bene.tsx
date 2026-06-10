"use client";

import { Reveal } from "@/components/reveal";

export function AscoltaBene() {
  return (
    <section className="bg-ink section" aria-labelledby="ascolta-h2">
      <div className="container-tight">
        <Reveal>
          <h2 id="ascolta-h2" className="mb-10">
            <span className="text-silver-white">Se riconosci anche solo uno di quei 4 segnali...</span>
          </h2>
        </Reveal>

        <Reveal delay={0.10}>
          <div className="space-y-6 text-[1.10rem] md:text-[1.20rem] text-white/75 leading-[1.85]">
            <p>
              Non è un problema di motivazione. Non è un problema di strategia.
              Non è un problema di prodotto.
            </p>
            <p>
              È un problema di sistema. Stai cercando di scalare un business
              con strumenti progettati per farlo stare fermo. Ogni task manuale
              che ripeti ogni giorno è un{" "}
              <strong className="text-silver-gold font-semibold">
                collo di bottiglia che hai costruito tu stesso
              </strong>
              , senza rendertene conto.
            </p>
            <p>
              La buona notizia è che i sistemi si costruiscono. Non in mesi,
              non con un team interno. Con un workflow AI ben progettato, in{" "}
              <em className="text-white/90 italic">3-4 settimane</em> quella
              parte della tua operatività smette di esistere come problema e
              inizia a girare da sola. H24, senza di te.
            </p>
            <p>
              Noi iniziamo sempre da lì. Dal punto esatto dove l&apos;operatività
              ti blocca. Solo quando abbiamo capito precisamente cosa automatizzare
              e perché,{" "}
              <strong className="text-silver-gold font-semibold">
                iniziamo a costruire il sistema
              </strong>
              . Mai prima.
            </p>
            <p>
              Perché un workflow costruito senza analisi non è un asset.
              È un costo.{" "}
              <span className="hl-block">
                Un workflow costruito sui tuoi processi reali, invece, lavora per te ogni giorno.
              </span>
            </p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
