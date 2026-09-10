---
name: beast-preventivi
description: >
  Usa questa skill ogni volta — anche se l'utente non dice esplicitamente "preventivo" ma menziona "quanto chiedo?", "come struturo la proposta?", "il cliente chiede il prezzo", "non so quanto farmi pagare" o "devo rispondere a un cliente". Costruisce preventivi freelance/agenzia che vendono, applicando il principio problem-first: tutto ruota attorno al problema del cliente. Adatta automaticamente al livello di consapevolezza del cliente (aware/unaware). Genera outline → documento completo su richiesta. Use this skill whenever a freelancer or agency needs to price and structure a commercial proposal.
---

# Beast Preventivi

> Il preventivo non è una lista prezzi. È una lettera di vendita che dimostra di capire il problema del cliente.

## Principio cardine

**Tutto gira intorno al problema.** Per vendere bisogna risolvere un problema.
Il preventivo non dice "ecco cosa faccio" — dice "ecco come risolvo il tuo problema e cosa otterrai".

Fondamenta teoriche + applicazione pratica: `references/concepts/problem-centric-selling.md`

---

## Contratto d'ingresso — senza questi, il documento non si scrive

Tre elementi sono obbligatori. Se ne manca anche uno solo: **chiedilo e rifiuta di produrre il
documento completo**. L'outline si puo' fare comunque (serve proprio a far emergere cosa manca); il
documento no.

1. **Brief di discovery** — output della skill `discovery-call-brief`, oppure la trascrizione o gli
   appunti grezzi della call.
2. **Il prezzo a catalogo applicabile** — uno dei quattro di `proposal-gate` punto 3
   (EUR 4.000 Outreach Factory / EUR 3.500 Content Factory / EUR 2.500 Second Brain /
   EUR 8.000 Engine Room). Mai un prezzo improvvisato.
3. **Il problema del cliente con le parole del cliente** — non una riformulazione di marketing. E' il
   punto 1 di `proposal-gate`, e senza di esso il documento nasce gia' bocciato.

**Perche' il rifiuto e non un semplice avviso:** `proposal-gate` blocca comunque a valle, ma solo
DOPO che il documento e' stato scritto. Bloccare a monte risparmia l'intera scrittura. Digital Empire
applica gia' questa disciplina ai gate di uscita (`proposal-gate` blocca, Content Forge Stage 8
blocca, i gate YouTube bloccano) e quasi mai ai contratti d'ingresso: questa e' la correzione di
quell'asimmetria, nel punto in cui costa di piu'.

Fonte: studio Andrei Pascu, cs2online Bonus 6 (KA-05 — SKILL.md scritto per "rifiutarsi
categoricamente di procedere" senza i documenti obbligatori) e cs2online Bonus 2 (KA-04 —
validazione dei dati obbligatori completata prima della generazione) — candidati AP-006 (patch A) e
AP-020, innestati 2026-09-10. L'automazione AI dei preventivi resta NO-GO
(`competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-B-capacita.md` §3.3).

---

## Come usare questa skill

**Step 1 — Fornisci il contesto cliente**

Se non già fornito, chiedi:
- Chi è il cliente? (settore, dimensione)
- Qual è il suo **problema** (non il servizio che chiede — il problema sottostante)
- Budget range (anche approssimativo)
- Il cliente è **consapevole** del problema o no?
- Hai già fatto la discovery call?

Livelli consapevolezza: `references/patterns/client-awareness.md`

**Step 2 — Scegli il percorso**

```
Hai già fatto discovery call?
├── Sì → [Build Document] (sezione sotto)
└── No → [Discovery Phase] (sezione sotto) — fai prima discovery, poi torna qui
```

**Step 3 — Output**
Genera prima l'**outline** (8 sezioni + prezzi bozza) → presentalo → su conferma genera il **documento completo**.

---

## Discovery Phase

Se non hai ancora fatto la discovery call:

Guida completa: `references/stages/01-discovery.md`

Principi chiave:
- Fai domande sul **problema**, non sul servizio richiesto
- Identifica il budget con la tecnica dell'ancoraggio — non chiedere "qual è il tuo budget?"
- **Non dare mai il prezzo prima della discovery**
- Durata minima: 30 min

---

## Build Document

Struttura canonica del preventivo in 8 sezioni:

| # | Sezione | Focus |
|---|---------|-------|
| 1 | Cover | Brand, prima impressione |
| 2 | Intro / USP | Perché noi, non altri |
| 3 | Il problema del cliente | Mirror back — dimostri di capire |
| 4 | Risultati attesi | Outcome misurabili, non feature |
| 5 | Deliverables | Cosa includiamo esattamente |
| 6 | Investment | 3 opzioni, mai listino |
| 7 | CTA + Scadenza | Next step chiaro, urgency |
| 8 | Contratto | Termini essenziali |

Template da compilare: `assets/templates/preventivo-canvas.md`
Dettaglio di ogni sezione: `references/stages/03-document-structure.md`

---

## Pricing Strategy

- **Mai** dare un numero prima della discovery
- **Sempre** 3 opzioni (Essenziale / Professionale / Full Service)
- **Cushion** del 10% sul prezzo mentale prima di scriverlo
- **Numeri tondi** — 2.000€ non 1.980€
- **Niente sconti** — proponi riduzione scope invece

Dettaglio completo: `references/stages/02-pricing.md`

---

## Presentation Call

Quando presenti il preventivo al cliente:
- Screen share obbligatorio — non mandare senza presentare
- Leggi insieme, commenta le sezioni chiave
- **Silenzio dopo il prezzo** — non giustificarti prima che lo chiedano
- Gestione obiezioni scriptata

Guida completa: `references/stages/04-call-presentation.md`

---

## Anti-patterns — evita sempre

`references/conventions/anti-patterns.md`

Top 5 fatali:
1. Mandare il preventivo senza call di presentazione
2. Iniziare il documento dalla lista prezzi
3. Scrivere il preventivo come una fattura (voce 1: X€, voce 2: Y€)
4. Giustificare il prezzo prima che il cliente lo chieda
5. Concedere sconti quando vengono richiesti

---

## Esempio end-to-end

Landing page agency → cliente e-commerce fashion: `assets/examples/landing-page-agency.md`

---

## Riferimento futuro (non applicato)

Lo studio competitor su Andrei Pascu (cs2online Bonus 6) documenta un sistema maturo di generazione
preventivi via AI con struttura a pagine (flowchart + SOP + skill Obsidian), osservato per intero in
un corso a pagamento — utile come secondo caso di studio se in futuro si decide di estendere questa
skill con automazione AI. Non risolve la tensione aperta su breakdown prezzi sì/no (segnalata a Max
nel run YouTube, mai decisa) — resta una scelta di Max.

---

## Routing rapido

| Se vuoi... | File |
|---|---|
| Capire il principio problem-first | `references/concepts/problem-centric-selling.md` |
| Preparare la discovery call | `references/stages/01-discovery.md` |
| Strutturare il documento | `references/stages/03-document-structure.md` |
| Decidere i prezzi (3 opzioni) | `references/stages/02-pricing.md` |
| Presentare il preventivo in call | `references/stages/04-call-presentation.md` |
| Adattare a cliente aware / unaware | `references/patterns/client-awareness.md` |
| Checklist errori da evitare | `references/conventions/anti-patterns.md` |
| Template da compilare | `assets/templates/preventivo-canvas.md` |
