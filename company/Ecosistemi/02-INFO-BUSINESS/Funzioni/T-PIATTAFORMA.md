> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.1 (Team L4) + sez. 4a (WF-CORSO step 5)

# T-PIATTAFORMA — Team Piattaforma Corso

> Funzione L4 · Reparto: IB-R1-PRODOTTO · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Caricare e configurare il corso su piattaforma **Supabase + Next.js**: schema dati,
contenuti, gestione accessi, UI, percorso studente. Coordina i 5 agenti `formazione-*`
esistenti (arruolati as-is da `~/.claude/agents/`) senza riscrittura.

---

## Agenti del team

| Agente | Ruolo | Stato |
|---|---|---|
| `formazione-orchestrator` | Coordina l'intera operazione di caricamento piattaforma | ESISTENTE |
| `formazione-database` | Schema/dati corso su Supabase (contenuti, progress, iscritti) | ESISTENTE |
| `formazione-admin` | Pannello admin, gestione iscritti, accessi | ESISTENTE |
| `formazione-student` | Esperienza studente: progress tracking, percorso moduli | ESISTENTE |
| `formazione-design` | UI piattaforma e asset visivi dell'interfaccia | ESISTENTE |

**Regola migrazione:** mappatura + wrapper, MAI riscrittura. Registrazione in Identity-HR.

---

## Input

- Curriculum validato da `T-CURRICULUM`
- Moduli video montati (da handoff CONTENT-FACTORY)
- Asset design: copertine, workbook, certificato (da `T-DESIGN-PRODOTTO`)

---

## Output

- Corso live su piattaforma Supabase: tutti i moduli accessibili, paywall attivo
- Smoke test "studente fantasma" completato (accesso + modulo 1 end-to-end)

---

## Gate di uscita obbligatorio

> "Smoke test studente fantasma: studente crea account → accede → completa modulo 1 end-to-end."
> Fail → blocco: il corso non si lancia senza questo gate verde (B3 del piano di build).

---

## Connessioni

- [[IB-R1-PRODOTTO]] — reparto di appartenenza
- [[T-CURRICULUM]] — fornitore struttura corso
- [[06-PLATFORM]] — infrastruttura tecnica (Supabase, Next.js, deploy)
- [[WF-CORSO]] — workflow che include questa funzione come step 5
