import Link from "next/link";
import { prenotaDa } from "@/lib/contatti";

/* RIFATTA 15 — SystemsShowcase «Ogni sistema, nel dettaglio» (BRIEF F3, blocco B; 39B §2 r.15).
   Sostituisce <SystemsShowcase /> in page.tsx (lo scambio lo fa Emperator). Il TESTO è copiato parola per parola
   da src/components/sections/systems-showcase.tsx, nello stesso ordine di lettura; cambia solo la forma:
   3 colonne monocrome (ink, bordo hairline), eyebrow in accento, cifra 34 px, liste a 15, UNA sola CTA-bottone
   (il terzo «Prenota ora»; i primi due restano link testuali), le 4 stat finali in una riga mono piccola.
   Niente gradienti, niente rosso/oro/blu, niente icone, 0 KB di JS. CSS: src/app/rifatte-b.css (.rb-ss*). */

const BOTTONE_IN = 2; // indice della colonna il cui «Prenota ora» è il bottone (le altre = link testuale)

const systems = [
  {
    id: "outreach",
    label: "Outreach Factory",
    tagline: "Il tuo sales team che lavora 24/7",
    metric: "312",
    metricUnit: "msg / giorno",
    metricSub: "Gmail + Instagram DM in parallelo",
    uptime: "99.7%",
    uptimeLabel: "uptime",
    steps: [
      { t: "Scraping", d: "Profili target estratti con filtri AI sul tuo ICP ideale" },
      { t: "Personalization", d: "GPT-4o scrive ogni messaggio con variabili dinamiche e brand voice" },
      { t: "Send & Track", d: "Notifica lead caldi → Slack in tempo reale + follow-up 3× automatico" },
    ],
    features: [
      "Gmail automation: 300+ email personalizzate/giorno con APSOC",
      "Instagram DM safe: proxy residenziali dedicati, comportamento umano",
      "Qualificazione semantica AI: lead caldi isolati automaticamente",
      "Follow-up sequenziale fino a 3 touchpoint per ogni prospect",
      "Dashboard web live: monitoraggio lead, status, conversazioni",
    ],
    stack: ["Python", "Selenium", "GPT-4o", "Slack API", "Gmail API", "Proxy Resi."],
    timeline: "Go-live in 7 giorni",
    roi: "Da 0 a 300+ contatti / giorno",
  },
  {
    id: "content",
    label: "Content Factory",
    tagline: "Pubblica ogni giorno senza toccare niente",
    metric: "24",
    metricUnit: "contenuti / giorno",
    metricSub: "caroselli · reels · caption + hashtag",
    uptime: "100%",
    uptimeLabel: "upload rate",
    steps: [
      { t: "Brief Input", d: "Un argomento o prompt → sistema si attiva in automatico" },
      { t: "Generazione AI", d: "Copy CRO + grafiche costruite via browser automation in parallelo" },
      { t: "Upload Drive", d: "File organizzati per categoria, data e formato — pronti all'uso" },
    ],
    features: [
      "Caroselli Instagram APSOC-optimized: copy CRO su ogni slide",
      "Script Reels: hook, corpo, CTA in formato 30-60 secondi",
      "Caption + hashtag strategici per massimizzare reach organico",
      "Costruzione automatica grafiche via browser automation",
      "Upload organizzato su Google Drive per argomento e data",
    ],
    stack: ["GPT-4o", "Browser Auto.", "Drive API", "Canva API", "FFmpeg"],
    timeline: "Go-live in 7 giorni",
    roi: "Settimane di contenuti in minuti",
  },
  {
    id: "brain",
    label: "Second Brain",
    tagline: "La tua azienda sa tutto. Sempre.",
    metric: "1.4k",
    metricUnit: "query / giorno",
    metricSub: "risposta media in 0.3 secondi",
    uptime: "99.8%",
    uptimeLabel: "uptime",
    steps: [
      { t: "Indicizzazione", d: "Notion, Drive, Obsidian vettorizzati in real-time nel knowledge graph" },
      { t: "Query AI", d: "Domanda in linguaggio naturale → risposta precisa con source citation" },
      { t: "Sync live", d: "Ogni documento nuovo aggiornato automaticamente nella base di conoscenza" },
    ],
    features: [
      "Wiki aziendale strutturata: prodotti, processi, clienti, decisioni",
      "AI risponde in tempo reale a qualsiasi domanda operativa",
      "Aggiornamento continuo: ogni info archiviata e resa ricercabile",
      "Connessione a Notion, Google Drive, Obsidian o sistema custom",
      "Accesso team: ogni membro trova ciò che cerca in secondi",
    ],
    stack: ["RAG Pipeline", "OpenAI Embed.", "Notion API", "Drive API", "Pinecone"],
    timeline: "Go-live in 10 giorni",
    roi: "Zero dispersione di conoscenza aziendale",
  },
];

const bottomStats = [
  { n: "312+", l: "messaggi / giorno per cliente" },
  { n: "7", l: "giorni al primo go-live" },
  { n: "0 €", l: "canoni mensili SaaS" },
  { n: "100%", l: "codice proprietario tuo" },
];

export function SystemsShowcaseV2() {
  return (
    <div className="vivo">
      <section id="servizi" className="sv sv-ink sv-section rb-ss" aria-labelledby="servizi-h2">
        <div className="sv-container">
          <header className="rb-ss-testa">
            <span className="sv-eyebrow"><b>Tre sistemi. Zero compromessi.</b></span>
            <h2 id="servizi-h2" className="sv-h2 mt-3">
              Ogni sistema, <span className="sv-it rb-accento">nel dettaglio.</span>
            </h2>
            <p className="sv-lead sv-muted rb-ss-lead">
              Implementazioni AI verticali — ognuna automatizza un&apos;area precisa del tuo business.
              Girano sui <strong>tuoi server</strong>, con il
              <strong> codice sorgente incluso</strong>. Nessun canone, nessuna dipendenza.
            </p>
          </header>

          <div className="rb-ss-colonne">
            {systems.map((s, si) => (
              <article key={s.id} className="rb-ss-col rb-grana grad-max">
                <div className="rb-ss-blocco rb-ss-intesta">
                  <span className="sv-mono rb-accento">{s.label}</span>
                  <span className="sv-mono rb-ss-live">live</span>
                  <p className="sv-it rb-ss-tagline">{s.tagline}</p>
                </div>

                <div className="rb-ss-blocco rb-ss-metrica">
                  <div>
                    <div className="rb-ss-cifra">{s.metric}</div>
                    <div className="sv-mono rb-accento">{s.metricUnit}</div>
                    <div className="rb-ss-sub sv-muted">{s.metricSub}</div>
                    <div className="sv-mono rb-ss-nota">Capacità del sistema · esempio di configurazione</div>
                  </div>
                  <div className="rb-ss-uptime">
                    <b>{s.uptime}</b>
                    <span className="sv-mono">{s.uptimeLabel}</span>
                  </div>
                </div>

                <div className="rb-ss-blocco">
                  <div className="sv-mono rb-accento rb-ss-titolo">Come funziona</div>
                  <ol className="rb-ss-passi">
                    {s.steps.map((step, i) => (
                      <li key={i}>
                        <b>{step.t}</b>
                        <span>{step.d}</span>
                      </li>
                    ))}
                  </ol>
                </div>

                <div className="rb-ss-blocco">
                  <div className="sv-mono rb-accento rb-ss-titolo">Cosa è incluso</div>
                  <ul className="rb-ss-lista">
                    {s.features.map((f, i) => (
                      <li key={i}>{f}</li>
                    ))}
                  </ul>
                </div>

                <div className="rb-ss-blocco">
                  <div className="sv-mono rb-accento rb-ss-titolo">Stack tecnico</div>
                  <ul className="rb-ss-stack">
                    {s.stack.map((t) => (
                      <li key={t} className="sv-mono">{t}</li>
                    ))}
                  </ul>
                </div>

                <div className="rb-ss-blocco">
                  <div className="sv-mono rb-accento rb-ss-titolo">Il risultato per te</div>
                  <p className="sv-it rb-ss-roi">{s.roi}</p>
                </div>

                <div className="rb-ss-blocco rb-ss-piede">
                  <span className="sv-mono">⚡ {s.timeline}</span>
                  {si === BOTTONE_IN ? (
                    <Link href={prenotaDa("F15")} className="sv-btn rb-btn" data-cta>
                      Prenota ora
                    </Link>
                  ) : (
                    <Link href={prenotaDa("F15")} className="rb-link">
                      Prenota ora
                    </Link>
                  )}
                </div>
              </article>
            ))}
          </div>

          <p className="sv-mono rb-ss-stat">
            {bottomStats.map((stat) => (
              <span key={stat.n}>
                <b>{stat.n}</b> {stat.l}
              </span>
            ))}
          </p>
        </div>
      </section>
    </div>
  );
}
