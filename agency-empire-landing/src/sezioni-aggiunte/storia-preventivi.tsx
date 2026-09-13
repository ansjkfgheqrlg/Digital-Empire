import { FATTI } from "@/lib/fatti";

/* F4 BLOCCO D (dossier 40, D1+D2) — «la storia dei preventivi». Montata PRIMA di <PrimaDopo />, superficie ink.
   Copy integrale in brief/COPY-F4-gamma.md (autocontrollo gate voce/fatti alla fine del file). Nome del cliente MAI
   scritto: «un'azienda che importa auto dalla Germania». Numeri solo da FATTI.novacar (65 preventivi, 11 marche,
   2 minuti a PDF, 3-13 luglio 2026) — il resto in parole («ore», «pochi minuti», «decine», «pochi secondi»).
   0 KB di JS: solo markup + CSS (frecce SVG ferme, hairline arancio, marker 5px, stile funnel-hero). CSS: f4-storia.css
   (.sp-*), importato dopo scala.css. Riempita dallo scagnozzo γ. */

const SCHEMA: { titolo: string; riga: string }[] = [
  { titolo: "Annuncio sul portale", riga: "il portale tedesco, ogni mattina" },
  { titolo: "Incolli il link", riga: "un click, non un modulo" },
  { titolo: "L'app legge tutto e calcola", riga: "dati e prezzo, in automatico" },
  { titolo: "PDF col loro logo, in secondi", riga: "pronto da mandare" },
];

const CHAT: { chi: "cliente" | "noi"; nome: string; ora: string; testo: string }[] = [
  { chi: "cliente", nome: "Titolare", ora: "19:04", testo: "Anche oggi decine di preventivi. E sono ancora qui." },
  { chi: "noi", nome: "Digital Empire", ora: "19:05", testo: "Mandami il link di un annuncio." },
  { chi: "noi", nome: "Digital Empire", ora: "19:06", testo: "Fatto. Ecco il PDF col vostro logo, prezzo già calcolato. Pochi secondi." },
  { chi: "cliente", nome: "Titolare", ora: "19:07", testo: "…lo puoi fare per tutti?" },
];

/* Frecce ferme fra i 4 blocchi dello schema — hairline arancio + punta 5 px, disegnate in CSS puro (::after per ogni
   blocco tranne l'ultimo, ancorata al bordo destro del blocco: `left:100%` la piazza esattamente nello spazio (gap)
   fra un blocco e il successivo, senza calcoli di viewBox — coerente con lo stile ferma di funnel-hero, 39B §5). */

export function StoriaPreventivi() {
  return (
    <div className="vivo">
      <section id="storia-preventivi" className="sv sv-ink sp-sezione" aria-labelledby="storia-preventivi-h2">
        <div className="sv-container sp-container">
          <p className="sp-apertura">
            Ok, sto andando troppo veloce. <span className="sp-apertura-it">Adesso ti faccio un esempio concreto…</span>
          </p>

          <div className="sp-storia">
            <p className="sv-eyebrow">Un cliente nostro, un caso vero</p>
            <h2 id="storia-preventivi-h2" className="sv-h2 mt-3 max-w-[24ch]">
              Un'azienda che importa auto <span className="sv-it" style={{ color: "var(--sv-orange)" }}>dalla Germania.</span>
            </h2>
            <p className="sv-body sv-muted sp-p">
              Ogni mattina apriva il portale tedesco e ripartiva da zero. Apriva un annuncio. Copiava i dati.
              Calcolava il prezzo a mano. Impaginava il PDF. Poi il prossimo annuncio. E il prossimo.
            </p>
            <p className="sv-body sv-muted sp-p">
              Decine di preventivi al giorno. Ore della sua giornata, ogni giorno — bruciate su un lavoro che una
              macchina fa meglio di lui.
            </p>
            <p className="sv-body sp-p">
              Allora abbiamo costruito una piccola applicazione privata, solo per loro: incolli il link
              dell'annuncio, esce il PDF — il loro logo, le caratteristiche che ci hanno chiesto, il prezzo già
              calcolato. In pochi secondi.
            </p>
            <p className="sp-prova sv-mono">
              In dieci giorni: <b>{FATTI.novacar.preventivi}</b> preventivi su <b>{FATTI.novacar.marche}</b> marche —
              circa {FATTI.novacar.minutiPerPdf} minuti a PDF, controlli compresi
            </p>
          </div>

          <ol className="sp-schema" role="list" aria-label="Dall'annuncio al PDF, in quattro passaggi">
            {SCHEMA.map((s) => (
              <li key={s.titolo} className="sp-blocco">
                <b className="sp-blocco-t">{s.titolo}</b>
                <span className="sp-blocco-r">{s.riga}</span>
              </li>
            ))}
          </ol>

          <div className="sp-chat" aria-label="Conversazione ricostruita, nomi generici">
            {CHAT.map((m, i) => (
              <div key={i} className={`sp-bolla sp-bolla--${m.chi}`}>
                <span className="sp-bolla-meta">
                  {m.nome} <span className="sp-bolla-ora">{m.ora}</span>
                </span>
                <p className="sp-bolla-testo">{m.testo}</p>
              </div>
            ))}
          </div>

          <div className="sp-primadopo">
            <div className="sp-pd-col">
              <span className="sp-pd-eyebrow">Prima</span>
              <b className="sp-pd-num">Ore</b>
              <span className="sp-pd-r">ogni giorno</span>
            </div>
            <div className="sp-pd-frx" aria-hidden="true" />
            <div className="sp-pd-col sp-pd-col--dopo">
              <span className="sp-pd-eyebrow">Dopo</span>
              <b className="sp-pd-num sp-pd-num--accento">Pochi minuti</b>
              <span className="sp-pd-r">tutti i giorni</span>
            </div>
          </div>

          <p className="sp-chiusura sv-it">
            Lo stesso lavoro. Fatto da una macchina che è loro. Adesso ti mostro quanto costa — e quanto costerebbe
            affittarlo.
          </p>
        </div>
      </section>
    </div>
  );
}
