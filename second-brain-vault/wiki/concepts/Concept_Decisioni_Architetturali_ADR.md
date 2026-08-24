---
Type: CONCEPT
Status: Active
Tags: #adr #decisioni #governance #memory-first #architettura
Created: 2026-08-24
Last updated: 2026-08-24
---

# Decisioni Architetturali (ADR) — Indice

## Overview
Indice di tutte le Architecture Decision Records registrate in `company/Memory/decisions/`
(REGOLA ZERO, ADR-002: memory-first, sempre rispettate — mai contraddette in silenzio).
Nessuna aveva ancora un punto di ingresso nella wiki: questa pagina colma il buco e fa da
hub cross-linkato verso le pagine progetto/concetto che ogni decisione tocca.

## Le 12 decisioni

| ADR | Titolo | Cosa decide |
|---|---|---|
| [ADR-001](../../../company/Memory/decisions/ADR-001-empire-os-10-ecosistemi.md) | EMPIRE OS — 10 ecosistemi | Architettura fondativa della holding: 10 ecosistemi di agenti AI, dossier esecutivi in `PIANO-MAESTRO/`. Vedi [[projects/Piano_Maestro_EMPIRE_OS]]. |
| [ADR-002](../../../company/Memory/decisions/ADR-002-memory-first.md) | Memory-first | Ogni task interroga `company/Memory/` prima di agire e scrive checkpoint dopo — regola zero non negoziabile del progetto. |
| [ADR-003](../../../company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md) | Wrap, non riscrittura | Gli asset/motori reali già esistenti si avvolgono (wrapper dichiarato `[WRAPPA]`), mai si riscrivono da zero. Regola applicata sistematicamente in tutto STEP 5 (vedi sotto) e in PreventivoForge/Novacar. |
| [ADR-004](../../../company/Memory/decisions/ADR-004-github-monorepo-sync.md) | GitHub monorepo + sync | Workspace intero su GitHub (`ansjkfgheqrlg/Digital-Empire`, privato), sync bidirezionale Max↔Gael via `scripts/empire-sync.ps1`. |
| [ADR-005](../../../company/Memory/decisions/ADR-005-backlog-non-blocca.md) | Backlog non blocca | Gli item minori vanno in `company/Memory/BACKLOG.md`, mai fermano la costruzione in corso. |
| [ADR-006](../../../company/Memory/decisions/ADR-006-ciclo-fase-9-passi.md) | Ciclo di fase a 9 passi | Metodo ufficiale di ogni fase di costruzione (RECALL→SPEC→PRE-MORTEM→BUILD→GATE→REVIEW→TEST→COMMIT→RETRO), vale per Max e per Gael; swarm obbligatorio su ≥2 aree disgiunte. |
| [ADR-007](../../../company/Memory/decisions/ADR-007-piano-v2-scala.md) | Piano V2 — direttiva di scala | Pivot da EMPIRE OS v1 a v2: reparti come team 6-10 agenti + workflow CF-grade, mega-reparti come aziende, organo MAXIMILIAN, ecosistema-Mandato. Base dello STEP 5 (build reparto-per-reparto) e del Genesi Core (ARCHITETTURA+FORGE+MAXIMILIAN) descritti in [[projects/Piano_Maestro_EMPIRE_OS]]. |
| [ADR-008](../../../company/Memory/decisions/ADR-008-catena-intestazione-controllo.md) | Memory Empire obbligatorio (Empire Studio) | Ogni pipeline di ingestione contenuto (Empire Studio) deve includere gli stage Memory Empire C-H come invariante #0 — nato da un errore reale (pipeline comunicato senza Memory Empire, 2026-06-13). |
| [ADR-009](../../../company/Memory/decisions/ADR-009-espansione-ecosistemi.md) | Espansione ecosistemi | Regole per l'espansione controllata dei 10 ecosistemi via i dossier v2. |
| [ADR-010](../../../company/Memory/decisions/ADR-010-fusione-ruflo-apex7.md) | Fusione Ruflo + APEX-7-CORE | Cura la frammentazione di 6 implementazioni APEX-7 divergenti fondendole su un motore condiviso multi-tenant. Vedi [[Tool_APEX7_Core_Motore_Condiviso]]. |
| [ADR-011](../../../company/Memory/decisions/ADR-011-quinta-implementazione-apex7.md) | Quinta implementazione APEX-7 | Censimento ADR-010 era incompleto (6 linee, non 4); `empire/intelligence/apex7/` entra come deprecata-non-cancellata. Vedi [[Tool_APEX7_Core_Motore_Condiviso]]. |
| [ADR-012](../../../company/Memory/decisions/ADR-012-ponte-memory-wiki.md) | Ponte memory-wiki | Costruito l'agente `memory-wiki-bridge` + comando `/sync-wiki-totale`: il lavoro interno in `company/Memory/` non aveva nessun percorso automatico verso questa wiki. Vedi [[Tool_Memory_Wiki_Bridge]]. |

## Come leggerle
`company/Memory/decisions/ADR-NNN-*.md` è la fonte di verità completa per ciascuna; questa
pagina è solo l'indice navigabile lato wiki. Se una decisione viene superata da una nuova
ADR, si registra una nuova voce — le ADR non si cancellano né si riscrivono (stesso
principio di ADR-003 applicato alle decisioni stesse).

## Connessioni
- [[projects/Piano_Maestro_EMPIRE_OS]] — il piano che ADR-001/006/007 governano
- [[Tool_APEX7_Core_Motore_Condiviso]] — ADR-010/011 in dettaglio
- [[Tool_Memory_Wiki_Bridge]] — ADR-012 in dettaglio

## Status
- First added: 2026-08-24 (backfill wiki storico 06→08/2026, permesso esplicito Max)
- Confidence: Alta — elenco verificato via `ls company/Memory/decisions/`
