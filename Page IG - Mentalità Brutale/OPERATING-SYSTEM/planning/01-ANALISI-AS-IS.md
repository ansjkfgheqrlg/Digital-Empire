# 01 — Analisi AS-IS di Mentalità Brutale

## 1. Diagnosi in una frase

Mentalità Brutale possiede già **un'identità forte, asset visuali e una parte significativa dell'infrastruttura**, ma non è ancora un business social autonomo perché mancano quattro ponti reali: **sicurezza credenziali, evidence video, autorizzazione/staging Meta e baseline performance**.

Il problema non è “creare più contenuti”. È collegare asset, decisioni, produzione, distribuzione, dati e monetizzazione in un loop misurabile.

## 2. Inventario verificato

| Area | Evidenza su disco | Stato | Gap reale |
|---|---|---|---|
| Brand | logo, palette nero/rosso/argento, font Anton/Inter | PRESENTE | consolidare esempi sì/no e accessibilità |
| Post statici | 5 visual in `POST/` | PRESENTE | nessun dato performance associato |
| Story reference | 2 screenshot | PARZIALE | non sono contenuti integrali né metriche |
| Caroselli | motore Node/Puppeteer + 1 output renderizzato | WRAPPABILE | input copy ancora non completamente industrializzato |
| Reel locali | 0 video tracciati nel checkout | ASSENTE | ingestione integrale obbligatoria |
| Reel Drive legacy | listing con 1 `.mp4` | NON OSSERVATO | download/frame/transcript/evidence |
| Publisher legacy | Playwright + Drive downloader | LEGACY | fragile, browser-first, sessioni/password |
| MB-OS runtime | OAuth, Graph publish, queue, gate, Insights | COSTRUITO SHADOW | token, media host e canary live |
| Memoria | Memory MB + company Memory/wiki | PRESENTE | nessun pattern performance reale MB |
| Analytics | parser/store/report implementati | OFFLINE READY | media ID e snapshot live assenti |
| Funnel | idea link-in-bio → lead magnet | NON DEFINITO | offerta, landing, UTM e CRM |
| Community | possibile via API/comments/messages | NON ATTIVA | permission, policy, escalation umana |

## 3. Readiness score — scala osservabile 0→5

Scala:

- `0` inesistente;
- `1` idea/documentazione;
- `2` prototipo isolato;
- `3` workflow offline testato;
- `4` canary live verificato;
- `5` automatico, misurato e con rollback.

| Capability | Score | Perché |
|---|---:|---|
| Identità visuale | 3 | config e asset reali, ma nessun QA visuale automatico completo |
| Strategia editoriale | 3 | pilastri/cadenza/esperimento definiti, baseline assente |
| Caroselli | 3 | renderer reale e output; manca batch end-to-end certificato |
| Reel | 1 | esistono ipotesi, non corpus osservato |
| QA | 3 | gate e test offline; nessun batch reale MB completo |
| Authorization Meta | 2 | codice e runbook esistono; OAuth non eseguito |
| Media staging | 2 | adapter e conversione testati; host pubblico non configurato |
| Scheduler/publish | 3 | queue/idempotenza/live guard testati con fake; nessun canary |
| Insights/learning | 2 | parser/store pronti; zero snapshot MB reali |
| Community operations | 1 | solo concetto/reparto |
| Funnel/attribution | 1 | direzione definita, asset business assenti |
| Autonomia complessiva | 2 | SHADOW robusto, non certificato live |

**Readiness media:** 2,25/5. Non è un voto estetico: indica che la base esiste ma il valore economico non è ancora dimostrato end-to-end.

## 4. Value chain attuale e rotture

```text
IDEA ──?──> EVIDENCE ──> COPY ──> ASSET ──?──> QA ──?──> PUBLISH ──?──> DATA ──?──> REVENUE
```

Rotture:

1. idea→evidence: video e competitor non ingeriti;
2. asset→QA: nessun batch MB recente con verdict persistiti;
3. QA→publish: OAuth e public media URL mancanti;
4. publish→data: nessun media ID reale;
5. data→revenue: funnel e attribution non attivi.

## 5. Colli di bottiglia ordinati

| Priorità | Collo di bottiglia | Blocca | Owner |
|---:|---|---|---|
| P0 | B-009 rotazione password/sessioni/2FA | qualsiasi live sicuro | Owner account |
| P0 | OAuth Meta su account professionale | publish/Insights | Owner + CF-R7 |
| P0 | Hosting media HTTPS | container Meta | Operations |
| P0 | Corpus Reel integrale | strategia video e skill Reel | Intelligence/Empire Studio |
| P1 | Buffer 7 contenuti con 5 gate | canary e continuità | CF-R1→R6 |
| P1 | Canary + permalink + Insights | certificazione | CF-R7/R8 |
| P1 | Baseline 28 giorni | ottimizzazione reale | Analytics |
| P1 | Lead magnet/funnel/UTM | revenue attribuibile | 05-MB/02-INFO/04-MKT |
| P2 | Community triage | relazione/retention | Marketing/Support |
| P2 | Productizzazione multi-page | scala esterna | Chief-Forge/Agency |

## 6. Analisi del pubblico — ipotesi da validare

### Job-to-be-done primari

1. “Fammi vedere dove mi sto raccontando una scusa.”
2. “Dammi uno standard semplice che posso applicare oggi.”
3. “Fammi sentire compreso senza consolarmi.”
4. “Dammi linguaggio da salvare/condividere per definire chi voglio diventare.”

### Tensioni editoriali

- comfort oggi vs costo domani;
- approvazione sociale vs identità;
- motivazione intermittente vs sistema;
- ambizione dichiarata vs lavoro invisibile;
- cerchia abituale vs crescita;
- conoscenza consumata vs azione ripetuta.

### Segmenti candidati

| Segmento | Problema | Contenuto utile | Rischio |
|---|---|---|---|
| giovane ambizioso bloccato | inconsistenza | disciplina/standard | frasi troppo generiche |
| freelance/creator | dispersione | lavoro, solitudine, sistemi | deriva business-only |
| lettore self-improvement | saturazione motivazionale | meccanismi e azioni | citazioni false |
| appassionato potere/storia | curiosità e status | P5 con fonti | pseudostoria/copying |
| persona in transizione | confini/cerchia | identità e relazioni | consigli psicologici impropri |

## 7. SWOT operativa

### Strengths

- brand name memorabile;
- estetica già differenziata;
- messaggio ad alta condivisibilità;
- motore carousel esistente;
- holding con reparti/skill/memoria già costruiti;
- runtime API-first già in SHADOW.

### Weaknesses

- zero corpus video osservato nel checkout;
- zero baseline performance verificata;
- sicurezza storica compromessa;
- business destination non definita;
- troppo materiale “frase forte” e poco meccanismo/prova;
- dipendenza potenziale da AI image per testo, con rischio errori tipografici.

### Opportunities

- contenuti salvabili e seriali;
- Reel faceless/voiceover industrializzabili;
- lead magnet su disciplina/sistemi;
- prodotti digitali e affiliate coerenti;
- IP editoriale riusabile su newsletter/KDP/YouTube;
- MB-OS come template vendibile ad altre pagine first-party/clienti.

### Threats

- policy Meta, token, rate limit;
- contenuti troppo aggressivi o borderline safety;
- musica/footage senza diritti;
- omologazione “motivational page”;
- engagement artificiale o automazioni DM abusive;
- ottimizzazione su vanity metrics;
- lock-in su un tool di generazione o hosting.

## 8. Assunzioni e livello di evidenza

| Assunzione | Livello | Come si valida |
|---|---|---|
| nero/rosso/argento è il core visuale | ALTO | asset/config osservati |
| hook “contrasto brutale” performa | BASSO | baseline n≥3 stesso formato |
| Reel aumenta reach rispetto ai caroselli | IPOTESI | 16 Reel vs 12 carousel, confronto per reach |
| CTA “salva” aumenta azioni qualità | IPOTESI | test bilanciato |
| slot 20:30 supera 13:00 | SCONOSCIUTO | matrice slot × formato |
| audience vuole un lead magnet disciplina | BASSO | comment/landing conversion test |
| pagina può vendere prodotti | MEDIO teorico | lead/revenue attribuiti, non follower |
| full auto mantiene qualità | SCONOSCIUTO | first-pass rate + incident rate dopo certification |

## 9. Cosa automatizzare / cosa non automatizzare

### Automatizzare

- ingestione tecnica e catalogo fonti;
- brief da regole validate;
- render e conversione;
- gate deterministici;
- schedule/publish/post-check;
- raccolta Insights;
- report e pattern candidate;
- retry controllato, alert, kill switch.

### Non automatizzare completamente

- rotazione credenziali e concessione OAuth;
- approvazione di nuove offerte/claim commerciali;
- diritti ambigui su musica/footage;
- crisis communication;
- risposte a salute mentale, minacce, autolesionismo o contestazioni legali;
- modifiche strutturali del brand;
- promozione di un pattern da correlazione a causalità.

## 10. Criterio di successo

Il progetto non è “finito” quando pubblica. È riuscito quando:

1. produce 7 giorni di buffer senza lavoro manuale ripetitivo;
2. pubblica senza incidenti e senza duplicati;
3. raccoglie 56 snapshot del ciclo baseline;
4. distilla almeno 3 pattern validati o dichiara correttamente “nessuna evidenza”;
5. porta traffico a un asset posseduto con UTM;
6. attribuisce almeno il primo lead/ricavo al canale senza inventarlo;
7. il sistema può essere replicato su un secondo tenant senza copiare segreti o hard-code.
