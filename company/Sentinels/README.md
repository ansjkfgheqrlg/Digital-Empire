# 🛡️ SENTINELS — Guardie always-on

> I Sentinel operano su **tutti i livelli** della holding — non su richiesta, ma in modo
> continuo e proattivo. Possono bloccare qualsiasi delivery che viola il Mandato Empire,
> indipendentemente dalla gerarchia. Sono l'autorità di enforcement di LX.

## I 5 Sentinel

| Sentinel | Cosa vigila | Blocca se... | Path |
|---|---|---|---|
| **Cost Sentinel** | spese API, crediti, budget per task/ecosistema | sfora budget autorizzato senza ok CFO | `Cost-Sentinel/` |
| **Quality Sentinel** | gate APSOC ≥80, zero claim senza prova | score < soglia o claim non verificato | `Quality-Sentinel/` |
| **Drift Sentinel** | coerenza architetturale tra ecosistemi e decisioni | output contraddice un ADR attivo | `Drift-Sentinel/` |
| **Security Sentinel** | segreti, PII, injection, sicurezza OWASP | leak credenziali, injection, PII non mascherata | `Security-Sentinel/` |
| **Brand-Voice Sentinel** | tono DE: diretto, provocatorio, trasparente | output generico, AI-slop, hype senza proof | `BrandVoice-Sentinel/` |

## Differenza Sentinel vs Guild

- **Guild**: expertise su richiesta (chiamata da ecosistemi)
- **Sentinel**: enforcement automatico (blocca senza essere chiamato)

Un Sentinel può bloccare qualsiasi livello (L0→L5) se rileva violazione del Mandato.
Solo i fondatori (LX) possono derogare a un Sentinel — e devono documentarlo con ADR.
