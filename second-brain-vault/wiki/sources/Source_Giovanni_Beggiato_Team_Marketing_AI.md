---
Type: SOURCE
Status: Active
Tags: #marketing #agenti-ai #team-multi-agente #claude-code #market-audit #competitor-research #verifica-dal-vivo #browser-mcp #agency-cro #gentes-ai #giovanni-beggiato #max17
Created: 2026-09-02
Last updated: 2026-09-02
---

# Source: Giovanni Beggiato (Gentes AI) — Ho creato un intero team di marketing AI con Claude Code in 20 minuti

## Overview
Walkthrough di 19m54 in cui l'autore costruisce e lancia un **team di 6 agenti Claude Code specialisti + 1 orchestratore** (Stratega, Analista Concorrenza, Specialista SEO, Copywriter, Esperto Conversioni, Media Buyer) che, da un singolo URL e un solo prompt in linguaggio naturale ("attiva il mio marketing team su questo URL"), produce un audit marketing completo per una PMI (pagella con voti, mappa opportunità impatto/sforzo, campagne ads, funnel, piano SEO, sequenza email, calendario social, piano 90 giorni) più un PDF pronto per il cliente. Video 2 del batch `max17`.

Il contributo che vale davvero per Digital Empire non è l'architettura del team (DE ha già un equivalente diretto, più sofisticato, in `market-audit`): è **il pattern "verifica dal vivo che smentisce l'analisi statica"** — un passaggio con browser realmente renderizzato che conferma o smentisce i claim raccolti da fetch statico, dimostrato sul checkout reale di un cliente e-commerce — e **la regola "mai concorrenti inventati", con fonte citata per ogni competitor**. Entrambi confermati come gap reali in `market-audit` prima di essere patchati.

## Dati Tecnici

- **Video ID:** yJOCyyP77bA
- **Durata:** 19m54s (1194s)
- **Canale:** Giovanni Beggiato — agenzia AI "Gentes AI" (`gentes.ai`), community "Avanguardia Plus" su Skool · **Lingua:** IT
- **Formato:** Talking head + slide Excalidraw + screen share IDE (Antigravity) + scroll di deliverable HTML/PDF
- **Frame:** 597 densi @2s → 165 unici sopra soglia | **Frame letti: 165/165 — coverage 100%** | NO-FINTO: PASS
- **Transcript:** 994 righe rolling-caption → 3.154 parole uniche dopo merge, timestamp conservati
- **KA:** 77 (21 alta rilevanza DE, 51 media, 5 bassa) | 76 osservati, 1 inferito
- **Processing:** pipeline Empire Studio (sessioni precedenti) · Memory Empire C-H 2026-09-02
- **Run:** `empire-studio/runs/max17-v02-beggiato-team`

## Il Sistema

```
6 SPECIALISTI IN PARALLELO + 1 ORCHESTRATORE

01 STRATEGA            -> vota Messaggio e Crescita: "prova dei 5 secondi",
                           fonti di traffico (Search/Instagram/LinkedIn/YouTube)
02 ANALISTA CONCORRENZA -> vota Concorrenza: recensioni vs concorrenti reali
                           (P.IVA -> Registro Imprese -> ATECO -> concorrenti)
03 SPECIALISTA SEO      -> vota Trovabilita: titoli pagina, posizione SERP
04 COPYWRITER           -> senza voto, dimostra: 3 testi piu deboli, prima/dopo
05 ESPERTO CONVERSIONI  -> vota Conversione: percorso cliente click-per-click
06 MEDIA BUYER          -> senza voto, verdetto: ads di oggi sono soldi buttati?

REGOLA DI SQUADRA (le 3 righe che contano davvero):
  1. Ogni voto cita il sito
  2. Mai numeri inventati
  3. Difetti provati nel browser vero
```

Architettura filesystem: `Company Brain/labs/team-marketing-AI/` con `skills/` (11 skill, una per deliverable: `marketing-ads`, `marketing-seo`, `marketing-funnel`, ecc.) e una cartella `squadra/` con i file `.md` degli agenti veri (frontmatter `name/description/tools` + corpo istruzioni). Pattern dichiarato a voce: *"ho creato un sacco di skill e poi ho fatto qui una mini squadra."*

## Il Pattern Riusabile — Verifica dal Vivo

```
CLAIM DAL FETCH STATICO           VERIFICA NEL BROWSER RENDERIZZATO (Chrome via MCP)
──────────────────────            ─────────────────────────────────────────────────
"hreflang assenti"          -->   SMENTITO: it/en/x-default presenti nel DOM
"categorie non tradotte"    -->   SMENTITO: tradotte via JS, invisibili al fetch
"spedizioni solo Italia"    -->   SMENTITO: "SHIPMENTS IN ITALY AND EU" nel checkout
zero widget recensioni      -->   CONFERMATO dal vivo (home/collezione/2 schede)
telefono non cliccabile     -->   CONFERMATO dal vivo
```

Il test reale eseguito: click, aggiunta al carrello, checkout raggiunto e abbandonato prima del pagamento. Risultato: il voto Conversione è stato **ricalcolato dentro lo stesso deliverable, da 6.0 a 6.5**, dopo che la verifica dal vivo ha scoperto ritiro in negozio, checkout ospite con express pay, "richiedi la taglia" — elementi che il fetch statico non vedeva.

## Regola Riusabile — Mai Concorrenti Inventati

```
URL cliente -> scraping P.IVA -> Registro Imprese -> codice ATECO
            -> concorrenti REALI nella stessa nicchia/città (mai inventati)
            -> confronto recensioni (numero E contenuto, non solo stelle)
```

Applicata al caso reale: 6 concorrenti trovati con fonte citata (Google Places + ricerca web), incluso un concorrente (Musto Calzature) sconosciuto persino all'autore del video — *"onestamente non ho idea di chi siano, ma a quanto pare va meglio di noi su quasi tutto"*, prova che il sistema non stava semplicemente confermando ciò che l'operatore già sapeva.

## L'Output — deliverable doppio

- **HTML aggregato** (`TUTTI-I-DELIVERABLE.html`, uso interno): 8 tab — Pagella, Mappa Opportunità, Campagne Ads, Funnel, Piano SEO, Sequenza Email, Calendario Social, Piano 90 giorni.
- **PDF cliente** (`REPORT-CLIENTE.pdf`): cover con voto (5.6/10), radar chart 5 assi vs il concorrente principale, confronto testa a testa 4 concorrenti, matrice priorità 2x2, pagina "Il primo passo" (una sola azione da fare per prima).

Deliverable clonabile per gli audit cliente dell'agenzia CRO DE: è sostanzialmente lo stesso tipo di output già prodotto da `market-report-pdf`.

## Key Quotes

> "Basta incollare il sito di una piccola impresa e in un paio di minuti sei agenti restituiscono un'analisi completa."

> "Mai concorrenti inventati." [regola dichiarata nella slide "La scala dei dati veri"]

> "Ogni voto cita il sito, mai numeri inventati, difetti provati nel browser vero." [regola di squadra, banner "OGNI VOTO HA DIETRO UNO SPECIALISTA"]

> "Vediamo che abbiamo circa 41.000 follower. Perfetto, 45, quindi ha fatto una buona approssimazione... tutti i dati, come vedete, sono effettivi." [verifica dal vivo di Instagram/Facebook fatta dall'autore stesso]

> "Onestamente non ho idea di chi siano, ma a quanto pare va meglio di noi su quasi tutto." [sul concorrente Musto Calzature, trovato dal sistema e sconosciuto all'autore]

> "Il nostro obiettivo non è mai fare one shot, ma è avvicinarci quanto più possibile ad un output di qualità."

## Numeri Dichiarati

- Durata totale del processo (dal link al piano completo): **20 minuti**
- Voto finale Marco Calzature: **5.6/10** (Messaggio 6.0, Trovabilità 5.0, Conversione 6.5, Concorrenza **3.5 — rosso**, Crescita 7.0)
- 6 concorrenti reali con fonte citata (Turci 4.9/1176 recensioni, Velasca 4.8/542, Musto 4.8/406, GHIGO 4.4/476, Walter 4.6/299, Pepperina 4.8/187)
- Volumi di ricerca mensili non intercettati: sneakers donna 90.500, ballerine donna 60.500, sandali donna 40.500
- Budget ads raccomandato: 1.200 €/mese (40 €/giorno)
- Community Skool "Avanguardia Plus": 91 membri al momento della registrazione

## Azione Concreta (Enrichment)

**2 artefatti reali valutati (`market-audit`, `market-competitors`) + 1 dichiarato assente (`market-competitive` come file standalone — non esiste, verificato con `find` su `.claude/skills/` e `.claude/agents/`). 2 file patchati, +22 righe, 0 cancellazioni.**

- `market-audit/SKILL.md` (**+18**) — nuovo §1.1b "Live Verification Pass (Browser Reale)" subito dopo §1.1 "Fetch the Target URL" (che oggi usa solo `WebFetch`): cosa controllare nel browser reale (rendering vs statico, CTA cliccabili, checkout/contatto fino in fondo, elementi solo-JS), come registrare l'esito (liste "Verificato dal vivo" / "Smentito dal vivo"), e dichiarazione esplicita del limite attuale — nessun MCP browser configurato in `.mcp.json` di progetto (solo `claude-flow`, disconnesso in sessione).
- `market-audit/SKILL.md` (**+2**) — dentro "Subagent 3: market-competitive", regola "mai concorrenti inventati: fonte verificabile obbligatoria per ogni competitor citato".
- `market-competitors/SKILL.md` (**+2**) — stessa regola, applicata a `COMPETITOR-REPORT.md`.

**NON costruito, dichiarato:** skill nuova `live-verification` (proposta reale del video-analysis.md) e agente nuovo `competitor-kyc` — entrambe registrate in backlog (**B-034**, **B-035**) per approvazione di Max, non costruite di iniziativa.

Dettaglio in `memory-empire/knowledge/yJOCyyP77bA/enrichment-report.md`.

## Nota di trasparenza — limiti della fonte

Il video mostra **un solo run pulito**, mai un secondo tentativo o una correzione manuale in diretta, pur dichiarando a parole che il processo normale prevede iterazioni ("non è mai one-shot"). L'orchestratore stesso non viene mai mostrato (nessuna configurazione di come i 6 agenti vengono lanciati in parallelo), né i nomi dei provider API per volumi di ricerca/registro imprese/Google Places (rimandati alla community a pagamento). Solo 1 file agente su 6 viene aperto (`copywriter-pmi.md`), e solo parzialmente — la sezione "Come riscrivi" è tagliata fuori dal frame successivo. Il registro imprese non è stato interrogato per questa run specifica (KYC dichiarato "in corso" nel deliverable), quindi la catena completa P.IVA→ATECO→concorrenti promessa a parole si appoggia in questo caso solo su Google Places + ricerca web.

## Backlog aperto (registrato, non applicato)

- **B-034** — skill nuova `live-verification`: prende una lista di claim CRO e restituisce "Verificato dal vivo / Smentito dal vivo", riusabile da `market-audit`, `cro-ricerca`, `market-competitors`.
- **B-035** — valutare un MCP browser (Playwright) a livello progetto: oggi `.mcp.json` non ne ha, e questo limita ogni audit alla lettura statica.

## Connessioni

- [[Source_Nico_AI_Ranking_Claude_Keyword_Research]] — stesso batch `max17`, stesso pattern di sessione (Memory Empire chiuso a valle di una pipeline Empire Studio già fatta): là il gap era sulle fonti di keyword research, qui sulla verifica browser reale — entrambi patchano skill `market-*` esistenti invece di inventarne di nuove.
- [[Concept_Meta_Ads_Library_Competitor_Research]] — stesso principio di fondo applicato a un'altra fonte: estrarre intelligence competitiva da dati pubblici verificabili invece che da stime. Qui la fonte è Google Places + registro imprese, lì è Meta Ads Library.
- [[Source_Andrei_Pascu_Ads_Library_Live|Andrei Pascu — Ads Library Live ITA]] — stesso genere di walkthrough (screen-share di un tool di ricerca competitor), stesso principio "mai numeri inventati" applicato però a un tool diverso.
- [[Tool_Memory_Wiki_Bridge|memory-wiki-bridge + /sync-wiki-totale]] — il ponte per cui questa ingestione esiste come pagina wiki invece di restare solo in `memory-empire/knowledge/`.
- [[Reparto_Produzione_Digital_Empire|🏭 Reparto Produzione Digital Empire]] — stesso principio organizzativo "stesso motore riusato dove possibile": qui applicato a `market-audit`, che riceve un potenziamento invece di una skill parallela duplicata.
