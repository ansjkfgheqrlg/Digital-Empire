---
Type: PROJECT
Status: Active
Tags: #lanci #ricognizione #L1 #ecosistema-14 #TASK-LANCI-ECO-W2
Created: 2026-09-02
Last updated: 2026-09-02
Autore: Gael (via Emperator)
Task: TASK-LANCI-ECO-W2 — sotto-task L1
---

# RICOGNIZIONE LANCI — cosa esiste davvero, misurato

> **Deliverable di L1.** Riga per riga: cosa fa / esiste davvero o è carta / si tiene, si
> assorbe o si butta / perché.
>
> **Regola di questo documento:** nessuna riga vale per fiducia. Ogni verdetto
> "esiste" o "è carta" porta accanto il **comando che lo dimostra**. Un PASS senza
> comando è un PASS finto, e qui non ne entra nessuno.

---

## 0. Il metodo — i comandi che hanno prodotto ogni verdetto

Eseguiti il 2026-09-02 dalla root del monorepo:

```bash
# inventario completo del reparto
find company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne -type f

# peso reale in righe
wc -l $(find <reparto> -name "*.md")

# prova di eseguibilità: quanti file NON sono documentazione
find <reparto> -type f \( -name "*.py" -o -name "*.ps1" -o -name "*.sh" \
     -o -name "*.json" -o -name "*.yaml" \) | wc -l

# prova di ufficialità degli agenti: compaiono in /agents?
ls .claude/agents/ | grep -iE "ib-|lanc"

# prova di esistenza del namespace di stato
find . -maxdepth 6 -type d -path "*infobusiness/lanci*"

# prova di esistenza delle skill dichiarate
ls .claude/skills/<nome>/SKILL.md
```

---

## 1. Il verdetto in una riga

Il reparto Lanci esiste **su carta e basta**: **2.377 righe** di documentazione,
**19 file**, **0 file eseguibili**, **0 agenti ufficiali**, **0 stato mai scritto**.

Descrive perfettamente un lancio che **nessun comando sa avviare**.

> **Correzione all'audit di partenza:** la task diceva *1.805 righe*. Rimisurate oggi
> con `wc -l` sono **2.377**. Il numero non cambia il verdetto — lo peggiora: sono
> 572 righe in più di descrizione, non una riga in più di esecuzione.

---

## 2. IB-L2-LANC — riga per riga

Percorso: `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/`

### 2.1 Struttura e dottrina

| File | Righe | Cosa fa | Esiste o è carta | Destino | Perché |
|---|---:|---|---|---|---|
| `ARCHITETTURA.md` | 196 | Namespace memoria, confini del reparto, handoff | 📄 **Carta** — descrive `infobusiness/lanci/`, che non esiste | **Si assorbe** | I confini e gli handoff sono ragionati bene: diventano §1 dell'ecosistema 14 |
| `README.md` | 152 | Missione del reparto, roster, indice | 📄 **Carta** | **Si assorbe** | La missione regge; il roster va rifatto perché gli agenti non sono ufficiali |
| `principi/PRINCIPI.md` | 90 | Principi di lancio | 📄 **Carta** | **Si tiene** | Dottrina pura: non deve essere eseguibile per valere |
| `regole/REGOLE.md` | 117 | Regole R1-R*, incluso R6 (delta budget >10% → BLOCK) | 📄 **Carta** | **Si tiene, va reso gate** | Le regole ci sono ma **nessuno le applica**: non c'è codice che le legga |
| `kpi/KPI.md` | 69 | KPI del lancio | 📄 **Carta** | **Si assorbe** | I KPI vanno agganciati al debrief eseguibile, oggi non misurano niente |

### 2.2 I 9 agenti — il difetto più grave

| Agente | Righe | Esiste o è carta | Destino |
|---|---:|---|---|
| `IB-COORD-LANCI` | 136 | 📄 Carta | Si assorbe → conductor dell'Esecuzione Lancio |
| `IB-LANC-QA` | 134 | 📄 Carta | Si assorbe → gate |
| `IB-LANC-WEBINAR` | 129 | 📄 Carta | Si assorbe |
| `IB-LANC-DEBRIEF` | 129 | 📄 Carta | Si assorbe |
| `IB-LANC-COPY-LIAISON` | 129 | 📄 Carta | Si assorbe → reparto Copy |
| `IB-LANC-PLANNER` | 128 | 📄 Carta | Si assorbe |
| `IB-LANC-ASSET` | 128 | 📄 Carta | Si assorbe |
| `IB-LANC-DRY` | 125 | 📄 Carta | Si assorbe → gate dry-run |
| `IB-LANC-TRACKER` | 123 | 📄 Carta | Si assorbe |

**La prova:**

```bash
$ ls .claude/agents/ | grep -iE "ib-|lanc"
       # nessun risultato
$ ls .claude/agents/*.md | wc -l
124    # 124 agenti ufficiali nell'Impero, zero di questi 9
```

**Cosa significa davvero.** Questi non sono agenti: sono **schede di agenti**.
1.161 righe che descrivono nove ruoli che Claude Code **non può invocare**, perché non
stanno in `.claude/agents/` col frontmatter valido. È esattamente il difetto che
ADR-008 vieta e che il 2026-08-31 aveva colpito 120 file: *funziona ≠ ufficiale*, e
qui non funziona nemmeno.

### 2.3 I workflow — la parte migliore

| File | Righe | Cosa fa | Esiste o è carta | Destino |
|---|---:|---|---|---|
| `workflow/WF-LANCIO.md` | 152 | Lancio T-30→T+7: trigger, input JSON, pipeline+owner, gate, output JSON, handoff, dry-run T-1, esempio | 📄 **Carta, ma di qualità** | **Si tiene quasi intero** |
| `workflow/WF-WEBINAR.md` | 144 | Funnel webinar + replay | 📄 **Carta** | **Si tiene** |

**Perché WF-LANCIO si salva.** Ha già la forma giusta: `Input JSON` → `Pipeline + owner`
→ `Gate` → `Output JSON` → `Handoff` → `Dry-run obbligatorio`. È la stessa anatomia del
flusso KDP che funziona. **Gli manca una cosa sola: il comando che lo esegue.**
È lo scheletro corretto di L4, non un documento da riscrivere.

### 2.4 Gli script — tre fantasmi dichiarati

`scripts/README.md` (71 righe) dice testualmente **"Script pianificati (build in V2)"**:

| Script dichiarato | Scopo dichiarato | Esiste |
|---|---|---|
| `launch_calendar.py` | Calendario T-30→T+7 deterministico | ❌ **No** |
| `dry_run_costs.py` | Costi dry-run T-1 + delta budget, PASS/BLOCK per R6 | ❌ **No** |
| `launch_debrief_diff.py` | Scarto piano vs reale per KPI, flag root-cause ≥10% | ❌ **No** |

```bash
$ find <reparto> -type f \( -name "*.py" -o -name "*.ps1" -o -name "*.sh" \
       -o -name "*.json" -o -name "*.yaml" \) | wc -l
0
```

**Destino: si tengono le SPECIFICHE, si buttano le promesse.** Le tre schede contengono
input, output e prerequisiti già definiti bene — sono spec pronte, non vaporware
concettuale. Diventano i tre eseguibili di L4. Ma finché il README dice "pianificato"
senza data e senza owner, quel file **mente per omissione** e va sostituito.

### 2.5 Lo stato — schema perfetto, zero righe

`state/README.md` (145 righe) definisce 4 namespace: `infobusiness/lanci/{lancio-id}/`,
`/webinar/`, `/libreria-evergreen/`, `infobusiness/reasoningbank/`. Con owner di scrittura
e lettori per ognuno.

```bash
$ find . -maxdepth 6 -type d -path "*infobusiness/lanci*"
       # nessun risultato — mai creato, nessun lancio mai tracciato
```

**Destino: lo schema si tiene** (è progettato bene e coerente col BRAIN), **la sua
inesistenza è il punto**. Zero lanci tracciati significa zero storico, zero ReasoningBank,
zero pattern distillati. Il reparto non ha mai girato nemmeno una volta a vuoto.

### 2.6 Le skill del reparto — una P0 mai forgiata

`skills/SKILLS.md` (80 righe) dichiara `launch-runbook` **Priorità P0**, "da forgiare via
07-FORGE".

```bash
$ ls .claude/skills/ | grep -iE "launch|lancio"
launch                      # skill generica installata, NON è launch-runbook
market-launch
script-video-lancio-ccm
youtube-channel-launch
```

**`launch-runbook` non esiste.** Le tre skill trovate sono altre cose. **Destino: la spec
si assorbe in L5**, ma va detto chiaro che una P0 dichiarata il 2026-06-21 è ancora a zero
dopo due mesi e mezzo.

---

## 3. Cosa esiste DAVVERO e si può usare subito

Qui il quadro si ribalta. Fuori dal reparto, **eseguibile e installato**, c'è già molto:

| Skill | `SKILL.md` presente | Reparto di destinazione (L3) |
|---|---|---|
| `launch` | ✅ | Esecuzione Lancio |
| `ads` | ✅ | Marketing & Traffico |
| `ad-creative` | ✅ | Marketing & Traffico |
| `cro-copy-architect` | ✅ | Copy |
| `empire-premium-style` | ✅ | Siti & Funnel |
| `site-build` | ✅ | Siti & Funnel |
| `site-copy` | ✅ | Siti & Funnel |
| `site-deploy` | ✅ | Siti & Funnel |
| `pricing` | ✅ | Pricing & Offerta |
| `signup` | ✅ | Siti & Funnel |
| `paywalls` | ✅ | Pricing & Offerta |

Verifica: `ls .claude/skills/<nome>/SKILL.md` per ognuna — **11 su 11 presenti**.

**Conseguenza per L3/L5, ed è la più importante di tutta la ricognizione:** l'ecosistema
14-LANCI **non deve costruire da zero** sei reparti su otto. Deve **cablare skill che
esistono già** dentro un flusso che oggi non c'è. Il buco non è la capacità — è
l'orchestrazione.

---

## 4. Numerazione ecosistema

```bash
$ ls company/Ecosistemi/
01-AGENCY  02-INFO-BUSINESS  03-CONTENT-FACTORY  04-MARKETING  05-MULTI-BUSINESS
06-PLATFORM  07-FORGE  08-INTELLIGENCE  09-OPERATIONS  10-MEMORY
11-APEX-7-CORE  12-STREAM-S7-BOT  13-ARENA-APEX
```

**`14-LANCI` confermato**: l'ultimo occupato è 13. ⚠️ **Nessuna cartella creata** — la
regola della task è esplicita, si crea solo dopo l'ok di Max.

---

## 5. Bilancio finale

| Metrica | Valore misurato |
|---|---|
| File totali nel reparto | **19** |
| Righe di documentazione | **2.377** |
| File eseguibili | **0** |
| Agenti ufficiali in `/agents` | **0 su 9** |
| Script esistenti su dichiarati | **0 su 3** |
| Skill di reparto forgiate su P0 | **0 su 1** |
| Namespace di stato creati | **0 su 4** |
| Lanci mai tracciati | **0** |
| Skill esterne pronte all'uso | **11 su 11** |

**Si tiene:** PRINCIPI, REGOLE, WF-LANCIO, WF-WEBINAR, schema state, spec dei 3 script.
**Si assorbe:** ARCHITETTURA, README, KPI, i 9 agenti (come ruoli, da riscrivere ufficiali).
**Si butta:** ogni dichiarazione "pianificato / da forgiare" senza data e owner — è la
forma che ha permesso a questo reparto di sembrare vivo per due mesi e mezzo.

---

## 6. Cosa passa a L2

L2 assorbe il **contenuto** dei progetti vecchi. Da questa ricognizione porta con sé
tre vincoli:

1. **Non copiare la forma di IB-L2-LANC.** Ha prodotto 2.377 righe e zero esecuzione.
   Ogni pezzo che entra in L3 deve nascere con il comando che lo prova.
2. **L'orchestrazione è il deliverable, non le capacità.** Con 11 skill già installate,
   il valore di 14-LANCI sta nel flusso che le mette in fila, non in nuovi strumenti.
3. **ADR-003 vale su WF-LANCIO.** Si sposta e si avvolge, non si riscrive.

---

## Connessioni

- [[ASSORBIMENTO-LANCI]] — L2, prossimo passo
- [[26-ECOSISTEMA-LANCI]] — L3/L4/L5, da scrivere
- `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md` — wrap, non riscrittura
- `company/Memory/decisions/ADR-008` — nessun artefatto orfano: qui violato su 9 agenti
- `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md` — la task madre
