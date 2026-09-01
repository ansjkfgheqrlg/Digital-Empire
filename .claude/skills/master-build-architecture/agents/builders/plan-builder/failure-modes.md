# Plan-Builder Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| vN not richer than v(N-1) | Shallow or similar content | Strict template + "expand every atom" rule | Conductor review + length_check | Force re-generation with more depth |
| Missing memory ecosystem section | No mention of screenshot structure | Mandate in template | schema_validator | Add section + re-log |
| No Ruflo commands | Missing integration | Explicit in playbook | manual + anti-pattern-hunter | Add section |