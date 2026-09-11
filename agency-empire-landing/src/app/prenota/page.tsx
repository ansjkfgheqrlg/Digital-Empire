import type { Metadata } from "next";
import Link from "next/link";
import { Calendario } from "./calendario";
import { FATTI } from "@/lib/fatti";
import { EMAIL } from "@/lib/contatti";

/* /prenota/ — la porta d'uscita del sito (Dossier 37 v2, C1.1/C2.1). Pagina NOSTRA, brand agenzia:
   un salto solo dalla home, Calendly inline caricato on demand (perf), `?da=` letto da analytics.tsx.
   Copy: COPY.md §/prenota/. */
export const metadata: Metadata = {
  title: "Prenota la chiamata · Digital Empire",
  description: `${FATTI.minutiChiamata} minuti con chi costruisce il sistema: l'Outreach Factory in live, il prezzo esatto per il tuo caso. Niente slide.`,
  alternates: { canonical: "/prenota/" },
};

const VOCI = ["Con chi costruisce il sistema, non con un venditore", "Il sistema vero davanti a te", "Il prezzo esatto, detto a voce"];

export default function PrenotaPage() {
  return (
    <main id="main" className="sv sv-ink min-h-screen">
      <div className="sv-container py-8">
        <Link href="/" className="sv-small sv-muted hover:text-white transition-colors">← Torna al sito</Link>
      </div>
      <div className="sv-container pb-20 grid lg:grid-cols-[minmax(0,1fr)_minmax(0,1.3fr)] gap-12 items-start">
        <div>
          <p className="sv-eyebrow">{FATTI.minutiChiamata} minuti · il sistema in live</p>
          <h1 className="sv-h1 mt-3">Prenota la chiamata.</h1>
          <p className="sv-lead sv-muted mt-5 max-w-[46ch]">
            Scegli un orario. In chiamata vedi l&apos;Outreach Factory che gira, la dashboard aperta, e ti diciamo il prezzo esatto per il
            tuo caso. Niente slide. Niente «ti richiamiamo».
          </p>
          <ul className="mt-8 space-y-3">
            {VOCI.map((v) => (
              <li key={v} className="sv-check sv-body sv-muted">{v}</li>
            ))}
          </ul>
          <p className="sv-small sv-muted mt-10 max-w-[46ch]">
            La prenotazione passa da Calendly, che usa i suoi cookie: li descriviamo nella pagina <Link href="/cookie/" className="underline">Cookie</Link>.
          </p>
          {EMAIL && (
            <p className="sv-small sv-muted mt-3 max-w-[46ch]">
              Se il calendario non si carica: scrivici a <a href={`mailto:${EMAIL}`} className="underline">{EMAIL}</a> e ti rispondiamo
              noi, non un modulo.
            </p>
          )}
        </div>
        <Calendario />
      </div>
    </main>
  );
}
