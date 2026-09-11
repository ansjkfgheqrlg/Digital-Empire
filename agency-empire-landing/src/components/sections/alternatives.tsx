"use client";

import { Reveal } from "@/components/reveal";
import { Scale } from "lucide-react";

/** Tabella comparativa contro le ALTERNATIVE D'ACQUISTO, non contro concorrenti nominati:
 *  e' la decisione che il cliente sta davvero prendendo. Una riga concede un punto
 *  a un'alternativa — senza quella, la tabella e' pubblicita' e si legge come tale. */
const cols = ["Fare a mano", "SaaS a canone", "Freelance o agenzia", "Digital Empire"] as const;

const rows: { label: string; cells: string[]; winner: number }[] = [
  {
    label: "Costo dopo 24 mesi",
    cells: ["Ore del tuo team, ogni mese", "Canone che non finisce mai", "Nuovo preventivo a ogni modifica", "Pagamento unico + API a consumo"],
    winner: 3,
  },
  {
    label: "Chi possiede il sistema",
    cells: ["Nessuno: vive nelle teste", "Il fornitore", "Chi l'ha scritto", "Tu. Codice sorgente in chiaro"],
    winner: 3,
  },
  {
    label: "Se smetti di pagare",
    cells: ["—", "Si spegne tutto", "Si ferma l'assistenza", "Continua a girare"],
    winner: 3,
  },
  {
    label: "Calibrato sul tuo caso",
    cells: ["Sì, ma non scala", "No: addestrato su tutti", "Dipende da chi ti capita", "Sul tuo ICP e sul tuo copy"],
    winner: 3,
  },
  {
    label: "Operativo in",
    cells: ["Mai del tutto", "Stesso giorno", "Settimane di brief", "7 giorni"],
    winner: 1,
  },
  {
    label: "Quando conviene davvero",
    cells: [
      "Volumi bassi e processo che cambia ogni settimana",
      "Ti serve una cosa standard entro domani",
      "Progetto una tantum, senza continuità",
      "Il processo è ripetitivo e lo fai ogni giorno",
    ],
    winner: -1,
  },
];

export function Alternatives() {
  return (
    <section className="bg-grey section section-border-t">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-12">
          <Reveal>
            <span className="bubble-orange mb-6">
              <Scale className="h-3.5 w-3.5" /> Le alternative, per intero
            </span>
          </Reveal>
          <Reveal delay={0.1}>
            <h2 className="text-[32px] md:text-[48px] font-bold leading-tight mt-6">
              <span className="text-silver-black">Non stai scegliendo noi contro un&apos;altra agenzia. </span>
              <span className="text-orange-pure italic font-medium">Stai scegliendo tra quattro strade.</span>
            </h2>
          </Reveal>
          <Reveal delay={0.2}>
            <p className="text-[#1c1c1c]/72 text-lg max-w-3xl mx-auto mt-6 leading-relaxed">
              Le mettiamo tutte in tabella, compresa la riga in cui{" "}
              <strong className="text-silver-black">non siamo noi la risposta giusta</strong>.
            </p>
          </Reveal>
        </div>

        <Reveal delay={0.25}>
          <div className="overflow-x-auto -mx-6 px-6">
            <table className="w-full min-w-[760px] border-collapse text-left">
              <thead>
                <tr>
                  <th className="w-[168px]" />
                  {cols.map((c, i) => (
                    <th
                      key={c}
                      className="px-4 py-4 text-[11px] uppercase tracking-[0.18em] font-black align-bottom"
                      style={{
                        color: i === 3 ? "#fb4604" : "rgba(28,28,28,0.55)",
                        borderBottom: i === 3 ? "2px solid #fb4604" : "1px solid rgba(28,28,28,0.16)",
                      }}
                    >
                      {c}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={r.label}>
                    <th
                      scope="row"
                      className="px-1 py-4 text-[12px] uppercase tracking-[0.14em] font-black text-[#1c1c1c]/60 align-top"
                      style={{ borderBottom: "1px solid rgba(28,28,28,0.10)" }}
                    >
                      {r.label}
                    </th>
                    {r.cells.map((cell, i) => (
                      <td
                        key={i}
                        className="px-4 py-4 text-[14px] leading-relaxed align-top"
                        style={{
                          borderBottom: "1px solid rgba(28,28,28,0.10)",
                          background:
                            i === 3 ? "rgba(251,70,4,0.055)" : r.winner === i ? "rgba(28,28,28,0.035)" : "transparent",
                          color: i === 3 || r.winner === i ? "#1c1c1c" : "rgba(42,42,42,0.72)",
                          fontWeight: i === 3 || r.winner === i ? 600 : 400,
                        }}
                      >
                        {cell}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Reveal>

        <Reveal delay={0.4}>
          <p className="text-center mt-10 text-[14px] leading-relaxed text-[#1c1c1c]/72 max-w-2xl mx-auto">
            Guarda la penultima riga:{" "}
            <strong className="text-silver-black">sul tempo di avvio un SaaS ci batte</strong>, e non
            fingiamo il contrario. Ci batte finché ti serve una cosa standard. Il giorno in cui ti
            serve la <span className="text-orange-pure font-semibold">tua</span>, quel vantaggio
            scade e il canone no.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
