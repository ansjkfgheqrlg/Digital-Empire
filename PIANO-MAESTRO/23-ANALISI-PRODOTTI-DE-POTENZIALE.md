# 23 — ANALISI PRODOTTI DIGITAL EMPIRE: potenziale reale + priorità revenue estate

> Creato 2026-07-23, Claude (Opus). Ordine Max: "analizza i prodotti (Outreach Factory, Content Factory,
> Second Brain, Preventa), il sito agency-empire, hanno potenziale?". + fatto NUOVO: **le pagine IG sono
> a zero.** Dati presi dal codice reale `agency-empire/src/sections/` (non a memoria). Onestà brutale.

---

## §0 — IL FATTO CHE CAMBIA TUTTO: IG morto → fork risolto
Max: "le page ig fanno schifo, praticamente a zero". Conseguenza diretta:
- **Opzione A del fork (dossier 22) È MORTA.** Non c'è audience calda su cui riaccendere il Corso.
- **Il fork si risolve da solo in Opzione B**: niente lancio a pubblico caldo (non esiste). Tutto il revenue
  estate deve venire da **outbound freddo** (l'agenzia contatta, non aspetta inbound).
- Il Corso CCM scende di priorità per l'estate (senza pubblico non si lancia in 1 settimana). Non muore:
  si rimanda a quando c'è traffico (YouTube funnel / outbound), non è un stream di luglio-agosto.

---

## §1 — I NUMERI VERI DEL SITO (agency-empire/src/sections/)
- Vende **2 workflow primari**: **Outreach Workflow** + **Content Workflow**.
- **Prezzo: da €5.000 a €15.000 per workflow** (setup done-for-you). Demo gratuita 30 min. (`11b-carte-scoperte.tsx:48`, `13-faq.tsx:17`).
- Claim di vendita: "workflow da €7.000 si ripaga al primo cliente" · "l'Outreach porta 3-5 clienti/mese, ticket medio cliente €3.000" (`15-objections.tsx:44,57`).
- Terzo servizio (complementare): **Landing Page + CRO**, standalone o add-on.
- **"Second Brain" NON è sul sito.** Max lo elenca come prodotto ma non è confezionato/a listino.

**Implicazione enorme:** il ticket qui è **10-200× quello di Preventa** (€490+€149). **UNA vendita workflow
(€5-15k) vale più di tutti i 7 concessionari di settembre messi insieme** (7×€149 = €1.043/mese). Il centro
di gravità del revenue estate NON è il Corso né Preventa: **è chiudere 1 workflow.**

---

## §2 — POTENZIALE PER PRODOTTO (verdetto onesto)

| Prodotto | Ticket | Ciclo vendita | Potenziale estate | Vincolo reale |
|----------|--------|---------------|-------------------|---------------|
| **Outreach Factory** (Outreach Workflow) | €5-15k build | lungo (demo→proposta→chiusura) | 🟢🟢 **ALTISSIMO** (1 vendita = estate risolta) | lead flow + PROVE (no testimonial) + capacità di delivery |
| **Content Factory** (Content Workflow) | €5-15k build | lungo | 🟢 **ALTO** | domanda leggermente < outreach; stessa esigenza prove |
| **Preventa** | €490 + €149/mese | breve-medio | 🟡 **MEDIO-ALTO** (volume, cash più veloce) | macchina outreach concessionari da costruire |
| **Second Brain** | non a listino | — | 🔴 **BASSO come standalone** | non è un prodotto confezionato; meglio come componente/upsell |

### Outreach Factory — il vero motore (ma non facile)
- **Perché altissimo:** ticket €5-15k. Una chiusura = più di tutto il resto del piano estate insieme.
- **Perché non facile:** ciclo lungo (demo→proposta→firma = settimane), serve un flusso di lead qualificati,
  e — come Andrei (audit CRO 51/100) — **mancano le prove** (testimonial, case study). Con l'IG morto,
  l'unico modo di alimentarlo è **outbound freddo**.
- **La leva geniale (dogfooding):** l'agenzia VENDE una macchina di outreach a freddo. **Usiamola su noi
  stessi** per prenotare demo dei workflow. Il prodotto genera i lead del prodotto. È anche la miglior prova
  possibile: "il sistema che ti vendo è quello con cui ti ho trovato".
- **Vincolo di capacità (onesto):** €5-15k = done-for-you reale. Ogni cliente va costruito da Max+Gael.
  Realisticamente **1-2 clienti max** consegnabili in estate. Il potenziale è alto per unità, limitato in volume.

### Content Factory — secondo, stesso tier
- Stesso prezzo/modello. Domanda un filo inferiore (l'outreach vende "clienti nuovi" = dolore più acuto del
  "pubblico contenuti"). Da vendere in bundle o come secondo passo dopo l'Outreach.

### Preventa — il cash più veloce, tier diverso
- Ticket basso ma **ciclo più corto e prodotto già vivo** (Novacar = prova reale esistente!). È il complemento
  perfetto ai workflow: mentre insegui 1 workflow da €10k (lento), Preventa fa cassa a volume più in fretta.
- **Va in sezione NUOVA e SEPARATA** sul sito (non nella grid dei 2 workflow): è un prodotto SaaS verticale
  per concessionari, non un build custom da €10k. Mischiarlo confonde il posizionamento.

### Second Brain — non forzarlo come prodotto
- Venderlo standalone a freddo è difficile (nessuno cerca "compro un second brain"). **Meglio:** componente
  incluso nei workflow ("ti diamo anche la knowledge base"), oppure upsell. Non farne un pilastro estate.

---

## §3 — RIPRIORITIZZAZIONE REVENUE ESTATE (dopo questi dati)

1. **🥇 Outreach Factory via dogfooding** — puntare 1 workflow (€5-15k). Motore: la nostra stessa macchina
   outreach a freddo → prenota demo. Prova = Novacar + il fatto che li abbiamo trovati col sistema.
2. **🥈 Preventa** — cash a volume più veloce, cold outreach concessionari nuovi (i 7 restano settembre).
3. **🥉 Content Factory** — bundle/secondo passo dopo contatto Outreach.
4. **Corso CCM** — parcheggiato per l'estate (no audience). Riparte con traffico (YouTube/outbound), non ora.
5. **Second Brain** — componente/upsell, non pilastro.
6. **NFT** — lane speculativa separata (dossier 22 §M4), fuori dal piano.

**Nuovo modello di cassa (onesto):** l'estate si gioca su **1 numero grande** (un workflow €5-15k, prob.
media, alto payoff) **+ un flusso piccolo** (Preventa, prob. più alta, payoff minore). Il primo è il jackpot,
il secondo è il pane. Entrambi via outbound freddo — perché l'inbound (IG) non esiste.

---

## §4 — TASK AGGIORNATI (agganciati al dossier 22)

### GAEL
- **G-EST-1 (aggiornato) — Sezione Preventa sul sito** `agency-empire/src/sections/03b-preventa.tsx`:
  sezione NUOVA e SEPARATA dopo i 2 workflow, posizionamento SaaS verticale concessionari (canone+kill-switch,
  non build €10k). Stile empire. Import in `page.tsx` dopo `03-servizi`. Gate: `npm run build` verde.
- **G-EST-2 — Macchina outreach freddo** (wrap ADR-003): serve DUE target → (a) aziende/agenzie per i workflow
  €5-15k (dogfooding), (b) concessionari per Preventa. Un motore, due liste, due script APSOC.
- **G-EST-5 (nuovo) — Sezione PROVE sul sito**: aggiungere testimonial/case study (Novacar reale) — è il gap
  CRO n.1 (come Andrei). Senza prove, un ticket da €10k non si chiude a freddo. Anche 1 case study cambia tutto.

### MAX
- **M-EST-6 (nuovo) — Chi è il cliente ideale dei workflow €5-15k?** (settore, dimensione, dove trovarlo)
  → serve per puntare la macchina outreach. Senza ICP, l'outbound spara nel buio.
- **M-EST-7 (nuovo) — Delivery: quanti workflow puoi consegnare in estate?** (capacità reale tua+Gael).
  Se è 1, l'outbound punta qualità non volume.
- M-EST-1 audience → **CHIUSA**: IG a zero, confermato. Fork → Opzione B.
- M-EST-4 prezzo Preventa (€490/€149) resta da vetare.

---

## §5 — RISPOSTA SECCA ALLA TUA DOMANDA "hanno potenziale?"
**Sì, e più di quanto pensavi — ma non dove guardavi.**
- **Outreach/Content Factory: potenziale ALTISSIMO** (€5-15k a vendita, una chiusura risolve l'estate). Il
  freno non è il prodotto, è che manca il **flusso di lead** (IG morto) e le **prove**. Entrambi risolvibili:
  outbound con la nostra stessa macchina + mettere Novacar come case study.
- **Preventa: potenziale solido e più veloce** (cash a volume), tier diverso, sezione sua sul sito.
- **Second Brain: no come prodotto standalone**, sì come componente.
- **Il vero sblocco dell'estate = flusso di lead a freddo + 1 prova credibile.** Non un altro prodotto: far
  girare la macchina che già vendiamo, su noi stessi.
