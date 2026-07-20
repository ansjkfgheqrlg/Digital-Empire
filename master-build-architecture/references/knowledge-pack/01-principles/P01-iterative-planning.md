# P01 — Iterative Planning

> **Definizione canonica**: Mai un piano solo. L'architettura emerge attraverso iterazioni esplicite di planning, dove ogni iterazione cattura un'osservazione critica che la precedente mancava. Il primo PLAN è sempre il più sbagliato; non sapere ancora cosa non sai è la condizione di partenza.

## Perché funziona

Tre ragioni convergenti:

### 1. L'ignoranza è asimmetrica
Quando inizi a pianificare un sistema, **non sai quello che non sai**. La prima versione del piano è inevitabilmente cieca su categorie intere di problemi (failure mode, edge case, interazioni tra componenti). Iterare è il modo strutturato per scoprire ciò che non sapevi.

Esempio concreto: nel PLAN-v1 di `content-forge` non c'era il concetto di **MKD** (Master Knowledge Document). Era nel PLAN-v5. Nessuno l'avrebbe potuto prevedere a PLAN-v1 perché emerge solo quando ti accorgi che generare un agente direttamente dal KG produce output thin.

### 2. Il pensiero esplicito costa poco, il refactor costa caro
Cambiare una riga in un PLAN markdown: 10 secondi. Cambiare un'architettura già implementata in 50 file: ore.

Le iterazioni di planning sono leva massima: prima fissi gli errori in `PLAN-vN.md`, meno paghi quando li scopriresti in `code.py`.

### 3. Il piano è anche memoria storica
Avere `PLAN-v1, v2, v3, v4, v5, v6` non è ridondanza: è **traceability**. Tra 6 mesi, quando vorrai capire "perché abbiamo aggiunto Stage 4 MKD?", vai in PLAN-v5 e leggi il razionale dell'iterazione che lo introdusse. Senza versioning, perdi questa memoria.

## Come applicarlo (operativo)

### Pattern di iterazione

```
PLAN-v1   →  prima bozza, sicuramente incompleta
   │
   ▼
USA / TESTA / OSSERVA  (anche solo mentalmente)
   │
   ▼
identifica 1-3 lacune o errori
   │
   ▼
PLAN-v2   →  fissa LE LACUNE specifiche, non riscrivere da capo
   │
   ▼
ripeti finché PLAN-vN non aggiunge novità sostanziali
```

### Quando una nuova versione è giustificata

Una nuova `PLAN-vN.md` è giustificata se aggiunge **una di queste** novità:
- Nuovo componente/agente/stage
- Riorganizzazione strutturale (non cosmetica)
- Cambio di principio fondante
- Inversione di una decisione precedente (con razionale)

**NON giustificano** una nuova versione:
- Refactoring di prosa
- Aggiunta di esempi
- Fix tipografici
- Espansione di sezioni esistenti

Per queste, modifica la versione corrente in-place.

### Cosa preservare tra versioni

Ogni nuova `PLAN-vN.md` deve contenere all'inizio:

```markdown
> Cosa cambia rispetto a PLAN-v(N-1):
> 1. ➕ <nuovo concetto/componente>
> 2. 🔄 <cambio strutturale>
> 3. ❌ <cosa abbiamo rimosso/invertito>
```

Questo è il **changelog architetturale**. Senza, le iterazioni diventano illeggibili.

## Esempi

### Esempio 1 — `content-forge` (nostro caso reale)

| Versione | Insight chiave aggiunto | Trigger |
|---|---|---|
| PLAN-v1 | Idea base: skill che trasforma sorgente in target | brainstorming iniziale |
| PLAN-v2 | Inventario 12 agenti specialisti | "manca chi fa cosa" |
| PLAN-v3 | 8 processi end-to-end per target | "ogni target ha logica diversa" |
| PLAN-v4 | Policy markdown+python embedded | "alcune parti sono codice, altre prosa" |
| PLAN-v5 | **Stage MKD obbligatorio** + multi-source | "agente generato direttamente dal KG è thin" |
| PLAN-v6 | Depth Architecture (team Ox + schema v0.3) | "bug reali trovati nei test: skill magre" |

Ogni iterazione catturava qualcosa che la precedente non poteva vedere senza esperienza accumulata.

### Esempio 2 — Software in generale

Pensa al `requirements.md` di un progetto software:
- **v1**: "vogliamo un'app per gestire X"
- **v2**: dopo prima demo: "abbiamo capito che servono ruoli utente"
- **v3**: dopo user testing: "il flusso onboarding va spezzato in 3 step"
- **v4**: dopo prima release: "manca completamente la gestione errori sistemica"

Niente di profondamente diverso dal pattern delle skill. La iterativa-planning è universale.

### Esempio 3 — ➕ (aggiunto, non da content-forge)

Costruire un evento aziendale:
- **v1**: data, location, agenda massima
- **v2**: dopo conferma sponsor: rivisto budget, aggiunto break sponsor
- **v3**: dopo issue logistici scoperti: aggiunta sezione contingency planning
- **v4**: dopo evento precedente in cui mancò AV setup: aggiunto vendor checklist

Il principio è **identico**: ogni iterazione è triggerata da un'osservazione reale, non da revisione cosmetica.

## Anti-pattern correlato

**AP07 — Skipping the Plan**: andare direttamente a costruire senza piano. Sintomo: 2 settimane dopo ti accorgi di dover rifare metà del lavoro perché manca una componente che un piano avrebbe identificato in 2 ore.

**Anti-pattern duale**: **Over-planning paralysis** — iterare PLAN-vN troppe volte senza mai costruire. Soglia pragmatica: dopo 3-4 iterazioni di PLAN senza nuovi insight sostanziali, è il momento di passare a scaffolding (Phase 1).

## Decision tree: "devo fare una nuova versione del PLAN?"

```
Hai osservato qualcosa di nuovo da quando hai scritto l'ultimo PLAN?
├─ NO → modifica in-place, no nuova versione
└─ SÌ
   ├─ È un nuovo componente, principio, o inversione decisionale?
   │  ├─ NO → modifica in-place, aggiungi sezione "amended"
   │  └─ SÌ → procedi con check successivo
   ├─ La novità impatta ≥2 componenti esistenti?
   │  ├─ NO → modifica in-place + log nel cambiamento
   │  └─ SÌ → NUOVA VERSIONE
   └─ Se NUOVA VERSIONE: scrivi prima il changelog (3 bullet max),
      poi il piano completo aggiornato.
```

## Quando NON iterare

- **Domini molto noti**: se stai facendo per la decima volta lo stesso tipo di skill (es. data extraction skill per il quinto cliente simile), iterare il PLAN è overhead. Riusa il template.
- **Time pressure assoluta**: se devi consegnare in 2 ore, fai un PLAN solo e accetta il debito tecnico.
- **Esperimenti throwaway**: per script una-tantum, no PLAN.

## Riferimenti esterni

- **Fred Brooks**, *The Mythical Man-Month* (1975) — "Plan to throw one away; you will, anyhow." Capitolo 11 articola perché la prima versione è destinata a essere buttata.
- **John Gall**, *Systemantics* (1975) — "A complex system that works is invariably found to have evolved from a simple system that worked." Le iterazioni di planning sono il meccanismo di evoluzione.
- **Donald Knuth** — "Premature optimization is the root of all evil." Da estendere: premature anything (including premature freezing of plan) è il root.
- **Anthropic skill-creator** — Il pattern stesso di skill-creator implementa P01: iterazioni di test → review → improve.

## Connessioni con altri principi

- Si appoggia su: P12 (Traceability) — senza traceability tra versioni il pattern non funziona
- Combina con: P09 (Failure modes first-class) — i failure mode scoperti in v_n diventano input di v_(n+1)
- Contrasta con: nessuno (è principio quasi universalmente accettato)
