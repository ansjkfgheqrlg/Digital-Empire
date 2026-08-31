# Lezione 3 — Livelli di utilizzo dell'intelligenza artificiale

**Corso:** Claude Speedrun 2 | **Sezione:** AI – Le basi (3/9)
**URL:** https://www.andrei-copy.com/cs2online/lezione-3-livelli-di-utilizzo-dellintelligenza-artificiale-srtyp
**Video:** Vimeo `1172370851`
**Tipo:** TEORIA — framework di autovalutazione, no dimostrazione UI.
**Fonte:** blocco ufficiale "Cosa hai imparato" (16 bullet). Nessuna trascrizione .md.

---

## Framework "10 livelli di utilizzo AI" (fonte primaria, integrale)

| Livello | Descrizione |
|---|---|
| 0 | Sapere che l'AI esiste, senza usarla davvero. |
| 1 | Usarla come Google — solo ricerca veloce, non le si fa fare lavoro. |
| 2 | Giocherellarci (scheda palestra, traduzioni, provare tool nuovi tipo Sora) — nessun workflow reale. |
| 3 | Usarla per lavoro reale (caption, email, post, risposte clienti) ma output generico che "sa di AI" e non porta risultati. **Il 90% delle persone è bloccato qui (livelli 1-3)** — effetto Dunning-Kruger: si sentono bravi ma non hanno risultati reali. |
| 4 | **Il salto critico.** Costruire contesto (info giuste, tante, ben strutturate — non PDF a caso) → output che performa davvero, meglio o più veloce del fare a mano. |
| 5 | Sistemi e automazioni che lavorano senza intervento manuale ogni volta (non aprire ChatGPT/Claude ogni volta) — es: cliente manda brief via email → Zapier → Claude crea bozza → arriva in email, pronta al risveglio. |
| 6 | Creare applicazioni, usare API, integrare l'AI nei propri servizi (es. tool sul sito che analizza un profilo via API OpenAI/Anthropic). |
| 7 | Fine-tuning modelli su dati propri + RAG — migliaia di € /mese in token API. |
| 8-9-10 | Budget milioni/miliardi, team ingegneri, data center, LLM proprietari — big tech/governi, fuori scope corso. |

**Obiettivo dichiarato del corso**: portare lo studente dal livello 0-3 al 4-5, iniziando a lavorare verso il 6.

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Framework 10 livelli (0-10) di utilizzo AI — vedi tabella sopra, riproducibile come strumento di autovalutazione. | "Cosa hai imparato" |
| KA-02 | Effetto Dunning-Kruger applicato all'AI: il 90% è bloccato ai livelli 1-3, si percepisce competente ma non ha risultati misurabili (non più vendite, non più views). | "Cosa hai imparato" |
| KA-03 | Il "muro" tra livello 3 e 4 è concettuale, non tecnico: l'AI non è un "bottone magico", il salto richiede costruzione deliberata di contesto (coerente con KA-09 lezione 2, Context Engineering). | "Cosa hai imparato" |
| KA-04 | Criterio esplicito per decidere quando NON usare l'AI: se per un task piccolo (es. 20 parole) l'AI fa peggio di te farlo a mano, fallo a mano — "il punto non è usare l'AI per usare l'AI". | "Cosa hai imparato" |
| KA-05 | 2 motivi legittimi per usare l'AI: (1) risparmiare tempo significativo, (2) fare cose che altrimenti non sapresti fare (es. scrivere codice senza saper programmare). | "Cosa hai imparato" |
| KA-06 | Esempio concreto di automazione livello 5: cliente manda brief via email → Zapier passa a Claude → Claude produce bozza strategica → invio email automatico → lavoro pronto al risveglio, zero intervento manuale nel mezzo. | "Cosa hai imparato" |

## Pattern

- **P1 — Framework di posizionamento come strumento di vendita/onboarding**: la scala 0-10 non è solo didattica, è anche un meccanismo di auto-diagnosi che crea urgenza ("sei bloccato al 3, il corso ti porta al 5") — pattern di funnel/positioning riutilizzabile.

## Connessione con Knowledge Base esistente

- KA-03 conferma esplicitamente KA-09 della lezione 2 (Context Engineering) — seconda conferma indipendente dello stesso principio all'interno del corso. Non ancora una terza fonte esterna (regola anti-overfitting DE), ma pattern che si consolida.
- KA-01 (framework 10 livelli) è potenzialmente riutilizzabile come tool di diagnosi/onboarding per clienti agency DE (assessment "a che livello AI sei") — nessuna skill DE lo copre oggi. **PROPOSTA aperta**, non applicata (serve valutazione strategica, non enrichment meccanico).

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — fonte ufficiale piattaforma |
| NO-STUB | PASS — framework completo 0-10 riportato integralmente |
| P12 traceability | PASS |

**Prossima lezione:** Lezione 4 — "3 tipi di lavoro"
