import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N12 — Per chi / non per chi: qualificazione negativa secca (Pascu la usa solo sui prodotti
   avanzati: per un'agenzia e' posizionamento). Copy: COPY-V2 §N12. */
const SI = [
  "Hai un'offerta che vende e l'operatività non tiene il passo",
  "Fai outreach a mano ogni giorno e vuoi smettere senza smettere di farlo",
  "Pubblichi quando riesci e vuoi pubblicare ogni giorno",
  "Vuoi crescere senza assumere altre persone per fare cose ripetitive",
  "Lavori da solo? Vale lo stesso: i 30 DM al giorno li mandi tu. Al posto del team, il collo di bottiglia sei tu.",
];
const NO = [
  "Stai ancora cercando cosa vendere (trova prima il prodotto: il sistema amplifica, non inventa)",
  "Vuoi qualcuno che faccia le cose al posto tuo ogni giorno senza voler capire come funzionano",
  "Non sei disposto a mostrarci come lavori oggi (senza il contesto il sistema è cieco)",
  "Cerchi la soluzione istantanea: sette giorni sono sette giorni",
];

export function PerChi() {
  return (
    <section id="per-chi" className="sv sv-carta" aria-labelledby="perchi-h2">
      <div className="container-default py-16 md:py-20">
        <div className="grid md:grid-cols-[1fr_280px] gap-10 items-end">
          <h2 id="perchi-h2" className="sv-h2 max-w-[18ch]">
            Lavoriamo solo con chi{" "}
            <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>ha già qualcosa che funziona.</span>
          </h2>
          <Aura
            file="n12-per-chi.webp"
            alt="Uomo in camicia e bretelle, mani giunte, in ufficio"
            riga="Se vuoi delegare senza capire, non siamo noi. Sul serio."
            tratt="carta"
            className="aspect-square rounded-[4px]"
          />
        </div>

        <div className="mt-10 grid md:grid-cols-2 gap-10">
          <div>
            <div className="sv-mono" style={{ color: "var(--sv-orange)" }}>È per te se</div>
            <ul className="mt-4 grid gap-3 list-none p-0 m-0">
              {SI.map((t) => <li key={t} className="sv-check sv-body" style={{ color: "#1c1c1c" }}>{t}</li>)}
            </ul>
          </div>
          <div>
            <div className="sv-mono" style={{ color: "#6f6a62" }}>Non è per te se</div>
            <ul className="mt-4 grid gap-3 list-none p-0 m-0">
              {NO.map((t) => <li key={t} className="sv-x sv-body sv-muted">{t}</li>)}
            </ul>
          </div>
        </div>

        <a href="/prenota" className="btn-gold mt-10" data-cta="per-chi">
          Se sei nella prima colonna, prenota <ArrowRight className="h-4 w-4" />
        </a>
      </div>
    </section>
  );
}
