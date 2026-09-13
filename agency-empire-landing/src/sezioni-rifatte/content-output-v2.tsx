/* RIFACIMENTO 21 (BRIEF F3, blocco A — 39B §2 r.21) — ContentOutput «Cosa produce la tua fabbrica di contenuti».
   TESTO: copiato parola per parola da src/components/sections/content-output.tsx (giugno), stesso ordine:
   bubble → h2 (con la coda in corsivo serif) → 6 celle, ognuna «[ DELIVERABLE 0N ]» + titolo + descrizione.
   FORMA: griglia 3×2 piatta su carta, bordo hairline (E06: tabella, non card), eyebrow mono in accento, titolo 18,
   corpo 15. Niente colori pieni, niente ombre. Nessuna CTA (il testo di giugno non ne ha). 0 KB di JS.
   La griglia è una superficie composta: grana locale in ::after. CSS: src/app/rifatte-a.css (.ra-co*, .ra-cella*). */

const DELIVERABLE = [
  {
    n: "01",
    title: "Caroselli Instagram",
    description:
      "L'AI genera il copy CRO per ogni slide, poi il motore di automazione costruisce le grafiche visive complete. Pronto da pubblicare.",
  },
  {
    n: "02",
    title: "Script Video AI",
    description:
      "Script parola per parola per Reels, TikTok e YouTube: hook di 3 secondi, corpo strutturato e CTA che genera engagement.",
  },
  {
    n: "03",
    title: "Caption + Hashtag",
    description:
      "Descrizione del post ottimizzata con emoji, CTA DM e set di hashtag calibrati tra volume alto e nicchia per massimizzare il reach.",
  },
  {
    n: "04",
    title: "Upload Google Drive",
    description:
      "I contenuti finiti vengono caricati automaticamente su Google Drive, organizzati per argomento e pronti da scaricare o condividere.",
  },
  {
    n: "05",
    title: "Pubblicazione Programmata",
    description:
      "Puoi collegare il workflow a strumenti di scheduling per pubblicare automaticamente sui tuoi canali social senza toccare nulla.",
  },
  {
    n: "06",
    title: "Batch Produzione Multipla",
    description:
      "Il sistema può girare in batch e generare 5, 10 o 20 caroselli in una sola sessione. Settimane di contenuti in pochi minuti.",
  },
] as const;

export function ContentOutputV2() {
  return (
    <div className="vivo">
      <section id="content-output" className="sv sv-carta sv-section ra-co" aria-labelledby="content-output-v2-h2">
        <div className="sv-container ra-col">
          <header className="ra-testa ra-testa--sx">
            <p className="sv-eyebrow">Output del Sistema</p>
            <h2 id="content-output-v2-h2" className="sv-h2 ra-h2">
              Cosa produce la tua <span className="sv-it">fabbrica di contenuti.</span>
            </h2>
          </header>

          <ol className="ra-griglia" aria-label="I sei deliverable">
            {DELIVERABLE.map((d) => (
              <li key={d.n} className="ra-cella">
                <span className="ra-cella-eyebrow">[ DELIVERABLE {d.n} ]</span>
                <h3 className="ra-cella-h3">{d.title}</h3>
                <p className="ra-cella-p">{d.description}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>
    </div>
  );
}
