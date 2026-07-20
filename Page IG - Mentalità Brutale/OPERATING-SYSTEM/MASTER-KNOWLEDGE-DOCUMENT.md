# MASTER KNOWLEDGE DOCUMENT — Mentalità Brutale Social Operating System

> Versione 1.0 · 2026-07-20 · Content-Forge target: `social-operating-system` + skill `mentalita-brutale-operator`.

## 1. Materia prima osservata

### Asset locali

- `Page IG - Mentalità Brutale/POST/`: 5 visual statici dark.
- `storie da rifare/`: 2 screenshot competitor/riferimento.
- `Leanding page/`: 2 immagini.
- `LOGO.png` e asset logo replicato nel brand carousel.
- `Workfolw crea caroselli à/carousel-factory/`: motore Node/Puppeteer, config `mentalita-brutale`, font Anton/Inter e un carosello renderizzato.
- `SKILL & Agenti/Workflow pubblicazione automatica/`: publisher precedente basato soprattutto su browser Playwright e download Drive.

### Evidenza visuale letta

I post locali usano nero dominante, oggetti simbolici (cervello, lucchetto, orologio, catena), emissione/glow rosso, testo bianco/argento e parole chiave rosse. La composizione è verticale e cinematografica, con forte spazio negativo. Gli esempi comunicano per **contrasto irreversibile**: oggi/domani, comfort/rimpianto, rumore/silenzio, cerchia/evoluzione.

Il carosello renderizzato dal motore esistente usa invece un volto di sfondo scurito, testo molto grande e pochi livelli tipografici. È più adatto a fermare lo scroll, ma la coerenza con i visual “oggetto simbolico + tesi” va misurata, non assunta.

Lo screenshot competitor visibile mostra una Story/Reel con footage scenico, testo centrale bianco, parole in grassetto, watermark e progressione in blocchi. È una prova di **formato di riferimento**, non prova delle performance né del processo dei Reel Mentalità Brutale.

### Limite di evidenza video

Il checkout contiene **zero file video tracciati**. La cartella Drive pubblica indicata dal vecchio runtime espone un solo file `.mp4` da circa 1,5 MB, ma il file non è stato acquisito/letto in questa sessione. Quindi:

- nessuna affermazione su durata, hook sonoro, montaggio, retention o CTA del video viene dichiarata come verificata;
- i pattern video restano `PENDING_SOURCE`;
- Empire Studio dovrà leggere il file integrale e frame reali prima di forgiare Reel Pattern Extractor.

Questa è applicazione del principio “video visto davvero, mai riassunto di seconda mano”.

## 2. DNA del brand estratto

### Tensione centrale

Mentalità Brutale non vende ottimismo. Vende una **frizione cognitiva controllata**: rende visibile il costo futuro dell'inazione e chiude con uno standard comportamentale presente.

Formula ricorrente:

```text
concessione presente → costo futuro → verità non negoziabile → azione concreta
```

Esempio astratto conforme:

```text
“oggi la scusa sembra ragionevole.
domani il risultato non saprà distinguerla da una resa.
scegli lo standard prima che sia l'urgenza a scegliere per te.”
```

### Voce

- forte, non isterica;
- breve, non povera;
- autoritaria, non abusiva;
- emotiva, ma collegata a un meccanismo o un'azione;
- nessuna citazione attribuita senza fonte;
- nessuna promessa di ricchezza, guarigione o successo garantito.

### Sistema visuale

1. nero = spazio e gravità;
2. rosso sangue = conflitto/parola decisiva, mai riempitivo;
3. argento/bianco = leggibilità e razionalità;
4. oggetto simbolico = concetto reso fisico;
5. grana/fumo/scintille = materia e tensione;
6. una gerarchia tipografica leggibile su mobile.

## 3. Strategia editoriale

### Cinque pilastri

- **P1 Disciplina operativa (30%)**: routine, attrito, standard, continuità.
- **P2 Identità e standard (25%)**: chi diventi attraverso le scelte ripetute.
- **P3 Ambizione e lavoro (20%)**: solitudine, costo del progresso, capacità.
- **P4 Relazioni/confini (15%)**: cerchia, distanza, approvazione, rispetto.
- **P5 Storie/leggi del potere (10%)**: storia e psicologia solo con fonti verificabili.

### Due motori di formato

**Reel:** conquista reach e tempo di visione. Un'idea, un contrasto, un payoff. Il 28-day baseline assegna 4 Reel/settimana.

**Carosello:** conquista salvataggi, condivisioni e profondità. Una progressione 7-10 slide, non una raccolta di frasi scollegate. Il baseline assegna 3 caroselli/settimana.

### Ladder CTA

1. valore: salva;
2. distribuzione: condividi;
3. audience: segui;
4. insight: commenta una parola/risposta reale;
5. conversione: link in bio solo quando esiste una risorsa coerente e tracciata.

Non ogni contenuto vende. Il business system, però, misura il passaggio verso asset posseduti e ricavo.

## 4. Strategia chirurgica 28 giorni

Il primo ciclo non “ottimizza”: costruisce il terreno su cui ottimizzare.

- 28 post: 16 Reel + 12 caroselli.
- 2 hook family: contrasto brutale vs domanda diagnostica.
- 2 slot: 13:00 vs 20:30 Europe/Rome.
- 2 CTA: salva vs condividi/segui.
- distribuzione bilanciata con almeno 3 esempi prima di valutare una cella.
- snapshots a +48h e +168h, perché i dati Insights possono essere ritardati fino a 48h.
- una sola variabile primaria cambia nel ciclo seguente.

Numeri di follower, reach target e conversion rate restano `[DA MISURARE]`: inventarli renderebbe il sistema apparentemente preciso ma operativamente falso.

## 5. Architettura operativa

### Input

Un ordine CF completo:

```json
{
  "brand": "mentalita-brutale",
  "format": "REEL|CAROUSEL|IMAGE",
  "pillar": "P1..P5",
  "hook_family": "...",
  "cta_family": "...",
  "slot": "...",
  "source_refs": [],
  "rights": {},
  "budget": {"credits": 0, "tier_max": "..."}
}
```

### Pipeline

1. Intelligence vede le fonti integrali.
2. Strategy formula una tesi e un test.
3. Copy scrive hook/corpo/CTA con claim ledger.
4. Visual/Video produce asset e manifest.
5. CF-R6 esegue format, brand, copy, rights, safety.
6. CF-R7 controlla token, quota, idempotenza e staging HTTPS.
7. Scheduler pubblica solo in modalità certificata.
8. Post-check acquisisce media id/permalink.
9. Analytics raccoglie snapshot +48h/+7d.
10. CF-R8 promuove pattern solo con n≥3 e fonti.
11. Chief-Forge trasforma gap ripetuti in skill/workflow, non in prompt volatili.

## 6. Authorization e tecnologia

Percorso scelto: Instagram API con Business Login for Instagram, account professionale owner-managed, Graph API v25.0 configurabile.

Scope core:

- `instagram_business_basic`
- `instagram_business_content_publish`
- `instagram_business_manage_insights`

Vincoli:

- media raggiungibili via HTTPS;
- immagini live JPEG;
- carosello max 10 elementi;
- 100 API-published post/24h Meta, cap interno 3;
- long-lived token 60 giorni, refresh prima della scadenza;
- Standard Access per account proprio; Advanced Access/App Review per account terzi.

## 7. Memoria e apprendimento

### Memoria transazionale locale

SQLite locale conserva job, run, publication, metric snapshots, controls e pattern. Il file non entra in Git.

### Memoria aziendale

- decisioni stabili → ADR;
- task chiusi → checkpoint;
- nuove fonti/conoscenza → wiki;
- pattern cross-run → CF-R8 / Memory Empire;
- errori → Ispettorato/registro quando ricorrenti.

### Regola di promozione pattern

```text
n >= 3
AND stessa unità di confronto (formato/brand)
AND fonti tracciate
AND mediana sopra baseline
AND nessun gate qualità degradato
THEN pattern candidato
ELSE osservazione, non regola
```

## 8. Content-Forge → skill

Ogni nuovo contenuto integrale attraversa:

```text
INGEST → ATOMS → MKD → TARGET MAP → BUILD → EVAL → CONTRADICTION → REGISTER → MEASURE
```

Target possibili:

- `reference`: conoscenza utile ma non procedurale;
- `rule`: principio stabile e falsificabile;
- `workflow`: sequenza con I/O e gate;
- `skill`: capability ricorrente con trigger, procedure, eval e failure modes;
- `agent/team`: solo se servono ownership concorrenti o specializzazione persistente.

Non tutto diventa skill. Una skill nasce quando il comportamento è ricorrente, misurabile e beneficia di progressive disclosure.

## 9. Failure modes dominanti

- autenticazione fragile o token in chiaro;
- dipendenza da browser selector;
- URL Drive non direttamente fetchable da Meta;
- output PNG non pubblicabile nel percorso scelto;
- duplicati dopo crash/retry;
- pattern promossi da un singolo post;
- copy intenso che scivola in danno/umiliazione;
- “automazione” dichiarata senza test live.

Il runtime costruito blocca, non maschera, queste condizioni.

## 10. Stato reale al termine della fase

- architettura: costruita;
- runtime: dry-run/testabile;
- segreti correnti: rimossi dai file di config e spostati su env;
- OAuth reale: da completare dall'owner nel Meta Dashboard;
- pubblicazione live: intenzionalmente bloccata finché manca certificazione;
- video reverse engineering: incompleto per mancanza file osservato;
- target operativo: `CERTIFIED_AUTO` dopo canary e insights.
