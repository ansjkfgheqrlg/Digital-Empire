---
Type: CONCEPT
Status: Active
Tags: #workflow #brand #audit #competitor #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-BRAND-AUDIT — Audit Brand Positioning

> **Workflow:** WF-BRAND-AUDIT · **Reparto:** L2.5 Brand & Creative Strategy
> **Trigger:** richiesta audit da committente (MKT-Conductor, BRAND-LEAD pro-attivo, o richiesta Max)
> **Output:** report audit completo con gap identificati e raccomandazioni prioritizzate
> **Gate di uscita:** BR-QA G5 PASS + approvazione BRAND-LEAD

---

## Scopo

Fotografia completa del brand positioning: chi siamo rispetto al mercato, dove siamo forti,
dove siamo deboli, cosa ci differenzia davvero dai competitor, come è percepita la nostra voce,
dove c'è gap tra come ci posizioniamo e come il mercato ci percepisce. Output: report con
raccomandazioni prioritizzate (3 azioni immediate + 2 evolutive) e flag per WF-BRAND-EVOLUTION
se emerge la necessità di modificare il brand.

---

## Agenti coinvolti

| Agente | Step | Ruolo nel workflow |
|---|---|---|
| `BRAND-LEAD` | 1 (kick-off) + 6 (approvazione) | Riceve richiesta, assegna task, approva report finale |
| `BR4` | 2 | Analisi competitor + awareness mercato + language map ICP |
| `BR1` | 3 | Gap posizionamento: USP attuale vs competitor, spazi vuoti |
| `BR2` | 4 | Audit voice: la voce attuale è coerente con il posizionamento? Deriva? |
| `BR3` | 5 | Audit visual: il visual language riflette il posizionamento? |
| `BR-QA` | 7 (gate) | Gate G5: il report stesso è prodotto nella voce corretta? I dati hanno fonte? |

---

## Passi del workflow

```
[1] BRAND-LEAD — kick-off
  → legge il brief del committente: brand_kit_id, scope (completo/parziale), urgenza
  → verifica in namespace: ultimo audit quando? (max 90gg per audit valido)
  → se audit recente: riusa e aggiorna solo le sezioni cambiate (idempotenza)
  → assegna task a BR4, BR1, BR2, BR3 in parallelo (scope indipendenti)

[2] BR4 — analisi competitiva (in parallelo con [3] [4] [5])
  → controlla 08-INTELLIGENCE: dossier competitor aggiornato?
  → se non aggiornato: raccoglie dati (siti, LinkedIn, case study, recensioni)
  → costruisce: competitor cards (5+ competitor), mappa posizionamento, language map ICP
  → output: dossier_competitor.json in marketing/brand/audit/{brand_id}/

[3] BR1 — analisi gap posizionamento (in parallelo con [2] [4] [5])
  → input: dossier_competitor di BR4 (se pronto) o brief iniziale
  → analizza: dove il brand si posiziona vs mappa competitiva
  → identifica: differenziatori forti, differenziatori deboli, gap di comunicazione
  → formula: USP attuale (come viene percepita vs come dovrebbe essere)
  → output: gap_analysis.md con 3-5 gap prioritizzati per impatto

[4] BR2 — audit voce (in parallelo con [2] [3] [5])
  → prende: ultimi 10-20 output copy del brand (campioni rappresentativi)
  → verifica: tono medio vs voice guide, parole usate vs proibizioni, proof_point frequenza
  → rileva: deriva silenziosà (il tono sta diventando più formale/generico?)
  → output: voice_audit.md con score coerenza 0-100 + pattern di deriva identificati

[5] BR3 — audit visual (in parallelo con [2] [3] [4])
  → prende: campione di asset visual recenti del brand
  → verifica: palette usata vs visual_brief, tipografia, composizione, mood
  → rileva: deviazioni dal brief (colori non nel kit, font non approvati, stili incoerenti)
  → output: visual_audit.md con lista deviazioni e gravità (bloccante / lieve)

[6] BRAND-LEAD — report integrato
  → integra output di BR4 + BR1 + BR2 + BR3
  → costruisce report finale strutturato:
     - sezione 1: stato posizionamento competitivo (da BR4 + BR1)
     - sezione 2: stato voce (da BR2)
     - sezione 3: stato visual (da BR3)
     - sezione 4: gap prioritizzati (3 immediati + 2 evolutivi)
     - sezione 5: raccomandazioni con next action per ogni gap
     - flag: WF-BRAND-EVOLUTION se gap richiede modifica fondamentale brand DE
  → path: marketing/brand/audit/{brand_id}_audit_YYYYMMDD.md

[7] BR-QA — gate G5
  → verifica che il report sia:
     (a) nella voce corretta per il brand (non scrive in voce generica)
     (b) con dati provvisti di fonte per ogni affermazione
     (c) senza claim senza evidenza (niente "il mercato percepisce che..." senza fonte)
  → se PASS: rilascia a BRAND-LEAD per consegna al committente
  → se FAIL: feedback granulare → BRAND-LEAD corregge → nuovo check

[8] CONSEGNA
  → BRAND-LEAD consegna report a MKT-Conductor o al committente diretto
  → aggiorna namespace: marketing/brand/audit/{brand_id}/
  → log in wiki/log.md: "WF-BRAND-AUDIT completato per {brand_id}"
```

---

## Input del workflow

```json
{
  "brand_kit_id": "DE | cliente-X",
  "scope": "completo | posizionamento | voce | visual",
  "committente": "MKT-Conductor | BRAND-LEAD | Max",
  "urgenza": "standard | urgente",
  "deadline": "YYYY-MM-DD",
  "materiali_aggiuntivi": ["link, asset, note dal committente"]
}
```

---

## Output del workflow

```
marketing/brand/audit/{brand_id}_audit_YYYYMMDD.md
  ├── sezione 1: stato posizionamento competitivo
  ├── sezione 2: stato voce (score coerenza + pattern deriva)
  ├── sezione 3: stato visual (deviazioni)
  ├── sezione 4: 3 gap immediati + 2 gap evolutivi
  └── sezione 5: raccomandazioni e next action

marketing/brand/audit/{brand_id}/
  ├── dossier_competitor.json    (BR4)
  ├── gap_analysis.md            (BR1)
  ├── voice_audit.md             (BR2)
  └── visual_audit.md            (BR3)
```

---

## Gate di uscita

| Gate | Chi | Criteri |
|---|---|---|
| G5 — Brand consistency | BR-QA | Dati con fonte, voce coerente, zero claim senza evidenza |
| Approvazione BRAND-LEAD | BRAND-LEAD | Report integrato e coerente, raccomandazioni prioritizzate |
| Flag WF-BRAND-EVOLUTION | BRAND-LEAD | Attivato se gap richiede modifica fondamentale brand DE |

---

## Esempio operativo

**Trigger:** Max richiede audit annuale brand DE.

**Output sintetico:**
- Posizionamento: DE è l'unica agenzia italiana che promette autonomia zero-canoni. Gap:
  non comunichiamo abbastanza il differenziatore "setup 7 giorni" — competitor lo ignorano,
  noi non lo sfruttiamo abbastanza.
- Voce: score 78/100. Deriva lieve: negli ultimi 2 mesi il copy email ha usato "soluzione"
  4 volte (parola vietata). Pattern: quando il tempo stringe, L2.1 scivola sul gergo generico.
- Visual: 2 deviazioni lievi (post LinkedIn con font non del kit), 0 deviazioni bloccanti.
- 3 azioni immediate: (1) aggiornare voice guide con reminder "setup 7 giorni come proof",
  (2) brief a L2.1 su parole vietate con campione difetti, (3) brief a 03-CF su font.
- Flag: nessuna evoluzione fondamentale necessaria — brand sano.

---

## Connessioni

- [[brand-lead]] · `agenti/brand-lead.md`
- [[br4-brand-analyst]] · `agenti/br4-brand-analyst.md`
- [[WF-BRAND-KIT-BUILD]] · `workflow/WF-BRAND-KIT-BUILD.md`
- [[WF-BRAND-EVOLUTION]] · `workflow/WF-BRAND-EVOLUTION.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 brand voice invariante)
