# Anti-Patterns — target-avatar

> Cosa NON fare quando usi questa skill.

| # | Anti-pattern | Sintomo | Fix |
|---|---|---|---|
| 1 | Skippare il brief | Output generic | Force brief extraction |
| 2 | Tone mismatch (formale vs informale) | Cliente lamenta tono | Voice detection da KG |
| 3 | Output senza handoff | Next agent confuso | Schema handoff hardcoded |
| 4 | Generazione senza context | Output detached | Pass KG context sempre |
| 5 | Skipping validation | Errori downstream | Pre-handoff schema check |
