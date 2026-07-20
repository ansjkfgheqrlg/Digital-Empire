# 04 — Piano Esecutivo 90 Giorni

## 1. Obiettivo del piano

In 90 giorni portare Mentalità Brutale da tenant `SHADOW` a:

1. pipeline Instagram first-party certificata;
2. 28 giorni di baseline comparabile;
3. almeno un ciclo learning completo;
4. funnel misurabile verso un asset posseduto;
5. decisione data-driven su monetizzazione e replica multi-tenant.

Il piano non promette follower o revenue arbitrari. Promette output, evidence, gate e decisioni misurabili.

## 2. Critical path

```text
B-009 SECURITY
  → META OAUTH
  → MEDIA HTTPS
  → BUFFER 7 GIORNI
  → 5 DRY-RUN
  → CANARY
  → POST-CHECK
  → INSIGHTS +48H
  → CERTIFIED_AUTO
  → BASELINE 28D
  → PATTERN DISTILLATION
  → FUNNEL / BUSINESS TEST
```

Se un nodo è rosso, il successivo non parte. Il lavoro parallelo consentito è indicato per fase.

## 3. Roadmap F0→F9

| Fase | Giorni | Obiettivo | Output | Gate di uscita |
|---|---:|---|---|---|
| F0 Security | 0-1 | eliminare rischio account | password ruotate, sessioni revocate, 2FA | owner evidence, B-009 chiudibile |
| F1 Evidence | 1-4 | capire davvero i Reel | 10 dossier video, ≥120 frame, rights ledger | no-finto-pass + coverage |
| F2 Auth/Infra | 1-3 | collegare account e media | OAuth, token local, IG ID, host HTTPS | `doctor --online` PASS |
| F3 Production | 3-6 | rendere seriale la creazione | 2 template carousel, Reel spec, manifest | 1 asset/formato riproducibile |
| F4 Buffer/QA | 5-7 | preparare una settimana | 4 Reel + 3 carousel, 35 verdict | 7 contenuti × 5 gate PASS |
| F5 Certification | 7-11 | provare il loop live | 5 dry-run, 1 canary, permalink, Insights | evidence completa → CERTIFIED_AUTO |
| F6 Baseline | 12-39 | misurare senza overfit | 28 post, 56 snapshot | coverage completa o gap dichiarati |
| F7 Learning | 40-46 | trasformare dati in IP | pattern/reject/rollback + v2 brief | n≥3 e same-format median |
| F8 Business | 47-60 | collegare audience a asset posseduto | profile sprint, lead magnet, landing, UTM | attribution end-to-end |
| F9 Scale | 61-90 | consolidare e decidere replica | cycle 2, P&L, tenant template | Board GO/HOLD/KILL |

F1 e F2 possono avanzare in parallelo. F3 può iniziare sui caroselli mentre F1 studia i Reel; il Reel engine non viene finalizzato prima del gate F1.

## 4. F0 — Security Reset (giorno 0-1)

### Task

- `MB-0001`: ruotare password Instagram, Google/Drive, LinkedIn coinvolte.
- `MB-0002`: revocare sessioni/app password/token legacy; controllare riuso.
- `MB-0003`: attivare/verificare 2FA e salvare recovery codes fuori Git.

### Owner

Owner umano degli account. Il sistema non deve conoscere le nuove password.

### DONE WHEN

- nessuna vecchia sessione resta valida;
- 2FA attiva;
- B-009 marcabile chiuso;
- secret scan corrente PASS;
- nessun segreto inviato in chat/repository.

## 5. F1 — Evidence & Video Intelligence (giorni 1-4)

### Campione minimo

- 10 Reel integrali;
- ≥12 frame letti per Reel;
- ≥120 frame totali;
- transcript/VTT integrale dove disponibile;
- almeno 3 Reel originali/MB se esistono;
- competitor solo come pattern trasformativo, mai per clonazione.

### Output

1. video manifest con hash/durata/formato/rights;
2. segmenti hook→meccanismo→payoff→CTA con timestamp;
3. evidence atoms;
4. matrice durata, densità testo, scene, voice, visual, CTA;
5. `Reel Pattern Extractor` forgiabile solo se ≥3 esempi per pattern.

### Gate

Empire Studio NO-FINTO PASS, rights ledger completo, 0 pattern senza locator.

## 6. F2 — Meta Authorization & Media Infrastructure (giorni 1-3)

### Task

- creare/configurare Meta Business app e Business Login for Instagram;
- concedere scope core basic/content_publish/insights;
- ottenere long-lived token e IG professional account ID;
- selezionare provider media HTTPS tramite gate;
- configurare `.env` locale e lifecycle staging;
- eseguire `doctor --online`.

### Gate provider

JPEG e MP4 raggiungibili via HTTPS, HEAD/GET 2xx, content-type corretto, URL stabile, delete controllabile, costo dichiarato, segreti server-side.

### DONE WHEN

`doctor --online` identifica esattamente `@mentalita.brutale`, endpoint quota risponde, file test è fetchable da Meta. Nessun token appare in log/version control.

## 7. F3 — Production System (giorni 3-6)

### Carousel lane

- fissare due sole famiglie visuali per il baseline;
- input JSON canonico;
- render via carousel-factory wrappato;
- conversione JPEG;
- alt text;
- manifest + checksum.

### Reel lane

- prima evidence, poi timing;
- JSON scene spec;
- voice/subtitle/visual/rights separati;
- render engine scelto dietro adapter;
- formato mobile, sottotitoli e safe area verificati.

### Copy lane

- hook, tensione, meccanismo, standard, CTA;
- una tesi per contenuto;
- claim ledger obbligatorio per dati/storia/citazioni;
- safety “brutale ≠ tossico”.

### Gate

Lo stesso input produce lo stesso asset/manifest; nessun hard-code tenant nel motore.

## 8. F4 — Buffer 7 Giorni + QA (giorni 5-7)

### Quantità precisa

- 4 Reel;
- 3 caroselli;
- 7 caption;
- 7 manifest;
- 35 verdict (7 × 5 gate);
- 7 slot calendario;
- 0 publish.

### Gate

Tutti i contenuti PASS su format, brand, copy, rights e safety. Un solo FAIL blocca quel contenuto, non l'intero batch. First-pass rate viene misurato, non preteso.

## 9. F5 — Shadow, Canary e Certification (giorni 7-11)

### Sequenza

1. dry-run contenuti 1-5;
2. verificare idempotenza ripetendo almeno un run;
3. test di ripianificazione senza nuova publish identity;
4. mode `SUPERVISED`;
5. canary con un contenuto a rischio basso;
6. post-check permalink/media id;
7. nessun duplicato dopo retry controllato;
8. snapshot Insights a +48h;
9. evidence JSON firmata dall'owner;
10. `certify` → `CERTIFIED_AUTO`.

### Rollback

Qualsiasi account mismatch, 401, media errato, duplicate, rights failure o safety incident → `PAUSED`, nessun retry cieco.

## 10. F6 — Baseline 28 Giorni (giorni 12-39)

### Produzione

- 16 Reel;
- 12 carousel;
- 7 post/settimana;
- slot 13:00/20:30 bilanciati;
- hook contrasto/domanda bilanciati;
- CTA save/share-follow bilanciate;
- pilastri P1=8, P2=7, P3=6, P4=4, P5=3.

### Dati

- 28 media ID/permalink;
- 28 snapshot +48h;
- 28 snapshot +168h;
- totale 56 snapshot;
- missing data resta null;
- confronto solo stesso formato/cella comparabile.

### Freeze

Durante il ciclo non si cambia simultaneamente font, palette, durata, hook e CTA. Incident fix e safety override sono sempre permessi e tracciati.

## 11. F7 — Learning & Content-Forge (giorni 40-46)

### Output

- matrice format × hook × slot × CTA;
- mediane e n per cella;
- pattern candidati;
- negative knowledge;
- decisione KEEP/ITERATE/KILL/NO DECISION;
- brief v2 con una variabile primaria cambiata;
- capability intake Chief-Forge solo su failure ricorrenti ≥3.

### Gate pattern

n≥3, fonte, contesto, same-format comparison, qualità non degradata, correlazione non chiamata causalità.

## 12. F8 — Business Funnel (giorni 47-60)

### Asset minimi

- bio con promessa e destinazione unica;
- 3 pinned post: manifesto, prova/metodo, next step;
- lead magnet operativo coerente;
- landing minimale;
- UTM per ogni entry point;
- email delivery + welcome;
- CRM/ledger lead;
- event mapping profile→click→lead→sale.

### Monetizzazione

Il prodotto e il prezzo non vengono inventati. 05-MB/02-INFO/team-pricing selezionano l'offerta usando intent signal, costo di delivery e posizionamento.

## 13. F9 — Scale & Productization (giorni 61-90)

### Cycle 2

- seconda ipotesi controllata;
- nuovo buffer 28 giorni;
- drift detector attivo;
- incident review;
- P&L organico.

### Decisione replica

Chief-Forge propone MB-OS multi-tenant solo se:

1. tenant interno ha completato almeno 2 cicli;
2. live incident severity alta = 0;
3. runbook è sufficiente per sessione fredda;
4. config è separata da codice;
5. onboarding secondo tenant non richiede fork;
6. costi e supporto sono misurati.

## 14. RACI sintetica

| Workstream | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Security/OAuth | Owner + CF-R7 | Social Director | Operations | Board |
| Video ingest | Intelligence/Empire Studio | D1 Lead | CF-R3/Forge | Strategy |
| Strategy/calendar | CF-R1 | Social Director | Analytics | Production |
| Copy | CF-R4/MKT | Copy Lead | Research | QA |
| Visual/Reel | CF-R5/CF-R3 | Production Lead | Brand | QA |
| QA | CF-R6 | L1 Post | Safety/Rights | CF-R7 |
| Publish | CF-R7 | Social Director | Operations | Analytics |
| Insights | CF-R8/Analytics | CMO | CF-R7 | Strategy |
| Funnel | 05-MB/02-INFO | CRO/CFO | Marketing | Board |
| Capability build | FORGE | Chief-Forge | ARCHITETTURA | Registry |

## 15. KPI di sistema

### Operativi

- content buffer days;
- gate first-pass rate;
- schedule success rate;
- duplicate publish count;
- token health days remaining;
- post-check coverage;
- Insights coverage;
- incident count/severity;
- manual minutes per content.

### Editoriali

- reach;
- views/watch/skip per Reel;
- saves, shares, comments;
- quality action rate;
- profile activity/visits;
- pillar/format balance.

### Business

- profile→link CTR;
- landing→lead CR;
- lead→sale CR;
- revenue attributed;
- revenue per 1.000 reached;
- content operating cost;
- contribution margin.

Tutti i target assoluti iniziano `[DA MISURARE]`; il primo ciclo costruisce il baseline.

## 16. Stop conditions

- sicurezza B-009 non chiusa;
- rights incerti;
- account/token mismatch;
- due failure publish consecutive;
- duplicate publish;
- safety incident;
- quality gate first-pass degrada per due batch;
- provider cost non approvato;
- metriche mancanti trattate come zero;
- task che modifica file owner di un altro half.

## 17. Prossime 10 azioni, in ordine

1. Owner chiude B-009.
2. D1 acquisisce corpus 10 Reel.
3. Owner/CF-R7 completa Meta app/OAuth.
4. Operations sceglie e prova media hosting.
5. CF-R1 congela calendario seed 7 giorni.
6. CF-R5 produce 3 carousel; CF-R3 produce 4 Reel solo dopo evidence sufficiente.
7. CF-R6 emette 35 verdict.
8. CF-R7 esegue 5 dry-run e idempotency test.
9. Owner approva un canary supervisionato.
10. CF-R8 raccoglie +48h e prepara evidence di certification.
