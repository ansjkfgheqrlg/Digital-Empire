import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A09 (Dossier 38 v2, Atto III) — «Guardalo girare». Inserita dopo <OutreachInside />.
   Parte 1: il video del sistema che gira. Finché VIDEO è null (gesto di Max: un file in public/ o un URL)
   rende SOLO la parte 2. Parte 2: la cucitura in colonna — colazione.webp INTERA (736×1309, resa 300 px, §14)
   a sinistra, a destra la riga grande col numero misurato (FATTI.messaggiGiorno) e la nota «misurato, non promesso».
   Nessuna CTA di vendita: siamo sopra metà pagina (§15). 0 KB di JS. CSS: src/app/aggiunte-b.css (.gg-*). */

/** Sorgente del video (mp4/webm in public/ o URL diretto). Gesto di Max: finché è null, la parte video non si rende. */
const VIDEO = null as string | null;

const COLAZIONE = { src: "/aura/colazione.webp", width: 736, height: 1309 } as const;

export function GuardaloGirare() {
  return (
    <div className="vivo">
      <section id="guardalo-girare" className="sv sv-ink sv-section gg" aria-labelledby="guardalo-girare-h2">
        <div className="sv-container">
          {VIDEO ? (
            <div className="gg-video">
              <video src={VIDEO} controls playsInline preload="metadata" aria-label="Il sistema di outreach mentre gira: la dashboard con invii, risposte e lead di oggi">
                Il tuo browser non riproduce questo video.
              </video>
            </div>
          ) : null}

          <div className="gg-cuc">
            <figure className="foto-intera gg-foto" style={{ aspectRatio: `${COLAZIONE.width}/${COLAZIONE.height}` }}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={COLAZIONE.src}
                width={COLAZIONE.width}
                height={COLAZIONE.height}
                alt="Una persona fa colazione con calma, tazza in mano, mentre il sistema lavora da solo"
                loading="lazy"
                decoding="async"
              />
            </figure>
            <div>
              <p className="sv-eyebrow">Guardalo girare</p>
              <h2 id="guardalo-girare-h2" className="gg-riga mt-3">
                Ha già mandato <b>{FATTI.messaggiGiorno}</b> messaggi.{" "}
                <span className="sv-it">Tu stai facendo colazione.</span>
              </h2>
              <p className="sv-body sv-muted mt-5 max-w-[42ch]">Il numero è misurato sulla dashboard, non promesso.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
