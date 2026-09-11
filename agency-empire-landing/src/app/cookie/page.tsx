import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = { title: "Cookie · Digital Empire", alternates: { canonical: "/cookie/" } };

/* La lezione di armageddon.bsns.it (dnt=1): scegliere strumenti senza cookie toglie il banner.
   L'unico terzo che può impostare cookie è Calendly su /prenota/ (C2.1): lo si dice qui. */
export default function CookiePage() {
  return (
    <main id="main" className="sv sv-ink-piatto min-h-screen">
      <div className="sv-container py-16 md:py-24">
        <p className="sv-eyebrow">Cookie</p>
        <h1 className="sv-h2 mt-3 max-w-[20ch]">Questo sito non usa cookie di profilazione.</h1>
        <div className="sv-body sv-muted mt-8 grid gap-5 max-w-[70ch]">
          <p>
            Niente cookie pubblicitari, niente tracciamento fra siti, niente banner da chiudere. Le statistiche (Vercel Web Analytics)
            funzionano senza cookie e senza identificare la persona.
          </p>
          <p>
            L&apos;unico servizio esterno che può impostare cookie tecnici è Calendly, sulla pagina /prenota/, per far funzionare la
            prenotazione: si caricano solo quando apri quella pagina, e si leggono nella sua informativa.
          </p>
          <p>Ultimo aggiornamento: settembre 2026.</p>
        </div>
        <p className="mt-10">
          <Link className="sv-btn-ghost" href="/">← Torna al sito</Link>
        </p>
      </div>
    </main>
  );
}
