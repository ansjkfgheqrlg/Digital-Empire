# Swarm-Builder Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Monolithic or too few agents | <10 agents or god-agents | Enforce PT01 + single responsibility | Conductor + SI | Re-design with more decomposition |
| No memory integration | Agents have no memory spec | Mandate in every agent definition | validation | Add memory.md to all specs |
| No Ruflo commands | Pure abstract topology | Always emit concrete commands | packaging check | Add ruflo_bridge output |