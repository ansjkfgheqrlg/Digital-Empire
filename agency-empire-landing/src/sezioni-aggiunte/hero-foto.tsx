/* F5 (ordine di Max, 14/09 notte): le tre foto di Max a destra dell'hero, a gruppo, un po' oblique
   ("una sotto, poi una accanto"). Componente NUOVO, montato in hero.tsx con 2 righe aggiunte subito dopo
   <HeroCards /> — nulla di hero.tsx viene rimosso o cambiato (ADR-030, gate §13).
   Tutta la geometria (posizione, rotazione, dimensioni, breakpoint) vive in f5-hero.css (.hf-*): qui solo
   struttura + le 3 <img> reali (dimensioni intrinseche dichiarate, mai ingrandite oltre 1:1).
   Decorativo puro (aria-hidden, alt vuoto, pointer-events:none da CSS): non porta informazione nuova,
   la foto di Max è già raccontata a parole nell'hero. */
export function HeroFoto() {
  return (
    <div className="hf-group" aria-hidden="true">
      <div className="hf-photo hf-photo--1">
        <img
          src="/foto/max-hero-1.jpg"
          width={1101}
          height={616}
          alt=""
          loading="eager"
          decoding="async"
        />
      </div>
      <div className="hf-photo hf-photo--2">
        <img
          src="/foto/max-hero-2.jpg"
          width={1110}
          height={618}
          alt=""
          loading="eager"
          decoding="async"
        />
      </div>
      <div className="hf-photo hf-photo--3">
        <img
          src="/foto/max-hero-3.jpg"
          width={555}
          height={544}
          alt=""
          loading="eager"
          decoding="async"
        />
      </div>
    </div>
  );
}
