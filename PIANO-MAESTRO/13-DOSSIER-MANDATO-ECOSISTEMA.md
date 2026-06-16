# ⚖️ 13 — MANDATO-ECOSISTEMA (il governo che fa rispettare la Costituzione)

> Dossier v2 (fase V2-2, ADR-007). Blueprint dell'ecosistema-Mandato da costruire in **V2-5**.
> Fonte vincolante: `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md` §3-4 + corpus reale di Max
> (`company/Memory/maximilian-corpus/`). Standard struttura: CF-grade (§0 del piano V2).
> Versione: 1.0 · Creato: 2026-06-16 · Stato: progettato (build in V2-5).

---

## 0. Missione + DONE WHEN

**Missione.** Il Mandato v1 è un documento di Articoli (`company/Mandato/MANDATO-EMPIRE.md`):
la Costituzione di Digital Empire. È giusto, ma — parole di Max (corpus) — *"adesso è più
piccolo di un reparto. Deve diventare un GIGANTE, potentissimo, perché deve controllare tutto,
anche le Sentinelle."* Questo dossier progetta la trasformazione: **da documento a ECOSISTEMA
di governo** che fa VIVERE, RISPETTARE ed EVOLVERE gli Articoli.

Distinzione netta (non ridondante con MAXIMILIAN, dossier 12):
- **Mandato = la LEGGE.** Cosa è lecito/illecito. Enforcement, blocco, Sentinelle.
- **MAXIMILIAN = lo STANDARD.** Cosa è all'altezza, cosa Max vorrebbe. Direzione e ambizione.
Un output può essere lecito ma non all'altezza (e viceversa). In conflitto: il Mandato prevale
sul lecito/illecito; MAXIMILIAN sullo standard/scala.

**DONE WHEN (misurabili) — la build V2-5 è completa quando:**
1. Gli Articoli 1-7 restano INVARIATI come cuore (ADR-003: wrap, non riscrittura) — solo Max
   li modifica via ADR. L'ecosistema li avvolge, non li tocca.
2. Esiste un **team custodi ≥6 agenti** a schede millimetriche (standard §0 piano V2).
3. Esistono ≥3 workflow CF-grade: WF-ENFORCEMENT, WF-EVOLUZIONE, WF-AUDIT-PERIODICO.
4. L'**enforcement-lead comanda le 5 Sentinelle** (catena di comando esplicita e tracciata).
5. Lo script di **contradiction-check automatico** gira: ogni nuovo ADR/output viene verificato
   contro gli Articoli prima di passare.
6. State + namespace memoria dedicati; ogni violazione e ogni evoluzione tracciata.
7. Test reale: un output che viola un Articolo (es. claim senza proof, dependency-language)
   viene BLOCCATO dal workflow di enforcement, con citazione dell'Articolo violato.

**OUT OF SCOPE.** L'ecosistema-Mandato non RISCRIVE gli Articoli (solo Max, via ADR), non
definisce lo standard di scala/qualità (quello è MAXIMILIAN), non esegue il lavoro degli
ecosistemi. Fa rispettare e propone evoluzioni — non comanda la strategia.

---

## 1. Cosa resta invariato — gli Articoli sono il cuore (wrap, non riscrittura)

I 7 Articoli del Mandato v1 restano la fonte costituzionale, INVARIATI:

| Art. | Tema | Invariante chiave |
|---|---|---|
| 1 | Identità e Posizionamento | "L'agenzia progettata per essere licenziata" — autonomia cliente |
| 2 | Brand Voice | "Prove non promesse" — CPB, mai claim senza evidenza |
| 3 | Offerta e Pricing | listino fisso, one-time €0 canoni, codice del cliente |
| 4 | Qualità | gate non bypassabili (0 bypass per definizione) |
| 5 | Memory/Wiki-first | memory-first + wiki fonte di verità |
| 6 | Multi-tenant | brand_kit + icp input obbligatori |
| 7 | Sicurezza | zero segreti nel repo, PII protetta |

**L'ecosistema NON li riscrive: li rende eseguibili, vigilati ed evolutivi.** Gli Articoli sono
la legge scritta; l'ecosistema è il tribunale + la polizia + il legislatore-proponente attorno ad essa.

---

## 2. Team custodi (≥6 agenti — schede a build V2-5)

Convenzione id: `MND-<ruolo>`. Tier: opus per interpretazione/enforcement critico, sonnet per
analisi e storico.

| ID | Ruolo | Tipo | Tier | Funzione in una frase |
|---|---|---|---|---|
| `MND-INTERPRETE` | Interprete del Mandato | coordinator | opus | Risolve "questo output viola l'Articolo X?" — l'autorità di lettura |
| `MND-CONFORMITA` | Analista di conformità | worker | sonnet | Scansiona output/ADR/decisioni e misura aderenza agli Articoli |
| `MND-EVOLUTORE` | Aggiornatore | worker | opus | Propone evoluzioni degli Articoli come ADR (mai cambia da sé) |
| `MND-ENFORCEMENT` | Enforcement-lead | coordinator | opus | Comanda le 5 Sentinelle; decide blocco/escalation |
| `MND-STORICO` | Storico | worker | sonnet | Custodisce versioni Articoli, precedenti di violazione, ADR collegati |
| `MND-VERIFICA` | Verificatore | worker | sonnet | Controlla che i blocchi siano stati applicati e le correzioni eseguite |

**Gerarchia interna.** `MND-INTERPRETE` è l'autorità di lettura (cosa dice l'Articolo nel caso
concreto). `MND-ENFORCEMENT` è l'autorità d'azione (comanda le Sentinelle, applica il blocco).
I due coordinator si dividono lettura vs azione; gli altri 4 sono specialisti. Ogni scheda
(build V2-5) segue lo standard millimetrico §0: identità, responsabilità, I/O JSON, logica
passo-passo, KPI, escalation, esempi reali di giudizio costituzionale.

---

## 3. Workflow CF-grade (≥3)

### WF-ENFORCEMENT (violazione → blocco → escalation)
Il cuore operativo. Innescato da ogni output destinato all'esterno o ogni decisione di policy.

```
Input: output/decisione + contesto (ecosistema, tipo, brand_kit)
  │
  ├─ MND-CONFORMITA: scan automatico vs Articoli (script contradiction-check, §5)
  ├─ se sospetta violazione → MND-INTERPRETE: lettura del caso vs Articolo specifico
  ├─ violazione confermata → MND-ENFORCEMENT: BLOCCO + dispatch alla Sentinella competente
  │     (Art.2 Brand Voice → Brand-Voice Sentinel · Art.4 Qualità → Quality · Art.7 → Security…)
  └─ MND-VERIFICA: conferma che il blocco sia stato applicato e la correzione eseguita
Output: { verdetto: "CONFORME" | "VIOLAZIONE", articolo, citazione, azione, sentinella }
```
**Regola di blocco:** come da Art.4.1, i gate NON sono bypassabili. Unica deroga: Board via
hive-mind raft, depositata in `Memory/decisions/`. L'enforcement è cieco al rango: blocca anche
il Board (Art.2.2 lo dice esplicito).

### WF-EVOLUZIONE (gli Articoli si aggiornano senza tradirsi)
Il Mandato deve "sempre aggiornarsi" (corpus). Ma solo Max modifica gli Articoli (Art. preambolo).

```
MND-CONFORMITA/MND-STORICO rilevano un gap o una tensione ricorrente
  → MND-EVOLUTORE redige una PROPOSTA come ADR (contesto, modifica, conseguenze,
    contradiction-check vs Articoli esistenti)
  → approvazione MAX (delega: NO — gli Articoli sono di Max)
  → pubblicazione: aggiorna MANDATO-EMPIRE.md + ADR in Memory/decisions/ + notifica via bus
```
Nessuna evoluzione silenziosa: ogni cambio di Articolo lascia traccia ADR (Art.5.3).

### WF-AUDIT-PERIODICO (controllo proattivo, non solo reattivo)
Cadenza schedulata (via 09-OPERATIONS). MND-CONFORMITA campiona output recenti di tutti gli
ecosistemi e misura il tasso di conformità per Articolo → report al Board + a MAXIMILIAN.
Trova le derive PRIMA che diventino incidenti (es. drift progressivo del brand voice).

---

## 4. Comando sulle Sentinelle (la catena di enforcement)

Le 5 Sentinelle (Cost, Quality, Drift, Security, Brand-Voice) sono il braccio operativo del
Mandato. In v2 ognuna è multi-workflow (§4 piano V2), ma la **catena di comando** è qui:

| Sentinella | Articolo che fa rispettare | Trigger di blocco |
|---|---|---|
| Brand-Voice | Art.2 (prove non promesse) | claim senza proof, AI-slop, dependency-language |
| Quality | Art.4 (gate) | score APSOC < soglia, P dopo S, gate tentato bypass |
| Security | Art.7 (segreti/PII) | segreto in commit, PII in output esterno |
| Cost | Art.4.3 (dry-run prima di spendere) | spesa API senza dry-run/ok |
| Drift | Art.5.2 (wiki fonte di verità) | lag sync wiki↔AgentDB > 24h, deriva da Memory |

`MND-ENFORCEMENT` è il loro comandante: riceve i segnali, coordina i blocchi cross-Sentinella,
gestisce le escalation (CTO → CEO per Security; CMO per Brand/Quality). Le Sentinelle vigilano
in continuo; il Mandato decide cosa fare quando scatta più di una.

---

## 5. Skill proprie + script (forgia/scrivi in V2-5)

| Asset | Tipo | Scopo |
|---|---|---|
| `mandato-contradiction-check` | skill + script .py/.ps1 | verifica automatica di un output/ADR contro i 7 Articoli; ritorna CONFORME/VIOLAZIONE + articolo |
| `mandato-enforcement-gate` | skill | checklist eseguibile del WF-ENFORCEMENT (la Checklist Brand Gate del Mandato v1, resa eseguibile) |
| `mandato-evolution-adr` | skill | redige una proposta-ADR di evoluzione di un Articolo con contradiction-check incorporato |

Lo script `mandato-contradiction-check` è il pezzo più importante: rende l'Art.5.3
("contradiction-check contro gli ADR attivi") un controllo reale e automatico, non una buona intenzione.

---

## 6. Relazione con MAXIMILIAN, Board, ADR

- **MAXIMILIAN (dossier 12, LX accanto):** Mandato = legge; MAXIMILIAN = standard. Lavorano in
  coppia ai confini di una fase: il Mandato verifica che sia *lecito*, MAXIMILIAN che sia
  *all'altezza*. Entrambi possono bloccare, per ragioni diverse.
- **Board C-Suite (L0, sotto):** esegue. Il Mandato lo vincola come chiunque (Art.2.2: blocca
  anche il Board). Il Board può derogare solo via raft documentato (Art.4.1).
- **ADR (Memory/decisions/):** il canale unico di evoluzione costituzionale. WF-EVOLUZIONE
  produce ADR; nessun Articolo cambia senza ADR + ok Max.

---

## 7. State + memoria

- **Namespace AgentDB:** `mandato/` — `mandato/violazioni` (ogni blocco: output, articolo,
  citazione, azione, esito), `mandato/conformita` (tasso di aderenza per Articolo per ecosistema,
  dai WF-AUDIT), `mandato/evoluzioni` (proposte ADR e loro esito), `mandato/precedenti` (casi
  interpretativi risolti — giurisprudenza interna).
- **State per esecuzione:** ogni enforcement e ogni audit producono un record ripartibile a
  freddo (test amnesia §6 piano V2).
- **ReasoningBank:** i pattern di violazione ricorrente alimentano la conoscenza corporate — gli
  ecosistemi imparano gli Articoli PRIMA di sbatterci contro (enforcement che educa, non solo punisce).

---

## 8. Build plan (V2-5, ciclo a 9 passi + review 5-bis MAXIMILIAN)

| Passo | Cosa |
|---|---|
| RECALL | questo dossier + MANDATO-EMPIRE.md (Articoli invariati) + §3-4 piano V2 |
| SPEC | DONE WHEN §0 (Articoli intatti, 6 custodi, 3 workflow, comando Sentinelle, contradiction-check) |
| PRE-MORTEM | rischio #1: l'ecosistema "riscrive" gli Articoli invece di avvolgerli → contromisura: Articoli read-only, solo WF-EVOLUZIONE via ADR+Max. Rischio #2: enforcement che blocca tutto e paralizza → soglie calibrate, minuzie in BACKLOG (ADR-005). Rischio #3: sovrapposizione con MAXIMILIAN → confine netto legge/standard (§6) |
| BUILD | swarm: custodi + 3 workflow + skill/script — architettura con skill §8 piano V2 |
| GATE | Articoli invariati (diff = 0); 6 custodi a schema; contradiction-check eseguibile; comando Sentinelle tracciato |
| REVIEW | indipendente sul contenuto vs Articoli |
| **5-bis** | REVIEW MAXIMILIAN ("Max approverebbe questo governo?") — attivo da V2-3 in poi |
| COMMIT | CP + STATO + wiki/log + push |
| RETRO | lezioni → ReasoningBank; pattern di violazione → educazione ecosistemi |

V2-5 costruisce, nello stesso blocco, anche le Sentinelle multi-workflow (§4) e le Guilds v2 (§5).

---

## 9. Connessioni

- [[11-PIANO-V2-DIRETTIVA-SCALA]] §3-4 — la direttiva che istituisce l'ecosistema-Mandato (fonte)
- `company/Mandato/MANDATO-EMPIRE.md` — i 7 Articoli (il cuore invariato che questo ecosistema avvolge)
- [[12-DOSSIER-MAXIMILIAN]] — l'organo dello standard (coppia legge/standard, §6)
- [[10-METODO-CICLO-FASE]] — ciclo a 9 passi + review 5-bis
- ADR-007 (pivot V2) · ADR-003 (wrap: Articoli non si riscrivono) · ADR-002 (memory-first) · ADR-005 (minuzie → BACKLOG)
- [[00-PIANO-MAESTRO]] — gerarchia LX→L5 (Mandato resta LX, ora come ecosistema di governo)
- `company/Sentinels/` — le 5 Sentinelle comandate dall'enforcement-lead (§4)
