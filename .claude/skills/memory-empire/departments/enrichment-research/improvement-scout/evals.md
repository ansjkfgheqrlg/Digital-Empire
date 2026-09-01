# Evals — improvement-scout

## PASS se:
- [ ] Ogni improvement ha: id, type, target_skill, evidence, source_atom, priority, confidence
- [ ] evidence è citazione diretta dall'atom (non inventata)
- [ ] source_atom è tracciabile (videoID#timestamp o file:riga)
- [ ] improvements filtrati per confidence >= 0.6
- [ ] JSON scritto anche se improvements=[]

## FAIL se:
- [ ] evidence non citata dall'atom
- [ ] source_atom inventato
- [ ] Miglioramenti duplicati di gap-analyzer
- [ ] confidence non calcolata (tutti a 1.0 sospetto)
