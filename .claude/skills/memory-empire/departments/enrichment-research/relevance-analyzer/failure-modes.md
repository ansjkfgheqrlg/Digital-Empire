# Failure Modes — relevance-analyzer

## FM-01: relevance_scan.py non disponibile
**Fix:** Leggi manualmente SKILL.md delle 20-30 skill più probabilmente rilevanti + le skill AI/Claude sempre

## FM-02: Score tutti bassi (< 0.4 per tutto)
**Causa:** atoms troppo generici o skill installate in dominio diverso
**Fix:** Abbassa threshold a 0.3 e includi skill con keyword parziale
