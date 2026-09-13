/* RIFACIMENTO 29 (BRIEF F3, blocco A — 39B §2 r.29) — ToolStack «Niente black box».
   TESTO: copiato parola per parola da src/components/sections/tool-stack.tsx (giugno), stesso ordine:
   bubble → h2 (due righe, coda in corsivo serif) → paragrafo (con la coda in grassetto) → 12 voci nome + riga →
   riga finale «→ Tutto lo stack è tuo · Codice sorgente consegnato a setup completato».
   FORMA: lista a 3 colonne senza card (E42: bordi e filetti, non scatole), nome bold 17 + una riga 15, separatori
   hairline, h2 ≤ 42 (var(--fs-h2), max 36). Un solo accento: la coda corsiva dell'h2 e la freccia finale.
   Nessuna CTA (il testo di giugno non ne ha). 0 KB di JS. Niente superfici composte → la grana la porta la sezione.
   CSS: src/app/rifatte-a.css (.ra-ts*, .ra-stack*). */

const TOOL = [
  { name: "Claude AI", desc: "Il cervello del sistema. Qualifica lead in ingresso, genera copy APSOC personalizzato, risponde alla knowledge base in tempo reale." },
  { name: "Gmail API", desc: "Il motore dell'Outreach Factory: 300+ email personalizzate al giorno, warm-up graduale, zero spam, massima deliverability." },
  { name: "Playwright", desc: "Automazione browser per l'outreach Instagram: simula comportamento umano con timing randomizzato. Zero ban, zero rischio account." },
  { name: "Proxy Residenziali", desc: "IP dedicati per blindare ogni account Instagram. Ogni profilo ha il suo proxy residenziale. Il sistema è invisibile alle detection." },
  { name: "APSOC Framework", desc: "Il framework copy proprietario che l'AI usa per scrivere ogni messaggio, caption e script. Calibrato sul tuo ICP e brand voice." },
  { name: "n8n", desc: "Il tessuto connettivo. Orchestra ogni flusso automatico: dalla qualificazione lead alla notifica Slack, dall'upload Drive alla risposta CRM." },
  { name: "OpenAI API", desc: "Generazione contenuti ad alto volume per la Content Factory: caroselli, script Reels, caption. Costi API minimi a consumo." },
  { name: "Supabase", desc: "Database real-time per lead, status conversazioni e metriche. La dashboard web custom legge da qui in tempo reale." },
  { name: "Google Drive", desc: "Storage organizzato per la Content Factory. Ogni output — caroselli, script, grafiche — viene uploadato automaticamente per argomento e data." },
  { name: "Slack / CRM", desc: "Notifiche istantanee quando l'AI identifica un lead caldo. Il tuo team riceve il profilo qualificato direttamente dove lavora." },
  { name: "React / Next.js", desc: "Le dashboard web custom che ti diamo. Interfaccia per monitorare lead, configurare brief contenuti, scaricare output in 30 secondi." },
  { name: "Obsidian / Notion", desc: "Il layer di accesso al Second Brain. L'AI indicizza tutto e risponde a qualsiasi domanda sulla tua knowledge base aziendale." },
] as const;

export function ToolStackV2() {
  return (
    <div className="vivo">
      <section id="tool-stack" className="sv sv-ink sv-section ra-ts" aria-labelledby="tool-stack-v2-h2">
        <div className="sv-container">
          <header className="ra-testa ra-testa--sx">
            <p className="sv-eyebrow">Lo stack tecnico del sistema</p>
            <h2 id="tool-stack-v2-h2" className="sv-h2 ra-h2 ra-ts-h2">
              Niente black box. <br />
              Ogni tool <span className="sv-it ra-accento">spiegato e consegnato.</span>
            </h2>
            <p className="sv-lead sv-muted ra-ts-lead">
              Ti mostriamo lo stack esatto che gira dentro ogni sistema AI che installiamo. Nessun componente nascosto,
              nessun vendor lock-in. Hai il codice sorgente di tutto —{" "}
              <strong className="ra-ts-forte">puoi vedere, modificare e gestire ogni pezzo.</strong>
            </p>
          </header>

          <ul className="ra-stack" aria-label="I dodici tool dello stack">
            {TOOL.map((t) => (
              <li key={t.name} className="ra-stack-voce">
                <h3 className="ra-stack-nome">{t.name}</h3>
                <p className="ra-stack-riga">{t.desc}</p>
              </li>
            ))}
          </ul>

          <p className="ra-ts-coda">
            <span className="ra-accento">→</span> Tutto lo stack è tuo · Codice sorgente consegnato a setup completato
          </p>
        </div>
      </section>
    </div>
  );
}
