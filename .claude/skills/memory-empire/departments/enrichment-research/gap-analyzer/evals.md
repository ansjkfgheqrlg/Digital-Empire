# Evals — gap-analyzer

## PASS se:
- [ ] Ogni gap ha: id, target_skill, missing_content, already_present=false, atom_ids
- [ ] skills_already_complete popolato per skill senza lacune
- [ ] Nessun falso positivo (contenuto già presente non marcato come gap)

## FAIL se:
- [ ] Gap con contenuto già presente nella skill
- [ ] atom_ids vuoti (gap non tracciabile)
