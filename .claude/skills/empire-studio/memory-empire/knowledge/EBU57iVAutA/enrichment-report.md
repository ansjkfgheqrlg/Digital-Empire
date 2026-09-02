# Enrichment Report — EBU57iVAutA
## Stage D/E/F/G — Memory Empire

**Video:** Se scrivi QUESTO nel tuo preventivo NON venderai
**Data:** 2026-08-26

---

## ⚠️ Stage D — SCOPERTA PRINCIPALE: tensione reale con skill esistente `beast-preventivi`

Questo video tratta esattamente il dominio di uno skill Digital Empire GIÀ ESISTENTE e maturo:
`C:\Users\Utente\.claude\skills\beast-preventivi\` (stages 01-discovery, 02-pricing, 03-document-structure,
04-call-presentation, conventions/anti-patterns.md). Non era mai stato individuato prima nel run
perché nessun video precedente trattava preventivi/proposal. Confronto punto per punto:

| KA di questo video | Confronto con `beast-preventivi` | Esito |
|---|---|---|
| KA-05-09 (struttura 5 pagine, prezzo alla fine) | Stage 03: struttura 8 sezioni, stesso principio "il prezzo appare alla fine, dopo aver costruito valore" | **CONFERMA** — stesso principio, Andrei propone una variante più compatta (5 pagine vs 8 sezioni) |
| KA-12 (mostralo in call, mai solo inviare) | Stage 04: "Mai mandare il preventivo senza presentarlo in call. Mai." | **CONFERMA identica**, quasi verbatim |
| KA-15 (dire il prezzo poi silenzio) | Stage 04, sezione "Il silenzio post-prezzo": "Non aggiungere niente dopo aver detto i prezzi... aspetta" | **CONFERMA identica** — stesso principio, stessa tecnica ("Bam, press price" ≈ "Silenzio") |
| KA-13 (essere diretti, no diplomazia eccessiva) | Stage 04, script gestione obiezioni ("Non difenderti. Non scendere di prezzo") | **CONFERMA di spirito**, skill esistente più specifico (script per obiezione) |
| KA-16 (struttura a 3 chiamate prima del preventivo) | Stage 01 discovery: struttura a 2 touchpoint (discovery call → call di presentazione) | **VARIANTE complementare**, non contraddizione — Andrei scala a 3 chiamate per progetti più complessi/costosi |
| **KA-14 (breakdown dei prezzi per componente: affitto+attori+makeup+operatore)** | **`anti-patterns.md` AP-05 "Preventivo formato fattura": "Voce 1: Wireframe 200€, Voce 2: Design 400€..." è marcato BLOCCANTE — "il cliente valuta ogni voce singolarmente e le trova tutte care"** | **⚠️ TENSIONE REALE, non risolta automaticamente** |

### Dettaglio della tensione KA-14 vs AP-05

Il video raccomanda esplicitamente di scomporre un prezzo alto in componenti di costo quando il
servizio è complesso ("€5.000 = affitto camera €900 + attori €500 + makeup €500 + operatore €250...")
per renderlo comprensibile invece che sospetto. Lo skill `beast-preventivi` esistente marca questa
esatta pratica come anti-pattern BLOCCANTE (AP-05), con la motivazione opposta: il breakdown invita
il cliente a valutare/negoziare ogni voce singolarmente.

**Non ho applicato una patch automatica** — questo è un caso che richiede un giudizio umano, non
una correzione meccanica. Ipotesi di riconciliazione (non verificata, solo proposta):
- AP-05 sembra riferirsi a scomposizione in **voci di FATTURA/servizio** (wireframe, design, sviluppo)
  dentro un'unica offerta — il rischio è che il cliente tratti ogni voce come negoziabile a sé.
- Il video invece scompone in **costi OPERATIVI sottostanti** (affitto, personale, attrezzatura) per
  giustificare il totale — non presenta le componenti come voci acquistabili separatamente, ma come
  spiegazione del "perché costa così tanto".
- Se questa distinzione regge, i due principi potrebbero NON essere in vera contraddizione (fee
  itemization = anti-pattern; cost-of-goods transparency = tecnica valida) — ma è un'ipotesi mia,
  non verificata con un secondo esempio, e tocca un file (`anti-patterns.md`) che è chiaramente il
  frutto di un lavoro di sistematizzazione precedente più ampio di questo singolo video. **Segnalo
  esplicitamente questa tensione a Max/al conductor invece di risolverla unilateralmente.**

---

## Stage D — Altre connessioni

| Questo video | Concetto esistente | Connessione |
|-------------|-------------------|--------------|
| KA-07 (obiettivi/risultati del cliente prima dei servizi) | Video 19 del run (CTA), framework "Situazione Attuale vs Situazione di Desiderio" | Stesso principio (risultati desiderati, non meccanica del servizio) applicato a un documento diverso — coerenza cross-dominio nel canale, non un gap. |
| KA-11 (estetica, template Canva, logo) | `beast-preventivi` Stage 03 Sezione 1 "Tono: professionale, curato" | Coerente, nessuna azione. |

---

## Stage D — Nuovi Concetti Identificati

**Nessuna nuova pagina Concept.** Il contenuto conferma in larghissima parte un framework DE già
esistente e più maturo (`beast-preventivi`) — non introduce un dominio nuovo. L'unico elemento
realmente degno di nota è la tensione KA-14/AP-05 sopra descritta, che richiede una decisione, non
una nuova pagina.

---

## Stage D — Applicazioni DE

| Concetto | Applicazione Digital Empire | Azione |
|----------|------------------------------|--------|
| Tensione breakdown prezzi (KA-14 vs AP-05) | `beast-preventivi/references/conventions/anti-patterns.md` | **NON APPLICATO — segnalato per decisione umana.** Non modifico un file di regole "BLOCCANTI" già sistematizzato sulla base di un singolo esempio esterno in apparente contraddizione. |
| Struttura a 3 chiamate per progetti complessi (KA-16) | `beast-preventivi/references/stages/01-discovery.md` | **PROPOSTO, non eseguito**: potrebbe essere una nota "variante per progetti ad alto ticket/complessità" — non applicato ora, singolo esempio, lo stage esistente già copre lo scenario base efficacemente. |

---

## Stage E — Gate di Qualità

| Check | Status | Note |
|-------|--------|------|
| NO-FINTO | PASS | 11/11 frame descritti = 11/11 letti nativamente; campionamento (11/263, non coverage 100%) dichiarato e giustificato — video lungo, 5 capitoli ufficiali usati |
| P12 traceability | PASS | Ogni KA ha source video#timestamp (+ frame dove disponibile) |
| Coverage sezioni | PASS | 5 capitoli ufficiali, tutti rappresentati nei KA |
| Quote dirette VTT | PASS | Trascrizione quasi integrale in contenuto-integrale.md (segmento sponsor centrale condensato, dichiarato esplicitamente) |
| Pattern estratti | PASS | 4 pattern in video-analysis.md |
| Connessioni KB | PASS | Confronto sistematico con skill esistente pertinente (`beast-preventivi`), non solo `cro-copy-architect` |
| Nuovi concetti | PASS (nessuno creato, motivato) | Contenuto prevalentemente confermativo di uno skill già maturo |
| Applicazioni DE | PASS | 0 applicate — 1 tensione segnalata esplicitamente per decisione umana, 1 proposta minore non eseguita |

**GATE: PASS** (con segnalazione attiva, non uno "PASS silenzioso")

---

## Stage F — Applicazione

**Fatto in questa sessione:** nessuna modifica a skill file. La scoperta principale (tensione
KA-14/AP-05) è stata deliberatamente NON risolta con una patch automatica — è il tipo di conflitto
tra una regola sistematizzata esistente e un singolo esempio esterno che richiede giudizio umano,
non una correzione meccanica di Memory Empire. Riportata qui e nel report di sessione a Max.

---

## Stage G — Audit

**Lacune / incertezze:**
- Segmento sponsor (~4:10-5:13) condensato per estratti nel contenuto-integrale.md invece di
  trascritto integralmente — dichiarato esplicitamente, contenuto promozionale ripetitivo non
  rilevante per i Knowledge Atom.
- Errore probabile di trascrizione automatica nel VTT: "IVA sarà €22" su un prodotto da €10 (dovrebbe
  essere €2,2 al 22%) — segnalato nel contenuto-integrale.md come nota, non riportato come fatto nei KA.

**Cross-reference:** Primo video del run sul dominio "preventivo/proposal commerciale" — rivela
l'esistenza di uno skill DE dedicato (`beast-preventivi`) più maturo e specifico di quanto emerso
finora dal run, con cui la maggior parte del contenuto converge, tranne la tensione KA-14/AP-05.

---

## Prossimo Video

Video 25 (`uqa06rlgmj4`, "Come migliorare con gli hook (1 consiglio)") — mai iniziato.
