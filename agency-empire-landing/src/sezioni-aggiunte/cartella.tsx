"use client";

import { useId, useState, type KeyboardEvent } from "react";
import { FATTI } from "@/lib/fatti";

/* AGGIUNTA A08 (Dossier 38 v2, Atto III) — La cartella delle consegne: quattro linguette, un foglio.
   Inserita dopo <SystemsShowcase />. h ≤ 700. Superficie ink.
   Le linguette sono <button> in clip-path (Codice · Dashboard · Documentazione · Formazione); la linguetta attiva cambia il
   foglio carta sotto. È l'unica eccezione JS del blocco A, dichiarata nel brief: "use client" + useState, niente altro.
   Pattern tabs accessibile (role=tablist/tab/tabpanel, frecce ← → fra le linguette). Il foglio è una superficie composta:
   porta la sua grana locale in ::after (D6). I giorni di supporto vengono da FATTI (§6/§8). Nessuna CTA di vendita (§15).
   Titolo: non è nel brief, è in voce di casa e si può cambiare. CSS: aggiunte-a.css (.ca-*). */
const LINGUETTE: { k: string; nome: string; frase: string; voci: string[] }[] = [
  {
    k: "codice",
    nome: "Codice",
    frase: "repository tuo, documentato, in chiaro",
    voci: [
      "repository privato a tuo nome",
      "README in italiano: avvio, stop, aggiornamento",
      "nessuna dipendenza da un nostro account",
      "licenza: tua, per sempre",
    ],
  },
  {
    k: "dashboard",
    nome: "Dashboard",
    frase: "invii, risposte, lead — aperta 24/7",
    voci: ["accesso tuo dal primo giorno", "ogni invio con esito", "ogni risposta in coda", "esportazione quando vuoi"],
  },
  {
    k: "documentazione",
    nome: "Documentazione",
    frase: "come gira, come si spegne, come si estende",
    voci: ["schema del flusso", "procedure di stop e riavvio", "dove mettere le mani", "cosa non toccare"],
  },
  {
    k: "formazione",
    nome: "Formazione",
    frase: "una sessione al tuo team, registrata",
    voci: ["registrata e tua", "domande aperte", `${FATTI.giorniSupporto} giorni di supporto dopo`, "niente corso da comprare"],
  },
];

export function Cartella() {
  const [attiva, setAttiva] = useState(0);
  const uid = useId();
  const l = LINGUETTE[attiva];

  function tasti(e: KeyboardEvent<HTMLButtonElement>, i: number) {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft" && e.key !== "Home" && e.key !== "End") return;
    e.preventDefault();
    const n = LINGUETTE.length;
    const prossima =
      e.key === "ArrowRight" ? (i + 1) % n : e.key === "ArrowLeft" ? (i - 1 + n) % n : e.key === "Home" ? 0 : n - 1;
    setAttiva(prossima);
    const el = document.getElementById(`${uid}-tab-${LINGUETTE[prossima].k}`);
    el?.focus();
  }

  return (
    <div className="vivo">
      <section id="cartella" className="sv sv-ink sv-section" aria-labelledby="cartella-h2">
        <div className="sv-container">
          <p className="sv-eyebrow">Cosa ti consegniamo</p>
          <h2 id="cartella-h2" className="sv-h2 ca-h2 mt-3 max-w-[20ch]">
            Una cartella. <span className="sv-it">Tutta tua.</span>
          </h2>

          <div className="ca-cartella">
            <div className="ca-tabs" role="tablist" aria-label="Le quattro consegne">
              {LINGUETTE.map((t, i) => (
                <button
                  key={t.k}
                  type="button"
                  role="tab"
                  id={`${uid}-tab-${t.k}`}
                  className="ca-tab"
                  aria-selected={i === attiva}
                  aria-controls={`${uid}-pannello`}
                  tabIndex={i === attiva ? 0 : -1}
                  onClick={() => setAttiva(i)}
                  onKeyDown={(e) => tasti(e, i)}
                >
                  {t.nome}
                </button>
              ))}
            </div>

            <div
              className="ca-foglio"
              role="tabpanel"
              id={`${uid}-pannello`}
              aria-labelledby={`${uid}-tab-${l.k}`}
              tabIndex={0}
            >
              <div className="ca-pannello" key={l.k}>
                <p className="sv-eyebrow ca-eyebrow">{l.nome}</p>
                <p className="ca-frase">{l.frase}</p>
                <ul className="ca-lista">
                  {l.voci.map((v) => (
                    <li key={v}>{v}</li>
                  ))}
                </ul>
                <p className="sv-mono ca-piede">
                  {attiva + 1} / {LINGUETTE.length} · è tutto nel contratto, scritto
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
