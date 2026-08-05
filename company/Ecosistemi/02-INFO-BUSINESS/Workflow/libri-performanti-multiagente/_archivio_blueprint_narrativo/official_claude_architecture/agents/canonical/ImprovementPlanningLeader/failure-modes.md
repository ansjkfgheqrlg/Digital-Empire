# Failure Modes - ImprovementPlanningLeader

| Failure | Symptom | Prevention | Detection | Recovery |
| missing output | empty | validator | OutputMonitor | retry rollback |
| Playwright failure | timeout | ErrorHandler | FailureDetector | retry timeout++ |
