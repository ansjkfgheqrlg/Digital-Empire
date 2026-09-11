export const metadata = { title: "Cookie · Digital Empire" };

/* La lezione di armageddon.bsns.it (dnt=1): scegliere strumenti senza cookie toglie il banner. */
export default function CookiePage() {
  return (
    <main id="main" className="sv sv-ink-piatto min-h-screen">
      <div className="container-tight py-16 md:py-24">
        <p className="sv-eyebrow">Cookie</p>
        <h1 className="sv-h2 mt-3">Questo sito non usa cookie di profilazione.</h1>
        <div className="sv-body sv-muted mt-8 grid gap-5" style={{ maxWidth: "70ch", lineHeight: 1.7 }}>
          <p>Niente cookie pubblicitari, niente tracciamento fra siti, niente banner da chiudere. Le statistiche (Vercel Web Analytics) funzionano senza cookie e senza identificare la persona.</p>
          <p>L&apos;unico servizio esterno che può impostare cookie tecnici è Calendly, sulla pagina /prenota, per far funzionare la prenotazione. Si legge nella sua informativa.</p>
          <p>Ultimo aggiornamento: settembre 2026.</p>
        </div>
        <p className="mt-10"><a className="sv-btn-ghost" href="/">← Torna al sito</a></p>
      </div>
    </main>
  );
}
