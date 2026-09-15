/* F6 A2/A3 (dossier 41, ordini di Max 15/09): headline NUOVA + sottotitolo NUOVO dell'hero.
   Componente aggiunto, montato in hero.tsx con 2 righe AGGIUNTE (import + <HeroTitolo />) subito prima
   del <h1> di giugno — 0 righe di hero.tsx toccate (ADR-030, deroga dichiarata: il titolo/paragrafo di
   giugno si nascondono da CSS in f6-hero.css, non da qui).
   A3 — le "ombre strane": qui NIENTE background-clip:text, NIENTE text-shadow. Colore pieno
   (argento #d9d4e1 / bianco #fff), niente gradiente sul testo: la grana del velo (.hero-tex-velo) sta
   comunque sotto perché questo blocco vive dentro lo stesso contenitore z-index:3 di f5-hero.css (B1). */
export function HeroTitolo() {
  return (
    <div className="f6-titolo">
      <h1 className="f6-h1">
        <span className="f6-h1-riga">Siamo l&apos;<b>agenzia</b></span>
        <span className="f6-h1-riga">che elimina il <b>lavoro ripetitivo</b></span>
        <span className="f6-h1-riga">dal tuo business. <b>Per sempre.</b></span>
      </h1>
      <p className="f6-sub">
        Hai <b>processi meccanici</b> che ti mangiano ore ogni settimana e che potrebbero{" "}
        <b>girare da soli</b>{" "}— ma ogni tool che hai provato era più complicato del problema stesso. Noi
        costruiamo l&apos;<b>automazione su misura</b> e te la consegniamo in un&apos;<b>app privata</b> dove
        basta <b>un click</b> per far partire tutto. <b>Zero configurazione. Zero manuali.</b> Il tuo
        processo gira in automatico, tu torni a fare quello che conta. È una soluzione{" "}
        <b>concreta e semplice</b>, senza complicazioni inutili, a un <b>problema reale</b>.
      </p>
    </div>
  );
}
