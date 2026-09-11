import type { Metadata } from "next";
import Link from "next/link";
import { LEGAL } from "@/lib/legal";
import { EMAIL } from "@/lib/contatti";

export const metadata: Metadata = { title: "Privacy · Digital Empire", alternates: { canonical: "/privacy/" } };

/* Informativa breve e vera: nessun cookie di profilazione, analytics senza cookie, la prenotazione è Calendly.
   I dati societari arrivano da legal.ts: se mancano, la riga non li nomina (mai "[da inserire]"). */
export default function PrivacyPage() {
  const contatto = LEGAL.email || EMAIL;
  return (
    <main id="main" className="vivo sv sv-ink-piatto min-h-screen">
      <div className="sv-container py-16 md:py-24">
        <p className="sv-eyebrow">Privacy</p>
        <h1 className="sv-h2 mt-3 max-w-[20ch]">Cosa raccogliamo su questo sito, e cosa no.</h1>
        <div className="sv-body sv-muted mt-8 grid gap-5 max-w-[70ch]">
          <p>
            <b className="text-white">Titolare.</b> {LEGAL.ragioneSociale}
            {LEGAL.piva ? `, P.IVA ${LEGAL.piva}` : ""}
            {LEGAL.sede ? `, ${LEGAL.sede}` : ""}.
            {contatto ? <> Contatto: <a className="underline" href={`mailto:${contatto}`}>{contatto}</a>.</> : null}
          </p>
          <p>
            <b className="text-white">Navigazione.</b> Usiamo Vercel Web Analytics: conta le visite e i clic sui bottoni senza cookie e
            senza identificare la persona (nessun ID persistente, IP non conservato). Non ci sono cookie di profilazione né pixel
            pubblicitari.
          </p>
          <p>
            <b className="text-white">Prenotazione.</b> La pagina /prenota/ incorpora Calendly: nome, email e orario che inserisci vanno a
            Calendly (con la sua informativa) e a noi, solo per fissare e tenere la chiamata. Non li cediamo a terzi e non li usiamo per
            newsletter senza il tuo consenso.
          </p>
          <p>
            <b className="text-white">I tuoi diritti.</b> Accesso, rettifica, cancellazione, opposizione (artt. 15-22 GDPR):
            {contatto ? ` scrivi a ${contatto}, rispondiamo entro 30 giorni.` : " scrivici dalla pagina Prenota, rispondiamo entro 30 giorni."}
          </p>
          <p>
            <b className="text-white">Aggiornamenti.</b> Questa pagina cambia quando cambia il sito. Ultimo aggiornamento: settembre 2026.
          </p>
        </div>
        <p className="mt-10">
          <Link className="sv-btn-ghost" href="/">← Torna al sito</Link>
        </p>
      </div>
    </main>
  );
}
