---
Type: SOURCE
Status: Active
Tags: #claude-code #codex #cross-model-review #security-audit #adversarial-review #adr-006 #sentinel #martes-ai #riccardo-belli #max17
Created: 2026-09-02
Last updated: 2026-09-02
---

# Source: Riccardo Belli Contarini (Martes AI) — Claude Code + Codex: Il Setup di cui NESSUNO Parla

## VERDETTO — leggere questo prima di tutto

**Il setup completo mostrato in questo video NON serve a Digital Empire.** Il principio cardine —
"chi costruisce non è chi giudica" — è già codificato in `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`
(ADR-006, step 5 REVIEW indipendente) e già implementato con i sentinel esistenti
(`sentinel-security`, `sentinel-quality`, `sentinel-drift`, `review-and-heal`, `security.agent`).
Non installare il plugin Codex, non configurare un secondo abbonamento OpenAI/ChatGPT per
l'organizzazione: sarebbe duplicare un ciclo che DE ha già.

**L'unico pezzo reale che vale la pena portare a casa da questo video**: tutti quei giudici DE
girano oggi su **modelli della stessa famiglia** di chi scrive il codice (Claude che rilegge
Claude, solo con tier diversi). Il video dimostra empiricamente, **3 casi su 3**, che un giudice
di famiglia diversa (GPT/OpenAI via Codex) trova falle di gravità alta su codice/piani già
dichiarati pronti dal primo giudice. Non è un giudizio su quale modello sia migliore — è che un
giudice della stessa famiglia condivide i punti ciechi dell'autore. Questo principio è ora una
**proposta di ADR** (non attiva, da approvare da Max):
[[../../../company/Memory/decisions/ADR-PROPOSTA-cross-model-review.md|ADR-PROPOSTA — Audit cross-model in fase GATE]].

Chi legge questa pagina fra sei mesi: **non serve rifare l'analisi del video**. Il contenuto
integrale (setup, comandi, i 3 casi con tutti i finding) è archiviato per intero in
`memory-empire/knowledge/T7PPX5M6Puo/contenuto-integrale.md`. L'unica azione aperta è la decisione
di Max sulla proposta di ADR.

## Overview
Walkthrough di 30m52s in cui l'autore mostra il plugin ufficiale OpenAI **"Codex Plugin"**
installato dentro Claude Code — 5 comandi (`/codex:review`, `/codex:adversarial-review`,
`/codex:rescue`, `/codex:transfer`, `/codex:status`/`result`) che permettono di far revisionare (o
correggere) il lavoro di Claude Code da Codex, un modello di famiglia diversa. Dimostra il metodo
su **3 casi reali** della sua agenzia (Martes AI): un clone di ManyChat che gestisce account
Instagram di clienti, un form di candidature con dati personali, e un piano di sviluppo (clone
Bitly) contestato prima ancora di scrivere codice. In tutti e tre i casi, Claude Code aveva già
dato il via libera (o scritto il piano) senza vedere il problema che Codex ha trovato. Video 6 del
batch `max17`.

## Dati Tecnici

- **Video ID:** T7PPX5M6Puo
- **Durata:** 30m52s (1852s)
- **Canale:** Riccardo Belli Contarini — fondatore/CEO **Martes AI** (agenzia AI, 65+ aziende clienti, 75+ soluzioni AI in produzione, ago 2026) · **Lingua:** IT
- **Formato:** Talking head + lavagna scritta a mano + screen share VS Code/terminale
- **Frame:** 926 densi @2s → 197 unici sopra soglia | **Frame letti: 197/197 — coverage 100%** | NO-FINTO: PASS
- **KA:** 70 (31 alta rilevanza DE, 27 media, 12 bassa) | 69 osservati, 1 inferito
- **Run:** `empire-studio/runs/max17-v06-belli-codex`
- **Archivio integrale:** `memory-empire/knowledge/T7PPX5M6Puo/`

## Il Principio Cardine (a lavagna, testo esatto)

```
CHI COSTRUISCE ≠ CHI GIUDICA
```

Il piano lo scrive Claude, Codex lo contesta (adversarial review), Claude produce piano v2, il
ciclo si ripete finché Codex non ha più obiezioni — sempre con revisione umana nel mezzo: *"non
vogliamo essere pipecoder seriali... altrimenti quello che abbiamo costruito diventa un mostro
incontrollabile."*

## I 5 comandi (plugin `openai/codex-plugin-cc`)

| Comando | Cosa fa | Flag |
|---|---|---|
| `/codex:review` | Legge solo le modifiche non committate su Git, non indirizzabile | — |
| `/codex:adversarial-review` | Come review, ma puntabile su un target (codice o piano) | `--background` |
| `/codex:rescue` | Indaga/corregge un'app o un bug, anche già committata | `--background/--wait/--resume/--fresh/--model/--effort` |
| `/codex:transfer` | Porta la conversazione Claude Code dentro Codex, continuando da dove si era | — |
| `/codex:status` / `/codex:result` | Stato dei job in background / report completo a fine job | richiede ID task |

Due pattern d'uso: **Pattern 1** — app pronta → `/codex:review` (o `/codex:rescue` se già
committata) → umano revisiona → Claude sistema → online. **Pattern 2** — piano scritto con Claude
→ `/codex:adversarial-review` sul piano → critiche tornano a Claude → piano v2 → ciclo fino a
convergenza → solo allora si scrive codice.

## I 3 Casi Reali — la prova dell'argomento

| Caso | Cosa aveva già dichiarato Claude | Cosa ha trovato Codex |
|---|---|---|
| **MaReply** (clone ManyChat, gestisce account Instagram clienti) | "pronta per essere mandata in produzione" | **2 falle Alte**: auth email/password senza verifica email (account dirottabile via invito); DM duplicati per assenza di claim atomico (spam, doppio consumo budget Meta, rischio phishing) |
| **Form candidature** (Cloudflare + Airtable, dati personali candidati) | nessun audit di sicurezza fatto prima | **4 findings Alti** (endpoint pubblico senza rate limiting/CAPTCHA, upload completamente fidato lato server, nessun limite dimensione campi, librerie terze senza SRI/CSP) + 10 medi + 1 info |
| **Piano clone Bitly** (Cloudflare Workers + D1, prima ancora di scrivere codice) | piano scritto e presentato come pronto per lo sviluppo | **1 critical** (API stats/delete senza verifica ownership — chiunque cancella link altrui) + 2 high (301 cachato rompe il tracciamento post-cancellazione; contatore gonfiato da eventi duplicati). Claude, ri-interrogato, conferma **4 obiezioni su 5 fondate** |

Sul caso Bitly, Claude riconosce anche di aver ripetuto un errore storico noto: aveva proposto un
redirect **301** (permanente, cachato indefinitamente), lo stesso errore che **Bitly stesso aveva
corretto passando a 302 nel 2016**.

Tutti e tre i casi trascritti per intero, con i testi esatti dei prompt e dei finding, in
`memory-empire/knowledge/T7PPX5M6Puo/contenuto-integrale.md` Parte 3.

## Confronto con Digital Empire

DE ha già l'equivalente architetturale del "giudice diverso da chi costruisce": ADR-006 (ciclo a 9
passi, step 5 REVIEW indipendente) più i sentinel dedicati. La differenza reale, non cosmetica: nel
video il giudice è un **provider diverso** (OpenAI vs Anthropic); in DE oggi tutti i giudici sono
Claude, solo con tier diversi (Haiku per i sentinel leggeri, Sonnet/Opus per i reviewer profondi).
Questo lascia aperto esattamente il tipo di blind spot che il video dimostra 3 volte su 3: un
modello che rilegge codice scritto dalla propria stessa famiglia tende a condividerne i punti
ciechi.

## Key Quotes

> "La domanda 'meglio Claude Code o Codex?' è sbagliata. La domanda giusta è come ottenere il massimo da entrambi."

> "CHI COSTRUISCE ≠ CHI GIUDICA" [lavagna, principio cardine del video]

> "Considerate che Claude Code mi aveva detto che questa applicazione era pronta per essere mandata in produzione... meno male che ho chiamato Codex." [sul caso MaReply, dopo aver trovato 2 falle Alte]

> "4 obiezioni su 5 hanno un nucleo valido." [Claude, ri-interrogato sulle obiezioni Codex al piano Bitly]

> "Venti dollari in più. Non il doppio. Perché qui Codex legge e critica, e scrive quasi mai. L'auditor costa molto meno che generare." [lavagna finale sui costi]

## Costi (dati dichiarati nel video)

- $200/mese solo Claude ("nessuno che lo controlla") o solo Codex ("nessuno che serve bene")
- Combo consigliata: Claude Max $100 + Codex/ChatGPT Plus $20 = **$120/mese**
- Alternativa gratis per testare: piano ChatGPT Free (Codex incluso, limiti stretti)
- Requisito minimo Claude per la combo: piano Pro $20/mese

## Nota di trasparenza — limiti della fonte

Fonte singola: un solo video, tre casi aneddotici di una sola agenzia (Martes AI). Nessun
benchmark quantitativo aggregato, nessun tasso di falsi positivi su un campione più ampio.
`/codex:review` non viene mai eseguito dal vivo (solo `rescue` e `adversarial-review`). Nessuna
gestione del disaccordo oltre il caso Bitly (4/5 obiezioni accettate) — non si vede cosa succede
se i due modelli restano in disaccordo per più cicli. Solo ambiente Mac + VS Code dimostrato. La
proposta di ADR nata da questa fonte dichiara questi limiti esplicitamente e non presenta la prova
come conclusiva oltre il perimetro dei tre casi mostrati.

## Azione Concreta

**Nessuna installazione, nessuna configurazione, nessun agente costruito** — per volontà esplicita
del verdetto già emesso: il setup completo non serve a DE. Unico artefatto prodotto:
**proposta di ADR** (non attiva, da approvare da Max):
`company/Memory/decisions/ADR-PROPOSTA-cross-model-review.md` — un secondo audit con modello di
famiglia diversa, **solo** in fase GATE e **solo** per deliverable ad alto rischio dati/credenziali
(candidati: Preventa Outreach, Formazione Empire, PreventivoForge).

## Backlog aperto (registrato, non applicato)

- **B-042** — Punto cieco strutturale: giudici e autori della stessa famiglia di modello. Vedi
  `company/Memory/BACKLOG.md`. Da approvare da Max.

## Connessioni

- [[../../../company/Memory/decisions/ADR-PROPOSTA-cross-model-review|ADR-PROPOSTA — Audit cross-model in fase GATE]] — la proposta nata da questa fonte
- [[Concept_Decisioni_Architetturali_ADR|Decisioni Architetturali (ADR) — Indice]] — hub delle 12+ ADR di DE, incluso ADR-006 (ciclo 9 passi) che questa proposta vorrebbe estendere
- [[Tool_Conoscenza_Empire_Agente|CONOSCENZA-EMPIRE — agente]] — biblioteca vivente dell'Impero, distribuisce questa fonte a chi la richieda con la fonte esatta
- [[Source_Giovanni_Beggiato_Team_Marketing_AI|Giovanni Beggiato — Team di marketing AI con Claude Code]] — stesso batch `max17`, stesso pattern di sessione (chiusura ciclo Memory Empire su pipeline Empire Studio già fatta); là il gap era operativo (browser reale) e ha prodotto una patch, qui il gap è architetturale (diversità di modello) e produce solo una proposta di ADR
- [[Source_Paolo_Trivellato_LinkedIn_Agency_1M|Paolo Trivellato — $1.2M ARR usando solo LinkedIn]] — stesso batch `max17`, stesso principio di fondo "l'umano/il sistema filtra, non applica alla cieca" applicato a un dominio diverso (LinkedIn outreach)
