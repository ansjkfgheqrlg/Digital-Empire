# ⚙️ 06 — PLATFORM

> **Livello:** L1 · **Priorità:** TRASVERSALE · **Stato:** parziale (Crea Siti attivo)
> Dossier completo: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §PLATFORM

## Missione

Infrastruttura tecnologica della holding: codice, siti, tooling, sicurezza, CI/CD, deploy.
Serve tutti gli ecosistemi. **Crea Siti** è il reparto L2 WEB-ENGINEERING principale — wrappato
as-is, non riscritto (ADR-003).

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Web-Engineering (Crea Siti) | landing pages, siti clienti, app Next.js | `Reparti/Web-Engineering/` |
| L2.2 | Tooling | script, automazioni infra, CLI interni | `Reparti/Tooling/` |
| L2.3 | Security | aidefence scan, PII check, segreti, OWASP | `Reparti/Security/` |
| L2.4 | CI/CD & Deploy | vercel deploy, github actions, verify-empire.sh | `Reparti/CI-CD/` |

## Siti attivi

| Sito | URL | Stack |
|---|---|---|
| Presentazione Empire | presentazione-empire.vercel.app | Next.js |
| Agency Landing | agency-empire-kohl.vercel.app | Next.js + Tailwind v4 |
| Preventivo Exponium | preventivo-exponium.vercel.app | Next.js |
| Outreach Dashboard | — | Next.js (locale) |

## Come si collega al Backbone

- **BUS:** riceve feature request da tutti gli ecosistemi; consegna tool/fix/siti
- **BRAIN:** namespace `platform/*` — deployment log, versioni, build status
- **GOVERNANCE:** Security Sentinel supervisiona ogni build; zero segreti in git
- **CTO:** supervisione diretta

## Asset esistenti (da migrare in F3)

- `Crea siti/` — tutti i progetti web
- `empire-style/` — design system condiviso
- `agency-empire/`, `agency-empire-landing/` — landing agency
- `presentazione-empire/` — presentazione vendita
- `preventivo-exponium/` — preventivo cliente
- `app-landing` (vendor — .git.bak)

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` · Aggiornato: 2026-06-11*
