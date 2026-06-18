---
Type: CONCEPT
Status: Active
Tags: #workflow #brand #kit #build #multi-tenant #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-BRAND-KIT-BUILD — Costruzione Brand Kit

> **Workflow:** WF-BRAND-KIT-BUILD · **Reparto:** L2.5 Brand & Creative Strategy
> **Trigger:** nuovo cliente agency, nuovo canale DE, nuovo prodotto multi-brand
> **Output:** brand_kit completo in `marketing/brand/kits/{brand_kit_id}/`
> **Gate di uscita:** BR-QA G5 PASS + BRAND-LEAD firma il kit

---

## Scopo

Costruire un brand_kit completo e operativo per un nuovo soggetto (cliente agency, canale DE,
prodotto multi-brand). Il kit è il prerequisito per ogni richiesta copy: senza kit dichiarato,
L2.1 blocca la richiesta. Il kit contiene 4 artefatti: voice_guide, visual_brief, icp, tone_chart.

**Principio:** il kit non è un documento di stile per l'identità estetica — è un sistema
operativo di regole binarie che A1-A8 di L2.1 seguono ad ogni run. Deve essere abbastanza
specifico da rendere inutile ogni interpretazione soggettiva.

---

## Agenti coinvolti

| Agente | Step | Ruolo nel workflow |
|---|---|---|
| `BRAND-LEAD` | 1 (kick-off) + 6 (revisione integrata) + 8 (firma) | Riceve brief, coordina, approva kit integrato |
| `BR4` | 2 | Ricerca ICP + analisi competitor del settore del committente |
| `BR1` | 3 | Posizionamento + USP + angolo di differenziazione |
| `BR2` | 4 | Voice guide operativa + tone chart |
| `BR3` | 5 | Visual brief (palette, tipografia, mood, reference, regole per canale) |
| `BR-QA` | 7 (gate) | Gate G5: il kit è internamente coerente? Non contraddice Mandato Art.2? |

---

## Passi del workflow

```
[1] BRAND-LEAD — kick-off e scope
  → riceve brief dal committente (via MKT-Conductor o direttamente)
  → verifica: esiste già un kit parziale in namespace? Se sì → aggiornamento, non creazione da zero
  → definisce scope: nuovo cliente completo / nuovo canale / aggiornamento sezione specifica
  → crea folder: marketing/brand/kits/{brand_kit_id}/
  → assegna task: BR4 (ricerca) → poi BR1 + BR2 + BR3 in parallelo (input condiviso da BR4)

[2] BR4 — ricerca ICP + analisi competitor
  → raccoglie: chi è l'ICP del committente (pain, obiettivi, linguaggio, fear)
  → analizza: 3-5 competitor del committente (posizionamento, voce, offer principale)
  → costruisce: competitor_map + language_map_ICP (citazioni reali dal linguaggio ICP)
  → output: research_brief.json → condiviso con BR1, BR2, BR3 per i loro step

[3] BR1 — positioning (input: research_brief di BR4)
  → formula: positioning statement tecnico + USP frase breve + angolo dominante
  → costruisce: matrice differenziazione (attributi vs competitor)
  → identifica: proof_point richiesti (dati/casi necessari per supportare l'USP)
  → output: positioning.md → input per BR2

[4] BR2 — voice guide + tone chart (input: positioning di BR1 + research_brief di BR4)
  → formalizza: tono, registro, parole vietate, pattern retorici preferiti, proibizioni assolute
  → produce: 2+ esempi "così sì" + 2+ esempi "così no" per ogni regola principale
  → costruisce: tone_chart per canali attivi (email, ads, social, ecc.)
  → output: voice_guide.md + tone_chart.md

[5] BR3 — visual brief (input: positioning di BR1 + voice_guide di BR2)
  → definisce: palette colori (primario, secondario, accento, neutri), font system, spacing
  → costruisce: mood board descrittivo (3-5 reference visivi con motivazione)
  → produce: regole visuali per piattaforma (Instagram / Meta Ads / LinkedIn / YouTube)
  → output: visual_brief.md

[6] BRAND-LEAD — revisione integrata
  → verifica coerenza cross-artefatto:
     - il visual brief amplificia il posizionamento?
     - la voice guide riflette i differenziatori?
     - la tone chart è applicabile senza interpretazione?
     - l'ICP in icp.md è allineato alla language map di BR4?
  → produce: icp.md finale (sintesi ICP per il kit)
  → consolida i 4 artefatti nella cartella brand_kit_id/
  → eventuali richieste di revisione mirate a BR1/BR2/BR3 prima di passare a BR-QA

[7] BR-QA — gate G5
  → check interno al kit:
     (a) voice guide non contraddice Mandato Art.2 (niente claim senza proof come regola,
         niente dependency-language istruita come stile)
     (b) visual brief non usa elementi vietati (es.: brand DE non può avere logotipi confondibili)
     (c) tono del kit stesso è coerente con la voce formalizzata
     (d) ICP è specifico (non "tutti gli imprenditori" ma "titolare PMI manifattura 10-50 dipendenti")
  → se PASS: rilascia il kit a BRAND-LEAD per firma
  → se FAIL: feedback granulare → BRAND-LEAD corregge → nuovo check

[8] BRAND-LEAD — firma e rilascio
  → aggiorna namespace: marketing/brand/kits/{brand_kit_id}/ con 4 file (voice_guide.md,
    visual_brief.md, icp.md, tone_chart.md) + metadata (data_creazione, data_scadenza_review,
    brand_kit_version: "1.0")
  → aggiorna state/README.md: catalogo brand_kit attivi
  → notifica MKT-Conductor: "kit {brand_kit_id} attivo, L2.1 può accettare richieste"
  → log in wiki/log.md: "WF-BRAND-KIT-BUILD completato per {brand_kit_id}"
```

---

## Input del workflow

```json
{
  "tipo_richiesta": "nuovo_cliente | nuovo_canale_de | aggiornamento",
  "brand_kit_id": "nuovo-id-da-assegnare | id-esistente",
  "committente": "01-AGENCY | 04-MKT (DE) | 02-INFO | 05-MB",
  "brief_iniziale": {
    "nome_brand": "...",
    "settore": "...",
    "icp_brief": "chi sono i clienti ideali del brand",
    "obiettivo_principale": "...",
    "competitor_noti": [],
    "vincoli_brand": ["es.: no umorismo, colori già definiti: #XXXXX"],
    "canali_attivi": ["email", "ads", "social", "blog"]
  },
  "deadline": "YYYY-MM-DD",
  "materiali_aggiuntivi": []
}
```

---

## Output del workflow

```
marketing/brand/kits/{brand_kit_id}/
  ├── voice_guide.md      → tono, registro, proibizioni, esempi, pattern retorici
  ├── visual_brief.md     → palette, font, mood, reference, regole per piattaforma
  ├── icp.md              → profilo ICP dettagliato (pain, obiettivi, linguaggio, fear)
  ├── tone_chart.md       → matrice tono × canale
  └── _metadata.json      → brand_kit_id, version, data_creazione, data_review, owner
```

---

## Gate di uscita

| Gate | Chi | Criteri |
|---|---|---|
| G5 — Brand consistency (interna) | BR-QA | Kit internamente coerente; non contraddice Mandato Art.2; ICP specifico; regole operative non astratte |
| Firma BRAND-LEAD | BRAND-LEAD | Revisione integrata superata; 4 artefatti presenti e completi |
| Notifica a L2.1 | BRAND-LEAD | Solo dopo firma: L2.1 può accettare richieste con questo brand_kit_id |

---

## Esempio operativo

**Trigger:** 01-AGENCY onboarda un nuovo cliente — studio di consulenza strategica B2B.

**Brief:** clienti = CEO PMI industriali 50-200 dipendenti, pain = "non hanno tempo per
fare strategia — la operazione li divora", differenziatore = "lavoriamo per 90 giorni poi
vi lasciamo autonomi". Competitor: consulenti tradizionali McKinsey-like (troppo costosi,
troppo lenti, troppe slide).

**Output WF-BRAND-KIT-BUILD:**
- `voice_guide.md`: tono da "advisor senior che parla da pari a pari con il CEO, non da
  esperto che spiega". Parole vietate: "synergy", "pivot", "roadmap" senza piano concreto.
  Pattern: inizia sempre con un numero o un dato, poi il problema.
- `icp.md`: CEO PMI industriale, 15+ anni di esperienza, stanco di consulenti che consegnano
  deck senza implementazione. Frase ricorrente: "i consulenti ci danno PowerPoint, io ho
  bisogno di qualcuno che metta le mani in pasta".
- `visual_brief.md`: palette industrial (antracite + giallo accento), tipografia serif per
  autorevolezza, no stock photo con strette di mano — foto di lavoro reale in fabbrica.
- `tone_chart.md`: email = formale ma diretto; LinkedIn = autorevole con dati e casi;
  ads = concreto con numero nell'headline.

---

## Connessioni

- [[brand-lead]] · `agenti/brand-lead.md`
- [[br4-brand-analyst]] · `agenti/br4-brand-analyst.md`
- [[WF-BRAND-AUDIT]] · `workflow/WF-BRAND-AUDIT.md`
- [[WF-BRAND-EVOLUTION]] · `workflow/WF-BRAND-EVOLUTION.md`
- [[state-readme]] · `state/README.md` (catalogo brand_kit attivi)
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 + Art.6.1)
