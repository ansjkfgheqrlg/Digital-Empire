# 🩺 CICLO v2 — SELF-AUDIT (l'ecosistema giudica sé stesso)
> Ciclo 1 di 3 · 2026-07-21 · Metodo: critica strutturale della v1 − **vincolo: vietato aggiungere agenti**. Solo fusioni, rimpasti di linea, rimozioni.
> Fonte audit: rilettura incrociata di PIANO-ECOSISTEMA-v1 + simulazione a secco dei flussi sulla board.

## 1. FINDINGS (10, ordinati per severità)

| # | Sev. | Finding (dove la v1 è malata) | Perché fa male |
|---|------|-------------------------------|----------------|
| F-01 | 🔴 | **Giudice-parte**: memory-auditor riporta a TRUTH-CMD, che è il proprietario della memoria da auditare | Chi controlla il controllore? Violazione di base della separazione |
| F-02 | 🔴 | **EMPIRE-COMMANDER = single point of failure**: muore/loopa lui, si ferma tutto | Nessuna successione, nessun heartbeat, nessun quorum |
| F-03 | 🟠 | **Dirigenti-router**: le REQUEST cross-team passano dal dirigente → diventa collo di bottiglia e punto di stallo singolo | 7 dirigenti diventano 7 semafori: latenza e fragilità |
| F-04 | 🟠 | **delivery-verifier ridondante**: dominio in sovrapposizione con funnel-verifier e outreach-verifier | 6 verificatori sono troppi: sovrapposizioni = verifiche doppie o buchi |
| F-05 | 🟠 | **devil-advocate usato da verificatore** della Strategy Cell: gli osservatori non bloccano, i verificatori sì — mescola le caste | Rompe il principio "le caste non si mischiano" |
| F-06 | 🟡 | **L'umano non è modellato**: Max riceve N messaggi N volte al giorno invece di UN digest | L'umano è il collo di bottiglia più costoso: va protetto dal rumore |
| F-07 | 🟡 | **Confusione skill vs agente**: "case-study-forge" è una skill usata come nome di agente | Mapping ambiguo, backup sbagliati |
| F-08 | 🟡 | **Nessun diritto d'appello** contro un RULE-BLOCK errato | Un falso positivo di un regolatore = gridlock senza via d'uscita |
| F-09 | 🟢 | **OBS-FEED come canale separato** è ridondante (gli osservatori postano già OBS-NOTE) | Due canali da leggere per lo stesso scopo |
| F-10 | 🟢 | **Stati delle decisioni ambigui** dopo scadenza veto (chi aggiorna a ATTIVA?) | Decisioni che restano "PROPOSTA" per sempre |

## 2. HEAL-PLAN (10 rimedi — nessuna aggiunta netta)

| # | Rimedio | Tipo |
|---|---------|------|
| R1 | Verificatori = **casta autonoma**: coordinamento logistico da TRUTH-CMD ma **veto non revocabile** da nessuno; **memory-auditor riporta a EMPIRE-COMMANDER** e audita anche TRUTH-CMD (audit-the-auditor) | rimpasto linee |
| R2 | **Catena di successione** EC → REVENUE-CMD → BUILD-CMD + heartbeat al SYNC delle 19:00 + **quorum 2/3** dei comandanti se EC AWOL >24h | struttura |
| R3 | **REQUEST peer-to-peer** tra operativi ammessa, con `cc: dirigente`; i dirigenti leggono il digest EOD, non approvano in real-time | rimozione collo |
| R4 | **delivery-verifier fuso** → 5 verificatori con domini netti: funnel-verifier (web/checkout/factory/contratti) · content-verifier (copy/carousel/case-study) · video-verifier · outreach-verifier (campagne/social) · memory-auditor | **rimozione** |
| R5 | Piani Strategy verificati da **memory-auditor** (aderenza Art.2); devil-advocate torna puro osservatore | rimpasto |
| R6 | Nuovo tipo messaggio **HUMAN-TASK** + **digest unico** per Max (1 messaggio/giorno con decisioni e task suoi, compilato dal router dalle DECISION-REQ) | capacità board |
| R7 | **Naming convention**: le skill tengono il nome del motore; gli agenti hanno ruolo (`-ops`, `-engineer`, `-architect`). case-study-forge (skill) → operata da `casestudy-ops` | pulizia |
| R8 | **Appello**: tipo messaggio OVERRIDE-REQ (comandante→Max, con evidenza). Costituzione definisce per ogni regola se è appellabile e da chi (es. swarm-quota appellabile da REVENUE-CMD per P0 con log) | struttura |
| R9 | OBS-FEED = **vista filtrata** della board (type=OBS-NOTE), non canale separato | **rimozione** |
| R10 | Il **router aggiorna le DEC scadute a ATTIVA** (default-activation), atomo memoria automatico | regola router |

## 3. Linee ridisegnate (v1 → v2)

```
v1: dirigenti = semafori cross-team   →  v2: p2p + cc, dirigenti solo in digest
v1: 6 verificatori sovrapposti        →  v2: 5 verificatori, domini disgiunti, casta autonoma
v1: memory-auditor sotto TRUTH-CMD    →  v2: sotto EMPIRE-COMMANDER, audita anche TRUTH-CMD
v1: EC orfano di successione          →  v2: chain EC→REV→BUILD + quorum 2/3 + heartbeat
v1: OBS-FEED canale separato          →  v2: vista filtrata (type=OBS-NOTE)
v1: Max bombardato                    →  v2: HUMAN-TASK + 1 digest/giorno
```

## 4. Bilancio del ciclo (prova del "non additivo")
- Agenti: −1 (delivery-verifier fuso) · Canali: −1 (OBS-FEED) · Semaphore-dirigenti: −6 passaggi/req cross-team
- Aggiunte: SOLO capacità della board (tipi HUMAN-TASK/OVERRIDE-REQ) — nessun agente nuovo. **Bilancio netto: dimagrito.**

---
⛓️ Trace P12: `CICLO-v2#ecosystem` · input: PIANO-ECOSISTEMA-v1 · output: HEAL-R1..R10 · prossimo: CICLO-v3 hardening
