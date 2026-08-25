# Builder Team Capability Report

Work item: `WI-ACT-001`

| Agent | Role | Responsibility |
|---|---|---|
| BUILD-LEAD | Coordinator | Own work-item scope, dependencies, WIP and checkpoints without producing or approving implementation. |
| ARCHITECT | Architecture and Contracts | Define architecture decisions, boundaries and executable contracts before implementation. |
| RUFLO-SCOUT | RuFlo Integration Auditor | Prove RuFlo capabilities against a pinned source and produce reproducible certification evidence. |
| IMPLEMENTER | Implementation | Implement only approved contracts inside the assigned file scope and produce an evidence manifest. |
| TESTER | Independent Verification | Design and execute independent tests, preserve raw results and refuse unverifiable success claims. |
| SECURITY | Security and Privacy | Threat-model changes, test abuse cases and block unresolved critical or high-risk findings. |
| GATEKEEPER | Independent Quality Gate | Evaluate immutable artifacts against versioned criteria and emit PASS, FAIL or ESCALATE with evidence. |
| RELEASE | Release Engineering | Assemble signed evidence, verify release-unit coherence and execute only approved promotion or rollback plans. |

WIP limit: 3. Concurrency limit: 4.

RuFlo execution: disabled. Production credentials: forbidden.
