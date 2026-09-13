import Link from "next/link";
import { LEGAL, LEGAL_RIGHE } from "@/lib/legal";

/* AGGIUNTA A22 (Dossier 38 v2, Atto VI) — «La coda legale»: una riga mono prima del footer + Privacy e Cookie.
   Inserita subito prima del <footer>. h ≤ 160. 0 KB di JS.
   Legge @/lib/legal (gesto di Max, ADR-026): finché P.IVA, sede e PEC sono tutte vuote la riga sarebbe solo il nome,
   e allora rende `null` — mai «[da inserire]» in pagina. Quando i dati arrivano in legal.ts, la riga si accende da sola. */
export function CodaLegale() {
  const haDati = Boolean(LEGAL.piva || LEGAL.sede || LEGAL.pec);
  if (!haDati || LEGAL_RIGHE.length === 0) return null;
  const righe = LEGAL_RIGHE.map((r) => (r === LEGAL.sede ? `Sede ${r}` : r));
  return (
    <div className="vivo">
      <section className="sv sv-ink-piatto coda-legale" aria-label="Dati societari">
        <div className="sv-container">
          <p className="coda-riga sv-mono m-0">
            <span>
              {righe.map((r, i) => (
                <span key={r}>
                  {i > 0 && <span className="coda-sep"> · </span>}
                  {r}
                </span>
              ))}
            </span>
            <span className="coda-sep" aria-hidden="true">
              ·
            </span>
            <span>
              <Link href="/privacy/">Privacy</Link>
              <span className="coda-sep"> · </span>
              <Link href="/cookie/">Cookie</Link>
            </span>
          </p>
        </div>
      </section>
    </div>
  );
}
