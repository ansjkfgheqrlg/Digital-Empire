# skill-forge

> Source: File system (`SKILL & Agenti\SKILL\Agente Max\skills\skill-forge.md`)
> Collected: 2026-05-06
> Published: Unknown

# SKILL-FORGE — Protocollo Creazione Skill

Usa questo protocollo quando devi creare una nuova skill Claude Code da zero, modificare una skill esistente, o iterare su una skill già esistente per migliorarla.

---

## FASE 1 — INTAKE (3 domande obbligatorie)

Prima di scrivere una sola riga di codice, poni queste domande all'utente se le informazioni non sono già nel prompt:

**Domanda 1 — Azione principale:**
"Cosa deve fare esattamente questa skill? Descrivi l'azione principale con un verbo + oggetto. Es: 'genera report settimanale', 'analizza competitor', 'crea calendario contenuti'."

**Domanda 2 — Trigger phrases:**
"Quando l'utente vuole usare questa skill, cosa dirà? Elenca 3-5 frasi naturali in italiano che la attivano. Es: 'fai il report della settimana', 'analizza questo competitor', 'crea il calendario del mese'."

**Domanda 3 — Output e complessità:**
"Cosa produce la skill? Una risposta testuale, un file Markdown, uno script Python, una serie di file? Ha bisogno di eseguire codice Python (deterministico) o solo istruzioni testuali?"

Se l'utente non risponde a tutte e tre, non procedere con la creazione. Le risposte a queste domande determinano il 90% della qualità della skill.

---

## FASE 2 — ANATOMIA DELLA SKILL

### Struttura cartella obbligatoria:

```
nome-skill/
├── SKILL.md            ← file principale (OBBLIGATORIO)
├── scripts/            ← solo se la skill esegue codice
│   └── main.py
└── references/         ← solo se la skill usa dati di riferimento
    └── framework.md
```

### YAML Frontmatter (obbligatorio):

```yaml
---
name: nome-skill
description: [descrizione — vedi FASE 3]
---
```

**Campi obbligatori:** `name`, `description`
**Campi opzionali:** `model` (default: sonnet), `tools`, `color`

### Regole del corpo (body):

- **Forma imperativa** — non seconda persona. Es: "Analizza il testo" NON "Tu devi analizzare il testo"
- **Lunghezza massima:** 500 righe in SKILL.md. Se supera, spostare contenuto in `references/`
- **Struttura raccomandata:** Obiettivo → Quando Usare → Prerequisiti → Processo → Output
- **Percorsi:** sempre Windows con backslash per questa macchina

---

## FASE 3 — DESCRIPTION ENGINEERING

La `description` è il meccanismo di routing. Claude Code la legge per decidere SE attivare questa skill. Una description debole = skill mai attivata.

### Struttura vincente della description:

```
[AZIONE PRINCIPALE della skill in terza persona].
Usa questa skill quando [CONTESTO SPECIFICO].
Trigger: "[frase1]", "[frase2]", "[frase3]", "[frase4]".
Non usare per [COSA NON FA — delimita il confine].
Output: [cosa produce].
```

### Esempio — description DEBOLE (da evitare):
```
description: Skill per report settimanale.
```

### Esempio — description FORTE:
```
description: Genera il report settimanale di performance con analisi KPI,
trend e raccomandazioni azionabili. Usa questa skill quando l'utente vuole
un riassunto strutturato della settimana lavorativa o dei risultati di un
progetto. Trigger: "fai il report della settimana", "report settimanale",
"riassumi la settimana", "analizza i risultati settimanali", "weekly report".
Non usare per report mensili o analisi di singoli dati. Output: documento
Markdown strutturato con sezioni KPI, trend, anomalie, raccomandazioni.
```

### Principio della "description pushy":
La description deve essere abbastanza specifica da triggerare anche quando l'utente usa parole leggermente diverse. Includi sinonimi e varianti naturali nelle trigger phrases.

---

## FASE 4 — SCRIPT INTEGRATION

### Quando aggiungere scripts/:

Aggiungi `scripts/` SOLO se la skill deve:
- Calcolare qualcosa in modo deterministico (punteggi, metriche, classificazioni)
- Generare output strutturato (JSON, CSV, report con formato fisso)
- Validare input con logica complessa
- Eseguire operazioni su file (batch processing)

NON aggiungere scripts/ se la skill genera solo testo narrativo o Markdown libero.

### Template script Python base:

```python
#!/usr/bin/env python3
"""
[Nome Script] — componente di [nome-skill]
Uso: python main.py --input X [--output Y]
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='[descrizione]')
    parser.add_argument('--input', required=True, help='[descrizione input]')
    parser.add_argument('--output', default='output.md', help='[descrizione output]')
    args = parser.parse_args()

    # Logica principale
    result = process(args.input)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"Output salvato in: {args.output}")

def process(input_data):
    # TODO: implementa qui la logica
    return f"# Output\n\n{input_data}"

if __name__ == '__main__':
    main()
```

### Come SKILL.md referenzia lo script:

```markdown
## Esecuzione

Esegui lo script per generare l'output strutturato:

```bash
python scripts/main.py --input "dati" --output "report.md"
```
```

---

## FASE 5 — PROCESSO DI CREAZIONE

Segui questi step in ordine:

1. **Raccogli le 3 risposte INTAKE** (o verificale se già nel prompt)

2. **Determina la struttura:**
   - Solo SKILL.md? O anche scripts/ e references/?
   - Quale modello? (default sonnet, usa opus solo per ragionamento complesso)

3. **Scrivi la description** seguendo il template FASE 3

4. **Crea la struttura cartella** con il nome corretto (lowercase, hyphens)

5. **Scrivi SKILL.md** con:
   ```
   --- frontmatter ---
   ## Obiettivo
   ## Quando Usare
   ## Prerequisiti (se applicabile)
   ## Processo
   ## Output
   ## Installazione
   ```

6. **Crea scripts/main.py** se richiesto (usa il template FASE 4)

7. **Crea references/framework.md** se la skill usa dati di riferimento fissi

8. **Esegui il QUALITY CHECKLIST** prima di consegnare

---

## QUALITY CHECKLIST PRE-DELIVERY

Prima di presentare la skill all'utente, verifica ogni punto:

- [ ] `name` è lowercase con hyphens (es: `report-settimanale` non `Report Settimanale`)
- [ ] `description` supera 80 caratteri e contiene almeno 3 trigger phrases in italiano
- [ ] Description delimita chiaramente cosa la skill NON fa
- [ ] Body è in forma imperativa (nessun "tu devi", "dovresti", "you should")
- [ ] Body non supera 500 righe
- [ ] Script Python incluso SE la skill richiede output deterministico
- [ ] Sezione "Installazione" inclusa alla fine di SKILL.md con percorso assoluto
- [ ] Percorsi Windows con backslash nel SKILL.md

---

## SEZIONE INSTALLAZIONE (da includere sempre in SKILL.md)

Ogni SKILL.md deve terminare con:

```markdown
## Installazione

Copia l'intera cartella `nome-skill/` in:

**Globale (disponibile in tutti i progetti):**
`C:\Users\Utente\.claude\skills\`

**Locale (solo questo progetto):**
`.claude\skills\` nella root del progetto

Poi riavvia Claude Code per attivare la skill.
```
