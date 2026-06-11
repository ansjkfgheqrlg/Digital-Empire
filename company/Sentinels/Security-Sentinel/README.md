# 🔒 Security Sentinel

> **Sentinel always-on.** Autorità di enforcement LX.
> Supervisore C-Suite: CTO (empire-cto)

## Cosa vigila

segreti (API key, password, token), PII, injection (prompt/SQL/XSS), sicurezza OWASP

## Quando blocca

qualsiasi operazione che mette segreti nel repo git, che espone PII, che introduce vulnerabilità

## Come opera

aidefence scan su ogni batch di file prima del commit; grep per pattern noti (API key, password=)

## Skill operative

aidefence (via ruflo), scan segreti pre-commit

## Stato

Struttura definita (F1). Implementazione automatica da costruire in F2-F5.
Nelle prime fasi (F1-F3): eseguito manualmente come checklist dal fondatore o da Claude.