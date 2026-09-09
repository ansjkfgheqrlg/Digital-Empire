# PIANO — AP-006 / AP-012 / AP-018 / AP-019+020
## Quattro candidati mai decisi dallo studio Andrei Pascu — go/no-go con motivazione

**Versione:** DRAFT V1 (destinato a critica a 3 giri: P0 → P1 → P2 → P3)
**Autore:** Doom Bot B — fronte "nuove capacità / tool"
**Data:** 2026-09-09
**Perimetro:** NON tocca l'ecosistema LANCI (AP-004/005/008/033), coperto in parallelo dal Doom Bot A.
**Natura:** documento di pianificazione. Nessun file di produzione modificato nel produrlo.

---

## 0. Sintesi esecutiva — i quattro verdetti

| # | Candidato | Verdetto | Cosa si fa davvero | Costo |
|---|---|---|---|---|
| **AP-006** | Automazione AI per i preventivi (cs2online Bonus 6) | **NO-GO sull'automazione** · GO su 2 micro-patch | Contratto d'ingresso in `beast-preventivi` + chiusura della tensione breakdown-prezzi (aperta da mesi) | ~1h |
| **AP-012** | Tag/scoring comportamentale (outFunnel L15) | **GO — ristretto** | 1 file reference in `emails/` + 6 righe nel kernel + correzione di un callout falso in `revops` | ~1,5-2h |
| **AP-018** | Framework 10 livelli maturità AI come tool d'agenzia (cs2online L3) | **NO-GO netto** | Una riga in BACKLOG con precondizione misurabile + salvataggio gratuito di KA-02 come input di copy | ~10 min |
| **AP-019 + AP-020** | Effort∝riuso (cs2online L6) + rifiuto se mancano dati (cs2online Bonus 2 / Bonus 6) | **GO entrambi — chirurgici** | AP-019: 8 righe di regola in un posto solo · AP-020: 2 skill patchate, non "tutte" | ~1,5h |

**Totale del piano: 4-5 ore di una sessione. Tutto additivo. Nessun file dell'ecosistema LANCI. Nessun prodotto nuovo.**

Se il giro di critica dovesse uccidere un solo GO, il candidato che io stesso indico come il più debole è **AP-019** (vedi §6.2, "Autocritica preventiva").

---

## 1. I quattro test applicati uniformemente

Ogni candidato è passato per gli stessi quattro filtri. Un GO che non passa T1, T2 e T3 non è un GO: è un desiderio.

| Test | Domanda | Se la risposta è vuota |
|---|---|---|
| **T1 — Chi** | Chi lo userebbe, con un nome (Max, Gael, Neri, un agente specifico, un cliente specifico)? | NO-GO |
| **T2 — Quando** | Entro quale data o quale evento già in calendario? | NO-GO |
| **T3 — Costo del non farlo** | Cosa costa NON costruirlo, in euro, ore o rischio dichiarato? | NO-GO |
| **T4 — Anti-overfitting** | La fonte è singola e dello stesso autore? Se sì, esiste conferma indipendente in casa o fuori? | Declassa a nota, non a build |

T4 non è mio: è la regola già applicata dai `enrichment-report` di Memory Empire (verificata in `cs2online-bonus-06/enrichment-report.md`, Stage E: *"3 occorrenze stesso corso ≠ conferma indipendente, non applicato"*). La rispetto, non la aggiro.

---

## 2. Fatti verificati sul disco, prima di giudicare

Non impressioni. Letture fatte oggi, con percorso.

| Fatto | Dove verificato | Perché pesa |
|---|---|---|
| **Digital Empire ha zero euro misurati.** `company/Memory/tesoreria/entrate.jsonl` = **0 righe**. `spese.jsonl` = **0 righe**. | letti oggi | È il numero più grande di tutta l'analisi. Ogni "costruiamo un tool" va pesato contro un'azienda che non ha ancora registrato un incasso. |
| Il reparto A3-PREVENTIVI ha **un solo file** in `handoffs/`: `HC-A3-A4-contratto.json`, datato **11 giugno**. | `company/01-agency/A3-PREVENTIVI/handoffs/` | Il processo preventivi d'agenzia non ha throughput. Vedi AP-006. |
| PreventivoForge **funziona davvero**: PDF reali generati il 2026-09-02 in `Agency page/Clienti/Prof Autocad/preventivo-forge/Memory/storico-preventivi/` (Smart ForTwo, MG3, Mercedes E300, Polo, GLA 220…). | listato oggi | Ma è un dominio diverso. Vedi §3.1. |
| `revops/SKILL.md` **documenta già** l'engagement/implicit scoring (righe 85-118: page visits, downloads, email engagement, product usage, negative scoring, soglia MQL 50-80, ricalibrazione trimestrale). | letto per intero | Smonta parzialmente il gap dichiarato in AP-012. Vedi §4. |
| `market-audit/SKILL.md` è **già** il diagnostico d'onboarding di DE: 5 subagent paralleli, punteggio pesato 0-100, grado A-F, quick wins / strategiche / lungo termine, stima di impatto revenue, pass di verifica live in browser. | letto per intero | Smonta AP-018. Vedi §5. |
| `free-tools/SKILL.md` contiene **già** il test economico per decidere se costruire un tool gratuito: *"Lead value × expected leads &gt; build cost + maintenance"*. | letto | Nessuno ha mai fatto questo conto per AP-018. |
| **`skill-forge` non esiste.** Il roster ha `skill-builder`, `content-forge`, `content-forge2.0`, `skill-creator` (globale), `agent-factory`. | `ls .claude/skills/` | La riga AP-019 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md` cita una skill inesistente. Puntatore da correggere. |
| **`content-forge` e `content-forge2.0` sono byte-identici** tranne il campo `name:` del front matter (verificato con `diff`). Stessa `description`, stessi trigger. | `diff content-forge/SKILL.md content-forge2.0/SKILL.md` → una sola riga diversa | Due skill con descrizione identica = ambiguità di trigger. Scoperta collaterale, vedi §7. |
| ULTIMO METRO, misurato il 2026-09-03: **25 pezzi finiti mai usciti, 2.137 MB fermi, il più vecchio da 135 giorni.** | `.claude/skills/ultimo-metro/SKILL.md` | È il modo di fallire documentato di questa azienda: produrre macchinari invece di incassare. Ogni GO qui deve difendersi da questa accusa. |

---

## 3. AP-006 — Automazione AI per i preventivi

**Fonte:** cs2online Bonus 6, *"Automatizzare processi con skills"*, Vimeo `1178259409`, 20:36.
Analisi: `runs/andrei-pascu-cs2online-001/lessons/bonus-06/lesson-analysis.md` (28 frame, SKILL.md del concorrente trascritto verbatim dal frame `t14m00s`).

### 3.1 Prima: una premessa del brief va corretta

Il brief mi chiedeva come l'automazione si integrerebbe *"con `preventivo-auto` esistente che già serve PreventivoForge/Novacar"*.

**Non si integra, e non deve.** Ho letto `preventivo-auto/SKILL.md` per intero: prende un URL **mobile.de** in tedesco e produce un PDF italiano per una concessionaria, con foto, scheda tecnica tradotta e prezzo calcolato (`esposto ×1.03 +1500 +1500`). Contratto dati congelato in `preventivo-forge/schema/listing.schema.json`. È una pipeline di **riscrittura annunci auto**, multi-tenant, cliente Novacar srl.

`beast-preventivi` è tutt'altro: una **proposta commerciale freelance/agenzia** in 8 sezioni, problem-first, 3 opzioni di prezzo, presentata in call.

Condividono la parola "preventivo" e nient'altro. Costruire un ponte fra i due sarebbe una finta integrazione che aggiunge accoppiamento e zero valore. **Segnalato perché una premessa sbagliata, se non corretta, si propaga nei giri di critica.**

La catena reale dei preventivi d'agenzia esiste già ed è a 4 anelli:

```
discovery-call-brief  →  beast-preventivi  →  proposal-gate  →  (invio)
(trascrizione → JSON)    (brief → documento)  (10 check BLOCCANTI)
```

### 3.2 Cosa mostra davvero il Bonus 6 e cosa DE non ha

| Pezzo del sistema di Andrei | DE ce l'ha? |
|---|---|
| SKILL.md con **contratto d'ingresso** e rifiuto categorico se mancano i documenti (KA-05) | **No.** Verificato con grep dall'enrichment-report di quel run: *"nessuna copertura"* |
| `struttura-preventivo.md` — struttura pagina per pagina usata come spec di generazione (KA-07) | Sì, equivalente: `assets/templates/preventivo-canvas.md` + `references/stages/03-document-structure.md` |
| `esempio.md` — un preventivo reale passato, per stile e tono (KA-07) | Sì: `assets/examples/landing-page-agency.md` |
| `brand-guidelines.json` (KA-07) | Parziale: `carousel-empire/brand/brand.json` esiste ma è scoped ai caroselli |
| Step separati e validati uno per uno, non un prompt unico (KA-06) | Sì: è la catena a 4 anelli sopra |
| `effort max` **solo** sullo step di validazione (KA-08) | **No** — vedi AP-019 |
| PDF finale brandizzato | Sì: `PIANO-MAESTRO/scripts/pdf_engine_empire.py`, standard-oro dossier 28 |
| Flowchart draw.io del processo con icone robot sugli step automatizzabili (KA-03/04) | Non su disco, ma è documentazione, non capacità |

Detto brutalmente: **DE ha già 6 pezzi su 8.** Non manca il sistema, manca il cablaggio. E il cablaggio è la parte che costa.

### 3.3 VERDETTO: NO-GO sull'automazione

Il no-go non è mio. È scritto nella lezione stessa, **KA-01**:

> *"la maggior parte della gente non riesce a implementare l'AI perché non ha un processo ripetuto che vale la pena automatizzare"*

Applicato a DE, con i numeri di §2:

- **T1 (chi)**: PASS in astratto — Max, quando manda un preventivo d'agenzia.
- **T2 (quando)**: **FAIL**. Nessuna data. Nessun preventivo d'agenzia in coda.
- **T3 (costo del non farlo)**: **FAIL misurabile**. `handoffs/` ha un file di giugno. `entrate.jsonl` ha zero righe. Il processo gira circa **zero volte al mese**. Automatizzare un processo a throughput zero fa risparmiare zero ore e produce un altro macchinario da mantenere. È ULTIMO METRO travestito da progresso: fabbricare il pezzo 26 mentre 25 marciscono.
- **T4**: PASS (dimostrazione osservata per intero, 28 frame) — ma T4 non salva un candidato che fallisce T2 e T3.

**Aggiungo l'argomento che rende il no-go definitivo: KA-02, "domain knowledge".** Andrei automatizza un processo che ha eseguito a mano centinaia di volte. DE lo ha eseguito quasi mai. Automatizzare prima di aver acquisito il domain knowledge produce un'automazione che codifica gli errori del principiante — e li rende invisibili perché ora escono da uno script.

### 3.4 Cosa si fa invece — due micro-patch, ~1 ora

**Patch A — Contratto d'ingresso in `beast-preventivi` (~30 min)**

È lo stesso pattern di AP-020 (§6.3), applicato dove il grep ha già confermato copertura zero.

File: `.claude/skills/beast-preventivi/SKILL.md`
Posizione: nuova sezione subito **prima** di "Come usare questa skill", cioè prima dello Step 1.

Contenuto:

```markdown
## Contratto d'ingresso — senza questi, non si scrive il documento

Tre elementi sono obbligatori. Se ne manca anche uno, chiedilo e RIFIUTA di
produrre il documento completo. L'outline si può fare comunque; il documento no.

1. Brief di discovery — output della skill `discovery-call-brief`, oppure la
   trascrizione/appunti grezzi della call.
2. Il prezzo a catalogo applicabile — uno dei quattro di `proposal-gate` punto 3
   (4.000 / 3.500 / 2.500 / 8.000 EUR). Mai un prezzo improvvisato.
3. Il problema del cliente con le parole del cliente — non una riformulazione
   di marketing. È il punto 1 di `proposal-gate` e senza di esso il documento
   nasce già bocciato.

Perché il rifiuto e non un avviso: `proposal-gate` blocca comunque a valle, ma
solo DOPO che il documento è già stato scritto. Bloccare a monte risparmia
l'intera scrittura. Fonte: studio Andrei Pascu, cs2online Bonus 6 (KA-05) e
Bonus 2 (KA-04) — pattern osservato tre volte nello stesso corso.
```

Perché è giusto ora: costa 30 minuti, non è un'automazione, e rende il primo preventivo vero — quando arriverà — meno probabile che nasca sbagliato.

**Patch B — Chiusura della tensione breakdown-prezzi (~30 min)**

Questa è aperta dal run YouTube (video 24, `EBU57iVAutA`) e non è mai stata decisa. `beast-preventivi/SKILL.md` oggi la dichiara irrisolta: *"resta una scelta di Max"*.

**La tensione, letta con precisione, non esiste. È un errore di categoria.**

- `beast-preventivi`, anti-pattern fatale n. 3: *"Scrivere il preventivo come una fattura (voce 1: X€, voce 2: Y€)"* → riguarda il **documento**.
- Andrei, KA-14 (`EBU57iVAutA#00:06:32` + frame-210): per servizi complessi e costosi, spiegare il breakdown dei singoli costi **in call** rende comprensibile un prezzo alto invece che sospetto. Esempio a schermo: shooting 5.000 € = affitto camera 900 + attori 500 + makeup 500 + operatore esterno 250. → riguarda la **call di presentazione**.

Due artefatti diversi. Le due regole non si sono mai toccate. La regola risolutiva:

> **Il breakdown non entra mai nel documento. Può uscire a voce in call, solo come risposta a un segnale di shock da prezzo su un servizio complesso, e solo dopo il silenzio post-prezzo.**

Dove va scritta: `references/stages/04-call-presentation.md` (nuovo paragrafo) + una riga in `references/conventions/anti-patterns.md` che rende esplicito il confine, così che nessuno "uniformi" le due regole in futuro. E si toglie da `SKILL.md` la frase "resta una scelta di Max", sostituendola con la regola e la fonte.

**Perché la decido io invece di rimandarla a Max, di nuovo:** ADR-028 (legge permanente, 2026-09-09) — *nessun impedimento blocca il lavoro intorno; un blocco "solo firma Max" va portato attivamente, mai lasciato scritto ad aspettare* (ADR-026). Questa tensione sta ferma da mesi in attesa di una firma per una decisione che, letta bene, non richiedeva una firma: richiedeva di distinguere due artefatti. La regola va scritta; Max la ribalta in dieci secondi se non gli piace.

**Quando si riapre AP-006 (condizione scritta, non "un giorno"):**

> Quando `company/01-agency/A3-PREVENTIVI/handoffs/` registra **≥ 4 preventivi d'agenzia reali al mese per 2 mesi consecutivi**, l'automazione torna sul tavolo. Prima di quella soglia, no.

Una condizione misurabile su un file che esiste. Non un "valuteremo".

---

## 4. AP-012 — Tag e scoring comportamentale

**Fonte:** outFunnel Lezione 15, *"Segmentazione Audience"*, Vimeo `1048613595`.
Analisi: `runs/andrei-pascu-armageddon-outfunnel-001/lessons/lezione-15/lesson-analysis.md` — KA-04 (Behaviour-Based Tags), KA-05 (Lead Scoring), KA-06 (Custom Audience Journey), KA-07 (l'avvertenza).

### 4.1 Il gap dichiarato è per metà falso — va detto

Il `lesson-analysis` scrive: *"sistemi di tag/scoring comportamentale non risultano oggi documentati esplicitamente in nessuna skill dell'Impero"*. Il callout aggiunto oggi in `revops/SKILL.md` (righe 202-206) ripete la stessa affermazione.

**È falso, e lo dice `revops` stesso 100 righe più sopra.** Sezione "Lead Scoring", righe 85-118:

- *Implicit scoring (engagement) — What they do:* page visits (especially pricing, demo, case studies), content downloads, webinar attendance, email engagement (opens, clicks), product usage.
- *Negative scoring*, procedura in 6 passi per costruire il modello, soglia MQL 50-80 su scala 100, ricalibrazione trimestrale.

Quello **è** scoring comportamentale. Lasciare in `revops` un callout che dice "non documentato in nessuna skill" mentre la skill stessa lo documenta è una contraddizione interna che, alla prima lettura da parte di un agente, produce lavoro duplicato. **Va corretto nello stesso turno in cui si tocca il tema** — è la stessa disciplina della REGOLA PUNTATORI di `CLAUDE.md`: un puntatore falso è peggio di nessun puntatore.

### 4.2 Cosa manca davvero — il gap vero, ristretto

Tolto il falso gap, resta un gap reale e più piccolo:

| Elemento di L15 | Coperto? |
|---|---|
| Punteggio da comportamento (KA-05) | **Sì**, `revops` §Lead Scoring |
| Il **tag** come artefatto nominato assegnato su un'azione (KA-04, es. visita sales page Prodotto 2 → tag `P2-SP`) | **No, in nessuna skill** |
| Le **ramificazioni condizionali** — visto-non-cliccato → follow-up mirato; cliccato-non-comprato → urgenza/scarsità (KA-04) | **No** |
| **Custom Audience Journey**: percorsi email diversi per comportamento (KA-06) | **No.** `emails/SKILL.md` ha solo il campo `Segment/Conditions: [If applicable]` nel template di output e le `Exit Conditions`. Zero guida su come costruire un ramo. |
| Il freno: non personalizzare ogni step, un principiante parte da tag semplici (KA-07) | **No** |

### 4.3 VERDETTO: GO — ristretto al livello skill

- **T1 (chi)**: chi scrive una sequenza email con `emails` — e, a valle, l'ecosistema LANCI, che sta cablando Brevo in `TASK-LANCI-BUILD-W3` in questi giorni.
- **T2 (quando)**: adesso, perché LANCI sta costruendo ora. Se il vocabolario dei tag arriva dopo il primo lancio, ogni lancio inventerà le proprie etichette e i dati cross-lancio nasceranno inconfrontabili.
- **T3 (costo del non farlo)**: dati di lancio non confrontabili fra un lancio e il successivo. Costo reale ma non in euro: dichiarato come tale, non gonfiato.
- **T4**: fonte singola per il *dettaglio tattico*, ma il principio (segmentare per comportamento) è pratica standard di settore e `revops` lo ha già a metà. Passa.

**Vincolo di perimetro, dichiarato:** questo GO si ferma al **livello skill**. Non progetto nulla dentro LANCI, non scelgo piattaforme, non tocco `TASK-LANCI-*`. Il fronte LANCI è del Doom Bot A.

### 4.4 Spec concreta

**Artefatto 1 — nuovo file:** `.claude/skills/emails/references/behavioral-branching.md` (~1 pagina)

Contenuto, sei blocchi:

1. **Convenzione di nome del tag** — `&lt;PRODOTTO&gt;-&lt;TAPPA&gt;-&lt;EVENTO&gt;`, maiuscolo, trattini (mai underscore né spazi: KA-07 di cs2online Bonus 2 sulla convenzione file, stessa disciplina). Esempi: `CCM-SP-VIEW`, `CCM-CHECKOUT-START`, `CCM-CHECKOUT-ABANDON`, `CCM-BUY`.
2. **Regola di esistenza del tag** — *un tag si crea solo insieme all'email che lo consuma. Nessun tag senza consumatore nominato.* Marcata `➕` (derivata, non presente nella fonte): è ULTIMO METRO applicato ai dati — tag creati e mai usati sono lavoro finito che non esce.
3. **Le tre ramificazioni canoniche** (KA-04, KA-06) — visto-non-cliccato → follow-up mirato sullo stesso contenuto; cliccato-non-comprato → gestione obiezione + urgenza/scarsità; ritorno multiplo (≥3 tocchi) → offerta dedicata o contatto umano.
4. **Soglia** — si riusa la scala già in `revops` (MQL 50-80 su 100). **Non si inventa una seconda scala**, altrimenti DE ha due punteggi che dicono cose diverse sullo stesso contatto. Il punteggio comportamentale decade dopo il tetto di inattività già presente in `emails` (1-2 mesi, AP-011 / outFunnel L10 KA-06).
5. **Il freno** (KA-07, che è la parte che quasi tutti saltano) — massimo 3 rami per sequenza al primo giro; chi parte, parte da tag semplici; non si personalizza ogni step, si cerca l'equilibrio con tempo e budget.
6. **Fuori scope dichiarato** — nessuna raccomandazione di piattaforma in questo file.

**Artefatto 2 — patch al kernel:** `.claude/skills/emails/SKILL.md`, ~6 righe dopo "Sequence Types Overview", con puntatore al file 1.

> Volutamente 6 righe e non 60: `emails/SKILL.md` è un file che LANCI potrebbe toccare in questi giorni. Superficie di conflitto minima, il contenuto sta nel file nuovo.

**Artefatto 3 — correzione:** `.claude/skills/revops/SKILL.md`, righe 202-206. Il callout "Gap identificato" diventa un cross-link onesto:

> *Fit ed engagement scoring sono già documentati qui sopra (§Lead Scoring). Quello che mancava è il **tag** come artefatto e la **ramificazione email** che lo consuma: vedi `emails/references/behavioral-branching.md`. Fonte: studio Andrei Pascu, outFunnel Lezione 15 (KA-04/05/06).*

**Effort: 1,5-2 ore.** Tre file, uno nuovo e due patch additive.

---

## 5. AP-018 — Framework a 10 livelli di maturità AI come tool d'agenzia

**Fonte:** cs2online Lezione 3, *"Livelli di utilizzo dell'intelligenza artificiale"*, Vimeo `1172370851`. **Lezione TEORICA, nessuna dimostrazione a schermo.** Analisi: `lessons/lezione-03/lesson-analysis.md` — 6 knowledge atoms, framework 0-10 riportato integralmente.

### 5.1 VERDETTO: NO-GO netto

Cinque ragioni, in ordine di peso.

**1. Il diagnostico d'onboarding di DE esiste già, ed è più forte di questo.**
`market-audit` produce: 5 subagent paralleli, punteggio pesato 0-100 (Content 25%, Conversion 20%, SEO 20%, Competitive 15%, Brand 10%, Growth 10%), grado A-F, quick wins / strategiche / lungo termine, stime di impatto revenue con tre scenari, tabella di confronto competitor, e un pass di verifica **live in browser** con due liste esplicite "Verificato dal vivo" / "Smentito dal vivo". Un secondo punteggio, su un asse scorrelato ("a che livello AI sei"), metterebbe due numeri in concorrenza nella stessa conversazione di vendita. Il cliente chiederà quale dei due conta. Non c'è una buona risposta.

**2. Il framework è il dispositivo di posizionamento di un concorrente, non uno strumento neutro.**
Il `lesson-analysis` lo dice esplicitamente, Pattern P1: *"la scala 0-10 non è solo didattica, è anche un meccanismo di auto-diagnosi che crea urgenza ('sei bloccato al 3, il corso ti porta al 5')"*. La scala è tarata **sulla destinazione che vende Andrei**. Adottarla significa adottare la sua definizione di progresso e la sua meta. DE finirebbe a competere nella sua categoria — formazione AI per business — con il suo strumento e la sua metrica.

**3. È anti-posizionato rispetto a DE.**
Il posizionamento di Digital Empire, da `CLAUDE.md`, è *"L'agenzia progettata per essere licenziata"* — autonomia del cliente, non dipendenza. Una scala che culmina al livello 7 con *"fine-tuning su dati propri + RAG, migliaia di €/mese in token API"* vende esattamente il contrario: una scalata infinita in cui il cliente ha sempre bisogno di salire di un gradino. Il framework spinge in direzione opposta al mandato.

**4. Fallisce T1, T2 e T3 insieme.**
- T1 (chi): nessun cliente d'agenzia nominato lo chiede. Zero richieste registrate.
- T2 (quando): nessuna data, nessun evento in calendario.
- T3 (costo del non farlo): **zero misurabile**. Nessun deal perso è attribuibile all'assenza di un assessment AI. Il costo del *farlo*, invece, è concreto: è un prodotto nuovo — pagine, logica di punteggio, copy, delivery, manutenzione — non un miglioramento di skill.

**5. `free-tools` contiene già il test che nessuno ha eseguito.**
La skill dice, testualmente: *"Lead value × expected leads &gt; build cost + maintenance"*. Nessuno ha mai messo un numero a sinistra della disuguaglianza per questa idea. Finché quel numero non esiste, non è una decisione: è entusiasmo.

**Bonus (T4):** singola lezione, singolo autore, **zero dimostrazioni** — la lezione è classificata TEORIA. Per la regola anti-overfitting già applicata dagli enrichment-report di DE, non basta nemmeno per una patch a una skill, figuriamoci per un prodotto.

### 5.2 L'unica obiezione seria al mio no-go, e perché non regge

C'è **un** posto in cui il framework non sarebbe scope creep: come **lead magnet / free tool davanti al Manuale Claude Code**, l'info-prodotto che compete frontalmente con Claude Speedrun 2. Lì il pubblico è giusto (chi vuole usare l'AI per lavoro), la meta è giusta (il Manuale porta dal livello 3 al 5), e il pattern P1 funzionerebbe a favore di DE.

Non regge lo stesso, per due motivi:

1. Quel terreno è del **fronte LANCI**, coperto dal Doom Bot A. Progettarlo qui produrrebbe due piani che si contraddicono sullo stesso asset.
2. **DE ha 25 pezzi finiti mai pubblicati, il più vecchio fermo da 135 giorni.** Aggiungere il pezzo 26 a un magazzino che non svuota è il fallimento documentato dall'ADR-016, ripetuto con più stile.

### 5.3 Cosa si fa invece — 10 minuti

**a) Una riga in `company/Memory/BACKLOG.md`**, con precondizione misurabile — non "da valutare":

> *AP-018 — assessment "a che livello AI sei" come free tool. NO-GO 2026-09-09 (piano AP). Si riapre solo se entrambe: (1) il Manuale Claude Code è lanciato e ha almeno una vendita registrata in `tesoreria/entrate.jsonl`; (2) qualcuno scrive il conto di `free-tools` con numeri veri: lead value × lead attesi &gt; costo di build + manutenzione. Fonte: cs2online Lezione 3 (KA-01).*

**b) Salvataggio gratuito — KA-02, che vale più del framework.**
L'atomo davvero utile della lezione non è la scala, è la diagnosi del pubblico:

> *Effetto Dunning-Kruger applicato all'AI: il 90% è bloccato ai livelli 1-3, si percepisce competente ma non ha risultati misurabili (non più vendite, non più views).*

Questo è **un input di copy**, non un prodotto: è la descrizione esatta del compratore del Manuale Claude Code nella sezione Problema di APSOC — uno che si sente bravo e non ha risultati. Costo di adozione: zero. Va segnalato al fronte LANCI/copy come nota, non costruito.

**c) Micro-item opzionale, bassa priorità (dichiarato come nice-to-have, non come GO):** KA-04 — *"se per un task piccolo l'AI fa peggio di te a mano, fallo a mano; il punto non è usare l'AI per usare l'AI"* — è un criterio operativo sano che oggi non è scritto da nessuna parte in casa. Sta bene in `free-tools` §"Worth the Investment" o in `workflow-automation`. Se un giro di critica lo taglia, non perdo niente.

---

## 6. AP-019 + AP-020 — I due pattern di prompt engineering

### 6.0 Correzione di premessa: dove vanno, visto che `skill-forge` non esiste

Il brief chiedeva di verificare se esistono `content-forge` o `skill-forge`. Risultato:

- **`skill-forge` non esiste.** La riga AP-019 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md` — *"valutare applicabilità a content-forge / skill-forge"* — punta a una skill inesistente. Va corretta nello stesso turno in cui si decide (REGOLA PUNTATORI).
- Esistono invece: `skill-builder` (tutorial generico sulla spec Anthropic, 911 righe, nessun gate specifico DE), `content-forge`, `content-forge2.0`, più `skill-creator` nel roster globale e `agent-factory`.
- L'**hub canonico** della forgia, per `company/Ecosistemi/07-FORGE/BACKBONE.md`, è: `skill-creator` + `content-forge` (MKD), con i gate `G-MKD`, `G-EVAL`, `G-CONTRADICTION`. Topologia a stella, *"tutto passa per l'hub… questo impedisce che due workflow producano artefatti divergenti dallo stesso ordine"*.

**Nota ironica ma seria:** proprio quell'hub oggi ha due copie identiche di sé stesso (`content-forge` / `content-forge2.0`, §7).

---

### 6.1 AP-019 — Il budget di sforzo segue il riuso, non la dimensione

**Fonte:** cs2online Lezione 6, *"Cucinando il tuo contesto"*, Vimeo `1172331550`, 12:25. **PRATICA**, 43 frame visionati. KA-04, workflow osservato per intero ai frame `t9m15s` / `t10m15s` / `t10m45s`.
**Fonte gemella:** cs2online Bonus 6, KA-08, frame `t19m30s`.

**Cosa c'è davvero dentro, oltre l'apparenza.** Letto male, AP-019 è "un convertitore PDF→JSON" — e come tale sarebbe un no-go immediato: DE non ha bisogno di un convertitore. Letto bene, KA-04 è una **regola di allocazione dello sforzo computazionale**, e la frase che la giustifica è la parte che conta:

> *usare Opus con Extended Thinking perché è un documento riusato indefinitamente — "se lo fai male, lo paghi ogni volta che lo usi"*

Accoppiata a KA-08 del Bonus 6 (`effort max` applicato **solo** allo step di validazione: *"Step 3: Validazione… utilizza expert per effort max"*, mentre lo Step 4 di generazione PDF non lo usa), si ottiene una regola sola, generalizzabile:

> **Lo sforzo si spende in proporzione a quante volte l'artefatto verrà riletto, non a quanto è grande il task. E dentro un task, si spende sullo step che valida, non su quello che produce.**

**Cosa ha DE oggi:** un routing a 3 tier (Haiku/Sonnet/Opus) presidiato da CFO e Cost Sentinel, e la gerarchia forze scagnozzo/sentinella/doom bot (ADR-015). Il criterio documentato è **il grado del compito**. Non esiste, in nessun punto letto, il criterio **"quante volte questo artefatto verrà riletto"**. Sono due assi diversi e il secondo manca.

**VERDETTO: GO — minimale.**

- T1 (chi): chiunque forgi una skill, un file reference, un set di token di brand, un system prompt — cioè `content-forge`, `skill-creator`, e ogni Doom Bot che scrive un documento canonico.
- T2 (quando): subito, costa mezz'ora.
- T3 (costo del non farlo): **debole, e lo dichiaro.** La spesa di token è reale ma non è mai stata misurata come incidente. Nessun caso registrato di "abbiamo usato il tier sbagliato su un file riusato".
- T4: due occorrenze indipendenti **dentro lo stesso corso** (L6 e Bonus 6), entrambe dimostrate a schermo, in contesti diversi (documento di contesto vs step di pipeline). Non è conferma esterna, ma è più solido di una singola menzione teorica.

**Spec concreta — un posto solo, 8 righe:**

File: `.claude/skills/content-forge/references/conventions/` — sezione aggiunta in `anti-patterns.md`, oppure nuovo file `effort-budget.md` se il primo è già denso (decidere aprendo il file; non ho letto quel file per intero, lo dichiaro).

```markdown
## Budget di sforzo: segue il riuso, non la dimensione

Prima di scegliere il modello/tier per uno step, rispondi a una domanda:
"quante volte questo artefatto verrà riletto da qui in avanti?"

- Artefatto usa-e-getta (un output di run, una bozza) → tier normale.
- Artefatto riusato indefinitamente (SKILL.md, file reference, token di brand,
  system prompt, schema) → massimo sforzo, una volta sola.
  "Se lo fai male, lo paghi ogni volta che lo usi."
- Dentro un task multi-step: il massimo sforzo va sullo step che VALIDA,
  non su quello che produce.

Fonte: studio Andrei Pascu, cs2online Lezione 6 (KA-04, workflow osservato per
intero) e cs2online Bonus 6 (KA-08, "effort max" solo sullo step di validazione).
```

**Effort: 20-30 minuti.** Nessun file nuovo se `anti-patterns.md` ha spazio.

**Nota di scoping, per non far crescere il candidato:** l'esempio applicativo naturale sarebbe un file unico di token di brand letto da PDF engine, Fabbrica Siti e caroselli. Oggi esiste `carousel-empire/brand/brand.json` (marca Digital Empire Agency, `#FF3D00`, Space Grotesk/Inter) e, separatamente, il brand CCM in `company/02-info-business/ccm/brand/` (`build_brand_guidelines.py` + HTML + PDF, `#fb4604`). Sono **marche diverse**, quindi non è un bug e **non propongo alcuna unificazione**: sarebbe un secondo progetto camuffato da esempio.

#### 6.2 Autocritica preventiva — perché AP-019 è il GO più debole

Lo dico io prima che lo dica il giro P1. AP-019 fallisce parzialmente T3: **non c'è un incidente misurato dietro.** È una regola plausibile, elegante, a costo quasi nullo — e le regole plausibili a costo quasi nullo sono esattamente il tipo di cosa che si accumula nei file finché nessuno li legge più. Il mio GO regge su un solo argomento: 30 minuti e 8 righe in un file di convenzioni già esistente sono sotto la soglia in cui vale la pena discutere. Se il giro di critica dice "regola senza incidente = rumore", **è una bocciatura legittima e non la difendo oltre.**

---

### 6.3 AP-020 — L'AI rifiuta se mancano dati obbligatori

**Fonte primaria:** cs2online Bonus 2, *"Come facciamo advertising report"*, Vimeo `1178254593`, 15:17. **PRATICA**, 25 frame. KA-04, osservato al frame `t12m15s`: step *"Validate all 4 required information pieces"* completato **prima** della generazione del PDF.
**Fonte gemella:** cs2online Bonus 6, KA-05, SKILL.md del concorrente trascritto verbatim dal frame `t14m00s`:

> *"Se queste info non entrano, chiederle all'utente e rifiutarsi categoricamente di procedere senza le seguenti documentazioni"*

**L'obiezione da sciogliere.** L'enrichment-report di quel run ha bloccato la patch così: *"Le 3 occorrenze sono però tutte interne allo stesso corso/autore — non conta come conferma cross-fonte indipendente per la regola anti-overfitting DE."*

**Ha ragione sul metodo, ma applica la regola alla cosa sbagliata.** L'anti-overfitting protegge da un *claim sul mondo* preso da una fonte sola (un benchmark, una soglia di prezzo, un tasso di conversione). Questo non è un claim sul mondo: è una **pratica ingegneristica**, e la conferma indipendente **DE ce l'ha già in casa**, sviluppata da sola:

- `proposal-gate` — *"BLOCCA, non suggerisce"*, 10 punti, 8 dei quali bloccanti.
- `content-forge` Stage 8 — check dichiarati bloccanti: `every_skill_has_min_3_references`, `every_agent_has_min_5_canonical_files`, `every_agent_md_min_400_words`.
- `ytf-niche-gate`, `ytf-qa-audio-video`, `ytf-seo-gate` — tutti BLOCCANO, tutti controlli indipendenti dal produttore.
- `market-report-pdf` usa già `reportlab`, la stessa tecnica del video, sviluppata indipendentemente (rilevato nell'enrichment-report bonus-02).

Quindi il pattern **non è nuovo per DE. È mal distribuito.** DE lo applica religiosamente ai **gate di uscita** e non lo applica quasi mai ai **contratti di ingresso**. Il costo di questa asimmetria è concreto: si produce un artefatto intero con dati incompleti, e lo si scopre alla fine.

**VERDETTO: GO — chirurgico, due file, non "tutte le skill".**

- T1 (chi): chi genera preventivi (`beast-preventivi`) e chi genera report PDF per clienti (`market-report-pdf`).
- T2 (quando): subito, è additivo.
- T3 (costo del non farlo): un documento intero scritto e poi bocciato dal gate a valle. In `beast-preventivi` significa scrivere un preventivo completo che `proposal-gate` respinge al punto 1 o al punto 3.
- T4: passa, per l'argomento sopra — conferma indipendente interna, quattro volte.

**Spec concreta — due patch, un divieto.**

**(a) `beast-preventivi/SKILL.md`** → è esattamente la Patch A già descritta in §3.4. Non si conta due volte: **AP-006 e AP-020 convergono sullo stesso intervento.** Motivo: il grep dell'enrichment-report bonus-06 aveva già confermato copertura zero proprio lì.

**(b) `.claude/skills/market-report-pdf/SKILL.md`** — promuovere il troubleshooting reattivo a validazione preventiva. Oggi, per l'enrichment-report bonus-02, la skill ha solo: *"Script produces empty PDF → Check that JSON data has all required fields"*. Cioè si scopre il dato mancante **guardando un PDF vuoto**. La patch:

```markdown
## Validazione a monte — prima di invocare lo script

Verifica che il JSON contenga tutti i campi obbligatori PRIMA di chiamare
`scripts/generate_pdf_report.py`. Se ne manca uno: fermati, dichiara quale
manca, chiedilo. Non generare un PDF parziale e non riempire un buco con
una stima.

Un report a un cliente con un numero inventato costa più di un report che
arriva un'ora dopo.

Fonte: studio Andrei Pascu, cs2online Bonus 2 (KA-04) — validazione dei 4 dati
obbligatori osservata a schermo PRIMA della generazione (frame t12m15s).
```

**(c) Il divieto — `discovery-call-brief` NON si tocca.**
Il suo "Gate check pre-output" segnala e **non blocca**, e quella è la scelta giusta: un brief incompleto è comunque informazione utile a valle, e il blocco vero sta in `proposal-gate`. Va scritto esplicitamente nel piano, altrimenti al prossimo giro di "uniformiamo i gate" qualcuno lo irrigidisce e rompe la catena. Le tre regole di DE sui dati mancanti, messe in fila, sono coerenti e diverse per un motivo:

| Skill | Comportamento su dato mancante | Perché è giusto così |
|---|---|---|
| `discovery-call-brief` | **Segnala** in `domande_irrisolte` | Il brief parziale serve comunque |
| `beast-preventivi` | **Rifiuta** il documento (l'outline sì) | Scrivere un documento che il gate boccerà è spreco puro |
| `proposal-gate` | **Blocca** l'invio | Ultimo controllo prima del cliente |

**Effort: 45-60 minuti**, di cui 30 già contati in AP-006.

**Perché NON si estende "a qualunque skill DE che genera output strutturati"**, come suggeriva la riga AP-020 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md`: una regola applicata ovunque diventa una regola che nessuno legge. Due skill dove il gap è stato **verificato con grep**, e basta. Le altre si patchano quando qualcuno mostra un caso reale.

---

## 7. Scoperte collaterali — non richieste, ma reali

Non fanno parte del piano. Vanno in BACKLOG, non nel lavoro di oggi (ADR-005: gli item minori non fermano la costruzione).

1. **`content-forge` e `content-forge2.0` sono byte-identici tranne il campo `name:`.** Verificato con `diff`: una sola riga diversa su tutto il file, `description` identica al carattere, quindi **trigger identici**. Due skill che si contendono le stesse frasi di attivazione, in un ecosistema (07-FORGE) il cui BACKBONE dichiara che la topologia a stella esiste *"perché due workflow non producano artefatti divergenti dallo stesso ordine"*. DE ha già la skill per diagnosticarlo: `skill-contradiction-analyzer`. → BACKLOG.

2. **`MIGLIORAMENTI-DIGITAL-EMPIRE.md`, riga AP-019, punta a `skill-forge` che non esiste.** Puntatore da correggere nello stesso turno della decisione (REGOLA PUNTATORI, `CLAUDE.md`).

3. **`revops/SKILL.md` righe 202-206 contengono un'affermazione falsa** ("non documentato in nessuna skill") smentita dalla stessa skill 100 righe sopra. Già dentro il piano come Artefatto 3 di AP-012.

4. **`tesoreria/entrate.jsonl` e `spese.jsonl` sono entrambi a zero righe.** Il reparto TESORERIA è nato per chiudere B-043 (*"Digital Empire non misura un solo euro"*), ma il registro è vuoto: lo strumento c'è, l'abitudine no. È il caso più puro di ULTIMO METRO applicato a un organo interno. → Fuori dal perimetro di questo piano, ma è la cosa più grave vista oggi.

---

## 8. Cosa NON si costruisce, e perché — riepilogo per il giro di critica

| Non si costruisce | Perché in una riga | Cosa lo riaprirebbe |
|---|---|---|
| Sistema AI di generazione preventivi | Il processo gira ~0 volte/mese; la lezione stessa (KA-01) dice di non automatizzare un processo non ripetuto | ≥4 preventivi reali/mese per 2 mesi in `A3-PREVENTIVI/handoffs/` |
| Assessment "a che livello AI sei" | `market-audit` copre già l'onboarding diagnostico; il framework è il posizionamento di un concorrente ed è anti-posizionato rispetto a "l'agenzia progettata per essere licenziata" | Manuale Claude Code lanciato e con almeno una vendita registrata + il conto di `free-tools` fatto con numeri veri |
| Ponte `beast-preventivi` ↔ `preventivo-auto` | Domini diversi: proposte d'agenzia vs riscrittura annunci auto mobile.de. Condividono una parola, non un problema | Niente. Non va costruito |
| Unificazione dei token di brand | Sono marche diverse (Digital Empire Agency vs CCM), non un bug | Un caso reale di divergenza fra due render della stessa marca |
| Estensione di AP-020 a "tutte le skill che generano output strutturati" | Una regola ovunque è una regola che nessuno legge | Un caso reale di output inventato in una terza skill |

---

## 9. Sequenza di esecuzione proposta

Tutto additivo, tutto in un'unica sessione, nessun file dell'ecosistema LANCI.

| # | Azione | File | Effort |
|---|---|---|---|
| 1 | Contratto d'ingresso (AP-006 A + AP-020 a, stesso intervento) | `beast-preventivi/SKILL.md` | 30 min |
| 2 | Chiusura tensione breakdown-prezzi (AP-006 B) | `beast-preventivi/references/stages/04-call-presentation.md` + `references/conventions/anti-patterns.md` + rimozione della frase "resta una scelta di Max" dal kernel | 30 min |
| 3 | Validazione a monte (AP-020 b) | `market-report-pdf/SKILL.md` | 15 min |
| 4 | Ramificazione comportamentale (AP-012) | nuovo `emails/references/behavioral-branching.md` + 6 righe in `emails/SKILL.md` | 60-90 min |
| 5 | Correzione callout falso (AP-012) | `revops/SKILL.md` righe 202-206 | 10 min |
| 6 | Budget di sforzo (AP-019) | `content-forge/references/conventions/` | 20-30 min |
| 7 | BACKLOG + puntatori | `company/Memory/BACKLOG.md`, `MIGLIORAMENTI-DIGITAL-EMPIRE.md` (AP-018 → NO-GO, AP-019 → correggere `skill-forge`) | 15 min |

**Totale: 3h20 – 4h20.**

**Rischio di collisione con Gael:** solo il punto 4 tocca un file (`emails/SKILL.md`) plausibilmente nel raggio di `TASK-LANCI-BUILD-W3`. Mitigato per costruzione: 6 righe nel kernel, tutto il contenuto in un file nuovo che non esiste ancora. Blocco COORDINAMENTO in `STATO-EMPIRE.md` non necessario per una superficie così piccola — ma è una valutazione che il giro P1 può ribaltare.

---

## 10. I punti deboli di questo piano — per i tre giri di critica

Li scrivo io, così P1 attacca questi e non deve prima trovarli.

1. **AP-019 fallisce parzialmente T3** (nessun incidente misurato dietro). Lo dichiaro in §6.2. Bocciarlo è legittimo.
2. **AP-012 giustifica T2 con LANCI**, che è il fronte dell'altro Doom Bot. Se il Doom Bot A ha già progettato un vocabolario di tag dentro LANCI, il mio Artefatto 1 diventa un doppione — **da riconciliare prima dell'esecuzione**, non dopo.
3. **La soglia "≥4 preventivi/mese per 2 mesi"** di AP-006 è scelta da me, non misurata. È difendibile (sotto quella soglia l'automazione non ripaga la manutenzione) ma resta un numero inventato, e va marcato come tale.
4. **La risoluzione della tensione breakdown-prezzi è una decisione di Max che sto prendendo io.** La difendo con ADR-028 e ADR-026, ma è una decisione presa per lui: va messa davanti a Max come *fatta*, non come *proposta*, e ribaltabile in dieci secondi.
5. **Non ho letto per intero** `beast-preventivi/references/conventions/anti-patterns.md` né `content-forge/references/conventions/anti-patterns.md`. Le due patch che li toccano vanno decise aprendo i file (aggiungere una sezione o creare un file nuovo). Lacuna dichiarata, non nascosta.
6. **Lo studio cs2online è al 50%** (20/40 lezioni). La **Lezione 12, "Come fare preventivi con Claude", non è ancora stata ingerita**, ed è dichiarata nella documentazione ufficiale come *"rilevante per la tensione aperta `beast-preventivi`"*. Il mio NO-GO su AP-006 potrebbe dover essere rivisto dopo quella lezione. **Lo dico prima**: chiudere L12 costa meno di costruire l'automazione, e va fatto prima di riaprire il candidato.

---

## 11. Fonti citate — tutte verificate oggi

**Materiale competitor**
- cs2online Lezione 3 — `runs/andrei-pascu-cs2online-001/lessons/lezione-03/lesson-analysis.md` (TEORIA, framework 0-10, KA-01/02/04, Pattern P1)
- cs2online Lezione 6 — `.../lezione-06/lesson-analysis.md` (PRATICA, 43 frame, KA-04 frame `t9m15s`/`t10m45s`)
- cs2online Bonus 2 — `.../bonus-02/lesson-analysis.md` (PRATICA, 25 frame, KA-04 frame `t12m15s`, KA-05 reportlab)
- cs2online Bonus 6 — `.../bonus-06/lesson-analysis.md` (PRATICA, 28 frame, KA-01/02/05/07/08, SKILL.md verbatim frame `t14m00s`)
- outFunnel Lezione 15 — `runs/andrei-pascu-armageddon-outfunnel-001/lessons/lezione-15/lesson-analysis.md` (KA-02/04/05/06/07, Pattern P1/P2)
- YouTube video 24 — `runs/andrei-pascu-001/cat1-copywriting/EBU57iVAutA/video-analysis.md` (KA-14 breakdown prezzi, `#00:06:32` + frame-210; KA-15 silenzio dopo il prezzo)
- Enrichment report `cs2online-bonus-06` e `cs2online-bonus-02` (i grep già eseguiti, la regola anti-overfitting applicata)
- `competitor/Andrei Pascu/MIGLIORAMENTI-DIGITAL-EMPIRE.md`, `CLAUDE-SPEEDRUN-2-DOCUMENTAZIONE-UFFICIALE.md`

**Skill Digital Empire lette per intero**
`beast-preventivi` (+ `references/stages/02-pricing.md`), `preventivo-auto`, `discovery-call-brief`, `proposal-gate`, `revops`, `emails`, `sales-enablement`, `market-audit`, `free-tools` (parziale), `content-forge`, `content-forge2.0` (diff), `skill-builder`, `ultimo-metro`, `brand-guidelines`

**Stato aziendale**
`company/Memory/tesoreria/entrate.jsonl` + `spese.jsonl` (entrambi vuoti), `company/Memory/STATO-EMPIRE.md`, `company/Memory/BACKLOG.md` (B-043), `company/Ecosistemi/07-FORGE/BACKBONE.md`, `company/01-agency/A3-PREVENTIVI/handoffs/`, ADR-005 / ADR-015 / ADR-016 / ADR-026 / ADR-028, `CLAUDE.md`

---

*Fine DRAFT V1. Destinato a P1 (critica del giro V1), P2 (critica di P1), P3 (critica di P2). Ogni giro attacca il giro precedente, non l'originale.*
