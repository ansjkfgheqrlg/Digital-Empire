# SCHEMA CANONICO — Reparto

> Forma PESANTE. Unità organizzativa permanente dentro un ecosistema (livello L2): missione,
> team L3/L4, workflow, gate, KPI. Esempio calibrante:
> `company/Ecosistemi/06-PLATFORM/Reparti/Web-Engineering.md`.

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando serve un'unità organizzativa stabile che possiede una capacità di business
  ricorrente (es. "Crea Siti", "ADR", "Sync"), con propri workflow, team e KPI permanenti.
- **NO se** è un gruppo ad-hoc per un obiettivo singolo → **Team**. NO se è un'intera area con più
  reparti, BACKBONE e namespace propri → **Ecosistema**. NO se è un singolo esecutore → **Agente**.
- **Trattamento PESANTE giustificato**: vive nel tempo, ha gerarchia interna e gate.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Intestazione**: livello (L2), ecosistema di appartenenza, riferimenti a ECOSISTEMA.md e BACKBONE.md.
2. **Missione**: cosa produce/garantisce il reparto, in modo permanente.
3. **Workflow L3**: tabella `{workflow, descrizione, lead time/gate}` — i processi che il reparto possiede.
4. **Funzioni / Team L4**: tabella `{id funzione/team, descrizione, workflow padre}`.
5. **Agenti L5**: roster `{id, ruolo, tier}` degli agenti del reparto (link a Schema-Agente).
6. **Handoff**: cosa riceve in input (da chi) e cosa consegna in output (a chi) — contratti.
7. **Gate**: i controlli di qualità/struttura che il reparto applica prima di consegnare.
8. **KPI**: metriche permanenti del reparto con target.
9. **Connessioni**.

## Template vuoto (copiabile)
```markdown
# L2 <NOME-REPARTO> — <claim in una frase>
> Reparto L2 · Ecosistema: <NN-NOME> · Rif: ECOSISTEMA.md · BACKBONE.md
## Missione
<cosa garantisce in modo permanente>
## Workflow L3
| Workflow | Descrizione | Lead time/Gate |
## Funzioni / Team L4
| ID | Team | Workflow padre |
## Agenti L5
| ID | Ruolo | Tier |
## Handoff
- Input da: <reparto/eco> → <payload> · Output a: <reparto/eco> → <payload>
## Gate
- <controllo bloccante>
## KPI
| KPI | Target |
## Connessioni
```

## Checklist di completezza (per struct-gate)
- [ ] Intestazione con **livello L2 + ecosistema** + riferimenti a ECOSISTEMA/BACKBONE.
- [ ] **Missione** permanente (non un obiettivo one-shot).
- [ ] **Workflow L3** in tabella (≥1).
- [ ] **Funzioni/Team L4** in tabella, ognuna con workflow padre.
- [ ] **Agenti L5** con id, ruolo e tier (link a Schema-Agente).
- [ ] **Handoff** input E output definiti (da chi / a chi / payload).
- [ ] **Gate** di consegna definiti.
- [ ] **KPI** in tabella con target misurabili.
- [ ] **Connessioni** ≥3.

## Esempio minimo compilato
**L2 WEB-ENGINEERING** (eco 06-PLATFORM). Missione: produce tutti i siti DE/clienti, standard
empire-premium-style. Workflow L3: WF-SITE-FULL (≤10gg), WF-LANDING-RAPIDA (<48h). Funzioni L4:
T-site-design, T-site-qa... Agenti L5: plt-director (opus), plt-site-builder (sonnet). Handoff:
input da MARKETING (copy), output a OPERATIONS (report). Gate: QA playwright PASS prima di deploy.
KPI: lead time WF-SITE-FULL ≤10gg. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Reparto senza KPI permanenti → indistinguibile da un Team ad-hoc.
- Handoff non definiti → il reparto "galleggia" senza input/output chiari nell'ecosistema.
- Agenti elencati senza tier/ruolo → non si capisce chi fa cosa.
- Trattare un intero ecosistema come reparto (manca BACKBONE/namespace) o un team come reparto.
- Workflow citati ma non posseduti (vivono altrove) → confine organizzativo confuso.

## Connessioni
- [[Schema-Ecosistema]] — il contenitore L1 di cui il reparto è parte
- [[Schema-Team]] / [[Schema-Agente]] — le unità interne del reparto
- [[Schema-Workflow]] — i processi L3 che il reparto possiede
- [[README]] · 14-DOSSIER-ARCHITETTURA §2 (reparti L2 di ARCHITETTURA)
