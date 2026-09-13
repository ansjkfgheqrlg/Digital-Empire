/* RIFATTA 42 — Objections «Le 4 obiezioni» (BRIEF F3, blocco B; 39B §2 r.42; 39A E33).
   Sostituisce <Objections /> in page.tsx (lo scambio lo fa Emperator). Il TESTO è copiato parola per parola
   da src/components/sections/objections.tsx, nello stesso ordine di lettura (eyebrow → citazione → kicker →
   3 blocchi «0N // KIND» + titolo + testo). Cambia solo la forma: carta, per ogni obiezione la citazione a 24 px
   (serif corsivo, le virgolette sono già nel testo) in una colonna a sinistra e i 3 paragrafi in una colonna da
   720 px a destra, con etichetta mono; niente card, niente lettere in filigrana (C/P/B: erano decorative,
   scala.css le nasconde già nel live), niente virgolettone gigante. 0 KB di JS. CSS: src/app/rifatte-b.css (.rb-ob*).
   NOTA: la rinomina delle etichette in «Dici / I fatti / Cosa cambia» NON è applicata perché la REGOLA ASSOLUTA
   vuole il testo di giugno identico («01 // CLAIM» ecc.). Se Max la vuole, basta cambiare ETICHETTA qui sotto. */

const ETICHETTA: Record<string, string> = { CLAIM: "CLAIM", PROOF: "PROOF", BENEFIT: "BENEFIT" };

const groups = [
  {
    eyebrow: "Obiezione #01 · Il tool",
    title: "“ChatGPT fa già tutto questo, gratis.”",
    kicker: "ChatGPT è una chat. Questo è un sistema.",
    cards: [
      { kind: "CLAIM", t: "ChatGPT non manda 300 email al giorno.", d: "Una chat risponde a domande. Un sistema autentica account, gestisce proxy, calibra timing, qualifica risposte e notifica su Slack — in automatico, h24." },
      { kind: "PROOF", t: "Outreach reale vs prompt manuale.", d: "Un utente ChatGPT manda ancora i messaggi a mano, uno ad uno. Il nostro sistema manda 300+ messaggi personalizzati al giorno, con follow-up automatici." },
      { kind: "BENEFIT", t: "Il sistema lavora mentre dormi.", d: "ChatGPT si ferma quando chiudi il browser. Il sistema AI proprietario gira h24 sui tuoi server, indipendentemente da te." },
    ],
  },
  {
    eyebrow: "Obiezione #02 · Il rischio ban",
    title: "“Ma Instagram mi banna se automatizzo.”",
    kicker: "Proxy residenziali dedicati. Zero rischio.",
    cards: [
      { kind: "CLAIM", t: "Il sistema simula comportamento umano.", d: "Timing randomizzato, pause naturali, sequenze di azioni che replicano un utente reale. I detection system di Instagram non vedono un bot." },
      { kind: "PROOF", t: "Proxy residenziali per ogni account.", d: "Ogni profilo Instagram ha il suo IP residenziale dedicato. Stesso IP di un utente reale, nella stessa area geografica. Zero shared proxy." },
      { kind: "BENEFIT", t: "Blindatura tecnica inclusa nel setup.", d: "Configurazione proxy, warm-up account progressivo, rate limiting intelligente. Il setup antidetection è parte integrante del sistema — non un extra." },
    ],
  },
  {
    eyebrow: "Obiezione #03 · La qualità copy",
    title: "“Il copy generato dall’AI sembra robotico.”",
    kicker: "APSOC Framework calibrato sul tuo ICP.",
    cards: [
      { kind: "CLAIM", t: "Il problema non è l'AI. È il prompt.", d: "Un modello generico scrive in modo generico. Il nostro sistema usa APSOC Framework, addestrato sul tuo brand, il tuo ICP e il tuo tono di voce esatto." },
      { kind: "PROOF", t: "Calibrazione pre-go-live obbligatoria.", d: "Prima del lancio, addestriamo il copy engine su esempi reali del tuo settore. Il sistema scrive come se fossi tu a scriverlo — perché è esattamente il tuo stile." },
      { kind: "BENEFIT", t: "Copy personalizzato su ogni lead.", d: "Ogni messaggio usa dati reali del prospect: nome, settore, profilo. Non un template con variabili — una scrittura contestuale generata in tempo reale." },
    ],
  },
  {
    eyebrow: "Obiezione #04 · La dipendenza",
    title: "“Diventerei dipendente da voi per sempre.”",
    kicker: "Il codice è tuo. Zero dipendenza strutturale.",
    cards: [
      { kind: "CLAIM", t: "Consegniamo il codice sorgente completo.", d: "Non un accesso a un pannello che gestiamo noi. Ti diamo il codice sorgente commentato, la documentazione tecnica e la formazione su come gestirlo." },
      { kind: "PROOF", t: "90 giorni di supporto, poi sei libero.", d: "Il supporto dedicato dura 90 giorni. Dopo quel periodo il sistema gira da solo — e se hai bisogno di modifiche, puoi farle tu o ingaggiare qualsiasi sviluppatore." },
      { kind: "BENEFIT", t: "Asset aziendale permanente.", d: "Un SaaS ti taglia fuori se smetti di pagare. Il tuo sistema AI gira finché vuoi, sui tuoi server, sotto il tuo controllo totale. Per sempre." },
    ],
  },
];

export function ObjectionsV2() {
  return (
    <div className="vivo">
      <section id="obiezioni" className="sv sv-carta sv-section rb-ob" aria-labelledby="obiezioni-h2">
        <div className="sv-container">
          <header className="rb-ob-testa">
            <span className="sv-eyebrow"><b>Gestione Obiezioni // Risposta diretta</b></span>
            <h2 id="obiezioni-h2" className="sv-h2 mt-3">
              Le 4 obiezioni che <span className="sv-it rb-accento">demoliamo</span> prima di iniziare.
            </h2>
          </header>

          {groups.map((g) => (
            <div key={g.eyebrow} className="rb-ob-gruppo">
              <div className="rb-ob-voce">
                <span className="sv-mono rb-accento">{g.eyebrow}</span>
                <h3 className="rb-ob-cit">{g.title}</h3>
                <p className="sv-mono rb-ob-kicker">→ {g.kicker}</p>
              </div>
              <div className="rb-ob-risposte">
                {g.cards.map((c, i) => (
                  <div key={c.kind} className="rb-ob-par">
                    <span className="sv-mono rb-ob-k">0{i + 1} // {ETICHETTA[c.kind]}</span>
                    <h4>{c.t}</h4>
                    <p className="sv-body">{c.d}</p>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
