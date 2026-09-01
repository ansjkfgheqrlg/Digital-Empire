# verification-integrity / department-lead

**Ruolo:** Controlla ogni modifica prima e dopo l'esecuzione. Gate di sicurezza per enrichment-research.
Nessuna modifica alle skill passa senza il suo gate.

## Pipeline
- permission-guard: gate approve/deny
- change-auditor: log + rollback
- integrity-verifier: test finale skill non rotta
