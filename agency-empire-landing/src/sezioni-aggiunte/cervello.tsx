/* F4 BLOCCO F3 (dossier 40) — il cervello di Max a cavallo di <BrainDeep /> + <SecondBrainInside />. Riempito dallo scagnozzo δ.
   Layer assoluto (mai ingrandito: 1200x628 nativo), allineato a destra, sotto i testi (z-index:0), le due
   sezioni figlie diventano trasparenti SOLO dentro questo wrapper (fondo ink spostato qui). CSS in f4-brain.css (.cv-*). */
export function Cervello({ children }: { children: React.ReactNode }) {
  return (
    <div className="cv-wrap">
      {children}
      <div className="cv-cervello" aria-hidden="true">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src="/texture/cervello-ORIGINALE.jpg" width={1200} height={628} alt="" loading="lazy" />
      </div>
    </div>
  );
}
