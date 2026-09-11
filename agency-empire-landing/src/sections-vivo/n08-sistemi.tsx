import { Aura, auraPresente } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";

/* N8 — Le tre fabbriche (8 sezioni v1 → 1). Cucitura fotografica (armageddon T2) se la foto c'è, ink piatto
   se manca (composizione B). Tre sistemi distinti con etichetta mono + numero romano, non con tre colori (Asse B).
   Dettagli tecnici nei <details>. Copy: COPY.md §N8. */
const BASE = process.env.NEXT_PUBLIC_AURA_BASE ?? "/aura/";

function Dettagli({ children }: { children: string }) {
  return (
    <details className="sv-dett">
      <summary>Cosa c&apos;è dentro</summary>
      <p>{children}</p>
    </details>
  );
}

export function Sistemi() {
  const cucitura = auraPresente("n8-outreach.webp");
  return (
    <section
      id="sistemi"
      className={cucitura ? "cuc" : "sv sv-ink"}
      style={cucitura ? ({ ["--foto" as string]: `url(${BASE}n8-outreach.webp)` } as React.CSSProperties) : undefined}
      aria-labelledby="sistemi-h2"
    >
      {/* I · OUTREACH FACTORY */}
      <div className={cucitura ? "cuc-a" : ""}>
        <div className="sv-container pt-20 pb-10 md:pt-24 md:pb-14">
          <p className="sv-eyebrow">Facciamo tre cose. Per scelta.</p>
          <p className="sv-etichetta mt-6"><b>I</b> · Outreach Factory</p>
          <h2 id="sistemi-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Alle 7:40 ha già mandato <span style={{ color: "var(--sv-orange)" }}>{FATTI.messaggiGiorno} messaggi.</span>
          </h2>
          <p className="sv-lead sv-muted mt-5 max-w-[52ch]">
            Sessioni browser reali, proxy residenziali, velocità di digitazione umana. Trova i contatti giusti, scrive un messaggio
            diverso per ognuno, fa i follow-up, e ti mette su Slack o nel tuo CRM solo chi ha risposto. Tu leggi le risposte. Non
            scrivi le domande.
          </p>
          <Dettagli>
            Dentro: email + DM Instagram (WhatsApp per i concessionari) · qualificazione AI del lead · follow-up automatici · dashboard
            web · lead con profilo e contesto nel CRM · proxy residenziali inclusi
          </Dettagli>
        </div>
      </div>

      <div className={cucitura ? "cuc-b" : ""}>
        <div className={`sv-container relative ${cucitura ? "min-h-[380px] pt-16 pb-20" : "pb-4"}`}>
          {cucitura && <p className="riga riga--libera">Tu stai facendo colazione.</p>}
          <Aura
            file="n8-dashboard.webp"
            alt="dashboard dell'Outreach Factory: invii di oggi, risposte in coda, lead in CRM"
            riga="outreach · oggi · invii / risposte in coda"
            className="mt-8 md:absolute md:right-6 md:bottom-[-18px] md:w-[min(440px,46%)] aspect-[16/10]"
          />
        </div>
      </div>

      {/* II · CONTENT FACTORY — foto a destra; III · SECOND BRAIN — solo testo */}
      <div className="sv sv-ink-piatto">
        <div className="sv-container py-16 md:py-20">
          <div className="due-col">
            <div>
              <p className="sv-etichetta"><b>II</b> · Content Factory</p>
              <h3 className="sv-h2 mt-3 max-w-[16ch]">
                Un argomento entra. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Carosello, reel, caption escono.</span>
              </h3>
              <p className="sv-lead sv-muted mt-5 max-w-[52ch]">
                Scrivi un argomento. Il sistema scrive il copy di ogni slide col metodo APSOC, monta le grafiche in un browser vero,
                scrive lo script del reel e la caption con gli hashtag, e carica tutto su Drive diviso per data. Pubblichi ogni giorno
                anche nelle settimane in cui non pubblicheresti.
              </p>
              <Dettagli>
                Dentro: caroselli con copy CRO su ogni slide · script reel · caption + hashtag · grafiche via browser · Drive ordinato per
                data · un brief → contenuti pronti
              </Dettagli>
            </div>
            <Aura file="n8-content.webp" alt="Uomo con occhiali al lavoro, braccia conserte, luce fredda" riga="Senza toccare niente." objectPosition="50% 15%" />
          </div>

          <div className="mt-16 md:mt-20 max-w-[60ch]">
            <p className="sv-etichetta"><b>III</b> · Second Brain</p>
            <h3 className="sv-h2 mt-3 max-w-[16ch]">
              La tua azienda <span className="sv-it" style={{ color: "var(--sv-silver)" }}>sa tutto. Sempre.</span>
            </h3>
            <p className="sv-lead sv-muted mt-5">
              Documenti, processi, clienti, decisioni: indicizzati. Ogni domanda sulla tua operatività ha una risposta in tempo reale, e
              ogni sistema AI che usi riceve il contesto giusto invece di ripartire da zero.
            </p>
            <Dettagli>
              Dentro: wiki indicizzata · risposte con la fonte · contesto per ogni sessione AI · niente informazione dispersa in cinque
              cartelle
            </Dettagli>
          </div>

          <div className="mt-12">
            <CallCTA da="N8" label="Vediamo la tua, in chiamata →" />
          </div>
        </div>
      </div>
    </section>
  );
}
