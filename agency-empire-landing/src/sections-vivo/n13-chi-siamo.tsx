import { Aura } from "@/components/vivo/aura";
import { FATTI } from "@/lib/fatti";

/* N13 — Chi siamo: la stanza (sv-stanza, unica volta), tre volti veri (posti 10-12; senza file: solo i nomi),
   la storia in prima persona: 2 paragrafi visibili + resto in <details>. Copy: COPY.md §N13. */
const PERSONE = [
  { file: "n13-max.webp", nome: "Maximilian (Max)", ruolo: "Fondatore", testo: "Sei anni di marketing, tre di AI a tempo pieno. Architetto dei flussi, voce del copy, quello che ha costruito il primo Outreach Factory per sé.", alt: "Maximilian (Max), fondatore" },
  { file: "n13-gael.webp", nome: "Gael", ruolo: "Socio, pari grado", testo: "Costruisce e tiene in piedi i sistemi dei clienti. Ci siamo conosciuti in un campeggio a Follonica, non in un ufficio.", alt: "Gael, socio pari grado" },
  { file: "n13-leonardo.webp", nome: "Leonardo", ruolo: "Team Empire", testo: "Esecuzione, presenza in ogni stanza dove si decide cosa spediamo e come. Quando lavori con noi, costruisci anche con lui.", alt: "Leonardo, team Empire" },
];

export function ChiSiamo() {
  return (
    <section id="chi-siamo" className="sv sv-stanza sv-section" aria-labelledby="chi-siamo-h2">
      <div className="sv-container">
        <p className="sv-eyebrow">«Ok, ma voi chi siete?» — Giusto. Guarda: siamo in {FATTI.persone}.</p>
        <h2 id="chi-siamo-h2" className="sv-h2 mt-3 max-w-[18ch]">
          Parli con chi ha le mani sui workflow. <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Per scelta, non per limite.</span>
        </h2>

        <ul className="mt-10 grid md:grid-cols-3 gap-8">
          {PERSONE.map((p) => (
            <li key={p.nome}>
              <Aura file={p.file} alt={p.alt} className="aspect-[4/5] max-w-[320px] mb-5" />
              <p className="sv-etichetta">{p.ruolo}</p>
              <h3 className="sv-h3 mt-2">{p.nome}</h3>
              <p className="sv-body sv-muted mt-2 max-w-[38ch]">{p.testo}</p>
            </li>
          ))}
        </ul>

        <p className="sv-lead sv-muted mt-10 max-w-[60ch]">
          Niente account manager in mezzo: chi ti risponde è chi ha scritto il codice. E sì: alla fine di questa pagina ti proponiamo di
          lavorare insieme. Ci guadagniamo tutti e due, o non lo faremmo.
        </p>

        <div className="mt-12 max-w-[64ch]">
          <p className="sv-eyebrow">La storia · in prima persona</p>
          <p className="sv-body mt-4">
            Sei anni fa ero un ragazzo ossessionato da Internet. Tutto è iniziato con YouTube. Ho provato tutto — non per dispersione, per
            un bisogno affamato di capire come funzionano davvero le cose.
          </p>
          <p className="sv-body sv-muted mt-4">
            Poi ho incontrato il copywriting, e ho capito che non è scrittura: è architettura della decisione. Spostare una scelta usando
            solo testo. Da lì l&apos;ho messo dentro ogni singolo passo del mio lavoro.
          </p>
          <details className="sv-dett">
            <summary>Continua a leggere</summary>
            <p>
              Poi l&apos;intelligenza artificiale: ogni release, ogni modello, ogni feature, usata per costruire sistemi che lavorano al
              posto tuo. Oggi fanno outreach, scrivono copy, tengono la conoscenza — per noi e per i clienti.
            </p>
            <p>
              A {FATTI.meseNascita} {FATTI.annoNascita} ho deciso di non lavorare più da solo. Avevo il metodo, i sistemi, i clienti che
              bussavano. Mancava un team con cui costruire qualcosa di più grande di me. Digital Empire è questo. Il sogno non è
              realizzato: lo sto realizzando, ogni giorno.
            </p>
          </details>
        </div>

        <p className="sv-small mt-10" style={{ color: "var(--sv-silver)" }}>
          L&apos;agenzia progettata per essere licenziata: ti consegniamo un sistema che cammina da solo, non una dipendenza.
        </p>
      </div>
    </section>
  );
}
