# 03 — Convergenza e Decision Matrix

## 1. Metodo di scoring

Ogni iniziativa riceve 1-5 su sei criteri. Il totale è su 100.

| Criterio | Peso | 1 | 5 |
|---|---:|---|---|
| Impatto business | 25 | marginale | sblocca value/revenue loop |
| Velocità | 15 | >30 giorni | ≤2 giorni |
| Leva automazione | 20 | manuale | elimina lavoro ricorrente |
| Evidence | 15 | speculativo | richiesto/provato |
| Sicurezza/rischio | 15 | rischio alto | riduce rischio |
| Efficienza costo | 10 | costo alto/lock-in | costo basso/reversibile |

Formula:

```text
score = Σ (voto / 5 × peso)
```

Lo score ordina il valore, ma **le dipendenze governano la sequenza**. Un task da 85 può aspettare un task da 70 se quest'ultimo è prerequisito.

## 2. Matrice delle 16 iniziative

| ID | Iniziativa | I | V | A | E | S | C | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| S08 | 5 dry-run end-to-end | 5 | 4 | 5 | 5 | 5 | 5 | **97** |
| S03 | OAuth Meta | 5 | 4 | 5 | 5 | 4 | 5 | **94** |
| S05 | Buffer editoriale 7 giorni | 5 | 4 | 4 | 5 | 5 | 5 | **93** |
| S09 | Canary + post-check | 5 | 4 | 5 | 5 | 4 | 5 | **94** |
| S04 | Media staging HTTPS | 5 | 4 | 5 | 5 | 4 | 4 | **92** |
| S06 | Carousel batch wrapper | 4 | 4 | 5 | 4 | 5 | 5 | **89** |
| S01 | Rotazione credenziali + 2FA | 5 | 5 | 2 | 5 | 5 | 5 | **88** |
| S10 | Baseline 28 giorni | 5 | 2 | 4 | 5 | 5 | 4 | **85** |
| S11 | Repurposing graph | 4 | 4 | 5 | 3 | 4 | 5 | **83** |
| S02 | Ingestione 10 Reel | 5 | 3 | 3 | 5 | 4 | 4 | **81** |
| S13 | Lead magnet + UTM funnel | 5 | 3 | 4 | 3 | 4 | 4 | **79** |
| S07 | Reel template engine | 4 | 3 | 5 | 3 | 3 | 4 | **75** |
| S12 | Drift detector | 4 | 3 | 4 | 4 | 5 | 4 | **80** |
| S15 | Low-ticket offer | 4 | 3 | 3 | 2 | 4 | 4 | **67** |
| S16 | Multi-tenant productization | 5 | 1 | 5 | 2 | 3 | 2 | **67** |
| S14 | Community triage | 3 | 3 | 4 | 2 | 2 | 4 | **60** |
| — | Auto-reply AI indiscriminato | 2 | 3 | 5 | 1 | 1 | 4 | **53 — REJECT** |

## 3. Sequenza risultante per dipendenze

### Critical path

```text
S01 Security
  → S03 OAuth
  → S04 HTTPS staging
  → S05 Buffer 7 giorni
  → S08 5 dry-run
  → S09 Canary/post-check
  → Insights +48h
  → CERTIFIED_AUTO
  → S10 Baseline 28 giorni
```

### Content intelligence path in parallelo

```text
S02 10 Reel integrali
  → Pattern Extractor
  → S07 Reel Template Engine
  → Buffer Reel
  → S08/S09
```

### Business path

```text
S10 primi segnali + G07 profile sprint
  → S13 Lead magnet/UTM
  → attribution reale
  → S15 Low-ticket/team pricing
  → S16 productizzazione solo dopo prova
```

## 4. Scelta stack di pubblicazione

Pesi: controllo/sicurezza 30, affidabilità 25, velocità 20, costo 15, scalabilità 10.

| Opzione | Controllo | Affidabilità | Velocità | Costo | Scala | Totale | Decisione |
|---|---:|---:|---:|---:|---:|---:|---|
| Meta API nativa | 5 | 5 | 3 | 5 | 5 | **92** | PRIMARY |
| Aggregatore SaaS | 3 | 4 | 5 | 2 | 4 | **72** | fallback commerciale |
| Browser automation | 1 | 1 | 4 | 4 | 2 | **43** | legacy/non certificato |

**Decisione:** continuare API-first. L'aggregatore si valuta solo se un endpoint critico non è disponibile o il costo totale di manutenzione supera il servizio. Browser automation non governa il live.

## 5. Scelta media hosting

Non viene hard-coded un vendor prima di conoscere account, dominio e policy. Si sceglie una **classe architetturale**:

```text
Object storage/CDN HTTPS pubblico
+ URL stabile
+ content-type corretto
+ lifecycle/TTL
+ credential server-side
+ costo egress misurabile
```

Candidati: Cloudflare R2, S3-compatible, Cloudinary o static mirror controllato. Gate di scelta F2:

1. Meta fetch PASS su JPEG e MP4;
2. HTTPS senza auth/cookie;
3. URL non scade prima del publish;
4. lifecycle delete controllabile;
5. costo mensile dichiarato;
6. nessun segreto nel client/repo.

## 6. Scelta architettura AI

| Layer | AI permessa | Deterministico obbligatorio |
|---|---|---|
| Research | sintesi/estrazione con trace | hash, frame, timestamp, coverage |
| Strategy | ipotesi/brief | schema, pilastri, esperimento |
| Copy | generazione/variazioni | length, forbidden claims, sources |
| Visual/video | prompt/script | dimensions, codec, rights, safe area |
| QA | supporto semantico | gate bloccanti e verdict persistito |
| Publish | **nessuna decisione creativa** | token, quota, idempotenza, API |
| Learning | pattern candidate | n≥3, mediana, fonte, rollback |

**Decisione:** LLM costruisce proposte; codice deterministico autorizza side effect.

## 7. Cosa entra NOW / NEXT / LATER / REJECT

### NOW — F0→F5

- S01 sicurezza;
- S02 ingestione 10 Reel;
- S03 OAuth;
- S04 media hosting;
- S05 buffer 7 giorni;
- S06 carousel wrapper;
- S08 dry-run;
- S09 canary.

### NEXT — F6→F8

- S07 Reel engine dopo evidence;
- S10 baseline;
- S11 repurposing;
- S12 drift detector;
- S13 lead magnet/UTM.

### LATER — dopo dati/revenue

- S14 community triage;
- S15 low-ticket;
- S16 multi-tenant productization.

### REJECT / PAUSE

- auto-DM e auto-reply indiscriminati;
- browser publisher come primary;
- acquisto follower/engagement;
- clonazione competitor;
- 20 format contemporanei;
- sponsorship prima di audience/fit/attribution;
- skill create senza evidence o portfolio check.

## 8. Decisioni ancora richieste all'owner

| Quando | Decisione | Default sicuro se non arriva |
|---|---|---|
| F0 | conferma rotazione password/2FA | live bloccato |
| F2 | provider/domain media HTTPS | static mirror test, solo SHADOW |
| F3 | disponibilità/diritti di 10 Reel | Reel engine bloccato, si lavora su carousel |
| F5 | approvazione canary | nessun publish |
| F7 | lead magnet/offerta | CTA non commerciale |
| F8 | prezzo low-ticket | team-pricing, nessun prezzo inventato |

## 9. Verdict

La strategia ottimale non massimizza il numero di automazioni. Massimizza il numero di passaggi **misurabili, reversibili e riusabili**. Prima si certifica il loop operativo interno; poi si monetizza; solo dopo si trasforma MB-OS in prodotto per altre pagine.
