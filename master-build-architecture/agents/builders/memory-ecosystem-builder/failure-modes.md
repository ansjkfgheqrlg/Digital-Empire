# Memory-Ecosystem-Builder Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Structure not matching screenshot | Missing subdirs or INDEX | Use exact template + validation | validator + conductor review | Re-run builder with strict template |
| No auto-update mechanism | Steps not logged after actions | Always include memory_manager.py | post-build check | Add script + update INDEX |
| Missing traceability | Entries have no source links | Mandate in every generated file | coverage + manual review | Re-generate with source tags |
| Two-layer not implemented | Only one layer present | Explicit design in playbook and INDEX | SI observer | Enhance with vector/Ruflo notes |