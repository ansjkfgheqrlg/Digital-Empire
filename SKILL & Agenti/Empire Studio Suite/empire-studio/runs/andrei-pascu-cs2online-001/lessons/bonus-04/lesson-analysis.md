# Bonus 4 — Claude Skills

**Corso:** Claude Speedrun 2 | **Sezione:** Lezioni BONUS (4/6)
**URL:** https://www.andrei-copy.com/cs2online/bonus-4--aeaj5
**Video:** Vimeo `1178102786`, durata 20:06 (1206s)
**Tipo:** **PRATICA** — confermata con 23 frame (14 scan 90s + 9 dense).
**Fonte:** panoramica + "Cosa hai imparato" ufficiali (18 bullet), nessuna trascrizione .md.

---

## Mappa timeline (confermata)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–4:30 | Talking head — problema del metodo tradizionale (riallegare sempre gli stessi file) | — |
| 4:30 | **Whiteboard**: analogia "ragazzino con la bancarella" — smiley + lista libri | `frame-t4m30s...jpg` |
| 7:30 | **Motion graphic**: libri colorati con "copertine" (front matter) disposti ad arco | `frame-t7m30s...jpg` |
| 9:00–13:30 | Talking head — struttura tecnica front matter YAML | — |
| 13:30 | **Demo (Excalidraw)**: scrittura "SKILL.md" — introduzione struttura file | `frame-t13m30s...jpg` |
| 14:30 | **Demo (MarkEdit)**: dialog salvataggio file, cartella reale "Skill Test" con esempio preesistente "skill-onboarding-cliente" + relativo .zip | `frame-t14m30s...jpg` |
| 17:00 | **Demo**: file "Struttura.md" (references file di esempio) — contenuto: "La struttura è divisa in tre parti: 1. Scrivere il topic 2. Fare hashtag 3. Fare una CTA" | `frame-t17m00s...jpg` |
| 18:00 | **Demo**: pagina Claude Settings → Skills, lista skill esistenti (**skill-creator** di Anthropic incluso come esempio ufficiale, + "algorithmic-art") | `frame-t18m00s...jpg` |
| 19:00 | **Demo — requisiti ufficiali**: dialog "Upload skill" con testo esatto: *".md file must contain skill name and description formatted in YAML" / ".zip or .skill file must include a SKILL.md file"* | `frame-t19m00s...jpg` |
| 19:30–20:06 | Talking head, chiusura | — |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Problema risolto dalle Skills: il metodo tradizionale (riallegare sempre gli stessi file/prompt) spreca context window, token e soldi; troppi documenti allegati rischiano di far "skippare" a Claude informazioni importanti per limiti di context. | "Cosa hai imparato" |
| KA-02 | Meccanismo Skills: Claude legge solo il "front matter" (nome+descrizione, la "copertina") di ogni skill disponibile, e carica il contenuto completo SOLO se la description matcha la richiesta — analogia esplicita "libri con copertina in una bancarella". | Panoramica + frame t4m30s, t7m30s |
| KA-03 | 4 livelli di risposta AI (framework didattico dell'autore): (1) risposta da memoria, (2) ricerca online, (3) documenti allegati (limitati da tempo/context), (4) skills (selezione intelligente via front matter). | "Cosa hai imparato" |
| KA-04 | Struttura tecnica: file `SKILL.md` con front matter YAML delimitato da `---` contenente `name` (trattini invece di spazi) e `description` (cosa fa + quando usarla) — la description è "la parte più importante" perché determina se Claude carica la skill. | "Cosa hai imparato" + frame t13m30s |
| KA-05 | **Requisiti ufficiali verbatim per l'upload** (osservati nel dialog reale, non nel testo del corso): ".md file must contain skill name and description formatted in YAML" — ".zip or .skill file must include a SKILL.md file". | frame-t19m00s |
| KA-06 | Struttura cartella completa: `SKILL.md` (obbligatorio) + `references/` (opzionale, file MD/TXT/PDF richiamabili per step specifici) + `assets/` (opzionale, immagini/supporto) + codici eseguibili (avanzato, non approfondito). | "Cosa hai imparato" |
| KA-07 | Procedura di caricamento: creare cartella sul Mac con SKILL.md + references → zippare la cartella → Claude → Customize → Skills → Upload Skill. | "Cosa hai imparato" + frame t14m30s |
| KA-08 | Esempio ufficiale osservato nella lista Skills di Claude: **"skill-creator"**, skill di Anthropic stessa per creare altre skill — presente come esempio nativo nell'interfaccia. | frame-t18m00s |
| KA-09 | Metodo in 2 step per implementare le Skills nel proprio lavoro: (1) identifica i processi ripetitivi dove usi l'AI, (2) per ognuno crea una skill dedicata. Esempio citato: skill per onboarding cliente con references multiple (discovery call, onboarding, overview). | "Cosa hai imparato" |

## Connessione con Knowledge Base esistente — RILEVANTE

**Questa lezione descrive esattamente il formato/processo che il nostro stesso ecosistema DE usa** (skill Digital Empire in `C:\Users\Utente\.claude\skills\`, ognuna con SKILL.md + front matter + references). KA-04/KA-05 confermano che la struttura DE è allineata alle specifiche ufficiali Anthropic osservate live nel dialog di upload — utile come validazione esterna indipendente del formato già in uso, non un gap.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 23 frame visionati, requisiti upload trascritti verbatim da screenshot reale |
| NO-STUB | PASS — video 20:06 intero mappato |
| P12 traceability | PASS |

**Prossima:** Bonus 5 — "Projects dentro co-work"
