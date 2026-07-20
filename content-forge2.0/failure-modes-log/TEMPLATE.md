---
fm_id: FM-NNN
slug: <slug-breve>
status: logged                # logged | triaged | resolved
date_logged: <YYYY-MM-DD>
date_triaged: null
date_resolved: null

# Compila in triage (lascia null in logged)
severity: null                # blocker | major | minor
category: null                # builder | optimizer | schema | pipeline | docs | packaging | trigger | other
scope: null                   # hotfix-v1.1.x | phase-10 | phase-11+
confidence_root_cause: null   # low | med | high
estimated_effort: null        # 30min | 2h | 1d | multi-day

# Riferimenti
related_fm: []                # altri FM correlati ["FM-002", "FM-005"]
related_components: []        # agenti/scripts/schema toccati ["B2", "O3", "schema_validator.py"]
forge_version_observed: "1.1"
---

# FM-NNN — <Titolo breve descrittivo>

## 1. Cosa è successo (1-3 frasi, fattuale)

<Es: "Ho invocato `/forge transcripts.md --target=skill`. Stage 6 ha prodotto la skill correttamente,
ma O2 in Stage 7 ha generato playbook con 5 conversazioni tutte identiche tranne per il numero
nell'intestazione.">

## 2. Cosa ti aspettavi

<Es: "Mi aspettavo 5 conversazioni distinte: 3 happy con scenari diversi, 1 edge, 1 failure recovery.">

## 3. Come riprodurlo

### Input

- **Sorgente**: <path o descrizione>
- **Target**: <doc/agent/skill/team/workflow/orchestration/wiki/custom>
- **Opzioni invocazione**: <flag, ASK answers principali>

### Comando

```bash
/forge <args>
```

### Output osservato

<paste o link al file/directory dell'output problematico>

## 4. Dove si è rotto (best guess)

<Quale stage / agente / script. Se non sai, lascia "non chiaro">

- [ ] Stage 1 (Ingestion / A1)
- [ ] Stage 2 (Analysis / A2)
- [ ] Stage 3 (KG / A3)
- [ ] Stage 4 (MKD / A5)
- [ ] Stage 5 (Target advisor / A4)
- [ ] Stage 6 (Build / Bx)
- [ ] Stage 7 (Depth pass / Ox)
- [ ] Stage 8 (QA / C1+C3)
- [ ] Stage 9 (Packaging)
- [ ] Trigger / description (la skill non si è attivata bene)
- [ ] Conductor (logica di coordinamento)
- [ ] Schema / validation
- [ ] Documentazione (SKILL.md, references/, ecc.)
- [ ] Non chiaro

## 5. Impatto

- **Frequenza**: <quante volte su quanti tentativi> (es. "3 su 3", "1 su 10")
- **Workaround**: <hai trovato modo di aggirare?> (es. "no", "sì: re-run con --target esplicito")
- **Blocca uso skill**: sì / no / parziale

## 6. Ipotesi di causa (se hai un sospetto)

<Es: "O2 probabilmente usa un template fisso senza variare i topic; nel SP manca un'istruzione tipo
'genera 5 scenari diversi non template-driven'.">

## 7. Suggerimento fix (se hai idea)

<Lascia vuoto se non hai idea. Anche solo 1 riga va bene.>

## 8. Note libere

<Qualunque cosa: screenshot, contesto, perché ti ha colpito particolarmente, ecc.>
