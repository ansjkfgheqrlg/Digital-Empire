# SCHEMA CANONICO — Ecosistema

> Forma PIÙ PESANTE. Un'intera area autonoma della holding (livello L1): org L1→L5 completa,
> BACKBONE, namespace memoria, dossier, handoff inter-eco. Esempio calibrante: la cartella
> `company/Ecosistemi/10-MEMORY/` (BACKBONE.md + ECOSISTEMA.md + Reparti/ + Agenti/ + Workflow/).

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando il Board dà mandato per un'intera area di business/funzione con vita propria
  (es. MEMORY, PLATFORM, un nuovo "E-commerce"): più reparti, memoria propria, dossier, confini.
- **NO se** è una singola unità organizzativa → **Reparto**. NO se è un gruppo ad-hoc → **Team**.
- **Trattamento MASSIMO giustificato SOLO qui**: è il livello di design più grande
  (`arch-org-designer`, WF-ECOSYSTEM-DESIGN). NON applicare questo peso a forme leggere.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **ECOSISTEMA.md** (org): missione dell'area, org chart **L1→L5** (organo → reparti L2 → workflow
   L3 → funzioni L4 → agenti L5), confini (cosa è / cosa NON è).
2. **BACKBONE.md**: l'ossatura tecnica/operativa condivisa — convenzioni, gate trasversali,
   pattern comuni, standard di naming (Title-Case fisso).
3. **Namespace memoria**: lo spazio AgentDB dedicato (es. `<eco>/...`) con i sotto-namespace e la
   regola di record ricostruibile (test amnesia).
4. **Reparti/** (≥1): cartella con i file dei reparti L2 (Schema-Reparto).
5. **Agenti/** + **Workflow/** (+ Funzioni/): i roster e i processi dell'ecosistema.
6. **Dossier**: il documento di blueprint dell'area (in PIANO-MAESTRO o equivalente) — fonte di verità.
7. **Handoff inter-eco**: contratti con gli altri ecosistemi (chi consegna cosa a chi).
8. **Gate di ecosistema** + **KPI** di area.
9. **Connessioni**.

## Template vuoto (copiabile)
```
<NN-NOME-ECOSISTEMA>/
├── ECOSISTEMA.md     # missione + org L1→L5 + confini
├── BACKBONE.md       # ossatura: convenzioni, gate trasversali, naming Title-Case
├── Reparti/          # ≥1 reparto (Schema-Reparto)
├── Agenti/           # roster L5 (Schema-Agente)
├── Workflow/         # processi (Schema-Workflow)
└── Funzioni/         # (opz.) funzioni L4
# + Dossier blueprint in PIANO-MAESTRO + namespace AgentDB <eco>/
```

## Checklist di completezza (per struct-gate)
- [ ] **ECOSISTEMA.md** con missione + org **L1→L5** completa + confini (è/non è).
- [ ] **BACKBONE.md** con convenzioni + gate trasversali + naming Title-Case fisso.
- [ ] **Namespace memoria** dedicato definito (+ sotto-namespace, record ricostruibile).
- [ ] **Reparti/** con ≥1 reparto conforme a Schema-Reparto.
- [ ] **Agenti/** e **Workflow/** presenti e popolati.
- [ ] **Dossier** blueprint referenziato (fonte di verità).
- [ ] **Handoff inter-eco** definiti (≥1 input + ≥1 output verso altri eco).
- [ ] **Gate** + **KPI** di ecosistema presenti.
- [ ] **Connessioni** ≥3.
- [ ] Navigabile nell'Explorer (visibilità totale — principio Maximilian).

## Esempio minimo compilato
**10-MEMORY.** ECOSISTEMA.md: org L1 organo → M3-ADR, M5-Sync (L2) → WF-ADR-REGISTER (L3) →
agenti ME-A05, ME-A10 (L5). BACKBONE.md: pattern backup→append→log→rollback, naming fisso.
Namespace `memory/` (checkpoints, decisions, ...). Reparti/, Agenti/, Workflow/ popolati. Dossier
09-ECOSISTEMA-MEMORY. Handoff: riceve CP dai team, consegna ADR-id. Gate G-ME3/G-ME4. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Un solo file invece della cartella navigabile → viola "visibilità totale nell'Explorer" (§0 dossier).
- Manca BACKBONE → ogni reparto reinventa convenzioni, niente ossatura condivisa.
- Namespace memoria assente → l'ecosistema non è ripartibile a freddo (fallisce test amnesia).
- Org chart incompleta (salta un livello L1→L5) → struttura ambigua.
- Applicare questo peso a una skill/principio/stile → spreco enorme, contro la FORMA GIUSTA.

## Connessioni
- [[Schema-Reparto]] — le unità L2 interne all'ecosistema
- [[Schema-Agente]] / [[Schema-Workflow]] — popolano l'ecosistema
- [[README]] — il principio della FORMA GIUSTA (questo è il peso MASSIMO, non il default)
- 14-DOSSIER-ARCHITETTURA §0 (visibilità totale) · §4 (WF-ECOSYSTEM-DESIGN) · §9 (gerarchia L1→L5)
