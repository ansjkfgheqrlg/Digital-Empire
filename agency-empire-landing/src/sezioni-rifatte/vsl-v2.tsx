import Link from "next/link";
import { ArrowRight, Phone, Shield } from "lucide-react";
import { prenotaDa } from "@/lib/contatti";

/* RIFACIMENTO 02 (BRIEF F3, blocco A — 39B §2 r.02) — VSL «Tre sistemi».
   TESTO: copiato parola per parola da src/components/sections/vsl.tsx (giugno), stesso ordine di lettura:
   bubble → eyebrow → h2 → per ogni card Input / chip / nome / live / cifra / unità / «Capacità del sistema» / riga barra /
   Output / 3 voci → riga di stato («All systems online» + «312 msg · 24 contenuti · 1.4k query») → CTA → riga fiducia.
   FORMA: sfondo ink piatto (niente vsl-bg.png), 3 card argento hairline con la SOLA cifra in accento, un solo bottone
   («Prenota una Chiamata Strategica»); «Prenota una Chiamata Gratuita · 30 min · Gratuita · Zero impegno» resta,
   identico, come link testuale. Le CTA vanno a prenotaDa() (mai al dominio del corso). 0 KB di JS, nessun "use client".
   Grana locale sulle card in ::after. CSS: src/app/rifatte-a.css (.ra-vsl*, .ra-nodo*). */

const NODI = [
  {
    id: "outreach",
    label: "Outreach Factory",
    metric: "312",
    metricSub: "msg / giorno",
    bar: 78,
    barLabel: "78% lead qualificati",
    inputs: ["Gmail", "Instagram DM"],
    outputs: ["Lead → Slack", "Follow-up ×3", "Dashboard live"],
  },
  {
    id: "content",
    label: "Content Factory",
    metric: "24",
    metricSub: "contenuti / giorno",
    bar: 91,
    barLabel: "Upload Drive: completato",
    inputs: ["Brief testuale"],
    outputs: ["Carosello Drive", "Script Reels", "Caption + tag"],
  },
  {
    id: "brain",
    label: "Second Brain",
    metric: "1.4k",
    metricSub: "query / giorno",
    bar: 98,
    barLabel: "Uptime 99.8%",
    inputs: ["Notion", "Google Drive"],
    outputs: ["Query → 0.3s", "Wiki indicizzata", "Sync live"],
  },
] as const;

export function VslV2() {
  return (
    <div className="vivo">
      <section id="vsl" className="sv sv-ink-piatto sv-section ra-vsl" aria-labelledby="vsl-v2-h2">
        <div className="sv-container ra-col">
          <header className="ra-testa">
            <span className="ra-pill">
              <i aria-hidden="true" />
              Sistema live · Tre implementazioni attive
            </span>
            <p className="sv-eyebrow ra-eyebrow">Digital Empire · Come funziona il sistema</p>
            <h2 id="vsl-v2-h2" className="sv-h2 ra-h2">
              Tre <b>sistemi.</b> Un&apos;unica <b>operatività</b>
              <br />
              <span className="ra-h2-grande">che gira da sola.</span>
            </h2>
          </header>

          <ul className="ra-nodi" aria-label="I tre sistemi">
            {NODI.map((n) => (
              <li key={n.id} className="ra-nodo grad-max">
                <div className="ra-nodo-blocco">
                  <span className="ra-k">Input</span>
                  <div className="ra-chips">
                    {n.inputs.map((inp) => (
                      <span key={inp} className="ra-chip">{inp}</span>
                    ))}
                  </div>
                </div>

                <div className="ra-nodo-blocco ra-nodo-centro">
                  <div className="ra-nodo-riga">
                    <span className="ra-nome">{n.label}</span>
                    <span className="ra-live"><i aria-hidden="true" />live</span>
                  </div>
                  <div className="ra-cifra">{n.metric}</div>
                  <div className="ra-unita">{n.metricSub}</div>
                  <div className="ra-k ra-cap">Capacità del sistema</div>
                  <div className="ra-bar" aria-hidden="true"><i style={{ width: `${n.bar}%` }} /></div>
                  <div className="ra-bar-label">{n.barLabel}</div>
                </div>

                <div className="ra-nodo-blocco">
                  <span className="ra-k">Output</span>
                  <ul className="ra-out">
                    {n.outputs.map((out) => (
                      <li key={out}>{out}</li>
                    ))}
                  </ul>
                </div>
              </li>
            ))}
          </ul>

          <div className="ra-stato">
            <span className="ra-live"><i aria-hidden="true" />All systems online</span>
            <span className="ra-stato-num">
              {NODI.map((n) => (
                <span key={n.id}>
                  <b>{n.metric}</b> {n.metricSub.split(" ")[0]}
                </span>
              ))}
            </span>
          </div>

          <div className="ra-cta">
            <Link href={prenotaDa("N02")} data-cta className="sv-btn">
              Prenota una Chiamata Strategica
              <ArrowRight className="h-4 w-4" aria-hidden="true" />
            </Link>
            <Link href={prenotaDa("N02b")} className="ra-link">
              <Phone className="h-4 w-4" strokeWidth={2} aria-hidden="true" />
              <span>
                Prenota una Chiamata Gratuita
                <small>30 min · Gratuita · Zero impegno</small>
              </span>
            </Link>
            <p className="ra-fiducia">
              <Shield className="h-3.5 w-3.5" aria-hidden="true" /> Setup in 7 giorni · Zero canoni · Codice tuo per sempre
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
