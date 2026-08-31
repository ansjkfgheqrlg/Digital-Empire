# Lezione 2 — Termini che devi sapere

**Corso:** Claude Speedrun 2 | **Sezione:** AI – Le basi (2/9)
**URL:** https://www.andrei-copy.com/cs2online/lezione-2-termini-che-devi-sapere-s527b
**Video:** Vimeo `1172381465`
**Tipo:** TEORIA (glossario/definizioni) — frame-by-frame non applicato.
**Fonte contenuto:** blocco ufficiale "Cosa hai imparato" (26 bullet) + Glossario ufficiale CSV/PDF (52 termini) — nessuna trascrizione .md disponibile per questa lezione (confermata la variabilità già segnalata da Max).

---

## Panoramica ufficiale

Vocabolario essenziale per lavorare con l'AI: system prompt, artifacts, projects, memory, web search, chain of thought/reasoning, temperatura, API/API key, vibe coding, agent, automazioni (Zapier).

## Knowledge Atoms — selezione operativa (fonte: "Cosa hai imparato" ufficiale + Glossario CSV)

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | System prompt = istruzione nascosta data dal provider (non modificabile dall'utente), fondamento su cui si costruiscono i prompt personalizzati. | "Cosa hai imparato" + Glossario |
| KA-02 | Artifact (Claude) / Canvas (ChatGPT, Gemini) = documento condiviso stile Google Docs collaborativo; si attiva chiedendo esplicitamente "lavora dentro un artifact". | "Cosa hai imparato" |
| KA-03 | Project (Claude) = equivalente Custom GPTs (ChatGPT)/Gems (Gemini): cartella che raggruppa chat per progetto/cliente, con nome, istruzioni fisse e file caricati (ricerche, trascrizioni, richieste cliente) — ogni nuova chat nel project eredita il contesto senza doverlo riscrivere. | "Cosa hai imparato" |
| KA-04 | Chain of thought/reasoning = l'AI mostra il ragionamento prima della risposta finale; risposte con reasoning attivo sono "significativamente migliori". Extended thinking (Claude Opus 4.6) = modalità per farlo ragionare più a lungo. | "Cosa hai imparato" |
| KA-05 | API = collega due servizi (es. Google Sheets → Yahoo Mail); API key = credenziale segreta, mai condivisa, reperibile su piattaforme developer (non nella chat consumer). | "Cosa hai imparato" |
| KA-06 | Vibe coding = scrivere codice in linguaggio naturale lasciando che l'AI lo produca. Esempio citato: calendario HTML collegato a Google Sheets via API con un singolo prompt. Applicazione dichiarata: la sales page del corso stesso ha copy scritto a mano ma development fatto da AI. | "Cosa hai imparato" |
| KA-07 | Agent = AI che esegue azioni autonome (non solo conversazione); Automazione = workflow che esegue step da solo (es. reminder email schedulata); Zapier citato come tool no-code per queste automazioni. | "Cosa hai imparato" |
| KA-08 | Hallucination = l'AI presenta un'informazione inventata come vera, con sicurezza — rischio esplicitamente segnalato come "pericoloso perché a volte non è ovvio che sta mentendo". | Glossario CSV |
| KA-09 | Context Engineering (definizione glossario, coerente con lezione 8 del corso) = "l'arte di organizzare e dare le informazioni giuste all'AI nel modo giusto ... non basta mandare PDF a raffica: serve struttura". | Glossario CSV |
| KA-10 | Persona (prompting) = istruire l'AI a comportarsi come un professionista specifico (es. "sei un copywriter senior con 10 anni di esperienza") — "cambia radicalmente la qualità della risposta". | Glossario CSV |
| KA-11 | Few-shot vs zero-shot prompting: dare esempi concreti nel prompt (few-shot) migliora l'output rispetto a chiedere senza esempi (zero-shot, funziona solo per task semplici). | Glossario CSV |

## Glossario completo (52 termini) — allegato integrale

Vedi `resources/glossario.csv` (fonte primaria, non riassunta) — copiato integralmente anche in `memory-empire/knowledge/cs2online-lezione-02/contenuto-integrale.md`.

## Risorse allegate

- Glossario PDF (3 pagine) + CSV (52 righe Termine/Definizione) — `resources/glossario.pdf`, `resources/glossario.csv`
- Immagine schema — `resources/schema-1.png`
- 3 Workflow citati (non ancora scaricati come documenti separati — solo titolo nella pagina, verificare se hanno risorsa scaricabile propria in revisione futura)

## Gate di qualità

| Check | Status | Note |
|---|---|---|
| NO-FINTO | PASS | Fonte = blocco ufficiale piattaforma + CSV glossario ufficiale, non trascrizione audio inferita |
| NO-STUB | PASS | Glossario copiato per intero (52/52 termini), non troncato |
| P12 traceability | PASS | Ogni atom riferisce sezione/fonte ufficiale |

**Prossima lezione:** Lezione 3 — "Livelli di utilizzo dell'intelligenza artificiale"
