---
Type: SCRIPTS
Status: Active
Tags: #scripts #CF-R4 #testo #validator #seo #repurposing #deterministico
Created: 2026-06-23
Last updated: 2026-06-23
---

# Scripts — CF-R4 Produzione Testuale

> Script deterministici: a parità di input, producono sempre lo stesso output.
> Nessuno script sostituisce il gate CF-R4-QA: lo affiancano per verifiche rapide.

---

## Script 1: `structure-validator`

**Scopo:** Verifica la struttura heading e i marcatori di uno script o articolo in modo
deterministico, senza invocare un agente LLM. Utile per CF-R4-WRITE come auto-verifica
rapida prima di passare il draft a CF-R4-QA.

**Input:** path del file `.md` o `.html` + formato dichiarato (`articolo | newsletter | script`)

**Output:** JSON con esito per ogni criterio strutturale

**Logica:**
- Per `articolo`: conta H1 (deve essere 1); verifica che H2 esistano (≥2); verifica che non
  ci siano salti di livello (H1→H3 senza H2 intermedio); conta parole; verifica presenza
  keyword nel H1 se keyword dichiarata nel brief.
- Per `newsletter`: verifica sezioni HTML marcate (header, corpo, footer); verifica presenza
  blocco CTA (o segnaposto `<!-- APSOC_BLOCK_PENDING -->`); verifica oggetto email nel frontmatter.
- Per `script`: verifica presenza marcatori `[HOOK]`, `[CORPO]`, `[CTA]` nell'ordine corretto;
  conta parole nel blocco `[HOOK]` (deve essere ≤25); conta parole totali.

**Esempio di output:**
```json
{
  "file": "orders/CF-2026-0101/02-copy/articolo-draft.md",
  "formato": "articolo",
  "h1_count": { "atteso": 1, "rilevato": 1, "esito": "PASS" },
  "h2_count": { "minimo": 2, "rilevato": 4, "esito": "PASS" },
  "salti_heading": { "trovati": 0, "esito": "PASS" },
  "word_count": { "rilevato": 1387, "range_brief": "1200-1600", "esito": "PASS" },
  "keyword_in_h1": { "keyword": "content marketing che converte", "trovata": true, "esito": "PASS" },
  "verdetto_finale": "PASS"
}
```

**Nota:** lo script non verifica il tono né i claim: quelli richiedono CF-R4-QA (LLM). Questo script
verifica solo la struttura (operazione puramente testuale, senza inferenza).

---

## Script 2: `seo-checker`

**Scopo:** Esegue il controllo SEO/AI-SEO su un testo in modo autonomo, restituendo
metriche di densità keyword, struttura meta, lunghezza snippet e schema type suggerito.
Usato da CF-R4-SEO per documentare il pass SEO prima della consegna a CF-R4-QA.

**Input:** path del file `.md` / `.html` + keyword target (stringa) + canale (`blog | knowledge-base | email`)

**Output:** JSON con metriche SEO e raccomandazioni non invasive

**Logica:**
- Conta le occorrenze della keyword nel testo e calcola la density su tot parole.
- Verifica presenza keyword in: H1, primo H2, primo paragrafo, meta_description (se presente
  nel frontmatter o nel commento HTML).
- Conta lunghezza meta_description (target: 150-160 caratteri).
- Verifica URL-friendly slug (se dichiarato nel brief).
- Suggerisce `schema_type` in base al formato: `Article` per blog, `HowTo` se il testo
  ha lista di passi numerati, `FAQPage` se il testo ha domande/risposte strutturate.
- Non modifica il testo: produce solo il report; CF-R4-SEO applica le modifiche.

**Esempio di output:**
```json
{
  "file": "orders/CF-2026-0101/02-copy/articolo-draft.md",
  "keyword": "content marketing che converte",
  "word_count_totale": 1387,
  "occorrenze_keyword": 4,
  "keyword_density_pct": 1.73,
  "keyword_in_h1": true,
  "keyword_in_primo_h2": true,
  "keyword_in_primo_paragrafo": false,
  "meta_description": { "testo": "Scopri perché il content marketing che converte non è questione di frequenza ma di architettura.", "lunghezza": 98, "target": "150-160", "esito": "CORTO — allungare" },
  "schema_type_suggerito": "Article",
  "slug_suggerito": "content-marketing-che-converte",
  "raccomandazioni": [
    "Aggiungere keyword nel primo paragrafo (attualmente assente)",
    "Allungare meta_description a 150-160 caratteri"
  ]
}
```

**Nota:** lo script non scrive la meta_description né modifica il testo: produce il report.
CF-R4-SEO legge il report e applica le modifiche al file.

---

## Script 3: `repurpose-splitter`

**Scopo:** Prende un pezzo madre in markdown o testo e lo suddivide nei blocchi tematici
utili per la derivazione in WF-REPURPOSING. Operazione puramente testuale e deterministica:
identifica le sezioni, estrae i punti chiave di ogni H2, calcola la lunghezza di ogni blocco.
Output usato da CF-R4-REPURP come input strutturato per la skill content-forge.

**Input:** path pezzo madre `.md` / `.html` + formati derivati richiesti (lista)

**Output:** JSON con blocchi tematici estratti + mappa formati richiesti → blocco sorgente ottimale

**Logica:**
- Estrae ogni sezione H2 come blocco indipendente con: heading, n. parole, primo paragrafo (hook candidato per derivato).
- Per ogni formato richiesto nella lista, mappa il blocco sorgente ottimale:
  - `caption-ig`: usa il blocco più breve con il punto più diretto (solitamente la chiusura o il primo H2)
  - `thread`: usa tutti i blocchi H2 come candidati per i tweet (1 tweet per H2)
  - `email-teaser`: usa il primo H2 + il corpo (esclude la chiusura CTA strutturale)
  - `slide-copy`: usa heading H2 come titoli slide + primo paragrafo come corpo slide
  - `articolo-derivato`: usa il blocco H2 più lungo come base per articolo secondario
- Stima il numero di token necessari per ogni derivazione.

**Esempio di output:**
```json
{
  "file": "orders/CF-2026-0101/02-copy/articolo-final.md",
  "blocchi_h2": [
    { "id": "h2-1", "heading": "Il contenuto informativo non converte da solo", "n_parole": 290, "hook_candidato": "Pubblicare contenuto e aspettarsi vendite è come..." },
    { "id": "h2-2", "heading": "Il problema non è la frequenza", "n_parole": 310, "hook_candidato": "Non sei lento. Stai correndo nel posto sbagliato." },
    { "id": "h2-3", "heading": "Come costruire il ponte", "n_parole": 480, "hook_candidato": "La differenza tra contenuto e conversione si chiama percorso." },
    { "id": "h2-4", "heading": "Il passo successivo", "n_parole": 150, "hook_candidato": "Smetti di produrre. Inizia a costruire." }
  ],
  "mappa_derivati": {
    "caption-ig": { "blocco_sorgente": "h2-4", "token_stimati": 80, "note": "blocco più diretto e sintetico" },
    "thread-5p": { "blocchi_sorgente": ["h2-1","h2-2","h2-3","h2-4"], "token_stimati": 320 },
    "email-teaser": { "blocchi_sorgente": ["h2-1","h2-2"], "token_stimati": 230 },
    "caption-linkedin": { "blocco_sorgente": "h2-3", "token_stimati": 160, "note": "blocco più sostanzioso per formato LinkedIn long" }
  }
}
```

---

## Connessioni

- [[cf-r4-write]] · `agenti/cf-r4-write.md` — usa structure-validator per auto-verifica
- [[cf-r4-seo]] · `agenti/cf-r4-seo.md` — usa seo-checker per documentare il pass SEO
- [[cf-r4-repurp]] · `agenti/cf-r4-repurp.md` — usa repurpose-splitter come input per content-forge
- [[WF-ARTICOLO]] · `workflow/WF-ARTICOLO.md` — contesto di uso di structure-validator e seo-checker
- [[WF-REPURPOSING]] · `workflow/WF-REPURPOSING.md` — contesto di uso di repurpose-splitter
