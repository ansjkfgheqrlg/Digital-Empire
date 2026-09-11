import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N10 — Il processo: 4 fasi con numero in filigrana (speedrun T15), lo stack in una riga.
   Qui la numerazione E' informazione: e' una sequenza di giorni. Copy: COPY-V2 §N10. */
const FASI = [
  ["Briefing", "giorno 1", "Un'ora. Chi contatti, cosa pubblichi, dove finiscono i lead. Se sai già cosa automatizzare, si parte da qui. Se non lo sai, si parte dalla chiamata."],
  ["Logica", "giorni 2-3", "Quali trigger fanno cosa, come si comporta il sistema in ogni caso, con quali dati decide. Niente scatola nera: ogni scelta è scritta e la puoi leggere."],
  ["Costruzione e test", "giorni 4-6", "Il sistema gira sui tuoi server con i tuoi account. Lo vedi mandare i primi messaggi veri prima del go-live."],
  ["Go-live e 30 giorni di guardia", "giorno 7 →", "Dashboard, alert automatici, correzioni incluse. Poi 90 giorni di supporto."],
];

export function Processo() {
  return (
    <section id="processo" className="sv sv-ink" aria-labelledby="processo-h2">
      <div className="container-default py-16 md:py-20">
        <p className="sv-eyebrow">Sette giorni, quattro fasi</p>
        <h2 id="processo-h2" className="sv-h2 mt-3 max-w-[18ch]">
          Dal briefing al go-live <span className="sv-it" style={{ color: "var(--sv-silver)" }}>senza mesi di sviluppo.</span>
        </h2>

        <div className="mt-10 grid md:grid-cols-[1fr_280px] gap-10 items-start">
          <ol className="grid sm:grid-cols-2 gap-px list-none p-0 m-0" style={{ background: "var(--sv-hair)" }}>
            {FASI.map(([t, g, d], i) => (
              <li key={t} className="relative p-6 overflow-hidden" style={{ background: "var(--sv-ink)" }}>
                <span
                  className="absolute right-3 top-1 font-black select-none"
                  style={{ fontSize: "var(--fs-word)", lineHeight: 1, color: "rgba(255,255,255,.06)" }}
                  aria-hidden
                >
                  {i + 1}
                </span>
                <div className="sv-mono" style={{ color: "var(--sv-orange)" }}>{g}</div>
                <div className="sv-h3 mt-2">{t}</div>
                <p className="sv-body sv-muted mt-2 max-w-[40ch]">{d}</p>
              </li>
            ))}
          </ol>
          <Aura
            file="n10-processo.webp"
            alt="Uomo con un bicchiere, fine giornata, luce calda"
            riga="Il giorno dopo il go-live: 30 giorni di monitoraggio nostri. Le serate tue."
            className="aspect-[3/4] rounded-[4px]"
          />
        </div>

        <p className="sv-mono mt-8 max-w-[70ch]" style={{ color: "var(--sv-silver-dim)", textTransform: "none", letterSpacing: ".04em", lineHeight: 1.7 }}>
          Sotto il cofano: Claude, Playwright, Python, proxy residenziali, Areus/Slack/CRM tuo. Niente SaaS in mezzo che può chiuderti il rubinetto.
        </p>
        <a href="/prenota" className="btn-gold mt-8" data-cta="processo">
          Partiamo dal briefing <ArrowRight className="h-4 w-4" />
        </a>
      </div>
    </section>
  );
}
