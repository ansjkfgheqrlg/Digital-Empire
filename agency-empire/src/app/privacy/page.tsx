import { LEGAL } from "@/lib/legal";

export const metadata = { title: "Privacy · Digital Empire" };

/* Informativa breve e vera: nessun cookie di profilazione, analytics senza cookie, il form e' Calendly. */
export default function PrivacyPage() {
  return (
    <main id="main" className="sv sv-ink-piatto min-h-screen">
      <div className="container-tight py-16 md:py-24">
        <p className="sv-eyebrow">Privacy</p>
        <h1 className="sv-h2 mt-3">Cosa raccogliamo su questo sito, e cosa no.</h1>
        <div className="sv-body sv-muted mt-8 grid gap-5" style={{ maxWidth: "70ch", lineHeight: 1.7 }}>
          <p><b className="text-white">Titolare.</b> {LEGAL.ragioneSociale}{LEGAL.partitaIva ? `, P.IVA ${LEGAL.partitaIva}` : ""}{LEGAL.indirizzo ? `, ${LEGAL.indirizzo}` : ""}. Contatto: <a className="underline" href={`mailto:${LEGAL.email}`}>{LEGAL.email}</a>.</p>
          <p><b className="text-white">Navigazione.</b> Usiamo Vercel Web Analytics: conta le visite e i clic sui bottoni senza cookie e senza identificare la persona (nessun ID persistente, IP non conservato). Non ci sono cookie di profilazione né pixel pubblicitari.</p>
          <p><b className="text-white">Prenotazione.</b> La pagina /prenota incorpora Calendly: nome, email e orario che inserisci vanno a Calendly (con la sua informativa) e a noi, solo per fissare e tenere la chiamata. Non li cediamo a terzi e non li usiamo per newsletter senza il tuo consenso.</p>
          <p><b className="text-white">I tuoi diritti.</b> Accesso, rettifica, cancellazione, opposizione (artt. 15-22 GDPR): scrivi a {LEGAL.email}, rispondiamo entro 30 giorni.</p>
          <p><b className="text-white">Aggiornamenti.</b> Questa pagina cambia quando cambia il sito. Ultimo aggiornamento: settembre 2026.</p>
        </div>
        <p className="mt-10"><a className="sv-btn-ghost" href="/">← Torna al sito</a></p>
      </div>
    </main>
  );
}
