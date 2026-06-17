---
Type: CONCEPT
Status: Active
Tags: #ceo #skills #board-consensus #decision-record #okr-tracker
Created: 2026-06-17
Last updated: 2026-06-17
---

# SKILLS — Skill Proprie della Figura CEO / Empire-Conductor

> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-CEO.md` §"Skill proprie"
> Connessioni: [[WF-DECISIONE-STRATEGICA]] · [[WF-REVIEW-TRIMESTRALE]] · [[ceo-okr-tracker]]

---

## Skill 1: `board-consensus`

### Scopo
Regge il voto raft del Board C-Suite per una decisione proposta. Garantisce che il voto abbia
il quorum corretto, che ogni membro voti esplicitamente (non per silenzio-assenso), che lo
stallo venga rilevato e il voto decisivo del conductor venga attivato se necessario. Produce
il record del voto nel formato standard per la documentazione.

### Come funziona
La skill riceve la proposta di decisione + la lista dei votanti rilevanti (non sempre tutto il
Board vota: solo le figure C-Suite competenti per il dominio della decisione). Esegue il giro
di voti, raccoglie le posizioni, verifica il quorum, calcola il risultato. Se c'è stallo
(voti pari), attiva il voto decisivo del conductor e lo registra come tale.

### Input
```json
{
  "proposta": "testo della decisione da votare",
  "votanti": ["COO", "CFO", "CRO", "CMO"],
  "quorum_richiesto": 3,
  "voto_decisivo_conductor_attivabile": true
}
```

### Output
```json
{
  "esito": "approvata | respinta | stallo_risolto_dal_conductor",
  "voti": {
    "favorevoli": [{"membro": "COO", "voto": "favorevole"}, {"membro": "CFO", "voto": "favorevole"}],
    "contrari": [{"membro": "CRO", "voto": "contrario"}],
    "astenuti": []
  },
  "quorum_raggiunto": true,
  "voto_decisivo_usato": false,
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Regole interne
- Il silenzio non è un voto: ogni membro deve esprimere favorevole / contrario / astensione.
- Il voto decisivo si usa solo se i voti sono matematicamente pari. Non per "velocizzare".
- Il record del voto è immutabile dopo la chiusura: non si "corregge" un voto.
- Astensione conta nel quorum (il membro ha partecipato) ma non nella maggioranza.

---

## Skill 2: `decision-record`

### Scopo
Ogni decisione presa dal CEO (dopo il voto raft e il gate Mandato) viene trasformata in un
record permanente nel sistema di memoria. Se la decisione è architetturale, produce un ADR
completo. Se è operativa, produce un checkpoint. In entrambi i casi aggiorna STATO-EMPIRE.
Garantisce che "documenta o non esiste" sia tecnicamente impossibile da violare.

### Come funziona
La skill riceve la decisione chiusa dal conductor (con rationale, voto, azioni). Classifica
il tipo: architetturale (impatta la struttura della holding, i workflow, le regole) o operativa
(risolve una questione senza cambiare la struttura). Scrive il documento nel formato corretto
(template ADR o template checkpoint), lo salva nel percorso corretto, aggiorna STATO-EMPIRE.

### Input
```json
{
  "decisione": "testo della decisione presa",
  "rationale": "perché",
  "tipo": "architetturale | operativa",
  "azioni": [{"chi": "string", "cosa": "string", "ac": [], "deadline": "string"}],
  "voto": {"esito": "string", "favorevoli": 0, "contrari": 0},
  "ecosistemi_coinvolti": []
}
```

### Output
```json
{
  "documento_creato": "ADR-NNN | CP-YYYYMMDD-NNN",
  "percorso": "company/Memory/decisions/ADR-NNN.md | company/Memory/checkpoints/CP-YYYYMMDD-NNN.md",
  "stato_empire_aggiornato": true,
  "contradiction_check": "nessuna contraddizione | CONTRADDIZIONE con ADR-X (segnalata)"
}
```

### Regole interne
- Contradiction check obbligatorio: prima di scrivere un ADR, verifica che non contraddica
  ADR attivi esistenti. Se contraddice → segnala al conductor (non scrive senza risoluzione).
- Il template ADR è fisso (da `company/Memory/templates/`): non si inventa il formato.
- Il checkpoint include sempre: titolo, data, decisione, rationale, azioni, chi verifica.
- STATO-EMPIRE viene aggiornato in ogni caso, anche per decisioni operative.

---

## Skill 3: `okr-tracker`

### Scopo
Mantiene il registro degli OKR trimestrali della holding aggiornato in tempo reale. Raccoglie
i progress report dagli ecosistemi, calcola lo stato di ogni OKR (on-track / at-risk / off-track),
produce il report sintetico per il conductor. Usata dal `ceo-okr-tracker` in ogni ciclo di
tracking e dal WF-REVIEW-TRIMESTRALE in apertura di review.

### Come funziona
La skill accede allo state `board/ceo/okr-trimestre`, legge gli OKR correnti e le loro deadline,
richiede i progress report agli ecosistemi owner (se la raccolta è attiva), aggiorna lo stato
di ogni OKR, classifica (on-track / at-risk / off-track), e produce il report aggregato.

### Input (richiesta tracking)
```json
{
  "modalita": "raccolta | update | report",
  "trimestre": "Q2-2026",
  "okr_da_aggiornare": ["OKR-Q2-01", "OKR-Q2-02"],
  "progress_ricevuti": [
    {
      "okr_id": "OKR-Q2-01",
      "ecosistema": "01-AGENCY",
      "progress": "80% verso target",
      "stato_stimato": "on-track"
    }
  ]
}
```

### Output
```json
{
  "trimestre": "Q2-2026",
  "sommario": {"on_track": 4, "at_risk": 2, "off_track": 1},
  "okr_critici": [
    {"okr_id": "OKR-Q2-03", "stato": "off-track", "motivo": "blocco copywriter", "owner": "04-MARKETING"}
  ],
  "aggiornamento_mancante": ["06-INFO-BUSINESS"],
  "stato_empire_aggiornato": false,
  "nota": "2 OKR richiedono attenzione prima del Board"
}
```

### Regole interne
- Non si inventano progressi: se l'ecosistema non risponde, stato = "aggiornamento mancante",
  non "si assume on-track".
- Il cambio da on-track a off-track in un ciclo → alert immediato al conductor, non si aspetta
  il report settimanale.
- Lo storico dei trimestri precedenti è mantenuto in `ceo-memoria` e non viene sovrascritto.

---

## Connessioni

- [[ceo-okr-tracker]] · `agenti/ceo-okr-tracker.md`
- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[WF-DECISIONE-STRATEGICA]] · `workflow/WF-DECISIONE-STRATEGICA.md`
- [[WF-REVIEW-TRIMESTRALE]] · `workflow/WF-REVIEW-TRIMESTRALE.md`
- [[STATE]] · `state/README.md`
