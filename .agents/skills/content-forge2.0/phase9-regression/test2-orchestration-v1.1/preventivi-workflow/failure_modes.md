# Failure modes orchestration

| ID | Failure | Mitigation |
|----|---|---|
| F1 | Component unreachable | Fallback to default |
| F2 | Routing ambiguous | LLM supervisor decides |
| F3 | Budget exceeded | Block + alert |
| F4 | Component timeout | Retry 1x |
| F5 | Invalid input | Reject + user feedback |
