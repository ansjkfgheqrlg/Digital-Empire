import { FATTI } from "@/lib/fatti";

/* F4 BLOCCO D (dossier 40, D1+D2) — «la storia dei preventivi». Montata PRIMA di <PrimaDopo />, superficie ink.
   Nome del cliente MAI scritto: «un'azienda che importa auto dalla Germania». Numeri solo da FATTI.novacar
   (65 preventivi, 11 marche, 2 minuti a PDF, 3-13 luglio 2026) — il resto in parole.

   F6 (ordine di Max 15/09, dossier 41 blocco F1, «più bella») — riscritta: due colonne a desktop (testo 56% a
   sinistra, immagine 44% a destra — public/card/storia-pdf.png, still generato da
   scripts/illustrazione_storia_pdf.py, stile risograph coerente con le card dell'hero, §14 originalità); chat
   con bolle+ombra, iniziali in cerchio, orari mono, «✓✓» argento; schema a 4 blocchi con frecce CURVE (bezier);
   2 frecce di spiegazione su spazi vuoti (mai sopra il testo, 8-10 px fuori dal bordo): dalla chat e dallo
   schema. Grassetti misti nel racconto. Copy delle due note: brief/COPY-F6-gamma.md §F1. Altezza desktop
   ≤ 1.500 px (vincolo del brief). CSS: f4-storia.css (.sp-*), importato dopo scala.css — vinto poi da
   f6-copy.css dove serve. */

const SCHEMA: { titolo: string; riga: string }[] = [
  { titolo: "Annuncio sul portale", riga: "il portale tedesco, ogni mattina" },
  { titolo: "Incolli il link", riga: "un click, non un modulo" },
  { titolo: "L'app legge tutto e calcola", riga: "dati e prezzo, in automatico" },
  { titolo: "PDF col loro logo, in secondi", riga: "pronto da mandare" },
];

const CHAT: { chi: "cliente" | "noi"; nome: string; iniziali: string; ora: string; testo: string; letto?: boolean }[] = [
  { chi: "cliente", nome: "Titolare", iniziali: "T", ora: "19:04", testo: "Anche oggi decine di preventivi. E sono ancora qui." },
  { chi: "noi", nome: "Digital Empire", iniziali: "DE", ora: "19:05", testo: "Mandami il link di un annuncio.", letto: true },
  { chi: "noi", nome: "Digital Empire", iniziali: "DE", ora: "19:06", testo: "Fatto. Ecco il PDF col vostro logo, prezzo già calcolato. Pochi secondi.", letto: true },
  { chi: "cliente", nome: "Titolare", iniziali: "T", ora: "19:07", testo: "…lo puoi fare per tutti?" },
];

/* Freccia curva (bezier) fra due blocchi dello schema — sostituisce la vecchia linea retta in CSS puro. */
function FrecciaSchema({ id }: { id: string }) {
  return (
    <svg className="sp-arrow-seg" viewBox="0 0 100 34" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <defs>
        <marker id={id} viewBox="0 0 10 10" refX="8.4" refY="5" markerWidth="4.4" markerHeight="4.4" orient="auto">
          <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
        </marker>
      </defs>
      <path d="M4,27 C 32,4 68,4 96,17" fill="none" stroke="#fb4604" strokeWidth="1.3" markerEnd={`url(#${id})`} />
    </svg>
  );
}

export function StoriaPreventivi() {
  return (
    <div className="vivo">
      <section id="storia-preventivi" className="sv sv-ink sp-sezione" aria-labelledby="storia-preventivi-h2">
        <div className="sv-container sp-container">
          <p className="sp-apertura">
            Ok, sto andando troppo veloce. <span className="sp-apertura-it">Adesso ti faccio un esempio concreto…</span>
          </p>

          <div className="sp-layout">
            <div className="sp-col-testo">
              <div className="sp-storia">
                <p className="sv-eyebrow">Un cliente nostro, un caso vero</p>
                <h2 id="storia-preventivi-h2" className="sv-h2 mt-3 max-w-[24ch]">
                  Un&apos;azienda che importa auto <span className="sv-it" style={{ color: "var(--sv-orange)" }}>dalla Germania.</span>
                </h2>
                <p className="sv-body sv-muted sp-p">
                  Ogni mattina apriva il portale tedesco e ripartiva da zero. Apriva un annuncio. Copiava i dati.
                  Calcolava il prezzo a mano. Impaginava il PDF. Poi il prossimo annuncio. E il prossimo.
                </p>
                <p className="sv-body sv-muted sp-p">
                  <b>Ore della sua giornata</b>, ogni giorno — bruciate su un lavoro che una macchina fa meglio di lui.
                </p>
                <p className="sv-body sp-p">
                  Allora abbiamo costruito una piccola applicazione privata, solo per loro: incolli il link
                  dell&apos;annuncio, esce il PDF — il loro logo, le caratteristiche che ci hanno chiesto, il prezzo già
                  calcolato. <b>In pochi secondi.</b>
                </p>
                <p className="sp-prova sv-mono">
                  In dieci giorni: <b>{FATTI.novacar.preventivi}</b> preventivi su <b>{FATTI.novacar.marche}</b> marche —
                  circa {FATTI.novacar.minutiPerPdf} minuti a PDF, controlli compresi
                </p>
              </div>

              <div className="sp-chat-wrap">
                <div className="sp-chat" aria-label="Conversazione ricostruita, nomi generici">
                  {CHAT.map((m, i) => (
                    <div key={i} className={`sp-riga-bolla sp-riga-bolla--${m.chi}`}>
                      <span className="sp-avatar" aria-hidden="true">{m.iniziali}</span>
                      <div className={`sp-bolla sp-bolla--${m.chi}`}>
                        <span className="sp-bolla-meta">
                          {m.nome} <span className="sp-bolla-ora">{m.ora}</span>
                          {m.letto && <span className="sp-bolla-letto" aria-hidden="true">✓✓</span>}
                        </span>
                        <p className="sp-bolla-testo">{m.testo}</p>
                      </div>
                    </div>
                  ))}
                </div>
                <svg className="sp-arrow-chat" viewBox="0 0 60 44" aria-hidden="true" focusable="false">
                  <defs>
                    <marker id="sp-arrow-chat-punta" viewBox="0 0 10 10" refX="8.4" refY="5" markerWidth="4.4" markerHeight="4.4" orient="auto">
                      <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                    </marker>
                  </defs>
                  <path d="M4,4 C 24,4 40,20 54,36" fill="none" stroke="#fb4604" strokeWidth="1.2" markerEnd="url(#sp-arrow-chat-punta)" />
                </svg>
                <p className="sp-nota-chat sv-mono">Questa è la richiesta vera, riassunta.</p>
              </div>
            </div>

            <div className="sp-col-img">
              <figure className="sp-img-fig">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/card/storia-pdf.png" width={900} height={700} alt="" loading="lazy" decoding="async" />
              </figure>
            </div>
          </div>

          <div className="sp-schema-wrap">
            <ol className="sp-schema" role="list" aria-label="Dall'annuncio al PDF, in quattro passaggi">
              {SCHEMA.map((s, i) => (
                <li key={s.titolo} className="sp-blocco">
                  <b className="sp-blocco-t">{s.titolo}</b>
                  <span className="sp-blocco-r">{s.riga}</span>
                  {i < SCHEMA.length - 1 && <FrecciaSchema id={`sp-schema-punta-${i}`} />}
                </li>
              ))}
            </ol>
            <svg className="sp-arrow-schema" viewBox="0 0 60 40" aria-hidden="true" focusable="false">
              <defs>
                <marker id="sp-arrow-schema-punta" viewBox="0 0 10 10" refX="1.6" refY="5" markerWidth="4.4" markerHeight="4.4" orient="auto-start-reverse">
                  <path d="M0,1 L9,5 L0,9 z" fill="#fb4604" />
                </marker>
              </defs>
              <path d="M6,4 C 20,16 36,22 54,36" fill="none" stroke="#fb4604" strokeWidth="1.2" markerStart="url(#sp-arrow-schema-punta)" />
            </svg>
            <p className="sp-nota-schema sv-mono">Ogni passaggio che prima era una persona.</p>
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
