---
Type: SKILLS
Status: Active
Tags: #skills #marketing-interno #proof #case-study #upsell #A6
Created: 2026-06-23
Last updated: 2026-06-23
---

# Skill — A6 Marketing Interno & Proof

> Mappa delle skill del reparto: skill esistenti mappate (ADR-003 wrap-not-rewrite) +
> skill ausiliarie. Il reparto privilegia il riuso (wrap) sulla riscrittura.

---

## Skill esistenti mappate ad A6 (ADR-003 wrap-not-rewrite)

| Skill | Stato | Ruolo in A6 | Owner agente |
|---|---|---|---|
| `case-study-forge` | Esistente, mappata | Motore di scrittura case study APSOC da delivery chiusa con metriche verificate | AG-A6-CASE |
| `upsell-mapper` | Esistente, mappata | Matrice cliente→offerta successiva (singolo → Engine Room → referral) | AG-A6-UPSELL |
| `market-report` | Esistente, mappata | Sintesi proof/metriche per report munizioni verso A2 e A3 | AG-A6-COORD + AG-A6-INBOUND |
| `social` | Esistente, mappata | Brief social proof per 03-CONTENT-FACTORY (post/carosello testimonianza) | AG-A6-CASE |
| `ad-creative` | Esistente, mappata (dove applicabile) | Variazioni claim per asset di proof riusati in vetrina/outreach | AG-A6-CASE |

**Principio ADR-003:** nessuna skill nuova viene forgiata se una esistente copre la funzione.
A6 wrappa `case-study-forge` e `upsell-mapper` (named nel dossier) e usa `market-report`,
`social`, `ad-creative` come ausiliarie. Nessuna riscrittura.

---

## Come si usano nel reparto

### `case-study-forge` (P0 — cuore del reparto)

**Quando invocarla:** quando AG-A6-PROOF ha consegnato un proof verificato e AG-A6-CASE deve
scrivere il case study.
**Input:** `{cliente, proof_status, metriche[] (con fonte), testimonianza, servizio_erogato, consenso}`
**Output:** case study APSOC completo (A→P→S→O→C→CTA) con ogni numero che cita la fonte.
**Vincolo:** solo metriche verificate; se `proof_status: qualitativo` → caso descrittivo senza numeri.

### `upsell-mapper`

**Quando invocarla:** quando A7-Account Mgmt segnala "90gg finiti + NPS ≥8".
**Input:** `{cliente, prodotto_attuale, nps, storico}`
**Output:** next mappato (Engine Room / referral_ask / nessuno) + razionale basato sul risultato reale.
**Vincolo:** mai durante supporto attivo (R3); segnala, non decide (proposta via A3/Max).

### `market-report` (ausiliaria)

**Quando invocarla:** per produrre la sintesi delle munizioni (quali case study/metriche
passare ad A2 per outreach e ad A3 per preventivi).
**Input:** `{case_study_pubblicati[], metriche_top, periodo}`
**Output:** report munizioni strutturato.

### `social` + `ad-creative` (ausiliarie, dove applicabili)

**Quando:** quando AG-A6-CASE prepara il brief per 03-CONTENT-FACTORY (caroselli/reel di
social proof) o quando un claim verificato va riusato come variazione creativa.
**Vincolo:** ogni variazione mantiene la fonte del claim; nessun claim amplificato oltre il dato reale.

---

## Regola anti-contraddizione (ADR-003)

Prima di proporre QUALSIASI skill nuova per A6:
1. Verificare che `case-study-forge`, `upsell-mapper`, `market-report`, `social`, `ad-creative`
   non coprano già la funzione.
2. Se sovrapposizione: wrappa l'esistente, non riscrivere (ADR-003 wrap-not-rewrite).
3. Una nuova skill richiede ADR dedicato + `skill-contradiction-analyzer` contro le mappate.

---

## Connessioni

- [[ag-a6-case]] · `agenti/ag-a6-case.md` — owner di `case-study-forge` e `social`
- [[ag-a6-upsell]] · `agenti/ag-a6-upsell.md` — owner di `upsell-mapper`
- [[WF-CASE-STUDY]] · `workflow/WF-CASE-STUDY.md` — workflow che usa `case-study-forge`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A6` — skill named nel dossier
