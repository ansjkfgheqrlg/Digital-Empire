import { Aura } from "@/components/vivo/aura";
import { CallCTA } from "@/components/call-cta";
import { FATTI } from "@/lib/fatti";

/* N10 — Il processo: sette giorni, quattro fasi. Copy: COPY.md §N10.
   Sfondo ink, .due-col (lista + foto Aura con la riga), stack sotto, CTA verso /prenota/. */
const FASI = [
  {
    titolo: "Briefing.",
    testo:
      "Un'ora. Chi contatti, cosa pubblichi, dove finiscono i lead. Se sai già cosa automatizzare, si parte da qui. Se non lo sai, si parte dalla chiamata.",
  },
  {
    titolo: "Logica.",
    testo:
      "Quali trigger fanno cosa, come si comporta il sistema in ogni caso, con quali dati decide. Niente scatola nera: ogni scelta è scritta e la puoi leggere.",
  },
  {
    titolo: "Costruzione e test.",
    testo: "Il sistema gira sul tuo server con i tuoi account. Lo vedi mandare i primi messaggi veri prima del go-live.",
  },
  {
    titolo: `Go-live, poi ${FATTI.giorniMonitoraggio} giorni di guardia.`,
    testo: `Dashboard, alert automatici, correzioni incluse. Poi ${FATTI.giorniSupporto} giorni di supporto e una sessione di formazione al tuo team.`,
  },
];

export function Processo() {
  return (
    <section id="processo" className="sv sv-ink sv-section" aria-labelledby="processo-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">Sette giorni, quattro fasi</p>
        <h2 id="processo-h2" className="sv-h2 mt-3">
          Dal contratto al go-live <span className="sv-it" style={{ color: "var(--sv-silver)" }}>senza mesi di sviluppo.</span>
        </h2>

        <div className="due-col mt-10">
          <ol className="grid gap-6" style={{ listStyle: "none", padding: 0, margin: 0 }}>
            {FASI.map((f, i) => (
              <li key={f.titolo}>
                <span className="sv-mono" style={{ color: "var(--sv-orange)" }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <p className="sv-body sv-muted mt-1">
                  <b>{f.titolo}</b> {f.testo}
                </p>
              </li>
            ))}
          </ol>
          <Aura
            file="n10-processo.webp"
            alt="uomo con bicchiere di whisky, giacca, luce calda"
            riga={`«Il giorno dopo il go-live: ${FATTI.giorniMonitoraggio} giorni di monitoraggio nostri. Le serate tue.»`}
          />
        </div>

        <p className="sv-small sv-muted mt-10 max-w-[70ch]">
          Sotto il cofano: Claude, Playwright, Python, proxy residenziali, Slack o il CRM tuo. Niente SaaS in mezzo che
          può chiuderti il rubinetto.
        </p>

        <div className="mt-8">
          <CallCTA da="N10" label="Partiamo dal briefing →" />
        </div>
      </div>
    </section>
  );
}
