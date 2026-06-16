# BLUEPRINT SKILL — maximilian-standard-gate

> Questo è il BLUEPRINT (la STRUTTURA che la FORGE costruirà), NON la skill finale.
> Forma: Skill (Schema-Skill canonico). Slug: `maximilian-standard-gate` (kebab, == cartella).
> Scopo: rende MAXIMILIAN un GATE REALE e non una descrizione — checklist BINARIA/VERIFICABILE,
> applicabile da chiunque, deterministica dove possibile. È la skill eseguita al passo 5 di
> [[WF-REVIEW-MAXIMILIAN]]. Fonte: `12-DOSSIER-MAXIMILIAN.md` §1 (gli 8 test) · §4 (skill).

---

## Quando si usa
- **USA** al passo 5-bis del ciclo a 9 passi: dato un deliverable di fase, eseguire la checklist
  degli 8 test §1 come voci binarie → emettere `APPROVA | RIFAI` bloccante.
- **USA** quando il conductor (fino a V2-3, manualmente) deve applicare lo standard di Max in modo
  ripetibile e non opinabile.
- **NO se** serve riscrivere/giudicare il TONO di un testo → `maximilian-voice`. NO se serve
  ANTICIPARE cosa Max vorrà → WF-ANTICIPAZIONE. Questa skill GIUDICA la forma+scala, non la voce.
- Trigger description (3ª persona): *"Esegue il review-gate di standard di Max sugli 8 test
  (Scala, Standard chirurgico, Visibilità, Velocità, Ambizione, Delega, Anticipazione, fai-di-più)
  come checklist binaria e ritorna APPROVA/RIFAI bloccante. Use when 'gate Max', 'Max approverebbe',
  'review 5-bis', deliverable di fase da validare. DO NOT use for riscrivere testi nella voce di Max
  (vedi maximilian-voice)."*

---

## Struttura (SKILL.md + references + evals)
```
maximilian-standard-gate/
├── SKILL.md                 # kernel ≤500 righe: frontmatter + la checklist binaria degli 8 test
├── references/
│   ├── tests/the-8-tests.md         # i test §1, ognuno con criterio binario + come si verifica
│   ├── processes/scoring.md         # regola di aggregazione: 1 FAIL bloccante = RIFAI
│   └── conventions/anti-patterns.md # "suona come Claude", giudizio a sensazione, minuzia bloccante
├── scripts/gate_check.py            # logica deterministica dove possibile (conteggi, presenza file)
├── evals/evals.json                 # ≥4 prompt (≥1 negativo: NON deve attivarsi)
└── README.md                        # installazione + uso
```
Kernel `SKILL.md` contiene la CHECKLIST eseguibile (sotto). `scripts/gate_check.py` automatizza
i check oggettivi (T2/T3/T5 in parte): conta file, righe, cartelle vuote, stub/TODO; emette JSON.

### La checklist binaria (cuore del gate — ogni voce è SÌ/NO verificabile)
| # | Test §1 | Voce binaria verificabile | Bloccante |
|---|---|---|---|
| T1 | **Scala** | L'unità è dimensionata "azienda/componente v2", NON "automazione/giocattolo"? (es. una figura-chiave NON è un singolo agente/file) | SÌ |
| T2 | **Standard chirurgico** | 0 reparti/figure rappresentati da un SOLO file .md? 0 file <15 righe? 0 stub/TODO/placeholder? *(deterministico via script)* | SÌ |
| T3 | **Visibilità totale** | La struttura è VISIBILE nell'albero (cartelle+file navigabili), 0 cartelle vuote, niente conoscenza implicita? *(deterministico via script)* | SÌ |
| T4 | **Velocità senza minuzie** | I rilievi-minuzia sono finiti in BACKLOG e NON hanno fermato il BUILD? (un FAIL qui = ci si è impantanati) | NO* |
| T5 | **Ambizione disciplinata** | La fase fa il MASSIMO possibile per il suo scope (non il minimo)? conteggi attesi del dossier raggiunti? | SÌ |
| T6 | **Delega aggressiva** | Dove un team può decidere, decide il team (non si è chiamato Max per ciò che è delegato)? | NO* |
| T7 | **Anticipazione** | Gli slot anticipati da WF-ANTICIPAZIONE sono stati onorati (o motivatamente rimandati a BACKLOG)? | SÌ |
| T8 | **"Fai di più del chiesto"** | È stato fatto anche l'ovvio non detto, o SOLO il letterale della richiesta? | SÌ |

\* T4/T6 non bloccano da soli ma alzano una nota; due note → escalation a MX-PRIME.

### Regola di scoring (deterministica)
`RIFAI` se ≥1 test **Bloccante** = FAIL (non-minuzia). Altrimenti `APPROVA`. Nessuna media,
nessun "quasi": il gate non negozia (come il Gate Bibbia). Output JSON identico a WF-REVIEW §Output.

---

## Checklist completezza (per struct-gate)
- [ ] `SKILL.md` con frontmatter `name: maximilian-standard-gate` + `description` (COSA+QUANDO+trigger+DO NOT).
- [ ] La checklist degli 8 test è nel kernel, ogni voce BINARIA (SÌ/NO), con marcatura bloccante.
- [ ] `references/` ≥3 file, ≥300 righe totali (tests + scoring + anti-patterns).
- [ ] `scripts/gate_check.py` automatizza i check oggettivi (T2/T3/conteggi T5) → JSON.
- [ ] `evals/evals.json` ≥4 prompt, ≥1 negativo (un deliverable VALIDO deve dare APPROVA, non RIFAI).
- [ ] `README.md` con installazione + uso. Nessun placeholder nel kernel.

---

## Esempio
Deliverable: cartella "reparto Ricerca" = 1 solo file `ricerca.md` di 40 righe.
→ T1 FAIL (è un giocattolo, non un'azienda) · T2 FAIL (figura = 1 .md) · T3 FAIL (niente team/workflow
visibili nell'albero) · T5 FAIL (sotto i conteggi attesi: 0 agenti dei 6-10 richiesti dal corpus §34).
Scoring: 4 bloccanti FAIL → **RIFAI**. Motivo dal corpus §32-38. Stesso esito che darebbe Max.

---

## Anti-pattern
- Giudizio "a sensazione" non riconducibile a una voce binaria → il gate diventa opinione (vietato).
- Far bloccare il gate su una minuzia (viola T4/ADR-005): le minuzie vanno in BACKLOG, non bocciano.
- Kernel che descrive i test ma non li rende ESEGUIBILI (checklist non binaria) → non è un gate, è prosa.
- `description` senza trigger/DO NOT → la skill non si attiva (P15).
- Verdetto che "suona come Claude gentile" invece che come Max → è compito di maximilian-voice, non qui;
  ma il gate non deve ammorbidire un FAIL in "suggerimento".

---

## Connessioni
- [[WF-REVIEW-MAXIMILIAN]] — esegue questa skill al passo 5 (è il motore del verdetto)
- [[maximilian-voice]] — confeziona il verdetto di questo gate nella voce di Max
- [[Schema-Skill]] — la forma canonica che la FORGE seguirà per costruirla
- [[12-DOSSIER-MAXIMILIAN]] §1 (gli 8 test = queste voci) · §4 (skill) · §0.7 (test reale = l'esempio)
- ADR-005 (minuzie → BACKLOG = test T4) · ADR-006 (ciclo) · ADR-007 (pivot V2)
